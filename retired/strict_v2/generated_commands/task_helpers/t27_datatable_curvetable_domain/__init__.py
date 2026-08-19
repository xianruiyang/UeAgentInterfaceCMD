"""Exact public helpers for the T27 DataTable/CurveTable HJSON domain."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType

from uai.generated_commands import uobject_dataasset as _content_graph


@dataclass(frozen=True, slots=True)
class DataTableCurveTableBinding:
    command_id: str
    contract_hash: str


_COMMAND_IDS = (
    "content_graph.import_workspace",
    "content_graph.structure",
    "content_graph.export_workspace",
)

BINDINGS = MappingProxyType(
    {
        command_id: DataTableCurveTableBinding(
            command_id,
            _content_graph.BINDINGS[command_id].contract_hash,
        )
        for command_id in _COMMAND_IDS
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


def structure(client, target: str, *, input: dict[str, object] | None = None):
    params: dict[str, object] = {"target": target}
    if input is not None:
        params["input"] = input
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


__all__ = [
    "BINDINGS",
    "DataTableCurveTableBinding",
    "export_workspace",
    "import_workspace",
    "structure",
]
