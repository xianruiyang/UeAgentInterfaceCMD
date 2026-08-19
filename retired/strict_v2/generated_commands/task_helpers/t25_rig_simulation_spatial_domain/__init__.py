"""Thin exact bindings for the T25 runtime rig/spatial HJSON domain."""

from __future__ import annotations

from types import MappingProxyType

from uai.generated_commands import uobject_dataasset as _content_graph


BINDINGS = MappingProxyType(
    {
        command_id: _content_graph.BINDINGS[command_id]
        for command_id in (
            "content_graph.import_workspace",
            "content_graph.structure",
            "content_graph.export_workspace",
        )
    }
)


def _send(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        params,
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
        params["limits"] = limits
    return _send(client, "content_graph.import_workspace", params)


def structure(client, target: str, **kwargs):
    params: dict[str, object] = {"target": target}
    params.update(kwargs)
    return _send(client, "content_graph.structure", params)


def export_workspace(
    client,
    target: str,
    workspace_path: str,
    *,
    profile_id: str | None = None,
):
    params: dict[str, object] = {
        "target": target,
        "workspace_path": workspace_path,
    }
    if profile_id is not None:
        params["profile_id"] = profile_id
    return _send(client, "content_graph.export_workspace", params)


__all__ = ["BINDINGS", "export_workspace", "import_workspace", "structure"]
