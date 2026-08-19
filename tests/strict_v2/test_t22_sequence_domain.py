from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = (
    "content_graph.import_workspace",
    "content_graph.structure",
    "content_graph.export_workspace",
)


class _Client:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id, params):
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(command_id, params, contract_hash=binding.binding_hash)


def _bindings():
    bindings = {command_id: BINDING_CATALOG.find(command_id) for command_id in COMMAND_IDS}
    assert all(
        binding is not None
        and binding.namespace == "content_graph"
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        for binding in bindings.values()
    )
    return bindings


def test_t22_uses_the_three_default_content_graph_bindings() -> None:
    bindings = _bindings()
    assert {binding.method for binding in bindings.values()} == {
        "import_workspace", "structure", "export_workspace"
    }


def test_t22_named_structure_forwards_one_exact_request() -> None:
    _bindings()
    client = _Client()
    bind_generated_commands(client).content_graph.structure("/Game/UAI/StrictV2/T22.Sequence")
    assert len(client.calls) == 1
    assert client.calls[0][0] == "content_graph.structure"
    assert client.calls[0][1] == {"target": "/Game/UAI/StrictV2/T22.Sequence"}


def test_t22_default_binding_contains_no_sequence_business() -> None:
    method = bind_generated_commands(_Client()).content_graph.structure
    assert not {"sequence", "track", "section", "channel", "key", "save", "reload"} & set(
        method.__func__.__code__.co_names
    )


def test_t22_task_projection_and_tutorial_authority_exit() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    helper = cmd_root / "cli/uai/generated_commands/t22_sequence_domain"
    assert not helper.exists()
    docs = (
        cmd_root / "docs/active/t22_sequence_domain.md",
        cmd_root.parent / "Plugins/UeAgentInterface/docs/active/t22_sequence_domain.md",
    )
    for document in docs:
        text = document.read_text(encoding="utf-8")
        for method in (
            "client.content_graph.import_workspace",
            "client.content_graph.structure",
            "client.content_graph.export_workspace",
        ):
            assert method in text
        assert "command_search" in text and "command_detail" in text and "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert "uai.generated_commands" not in text
