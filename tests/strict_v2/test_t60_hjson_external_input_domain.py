from __future__ import annotations

from pathlib import Path
import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = ("content_graph.import_workspace", "content_graph.export_workspace")


class FakeClient:
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


def _bindings():
    bindings = {command_id: _BINDING_CATALOG.find(command_id) for command_id in COMMAND_IDS}
    assert all(
        binding is not None
        and binding.namespace == "content_graph"
        and binding.method in {"import_workspace", "export_workspace"}
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        for binding in bindings.values()
    )
    return bindings


