from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = (
    "editor_project.config_section.update",
    "editor_project.device_profile.update",
    "editor_project.localization_target.update",
    "editor_project.platform_config.update",
    "editor_project.project_settings.update",
    "editor_project.scalability_group.update",
    "editor_project.string_table.update",
)

SLEEP_COMMAND_IDS = (
    "editor_project.localization_target.update",
    "editor_project.string_table.update",
)
ACTIVE_COMMAND_IDS = tuple(
    command_id for command_id in COMMAND_IDS if command_id not in SLEEP_COMMAND_IDS
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
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_bindings():
    bindings = {
        command_id: _BINDING_CATALOG.find(command_id) for command_id in ACTIVE_COMMAND_IDS
    }
    assert all(
        binding is not None
        and binding.command_id == command_id
        and binding.namespace == "editor_project"
        and binding.status == "active"
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    dormant = {
        command_id: _BINDING_CATALOG.find(command_id) for command_id in SLEEP_COMMAND_IDS
    }
    assert all(
        binding is not None
        and binding.command_id == command_id
        and binding.namespace == "editor_project"
        and binding.status == "dormant"
        for command_id, binding in dormant.items()
    )
    return bindings


def test_t39_sleep_commands_are_dormant_and_not_named_sdk() -> None:
    _require_bindings()
    namespaces = bind_generated_commands(_FakeClient())
    for command_id in SLEEP_COMMAND_IDS:
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        assert binding.status == "dormant"
        assert not hasattr(namespaces.editor_project, binding.method)


def test_t39_non_hjson_commands_remain_active_named_sdk() -> None:
    bindings = _require_bindings()
    namespaces = bind_generated_commands(_FakeClient())
    for command_id in ACTIVE_COMMAND_IDS:
        assert bindings[command_id].status == "active"
        assert hasattr(namespaces.editor_project, bindings[command_id].method)


def _config_params() -> dict[str, Any]:
    return {
        "changes": [{"key": "Fixture", "value": "1"}],
        "expected_revision": "fixture-revision",
        "target_ref": "config:/Script/Engine.Engine",
    }


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
