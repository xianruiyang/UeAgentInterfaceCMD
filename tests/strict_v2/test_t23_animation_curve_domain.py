from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands

COMMAND_IDS = ("content_graph.import_workspace", "content_graph.structure", "content_graph.export_workspace")

class _Client:
    def __init__(self): self.calls: list[tuple[str, dict[str, Any], str]] = []
    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash)); return {"ok": True}
    def execute(self, command_id, params):
        binding = BINDING_CATALOG.find(command_id); assert binding is not None
        return self.execute_exact(command_id, params, contract_hash=binding.binding_hash)

def _bindings():
    values = {cid: BINDING_CATALOG.find(cid) for cid in COMMAND_IDS}
    assert all(v is not None and v.namespace == "content_graph" and re.fullmatch(r"sha256:[0-9a-f]{64}", v.binding_hash) for v in values.values())
    return values

def test_t23_uses_the_three_default_content_graph_bindings() -> None:
    assert {v.method for v in _bindings().values()} == {"import_workspace", "structure", "export_workspace"}

def test_t23_named_structure_forwards_one_exact_request() -> None:
    client = _Client(); bind_generated_commands(client).content_graph.structure("/Game/UAI/StrictV2/T23.Curve")
    assert len(client.calls) == 1 and client.calls[0][0] == "content_graph.structure"

def test_t23_default_binding_contains_no_curve_business() -> None:
    names = set(bind_generated_commands(_Client()).content_graph.structure.__func__.__code__.co_names)
    assert not {"curve", "channel", "key", "notify", "compress", "save", "reload"} & names

def test_t23_task_projection_and_tutorial_authority_exit() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    assert not (cmd_root / "cli/uai/generated_commands/t23_animation_curve_domain").exists()
    docs = (cmd_root / "docs/active/t23_animation_curve_domain.md", cmd_root.parent / "Plugins/UeAgentInterface/docs/active/t23_animation_curve_domain.md")
    for document in docs:
        text = document.read_text(encoding="utf-8")
        for method in ("client.content_graph.import_workspace", "client.content_graph.structure", "client.content_graph.export_workspace"): assert method in text
        assert "command_search" in text and "command_detail" in text and "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert "uai.generated_commands" not in text
