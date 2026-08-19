from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
import http.client
import socket
import ssl
from types import MappingProxyType
from typing import Any
from typing import Protocol
from urllib.parse import urlsplit

from .. import (
    DeliveryRequirements,
    ITransportClient,
    TransportCapabilities,
    TransportDelivery,
    TransportDeliveryState,
    TransportDiagnostic,
    TransportFrame,
    TransportReply,
    bind_capabilities,
)


@dataclass(frozen=True, slots=True)
class HttpRequest:
    base_url: str
    method: str
    route_path: str
    headers: tuple[tuple[str, str], ...]
    body: bytes


@dataclass(frozen=True, slots=True)
class HttpResponse:
    status_code: int
    headers: tuple[tuple[str, str], ...]
    body: bytes


class IHttpExchange(Protocol):
    def exchange(self, request: HttpRequest) -> HttpResponse: ...

    def close(self) -> None: ...


def _default_capabilities() -> TransportCapabilities:
    return TransportCapabilities(
        ordered=True,
        reliable=True,
        preserves_message_boundaries=True,
        max_frame_bytes=16 * 1024 * 1024,
        request_reply=True,
        duplicate_suppression=False,
    )


def _validate_http_endpoint(endpoint: str) -> str:
    normalized = endpoint.strip()
    try:
        parsed = urlsplit(normalized)
        parsed.port
    except ValueError as exc:
        raise ValueError("http_endpoint_invalid") from exc
    if (
        parsed.scheme not in {"http", "https"}
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
    ):
        raise ValueError("http_endpoint_invalid")
    return normalized.rstrip("/")


def _find_header(
    headers: tuple[tuple[str, str], ...],
    name: str,
) -> str | None:
    expected = name.casefold()
    for header_name, value in headers:
        if header_name.casefold() == expected:
            normalized = value.strip()
            return normalized or None
    return None


@dataclass(frozen=True, slots=True)
class HttpAdapterConfig:
    base_url: str
    method: str
    route_path: str
    probe_path: str
    connect_timeout_seconds: float
    io_timeout_seconds: float
    auth_header: str | None = None
    auth_token: str | None = None
    tls_verify: bool = True
    capabilities: TransportCapabilities = field(
        default_factory=_default_capabilities
    )

    def __post_init__(self) -> None:
        if not isinstance(self.base_url, str) or not self.base_url.strip():
            raise ValueError("http_base_url_missing")
        object.__setattr__(
            self,
            "base_url",
            _validate_http_endpoint(self.base_url),
        )
        method = self.method.strip().upper()
        if not method:
            raise ValueError("http_method_missing")
        object.__setattr__(self, "method", method)
        route_path = self.route_path.strip()
        if not route_path.startswith("/"):
            raise ValueError("http_route_path_invalid")
        object.__setattr__(self, "route_path", route_path)
        probe_path = self.probe_path.strip()
        if not probe_path.startswith("/"):
            raise ValueError("http_probe_path_invalid")
        object.__setattr__(self, "probe_path", probe_path)
        if (self.auth_header is None) != (self.auth_token is None):
            raise ValueError("http_auth_incomplete")
        if self.auth_header is not None:
            auth_header = self.auth_header.strip()
            if not auth_header:
                raise ValueError("http_auth_header_missing")
            if not self.auth_token:
                raise ValueError("http_auth_token_missing")
            object.__setattr__(self, "auth_header", auth_header)
        for field_name, value in (
            (
                "connect_timeout_seconds",
                self.connect_timeout_seconds,
            ),
            (
                "io_timeout_seconds",
                self.io_timeout_seconds,
            ),
        ):
            if (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or value <= 0
            ):
                raise ValueError(f"http_{field_name}_invalid")
        if type(self.tls_verify) is not bool:
            raise TypeError("http_tls_verify_invalid")


class StdlibHttpExchange:
    def __init__(
        self,
        connect_timeout_seconds: float,
        io_timeout_seconds: float,
        *,
        tls_verify: bool = True,
    ) -> None:
        if connect_timeout_seconds <= 0:
            raise ValueError("http_connect_timeout_invalid")
        if io_timeout_seconds <= 0:
            raise ValueError("http_io_timeout_invalid")
        self._connect_timeout_seconds = float(
            connect_timeout_seconds
        )
        self._io_timeout_seconds = float(io_timeout_seconds)
        self._ssl_context = (
            ssl.create_default_context()
            if tls_verify
            else ssl._create_unverified_context()
        )
        self._closed = False

    def exchange(self, request: HttpRequest) -> HttpResponse:
        if self._closed:
            raise RuntimeError("http_exchange_closed")
        parsed = urlsplit(
            request.base_url.rstrip("/") + request.route_path
        )
        if parsed.scheme not in {"http", "https"} or not parsed.hostname:
            raise ValueError("http_request_url_invalid")
        if parsed.scheme == "https":
            connection: http.client.HTTPConnection = (
                http.client.HTTPSConnection(
                    parsed.hostname,
                    parsed.port,
                    timeout=self._connect_timeout_seconds,
                    context=self._ssl_context,
                )
            )
        else:
            connection = http.client.HTTPConnection(
                parsed.hostname,
                parsed.port,
                timeout=self._connect_timeout_seconds,
            )
        target = parsed.path or "/"
        if parsed.query:
            target += f"?{parsed.query}"
        try:
            connection.connect()
            if connection.sock is not None:
                connection.sock.settimeout(self._io_timeout_seconds)
            connection.request(
                request.method,
                target,
                body=request.body if request.body else None,
                headers=dict(request.headers),
            )
            response = connection.getresponse()
            return HttpResponse(
                status_code=int(response.status),
                headers=tuple(response.getheaders()),
                body=response.read(),
            )
        finally:
            connection.close()

    def close(self) -> None:
        self._closed = True


class HttpTransportAdapter(ITransportClient):
    def __init__(
        self,
        *,
        config: HttpAdapterConfig,
        exchange: IHttpExchange | None = None,
    ) -> None:
        self._config = config
        self._exchange = exchange or StdlibHttpExchange(
            config.connect_timeout_seconds,
            config.io_timeout_seconds,
            tls_verify=config.tls_verify,
        )
        self._closed = False

    def send(
        self,
        frame: TransportFrame,
        requirements: DeliveryRequirements,
    ) -> TransportDelivery:
        bind_capabilities(self._config.capabilities, requirements)
        limit = min(
            self._config.capabilities.max_frame_bytes,
            requirements.max_frame_bytes,
        )
        if len(frame.payload) > limit:
            return self._failure(
                frame,
                TransportDeliveryState.UNSUPPORTED,
                "frame_too_large",
                "frame exceeds bound transport capacity",
            )
        if self._closed:
            return self._failure(
                frame,
                TransportDeliveryState.DISCONNECTED,
                "transport_closed",
                "transport exchange is closed",
            )

        request = HttpRequest(
            base_url=self._config.base_url,
            method=self._config.method,
            route_path=self._config.route_path,
            headers=self._headers(frame.correlation_id),
            body=frame.payload,
        )
        try:
            response = self._exchange.exchange(request)
        except (TimeoutError, socket.timeout) as exc:
            return self._failure(
                frame,
                TransportDeliveryState.TIMED_OUT,
                "transport_timed_out",
                str(exc) or "transport exchange timed out",
            )
        except OSError as exc:
            return self._failure(
                frame,
                TransportDeliveryState.DISCONNECTED,
                "transport_disconnected",
                str(exc) or "transport exchange disconnected",
            )
        except Exception as exc:
            return self._failure(
                frame,
                TransportDeliveryState.FAILED,
                "transport_failed",
                str(exc) or "transport exchange failed",
            )

        reply_frame = TransportFrame(
            channel=frame.channel,
            payload=response.body,
            correlation_id=frame.correlation_id,
            peer=frame.peer,
        )
        reply = TransportReply(frame=reply_frame)
        if 200 <= response.status_code < 300:
            return TransportDelivery(
                correlation_id=frame.correlation_id,
                state=TransportDeliveryState.DELIVERED,
                reply=reply,
                diagnostic=None,
                attempts=1,
            )
        diagnostic_code = _find_header(
            response.headers,
            "X-Transport-Diagnostic",
        )
        return TransportDelivery(
            correlation_id=frame.correlation_id,
            state=TransportDeliveryState.FAILED,
            reply=reply,
            diagnostic=TransportDiagnostic(
                code=diagnostic_code or "remote_rejected",
                message="remote transport endpoint rejected the frame",
            ),
            attempts=1,
        )

    def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        self._exchange.close()

    def probe(self) -> bool:
        if self._closed:
            return False
        response = self._exchange.exchange(
            HttpRequest(
                base_url=self._config.base_url,
                method="GET",
                route_path=self._config.probe_path,
                headers=self._headers(None),
                body=b"",
            )
        )
        return 200 <= response.status_code < 300

    def _headers(
        self,
        correlation_id: str | None,
    ) -> tuple[tuple[str, str], ...]:
        headers: list[tuple[str, str]] = []
        if (
            self._config.auth_header is not None
            and self._config.auth_token is not None
        ):
            headers.append(
                (
                    self._config.auth_header,
                    self._config.auth_token,
                )
            )
        headers.append(("Content-Type", "application/octet-stream"))
        if correlation_id is not None:
            headers.append(
                ("X-Transport-Correlation", correlation_id)
            )
        return tuple(headers)

    @staticmethod
    def _failure(
        frame: TransportFrame,
        state: TransportDeliveryState,
        code: str,
        message: str,
    ) -> TransportDelivery:
        return TransportDelivery(
            correlation_id=frame.correlation_id,
            state=state,
            reply=None,
            diagnostic=TransportDiagnostic(code=code, message=message),
            attempts=1,
        )


def load_http_transport_options(
    raw: Any,
    *,
    endpoint: str,
) -> Mapping[str, Any]:
    _validate_http_endpoint(endpoint)
    if not isinstance(raw, Mapping):
        raise TypeError(
            "transport_options.http must be a table"
        )
    expected = {
        "auth_header",
        "probe_path",
        "route_path",
        "tls_verify",
    }
    unknown = sorted(set(raw) - expected)
    if unknown:
        raise ValueError(
            "transport_options.http contains unknown fields: "
            + ",".join(unknown)
        )
    missing = sorted(expected - set(raw))
    if missing:
        raise ValueError(
            "transport_options.http is missing fields: "
            + ",".join(missing)
        )
    tls_verify = raw.get("tls_verify")
    if type(tls_verify) is not bool:
        raise TypeError(
            "transport_options.http.tls_verify must be a boolean"
        )
    normalized: dict[str, Any] = {
        "tls_verify": tls_verify,
    }
    for name in ("auth_header", "probe_path", "route_path"):
        value = raw.get(name)
        if not isinstance(value, str) or not value.strip():
            raise TypeError(
                f"transport_options.http.{name} "
                "must be a non-empty string"
            )
        normalized[name] = value.strip()
    for name in ("probe_path", "route_path"):
        if not normalized[name].startswith("/"):
            raise ValueError(
                f"transport_options.http.{name} must start with /"
            )
    return MappingProxyType(normalized)


def build_http_transport(snapshot: Any) -> HttpTransportAdapter:
    secret = snapshot.authentication.get_secret_value()
    auth_header = (
        "X-UeAgentInterface-Token"
        if secret is not None
        else None
    )
    http_options = snapshot.transport_options["http"]
    return HttpTransportAdapter(
        config=HttpAdapterConfig(
            base_url=snapshot.endpoint,
            method="POST",
            route_path=http_options["route_path"],
            probe_path=http_options["probe_path"],
            connect_timeout_seconds=(
                snapshot.connect_timeout_seconds
            ),
            io_timeout_seconds=snapshot.io_timeout_seconds,
            auth_header=(
                http_options["auth_header"]
                if auth_header is not None
                else None
            ),
            auth_token=secret,
            tls_verify=http_options["tls_verify"],
        )
    )


__all__ = [
    "HttpAdapterConfig",
    "HttpRequest",
    "HttpResponse",
    "HttpTransportAdapter",
    "IHttpExchange",
    "StdlibHttpExchange",
    "build_http_transport",
    "load_http_transport_options",
]
