from __future__ import annotations

from pathlib import Path
import re
from typing import Any

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_BINDINGS = {
    "pcg.node.candidates": ("pcg", "node_candidates"),
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
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id, params):
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            command_id, params, contract_hash=binding.binding_hash
        )


def test_t19_uses_only_default_pcg_and_content_graph_bindings() -> None:
    for command_id, expected_projection in COMMAND_BINDINGS.items():
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        assert (binding.namespace, binding.method) == expected_projection
        assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)


def test_t19_default_candidate_preserves_exact_public_identity() -> None:
    client = _RecordingClient()
    bind_generated_commands(client).pcg.node_candidates(
        "/Game/UAI/PCG_T19.PCG_T19", query="Point"
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "pcg.node.candidates"
    assert params == {"target": "/Game/UAI/PCG_T19.PCG_T19", "query": "Point"}
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t19_default_hjson_import_forwards_one_exact_source_union() -> None:
    client = _RecordingClient()
    document = (
        '{schema:"uai.pcg.edit/1",'
        'root:{type:"/Script/PCG.PCGGraph",operation:{}}}'
    )
    bind_generated_commands(client).content_graph.import_workspace(
        "/Game/UAI/PCG_T19",
        {"kind": "inline", "document": document},
        "native-revision:t19",
        "auth:t19:test",
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.import_workspace"
    assert params == {
        "target": "/Game/UAI/PCG_T19",
        "source": {"kind": "inline", "document": document},
        "expected_revision": "native-revision:t19",
        "authorization_id": "auth:t19:test",
    }
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t19_default_bindings_contain_no_pcg_or_recursive_business() -> None:
    commands = bind_generated_commands(_RecordingClient())
    names = set(commands.pcg.node_candidates.__func__.__code__.co_names)
    names.update(commands.content_graph.import_workspace.__func__.__code__.co_names)
    assert not {
        "pcg",
        "node",
        "recursive",
        "initialization",
        "compile",
        "save",
        "reload",
        "cleanup",
    } & names


def test_t19_task_helper_and_tutorial_authority_are_retired() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    project = cmd_root.parent
    assert not (cmd_root / "cli/uai/generated_commands/t19_pcg_domain").exists()
    docs = (
        cmd_root / "docs/active/t19_pcg_domain.md",
        project / "Plugins/UeAgentInterface/docs/active/t19_pcg_domain.md",
    )
    for document in docs:
        text = document.read_text(encoding="utf-8")
        assert "client.pcg.node_candidates" in text
        assert "client.content_graph.import_workspace" in text
        assert "command_search" in text and "command_detail" in text
        assert "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert "uai.generated_commands" not in text
    registration = (
        project
        / "Plugins/UeAgentInterface/Source/UeAgentInterface/Private/Module/CommandRegistration/Pcg/UeAgentPcgDomainRegistration.cpp"
    ).read_text(encoding="utf-8")
    assert 'Result.PythonNamespace = TEXT("pcg")' in registration
    assert 'Result.PythonFunction = TEXT("node_candidates")' in registration
