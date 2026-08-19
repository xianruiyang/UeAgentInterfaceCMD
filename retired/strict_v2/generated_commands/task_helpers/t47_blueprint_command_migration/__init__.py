"""Exact projection-only bindings for T47 Blueprint commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class BlueprintCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "blueprint.asset.create": "sha256:5e90ac2690d8806a9bc2f92ce7f771e10658d98d6465513984bebb142e263705",
    "blueprint.component.events.discover": "sha256:fdd2de78fa8f8bf9754f306061529b9c59fbe6b9021649872edaef4765d10175",
}
BINDINGS = MappingProxyType(
    {
        command_id: BlueprintCommandBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact Blueprint command without local mechanics."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


__all__ = ["BINDINGS", "BlueprintCommandBinding", "execute"]
