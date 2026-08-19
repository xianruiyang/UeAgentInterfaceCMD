from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands

COMMAND_IDS = ("content_graph.import_workspace", "content_graph.structure", "content_graph.export_workspace")

HISTORICAL_SUCCESSORS = {
    "curve_apply_json": ("content_graph.import_workspace",),
    "curve_export_json": ("content_graph.export_workspace",),
    "data_asset_apply_json": ("content_graph.import_workspace",),
    "data_asset_create": ("content_graph.import_workspace",),
    "data_asset_diff_json": (
        "content_graph.import_workspace",
        "content_graph.structure",
    ),
    "data_asset_export_json": ("content_graph.export_workspace",),
    "data_asset_validate_json": (
        "content_graph.import_workspace",
        "content_graph.structure",
    ),
    "data_table_apply_json": ("content_graph.import_workspace",),
    "data_table_diff_json": (
        "content_graph.import_workspace",
        "content_graph.structure",
    ),
    "data_table_export_json": ("content_graph.export_workspace",),
    "data_table_validate_json": (
        "content_graph.import_workspace",
        "content_graph.structure",
    ),
}

class _Client:
    def __init__(self): self.calls: list[tuple[str, dict[str, Any], str]] = []
    def execute_exact(self, command_id, params, *, contract_hash): self.calls.append((command_id, dict(params), contract_hash)); return {"ok": True}
    def execute(self, command_id, params):
        binding=BINDING_CATALOG.find(command_id); assert binding is not None
        return self.execute_exact(command_id, params, contract_hash=binding.binding_hash)

def _bindings():
    values={cid:BINDING_CATALOG.find(cid) for cid in COMMAND_IDS}
    assert all(v is not None and v.namespace=="content_graph" and re.fullmatch(r"sha256:[0-9a-f]{64}",v.binding_hash) for v in values.values())
    return values

def test_t27_uses_the_three_default_content_graph_bindings() -> None:
    assert {v.method for v in _bindings().values()} == {"import_workspace","structure","export_workspace"}

def test_t27_named_structure_forwards_one_exact_request() -> None:
    client=_Client(); bind_generated_commands(client).content_graph.structure("/Game/UAI/StrictV2/T27.Table")
    assert len(client.calls)==1 and client.calls[0][0]=="content_graph.structure"

def test_t27_default_binding_contains_no_table_business() -> None:
    names=set(bind_generated_commands(_Client()).content_graph.structure.__func__.__code__.co_names)
    assert not {"row","datatable","curvetable","key","source","save","reload"}&names

def test_t27_task_projection_and_tutorial_authority_exit() -> None:
    cmd_root=Path(__file__).resolve().parents[2]
    assert not (cmd_root/"cli/uai/generated_commands/t27_datatable_curvetable_domain").exists()
    docs=(cmd_root/"docs/active/t27_datatable_curvetable_domain.md",cmd_root.parent/"Plugins/UeAgentInterface/docs/active/t27_datatable_curvetable_domain.md")
    for document in docs:
        text=document.read_text(encoding="utf-8")
        for method in ("client.content_graph.import_workspace","client.content_graph.structure","client.content_graph.export_workspace"): assert method in text
        assert "command_search" in text and "command_detail" in text and "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert "export_workspace" in text and "verified" in text
        assert "explicitly rejected" not in text
        assert "uai.generated_commands" not in text


def test_t27_historical_successors_are_exact_and_row_complete() -> None:
    project_root = Path(__file__).resolve().parents[2].parent
    path = (
        project_root
        / "Plugins/UeAgentInterface/docs/active/successors/t27_datatable_curvetable_domain.json"
    )
    payload = __import__("json").loads(path.read_text(encoding="utf-8"))
    assert payload["schema"] == "uai.historical_successor.v2"
    assert payload["owner_task_id"] == "T27-DATATABLE-CURVETABLE-DOMAIN"
    rows = {row["historical_command_id"]: row for row in payload["commands"]}
    assert set(rows) == set(HISTORICAL_SUCCESSORS)
    for command_id, expected in HISTORICAL_SUCCESSORS.items():
        row = rows[command_id]
        assert row["approval"] == "2)"
        assert row["successor"] == {
            "kind": "exact_command_set",
            "command_ids": list(expected),
        }
        assert all(
            row["semantic_coverage"][field]["status"] == "covered"
            for field in ("purpose", "inputs", "outputs")
        )
        assert row["old_id_exit"] == {
            "public_executable": False,
            "manifest_active": False,
            "sdk_binding_active": False,
            "compatibility_alias": False,
        }


def test_t27_uses_the_common_verified_export_publisher() -> None:
    project_root = Path(__file__).resolve().parents[2].parent
    mechanics = (
        project_root
        / "Plugins/UeAgentInterface/Source/UeAgentInterface/Private/DomainAdapters"
        / "DataTableCurveTable/UeAgentDataTableCurveTableDomainMechanics.cpp"
    ).read_text(encoding="utf-8")
    assert "TryExportVerifiedWorkspace" in mechanics
    assert "FVerifiedExportRequest" in mechanics
    assert "datatable_curvetable_export_not_registered" not in mechanics
