from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

import pytest

from uai.commands import _BINDING_CATALOG, bind_generated_commands


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
DORMANT_IDS = frozenset(
    {
        "animation.deformer_graph.topology.apply",
        "animation.deformer_source_library.bindings.apply",
        "animation.mesh_deformer_collection.entries.apply",
        "animation.ml_deformer.configuration.apply",
        "physics.asset.structure.replace",
        "physics.constraint.update",
        "physics.material.update",
    }
)
DISABLED_IDS = frozenset(
    {
        "animation.deformer_source_library.asset.create",
        "animation.ml_deformer.asset.create",
    }
)
ACTIVE_COMMAND_IDS = tuple(
    command_id
    for command_id in COMMAND_IDS
    if command_id not in DORMANT_IDS and command_id not in DISABLED_IDS
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
        binding = _BINDING_CATALOG.find(command_id)
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
        command_id: _BINDING_CATALOG.find(command_id)
        for command_id in ACTIVE_COMMAND_IDS
    }
    assert all(
        binding is not None
        and (binding.namespace, binding.method) == DEFAULT_METHODS[command_id]
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def _require_dormant_bindings():
    bindings = {command_id: _BINDING_CATALOG.find(command_id) for command_id in DORMANT_IDS}
    assert all(binding is not None and binding.status == "dormant" for binding in bindings.values())
    generated = bind_generated_commands(_FakeClient())
    for binding in bindings.values():
        namespace = getattr(generated, binding.namespace)
        with pytest.raises(AttributeError):
            getattr(namespace, binding.method)
    return bindings


def _require_disabled_bindings():
    bindings = {
        command_id: _BINDING_CATALOG.find(command_id)
        for command_id in DISABLED_IDS
    }
    assert all(
        binding is not None and binding.status == "disabled"
        for binding in bindings.values()
    )
    generated = bind_generated_commands(_FakeClient())
    for binding in bindings.values():
        namespace = getattr(generated, binding.namespace)
        with pytest.raises(AttributeError):
            getattr(namespace, binding.method)
    return bindings


def _params(binding) -> dict[str, Any]:
    return {parameter.name: _dummy(parameter.wire_type) for parameter in binding.parameters}


def _named_call(client: _FakeClient, binding, params: dict[str, Any]) -> None:
    namespace = getattr(bind_generated_commands(client), binding.namespace)
    method = getattr(namespace, binding.method)
    method(**params)


def test_hjson_operations_are_dormant_and_have_no_named_sdk_method() -> None:
    _require_dormant_bindings()


def test_unavailable_create_families_are_disabled_without_named_sdk_methods() -> None:
    _require_disabled_bindings()
