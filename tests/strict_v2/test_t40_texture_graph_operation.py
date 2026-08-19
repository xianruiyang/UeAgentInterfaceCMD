from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands
from tools.uai_repository.migration_evidence import (
    historical_obligation_fingerprint,
    load_active_command_snapshot,
    load_historical_owner_obligations,
    validate_historical_successor,
)


COMMAND_IDS = (
    "texture_graph.artifact.capture",
    "texture_graph.artifact.bake",
    "texture_graph.graph.link.mutate",
    "texture_graph.graph.node.mutate",
    "texture_graph.graph.parameter.mutate",
    "texture_graph.graph.validate_evaluate_settle",
    "texture_graph.runtime.probe",
)

HISTORICAL_SUCCESSORS = {
    "texture_graph_apply_folder": {
        "kind": "exact_command_set",
        "command_ids": ["content_graph.import_workspace"],
    },
    "texture_graph_bake_outputs": {
        "kind": "exact_command_set",
        "command_ids": ["texture_graph.artifact.bake"],
    },
    "texture_graph_create": {
        "kind": "exact_command_set",
        "command_ids": ["audio_media.asset.create"],
    },
    "texture_graph_export_folder": {
        "kind": "exact_command_set",
        "command_ids": ["content_graph.export_workspace"],
    },
    "texture_graph_get_info": {
        "kind": "exact_command_set",
        "command_ids": [
            "content_graph.summary",
            "content_graph.structure",
            "content_graph.items",
            "content_graph.relations",
            "content_graph.properties",
        ],
    },
    "texture_graph_runtime_probe": {
        "kind": "exact_command_set",
        "command_ids": ["texture_graph.runtime.probe"],
    },
    "texture_graph_validate_folder": {
        "kind": "architecture_contract",
        "contract_id": "uai.hjson.import.preflight/1",
        "representative_command_ids": ["content_graph.import_workspace"],
    },
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
        and binding.namespace == "texture_graph"
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def _capture_params() -> dict[str, Any]:
    return {
        "expected_settled_revision": "fixture-revision",
        "outputs": ["base_color"],
        "target_ref": "/Game/StrictV2/T40/TG_Default.TG_Default",
    }


def test_all_7_texture_graph_commands_have_exact_default_bindings() -> None:
    assert len(COMMAND_IDS) == 7
    _require_bindings()


def test_default_artifact_capture_preserves_the_exact_request() -> None:
    _require_bindings()
    client = _FakeClient()
    params = _capture_params()
    bind_generated_commands(client).texture_graph.artifact_capture(**params)
    assert client.calls[0][0] == "texture_graph.artifact.capture"
    assert client.calls[0][1] == params


def test_named_and_generic_capture_use_the_same_exact_binding() -> None:
    bindings = _require_bindings()
    named = _FakeClient()
    generic = _FakeClient()
    params = _capture_params()
    bind_generated_commands(named).texture_graph.artifact_capture(**params)
    generic.execute_exact(
        "texture_graph.artifact.capture",
        params,
        contract_hash=bindings["texture_graph.artifact.capture"].binding_hash,
    )
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_ue_business_logic() -> None:
    _require_bindings()
    method = bind_generated_commands(_FakeClient()).texture_graph.artifact_capture
    names = set(method.__func__.__code__.co_names)
    assert not {
        "requests",
        "httpx",
        "urllib",
        "retry",
        "sleep",
        "registry",
        "evaluate",
        "save",
        "reload",
        "rollback",
    } & names


def test_t40_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = (
        cmd_root
        / "cli"
        / "uai"
        / "generated_commands"
        / "t40_texture_graph_operation"
    )
    task_doc = cmd_root / "docs" / "active" / "t40_texture_graph_operation.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t40_texture_graph_operation.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.texture_graph.artifact_capture" in text
        assert "client.texture_graph.artifact_bake" in text
        assert "client.texture_graph.graph_node_mutate" in text
        assert "client.texture_graph.runtime_probe" in text
        assert "command_search" in text
        assert "command_detail" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text


def test_t40_historical_successor_consumes_all_7_frozen_rows_exactly() -> None:
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
        if row.get("target_task_id") == "T40-TEXTURE-GRAPH-OPERATION"
    ]
    assert len(frozen_rows) == 7
    assert {row["historical_command_id"] for row in frozen_rows} == set(
        HISTORICAL_SUCCESSORS
    )

    successor = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/docs/active/successors"
            / "t40_texture_graph_operation.json"
        ).read_text(encoding="utf-8")
    )
    assert successor["schema"] == "uai.historical_successor.v2"
    assert successor["owner_task_id"] == "T40-TEXTURE-GRAPH-OPERATION"
    rows = {row["historical_command_id"]: row for row in successor["commands"]}
    assert set(rows) == set(HISTORICAL_SUCCESSORS)
    for frozen in frozen_rows:
        historical_id = frozen["historical_command_id"]
        row = rows[historical_id]
        assert row["historical_contract"] == frozen["historical_contract"]
        assert row["resolved_from_contract_id"] == frozen["semantic_resolution"][
            "contract_id"
        ]
        assert row["successor"] == HISTORICAL_SUCCESSORS[historical_id]
        assert all(
            row["semantic_coverage"][axis]["status"] == "covered"
            for axis in ("purpose", "inputs", "outputs")
        )
        assert set(row["old_id_exit"].values()) == {False}


def test_t40_old_ids_are_absent_and_bake_probe_are_distinct_current_commands() -> None:
    project_root = Path(__file__).resolve().parents[3]
    manifest = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
        ).read_text(encoding="utf-8")
    )
    active_ids = {command["command_id"] for command in manifest["commands"]}
    assert set(HISTORICAL_SUCCESSORS).isdisjoint(active_ids)
    assert all(
        BINDING_CATALOG.find(command_id) is None
        for command_id in HISTORICAL_SUCCESSORS
    )
    assert "texture_graph.artifact.bake" in active_ids
    assert "texture_graph.runtime.probe" in active_ids
    assert "texture_graph.artifact.capture" in active_ids


def test_t40_current_successor_consumes_the_complete_inventory_fingerprint_and_product_receipt() -> None:
    project_root = Path(__file__).resolve().parents[3]
    plan_root = (
        project_root
        / "docs"
        / "plan"
        / "20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
    )
    obligations = load_historical_owner_obligations(
        plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json",
        owner_task_id="T40-TEXTURE-GRAPH-OPERATION",
    )
    expected_fingerprint = (
        "sha256:ca29e1d49edd23137dd6c0e13031a1d8e06055b640cce47e52d0df9795f6d727"
    )
    assert historical_obligation_fingerprint(obligations) == expected_fingerprint

    successor = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/docs/active/successors"
            / "t40_texture_graph_operation.json"
        ).read_text(encoding="utf-8")
    )
    evidence_ref = (
        "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT/evidence/"
        "T40-TEXTURE-GRAPH-OPERATION-current-verification.json"
    )
    evidence_path = project_root / evidence_ref
    active_commands = load_active_command_snapshot(
        project_root / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    report = validate_historical_successor(
        document=successor,
        expected_owner_task_id="T40-TEXTURE-GRAPH-OPERATION",
        expected_row_ids=tuple(HISTORICAL_SUCCESSORS),
        expected_obligations=obligations,
        expected_obligation_fingerprint=expected_fingerprint,
        active_commands=active_commands,
        project_root=project_root,
        receipt_bindings=(
            {
                "test_id": "UAI.DeliveryWorkflow.T40.TEXTURE.GRAPH.OPERATION",
                "ref": evidence_ref,
                "sha256": hashlib.sha256(evidence_path.read_bytes()).hexdigest(),
                "active_registry_hash": active_commands.registry_hash,
                "public_command_ids": [
                    "audio_media.asset.create",
                    "content_graph.export_workspace",
                    "content_graph.import_workspace",
                    "content_graph.items",
                    "content_graph.properties",
                    "content_graph.relations",
                    "content_graph.structure",
                    "content_graph.summary",
                    "texture_graph.artifact.bake",
                    "texture_graph.runtime.probe",
                ],
                "assertions": [
                    {"pointer": "/status", "equals": "passed"},
                    {"pointer": "/historical_obligation_count", "equals": 7},
                    {"pointer": "/claims/public_to_real_ue", "equals": True},
                    {"pointer": "/claims/real_render", "equals": True},
                    {"pointer": "/claims/directory_workspace", "equals": True},
                    {
                        "pointer": "/claims/restart_independent_readback",
                        "equals": True,
                    },
                    {"pointer": "/claims/old_public_ids_absent", "equals": True},
                    {"pointer": "/claims/cleanup_confirmed", "equals": True},
                ],
            },
        ),
    )
    assert report.row_count == 7
    assert report.obligation_fingerprint == expected_fingerprint
