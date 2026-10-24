from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
PLUGIN_ROOT = PROJECT_ROOT / "Plugins/UeAgentInterface"
CATALOG_ROOT = PLUGIN_ROOT / "docs/active/capability-catalog"
CATALOG_PATH = CATALOG_ROOT / "catalog.json"
HISTORY_PATH = CATALOG_ROOT / "historical-decisions.json"
MANIFEST_PATH = PLUGIN_ROOT / "Resources/UaiCommandManifest.json"
SCHEMA_ROOT = PLUGIN_ROOT / "docs/active/schemas"
OLD_ROOT = (
    PROJECT_ROOT
    / "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
)


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return f"sha256:{hashlib.sha256(path.read_bytes()).hexdigest()}"


def units_by_id(catalog: dict) -> dict[str, dict]:
    units = catalog["units"]
    result = {unit["id"]: unit for unit in units}
    assert len(result) == len(units)
    return result


def contains_key(value: object, key: str) -> bool:
    if isinstance(value, dict):
        return key in value or any(
            contains_key(item, key) for item in value.values()
        )
    if isinstance(value, list):
        return any(contains_key(item, key) for item in value)
    return False


def test_catalog_schema_identity_and_manifest_partition_are_current() -> None:
    catalog = load(CATALOG_PATH)
    manifest = load(MANIFEST_PATH)
    schema = load(SCHEMA_ROOT / "uai.capability_catalog.v2.schema.json")

    assert catalog["schema"] == schema["$id"] == "uai.capability_catalog.v2"
    assert set(catalog) == set(schema["required"]) == set(schema["properties"])
    assert catalog["command_manifest"] == {
        "path": "Resources/UaiCommandManifest.json",
        "file_sha256": digest(MANIFEST_PATH),
        "registry_hash": manifest["registry_hash"],
        "command_count": len(manifest["commands"]),
    }

    manifest_ids = [item["command_id"] for item in manifest["commands"]]
    assigned = [
        command_id
        for unit in catalog["units"]
        for command_id in unit["current_command_ids"]
    ]
    assert len(assigned) == len(set(assigned))
    assert set(assigned) == set(manifest_ids)
    assert len(assigned) == len(manifest_ids)

    assert "delivery_tasks" not in catalog
    assert not contains_key(catalog, "next_task_id")
    assert catalog["catalog_policy"] == {
        "command_count_is_completion": False,
        "old_task_done_is_current_evidence": False,
        "historical_exact_successor_is_current_without_revalidation": False,
        "unit_completion_requires": [
            "exact public ingress",
            "unique mechanics owner",
            "real UE mechanics",
            "applicable settle and persistence",
            "independent readback",
            "failure and cleanup",
            "current documentation and distribution",
        ],
        "unproven_scope_creates_task": False,
        "catalog_owns_task_state": False,
        "catalog_owns_next_action": False,
        "task_lifecycle_owner": "outer_project_task_table",
        "new_task_requires_concrete_real_content_consumer": True,
    }
    unit_schema = schema["$defs"]["unit"]
    for unit in catalog["units"]:
        assert set(unit_schema["required"]) <= set(unit) <= set(
            unit_schema["properties"]
        )
        assert unit["source_ids"]
        assert unit["object_types"]
        assert unit["authoring_surfaces"]
        assert unit["operations"]
        assert unit["lifecycles"]
        assert set(unit["focus_command_ids"]) <= set(unit["current_command_ids"])
        assert unit["evidence"]["not_proven"]


def test_post_t94_identities_have_one_current_unit_without_waking_dormant_commands() -> None:
    catalog = load(CATALOG_PATH)
    manifest = load(MANIFEST_PATH)
    units = units_by_id(catalog)

    expected_units = {
        "animation.state_machine.candidates": (
            "CU-ANIMATION-BLUEPRINT-COMMANDS"
        ),
        "umg.widget.candidates": "CU-UMG-COMMANDS",
        "runtime.scenario.execute": "CU-OPERATION-LIFECYCLE",
    }
    assigned_units = {
        command_id: unit["id"]
        for unit in catalog["units"]
        for command_id in unit["current_command_ids"]
    }
    assert {
        command_id: assigned_units[command_id]
        for command_id in expected_units
    } == expected_units
    assert all(
        units[unit_id]["evidence"]["not_proven"]
        for unit_id in set(expected_units.values())
    )

    dormant_ids = {
        item["command_id"]
        for item in manifest["commands"]
        if item["status"] == "dormant"
    }
    assert dormant_ids == {
        "world.actor_components",
        "world.actors",
        "world.object_transform.read",
        "world.object_transform.update",
        "world.property",
    }
    assert {
        item["status"] for item in manifest["commands"]
    } <= {"active", "dormant"}


def test_historical_decisions_are_final_but_do_not_promote_old_successors() -> None:
    catalog = load(CATALOG_PATH)
    history = load(HISTORY_PATH)
    schema = load(
        SCHEMA_ROOT / "uai.capability_historical_decisions.v2.schema.json"
    )
    source_path = OLD_ROOT / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json"
    approval_path = OLD_ROOT / "UAI_PRE_REFACTOR_COMMAND_APPROVAL.md"
    source = load(source_path)

    assert history["schema"] == schema["$id"] == (
        "uai.capability_historical_decisions.v2"
    )
    assert history["source"]["sha256"] == digest(source_path)
    assert history["approval_source"]["sha256"] == digest(approval_path)

    decisions = history["decisions"]
    decision_ids = [item["historical_command_id"] for item in decisions]
    source_ids = [item["historical_command_id"] for item in source["commands"]]
    assert len(decisions) == len(set(decision_ids)) == len(source_ids) == 939
    assert set(decision_ids) == set(source_ids)
    assert Counter(item["current_disposition"] for item in decisions) == {
        "required_capability_contract": 736,
        "explicit_non_support": 202,
        "retire_public_capability": 1,
    }

    assert history["policy"] == {
        "candidate_resolution_is_not_current_successor_proof": True,
        "current_disposition_is_final_resolution": True,
        "required_capability_contract_does_not_claim_exact_successor": True,
        "required_capability_contract_does_not_claim_full_implementation": True,
        "implementation_and_product_evidence_owner": (
            "catalog_units_and_task_results"
        ),
    }
    assert history["legacy_public_surface_exit"] == {
        "historical_identity_count": 939,
        "current_manifest_status": "all_historical_identities_absent",
        "compiled_public_surface_status": (
            "legacy_registry_and_http_handler_removed"
        ),
        "active_consumer_status": "legacy_public_consumers_removed",
        "retained_mechanics_status": "private_current_owner_only",
        "evidence_task_id": "TROOT-UAI-44-LEGACY-SURFACE-EXIT",
    }

    expected_row_keys = {
        "historical_command_id",
        "capability_unit_id",
        "current_disposition",
        "candidate_resolution_kind",
        "candidate_successor",
        "candidate_authority",
    }
    unit_ids = set(units_by_id(catalog))
    for item in decisions:
        assert set(item) == expected_row_keys
        assert item["capability_unit_id"] in unit_ids
        assert item["candidate_authority"] == "historical_evidence_only"


def test_high_value_recovery_units_are_explicit_and_non_overclaiming() -> None:
    catalog = load(CATALOG_PATH)
    units = units_by_id(catalog)

    cube_grid_ids = {
        "modeling_voxel_grid_begin",
        "modeling_voxel_grid_add_bounds",
        "modeling_voxel_grid_remove_bounds",
        "modeling_voxel_grid_apply",
    }
    cube_grid = units["CU-MODELING-VOXEL-GRID"]
    assert set(cube_grid["current_command_ids"]) == {
        "mesh.voxel_grid.apply",
        "mesh.voxel_grid.session",
    }
    assert cube_grid["command_contract_state"] == "registered_exact_contract"
    assert cube_grid["implementation_state"] == (
        "ue_owned_authoring_state_c8d_c9_public_vertical_with_legacy_sidecar_import_only"
    )
    assert "UE-owned serialized authoring state" in cube_grid["authoring_surfaces"]
    assert "sidecar" not in cube_grid["authoring_surfaces"]
    assert cube_grid["evidence"]["highest_verified_layer"] == (
        "public_sdk_real_ue_c8d_c9_persisted_vertical"
    )
    assert any(
        ref.endswith("/public_sdk/cubegrid-product.json")
        for ref in cube_grid["evidence"]["evidence_refs"]
    )
    assert set(cube_grid["historical_command_ids"]) == cube_grid_ids
    assert cube_grid["historical_obligation_count"] == 4
    assert {
        item["historical_command_id"]
        for item in catalog["recovered_historical_identities"]
    } == cube_grid_ids
    assert all(
        item["current_resolution_status"]
        == "required_capability_contract_c8d_c9_verified"
        and item["current_capability_ids"]
        == ["mesh.voxel_grid.apply", "mesh.voxel_grid.session"]
        and item["successor_equivalence"] == "non_exact"
        and item["current_capability_evidence_status"]
        == "c8d_c9_public_sdk_product_verified"
        and item["resolution_evidence_task_id"]
        == "TROOT-UAI-50-MODELING-WORLD-PHYSICS-EXACT-MATRIX"
        for item in catalog["recovered_historical_identities"]
    )

    assert set(units["CU-CAPTURE-MEDIA"]["focus_command_ids"]) == {
        "capture.image.execute",
        "capture.media.execute",
        "capture.render.execute",
    }
    assert "viewport.camera.frame" in units["CU-VIEWPORT-GRAPH"][
        "focus_command_ids"
    ]
    assert "content_graph.import_workspace" in units["CU-CONTENT-GRAPH"][
        "focus_command_ids"
    ]
    assert "blueprint.asset.create" in units["CU-BLUEPRINT-COMMANDS"][
        "focus_command_ids"
    ]
    assert "pcg.graph.apply" in units["CU-PCG-COMMANDS"]["focus_command_ids"]
    assert "pcg.graph.asset.create" in units["CU-PCG-COMMANDS"][
        "focus_command_ids"
    ]
    assert {
        "asset.paper_sprite.create",
        "asset.paper_flipbook.create",
        "asset.paper_tileset.update",
        "asset.paper_tilemap.update",
    } <= set(units["CU-ASSET-SIMPLE"]["focus_command_ids"])

    unified = units["CU-UNIFIED-CONTENT-DISCOVERY"]
    assert unified["current_command_ids"] == ["query.content.search"]
    assert unified["activation_contribution_ids"] == ["unified-content-search"]
    assert unified["blockers"] == []


def test_durable_maintenance_is_not_owned_by_asset_or_operation_commands() -> None:
    catalog = load(CATALOG_PATH)
    units = units_by_id(catalog)

    durable_ids = {
        "asset_durable.journal.read",
        "asset_durable.journal.reconcile",
    }
    durable = units["CU-DURABLE-MAINTENANCE"]
    assert set(durable["current_command_ids"]) == durable_ids
    assert durable["activation_contribution_ids"] == [
        "asset-durable-maintenance-owner"
    ]
    assert durable["evidence"]["highest_verified_layer"] == (
        "persistence_independent_readback"
    )
    assert any(
        "other than the exact 7E26" in boundary
        for boundary in durable["evidence"]["not_proven"]
    )

    assert durable_ids.isdisjoint(
        units["CU-ASSET-SIMPLE"]["current_command_ids"]
    )
    assert durable_ids.isdisjoint(
        units["CU-OPERATION-LIFECYCLE"]["current_command_ids"]
    )


def test_removed_candidate_identities_have_final_non_exact_resolutions() -> None:
    catalog = load(CATALOG_PATH)
    removed = catalog["retired_candidate_current_identities"]
    assert {item["command_id"] for item in removed} == {
        "animation_blueprint.authoring.apply",
        "blueprint.authoring.apply",
        "niagara.script.graph.apply",
        "niagara.stack.apply",
        "umg.authoring.apply",
    }
    assert all(
        item["current_status"] == "absent_from_current_manifest"
        and item["current_resolution_status"]
        == "required_capability_contract_recorded_no_exact_successor_claim"
        and item["resolution_evidence_task_id"]
        in {
            "TROOT-UAI-37-BLUEPRINT-UMG-GRAPH-VERTICAL",
            "TROOT-UAI-39-NIAGARA-PCG-AI-VERTICAL",
        }
        for item in removed
    )


def test_all_historical_rows_share_one_final_public_surface_exit_contract() -> None:
    history = load(HISTORY_PATH)
    manifest = load(MANIFEST_PATH)
    decisions = history["decisions"]
    assert len(decisions) == 939
    assert history["legacy_public_surface_exit"]["historical_identity_count"] == (
        len(decisions)
    )
    historical_ids = {item["historical_command_id"] for item in decisions}
    current_ids = {item["command_id"] for item in manifest["commands"]}
    assert historical_ids.isdisjoint(current_ids)


def test_compiled_legacy_public_surface_files_are_physically_absent() -> None:
    removed = {
        PLUGIN_ROOT
        / "Source/UeAgentInterface/Private/Server/UeAgentCommandRegistry.h",
        PLUGIN_ROOT
        / "Source/UeAgentInterface/Private/Server/UeAgentCommandRegistry.cpp",
        PLUGIN_ROOT
        / (
            "Source/UeAgentInterface/Private/Server/Generated/"
            "UeAgentCommandRegistry_NodeGraphExact.h"
        ),
        PLUGIN_ROOT
        / "Source/UeAgentInterface/Private/Server/UeAgentHttpServer.h",
        PLUGIN_ROOT
        / "Source/UeAgentInterface/Private/Server/UeAgentHttpServer.cpp",
    }
    assert not {path for path in removed if path.exists()}
    assert (
        PLUGIN_ROOT
        / (
            "Source/UeAgentInterface/Private/LegacyMechanics/"
            "UeAgentLegacyMechanics.h"
        )
    ).is_file()


def test_active_cpp_consumers_do_not_reference_legacy_public_surfaces() -> None:
    forbidden = {
        '#include "Server/UeAgentCommandRegistry.h"',
        "UeAgentCommandRegistry::",
        '#include "Server/UeAgentHttpServer.h"',
        "FUeAgentHttpServer",
    }
    roots = {
        PLUGIN_ROOT / "Source/UeAgentInterface",
        PLUGIN_ROOT / "Source/UeAgentInterfaceTests",
    }
    violations: list[str] = []
    for root in roots:
        for path in root.rglob("*"):
            if path.suffix not in {".h", ".cpp", ".inl"}:
                continue
            text = path.read_text(encoding="utf-8", errors="strict")
            for token in forbidden:
                if token in text:
                    violations.append(
                        f"{path.relative_to(PROJECT_ROOT).as_posix()}:{token}"
                    )
    assert violations == []
