from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = (
    "editor_project.config_section.update",
    "editor_project.device_profile.update",
    "editor_project.localization_target.update",
    "editor_project.platform_config.update",
    "editor_project.project_settings.update",
    "editor_project.scalability_group.update",
    "editor_project.string_table.update",
)

QUERY_SUCCESSORS = {
    "device_profile_diff_json": ("project.validation", "device_profile.diff"),
    "device_profile_export_json": ("config.section", "device_profile.export"),
    "device_profile_query": ("config.section", "device_profile.query"),
    "device_profile_resolve_cvars": (
        "config.resolved_value",
        "device_profile.resolve_cvars",
    ),
    "device_profile_validate_json": (
        "project.validation",
        "device_profile.validate",
    ),
    "platform_config_export_json": (
        "project.platform",
        "platform_config.export",
    ),
    "platform_config_validate_json": (
        "project.validation",
        "platform_config.validate",
    ),
    "platform_profile_validate_packaging": (
        "project.validation",
        "platform_profile.validate_packaging",
    ),
    "project_settings_diff_page": (
        "project.validation",
        "project_settings.diff",
    ),
    "project_settings_export_index": (
        "project.settings",
        "project_settings.index",
    ),
    "project_settings_export_page": (
        "project.settings",
        "project_settings.page",
    ),
    "project_settings_validate_page": (
        "project.validation",
        "project_settings.validate",
    ),
    "scalability_export_json": ("config.section", "scalability.export"),
    "scalability_validate_json": (
        "project.validation",
        "scalability.validate",
    ),
    "target_platform_query": ("project.platform", "target_platform.query"),
}

WRITE_SUCCESSORS = {
    "config_apply_section": (
        "editor_project.config_section.update",
        "config.section",
        "config.section",
    ),
    "device_profile_apply_json": (
        "editor_project.device_profile.update",
        "config.section",
        "config.section",
    ),
    "platform_config_apply_json": (
        "editor_project.platform_config.update",
        "config.section",
        "project.platform",
    ),
    "project_settings_apply_page": (
        "editor_project.project_settings.update",
        "project.settings",
        "project.settings",
    ),
    "scalability_apply_json": (
        "editor_project.scalability_group.update",
        "config.section",
        "config.section",
    ),
}

HISTORICAL_IDS = frozenset(QUERY_SUCCESSORS) | frozenset(WRITE_SUCCESSORS)


class _FakeClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(
        self,
        command_id: str,
        params: dict[str, Any],
        *,
        contract_hash: str,
    ) -> dict[str, object]:
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id: str, params: dict[str, Any]) -> dict[str, object]:
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_bindings():
    bindings = {
        command_id: BINDING_CATALOG.find(command_id) for command_id in COMMAND_IDS
    }
    assert all(
        binding is not None
        and binding.command_id == command_id
        and binding.namespace == "editor_project"
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def _config_params() -> dict[str, Any]:
    return {
        "changes": [{"key": "Fixture", "value": "1"}],
        "expected_revision": "fixture-revision",
        "target_ref": "config:/Script/Engine.Engine",
    }


def test_all_7_editor_project_commands_have_exact_default_bindings() -> None:
    assert len(COMMAND_IDS) == 7
    _require_bindings()


def test_default_config_update_preserves_the_exact_request() -> None:
    _require_bindings()
    client = _FakeClient()
    params = _config_params()
    bind_generated_commands(client).editor_project.config_section_update(**params)
    assert client.calls[0][0] == "editor_project.config_section.update"
    assert client.calls[0][1] == params


def test_named_and_generic_config_update_use_the_same_exact_binding() -> None:
    bindings = _require_bindings()
    named = _FakeClient()
    generic = _FakeClient()
    params = _config_params()
    bind_generated_commands(named).editor_project.config_section_update(**params)
    generic.execute_exact(
        "editor_project.config_section.update",
        params,
        contract_hash=bindings["editor_project.config_section.update"].binding_hash,
    )
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_ue_business_logic() -> None:
    _require_bindings()
    method = bind_generated_commands(_FakeClient()).editor_project.config_section_update
    names = set(method.__func__.__code__.co_names)
    assert not {
        "requests",
        "httpx",
        "urllib",
        "retry",
        "sleep",
        "configparser",
        "registry",
        "save",
        "reload",
        "rollback",
    } & names


def test_t39_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = (
        cmd_root
        / "cli"
        / "uai"
        / "generated_commands"
        / "t39_editor_project_operation"
    )
    task_doc = cmd_root / "docs" / "active" / "t39_editor_project_operation.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t39_editor_project_operation.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.editor_project.config_section_update" in text
        assert "client.editor_project.string_table_update" in text
        assert "command_search" in text
        assert "command_detail" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text


def test_t39_historical_successor_consumes_all_20_frozen_rows_exactly() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    project_root = cmd_root.parent
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
    preflight = json.loads(
        (plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json").read_text(
            encoding="utf-8"
        )
    )
    frozen_rows = [
        row
        for row in preflight["commands"]
        if row.get("target_task_id") == "T39-EDITOR-PROJECT-OPERATION"
    ]
    assert len(frozen_rows) == 20

    successor_path = (
        project_root
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "successors"
        / "t39_editor_project_operation.json"
    )
    successor = json.loads(successor_path.read_text(encoding="utf-8"))
    assert successor["schema"] == "uai.historical_successor.v2"
    assert successor["owner_task_id"] == "T39-EDITOR-PROJECT-OPERATION"
    rows = {row["historical_command_id"]: row for row in successor["commands"]}
    assert set(rows) == {
        row["historical_command_id"] for row in frozen_rows
    } == HISTORICAL_IDS

    for frozen in frozen_rows:
        historical_id = frozen["historical_command_id"]
        row = rows[historical_id]
        assert row["historical_contract"] == frozen["historical_contract"]
        assert row["resolved_from_contract_id"] == frozen["semantic_resolution"][
            "contract_id"
        ]
        assert all(
            row["semantic_coverage"][axis]["status"] == "covered"
            for axis in ("purpose", "inputs", "outputs")
        )
        assert row["product_evidence"]["test_id"] == (
            "UAI.DeliveryWorkflow.T39.EDITOR.PROJECT.OPERATION"
        )
        assert set(row["old_id_exit"].values()) == {False}
        if historical_id in QUERY_SUCCESSORS:
            command_id, action = QUERY_SUCCESSORS[historical_id]
            assert row["successor"] == {
                "kind": "exact_command_set",
                "command_ids": [command_id],
            }
            assert row["routing"] == {
                "query_command_id": command_id,
                "editor_project_capability": action,
            }
        else:
            operation_id, readback_id, target_read_id = WRITE_SUCCESSORS[
                historical_id
            ]
            assert row["successor"] == {
                "kind": "exact_command_set",
                "command_ids": [operation_id, readback_id],
            }
            assert row["routing"] == {
                "operation_command_id": operation_id,
                "readback_command_id": readback_id,
                "target_read_command_id": target_read_id,
                "target_read_capability": "target.read",
            }


def test_t39_all_20_old_ids_are_absent_from_manifest_and_sdk_catalog() -> None:
    project_root = Path(__file__).resolve().parents[3]
    manifest = json.loads(
        (
            project_root
            / "Plugins"
            / "UeAgentInterface"
            / "Resources"
            / "UaiCommandManifest.json"
        ).read_text(encoding="utf-8")
    )
    active_ids = {command["command_id"] for command in manifest["commands"]}
    assert HISTORICAL_IDS.isdisjoint(active_ids)
    assert all(BINDING_CATALOG.find(command_id) is None for command_id in HISTORICAL_IDS)


def test_t39_query_adapter_declares_every_closed_capability_action() -> None:
    project_root = Path(__file__).resolve().parents[3]
    source = (
        project_root
        / "Plugins"
        / "UeAgentInterface"
        / "Source"
        / "UeAgentInterface"
        / "Private"
        / "DomainAdapters"
        / "EditorProject"
        / "UeAgentEditorProjectMechanicsBoundary.cpp"
    ).read_text(encoding="utf-8")
    asset_project_read = (
        project_root
        / "Plugins"
        / "UeAgentInterface"
        / "Source"
        / "UeAgentInterface"
        / "Private"
        / "DomainAdapters"
        / "AssetProjectRead"
        / "UeAgentAssetProjectReadNative.cpp"
    ).read_text(encoding="utf-8")
    target_capabilities = (
        project_root
        / "Plugins"
        / "UeAgentInterface"
        / "Source"
        / "UeAgentInterface"
        / "Private"
        / "DomainAdapters"
        / "EditorProjectSimpleEffect"
        / "UeAgentEditorProjectSimpleEffectCapabilities.h"
    ).read_text(encoding="utf-8")
    runtime = (
        project_root
        / "Plugins"
        / "UeAgentInterface"
        / "Source"
        / "UeAgentInterface"
        / "Private"
        / "Composition"
        / "SimpleAuthoring"
        / "UeAgentSimpleAuthoringEditorProjectRuntime.cpp"
    ).read_text(encoding="utf-8")
    for _command_id, action in QUERY_SUCCESSORS.values():
        assert f'TEXT("{action}")' in source
    assert 'Action == TEXT("target.read")' in source
    for provider_binding in {
        "asset_project.read.config_section",
        "asset_project.read.config_resolved_value",
        "asset_project.read.project_settings",
        "asset_project.read.project_platform",
        "asset_project.read.project_validation",
    }:
        assert provider_binding in source
    assert "editor_project_capability" in asset_project_read
    assert "CreateEditorProjectQueryMechanicsPort" in asset_project_read
    assert "FUeAgentEditorProjectSettingsFieldObservation" in target_capabilities
    assert "TryReadSettingsFields" in target_capabilities
    assert "TryReadSettingsFields" in runtime
    assert 'SetArrayField(TEXT("fields")' in source
