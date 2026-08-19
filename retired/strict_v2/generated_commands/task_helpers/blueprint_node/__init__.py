"""Exact projection-only binding for T11 Blueprint node candidate discovery."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class BlueprintNodeBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "blueprint.node.candidates": "sha256:0bb6dda908f98a8f13005caef662b3f71c25978bbee86d8eefb8da25fba069d1",
}
BINDINGS = MappingProxyType(
    {
        command_id: BlueprintNodeBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact Blueprint-node query without local mechanics."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


def blueprint_node_candidates(
    client,
    target: str,
    graph_id: str,
    *,
    query: str | None = None,
):
    params: dict[str, object] = {"target": target, "graph_id": graph_id}
    if query is not None:
        params["query"] = query
    return execute(client, "blueprint.node.candidates", params)


__all__ = [
    "BINDINGS",
    "BlueprintNodeBinding",
    "blueprint_node_candidates",
    "execute",
]
