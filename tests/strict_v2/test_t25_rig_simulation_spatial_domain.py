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


def test_t25_uses_only_default_content_graph_bindings() -> None:
    for command_id, expected_projection in COMMAND_BINDINGS.items():
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        assert (binding.namespace, binding.method) == expected_projection
        assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)


def test_t25_default_import_preserves_frame_and_operation_fences() -> None:
    client = _RecordingClient()
    target = (
        "/Game/Maps/WB_WhiteBox01.WB_WhiteBox01:"
        "PersistentLevel.UAI_T25_Pose"
    )
    document = (
        '{schema:"uai.rig_simulation_spatial.edit/1",'
        'root:{type:"/Script/Engine.PoseableMeshComponent",'
        'operation:{kind:"update_runtime_pose"}}}'
    )
    bind_generated_commands(client).content_graph.import_workspace(
        target,
        {"kind": "inline", "document": document},
        "runtime:1",
        "auth:t25:test",
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.import_workspace"
    assert params == {
        "target": target,
        "source": {"kind": "inline", "document": document},
        "expected_revision": "runtime:1",
        "authorization_id": "auth:t25:test",
    }
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t25_default_structure_preserves_runtime_subject_identity() -> None:
    client = _RecordingClient()
    target = (
        "/Game/Maps/WB_WhiteBox01.WB_WhiteBox01:"
        "PersistentLevel.UAI_T25_Pose"
    )
    bind_generated_commands(client).content_graph.structure(target)
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.structure"
    assert params == {"target": target}
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t25_default_bindings_contain_no_pose_or_recursive_business() -> None:
    commands = bind_generated_commands(_RecordingClient())
    names = set(commands.content_graph.import_workspace.__func__.__code__.co_names)
    names.update(commands.content_graph.structure.__func__.__code__.co_names)
    assert not {
        "poseable_mesh",
        "bone_transform",
        "simulation",
        "recursive",
        "initialization",
        "save",
        "reload",
        "cleanup",
    } & names


def test_t25_task_helper_and_tutorial_authority_are_retired() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    project = cmd_root.parent
    assert not (
        cmd_root / "cli/uai/generated_commands/t25_rig_simulation_spatial_domain"
    ).exists()
    docs = (
        cmd_root / "docs/active/t25_rig_simulation_spatial_domain.md",
        project
        / "Plugins/UeAgentInterface/docs/active/t25_rig_simulation_spatial_domain.md",
    )
    for document in docs:
        text = document.read_text(encoding="utf-8")
        assert "client.content_graph.import_workspace" in text
        assert "client.content_graph.structure" in text
        assert "command_search" in text and "command_detail" in text
        assert "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert "runtime_non_persistent" in text
        assert "uai.generated_commands" not in text
