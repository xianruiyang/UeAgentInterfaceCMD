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
    "sha256:7af7e45c1e03b82e658250644efbdad9408017b6bff7ca599abf881de8681ac0"
)
METHODS = {
    "blueprint.asset.create": ("blueprint", "asset_create"),
    "blueprint.component.events.discover": ("blueprint", "component_events_discover"),
}
SUCCESSOR_COMMANDS = {
    "job.compile_build",
    "operation.status",
    "operation.receipt",
    "operation.release",
    "graph.view.read",
    "graph.view.update",
    "viewport.state.read",
    "viewport.state.update",
}
class _FakeClient:
    def __init__(self): self.calls: list[tuple[str,dict[str,Any],str]]=[]
    def execute_exact(self,command_id,params,*,contract_hash): self.calls.append((command_id,dict(params),contract_hash)); return {"ok":True}
    def execute(self,command_id,params):
        binding=BINDING_CATALOG.find(command_id); assert binding is not None
        return self.execute_exact(command_id,params,contract_hash=binding.binding_hash)
def _bindings():
    values={cid:BINDING_CATALOG.find(cid) for cid in METHODS}
    assert all(b is not None and (b.namespace,b.method)==METHODS[cid] and re.fullmatch(r"sha256:[0-9a-f]{64}",b.binding_hash) and b.binding_hash!="sha256:"+"0"*64 for cid,b in values.items()); return values
def _params(b):
    samples={"string":"fixture","integer":1,"number":1.0,"boolean":True,"array":[],"object":{}}
    return {p.name:samples.get(p.wire_type,{}) for p in b.parameters}
def test_exact_default_inventory(): assert len(METHODS)==2; _bindings()
def test_default_named_method_forwards_one_exact_request():
    b=_bindings()["blueprint.asset.create"]; c=_FakeClient(); p=_params(b)
    getattr(getattr(bind_generated_commands(c),b.namespace),b.method)(**p)
    assert c.calls==[(b.command_id,p,b.binding_hash)]
def test_default_projection_has_no_transport_or_blueprint_business():
    b=_bindings()["blueprint.asset.create"]; m=getattr(getattr(bind_generated_commands(_FakeClient()),b.namespace),b.method)
    assert not {"requests","httpx","urllib","retry","sleep","registry","compile","save","reload"} & set(m.__func__.__code__.co_names)
def test_t47_legacy_binding_and_tutorial_authority_exit():
    _bindings(); root=Path(__file__).resolve().parents[2]; helper=root/"cli"/"uai"/"generated_commands"/"t47_blueprint_command_migration"
    docs=(root/"docs"/"active"/"t47_blueprint_command_migration.md",root.parent/"Plugins"/"UeAgentInterface"/"docs"/"active"/"t47_blueprint_command_migration.md")
    assert not helper.exists()
    for d in docs:
        text=d.read_text(encoding="utf-8")
        for ns,m in METHODS.values(): assert f"client.{ns}.{m}" in text
        assert "command_search" in text and "command_detail" in text and "uai-cli" in text
        assert "uai.generated_commands" not in text

@pytest.mark.historical_evidence
def test_t47_historical_successor_consumes_all_7_frozen_rows_and_product_receipt():
    project_root = Path(__file__).resolve().parents[3]
    plan_root = project_root / "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
    obligations = load_historical_owner_obligations(
        plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json",
        owner_task_id="T47-BLUEPRINT-COMMAND-MIGRATION",
    )
    assert len(obligations) == 7
    assert historical_obligation_fingerprint(obligations) == EXPECTED_OBLIGATION_FINGERPRINT
    old_ids = {str(row["historical_command_id"]) for row in obligations}
    successor_path = (
        project_root
        / "Plugins/UeAgentInterface/docs/active/successors/t47_blueprint_command_migration.json"
    )
    successor = json.loads(successor_path.read_text(encoding="utf-8"))
    plugin_doc = (
        project_root / "Plugins/UeAgentInterface/docs/active/t47_blueprint_command_migration.md"
    ).read_text(encoding="utf-8")
    assert all(old_id in plugin_doc for old_id in old_ids)

    active_commands = load_active_command_snapshot(
        project_root / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    assert old_ids.isdisjoint(active_commands.command_ids)
    assert SUCCESSOR_COMMANDS.issubset(active_commands.command_ids)
    assert all(BINDING_CATALOG.find(command_id) is None for command_id in old_ids)
    public_command_ids = [*METHODS, *sorted(SUCCESSOR_COMMANDS)]
    evidence_ref = (
        "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT/evidence/"
        "T47-BLUEPRINT-COMMAND-MIGRATION-current-verification.json"
    )
    evidence_path = project_root / evidence_ref
    report = validate_historical_successor(
        document=successor,
        expected_owner_task_id="T47-BLUEPRINT-COMMAND-MIGRATION",
        expected_row_ids=tuple(str(row["historical_command_id"]) for row in obligations),
        expected_obligations=obligations,
        expected_obligation_fingerprint=EXPECTED_OBLIGATION_FINGERPRINT,
        active_commands=active_commands,
        project_root=project_root,
        receipt_bindings=(
            {
                "test_id": "UAI.DeliveryWorkflow.T47.BLUEPRINT.COMMAND.MIGRATION",
                "ref": evidence_ref,
                "sha256": hashlib.sha256(evidence_path.read_bytes()).hexdigest(),
                "active_registry_hash": active_commands.registry_hash,
                "public_command_ids": public_command_ids,
                "assertions": [
                    {"pointer": "/status", "equals": "passed"},
                    {"pointer": "/historical_obligation_count", "equals": 7},
                    {"pointer": "/claims/public_to_real_ue", "equals": True},
                    {"pointer": "/claims/blueprint_create_persisted", "equals": True},
                    {"pointer": "/claims/component_events_covered", "equals": True},
                    {"pointer": "/claims/compile_and_log_covered", "equals": True},
                    {"pointer": "/claims/graph_live_persisted_covered", "equals": True},
                    {"pointer": "/claims/preview_camera_covered", "equals": True},
                    {"pointer": "/claims/failure_semantics", "equals": True},
                    {"pointer": "/claims/historical_semantics_covered", "equals": True},
                    {"pointer": "/claims/old_public_ids_absent", "equals": True},
                    {"pointer": "/claims/cleanup_confirmed", "equals": True},
                    {"pointer": "/claims/editor_preserved", "equals": True},
                ],
            },
        ),
    )
    assert report.row_count == 7
    assert report.obligation_fingerprint == EXPECTED_OBLIGATION_FINGERPRINT
