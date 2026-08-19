"""Exact projection-only bindings for the T44 capture commands."""

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class CaptureMediaBinding:
    command_id: str
    contract_hash: str


_CONTRACT_HASHES = {
    "capture.image.execute": "sha256:bba4ff1bd088ec29a36f3ee2e737ed65149eac2920d1d4381bcc76ccc8cc1b58",
    "capture.media.execute": "sha256:1443c13cb19e04ca572468919a02af8cf0c2d3017115c37f17f943d006efd6f1",
    "capture.render.execute": "sha256:61a9d55b9bcf249672ec507f3d07d94559f80e9d7688be409474f4996915c386",
}
BINDINGS = MappingProxyType({
    command_id: CaptureMediaBinding(command_id, contract_hash)
    for command_id, contract_hash in _CONTRACT_HASHES.items()
})


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS.get(command_id)
    if binding is None:
        raise ValueError(f"capture_media_command_unknown: {command_id}")
    return client.execute_exact(
        binding.command_id, params, contract_hash=binding.contract_hash
    )


__all__ = ["BINDINGS", "CaptureMediaBinding", "execute"]
