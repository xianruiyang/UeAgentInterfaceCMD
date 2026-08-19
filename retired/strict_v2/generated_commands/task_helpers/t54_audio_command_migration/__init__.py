"""Exact projection-only bindings for the ten T54 audio/media commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class AudioCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "audio_media.asset.create": "sha256:2dfeb21c3205e90e633bc2b4b82fcb0b3a2e27b221f51dfbb2a291503da76d6c",
    "metasound.graph.compile_settle": "sha256:b7ec66fd80c8351e8718322b1b584eb5b18646f811e9ebea0b71ff4278678eb9",
    "metasound.graph.default.mutate": "sha256:c9509e369b3e6c52e2df7ef784eb59b67e80113def6f77e7cb984b5bcf74868a",
    "metasound.graph.interface.mutate": "sha256:1eff16c67941eb3b663fd8201f6891396b8e0fcca49b0514609f31240ad4cfd1",
    "metasound.graph.link.mutate": "sha256:19e3f4834d9d76cca195a6be9734b1cdca30eedb83b5edbd7586e62b3b8ceaba",
    "metasound.graph.node.mutate": "sha256:37aa68f39255e6b9fc273b7d683071fe4621d337d22e652fae53cf2735d415e6",
    "sound_cue.graph.compile_settle": "sha256:990c9da1858f13ecc17beebd48db6b1c91a16ba37d66f13120ab3c57a8e4d760",
    "sound_cue.graph.node.mutate": "sha256:9a113b904df7220ef773745f7bde55555e8e4ab5a19a8779cfe57e80bbb67028",
    "sound_cue.graph.relation.mutate": "sha256:e88a4407a04c62deb3acbf4d8ad2656dd73fa61b31c48ef6069371a6851b082f",
    "sound_cue.graph.root.mutate": "sha256:65a2bde0cadddd18764e2c186aa8a5379d7814f8c325c50fa3928b9db067d5b5",
}
BINDINGS = MappingProxyType(
    {command_id: AudioCommandBinding(command_id, contract_hash)
     for command_id, contract_hash in _HASHES.items()}
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id, dict(params), contract_hash=binding.contract_hash
    )


__all__ = ["AudioCommandBinding", "BINDINGS", "execute"]
