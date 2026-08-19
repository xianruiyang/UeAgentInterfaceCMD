"""Exact projection-only bindings for the twelve T58 Rig Spatial commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class RigSpatialCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "animation.ik_probe_candidate.apply": "sha256:3d871022f91f53ce99321ace8e0fcfd08eae5bcf2472d50deadca6819f063812",
    "animation.subject.morph_weights.update": "sha256:ee665ff3504d572bb2f8e618f0e89df469e46e29f76e2a7a1d1db508e03a6d48",
    "animation.subject.pose.update": "sha256:648eb339fc1d492f522b3e0ea74543a8cd547ddcc1f9638d70b6a249f223085d",
    "rig.control.bake.animation": "sha256:336ee3fd89e072fe18fc6c826e116b344f574b3bc98528d2ed9091247e44cab1",
    "rig.control.bake.controls": "sha256:c5887d968c4801d97b502ba8745eb92dc32acfcc2b12edcdf174747178b1e6c6",
    "rig.ik.definition.update": "sha256:14ff13a441315cd8b0149ad7cc99f7676c84f5feb2f3dad95bdd0209bd5567d3",
    "rig.retarget.assets.generate": "sha256:f6a3568cae847d7774f2adb81d4eed20a770240f8c11c4b4871a1522017ae8f1",
    "rig.retarget.definition.update": "sha256:47c853666aad70e4e9e7ef55063db1091920d5ec0207baf9f987f527a3981687",
    "rig.retarget.pose.auto_align": "sha256:2d641e939b8541c3b856f65e2313383d6df1f25f1f6cf6797a4184198acf985b",
    "rig.retarget.pose.update": "sha256:f010e71343be99e46eaa52f2185574e5efff013422b85d8a214de5c4253ad2c0",
    "rig.skeleton.preview_mesh.bind": "sha256:d0692e1ddfe7ead6a9c84e533b5016b7e8dbb6492058ee2963fad7959ccff075",
    "rig.skeleton.socket.update": "sha256:70588cffdde5d5b07598f7ba80f7dfca29a033436de7f6930c4d4ab408b9e5dc",
}
BINDINGS = MappingProxyType(
    {
        command_id: RigSpatialCommandBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id, dict(params), contract_hash=binding.contract_hash
    )


__all__ = ["RigSpatialCommandBinding", "BINDINGS", "execute"]
