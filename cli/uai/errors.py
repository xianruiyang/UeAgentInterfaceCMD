from __future__ import annotations

import json
from copy import deepcopy
from collections.abc import Mapping
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
        diagnostic: Mapping[str, object] | None = None,
    ) -> None:
        normalized_code = str(code).strip()
        normalized_message = str(message).strip()
        if not normalized_code:
            raise ValueError("uai_error_code_missing")
        if not normalized_message:
            raise ValueError("uai_error_message_missing")
        self.code = normalized_code
        self.message = normalized_message
        # Producers own public facts. Remote diagnostics already passed through
        # the server boundary and are copied intact, never decoded from prose.
        self.diagnostic = (deepcopy(dict(diagnostic)) if isinstance(diagnostic, Mapping)
                           else {"code": self.code, "message": self.message, "stage": "sdk"})
        super().__init__(f"{self.code}: {self.message}")

    @classmethod
    def at_source(cls, *, code: str, message: str, facts: Mapping[str, object]) -> Error:
        """Construct local public facts where the failure is detected.

        Already-constructed remote diagnostics use ``diagnostic=`` unchanged.
        """
        diagnostic = {"stage": "sdk", **facts, "code": code, "message": message}
        return cls(code=code, message=message, diagnostic=diagnostic)


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
        diagnostic = None
        if isinstance(error, dict):
            code = str(error.get("code") or "server_command_failed")
            message = str(error.get("message") or "server command failed")
            diagnostic = error.get("diagnostic")
            if isinstance(diagnostic, dict):
                # Result has already projected this public carrier. Keep locations
                # and all collected errors visible when callers use raise_for_error.
                message = json.dumps(diagnostic, ensure_ascii=False, separators=(",", ":"))
            recovery = error.get("recovery_action")
            if isinstance(recovery, str) and recovery:
                message += "; recovery: " + recovery
        else:
            code = "server_command_failed"
            message = (
                str(error).strip()
                if error is not None
                else "server command failed"
            )
        self.result = result
        super().__init__(code=code, message=message, diagnostic=diagnostic)


__all__ = [
    "Error",
    "ProtocolError",
    "SerializationError",
    "ServerCommandError",
    "TransportError",
    "UsageError",
]
