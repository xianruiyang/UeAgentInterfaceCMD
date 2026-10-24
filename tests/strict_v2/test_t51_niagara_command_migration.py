from __future__ import annotations
from pathlib import Path
import re
from uai.commands import _BINDING_CATALOG,bind_generated_commands
METHODS={
    "niagara.asset.duplicate": ("niagara", "asset_duplicate"),
    "niagara.compile_refresh_settle": ("niagara", "compile_refresh_settle"),
    "niagara.compound.apply": ("niagara", "compound_apply"),
    "niagara.emitter.asset.create": ("niagara", "emitter_asset_create"),
    "niagara.stack.issue_fix": ("niagara", "stack_issue_fix"),
    "niagara.system.asset.create": ("niagara", "system_asset_create"),
}
SLEEP_COMMAND_IDS={
    "niagara.compound.apply",
}
KEEP_COMMAND_IDS={
    "niagara.asset.duplicate",
    "niagara.compile_refresh_settle",
    "niagara.emitter.asset.create",
    "niagara.stack.issue_fix",
    "niagara.system.asset.create",
}
class _FakeClient:
 def __init__(self):self.calls=[]
 def execute_exact(self,command_id,params,*,contract_hash):self.calls.append((command_id,dict(params),contract_hash));return {"ok":True}
 def execute(self,command_id,params):
  b=_BINDING_CATALOG.find(command_id);assert b is not None;return self.execute_exact(command_id,params,contract_hash=b.binding_hash)
def _bindings():
 v={cid:_BINDING_CATALOG.find(cid) for cid in METHODS};assert all(b is not None and (b.namespace,b.method)==METHODS[cid] and re.fullmatch(r"sha256:[0-9a-f]{64}",b.binding_hash) and b.binding_hash!="sha256:"+"0"*64 for cid,b in v.items());assert all(v[cid].status=="dormant" for cid in SLEEP_COMMAND_IDS);assert all(v[cid].status=="active" for cid in KEEP_COMMAND_IDS);return v
def _params(b):
 s={"string":"fixture","integer":1,"number":1.0,"boolean":True,"array":[],"object":{}};return {p.name:s.get(p.wire_type,{}) for p in b.parameters}

def test_t51_sleep_commands_are_dormant_and_not_named_sdk():
 bindings=_bindings(); namespaces=bind_generated_commands(_FakeClient())
 for cid in SLEEP_COMMAND_IDS:
  assert bindings[cid].status=="dormant"
  assert not hasattr(namespaces.niagara, bindings[cid].method)

def test_t51_non_hjson_command_remains_active_named_sdk():
 bindings=_bindings(); namespaces=bind_generated_commands(_FakeClient())
 for cid in KEEP_COMMAND_IDS:
  assert bindings[cid].status=="active"
  assert hasattr(namespaces.niagara, bindings[cid].method)
