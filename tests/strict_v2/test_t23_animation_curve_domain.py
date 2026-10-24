from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands

COMMAND_IDS = ("content_graph.import_workspace", "content_graph.structure", "content_graph.export_workspace")

class _Client:
    def __init__(self): self.calls: list[tuple[str, dict[str, Any], str]] = []
    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash)); return {"ok": True}
    def execute(self, command_id, params):
        binding = _BINDING_CATALOG.find(command_id); assert binding is not None
        return self.execute_exact(command_id, params, contract_hash=binding.binding_hash)

def _bindings():
    values = {cid: _BINDING_CATALOG.find(cid) for cid in COMMAND_IDS}
    assert all(v is not None and v.namespace == "content_graph" and re.fullmatch(r"sha256:[0-9a-f]{64}", v.binding_hash) for v in values.values())
    return values

