from __future__ import annotations

import json
from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


EXPECTED_COMMAND_IDS = {
    "asset.collection",
    "asset.properties",
    "asset.registry_record",
    "asset.registry_relations",
    "asset.relations",
    "asset.sample",
    "asset.summary",
    "asset.validation",
    "config.resolved_value",
    "config.section",
    "editor.dirty_resources",
    "editor.open_assets",
    "project.platform",
    "project.settings",
    "project.summary",
    "project.validation",
    "reference.asset_read",
    "reference.origin.resolve",
    "world.actor_components",
    "world.actors",
    "world.capsule_path",
    "world.capsule_sweep",
    "world.content",
    "world.data_layers",
    "world.hlod_assignments",
    "world.mesh_closest_vertex",
    "world.mesh_vertex_position",
    "world.nav_connectivity",
    "world.nav_find_path",
    "world.nav_project_point",
    "world.nearby_shapes",
    "world.overlap",
    "world.partition",
    "world.partition_health",
    "world.physics_component",
    "world.physics_constraint",
    "world.property",
    "world.ray_trace",
    "world.selection",
    "world.streaming_levels",
    "world.summary",
}

HISTORICAL_SUCCESSORS = {
    "actor_list_components": "world.actor_components",
    "asset_reference_graph": "asset.registry_relations",
    "config_export_section": "config.section",
    "editor_get_open_assets": "editor.open_assets",
    "editor_list_dirty_resources": "editor.dirty_resources",
    "get_world_state": "world.summary",
    "hlod_query_actors": "world.hlod_assignments",
    "level_check_overlaps": "world.overlap",
    "level_get_nearby_actor_obbs": "world.nearby_shapes",
    "level_get_selection": "world.selection",
    "level_list_actor_components": "world.actor_components",
    "level_streaming_query": "world.streaming_levels",
    "level_sweep_capsule": "world.capsule_sweep",
    "level_sweep_capsule_path": "world.capsule_path",
    "level_trace_world_ray": "world.ray_trace",
    "level_validate_connectivity": "world.nav_connectivity",
    "list_actors": "world.actors",
    "mesh_get_closest_vertex": "world.mesh_closest_vertex",
    "mesh_get_vertex_world_position": "world.mesh_vertex_position",
    "navmesh_find_path": "world.nav_find_path",
    "navmesh_project_point": "world.nav_project_point",
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

    def execute(
        self,
        command_id: str,
        params: dict[str, Any],
    ) -> _RecordedResult:
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_bindings():
    bindings = {
        command_id: BINDING_CATALOG.find(command_id)
        for command_id in EXPECTED_COMMAND_IDS
    }
    assert all(binding is not None for binding in bindings.values())
    assert all(
        binding is not None
        and binding.command_id == command_id
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        for command_id, binding in bindings.items()
    )
    return bindings


def test_all_audited_non_hjson_queries_have_exact_default_bindings() -> None:
    bindings = _require_bindings()
    assert {binding.namespace for binding in bindings.values() if binding} == {
        "asset",
        "config",
        "editor",
        "project",
        "reference",
        "world",
    }


def test_named_default_method_and_generic_execution_are_equivalent() -> None:
    bindings = _require_bindings()
    named = _RecordingClient()
    generic = _RecordingClient()

    bind_generated_commands(named).project.summary(
        projection={"include_provenance": True, "max_items": 25},
    )
    generic.execute_exact(
        "project.summary",
        {"projection": {"include_provenance": True, "max_items": 25}},
        contract_hash=bindings["project.summary"].binding_hash,
    )
    assert named.calls == generic.calls


def test_targeted_default_method_preserves_exact_target_and_input() -> None:
    _require_bindings()
    client = _RecordingClient()
    target = "/Game/Maps/TestMap.TestMap:PersistentLevel.Actor_1"
    bind_generated_commands(client).world.actor_components(
        target,
        input={"include_inherited": True},
        context={"state_plane": "authoring_memory"},
        projection={"max_items": 7},
    )
    assert client.calls[0][0] == "world.actor_components"
    assert client.calls[0][1] == {
        "target": target,
        "input": {"include_inherited": True},
        "context": {"state_plane": "authoring_memory"},
        "projection": {"max_items": 7},
    }


def test_reference_asset_read_is_server_owned_not_a_client_alias() -> None:
    _require_bindings()
    client = _RecordingClient()
    object_path = "/Game/UAI/Reference/BP_Reference.BP_Reference"
    bind_generated_commands(client).reference.asset_read(object_path)
    assert client.calls[0][0] == "reference.asset_read"
    assert client.calls[0][1] == {"object_path": object_path}


def test_t06_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = cmd_root / "cli" / "uai" / "generated_commands" / "query"
    task_doc = cmd_root / "docs" / "active" / "t06_non_hjson_query_migration.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t06_non_hjson_query_migration.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.project.summary" in text
        assert "client.world.actor_components" in text
        assert "client.reference.asset_read" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text


def test_all_historical_query_obligations_have_exact_v2_successors() -> None:
    project_root = Path(__file__).resolve().parents[2]
    plan_root = (
        project_root.parent
        / "docs"
        / "plan"
        / "20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
    )
    successor_path = (
        project_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "successors"
        / "t06_non_hjson_query_migration.json"
    )
    document = json.loads(successor_path.read_text(encoding="utf-8"))
    inventory = json.loads(
        (plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json").read_text(
            encoding="utf-8"
        )
    )
    frozen_rows = {
        row["historical_command_id"]: row
        for row in inventory["commands"]
        if row.get("historical_lifecycle") == "active"
        and row.get("target_task_id") == "T06-NON-HJSON-QUERY-MIGRATION"
    }

    assert document["schema"] == "uai.historical_successor.v2"
    assert document["owner_task_id"] == "T06-NON-HJSON-QUERY-MIGRATION"
    by_id = {row["historical_command_id"]: row for row in document["commands"]}
    assert set(by_id) == set(frozen_rows) == set(HISTORICAL_SUCCESSORS)
    assert len(by_id) == 21

    for historical_id, successor_id in HISTORICAL_SUCCESSORS.items():
        row = by_id[historical_id]
        frozen = frozen_rows[historical_id]
        assert row["approval"] == frozen["approval"]
        assert row["historical_source"] == frozen["historical_source"]
        assert row["historical_contract"] == frozen["historical_contract"]
        assert row["successor"] == {
            "kind": "exact_command_set",
            "command_ids": [successor_id],
        }
        if frozen["semantic_resolution"]["kind"] == "required_capability_contract":
            assert row["resolved_from_contract_id"] == frozen["semantic_resolution"][
                "contract_id"
            ]
        for surface in ("purpose", "inputs", "outputs"):
            coverage = row["semantic_coverage"][surface]
            assert coverage["status"] == "covered"
            assert coverage["by"] == [successor_id]
            assert coverage["explanation"].strip()
        evidence = row["product_evidence"]
        assert evidence["test_id"] == "UAI.StrictV2.T06.NON.HJSON.QUERY.MIGRATION"
        assert evidence["public_command_ids"] == [successor_id]
        assert {
            "public_entry",
            "behavior",
            "readback",
            "failure_semantics",
            "cleanup",
            "legacy_exit",
            "documentation",
        } <= set(evidence["required_claims"])
        assert set(row["old_id_exit"].values()) == {False}
        assert row["final_lifecycle"] == "deprecated_replaced"
