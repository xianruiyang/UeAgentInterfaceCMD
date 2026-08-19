"""Exact Sequence-domain helpers over the shared content_graph authority."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class SequenceDomainBinding:
    command_id: str
    contract_hash: str


BINDINGS = MappingProxyType(
    {
        "content_graph.import_workspace": SequenceDomainBinding(
            "content_graph.import_workspace",
            "sha256:201f63959442d432fa4b82520928e165779e15c3a0cc605347d71e9b9782eaa4",
        ),
        "content_graph.structure": SequenceDomainBinding(
            "content_graph.structure",
            "sha256:f41fb62f3c5fad2af29756740b45abfb01b1af2479f55ed88c9940ba84e4fa5a",
        ),
        "content_graph.export_workspace": SequenceDomainBinding(
            "content_graph.export_workspace",
            "sha256:72ce5103c51c776b7ca58a548d353aa12e947e375b4b76d6e22cefe5d87ed30b",
        ),
    }
)


def _send(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


def import_workspace(
    client,
    target: str,
    hjson_document: str,
    *,
    expected_revision: str,
    authorization_id: str,
    carrier: str = "inline",
    limits: dict[str, object] | None = None,
):
    params: dict[str, object] = {
        "target": target,
        "hjson_document": hjson_document,
        "expected_revision": expected_revision,
        "authorization_id": authorization_id,
        "carrier": carrier,
    }
    if limits is not None:
        params["limits"] = dict(limits)
    return _send(client, "content_graph.import_workspace", params)


def structure(client, target: str):
    return _send(client, "content_graph.structure", {"target": target})


def export_workspace(client, target: str, workspace_path: str):
    return _send(
        client,
        "content_graph.export_workspace",
        {"target": target, "workspace_path": workspace_path},
    )


__all__ = [
    "BINDINGS",
    "SequenceDomainBinding",
    "export_workspace",
    "import_workspace",
    "structure",
]
