from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Protocol


def _required_text(field_name: str, value: str) -> str:
    normalized = str(value).strip()
    if not normalized:
        raise ValueError(f"{field_name}_missing")
    return normalized


@dataclass(frozen=True, slots=True)
class TransportPrincipal:
    subject: str
    authentication_method: str

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "subject",
            _required_text("transport_principal_subject", self.subject),
        )
        object.__setattr__(
            self,
            "authentication_method",
            _required_text(
                "transport_authentication_method",
                self.authentication_method,
            ),
        )


@dataclass(frozen=True, slots=True)
class TransportPeer:
    peer_id: str
    principal: TransportPrincipal

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "peer_id",
            _required_text("transport_peer_id", self.peer_id),
        )
        if not isinstance(self.principal, TransportPrincipal):
            raise TypeError("transport_peer_principal_invalid")


@dataclass(frozen=True, slots=True)
class TransportFrame:
    channel: str
    payload: bytes
    correlation_id: str
    peer: TransportPeer

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "channel",
            _required_text("transport_channel", self.channel),
        )
        object.__setattr__(
            self,
            "correlation_id",
            _required_text(
                "transport_correlation_id",
                self.correlation_id,
            ),
        )
        if type(self.payload) is not bytes:
            raise TypeError("transport_frame_payload_must_be_bytes")
        if not isinstance(self.peer, TransportPeer):
            raise TypeError("transport_frame_peer_invalid")


@dataclass(frozen=True, slots=True)
class TransportCapabilities:
    ordered: bool
    reliable: bool
    preserves_message_boundaries: bool
    max_frame_bytes: int
    request_reply: bool
    duplicate_suppression: bool

    def __post_init__(self) -> None:
        if (
            isinstance(self.max_frame_bytes, bool)
            or self.max_frame_bytes <= 0
        ):
            raise ValueError("transport_max_frame_bytes_invalid")


@dataclass(frozen=True, slots=True)
class DeliveryRequirements:
    require_ordered: bool
    require_reliable: bool
    require_message_boundaries: bool
    max_frame_bytes: int
    require_request_reply: bool
    require_duplicate_suppression: bool

    def __post_init__(self) -> None:
        if (
            isinstance(self.max_frame_bytes, bool)
            or self.max_frame_bytes <= 0
        ):
            raise ValueError("delivery_max_frame_bytes_invalid")


@dataclass(frozen=True, slots=True)
class CapabilityBinding:
    capabilities: TransportCapabilities
    requirements: DeliveryRequirements


class TransportBindingError(ValueError):
    def __init__(self, missing_capabilities: tuple[str, ...]) -> None:
        self.code = "transport_capability_unsupported"
        self.missing_capabilities = tuple(missing_capabilities)
        super().__init__(
            f"{self.code}:{','.join(self.missing_capabilities)}"
        )


def bind_capabilities(
    capabilities: TransportCapabilities,
    requirements: DeliveryRequirements,
) -> CapabilityBinding:
    missing: list[str] = []
    if requirements.require_ordered and not capabilities.ordered:
        missing.append("ordered")
    if requirements.require_reliable and not capabilities.reliable:
        missing.append("reliable")
    if (
        requirements.require_message_boundaries
        and not capabilities.preserves_message_boundaries
    ):
        missing.append("message_boundaries")
    if requirements.max_frame_bytes > capabilities.max_frame_bytes:
        missing.append("max_frame_bytes")
    if requirements.require_request_reply and not capabilities.request_reply:
        missing.append("request_reply")
    if (
        requirements.require_duplicate_suppression
        and not capabilities.duplicate_suppression
    ):
        missing.append("duplicate_suppression")
    if missing:
        raise TransportBindingError(tuple(missing))
    return CapabilityBinding(
        capabilities=capabilities,
        requirements=requirements,
    )


class TransportDeliveryState(str, Enum):
    DELIVERED = "delivered"
    BACKPRESSURED = "backpressured"
    TIMED_OUT = "timed_out"
    DISCONNECTED = "disconnected"
    FAILED = "failed"
    UNSUPPORTED = "unsupported"


@dataclass(frozen=True, slots=True)
class TransportDiagnostic:
    code: str
    message: str

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "code",
            _required_text("transport_diagnostic_code", self.code),
        )


@dataclass(frozen=True, slots=True)
class TransportReply:
    frame: TransportFrame


@dataclass(frozen=True, slots=True)
class TransportDelivery:
    correlation_id: str
    state: TransportDeliveryState
    reply: TransportReply | None
    diagnostic: TransportDiagnostic | None
    attempts: int

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "correlation_id",
            _required_text(
                "transport_delivery_correlation_id",
                self.correlation_id,
            ),
        )
        if self.attempts != 1:
            raise ValueError("transport_delivery_attempts_must_equal_one")


class ITransportClient(Protocol):
    def send(
        self,
        frame: TransportFrame,
        requirements: DeliveryRequirements,
    ) -> TransportDelivery: ...

    def close(self) -> None: ...


__all__ = [
    "CapabilityBinding",
    "DeliveryRequirements",
    "ITransportClient",
    "TransportBindingError",
    "TransportCapabilities",
    "TransportDelivery",
    "TransportDeliveryState",
    "TransportDiagnostic",
    "TransportFrame",
    "TransportPeer",
    "TransportPrincipal",
    "TransportReply",
    "bind_capabilities",
]
