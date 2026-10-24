"""Transport-neutral public command wire boundary."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from dataclasses import dataclass, field
import json
import math
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
        raise error_type.at_source(
            code=f"{field_name}_invalid",
            message=f"{field_name} must be a non-empty string",
            facts={"stage": "command_encode", "json_pointer": f"/{field_name}",
                   "expected_value": "non-empty string", "actual_type": type(value).__name__},
        )
    return value.strip()


@dataclass(frozen=True, slots=True)
class CommandRequest:
    command_id: str
    command_binding_hash: str = field(repr=False)
    params: Mapping[str, Any] = field(repr=False)
    correlation_id: str = field(repr=False)
    request_id: str = field(repr=False)

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
            raise SerializationError.at_source(
                code="command_params_invalid",
                message="command params must be an object",
                facts={"stage": "command_encode", "json_pointer": "/params", "expected_value": "object", "actual_type": type(self.params).__name__},
            )
        snapshot = deepcopy(dict(self.params))
        for index, key in enumerate(snapshot):
            if not isinstance(key, str):
                raise SerializationError.at_source(
                    code="command_params_invalid",
                    message="Command parameter names must be strings.",
                    facts={"stage": "command_encode", "json_pointer": "/params", "key_index": index,
                           "expected_value": "string", "actual_type": type(key).__name__},
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
    raise ProtocolError.at_source(
        code="command_result_json_invalid", message="Command result contains a non-standard JSON numeric constant.",
        facts={"stage": "command_decode", "actual_value": value, "expected_value": "finite JSON number"},
    )


def _field_error(code: str, message: str, pointer: str, value: Any, expected: Any) -> ProtocolError:
    facts = {"stage": "command_decode", "json_pointer": pointer,
             "actual_type": type(value).__name__, "expected_value": expected}
    if value is None or type(value) in (str, bool, int, float):
        facts["actual_value"] = str(value) if type(value) is float and not math.isfinite(value) else value
    return ProtocolError.at_source(code=code, message=message, facts=facts)


class UaiCommandCodec:
    def encode_request(self, request: CommandRequest) -> bytes:
        if not isinstance(request, CommandRequest):
            raise SerializationError.at_source(
                code="command_request_invalid",
                message="command request model is invalid",
                facts={"stage": "command_encode", "expected_value": "CommandRequest", "actual_type": type(request).__name__},
            )
        try:
            text = json.dumps(
                request.to_model(),
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
                allow_nan=False,
            )
            return text.encode("utf-8")
        except UnicodeEncodeError as exc:
            raise SerializationError.at_source(
                code="command_request_encode_failed", message="Command request contains text that cannot be encoded as UTF-8.",
                facts={"stage": "command_encode", "character": exc.start, "expected_value": "UTF-8 text", "reason": exc.reason},
            ) from None
        except (TypeError, ValueError, OverflowError) as exc:
            raise SerializationError.at_source(
                code="command_request_encode_failed",
                message="command request cannot be encoded",
                facts={"stage": "command_encode", "exception_type": type(exc).__name__},
            ) from None

    def decode_result(
        self,
        payload: bytes,
        *,
        expected_request: CommandRequest,
    ) -> Result:
        if type(payload) is not bytes:
            raise _field_error("command_result_payload_invalid", "Command result payload must be bytes.", "", payload, "bytes")
        try:
            root = json.loads(
                payload.decode("utf-8"),
                parse_constant=_reject_json_constant,
            )
        except UnicodeDecodeError as exc:
            raise ProtocolError.at_source(
                code="command_result_json_invalid", message="Command result is not valid UTF-8.",
                facts={"stage": "command_decode", "byte_offset": exc.start, "expected_value": "utf-8", "reason": exc.reason},
            ) from None
        except json.JSONDecodeError as exc:
            raise ProtocolError.at_source(
                code="command_result_json_invalid", message=exc.msg,
                facts={"stage": "command_decode", "line": exc.lineno, "column": exc.colno, "character": exc.pos},
            ) from None
        except ValueError as exc:
            raise ProtocolError.at_source(
                code="command_result_json_invalid", message="Command result cannot be decoded as JSON.",
                facts={"stage": "command_decode", "exception_type": type(exc).__name__},
            ) from None
        if not isinstance(root, dict):
            raise _field_error("command_result_envelope_invalid", "Command result envelope must be an object.", "", root, "object")
        if root.get("schema") != WIRE_SCHEMA:
            raise _field_error("command_result_envelope_invalid", "Command result schema is invalid.", "/schema", root.get("schema"), WIRE_SCHEMA)
        if type(root.get("version")) is not int or root.get("version") != WIRE_VERSION:
            raise _field_error("command_result_envelope_invalid", "Command result version is invalid.", "/version", root.get("version"), WIRE_VERSION)
        message_kind = root.get("message_kind")
        expected_fields = (
            _PROTOCOL_ERROR_FIELDS
            if message_kind == "protocol_error"
            else _RESULT_FIELDS
        )
        if message_kind == "command_result" and "diagnostics" in root:
            expected_fields = expected_fields | {"diagnostics"}
        if set(root) != expected_fields:
            raise ProtocolError.at_source(
                code="command_result_envelope_invalid",
                message="command result fields do not match the protocol envelope",
                facts={"stage": "command_decode", "json_pointer": "", "missing_fields": sorted(expected_fields - set(root)),
                            "unexpected_fields": sorted(set(root) - expected_fields)},
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
                raise ProtocolError.at_source(
                    code="command_result_identity_mismatch",
                    message=(
                        "command result identity does not match "
                        f"the request: {field_name}"
                    ),
                    facts={"stage": "command_decode", "json_pointer": f"/{field_name}"},
                )
        if message_kind == "protocol_error":
            error = root.get("error")
            if not isinstance(error, dict):
                raise _field_error("command_protocol_error_invalid", "Protocol error must contain an error object.", "/error", error, "object")
            code = error.get("code")
            diagnostic = error.get("diagnostic")
            if not isinstance(diagnostic, dict):
                raise _field_error("command_protocol_error_invalid", "Protocol error must contain a structured diagnostic.", "/error/diagnostic", diagnostic, "object")
            message = diagnostic.get("message")
            if not isinstance(code, str) or not code.strip():
                raise _field_error("command_protocol_error_invalid", "Protocol error requires a non-empty code.", "/error/code", code, "non-empty string")
            if not isinstance(message, str) or not message.strip():
                raise _field_error("command_protocol_error_invalid", "Protocol error requires a non-empty diagnostic message.", "/error/diagnostic/message", message, "non-empty string")
            protocol_error = ProtocolError(
                code=code,
                message=message,
                diagnostic=diagnostic,
            )
            protocol_error.raw_response = MappingProxyType(
                deepcopy(root)
            )
            raise protocol_error
        if message_kind != "command_result":
            raise _field_error("command_result_envelope_invalid", "Command result message kind is invalid.", "/message_kind", message_kind, "command_result or protocol_error")
        if type(root.get("ok")) is not bool:
            raise _field_error("command_result_ok_invalid", "Command result ok must be a boolean.", "/ok", root.get("ok"), "boolean")
        if not isinstance(root.get("payload"), dict):
            raise _field_error("command_result_payload_invalid", "Command result payload must be an object.", "/payload", root.get("payload"), "object")
        error = root.get("error")
        if root["ok"] and error is not None:
            raise _field_error("command_result_error_invalid", "Successful command result error must be null.", "/error", error, "null")
        if not root["ok"] and not isinstance(error, dict):
            raise _field_error("command_result_error_invalid", "Failed command result must contain an error object.", "/error", error, "object")
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
            raise TransportError.at_source(
                code="transport_attempt_count_invalid",
                message="command transport attempted delivery more than once",
                facts={"stage": "command_delivery", "json_pointer": "/attempts", "actual_value": delivery.attempts, "expected_value": 1},
            )
        if delivery.reply is not None:
            reply = delivery.reply.frame
            if (
                reply.channel != COMMAND_CHANNEL
                or reply.correlation_id != request.correlation_id
            ):
                field = "channel" if reply.channel != COMMAND_CHANNEL else "correlation_id"
                raise ProtocolError.at_source(
                    code="command_reply_frame_mismatch",
                    message=(
                        f"Command reply {field} does not match the request."
                    ),
                    facts={"stage": "command_delivery", "json_pointer": f"/{field}"},
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
        if diagnostic is None or delivery.state == TransportDeliveryState.DELIVERED:
            facts = {"stage": "transport"}
            if diagnostic is not None:
                facts["cause"] = diagnostic.as_dict()
            raise TransportError.at_source(
                code="transport_reply_missing", message="transport returned no command reply", facts=facts,
            )
        raise TransportError(
            code=diagnostic.code, message=diagnostic.message, diagnostic=diagnostic.as_dict(),
        )


__all__ = [
    "COMMAND_CHANNEL",
    "CommandRequest",
    "UaiCommandCodec",
    "UaiCommandProtocolClient",
    "WIRE_SCHEMA",
    "WIRE_VERSION",
]
