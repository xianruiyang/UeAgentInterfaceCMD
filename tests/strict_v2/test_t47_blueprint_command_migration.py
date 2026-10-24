from __future__ import annotations
from pathlib import Path
from typing import Any
import hashlib
import json
import re

import pytest

from uai.commands import _BINDING_CATALOG, bind_generated_commands

METHODS = {
    "blueprint.asset.create": ("blueprint", "asset_create"),
    "blueprint.component.events.discover": ("blueprint", "component_events_discover"),
}
SUCCESSOR_COMMANDS = {
    "job.compile_build",
    "operation.status",
    "operation.receipt",
    "operation.release",
    "graph.view.read",
    "graph.view.update",
    "viewport.state.read",
    "viewport.state.update",
}
class _FakeClient:
    def __init__(self): self.calls: list[tuple[str,dict[str,Any],str]]=[]
    def execute_exact(self,command_id,params,*,contract_hash): self.calls.append((command_id,dict(params),contract_hash)); return {"ok":True}
    def execute(self,command_id,params):
        binding=_BINDING_CATALOG.find(command_id); assert binding is not None
        return self.execute_exact(command_id,params,contract_hash=binding.binding_hash)
def _bindings():
    values={cid:_BINDING_CATALOG.find(cid) for cid in METHODS}
    assert all(b is not None and (b.namespace,b.method)==METHODS[cid] and re.fullmatch(r"sha256:[0-9a-f]{64}",b.binding_hash) and b.binding_hash!="sha256:"+"0"*64 for cid,b in values.items()); return values
def _params(b):
    samples={"string":"fixture","integer":1,"number":1.0,"boolean":True,"array":[],"object":{}}
    return {p.name:samples.get(p.wire_type,{}) for p in b.parameters}
