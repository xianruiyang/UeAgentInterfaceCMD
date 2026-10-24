from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
import http.client
import math
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
    TransportExchangeError,
    TransportFrame,
    TransportOptionsError,
    TransportReply,
    bind_capabilities,
)


@dataclass(frozen=True, slots=True)
class HttpRequest:
    base_url: str = field(repr=False)
    method: str
    route_path: str = field(repr=False)
    headers: tuple[tuple[str, str], ...] = field(repr=False)
    body: bytes = field(repr=False)


@dataclass(frozen=True, slots=True)
class HttpResponse:
    status_code: int
    headers: tuple[tuple[str, str], ...] = field(repr=False)
    body: bytes = field(repr=False)


class IHttpExchange(Protocol):
    def exchange(self, request: HttpRequest) -> HttpResponse: ...

    def close(self) -> None: ...


def _exchange_error(exc: Exception, phase: str, request: HttpRequest) -> TransportExchangeError:
    # Never copy connection identity, credentials, or request content into a
    # public diagnostic, including when an exchange includes them in its text.
    parsed = urlsplit(request.base_url)
    redacted_values = (
        request.base_url, parsed.netloc, parsed.hostname or "",
        request.route_path if len(request.route_path) > 1 else "",
        request.body.decode("utf-8", errors="ignore"),
        *(value for _, value in request.headers),
    )
    return TransportExchangeError.from_exception(
        exc, phase=phase, redacted_values=redacted_values,
    )


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
    except ValueError:
        raise TransportOptionsError("The HTTP endpoint has an invalid host or port.",
                                    property_path="connection.endpoint",
                                    expected_value="HTTP(S) URL with a valid host and port") from None
    if (
        parsed.scheme not in {"http", "https"}
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
    ):
        raise TransportOptionsError("The HTTP endpoint requires an HTTP(S) scheme and host, without credentials, query or fragment.",
                                    property_path="connection.endpoint",
                                    expected_value="HTTP(S) URL without credentials, query or fragment")
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
    base_url: str = field(repr=False)
    method: str
    route_path: str
    probe_path: str
    connect_timeout_seconds: float
    io_timeout_seconds: float
    auth_header: str | None = field(default=None, repr=False)
    auth_token: str | None = field(default=None, repr=False)
    tls_verify: bool = True
    capabilities: TransportCapabilities = field(
        default_factory=_default_capabilities
    )

    def __post_init__(self) -> None:
        if not isinstance(self.base_url, str) or not self.base_url.strip():
            raise TransportOptionsError("The HTTP endpoint must be a non-empty URL string.",
                                        property_path="connection.endpoint", expected_value="non-empty HTTP(S) URL")
        object.__setattr__(
            self,
            "base_url",
            _validate_http_endpoint(self.base_url),
        )
        if not isinstance(self.method, str):
            raise TransportOptionsError("The HTTP method must be a string.", property_path="transport.method",
                                        expected_value="string", actual_value=type(self.method).__name__)
        method = self.method.strip().upper()
        if not method:
            raise TransportOptionsError("The HTTP method must not be empty.", property_path="transport.method",
                                        expected_value="non-empty string", actual_value=method)
        object.__setattr__(self, "method", method)
        if not isinstance(self.route_path, str):
            raise TransportOptionsError("The HTTP route path must be a string beginning with a slash.",
                                        property_path="transport_options.http.route_path", expected_value="absolute route path",
                                        actual_value=type(self.route_path).__name__)
        route_path = self.route_path.strip()
        if not route_path.startswith("/"):
            raise TransportOptionsError("The HTTP route path must begin with a slash.",
                                        property_path="transport_options.http.route_path", expected_value="absolute route path")
        object.__setattr__(self, "route_path", route_path)
        if not isinstance(self.probe_path, str):
            raise TransportOptionsError("The HTTP probe path must be a string beginning with a slash.",
                                        property_path="transport_options.http.probe_path", expected_value="absolute route path",
                                        actual_value=type(self.probe_path).__name__)
        probe_path = self.probe_path.strip()
        if not probe_path.startswith("/"):
            raise TransportOptionsError("The HTTP probe path must begin with a slash.",
                                        property_path="transport_options.http.probe_path", expected_value="absolute route path")
        object.__setattr__(self, "probe_path", probe_path)
        if (self.auth_header is None) != (self.auth_token is None):
            raise TransportOptionsError("The authentication header and token must be supplied together.",
                                        property_path="transport_options.http.auth", expected_value="both header and token, or neither")
        if self.auth_header is not None:
            if not isinstance(self.auth_header, str):
                raise TransportOptionsError("The authentication header name must be a string.",
                                            property_path="transport_options.http.auth_header", expected_value="non-empty string",
                                            actual_value=type(self.auth_header).__name__)
            auth_header = self.auth_header.strip()
            if not auth_header:
                raise TransportOptionsError("The authentication header name must not be empty.",
                                            property_path="transport_options.http.auth_header", expected_value="non-empty string")
            if not isinstance(self.auth_token, str) or not self.auth_token:
                raise TransportOptionsError("The authentication token must be a non-empty string.",
                                            property_path="transport_options.http.auth_token", expected_value="non-empty string")
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
                or not math.isfinite(value)
            ):
                path = "timeouts.connect_seconds" if field_name == "connect_timeout_seconds" else "timeouts.io_seconds"
                actual = value if type(value) in (int, float) and math.isfinite(value) else type(value).__name__
                raise TransportOptionsError("The transport timeout must be a finite number greater than zero.",
                                            property_path=path, expected_value="finite number > 0", actual_value=actual)
        if type(self.tls_verify) is not bool:
            raise TransportOptionsError("TLS verification must be a boolean.",
                                        property_path="transport_options.http.tls_verify",
                                        expected_value="boolean", actual_value=type(self.tls_verify).__name__)


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
        phase = "connect"
        try:
            connection.connect()
            phase = "configure_socket"
            if connection.sock is not None:
                connection.sock.settimeout(self._io_timeout_seconds)
            phase = "send_request"
            connection.request(
                request.method,
                target,
                body=request.body if request.body else None,
                headers=dict(request.headers),
            )
            phase = "receive_headers"
            response = connection.getresponse()
            phase = "read_body"
            return HttpResponse(
                status_code=int(response.status),
                headers=tuple(response.getheaders()),
                body=response.read(),
            )
        except Exception as exc:
            raise _exchange_error(exc, phase, request) from exc
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
            response = self._exchange_request(request)
        except TransportExchangeError as exc:
            return TransportDelivery(
                correlation_id=frame.correlation_id,
                state=exc.state, reply=None,
                diagnostic=exc.diagnostic, attempts=1,
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
        diagnostic_message = _find_header(
            response.headers,
            "X-Transport-Diagnostic-Message",
        )
        return TransportDelivery(
            correlation_id=frame.correlation_id,
            state=(TransportDeliveryState.BACKPRESSURED
                   if diagnostic_code == "transport_backpressured"
                   else TransportDeliveryState.FAILED),
            reply=reply,
            diagnostic=TransportDiagnostic(
                code=diagnostic_code or "remote_rejected",
                message=diagnostic_message or "remote transport endpoint rejected the frame",
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
        response = self._exchange_request(
            HttpRequest(
                base_url=self._config.base_url,
                method="GET",
                route_path=self._config.probe_path,
                headers=self._headers(None),
                body=b"",
            )
        )
        return 200 <= response.status_code < 300

    def _exchange_request(self, request: HttpRequest) -> HttpResponse:
        try:
            return self._exchange.exchange(request)
        except TransportExchangeError:
            raise
        except Exception as exc:
            # Custom exchanges may not identify a more specific phase.
            raise _exchange_error(exc, "exchange", request) from exc

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
        raise TransportOptionsError(
            "transport_options.http must be a table", property_path="transport_options.http",
            expected_value="table", actual_type=type(raw).__name__,
        )
    expected = {
        "auth_header",
        "probe_path",
        "route_path",
        "tls_verify",
    }
    unknown = sorted(set(raw) - expected)
    if unknown:
        raise TransportOptionsError(
            "transport_options.http contains unknown fields: "
            + ",".join(unknown), property_path="transport_options.http",
            actual_value=unknown, expected_value=sorted(expected),
        )
    missing = sorted(expected - set(raw))
    if missing:
        raise TransportOptionsError(
            "transport_options.http is missing fields: "
            + ",".join(missing), property_path="transport_options.http",
            missing_fields=missing,
        )
    tls_verify = raw.get("tls_verify")
    if type(tls_verify) is not bool:
        raise TransportOptionsError(
            "transport_options.http.tls_verify must be a boolean", property_path="transport_options.http.tls_verify",
            expected_value="boolean", actual_type=type(tls_verify).__name__,
        )
    normalized: dict[str, Any] = {
        "tls_verify": tls_verify,
    }
    for name in ("auth_header", "probe_path", "route_path"):
        value = raw.get(name)
        if not isinstance(value, str) or not value.strip():
            raise TransportOptionsError(
                f"transport_options.http.{name} "
                "must be a non-empty string", property_path=f"transport_options.http.{name}",
                expected_value="non-empty string", actual_type=type(value).__name__,
            )
        normalized[name] = value.strip()
    for name in ("probe_path", "route_path"):
        if not normalized[name].startswith("/"):
            raise TransportOptionsError(
                f"transport_options.http.{name} must start with /", property_path=f"transport_options.http.{name}",
                expected_value="path starting with /",
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
