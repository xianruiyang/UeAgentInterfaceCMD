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
    "animation.deformer_graph.asset.create",
    "animation.deformer_graph.topology.apply",
    "animation.deformer_source_library.asset.create",
    "animation.deformer_source_library.bindings.apply",
    "animation.mesh_deformer_collection.asset.create",
    "animation.mesh_deformer_collection.entries.apply",
    "animation.ml_deformer.asset.create",
    "animation.ml_deformer.configuration.apply",
    "deformer.evaluation.sample",
    "deformer.geometry.sample",
    "deformer.training_inputs.validate",
    "physics.asset.structure.replace",
    "physics.constraint.update",
    "physics.material.update",
    "physics.simulation.probe",
)
DEFAULT_METHODS = {
    "animation.deformer_graph.asset.create": ("animation", "deformer_graph_asset_create"),
    "animation.deformer_graph.topology.apply": ("animation", "deformer_graph_topology_apply"),
    "animation.deformer_source_library.asset.create": ("animation", "deformer_source_library_asset_create"),
    "animation.deformer_source_library.bindings.apply": ("animation", "deformer_source_library_bindings_apply"),
    "animation.mesh_deformer_collection.asset.create": ("animation", "mesh_deformer_collection_asset_create"),
    "animation.mesh_deformer_collection.entries.apply": ("animation", "mesh_deformer_collection_entries_apply"),
    "animation.ml_deformer.asset.create": ("animation", "ml_deformer_asset_create"),
    "animation.ml_deformer.configuration.apply": ("animation", "ml_deformer_configuration_apply"),
    "deformer.evaluation.sample": ("deformer", "evaluation_sample"),
    "deformer.geometry.sample": ("deformer", "geometry_sample"),
    "deformer.training_inputs.validate": ("deformer", "training_inputs_validate"),
    "physics.asset.structure.replace": ("physics", "asset_structure_replace"),
    "physics.constraint.update": ("physics", "constraint_update"),
    "physics.material.update": ("physics", "material_update"),
    "physics.simulation.probe": ("physics", "simulation_probe"),
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


def _dummy(wire_type: str) -> Any:
    return {
        "string": "fixture",
        "integer": 1,
        "number": 1.0,
        "boolean": True,
        "array": [],
        "object": {},
    }.get(wire_type, {})


def _require_bindings():
    bindings = {
        command_id: BINDING_CATALOG.find(command_id) for command_id in COMMAND_IDS
    }
    assert all(
        binding is not None
        and (binding.namespace, binding.method) == DEFAULT_METHODS[command_id]
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def _params(binding) -> dict[str, Any]:
    return {parameter.name: _dummy(parameter.wire_type) for parameter in binding.parameters}


def _named_call(client: _FakeClient, binding, params: dict[str, Any]) -> None:
    namespace = getattr(bind_generated_commands(client), binding.namespace)
    method = getattr(namespace, binding.method)
    method(**params)


def test_all_15_physics_deformer_commands_have_exact_default_bindings() -> None:
    assert len(COMMAND_IDS) == 15
    assert len(set(COMMAND_IDS)) == 15
    _require_bindings()


def test_default_named_method_preserves_one_exact_request() -> None:
    binding = _require_bindings()[COMMAND_IDS[0]]
    client = _FakeClient()
    params = _params(binding)
    _named_call(client, binding, params)
    assert client.calls == [(binding.command_id, params, binding.binding_hash)]


def test_named_and_generic_methods_use_the_same_exact_binding() -> None:
    binding = _require_bindings()[COMMAND_IDS[-1]]
    named = _FakeClient()
    generic = _FakeClient()
    params = _params(binding)
    _named_call(named, binding, params)
    generic.execute_exact(binding.command_id, params, contract_hash=binding.binding_hash)
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_ue_business_logic() -> None:
    binding = _require_bindings()[COMMAND_IDS[0]]
    namespace = getattr(bind_generated_commands(_FakeClient()), binding.namespace)
    method = getattr(namespace, binding.method)
    names = set(method.__func__.__code__.co_names)
    assert not {
        "requests", "httpx", "urllib", "retry", "sleep", "registry",
        "save", "reload", "rollback", "physics", "deformer",
    } & names


def test_t42_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = cmd_root / "cli" / "uai" / "generated_commands" / "t42_physics_deformer_operation"
    task_doc = cmd_root / "docs" / "active" / "t42_physics_deformer_operation.md"
    plugin_doc = (
        cmd_root.parent / "Plugins" / "UeAgentInterface" / "docs" / "active"
        / "t42_physics_deformer_operation.md"
    )
    assert not helper_root.exists()
    expected_calls = {
        f"client.{namespace}.{method}" for namespace, method in DEFAULT_METHODS.values()
    }
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert expected_calls <= {item.split("(")[0] for item in text.split() if item.startswith("client.")}
        assert "command_search" in text
        assert "command_detail" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text


def test_t42_current_successor_consumes_all_41_frozen_rows_and_product_receipt() -> None:
    project_root = Path(__file__).resolve().parents[3]
    plan_root = (
        project_root
        / "docs"
        / "plan"
        / "20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
    )
    obligations = load_historical_owner_obligations(
        plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json",
        owner_task_id="T42-PHYSICS-DEFORMER-OPERATION",
    )
    expected_fingerprint = (
        "sha256:d300a874e8bfdd2add33e4498b0028cfcbce83d2986de5bea16765a4ae98fa2c"
    )
    assert len(obligations) == 41
    assert historical_obligation_fingerprint(obligations) == expected_fingerprint

    successor = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/docs/active/successors"
            / "t42_physics_deformer_operation.json"
        ).read_text(encoding="utf-8")
    )
    evidence_ref = (
        "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT/evidence/"
        "T42-PHYSICS-DEFORMER-OPERATION-current-verification.json"
    )
    evidence_path = project_root / evidence_ref
    active_commands = load_active_command_snapshot(
        project_root / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    report = validate_historical_successor(
        document=successor,
        expected_owner_task_id="T42-PHYSICS-DEFORMER-OPERATION",
        expected_row_ids=tuple(
            str(row["historical_command_id"]) for row in obligations
        ),
        expected_obligations=obligations,
        expected_obligation_fingerprint=expected_fingerprint,
        active_commands=active_commands,
        project_root=project_root,
        receipt_bindings=(
            {
                "test_id": "UAI.DeliveryWorkflow.T42.PHYSICS.DEFORMER.OPERATION",
                "ref": evidence_ref,
                "sha256": hashlib.sha256(evidence_path.read_bytes()).hexdigest(),
                "active_registry_hash": active_commands.registry_hash,
                "public_command_ids": list(COMMAND_IDS),
                "assertions": [
                    {"pointer": "/status", "equals": "passed"},
                    {"pointer": "/historical_obligation_count", "equals": 41},
                    {"pointer": "/claims/public_to_real_ue", "equals": True},
                    {"pointer": "/claims/persistence", "equals": True},
                    {"pointer": "/claims/independent_readback", "equals": True},
                    {
                        "pointer": "/claims/historical_semantics_covered",
                        "equals": True,
                    },
                    {"pointer": "/claims/old_public_ids_absent", "equals": True},
                    {"pointer": "/claims/cleanup_confirmed", "equals": True},
                ],
            },
        ),
    )
    assert report.row_count == 41
    assert report.obligation_fingerprint == expected_fingerprint
