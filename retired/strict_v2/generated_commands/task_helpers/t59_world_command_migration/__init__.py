"""Exact projection-only bindings for the nine T59 World commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class WorldCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "world.actor_hlod_layer.update": "sha256:3acc40240aba2e28eab95ae1ef1626693cf15c53cdddb84681d54a4bfda9571c",
    "world.actor_streaming_policy.update": "sha256:9b2142dafa0a2bd22f69b507bb839f63345829143c1c554a1bd5e88c07b679e5",
    "world.data_layer_instance.create": "sha256:1626857096ccf38dae8a584049d03d0a48fbcf7f0181dc588a85288cb57b6cc6",
    "world.data_layer_relation.update": "sha256:8608712ae00fff667667f81fc5b3dec037b51ad6bee56dbb86060b3c28fc90d7",
    "world.data_layer_state.update": "sha256:d1c5e9ec8b6b624644101ff3b0cf55816c269d139559f4d9009f3f632baf822d",
    "world.streaming_relation.create": "sha256:871195b9bd4aa5af58a98a25080547eea45190eb1693d8408aa3f2b1db39ed30",
    "world.streaming_relation.state.update": "sha256:f8ab81ac4a704fe1f423c36bc03edeb89b2bccd670fa16144f967166e75fb359",
    "world.wall.create_with_opening": "sha256:2d258d2d9e18f942121da02dda7e42b466fb5c6ef1e32f19c0dc3cb2b1762b26",
    "world.world_partition_streaming.update": "sha256:4d15aa0b561ab1d9ca0900ed9b01283099f92d4f12d4488995660101578f6748",
}
BINDINGS = MappingProxyType(
    {
        command_id: WorldCommandBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id, dict(params), contract_hash=binding.contract_hash
    )


__all__ = ["WorldCommandBinding", "BINDINGS", "execute"]
