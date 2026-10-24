from __future__ import annotations
from pathlib import Path
import re
from uai.commands import _BINDING_CATALOG,bind_generated_commands
METHODS={
    "ai.behavior_tree.asset.create": ("ai", "behavior_tree_asset_create"),
    "ai.blackboard.asset.create": ("ai", "blackboard_asset_create"),
    "ai.eqs.asset.create": ("ai", "eqs_asset_create"),
    "ai.smart_object_definition.asset.create": ("ai", "smart_object_definition_asset_create"),
    "ai.state_tree.asset.create": ("ai", "state_tree_asset_create"),
}
INTERNAL_APPLY_IDS={
    "ai.behavior_tree.graph.apply",
    "ai.blackboard.schema.apply",
    "ai.eqs.graph.apply",
    "ai.smart_object_definition.apply",
    "ai.state_tree.hierarchy.apply",
}
class _FakeClient:
 def __init__(self):self.calls=[]
 def execute_exact(self,command_id,params,*,contract_hash):self.calls.append((command_id,dict(params),contract_hash));return {"ok":True}
 def execute(self,command_id,params):
  b=_BINDING_CATALOG.find(command_id);assert b is not None;return self.execute_exact(command_id,params,contract_hash=b.binding_hash)
def _bindings():
 v={cid:_BINDING_CATALOG.find(cid) for cid in METHODS};assert all(b is not None and (b.namespace,b.method)==METHODS[cid] and re.fullmatch(r"sha256:[0-9a-f]{64}",b.binding_hash) and b.binding_hash!="sha256:"+"0"*64 for cid,b in v.items());return v
def _params(b):
 s={"string":"fixture","integer":1,"number":1.0,"boolean":True,"array":[],"object":{}};return {p.name:s.get(p.wire_type,{}) for p in b.parameters}
