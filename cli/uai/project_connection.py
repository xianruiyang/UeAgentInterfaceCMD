"""Local Unreal project discovery and the shared project connection lifecycle."""
from __future__ import annotations

import configparser
from contextlib import ExitStack, contextmanager
import os
from pathlib import Path
import secrets
import sys
from typing import Iterator

from .connection import connect
from .errors import UsageError
from .uai_client import Client


_SETTINGS_SECTION = "/Script/UeAgentInterface.UeAgentInterfaceSettings"
TOKEN_ENV = "UAI_AUTH_TOKEN"


class _RuntimeSettingsError(UsageError, ValueError):
    """Typed configuration error; retain ValueError compatibility for runners."""


def find_project(project: str | Path | None = None) -> Path:
    """Use an explicit project, or the nearest Unreal project above cwd."""
    start = Path(project).expanduser().resolve() if project is not None else Path.cwd().resolve()
    if start.is_file() and start.suffix.lower() == ".uproject":
        return start.parent
    candidates = (start,) if project is not None else (start, *start.parents)
    for directory in candidates:
        projects = list(directory.glob("*.uproject")) if directory.is_dir() else []
        if len(projects) == 1:
            return directory
        if len(projects) > 1:
            raise UsageError(code="project_ambiguous", message="Specify one .uproject with --project.")
    raise UsageError(
        code="project_not_found",
        message="Run inside an Unreal project, or supply --project or --connection.",
    )


def _read_ini_value(path: Path, key: str, source_file: str) -> str:
    parser = configparser.ConfigParser(interpolation=None)
    parser.optionxform = str
    diagnostic = {"stage": "connection_config", "source_file": source_file, "property_path": key}
    if not path.is_file():
        raise _RuntimeSettingsError(code="uai_runner_config_missing", message="The UAI configuration file is missing.", diagnostic=diagnostic)
    try:
        with path.open(encoding="utf-8-sig") as stream:
            parser.read_file(stream)
    except configparser.Error as exc:
        line = getattr(exc, "lineno", None)
        if not isinstance(line, int):
            errors = getattr(exc, "errors", ())
            if errors:
                line = errors[0][0]
        if isinstance(line, int) and line > 0:
            diagnostic["line"] = line
        raise _RuntimeSettingsError(code="uai_runner_config_invalid", message="The UAI configuration file has invalid INI syntax.", diagnostic=diagnostic) from exc
    except (OSError, UnicodeError) as exc:
        raise _RuntimeSettingsError(code="uai_runner_config_read_failed", message="The UAI configuration file could not be read as UTF-8.", diagnostic=diagnostic) from exc
    if not parser.has_option(_SETTINGS_SECTION, key):
        raise _RuntimeSettingsError(code="uai_runner_config_field_missing", message="The required configuration field is missing.", diagnostic={**diagnostic, "actual_present": False})
    value = parser.get(_SETTINGS_SECTION, key).strip()
    if not value:
        raise _RuntimeSettingsError(code="uai_runner_config_field_empty", message="The required configuration field is empty.", diagnostic=diagnostic)
    return value


def read_runtime_settings(project_root: Path) -> tuple[int, str]:
    root = project_root.resolve()
    source_file = "Config/DefaultUeAgentInterface.ini"
    port_text = _read_ini_value(root / source_file, "Port", source_file)
    port_diagnostic = {"stage": "connection_config", "source_file": source_file, "property_path": "Port",
                       "expected_value": "integer in [1, 65535]", "actual_value": port_text}
    try:
        port = int(port_text)
    except ValueError as exc:
        raise _RuntimeSettingsError(code="uai_runner_port_invalid", message="The configured port is not an integer.", diagnostic=port_diagnostic) from exc
    if not 1 <= port <= 65535:
        raise _RuntimeSettingsError(code="uai_runner_port_invalid", message="The configured port is outside the valid range.", diagnostic=port_diagnostic)
    platform = {"win32": "WindowsEditor", "darwin": "MacEditor"}.get(sys.platform, "LinuxEditor")
    token_source = f"Saved/Config/{platform}/UeAgentInterface.ini"
    token = _read_ini_value(root / token_source, "AuthToken", token_source)
    return port, token


def connection_text(port: int, io_timeout_seconds: float = 120.0) -> str:
    return f'''format_version = 1

[connection]
transport = "http"
endpoint = "http://127.0.0.1:{port}"

[protocol]
version = "current"

[timeouts]
connect_seconds = 5.0
io_seconds = {float(io_timeout_seconds)}

[authentication]
mode = "bearer_env"
bearer_env = "{TOKEN_ENV}"

[transport_options.http]
tls_verify = true
route_path = "/api/uai/command"
probe_path = "/api/ping"
auth_header = "X-UeAgentInterface-Token"
'''


@contextmanager
def temporary_connection(
    project_root: Path, port: int, token: str, *, io_timeout_seconds: float = 120.0,
) -> Iterator[Path]:
    temporary_root = project_root / "tmp" / "uai_params"
    temporary_root.mkdir(parents=True, exist_ok=True)
    connection_path = temporary_root / f"connection-{os.getpid()}-{secrets.token_hex(8)}.toml"
    connection_path.write_text(connection_text(port, io_timeout_seconds), encoding="utf-8")
    previous = os.environ.get(TOKEN_ENV)
    os.environ[TOKEN_ENV] = token
    try:
        yield connection_path
    finally:
        if previous is None:
            os.environ.pop(TOKEN_ENV, None)
        else:
            os.environ[TOKEN_ENV] = previous
        connection_path.unlink(missing_ok=True)


@contextmanager
def connect_project(
    project: str | Path | None = None, *, io_timeout_seconds: float = 120.0,
) -> Iterator[Client]:
    """Connect to a local project without exposing its credentials to callers."""
    root = find_project(project)
    with ExitStack() as stack:
        try:
            port, token = read_runtime_settings(root)
            path = stack.enter_context(temporary_connection(root, port, token, io_timeout_seconds=io_timeout_seconds))
        except (OSError, ValueError) as exc:
            if isinstance(exc, UsageError):
                raise UsageError(
                    code="project_connection_invalid",
                    message=exc.message,
                    diagnostic=exc.diagnostic,
                ) from exc
            reason = (exc.strerror if isinstance(exc, OSError) else str(exc)) or type(exc).__name__
            raise UsageError.at_source(
                code="project_connection_invalid",
                message=f"Cannot prepare the local UAI connection: {reason}",
                facts={"stage": "connection_config", "source_file": str(root),
                       "actual_value": getattr(exc, "errno", None)},
            ) from exc
        client = stack.enter_context(connect(str(path)))
        yield client
