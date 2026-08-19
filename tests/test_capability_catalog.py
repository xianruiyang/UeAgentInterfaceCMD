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


def test_catalog_schema_identity_and_manifest_partition_are_current() -> None:
    catalog = load(CATALOG_PATH)
    manifest = load(MANIFEST_PATH)
    schema = load(SCHEMA_ROOT / "uai.capability_catalog.v1.schema.json")

    assert catalog["schema"] == schema["$id"] == "uai.capability_catalog.v1"
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
    assert len(assigned) == 342

    delivery_task_ids = {item["id"] for item in catalog["delivery_tasks"]}
    for unit in catalog["units"]:
        assert unit["source_ids"]
        assert unit["object_types"]
        assert unit["authoring_surfaces"]
        assert unit["operations"]
        assert unit["lifecycles"]
        assert set(unit["focus_command_ids"]) <= set(unit["current_command_ids"])
        assert unit["next_task_id"] in delivery_task_ids
        assert unit["evidence"]["not_proven"]


def test_historical_decisions_are_complete_but_do_not_promote_old_successors() -> None:
    catalog = load(CATALOG_PATH)
    history = load(HISTORY_PATH)
    schema = load(
        SCHEMA_ROOT / "uai.capability_historical_decisions.v1.schema.json"
    )
    source_path = OLD_ROOT / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json"
    approval_path = OLD_ROOT / "UAI_PRE_REFACTOR_COMMAND_APPROVAL.md"
    source = load(source_path)

    assert history["schema"] == schema["$id"] == (
        "uai.capability_historical_decisions.v1"
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

    unit_ids = set(units_by_id(catalog))
    delivery_task_ids = {item["id"] for item in catalog["delivery_tasks"]}
    for item in decisions:
        assert item["capability_unit_id"] in unit_ids
        assert item["candidate_authority"] == "historical_evidence_only"
        assert item["current_exact_ingress_status"] == (
            "absent_from_current_manifest"
        )
        assert item["physical_exit_status"] == (
            "requires_legacy_surface_exit_audit"
        )
        assert item["next_task_id"] in delivery_task_ids
        if item["current_disposition"] == "required_capability_contract":
            assert item["current_successor_status"] == (
                "requires_vertical_semantic_and_product_revalidation"
            )


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
    assert cube_grid["current_command_ids"] == []
    assert cube_grid["command_contract_state"] == "missing_after_refactor"
    assert cube_grid["implementation_state"] == "removed_from_current_tree"
    assert set(cube_grid["historical_command_ids"]) == cube_grid_ids
    assert cube_grid["historical_obligation_count"] == 4
    assert {
        item["historical_command_id"]
        for item in catalog["recovered_historical_identities"]
    } == cube_grid_ids

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
    assert {
        "asset.paper_sprite.create",
        "asset.paper_flipbook.create",
        "asset.paper_tileset.update",
        "asset.paper_tilemap.update",
    } <= set(units["CU-ASSET-SIMPLE"]["focus_command_ids"])

    unified = units["CU-UNIFIED-CONTENT-DISCOVERY"]
    assert unified["current_command_ids"] == []
    assert unified["blockers"] == ["current unified contract is absent"]


def test_removed_candidate_identities_remain_non_exact_until_vertical_closure() -> None:
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
        and item["successor_status"]
        == "required_capability_contract_not_exact_successor"
        for item in removed
    )
