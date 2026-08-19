"""Exact projection-only bindings for the five T50 non-HJSON commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class MaterialCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "material.asset.create": "sha256:8b6338f5661a08324bbb336033033749d0f7b75580a242d456a31af18f75efe6",
    "material.function.graph.apply": "sha256:b84dc2e9604ae5203e38206788d6e282ddb0dcdf1c8cf443cdc9f6b5b2ac9109",
    "material.graph.apply": "sha256:138bd85b4e83a0ebcc112d2a2c4f7cdebcba0601b0775d02005d5acdc7947925",
    "material_instance.asset.create": "sha256:bc72ecdb7f2c64a444e5feb8e9f817c9684d3732a1857dfb9a9949eca543b363",
    "material_instance.parameters.apply": "sha256:9f5f49a275a8e4ad7a179d8227a543cd8821a57ac24698bf41e4ef8148618220",
}
BINDINGS = MappingProxyType(
    {
        command_id: MaterialCommandBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact material command without local mechanics."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


__all__ = ["BINDINGS", "MaterialCommandBinding", "execute"]


