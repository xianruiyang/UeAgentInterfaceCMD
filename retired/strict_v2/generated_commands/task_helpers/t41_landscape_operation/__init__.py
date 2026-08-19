"""Exact, projection-only bindings for the T41 Landscape operations."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class LandscapeOperationBinding:
    command_id: str
    contract_hash: str


COMMAND_IDS = (
    "landscape.create",
    "landscape.height_delta",
)


_CONTRACT_HASHES = {
    "landscape.create": "sha256:c9668ed3377e3cc97988f4fe68d707f1d770c02ce280a1adcf243d653daa20b8",
    "landscape.height_delta": "sha256:e7626a7692dbe13028ef022fe77dcf30fd7fc746e76168dde50712ab70a6fe20",
}

BINDINGS = MappingProxyType(
    {
        command_id: LandscapeOperationBinding(
            command_id,
            _CONTRACT_HASHES[command_id],
        )
        for command_id in COMMAND_IDS
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS.get(command_id)
    if binding is None:
        raise ValueError(f"landscape_operation_command_unknown: {command_id}")
    return client.execute_exact(
        binding.command_id,
        params,
        contract_hash=binding.contract_hash,
    )


__all__ = [
    "BINDINGS",
    "COMMAND_IDS",
    "LandscapeOperationBinding",
    "execute",
]
