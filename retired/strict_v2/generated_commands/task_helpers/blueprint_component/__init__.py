"""Exact projection-only binding for T12 Blueprint Component candidates."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class BlueprintComponentBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "blueprint.component.candidates": "sha256:e08f0c5d16f3c637ebaceb416fa9d44fc738f23aaad50ef37d380caf62f0d0ef",
}
BINDINGS = MappingProxyType(
    {
        command_id: BlueprintComponentBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact Blueprint Component query without local mechanics."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


def blueprint_component_candidates(
    client,
    target: str,
    component_class: str,
    requested_name: str,
):
    return execute(
        client,
        "blueprint.component.candidates",
        {
            "target": target,
            "component_class": component_class,
            "requested_name": requested_name,
        },
    )


__all__ = [
    "BINDINGS",
    "BlueprintComponentBinding",
    "blueprint_component_candidates",
    "execute",
]
