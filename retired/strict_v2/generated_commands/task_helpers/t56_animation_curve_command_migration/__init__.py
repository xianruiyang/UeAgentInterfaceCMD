"""Exact projection-only bindings for the thirteen T56 Animation/Curve commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class AnimationCurveCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "animation.blend_space.asset.create": "sha256:03397031f048aa08769714b6ec29bfebe7b2f8b2fff0b3827f93cc0f85c363fa",
    "animation.blend_space.definition.apply": "sha256:0b26fcd148c2da3770500bd7285388a68a9585b9db58ab71968490953f885279",
    "animation.blend_space.sample": "sha256:a96bb7760911285db84be185abc77577edc49ddd3a50984706cf79b9ca5f1652",
    "animation.montage.create": "sha256:581f2578e33d0614968226597ec416f8cb6765cf7c2be1593737610595480acb",
    "animation.montage.read": "sha256:a3ff74f58f7f0ac762e80f17baebc440ae7ec9e1c4d232c51906ba93425cb765",
    "animation.montage.structure.replace": "sha256:4304eed3e66eff421b1080ad03c5b4e13c1911100acbfdabb85936bcd3218086",
    "animation.sequence.bone_tracks.replace": "sha256:0c0919a38db87dd984ab19ec6c7e6d5c9c234b1218d62006ff49c07b288f7a28",
    "animation.sequence.curves.update": "sha256:5eb2a3b1ab6b74deb62afb2c23bca6fb9deeb6ef40a553650e43e651386fd75b",
    "animation.sequence.events.update": "sha256:fd26da85952a066765962b29e792e5807604aa4bd070b893e467d5ef8d885bff",
    "animation.sequence.metadata.update": "sha256:5cdb5f1fec3a3642810d189e96e1c81183deed173cec25599e827cd7a7ffa8d7",
    "animation.sequence.pose.sample": "sha256:96d0be60cfd3d8efac6c5d4fff43e4c9eee96c7e2ec7bdc0441ca4a0e16f5cee",
    "animation.sequence.read": "sha256:4d000fea98a85202e2f2eb4230a00eb545a52f22bf04011feffa4548c410b13a",
    "animation.sequence.root_motion.analyze": "sha256:fbb0067272c67269514cd564be65f838a174dfa36ad24f37bfb0eec473e952ab",
}
BINDINGS = MappingProxyType(
    {
        command_id: AnimationCurveCommandBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id, dict(params), contract_hash=binding.contract_hash
    )


__all__ = ["AnimationCurveCommandBinding", "BINDINGS", "execute"]
