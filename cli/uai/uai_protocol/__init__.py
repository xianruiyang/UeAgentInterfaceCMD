"""Transport-neutral public command wire boundary."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from dataclasses import dataclass
import json
from types import MappingProxyType
from typing import Any

from ..errors import (
    ProtocolError,
    SerializationError,
    TransportError,
)
from ..network_transport import (
    DeliveryRequirements,
    ITransportClient,
    TransportDeliveryState,
    TransportFrame,
    TransportPeer,
    TransportPrincipal,
)
from ..result import Result


WIRE_SCHEMA = "uai.command.v1"
WIRE_VERSION = 1
COMMAND_CHANNEL = "uai.command"

_REQUEST_FIELDS = frozenset(
    {
        "schema",
        "version",
        "message_kind",
        "correlation_id",
        "request_id",
        "command_id",
        "command_binding_hash",
        "params",
    }
)
_RESULT_FIELDS = frozenset(
    {
        "schema",
        "version",
        "message_kind",
        "correlation_id",
        "request_id",
        "command_id",
        "command_binding_hash",
        "ok",
        "payload",
        "error",
    }
)
_PROTOCOL_ERROR_FIELDS = frozenset(
    {
        "schema",
        "version",
        "message_kind",
        "correlation_id",
        "request_id",
        "command_id",
        "command_binding_hash",
        "error",
    }
)


def _required_text(
    value: Any,
    *,
    field_name: str,
    error_type=SerializationError,
) -> str:
    if not isinstance(value, str) or not value.strip():
        raise error_type(
            code=f"{field_name}_invalid",
            message=f"{field_name} must be a non-empty string",
        )
    return value.strip()


@dataclass(frozen=True, slots=True)
class CommandRequest:
    command_id: str
    command_binding_hash: str
    params: Mapping[str, Any]
    correlation_id: str
    request_id: str

    def __post_init__(self) -> None:
        for field_name in (
            "command_id",
            "command_binding_hash",
            "correlation_id",
            "request_id",
        ):
            object.__setattr__(
                self,
                field_name,
                _required_text(
                    getattr(self, field_name),
                    field_name=field_name,
                ),
            )
        if not isinstance(self.params, Mapping):
            raise SerializationError(
                code="command_params_invalid",
                message="command params must be an object",
            )
        snapshot = deepcopy(dict(self.params))
        if any(not isinstance(key, str) for key in snapshot):
            raise SerializationError(
                code="command_params_invalid",
                message="command parameter names must be strings",
            )
        object.__setattr__(
            self,
            "params",
            MappingProxyType(snapshot),
        )

    def to_model(self) -> dict[str, Any]:
        return {
            "schema": WIRE_SCHEMA,
            "version": WIRE_VERSION,
            "message_kind": "command_request",
            "correlation_id": self.correlation_id,
            "request_id": self.request_id,
            "command_id": self.command_id,
            "command_binding_hash": self.command_binding_hash,
            "params": deepcopy(dict(self.params)),
        }


def _reject_json_constant(value: str) -> None:
    raise ValueError(f"invalid JSON constant: {value}")


class UaiCommandCodec:
    def encode_request(self, request: CommandRequest) -> bytes:
        if not isinstance(request, CommandRequest):
            raise SerializationError(
                code="command_request_invalid",
                message="command request model is invalid",
            )
        try:
            text = json.dumps(
                request.to_model(),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            )
        except (TypeError, ValueError, OverflowError) as exc:
            raise SerializationError(
                code="command_request_encode_failed",
                message=str(exc) or "command request cannot be encoded",
            ) from exc
        return text.encode("utf-8")

    def decode_result(
        self,
        payload: bytes,
        *,
        expected_request: CommandRequest,
    ) -> Result:
        if type(payload) is not bytes:
            raise ProtocolError(
                code="command_result_payload_invalid",
                message="command result payload must be bytes",
            )
        try:
            root = json.loads(
                payload.decode("utf-8"),
                parse_constant=_reject_json_constant,
            )
        except (UnicodeError, json.JSONDecodeError, ValueError) as exc:
            raise ProtocolError(
                code="command_result_json_invalid",
                message="command result is not valid UTF-8 JSON",
            ) from exc
        if not isinstance(root, dict):
            raise ProtocolError(
                code="command_result_envelope_invalid",
                message="command result envelope must be an object",
            )
        if (
            root.get("schema") != WIRE_SCHEMA
            or type(root.get("version")) is not int
            or root.get("version") != WIRE_VERSION
        ):
            raise ProtocolError(
                code="command_result_envelope_invalid",
                message="command result schema or version is invalid",
            )
        message_kind = root.get("message_kind")
        expected_fields = (
            _PROTOCOL_ERROR_FIELDS
            if message_kind == "protocol_error"
            else _RESULT_FIELDS
        )
        if set(root) != expected_fields:
            raise ProtocolError(
                code="command_result_envelope_invalid",
                message="command result fields are invalid",
            )
        for field_name in (
            "correlation_id",
            "request_id",
            "command_id",
            "command_binding_hash",
        ):
            if root.get(field_name) != getattr(
                expected_request,
                field_name,
            ):
                raise ProtocolError(
                    code="command_result_identity_mismatch",
                    message=(
                        "command result identity does not match "
                        f"the request: {field_name}"
                    ),
                )
        if message_kind == "protocol_error":
            error = root.get("error")
            if not isinstance(error, dict):
                raise ProtocolError(
                    code="command_protocol_error_invalid",
                    message="protocol error must contain an error object",
                )
            code = error.get("code")
            message = error.get("message")
            if not isinstance(code, str) or not code.strip():
                code = "command_protocol_error"
            if not isinstance(message, str) or not message.strip():
                message = "server rejected the command envelope"
            protocol_error = ProtocolError(
                code=code,
                message=message,
            )
            protocol_error.raw_response = MappingProxyType(
                deepcopy(root)
            )
            raise protocol_error
        if message_kind != "command_result":
            raise ProtocolError(
                code="command_result_envelope_invalid",
                message="command result message_kind is invalid",
            )
        if type(root.get("ok")) is not bool:
            raise ProtocolError(
                code="command_result_ok_invalid",
                message="command result ok must be a boolean",
            )
        if not isinstance(root.get("payload"), dict):
            raise ProtocolError(
                code="command_result_payload_invalid",
                message="command result payload must be an object",
            )
        error = root.get("error")
        if root["ok"] and error is not None:
            raise ProtocolError(
                code="command_result_error_invalid",
                message="successful command result error must be null",
            )
        if not root["ok"] and not isinstance(error, dict):
            raise ProtocolError(
                code="command_result_error_invalid",
                message=(
                    "failed command result must contain an error object"
                ),
            )
        return Result(root)


class UaiCommandProtocolClient:
    __slots__ = ("_codec", "_peer", "_transport")

    def __init__(
        self,
        *,
        transport: ITransportClient,
        codec: UaiCommandCodec | None = None,
    ) -> None:
        self._transport = transport
        self._codec = codec or UaiCommandCodec()
        self._peer = TransportPeer(
            peer_id="uai-server",
            principal=TransportPrincipal(
                subject="transport-managed",
                authentication_method="adapter",
            ),
        )

    def invoke(
        self,
        *,
        command_id: str,
        command_binding_hash: str,
        params: Mapping[str, Any],
        correlation_id: str,
        request_id: str,
    ) -> Result:
        request = CommandRequest(
            command_id=command_id,
            command_binding_hash=command_binding_hash,
            params=params,
            correlation_id=correlation_id,
            request_id=request_id,
        )
        payload = self._codec.encode_request(request)
        frame = TransportFrame(
            channel=COMMAND_CHANNEL,
            payload=payload,
            correlation_id=request.correlation_id,
            peer=self._peer,
        )
        delivery = self._transport.send(
            frame,
            DeliveryRequirements(
                require_ordered=True,
                require_reliable=True,
                require_message_boundaries=True,
                max_frame_bytes=max(1, len(payload)),
                require_request_reply=True,
                require_duplicate_suppression=False,
            ),
        )
        if delivery.attempts != 1:
            raise TransportError(
                code="transport_attempt_count_invalid",
                message="command transport attempted delivery more than once",
            )
        if delivery.reply is not None:
            reply = delivery.reply.frame
            if (
                reply.channel != COMMAND_CHANNEL
                or reply.correlation_id != request.correlation_id
            ):
                raise ProtocolError(
                    code="command_reply_frame_mismatch",
                    message=(
                        "command reply channel or correlation is invalid"
                    ),
                )
            if delivery.state == TransportDeliveryState.DELIVERED:
                return self._codec.decode_result(
                    reply.payload,
                    expected_request=request,
                )
            try:
                self._codec.decode_result(
                    reply.payload,
                    expected_request=request,
                )
            except ProtocolError as exc:
                raw_response = getattr(exc, "raw_response", None)
                if (
                    isinstance(raw_response, Mapping)
                    and raw_response.get("message_kind")
                    == "protocol_error"
                ):
                    raise
        diagnostic = delivery.diagnostic
        code = (
            diagnostic.code
            if diagnostic is not None
            else "transport_reply_missing"
        )
        message = (
            diagnostic.message
            if diagnostic is not None
            else "transport returned no command reply"
        )
        if delivery.state == TransportDeliveryState.DELIVERED:
            code = "transport_reply_missing"
        raise TransportError(code=code, message=message)


__all__ = [
    "COMMAND_CHANNEL",
    "CommandRequest",
    "UaiCommandCodec",
    "UaiCommandProtocolClient",
    "WIRE_SCHEMA",
    "WIRE_VERSION",
]
