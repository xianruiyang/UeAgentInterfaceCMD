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

EXPECTED_OBLIGATION_FINGERPRINT = (
    "sha256:d80674ed9290a1013e7c7445f254966d85f32f41205757466d7de73d68afa815"
)

METHODS = {
    "graph.view.read": ("graph", "view_read"),
    "graph.view.update": ("graph", "view_update"),
    "viewport.actor.pick": ("viewport", "actor_pick"),
    "viewport.actor.select": ("viewport", "actor_select"),
    "viewport.camera.frame": ("viewport", "camera_frame"),
    "viewport.instance.list": ("viewport", "instance_list"),
    "viewport.pixel_scale.read": ("viewport", "pixel_scale_read"),
    "viewport.ray.deproject": ("viewport", "ray_deproject"),
    "viewport.ray.trace": ("viewport", "ray_trace"),
    "viewport.state.read": ("viewport", "state_read"),
    "viewport.state.restore": ("viewport", "state_restore"),
    "viewport.state.update": ("viewport", "state_update"),
    "viewport.view_mode.list": ("viewport", "view_mode_list"),
    "viewport.warning.list": ("viewport", "warning_list"),
}

class _FakeClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []
    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}
    def execute(self, command_id, params):
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(command_id, params, contract_hash=binding.binding_hash)

def _bindings():
    values = {command_id: BINDING_CATALOG.find(command_id) for command_id in METHODS}
    assert all(
        binding is not None
        and (binding.namespace, binding.method) == METHODS[command_id]
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in values.items()
    )
    return values

def _params(binding) -> dict[str, Any]:
    samples = {"string": "fixture", "integer": 1, "number": 1.0, "boolean": True, "array": [], "object": {}}
    return {item.name: samples.get(item.wire_type, {}) for item in binding.parameters}

def test_all_14_viewport_graph_commands_have_exact_default_bindings() -> None:
    assert len(METHODS) == 14 and len(set(METHODS)) == 14
    _bindings()

def test_default_named_method_preserves_one_exact_request() -> None:
    binding = _bindings()["viewport.state.read"]
    client = _FakeClient()
    params = _params(binding)
    getattr(getattr(bind_generated_commands(client), binding.namespace), binding.method)(**params)
    assert client.calls == [(binding.command_id, params, binding.binding_hash)]

def test_default_projection_contains_no_transport_or_editor_business_logic() -> None:
    binding = _bindings()["viewport.state.update"]
    method = getattr(getattr(bind_generated_commands(_FakeClient()), binding.namespace), binding.method)
    names = set(method.__func__.__code__.co_names)
    assert not {"requests", "httpx", "urllib", "retry", "sleep", "registry", "viewport", "layout", "restore"} & names

def test_t45_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper = cmd_root / "cli" / "uai" / "generated_commands" / "viewport_graph"
    docs = (
        cmd_root / "docs" / "active" / "t45_viewport_graph_control.md",
        cmd_root.parent / "Plugins" / "UeAgentInterface" / "docs" / "active" / "t45_viewport_graph_control.md",
    )
    assert not helper.exists()
    for document in docs:
        text = document.read_text(encoding="utf-8")
        for namespace, method in METHODS.values():
            assert f"client.{namespace}.{method}" in text
        assert "command_search" in text and "command_detail" in text and "uai-cli" in text
        assert "uai.generated_commands" not in text

def test_t45_historical_successor_consumes_all_19_frozen_rows_and_product_receipt() -> None:
    project_root = Path(__file__).resolve().parents[3]
    plan_root = project_root / "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
    obligations = load_historical_owner_obligations(
        plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json",
        owner_task_id="T45-VIEWPORT-GRAPH-CONTROL",
    )
    assert len(obligations) == 19
    assert historical_obligation_fingerprint(obligations) == EXPECTED_OBLIGATION_FINGERPRINT
    old_ids = {str(row["historical_command_id"]) for row in obligations}
    successor = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/docs/active/successors/t45_viewport_graph_control.json"
        ).read_text(encoding="utf-8")
    )
    plugin_doc = (
        project_root / "Plugins/UeAgentInterface/docs/active/t45_viewport_graph_control.md"
    ).read_text(encoding="utf-8")
    assert all(old_id in plugin_doc for old_id in old_ids)

    active_commands = load_active_command_snapshot(
        project_root / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    assert old_ids.isdisjoint(active_commands.command_ids)
    assert all(BINDING_CATALOG.find(command_id) is None for command_id in old_ids)
    evidence_ref = (
        "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT/evidence/"
        "T45-VIEWPORT-GRAPH-CONTROL-current-verification.json"
    )
    evidence_path = project_root / evidence_ref
    report = validate_historical_successor(
        document=successor,
        expected_owner_task_id="T45-VIEWPORT-GRAPH-CONTROL",
        expected_row_ids=tuple(
            str(row["historical_command_id"]) for row in obligations
        ),
        expected_obligations=obligations,
        expected_obligation_fingerprint=EXPECTED_OBLIGATION_FINGERPRINT,
        active_commands=active_commands,
        project_root=project_root,
        receipt_bindings=(
            {
                "test_id": "UAI.DeliveryWorkflow.T45.VIEWPORT.GRAPH.CONTROL",
                "ref": evidence_ref,
                "sha256": hashlib.sha256(evidence_path.read_bytes()).hexdigest(),
                "active_registry_hash": active_commands.registry_hash,
                "public_command_ids": list(METHODS),
                "assertions": [
                    {"pointer": "/status", "equals": "passed"},
                    {"pointer": "/historical_obligation_count", "equals": 19},
                    {"pointer": "/claims/public_to_real_ue", "equals": True},
                    {"pointer": "/claims/editor_transient_state", "equals": True},
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
    assert report.row_count == 19
    assert report.obligation_fingerprint == EXPECTED_OBLIGATION_FINGERPRINT
