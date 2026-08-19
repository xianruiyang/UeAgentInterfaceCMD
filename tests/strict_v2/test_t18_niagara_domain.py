from __future__ import annotations

from pathlib import Path
import re
from typing import Any

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_BINDINGS = {
    "niagara.module.candidates": ("niagara", "module_candidates"),
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

    def execute_exact(
        self,
        command_id: str,
        params: dict[str, Any],
        *,
        contract_hash: str,
    ) -> dict[str, bool]:
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id: str, params: dict[str, Any]):
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def test_t18_uses_only_default_niagara_and_content_graph_bindings() -> None:
    for command_id, expected_projection in COMMAND_BINDINGS.items():
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        assert (binding.namespace, binding.method) == expected_projection
        assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)


def test_t18_default_candidate_preserves_exact_public_identity() -> None:
    client = _RecordingClient()
    bind_generated_commands(client).niagara.module_candidates(
        "/Game/UAI/NS_T18.NS_T18",
        "particle_spawn",
        query="Initialize Particle",
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "niagara.module.candidates"
    assert params == {
        "target": "/Game/UAI/NS_T18.NS_T18",
        "target_usage": "particle_spawn",
        "query": "Initialize Particle",
    }
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t18_default_hjson_import_forwards_one_exact_document() -> None:
    client = _RecordingClient()
    document = (
        '{schema:"uai.niagara.edit/1",'
        'root:{type:"/Script/Niagara.NiagaraSystem",stack_edits:[]}}'
    )
    bind_generated_commands(client).content_graph.import_workspace(
        "/Game/UAI/NS_T18",
        {"kind": "inline", "document": document},
        "native-revision:t18",
        "auth:t18:test",
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.import_workspace"
    assert params == {
        "target": "/Game/UAI/NS_T18",
        "source": {"kind": "inline", "document": document},
        "expected_revision": "native-revision:t18",
        "authorization_id": "auth:t18:test",
    }
    assert contract_hash == BINDING_CATALOG.find(command_id).binding_hash


def test_t18_default_bindings_contain_no_niagara_or_recursive_business() -> None:
    commands = bind_generated_commands(_RecordingClient())
    names = set(commands.niagara.module_candidates.__func__.__code__.co_names)
    names.update(
        commands.content_graph.import_workspace.__func__.__code__.co_names
    )
    assert not {
        "niagara",
        "module",
        "recursive",
        "initialization",
        "compile",
        "save",
        "reload",
        "cleanup",
    } & names


def test_t18_replaced_niagara_hjson_bindings_are_absent() -> None:
    assert BINDING_CATALOG.find("niagara.script.graph.apply") is None
    assert BINDING_CATALOG.find("niagara.stack.apply") is None
    commands = bind_generated_commands(_RecordingClient())
    assert not hasattr(commands.niagara, "script_graph_apply")
    assert not hasattr(commands.niagara, "stack_apply")


def test_t18_task_helper_and_tutorial_authority_are_retired() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    project = cmd_root.parent
    assert not (
        cmd_root / "cli/uai/generated_commands/t18_niagara_domain"
    ).exists()
    docs = (
        cmd_root / "docs/active/t18_niagara_domain.md",
        project / "Plugins/UeAgentInterface/docs/active/t18_niagara_domain.md",
    )
    for document in docs:
        text = document.read_text(encoding="utf-8")
        assert "client.niagara.module_candidates" in text
        assert "client.content_graph.import_workspace" in text
        assert "command_search" in text and "command_detail" in text
        assert "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert "uai.generated_commands" not in text
    registration = (
        project
        / "Plugins/UeAgentInterface/Source/UeAgentInterface/Private/Module/CommandRegistration/Niagara/UeAgentNiagaraDomainRegistration.cpp"
    ).read_text(encoding="utf-8")
    assert 'Result.PythonNamespace = TEXT("niagara")' in registration
    assert 'Result.PythonFunction = TEXT("module_candidates")' in registration
