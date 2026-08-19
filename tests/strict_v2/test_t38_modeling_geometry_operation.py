from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = (
    "mesh.modeling_session",
    "mesh.attribute.material_slot.add",
    "mesh.attribute.material_slot.assign",
    "mesh.attribute.normals.recompute",
    "mesh.attribute.uv.auto",
    "mesh.attribute.uv.project",
    "mesh.collision.convex.generate",
    "mesh.collision.simple.generate",
    "mesh.primitive.box.create",
    "mesh.primitive.cylinder.create",
    "mesh.primitive.plane.create",
    "mesh.primitive.ramp.create",
    "mesh.primitive.ramp_corner.create",
    "mesh.primitive.sphere.create",
    "mesh.primitive.stairs.create",
    "mesh.topology.boolean",
    "mesh.topology.edges.bevel",
    "mesh.topology.edges.weld",
    "mesh.topology.faces.duplicate",
    "mesh.topology.faces.extrude",
    "mesh.topology.faces.inset",
    "mesh.topology.faces.offset",
    "mesh.topology.faces.push_pull",
    "mesh.topology.holes.fill",
    "mesh.topology.mesh_cut",
    "mesh.topology.mirror",
    "mesh.topology.plane_cut",
    "mesh.topology.remesh",
    "mesh.topology.simplify",
    "mesh.topology.subdivide",
    "mesh.topology.trim",
    "mesh.topology.voxel_boolean",
)


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
        and binding.namespace == "mesh"
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def _box_params() -> dict[str, Any]:
    return {
        "anchor": "center",
        "placement": {
            "location_cm": [0.0, 0.0, 0.0],
            "rotation_deg": [0.0, 0.0, 0.0],
        },
        "size_cm": [100.0, 100.0, 100.0],
        "subdivisions": [1, 1, 1],
        "target_ref": "/Game/StrictV2/T38/SM_Default.SM_Default",
    }


def test_all_32_mesh_commands_have_exact_default_bindings() -> None:
    assert len(COMMAND_IDS) == 32
    _require_bindings()


def test_default_box_create_preserves_the_exact_request() -> None:
    _require_bindings()
    client = _FakeClient()
    params = _box_params()
    bind_generated_commands(client).mesh.primitive_box_create(**params)
    assert client.calls[0][0] == "mesh.primitive.box.create"
    assert client.calls[0][1] == params


def test_modeling_session_uses_one_exact_action_discriminator() -> None:
    _require_bindings()
    client = _FakeClient()
    params = {
        "action": "observe_tool",
        "target": "modeling-session:current",
        "input": {},
        "context": {"world_type": "editor"},
        "projection": {"include_properties": True},
    }
    bind_generated_commands(client).mesh.modeling_session(**params)
    assert client.calls[0][0] == "mesh.modeling_session"
    assert client.calls[0][1] == params


def test_named_and_generic_box_create_use_the_same_exact_binding() -> None:
    bindings = _require_bindings()
    named = _FakeClient()
    generic = _FakeClient()
    params = _box_params()
    bind_generated_commands(named).mesh.primitive_box_create(**params)
    generic.execute_exact(
        "mesh.primitive.box.create",
        params,
        contract_hash=bindings["mesh.primitive.box.create"].binding_hash,
    )
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_ue_business_logic() -> None:
    _require_bindings()
    method = bind_generated_commands(_FakeClient()).mesh.primitive_box_create
    names = set(method.__func__.__code__.co_names)
    assert not {
        "requests",
        "httpx",
        "urllib",
        "retry",
        "sleep",
        "registry",
        "mesh",
        "save",
        "reload",
        "rollback",
    } & names


def test_t38_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = (
        cmd_root
        / "cli"
        / "uai"
        / "generated_commands"
        / "t38_modeling_geometry_operation"
    )
    task_doc = cmd_root / "docs" / "active" / "t38_modeling_geometry_operation.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t38_modeling_geometry_operation.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.mesh.primitive_box_create" in text
        assert "client.mesh.topology_mirror" in text
        assert "command_search" in text
        assert "command_detail" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text


def test_modeling_session_receives_an_injected_native_mechanics_port() -> None:
    project_root = Path(__file__).resolve().parents[2].parent
    plugin_private = (
        project_root
        / "Plugins"
        / "UeAgentInterface"
        / "Source"
        / "UeAgentInterface"
        / "Private"
    )
    handler = (
        plugin_private
        / "CommandHandlers"
        / "ModelingGeometry"
        / "UeAgentModelingGeometryCommandHandlers.cpp"
    ).read_text(encoding="utf-8")
    boundary = (
        plugin_private
        / "DomainAdapters"
        / "ModelingGeometry"
        / "UeAgentModelingGeometryMechanicsBoundary.h"
    ).read_text(encoding="utf-8")
    registration = (
        plugin_private
        / "Module"
        / "CommandRegistration"
        / "ModelingGeometry"
        / "UeAgentModelingGeometryRegistration.cpp"
    ).read_text(encoding="utf-8")

    assert "IUeAgentModelingSessionNativeMechanicsPort" in boundary
    assert "CreateModelingSessionNativeMechanicsPort" in boundary
    assert "CreateModelingSessionNativeMechanicsPort()" in registration
    assert re.search(
        r"TryCreateHandlers\(\s*NativeMechanicsPort\s*,", registration
    )
    assert 'Server/UeAgentHttpServer.h' not in handler
    assert "FUeAgentHttpServer NativePort" not in handler
