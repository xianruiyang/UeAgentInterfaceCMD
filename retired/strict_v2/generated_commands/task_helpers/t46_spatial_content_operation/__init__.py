"""Exact projection-only bindings for T46 spatial-content commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class SpatialContentBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "mesh.element.select_by_ray": "sha256:55ccc0726589d872328f2684426c111107c5ff811026f2e3ef406505f9c8be37",
    "mesh.pivot.update": "sha256:3c2a3d0185afac79f23aedcaf0844b647280eed8f8bc10b40018922922fc3459",
    "mesh.transform.bake": "sha256:c733a1bab4daf4fbfa912e8bcd79f556d491bee1a302f1198dcffaa7af71856b",
    "world.object_align": "sha256:e257a7dcc236857d352a364056e63d3c134dd7e943162e8e426b1cd0fe4b44c3",
    "world.object_snap_to_surface": "sha256:d18818788d2bb5cc5c8f0166644d540f5f5d75a4e1643d0ae2eb9b62a73bbed2",
    "world.object_transform.read": "sha256:de4ae1a565e5ce147e97474f2b6354adbba2260f1832ddfbc60bafe8dd40dfd7",
    "world.transform_candidates.evaluate": "sha256:e5d80d9c04617d169623404addc365bff275932506d6f31fa33a754d1df94f86",
}
BINDINGS = MappingProxyType(
    {
        command_id: SpatialContentBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact spatial-content command without local mechanics."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


__all__ = ["BINDINGS", "SpatialContentBinding", "execute"]
