"""Exact projection-only bindings for the four T55 Timeline/Sequence commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class TimelineSequenceCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "timeline.sequence.create": "sha256:86f7b7b54881d1aadc60fce2ec4238c4024198b7100001539a1456064632ca4c",
    "timeline.sequence.read": "sha256:2102ec72188da3303b35710799ef4e3e638e0e633467afe38d6dce4430871bb5",
    "timeline.sequence.structure.replace": "sha256:546a1b690f6cad8a0a5eb54e6a6acd38467784bbec012ac0b1639a2f77911c2a",
    "timeline.widget_animation.read": "sha256:c58bc09025db52d75c6c3f79fa8b90b6d5212eaa6257c03646e392e961a7a63e",
}
BINDINGS = MappingProxyType(
    {command_id: TimelineSequenceCommandBinding(command_id, contract_hash)
     for command_id, contract_hash in _HASHES.items()}
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id, dict(params), contract_hash=binding.contract_hash
    )


__all__ = ["TimelineSequenceCommandBinding", "BINDINGS", "execute"]
