from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .result import Result


class Error(Exception):
    """Base error for failures that prevent or wrap a UAI client call."""

    def __init__(
        self,
        *,
        code: str,
        message: str,
    ) -> None:
        normalized_code = str(code).strip()
        normalized_message = str(message).strip()
        if not normalized_code:
            raise ValueError("uai_error_code_missing")
        if not normalized_message:
            raise ValueError("uai_error_message_missing")
        self.code = normalized_code
        self.message = normalized_message
        super().__init__(f"{self.code}: {self.message}")


class UsageError(Error):
    """The local API, connection file, or CLI input is invalid."""


class SerializationError(Error):
    """A request cannot be encoded into the UAI wire format."""


class TransportError(Error):
    """The transport cannot deliver or obtain a reply."""


class ProtocolError(Error):
    """The remote response does not satisfy the UAI wire contract."""


class ServerCommandError(Error):
    """Explicit exception view of an unsuccessful server Result."""

    def __init__(self, *, result: Result) -> None:
        error = result.error
        if isinstance(error, dict):
            code = str(error.get("code") or "server_command_failed")
            message = str(error.get("message") or "server command failed")
        else:
            code = "server_command_failed"
            message = (
                str(error).strip()
                if error is not None
                else "server command failed"
            )
        self.result = result
        super().__init__(code=code, message=message)


__all__ = [
    "Error",
    "ProtocolError",
    "SerializationError",
    "ServerCommandError",
    "TransportError",
    "UsageError",
]
