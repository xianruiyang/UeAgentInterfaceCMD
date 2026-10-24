from __future__ import annotations

import json
from pathlib import Path
from typing import Any
import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands


EXPECTED_COMMAND_IDS = {
    "asset.collection",
    "asset.registry_record",
    "asset.registry_relations",
    "asset.relations",
    "asset.sample",
    "asset.validation",
    "config.resolved_value",
    "config.section",
    "editor.dirty_resources",
    "editor.open_assets",
    "project.platform",
    "project.settings",
    "project.summary",
    "project.validation",
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

HJSON_PRIMARY_COMMAND_IDS = {
    "asset.properties",
    "asset.summary",
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
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_bindings():
    bindings = {
        command_id: _BINDING_CATALOG.find(command_id)
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
    target = "/Game/Test.Test"
    bind_generated_commands(client).asset.registry_record(
        target,
        input={"include_tags": True},
        context={"state_plane": "persisted"},
        projection={"max_items": 7},
    )
    assert client.calls[0][0] == "asset.registry_record"
    assert client.calls[0][1] == {
        "target": target,
        "input": {"include_tags": True},
        "context": {"state_plane": "persisted"},
        "projection": {"max_items": 7},
    }


def test_active_replacements_exist_and_compatibility_queries_are_dormant() -> None:
    assert _BINDING_CATALOG.find("asset.relations") is not None
    assert _BINDING_CATALOG.find("content_graph.structure") is not None
    assert _BINDING_CATALOG.find("content_graph.items") is not None
    for command_id in (
        "asset.registry_relations",
        "world.actors",
        "world.actor_components",
        "world.property",
    ):
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None and binding.status == "dormant"


def test_hjson_primary_queries_are_dormant_without_named_methods() -> None:
    namespaces = bind_generated_commands(_RecordingClient())
    for command_id in HJSON_PRIMARY_COMMAND_IDS:
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None and binding.status == "dormant"
        namespace = getattr(namespaces, binding.namespace, None)
        if namespace is not None:
            assert not hasattr(namespace, binding.method), command_id
