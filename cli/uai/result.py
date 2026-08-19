from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from types import MappingProxyType
from typing import Any

from .errors import ProtocolError, ServerCommandError


class Result:
    """Read-only, lossless view of one server response envelope."""

    __slots__ = ("_response",)

    def __init__(self, raw_response: Mapping[str, Any]) -> None:
        if not isinstance(raw_response, Mapping):
            raise ProtocolError(
                code="response_envelope_invalid",
                message="server response must be a mapping",
            )
        snapshot = deepcopy(dict(raw_response))
        if type(snapshot.get("ok")) is not bool:
            raise ProtocolError(
                code="response_ok_invalid",
                message="server response ok must be a boolean",
            )
        correlation = snapshot.get("correlation_id")
        if not isinstance(correlation, str) or not correlation.strip():
            raise ProtocolError(
                code="response_correlation_missing",
                message="server response correlation_id is required",
            )
        self._response = MappingProxyType(snapshot)

    @property
    def ok(self) -> bool:
        return self._response["ok"]

    @property
    def payload(self) -> Any:
        return deepcopy(self._response.get("payload"))

    @property
    def error(self) -> Any:
        return deepcopy(self._response.get("error"))

    @property
    def correlation_id(self) -> str:
        return self._response["correlation_id"]

    @property
    def raw_response(self) -> Mapping[str, Any]:
        return MappingProxyType(deepcopy(dict(self._response)))

    def raise_for_error(self) -> Result:
        if not self.ok:
            raise ServerCommandError(result=self)
        return self


__all__ = ["Result"]
