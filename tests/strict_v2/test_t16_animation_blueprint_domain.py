from __future__ import annotations

from pathlib import Path
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_BINDINGS = {
    "content_graph.compound": ("content_graph", "compound"),
    "content_graph.diagnostics": ("content_graph", "diagnostics"),
    "content_graph.export_workspace": ("content_graph", "export_workspace"),
    "content_graph.import_workspace": ("content_graph", "import_workspace"),
    "content_graph.items": ("content_graph", "items"),
    "content_graph.properties": ("content_graph", "properties"),
    "content_graph.relations": ("content_graph", "relations"),
    "content_graph.structure": ("content_graph", "structure"),
    "content_graph.summary": ("content_graph", "summary"),
}


class _RecordingClient:
    def __init__(self):
        self.calls = []

    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id, params):
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            command_id, params, contract_hash=binding.binding_hash
        )


def test_t16_uses_only_default_animation_blueprint_bindings() -> None:
    for command_id, expected_projection in COMMAND_BINDINGS.items():
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        assert (binding.namespace, binding.method) == expected_projection
        assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)


def test_t16_default_domain_ingress_forwards_exact_create_source() -> None:
    client = _RecordingClient()
    document = (
        '{schema:"uai.animation_blueprint.edit/1",'
        'root:{type:"/Script/Engine.AnimBlueprint",'
        'document:{operation:create,target:{asset_path:"/Game/UAI/ABP_T16"},'
        'provider_extension:{class_settings:{},blueprint_surfaces:{},'
        'animation_graphs:{},state_machines:{}}}}}'
    )
    bind_generated_commands(client).content_graph.import_workspace(
        "/Game/UAI/ABP_T16.ABP_T16",
        {"kind": "inline", "document": document},
        "missing",
        authorization_id="auth:t16:test",
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.import_workspace"
    assert params == {
        "target": "/Game/UAI/ABP_T16.ABP_T16",
        "source": {"kind": "inline", "document": document},
        "expected_revision": "missing",
        "authorization_id": "auth:t16:test",
    }
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t16_default_content_graph_readback_preserves_identity() -> None:
    client = _RecordingClient()
    bind_generated_commands(client).content_graph.structure(
        "/Game/UAI/ABP_T16.ABP_T16"
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.structure"
    assert params == {"target": "/Game/UAI/ABP_T16.ABP_T16"}
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t16_default_bindings_contain_no_animation_or_recursive_business() -> None:
    commands = bind_generated_commands(_RecordingClient())
    names = set(commands.content_graph.import_workspace.__func__.__code__.co_names)
    assert not {
        "uanimblueprint",
        "state_machine",
        "transition",
        "recursive",
        "initialization",
        "compile",
        "save",
        "unload",
        "reload",
        "cleanup",
    } & names


def test_t16_replaced_animation_blueprint_hjson_binding_is_absent() -> None:
    assert BINDING_CATALOG.find("animation_blueprint.authoring.apply") is None
    commands = bind_generated_commands(_RecordingClient())
    assert not hasattr(commands, "animation_blueprint") or not hasattr(
        commands.animation_blueprint, "authoring_apply"
    )


def test_t16_task_helper_and_tutorial_authority_are_retired() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    project = cmd_root.parent
    assert not (
        cmd_root / "cli/uai/generated_commands/t16_animation_blueprint_domain"
    ).exists()
    docs = (
        cmd_root / "docs/active/t16_animation_blueprint_domain.md",
        project
        / "Plugins/UeAgentInterface/docs/active/t16_animation_blueprint_domain.md",
    )
    for document in docs:
        text = document.read_text(encoding="utf-8")
        assert "client.animation_blueprint.authoring_apply" not in text
        assert "client.content_graph.import_workspace" in text
        assert "command_search" in text and "command_detail" in text
        assert "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert "uai.generated_commands" not in text
    registration = (
        project
        / "Plugins/UeAgentInterface/Source/UeAgentInterface/Private/Module/CommandRegistration/AnimationBlueprint/UeAgentAnimationBlueprintRegistration.cpp"
    ).read_text(encoding="utf-8")
    assert 'Result.PythonNamespace = TEXT("animation_blueprint")' not in registration
    assert 'Result.PythonFunction = TEXT("authoring_apply")' not in registration
