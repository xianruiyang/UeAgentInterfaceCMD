"""Exact projection-only bindings for the nine T52 PCG commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class PcgCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "pcg.component.apply": "sha256:3191823d94dea8d52fa79201be04cde64b02edf3c9a87dcc13c931165a1b395c",
    "pcg.component.world_binding.apply": "sha256:04a797720928dda169018d048efabcffb2a5298430b2073883ad0a89d89eb058",
    "pcg.data_asset.apply": "sha256:9afa2d99d1e8e0947871551d2f8b5e2cb4f0586af8317fab44ccc972a89c131e",
    "pcg.data_asset.create_from_level": "sha256:7dc3d5f3b5e7172a1177653cf764f128aeed9e458aaf8525b4c5f4104439dad6",
    "pcg.generated_spatial_data.read": "sha256:91dff7e10e6cc3bc2ae8ab4a461ab6e27c7669d498c22383211cc00223fc0f49",
    "pcg.graph.apply": "sha256:e6a63f72ec53b3c9f4ceba8f0444b7ac3b3bece8fac62ecb717c561a047df73b",
    "pcg.graph_instance.apply": "sha256:f3d40c4a3b118058557bf0bd88fd7a6317e71763dcbd951e92ac01851ef1f681",
    "pcg.graph_parameters.apply": "sha256:ee48c01e1739e2106f32c39462ca7f566f1d57b7a33e6a3b9785192d25c8cfaf",
    "pcg.partition.spatial_state.read": "sha256:8952dc72d1f598a7fceca94d47d99db1de4e4842d8e0ae1ef91dba9cff34842a",
}
BINDINGS = MappingProxyType(
    {
        command_id: PcgCommandBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact PCG command without local mechanics."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


__all__ = ["BINDINGS", "PcgCommandBinding", "execute"]
