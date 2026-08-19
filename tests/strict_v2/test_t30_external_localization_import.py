from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_ID = "external.localization.po.import"

SUCCESSOR_COMMANDS = {
    "localization_apply_json": (
        "content_graph.import_workspace",
    ),
    "localization_compile_text": (
        "job.compile_build",
        "operation.status",
        "operation.receipt",
        "operation.release",
    ),
    "localization_diff_json": ("content_graph.compound",),
    "localization_export_json": ("content_graph.export_workspace",),
    "localization_export_po": (
        "job.compile_build",
        "operation.status",
        "operation.receipt",
        "operation.release",
    ),
    "localization_gather_text": (
        "job.compile_build",
        "operation.status",
        "operation.receipt",
        "operation.release",
    ),
    "localization_import_po": (
        "external.localization.po.import",
        "content_graph.compound",
    ),
    "localization_preview_culture": (
        "content_graph.compound",
        "editor.session",
        "operation.status",
        "operation.receipt",
        "operation.release",
    ),
    "localization_query_targets": ("content_graph.compound",),
    "localization_report": ("content_graph.compound",),
    "localization_validate_json": ("content_graph.compound",),
    "string_table_apply_json": (
        "content_graph.import_workspace",
    ),
    "string_table_diff_json": ("content_graph.compound",),
    "string_table_export_json": ("content_graph.export_workspace",),
    "string_table_validate_json": ("content_graph.compound",),
}

CONTENT_GRAPH_ACTIONS = {
    "localization_diff_json": "localization.diff",
    "localization_import_po": "localization.target.read",
    "localization_preview_culture": "localization.culture.read",
    "localization_query_targets": "localization.query_targets",
    "localization_report": "localization.report",
    "localization_validate_json": "localization.validate",
    "string_table_diff_json": "string_table.diff",
    "string_table_validate_json": "string_table.validate",
}

HJSON_PROVIDER_ROWS = {
    "localization_apply_json",
    "localization_export_json",
    "string_table_apply_json",
    "string_table_export_json",
}

LONG_RUNNING_POLICIES = {
    "localization_compile_text": "policy:owned-tool:localization-compile-text/v1",
    "localization_export_po": "policy:owned-tool:localization-export-po/v1",
    "localization_gather_text": "policy:owned-tool:localization-gather-text/v1",
    "localization_preview_culture": "policy:runtime-session:culture-preview/v1",
}


class _RecordedResult:
    ok = True


class _RecordingClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(
        self,
        command_id: str,
        params: dict[str, Any],
        *,
        contract_hash: str,
    ) -> _RecordedResult:
        self.calls.append((command_id, dict(params), contract_hash))
        return _RecordedResult()

    def execute(self, command_id: str, params: dict[str, Any]) -> _RecordedResult:
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_binding():
    binding = BINDING_CATALOG.find(COMMAND_ID)
    assert binding is not None
    assert binding.command_id == COMMAND_ID
    assert binding.namespace == "external"
    assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
    assert binding.binding_hash != "sha256:" + "0" * 64
    return binding


def test_localization_import_has_one_exact_default_binding() -> None:
    _require_binding()


def test_default_method_preserves_source_and_target() -> None:
    _require_binding()
    client = _RecordingClient()
    bind_generated_commands(client).external.localization_po_import(
        "D:/fixture.po",
        "StrictV2T30",
    )
    assert client.calls[0][0] == COMMAND_ID
    assert client.calls[0][1] == {
        "source_ref": "D:/fixture.po",
        "target_ref": "StrictV2T30",
    }


def test_named_and_generic_execution_use_the_same_exact_binding() -> None:
    binding = _require_binding()
    named = _RecordingClient()
    generic = _RecordingClient()
    params = {
        "source_ref": "D:/fixture.po",
        "target_ref": "StrictV2T30",
    }
    bind_generated_commands(named).external.localization_po_import(
        params["source_ref"],
        params["target_ref"],
    )
    generic.execute_exact(COMMAND_ID, params, contract_hash=binding.binding_hash)
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_ue_business_logic() -> None:
    _require_binding()
    method = bind_generated_commands(_RecordingClient()).external.localization_po_import
    names = set(method.__func__.__code__.co_names)
    assert "requests" not in names
    assert "httpx" not in names
    assert "urllib" not in names
    assert "retry" not in names
    assert "ImportTextForCulture" not in names
    assert "RefreshResources" not in names


def test_t30_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_binding()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = (
        cmd_root
        / "cli"
        / "uai"
        / "generated_commands"
        / "t30_external_localization_import"
    )
    task_doc = cmd_root / "docs" / "active" / "t30_external_localization_import.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t30_external_localization_import.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.external.localization_po_import" in text
        assert "command_search" in text
        assert "command_detail" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text


def test_t30_historical_successor_consumes_all_15_frozen_rows_exactly() -> None:
    project_root = Path(__file__).resolve().parents[3]
    plan_root = (
        project_root
        / "docs"
        / "plan"
        / "20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
    )
    annex = plan_root / "UAI_PRE_REFACTOR_COMMAND_APPROVAL.md"
    assert hashlib.sha256(annex.read_bytes()).hexdigest() == (
        "3972f62273a13c8c8a971d7e31924e08c8fc59dad9f35abbb87089728c1c265e"
    )
    inventory = json.loads(
        (plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json").read_text(
            encoding="utf-8"
        )
    )
    frozen_rows = [
        row
        for row in inventory["commands"]
        if row.get("target_task_id") == "T30-EXTERNAL-LOCALIZATION-IMPORT"
    ]
    assert len(frozen_rows) == 15
    assert {row["historical_command_id"] for row in frozen_rows} == set(
        SUCCESSOR_COMMANDS
    )

    successor = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/docs/active/successors"
            / "t30_external_localization_import.json"
        ).read_text(encoding="utf-8")
    )
    assert successor["schema"] == "uai.historical_successor.v2"
    assert successor["owner_task_id"] == "T30-EXTERNAL-LOCALIZATION-IMPORT"
    rows = {row["historical_command_id"]: row for row in successor["commands"]}
    assert set(rows) == set(SUCCESSOR_COMMANDS)
    for frozen in frozen_rows:
        historical_id = frozen["historical_command_id"]
        row = rows[historical_id]
        assert row["historical_contract"] == frozen["historical_contract"]
        assert row["resolved_from_contract_id"] == frozen["semantic_resolution"][
            "contract_id"
        ]
        assert row["successor"] == {
            "kind": "exact_command_set",
            "command_ids": list(SUCCESSOR_COMMANDS[historical_id]),
        }
        assert all(
            row["semantic_coverage"][axis]["status"] == "covered"
            for axis in ("purpose", "inputs", "outputs")
        )
        assert set(row["old_id_exit"].values()) == {False}
        if historical_id in CONTENT_GRAPH_ACTIONS:
            assert row["routing"]["content_graph_capability"] == (
                CONTENT_GRAPH_ACTIONS[historical_id]
            )
        if historical_id in HJSON_PROVIDER_ROWS:
            assert row["routing"]["hjson_provider_id"] == (
                "localization-string-table-hjson-provider"
            )
        if historical_id in LONG_RUNNING_POLICIES:
            assert row["routing"]["policy_id"] == LONG_RUNNING_POLICIES[historical_id]


def test_t30_old_ids_are_absent_and_closed_policies_have_production_owners() -> None:
    project_root = Path(__file__).resolve().parents[3]
    manifest = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
        ).read_text(encoding="utf-8")
    )
    active_ids = {command["command_id"] for command in manifest["commands"]}
    assert set(SUCCESSOR_COMMANDS).isdisjoint(active_ids)
    assert all(BINDING_CATALOG.find(command_id) is None for command_id in SUCCESSOR_COMMANDS)

    production = (
        project_root
        / "Plugins/UeAgentInterface/Source/UeAgentInterface/Private/Composition"
        / "LongRunningSession/UeAgentLongRunningSessionProduction.cpp"
    ).read_text(encoding="utf-8")
    provider = (
        project_root
        / "Plugins/UeAgentInterface/Source/UeAgentInterface/Private/DomainAdapters"
        / "ContentGraphRead/UeAgentExternalLocalizationContentGraphProvider.cpp"
    ).read_text(encoding="utf-8")
    hjson_provider = (
        project_root
        / "Plugins/UeAgentInterface/Source/UeAgentInterface/Private/DomainAdapters"
        / "LocalizationStringTable/UeAgentLocalizationStringTableHjsonProvider.cpp"
    ).read_text(encoding="utf-8")
    for policy_id in LONG_RUNNING_POLICIES.values():
        assert policy_id in production
    for action in CONTENT_GRAPH_ACTIONS.values():
        assert f'TEXT("{action}")' in provider
    assert 'TEXT("localization-string-table-hjson-provider")' in hjson_provider
    assert 'TEXT("content_graph.import_workspace")' in hjson_provider
    assert 'TEXT("content_graph.export_workspace")' in hjson_provider
