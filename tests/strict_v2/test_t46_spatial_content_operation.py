from __future__ import annotations
from pathlib import Path
from typing import Any
import hashlib
import json
import re

import pytest

from uai.commands import BINDING_CATALOG, bind_generated_commands
from tools.uai_repository.migration_evidence import (
    historical_obligation_fingerprint,
    load_active_command_snapshot,
    load_historical_owner_obligations,
    validate_historical_successor,
)

EXPECTED_OBLIGATION_FINGERPRINT = (
    "sha256:1be62e898a7b750e62ca175ba5d9d34a153f760cbc22797b06e10e295a68b832"
)

METHODS = {
    "mesh.element.select_by_ray": ("mesh", "element_select_by_ray"),
    "mesh.pivot.update": ("mesh", "pivot_update"),
    "mesh.transform.bake": ("mesh", "transform_bake"),
    "reference.origin.resolve": ("reference", "origin_resolve"),
    "world.object_align": ("world", "object_align"),
    "world.object_snap_to_surface": ("world", "object_snap_to_surface"),
}
DORMANT_HJSON_COMMANDS = {
    "world.object_transform.read",
    "world.object_transform.update",
}
class _FakeClient:
    def __init__(self): self.calls: list[tuple[str, dict[str, Any], str]] = []
    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash)); return {"ok": True}
    def execute(self, command_id, params):
        binding = BINDING_CATALOG.find(command_id); assert binding is not None
        return self.execute_exact(command_id, params, contract_hash=binding.binding_hash)

def _bindings():
    values = {command_id: BINDING_CATALOG.find(command_id) for command_id in METHODS}
    assert all(binding is not None and (binding.namespace, binding.method) == METHODS[command_id]
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64 for command_id, binding in values.items())
    return values
def _params(binding):
    samples = {"string":"fixture","integer":1,"number":1.0,"boolean":True,"array":[],"object":{}}
    return {item.name: samples.get(item.wire_type,{}) for item in binding.parameters}

def test_all_6_spatial_content_commands_have_exact_default_bindings():
    assert len(METHODS) == 6 and len(set(METHODS)) == 6
    _bindings()
def test_default_named_method_preserves_one_exact_request():
    binding = _bindings()["world.object_align"]; client = _FakeClient(); params = _params(binding)
    getattr(getattr(bind_generated_commands(client), binding.namespace), binding.method)(**params)
    assert client.calls == [(binding.command_id, params, binding.binding_hash)]

def test_generic_world_transform_commands_are_dormant_behind_hjson():
    assert all(
        (binding := BINDING_CATALOG.find(command_id)) is not None
        and binding.status == "dormant"
        for command_id in DORMANT_HJSON_COMMANDS
    )
    assert BINDING_CATALOG.find("content_graph.items") is not None
    assert BINDING_CATALOG.find("content_graph.import_workspace") is not None
def test_default_projection_contains_no_transport_or_spatial_business_logic():
    binding = _bindings()["world.object_align"]
    method = getattr(getattr(bind_generated_commands(_FakeClient()), binding.namespace), binding.method)
    assert not {"requests","httpx","urllib","retry","sleep","registry","transform","trace","align","snap"} & set(method.__func__.__code__.co_names)
def test_t46_has_no_task_specific_binding_or_tutorial_authority():
    _bindings(); cmd_root = Path(__file__).resolve().parents[2]
    helper = cmd_root/"cli"/"uai"/"generated_commands"/"t46_spatial_content_operation"
    docs = (cmd_root/"docs"/"active"/"t46_spatial_content_operation.md",
        cmd_root.parent/"Plugins"/"UeAgentInterface"/"docs"/"active"/"t46_spatial_content_operation.md")
    assert not helper.exists()
    for document in docs:
        text = document.read_text(encoding="utf-8")
        for namespace, method in METHODS.values(): assert f"client.{namespace}.{method}" in text
        assert "command_search" in text and "command_detail" in text and "uai-cli" in text
        assert "frame_id" in text and "uai.generated_commands" not in text

@pytest.mark.historical_evidence
def test_t46_historical_successor_consumes_all_5_frozen_rows_and_product_receipt():
    project_root = Path(__file__).resolve().parents[3]
    plan_root = project_root / "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
    obligations = load_historical_owner_obligations(
        plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json",
        owner_task_id="T46-SPATIAL-CONTENT-OPERATION",
    )
    assert len(obligations) == 5
    assert historical_obligation_fingerprint(obligations) == EXPECTED_OBLIGATION_FINGERPRINT
    old_ids = {str(row["historical_command_id"]) for row in obligations}
    successor = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/docs/active/successors/t46_spatial_content_operation.json"
        ).read_text(encoding="utf-8")
    )
    plugin_doc = (
        project_root / "Plugins/UeAgentInterface/docs/active/t46_spatial_content_operation.md"
    ).read_text(encoding="utf-8")
    assert all(old_id in plugin_doc for old_id in old_ids)

    active_commands = load_active_command_snapshot(
        project_root / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    assert old_ids.isdisjoint(active_commands.command_ids)
    assert all(BINDING_CATALOG.find(command_id) is None for command_id in old_ids)
    evidence_ref = (
        "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT/evidence/"
        "T46-SPATIAL-CONTENT-OPERATION-current-verification.json"
    )
    evidence_path = project_root / evidence_ref
    report = validate_historical_successor(
        document=successor,
        expected_owner_task_id="T46-SPATIAL-CONTENT-OPERATION",
        expected_row_ids=tuple(str(row["historical_command_id"]) for row in obligations),
        expected_obligations=obligations,
        expected_obligation_fingerprint=EXPECTED_OBLIGATION_FINGERPRINT,
        active_commands=active_commands,
        project_root=project_root,
        receipt_bindings=(
            {
                "test_id": "UAI.DeliveryWorkflow.T46.SPATIAL.CONTENT.OPERATION",
                "ref": evidence_ref,
                "sha256": hashlib.sha256(evidence_path.read_bytes()).hexdigest(),
                "active_registry_hash": active_commands.registry_hash,
                "public_command_ids": list(METHODS),
                "assertions": [
                    {"pointer": "/status", "equals": "passed"},
                    {"pointer": "/historical_obligation_count", "equals": 5},
                    {"pointer": "/claims/public_to_real_ue", "equals": True},
                    {"pointer": "/claims/alignment_modes_covered", "equals": True},
                    {"pointer": "/claims/origin_sources_covered", "equals": True},
                    {"pointer": "/claims/independent_readback", "equals": True},
                    {"pointer": "/claims/failure_before_mutation", "equals": True},
                    {"pointer": "/claims/historical_semantics_covered", "equals": True},
                    {"pointer": "/claims/old_public_ids_absent", "equals": True},
                    {"pointer": "/claims/cleanup_confirmed", "equals": True},
                    {"pointer": "/claims/editor_preserved", "equals": True},
                ],
            },
        ),
    )
    assert report.row_count == 5
    assert report.obligation_fingerprint == EXPECTED_OBLIGATION_FINGERPRINT
