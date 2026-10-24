from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
from enum import Enum
from types import MappingProxyType
from typing import Protocol


class TransportOptionsError(ValueError):
    """Transport option validation with public, credential-free source facts."""

    def __init__(self, message: str, *, property_path: str, **facts: object) -> None:
        self.code = "connection_config_invalid"
        self.message = message
        self.diagnostic = {"code": self.code, "message": message, "stage": "connection_config",
                           "property_path": property_path, **facts}
        super().__init__(message)


def _required_text(field_name: str, value: str) -> str:
    normalized = str(value).strip()
    if not normalized:
        raise ValueError(f"{field_name}_missing")
    return normalized


@dataclass(frozen=True, slots=True)
class TransportPrincipal:
    subject: str = field(repr=False)
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
    peer_id: str = field(repr=False)
    principal: TransportPrincipal = field(repr=False)

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
    payload: bytes = field(repr=False)
    correlation_id: str = field(repr=False)
    peer: TransportPeer = field(repr=False)

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
    max_frame_bytes: int  # Legacy metadata, no frame-size admission limit.
    request_reply: bool
    duplicate_suppression: bool


@dataclass(frozen=True, slots=True)
class DeliveryRequirements:
    require_ordered: bool
    require_reliable: bool
    require_message_boundaries: bool
    max_frame_bytes: int  # Legacy metadata, no frame-size admission limit.
    require_request_reply: bool
    require_duplicate_suppression: bool


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
    message: str = field(repr=False)
    details: Mapping[str, object] = field(default_factory=dict, repr=False)

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "code",
            _required_text("transport_diagnostic_code", self.code),
        )
        object.__setattr__(self, "details", MappingProxyType(dict(self.details)))

    def as_dict(self) -> dict[str, object]:
        diagnostic: dict[str, object] = {
            "code": self.code, "message": self.message, "stage": "transport",
        }
        if self.details:
            diagnostic["details"] = dict(self.details)
        return diagnostic


class TransportExchangeError(Exception):
    """A transport failure captured at its source, before delivery projection."""

    def __init__(self, state: TransportDeliveryState, diagnostic: TransportDiagnostic):
        self.state = state
        self.diagnostic = diagnostic
        super().__init__(diagnostic.message)

    @classmethod
    def from_exception(
        cls, exc: Exception, *, phase: str,
        redacted_values: tuple[str, ...] = (),
    ) -> TransportExchangeError:
        if isinstance(exc, cls):
            return exc
        if isinstance(exc, TimeoutError):
            state, code, summary = TransportDeliveryState.TIMED_OUT, "transport_timed_out", "transport exchange timed out"
        elif isinstance(exc, OSError):
            state, code, summary = TransportDeliveryState.DISCONNECTED, "transport_disconnected", "transport exchange disconnected"
        else:
            state, code, summary = TransportDeliveryState.FAILED, "transport_failed", "transport exchange failed"
        reason = str(exc).strip()
        for value in sorted(set(redacted_values), key=len, reverse=True):
            if value:
                reason = reason.replace(value, "<redacted>")
        exception_type = type(exc).__name__
        details: dict[str, object] = {"phase": phase, "exception_type": exception_type}
        for name in ("errno", "winerror"):
            value = getattr(exc, name, None)
            if isinstance(value, int):
                details[name] = value
        message = f"{summary} during {phase}: {exception_type}"
        if reason:
            message += f": {reason}"
        return cls(state, TransportDiagnostic(code, message, details))


@dataclass(frozen=True, slots=True)
class TransportReply:
    frame: TransportFrame = field(repr=False)


@dataclass(frozen=True, slots=True)
class TransportDelivery:
    correlation_id: str = field(repr=False)
    state: TransportDeliveryState
    reply: TransportReply | None = field(repr=False)
    diagnostic: TransportDiagnostic | None = field(repr=False)
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
    "TransportExchangeError",
    "TransportFrame",
    "TransportPeer",
    "TransportPrincipal",
    "TransportReply",
    "bind_capabilities",
]
