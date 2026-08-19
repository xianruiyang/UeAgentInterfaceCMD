"""Exact projection-only bindings for the T24 animation rig graph HJSON domain."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class AnimationRigGraphDomainBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "animation_rig_graph.candidates": "sha256:c054dd2fb1846b127b03358839c17a5b5b23f7668d0605f51591835f2cf62306",
    "content_graph.compound": "sha256:0d450dd05bf2f67d2d026e1d619a9c2baea837fdbd2e758da16f9809c6e77a82",
    "content_graph.diagnostics": "sha256:8ef8e8674ae6e1834f644b8144ce8ca29772fb437c6224eb1871612dc2673979",
    "content_graph.export_workspace": "sha256:72ce5103c51c776b7ca58a548d353aa12e947e375b4b76d6e22cefe5d87ed30b",
    "content_graph.import_workspace": "sha256:201f63959442d432fa4b82520928e165779e15c3a0cc605347d71e9b9782eaa4",
    "content_graph.items": "sha256:fdf312a079cadb047d52ad4f22a5296075b721fe8eb47da6256da27542eb4f1c",
    "content_graph.properties": "sha256:3d556e9127e47fde436f60b58a93b9d9ca402c07a879bb1ae5f1b159e6bfc352",
    "content_graph.relations": "sha256:63f8fae69b94835adeb722757a6ac7019c76ca19a14e7897640128e0e02314e8",
    "content_graph.structure": "sha256:f41fb62f3c5fad2af29756740b45abfb01b1af2479f55ed88c9940ba84e4fa5a",
    "content_graph.summary": "sha256:28642e5be9673960e50938385f89a596f23ea01748d413b529a02324d81c2655",
}
BINDINGS = MappingProxyType(
    {
        command_id: AnimationRigGraphDomainBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


def _query(client, command_id: str, target: str):
    return execute(client, command_id, {"target": target})


def animation_rig_graph_candidates(
    client,
    target: str,
    *,
    query: str | None = None,
    space_ref: str | None = None,
    limit: int | None = None,
    cursor: int | None = None,
):
    params: dict[str, object] = {"target": target}
    if query is not None:
        params["query"] = query
    if space_ref is not None:
        params["space_ref"] = space_ref
    if limit is not None:
        params["limit"] = limit
    if cursor is not None:
        params["cursor"] = cursor
    return execute(client, "animation_rig_graph.candidates", params)


def content_graph_compound(client, target: str):
    return _query(client, "content_graph.compound", target)


def content_graph_diagnostics(client, target: str):
    return _query(client, "content_graph.diagnostics", target)


def content_graph_items(client, target: str):
    return _query(client, "content_graph.items", target)


def content_graph_properties(client, target: str):
    return _query(client, "content_graph.properties", target)


def content_graph_relations(client, target: str):
    return _query(client, "content_graph.relations", target)


def content_graph_structure(client, target: str):
    return _query(client, "content_graph.structure", target)


def content_graph_summary(client, target: str):
    return _query(client, "content_graph.summary", target)


def content_graph_export_workspace(client, target: str, workspace_path: str):
    return execute(
        client,
        "content_graph.export_workspace",
        {"target": target, "workspace_path": workspace_path},
    )


def content_graph_import_workspace(
    client,
    target: str,
    hjson_document: str,
    *,
    expected_revision: str,
    authorization_id: str,
    carrier: str = "inline",
):
    return execute(
        client,
        "content_graph.import_workspace",
        {
            "target": target,
            "hjson_document": hjson_document,
            "expected_revision": expected_revision,
            "authorization_id": authorization_id,
            "carrier": carrier,
        },
    )


__all__ = [
    "AnimationRigGraphDomainBinding",
    "BINDINGS",
    "animation_rig_graph_candidates",
    "content_graph_compound",
    "content_graph_diagnostics",
    "content_graph_export_workspace",
    "content_graph_import_workspace",
    "content_graph_items",
    "content_graph_properties",
    "content_graph_relations",
    "content_graph_structure",
    "content_graph_summary",
    "execute",
]
