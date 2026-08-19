"""Exact projected helpers for the query calibration command set."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class QueryCalibrationBinding:
    command_id: str
    contract_hash: str


BINDINGS = MappingProxyType(
    {
        "query.command.search": QueryCalibrationBinding(
            "query.command.search",
            "sha256:40ebd19c418de793a28ca2d4b1f95de83e514068302aae19fc0e5eb2b7ab901c",
        ),
        "query.command.detail": QueryCalibrationBinding(
            "query.command.detail",
            "sha256:b7b58108ecb4e24f14eaf53d1c27dbbf80cc8eddee0c4e107d60df06a6dbcc93",
        ),
        "query.calibration.read": QueryCalibrationBinding(
            "query.calibration.read",
            "sha256:1b6bc3e66fa58f1700883469e4fcc83605aa20f18eef75cc64d3e5f7a8df31ac",
        ),
    }
)


def _send(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        params,
        contract_hash=binding.contract_hash,
    )


def command_search(client, intent: str, *, limit: int = 3, cursor: int = 0):
    params: dict[str, object] = {"intent": intent, "limit": limit}
    if cursor:
        params["cursor"] = cursor
    return _send(client, "query.command.search", params)


def command_detail(client, command_id: str, contract_hash: str):
    return _send(
        client,
        "query.command.detail",
        {"command_id": command_id, "contract_hash": contract_hash},
    )


def calibration_read(
    client,
    category: str,
    *,
    search_text: str | None = None,
    limit: int = 50,
    cursor: int = 0,
):
    params: dict[str, object] = {"category": category, "limit": limit}
    if search_text is not None:
        params["search_text"] = search_text
    if cursor:
        params["cursor"] = cursor
    return _send(client, "query.calibration.read", params)


__all__ = [
    "BINDINGS",
    "QueryCalibrationBinding",
    "calibration_read",
    "command_detail",
    "command_search",
]
