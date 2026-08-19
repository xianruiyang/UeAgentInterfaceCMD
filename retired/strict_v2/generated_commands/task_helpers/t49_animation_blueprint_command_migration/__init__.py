"""Exact projection-only bindings for the three T49 non-HJSON commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class AnimationBlueprintCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "animation.anim_blueprint.asset.create": "sha256:658ecb27f241d46d1784d7e69c4d852a32ceeb166c55cb98a2e4c81d3b4421ad",
    "animation.anim_blueprint.graph.apply": "sha256:9c4ba05244c585f5e0a757661926d15586e0baa93633450e66131a769674a2e9",
    "animation.anim_blueprint.layer_interface.asset.create": "sha256:cd66b39c136dcd210293cc0b9c80f1cb16dfcb48128b7b35acb78d75c4658f32",
}
BINDINGS = MappingProxyType(
    {
        command_id: AnimationBlueprintCommandBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact Animation Blueprint command without local mechanics."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


__all__ = ["BINDINGS", "AnimationBlueprintCommandBinding", "execute"]

