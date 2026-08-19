from __future__ import annotations

from pathlib import Path
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_BINDINGS = {
    "blueprint.component.candidates": ("blueprint", "component_candidates"),
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


def test_t26_uses_only_default_component_and_content_graph_bindings() -> None:
    for command_id, expected_projection in COMMAND_BINDINGS.items():
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        assert (binding.namespace, binding.method) == expected_projection
        assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)


def test_t26_default_shared_import_forwards_explicit_space_document() -> None:
    client = _RecordingClient()
    document = (
        '{schema:"uai.world.edit/1",root:{type:"/Script/Engine.World",'
        'document:{operation:update,target:{asset_path:"/Game/UAI/LV_T26"},'
        'provider_extension:{frame:{dimension:3,semantic_frame:"ue_world",'
        'write_frame:"ue_world",read_frame:"ue_world",unit:"centimeter"},'
        'actors:[]}}}}'
    )
    bind_generated_commands(client).content_graph.import_workspace(
        "/Game/UAI/LV_T26.LV_T26",
        {"kind": "inline", "document": document},
        "content-graph:t26",
        authorization_id="auth:t26:test",
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.import_workspace"
    assert params == {
        "target": "/Game/UAI/LV_T26.LV_T26",
        "source": {"kind": "inline", "document": document},
        "expected_revision": "content-graph:t26",
        "authorization_id": "auth:t26:test",
    }
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t26_default_candidate_and_readback_routes_preserve_identities() -> None:
    client = _RecordingClient()
    target = "/Game/UAI/LV_T26.LV_T26"
    commands = bind_generated_commands(client)
    commands.content_graph.diagnostics(target)
    commands.blueprint.component_candidates(
        target=target,
        component_class="/Script/Engine.SceneComponent",
        requested_name="EvidenceSceneT26",
    )
    commands.content_graph.structure(target)
    assert [call[0] for call in client.calls] == [
        "content_graph.diagnostics",
        "blueprint.component.candidates",
        "content_graph.structure",
    ]
    assert client.calls[1][1] == {
        "target": target,
        "component_class": "/Script/Engine.SceneComponent",
        "requested_name": "EvidenceSceneT26",
    }


def test_t26_default_bindings_contain_no_world_or_recursive_business() -> None:
    commands = bind_generated_commands(_RecordingClient())
    names = set(commands.blueprint.component_candidates.__func__.__code__.co_names)
    names.update(commands.content_graph.import_workspace.__func__.__code__.co_names)
    assert not {
        "uworld",
        "spawnactor",
        "data_layer",
        "recursive",
        "initialization",
        "save",
        "reload",
        "cleanup",
    } & names


def test_t26_task_helper_and_tutorial_authority_are_retired() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    project = cmd_root.parent
    assert not (
        cmd_root / "cli/uai/generated_commands/t26_level_world_domain"
    ).exists()
    docs = (
        cmd_root / "docs/active/t26_level_world_domain.md",
        project / "Plugins/UeAgentInterface/docs/active/t26_level_world_domain.md",
    )
    for document in docs:
        text = document.read_text(encoding="utf-8")
        assert "client.blueprint.component_candidates" in text
        assert "client.content_graph.import_workspace" in text
        assert "client.content_graph.diagnostics" in text
        assert "command_search" in text and "command_detail" in text
        assert "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert (
            "do not use or invent `level_apply_folder`" in text
            or "There is no `level_apply_folder`" in text
        )
        assert "uai.generated_commands" not in text


def test_t26_has_no_domain_specific_hjson_ingress() -> None:
    for command_id in (
        "level_apply_folder",
        "level.apply_folder",
        "level.apply_file",
        "world.authoring.apply",
    ):
        assert BINDING_CATALOG.find(command_id) is None
