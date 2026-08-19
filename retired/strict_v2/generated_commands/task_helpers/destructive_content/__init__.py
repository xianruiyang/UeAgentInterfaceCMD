"""Exact, projection-only bindings for the T31 destructive-content operations."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class DestructiveContentBinding:
    command_id: str
    contract_hash: str


COMMAND_IDS = (
    "asset.delete",
    "asset.fixup_redirectors",
    "asset.move",
    "asset.object.clone",
    "modeling.actor.mesh.replace",
    "modeling.asset.material_slot.remove",
    "modeling.voxel.bounds.remove",
    "skeletal_mesh.remove_morph_target",
    "skeletal_mesh.remove_skin_weight_profile",
    "world.data_layer.delete",
    "world.level_content.delete_scope",
    "world.level_streaming.move_actors",
    "world.level_streaming.remove",
    "world.pcg.cleanup",
)


_CONTRACT_HASHES = {
    "asset.delete": "sha256:6ebfb6037b47d81db063b1743b6a1f4e4d1ae7784e8f7a1725d4abe30c5e486d",
    "asset.fixup_redirectors": "sha256:35097d782922815c6a5072ed275033f47579dcabff7202ed350f2d76b724f587",
    "asset.move": "sha256:6e171c87edbdbba9b8947baffa79cbf374fb13984819f73f19dbea9d1236ba68",
    "asset.object.clone": "sha256:24be997e268d424e0089763c2805f2009c40ebec5b8b4baaf6e8d2669542a1f7",
    "modeling.actor.mesh.replace": "sha256:2d911cd6055f513d4ef6fad58fd12de3b7ef02a08b4d4abfe8ea79e573720f14",
    "modeling.asset.material_slot.remove": "sha256:0db95f0ac9c646e21f1690bca5fecb95502802b8c83adefffe2ca071d527e7a2",
    "modeling.voxel.bounds.remove": "sha256:8168db45ce78828c185b426ca753019ac774fe0ee2ded88ae837f1c2c91e935c",
    "skeletal_mesh.remove_morph_target": "sha256:cc46eec7a4d3fa4f615615136982b454ab8c74ff632cf3da0d1071107b320afd",
    "skeletal_mesh.remove_skin_weight_profile": "sha256:e4d2f6502aef2d4a6a82e77ecdcf359c055faf78a9eefee4d5307990f64159f3",
    "world.data_layer.delete": "sha256:16790050c9d0a053675dc02212dc8412304ebdd4b4e5da786ff66595f450c136",
    "world.level_content.delete_scope": "sha256:92368e06077c92fffa3307cede7ea722cad5a7461e8effb77156bbc9708b8040",
    "world.level_streaming.move_actors": "sha256:aced3bb59b8d151a6a74191d4e6dc72b103494db14939907a6c176c5a789692a",
    "world.level_streaming.remove": "sha256:d9ad569d46256efe806f84fd42196ad1c2284f97f12761325ca0beb32bb55874",
    "world.pcg.cleanup": "sha256:634048500a7824314aeb3f800e8e189e37260cb91a4613dff97d380aac581410",
}
BINDINGS = MappingProxyType(
    {
        command_id: DestructiveContentBinding(
            command_id,
            _CONTRACT_HASHES[command_id],
        )
        for command_id in COMMAND_IDS
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS.get(command_id)
    if binding is None:
        raise ValueError(f"destructive_content_command_unknown: {command_id}")
    return client.execute_exact(
        binding.command_id,
        params,
        contract_hash=binding.contract_hash,
    )


__all__ = [
    "BINDINGS",
    "COMMAND_IDS",
    "DestructiveContentBinding",
    "execute",
]
