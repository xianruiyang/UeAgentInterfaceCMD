from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass, field
import os
from pathlib import Path
from typing import Any

try:
    import tomllib as _toml
except ModuleNotFoundError:  # pragma: no cover - Python 3.10 only
    import tomli as _toml

from .errors import UsageError
from .transport_catalog import (
    TransportOptionsError,
    UnsupportedTransportError,
    load_transport_options,
)


_TOP_LEVEL_FIELDS = frozenset(
    {
        "format_version",
        "connection",
        "protocol",
        "timeouts",
        "authentication",
        "transport_options",
    }
)


def _usage(code: str, message: str) -> UsageError:
    return UsageError(code=code, message=message)


def _mapping(
    value: Any,
    *,
    field_name: str,
) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise _usage(
            "connection_config_invalid",
            f"{field_name} must be a table",
        )
    return value


def _reject_unknown(
    value: Mapping[str, Any],
    *,
    allowed: frozenset[str],
    field_name: str,
) -> None:
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise _usage(
            "connection_config_invalid",
            f"{field_name} contains unknown fields: {','.join(unknown)}",
        )


def _required_text(
    value: Any,
    *,
    field_name: str,
) -> str:
    if not isinstance(value, str) or not value.strip():
        raise _usage(
            "connection_config_invalid",
            f"{field_name} must be a non-empty string",
        )
    return value.strip()


def _positive_seconds(
    value: Any,
    *,
    field_name: str,
) -> float:
    if (
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        or value <= 0
    ):
        raise _usage(
            "connection_config_invalid",
            f"{field_name} must be a positive number",
        )
    return float(value)


@dataclass(frozen=True, slots=True)
class AuthenticationSnapshot:
    mode: str
    secret_source: Path | str | None = None
    _secret_value: str | None = field(default=None, repr=False)

    def get_secret_value(self) -> str | None:
        return self._secret_value


@dataclass(frozen=True, slots=True)
class ConnectionSnapshot:
    source_path: Path
    format_version: int
    transport: str
    endpoint: str
    protocol_version: str
    connect_timeout_seconds: float
    io_timeout_seconds: float
    authentication: AuthenticationSnapshot
    transport_options: Mapping[str, Mapping[str, Any]]


def _load_authentication(
    raw: Any,
    *,
    source_path: Path,
    environ: Mapping[str, str],
) -> AuthenticationSnapshot:
    table = _mapping(raw, field_name="authentication")
    mode = _required_text(
        table.get("mode"),
        field_name="authentication.mode",
    )
    if mode == "none":
        _reject_unknown(
            table,
            allowed=frozenset({"mode"}),
            field_name="authentication",
        )
        return AuthenticationSnapshot(mode=mode)

    if mode == "bearer_env":
        _reject_unknown(
            table,
            allowed=frozenset({"mode", "bearer_env"}),
            field_name="authentication",
        )
        variable = _required_text(
            table.get("bearer_env"),
            field_name="authentication.bearer_env",
        )
        secret = environ.get(variable)
        if not isinstance(secret, str) or not secret.strip():
            raise _usage(
                "connection_secret_missing",
                f"connection secret environment variable is missing: {variable}",
            )
        return AuthenticationSnapshot(
            mode=mode,
            secret_source=f"env:{variable}",
            _secret_value=secret,
        )

    if mode == "bearer_file":
        _reject_unknown(
            table,
            allowed=frozenset({"mode", "bearer_file"}),
            field_name="authentication",
        )
        configured_path = _required_text(
            table.get("bearer_file"),
            field_name="authentication.bearer_file",
        )
        candidate = Path(configured_path)
        secret_path = (
            candidate
            if candidate.is_absolute()
            else source_path.parent / candidate
        ).resolve()
        if not secret_path.is_file():
            raise _usage(
                "connection_secret_missing",
                f"connection secret file is missing: {secret_path}",
            )
        try:
            secret = secret_path.read_text(encoding="utf-8-sig")
        except OSError as exc:
            raise _usage(
                "connection_secret_missing",
                f"connection secret file cannot be read: {secret_path}",
            ) from exc
        secret = secret.rstrip("\r\n")
        if not secret.strip():
            raise _usage(
                "connection_secret_invalid",
                f"connection secret file is empty: {secret_path}",
            )
        return AuthenticationSnapshot(
            mode=mode,
            secret_source=secret_path,
            _secret_value=secret,
        )

    raise _usage(
        "connection_config_invalid",
        f"authentication mode is unsupported: {mode}",
    )


def load_connection_toml(
    path: str | os.PathLike[str],
    *,
    environ: Mapping[str, str] | None = None,
) -> ConnectionSnapshot:
    source_path = Path(path).expanduser().resolve()
    if not source_path.is_file():
        raise _usage(
            "connection_file_missing",
            f"connection file is missing: {source_path}",
        )
    try:
        text = source_path.read_text(encoding="utf-8-sig")
        raw = _toml.loads(text)
    except (OSError, UnicodeError, _toml.TOMLDecodeError) as exc:
        raise _usage(
            "connection_toml_invalid",
            f"connection TOML cannot be parsed: {source_path}",
        ) from exc

    root = _mapping(raw, field_name="root")
    _reject_unknown(
        root,
        allowed=_TOP_LEVEL_FIELDS,
        field_name="root",
    )

    format_version = root.get("format_version")
    if isinstance(format_version, bool) or not isinstance(
        format_version,
        int,
    ):
        raise _usage(
            "connection_config_invalid",
            "format_version must be an integer",
        )
    if format_version != 1:
        raise _usage(
            "connection_format_unsupported",
            f"connection format is unsupported: {format_version}",
        )

    connection = _mapping(
        root.get("connection"),
        field_name="connection",
    )
    _reject_unknown(
        connection,
        allowed=frozenset({"transport", "endpoint"}),
        field_name="connection",
    )
    transport = _required_text(
        connection.get("transport"),
        field_name="connection.transport",
    )
    endpoint = _required_text(
        connection.get("endpoint"),
        field_name="connection.endpoint",
    )
    try:
        transport_options = load_transport_options(
            transport,
            root.get("transport_options"),
            endpoint=endpoint,
        )
    except UnsupportedTransportError as exc:
        raise _usage(
            "connection_transport_unsupported",
            f"connection transport is unsupported: {transport}",
        ) from exc
    except TransportOptionsError as exc:
        raise _usage(
            "connection_config_invalid",
            str(exc),
        ) from exc

    protocol = _mapping(
        root.get("protocol"),
        field_name="protocol",
    )
    _reject_unknown(
        protocol,
        allowed=frozenset({"version"}),
        field_name="protocol",
    )
    protocol_version = _required_text(
        protocol.get("version"),
        field_name="protocol.version",
    )

    timeouts = _mapping(
        root.get("timeouts"),
        field_name="timeouts",
    )
    _reject_unknown(
        timeouts,
        allowed=frozenset({"connect_seconds", "io_seconds"}),
        field_name="timeouts",
    )
    connect_timeout_seconds = _positive_seconds(
        timeouts.get("connect_seconds"),
        field_name="timeouts.connect_seconds",
    )
    io_timeout_seconds = _positive_seconds(
        timeouts.get("io_seconds"),
        field_name="timeouts.io_seconds",
    )

    environment = os.environ if environ is None else environ
    authentication = _load_authentication(
        root.get("authentication"),
        source_path=source_path,
        environ=environment,
    )
    return ConnectionSnapshot(
        source_path=source_path,
        format_version=format_version,
        transport=transport,
        endpoint=endpoint,
        protocol_version=protocol_version,
        connect_timeout_seconds=connect_timeout_seconds,
        io_timeout_seconds=io_timeout_seconds,
        authentication=authentication,
        transport_options=transport_options,
    )


__all__ = [
    "AuthenticationSnapshot",
    "ConnectionSnapshot",
    "load_connection_toml",
]
