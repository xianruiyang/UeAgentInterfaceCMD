from __future__ import annotations

from pathlib import Path
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_BINDINGS = {
    "animation_rig_graph.candidates": ("animation_rig_graph", "candidates"),
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


def test_t24_uses_only_default_rig_and_content_graph_bindings() -> None:
    for command_id, expected_projection in COMMAND_BINDINGS.items():
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        assert (binding.namespace, binding.method) == expected_projection
        assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)


def test_t24_default_candidate_forwards_compact_search_and_exact_id() -> None:
    client = _RecordingClient()
    bind_generated_commands(client).animation_rig_graph.candidates(
        "/Game/UAI/Rig_T24.Rig_T24",
        query="Add Spaces",
        id="candidate:t24",
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "animation_rig_graph.candidates"
    assert params == {
        "target": "/Game/UAI/Rig_T24.Rig_T24",
        "query": "Add Spaces",
        "id": "candidate:t24",
    }
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t24_default_hjson_import_forwards_one_exact_source_union() -> None:
    client = _RecordingClient()
    document = (
        '{schema:"uai.animation_rig_graph.edit/1",'
        'root:{type:"/Script/ControlRigDeveloper.ControlRigBlueprint",operation:{}}}'
    )
    bind_generated_commands(client).content_graph.import_workspace(
        "/Game/UAI/Rig_T24",
        {"kind": "inline", "document": document},
        "native-revision:t24",
        "auth:t24:test",
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.import_workspace"
    assert params == {
        "target": "/Game/UAI/Rig_T24",
        "source": {"kind": "inline", "document": document},
        "expected_revision": "native-revision:t24",
        "authorization_id": "auth:t24:test",
    }
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t24_default_bindings_contain_no_rig_or_recursive_business() -> None:
    commands = bind_generated_commands(_RecordingClient())
    names = set(commands.animation_rig_graph.candidates.__func__.__code__.co_names)
    names.update(commands.content_graph.import_workspace.__func__.__code__.co_names)
    assert not {
        "rigvm",
        "control_rig",
        "ik_rig",
        "skeleton",
        "recursive",
        "initialization",
        "compile",
        "save",
        "reload",
        "cleanup",
    } & names


def test_t24_task_helper_and_tutorial_authority_are_retired() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    project = cmd_root.parent
    assert not (
        cmd_root / "cli/uai/generated_commands/t24_animation_rig_graph_domain"
    ).exists()
    docs = (
        cmd_root / "docs/active/t24_animation_rig_graph_domain.md",
        project
        / "Plugins/UeAgentInterface/docs/active/t24_animation_rig_graph_domain.md",
    )
    for document in docs:
        text = document.read_text(encoding="utf-8")
        assert "client.animation_rig_graph.candidates" in text
        assert "client.content_graph.import_workspace" in text
        assert "command_search" in text and "command_detail" in text
        assert "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert "uai.generated_commands" not in text
    registration = (
        project
        / "Plugins/UeAgentInterface/Source/UeAgentInterface/Private/Module/CommandRegistration/AnimationRigGraph/UeAgentAnimationRigGraphDomainRegistration.cpp"
    ).read_text(encoding="utf-8")
    assert 'Result.PythonNamespace = TEXT("animation_rig_graph")' in registration
    assert 'Result.PythonFunction = TEXT("candidates")' in registration
