from __future__ import annotations

from pathlib import Path
import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands


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
    "world.actor.candidates": ("world", "actor_candidates"),
}


class _RecordingClient:
    def __init__(self):
        self.calls = []

    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id, params):
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            command_id, params, contract_hash=binding.binding_hash
        )


def test_t26_has_no_domain_specific_hjson_ingress() -> None:
    for command_id in (
        "level_apply_folder",
        "level.apply_folder",
        "level.apply_file",
        "world.authoring.apply",
    ):
        assert _BINDING_CATALOG.find(command_id) is None
