"""Exact, projection-only bindings for T40 TextureGraph operations."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class TextureGraphBinding:
    command_id: str
    contract_hash: str


COMMAND_IDS = (
    "texture_graph.artifact.capture",
    "texture_graph.graph.link.mutate",
    "texture_graph.graph.node.mutate",
    "texture_graph.graph.parameter.mutate",
    "texture_graph.graph.validate_evaluate_settle",
)


_CONTRACT_HASHES = {
    "texture_graph.artifact.capture": "sha256:723f0561d1a5ad38f4d6904d53093d54c57a1147b40b478e16aa6cac31f88108",
    "texture_graph.graph.link.mutate": "sha256:8b8dfff1c02d59ec6ae39299820540d74f4be16438c6ce58b1e78ecac98fc5ac",
    "texture_graph.graph.node.mutate": "sha256:465bb08b7aad1f27c9580643c9e384ed31d86a0ea54da734ff8bae1fc09c36ff",
    "texture_graph.graph.parameter.mutate": "sha256:31e1891372c091521ce6079b42509cb6a1c5618182469cbafcf19669783c1dd8",
    "texture_graph.graph.validate_evaluate_settle": "sha256:46e73e1388146d140b57bb6c4c736549311eacf882641df309b3111e9e79f0f1",
}

BINDINGS = MappingProxyType(
    {
        command_id: TextureGraphBinding(command_id, _CONTRACT_HASHES[command_id])
        for command_id in COMMAND_IDS
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        params,
        contract_hash=binding.contract_hash,
    )
