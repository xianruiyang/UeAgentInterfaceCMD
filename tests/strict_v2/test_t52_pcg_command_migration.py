from __future__ import annotations
from pathlib import Path
import re
from uai.commands import _BINDING_CATALOG,bind_generated_commands
METHODS={
    "pcg.component.apply": ("pcg", "component_apply"),
    "pcg.component.world_binding.apply": ("pcg", "component_world_binding_apply"),
    "pcg.data_asset.apply": ("pcg", "data_asset_apply"),
    "pcg.data_asset.create_from_level": ("pcg", "data_asset_create_from_level"),
    "pcg.generated_spatial_data.read": ("pcg", "generated_spatial_data_read"),
    "pcg.graph_instance.apply": ("pcg", "graph_instance_apply"),
    "pcg.partition.spatial_state.read": ("pcg", "partition_spatial_state_read"),
}
SLEEP_COMMAND_IDS={
    "pcg.component.apply",
    "pcg.component.world_binding.apply",
    "pcg.data_asset.apply",
    "pcg.graph_instance.apply",
}
KEEP_COMMAND_IDS={
    "pcg.data_asset.create_from_level",
    "pcg.generated_spatial_data.read",
    "pcg.partition.spatial_state.read",
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

def test_t52_sleep_commands_are_dormant_and_not_named_sdk():
 bindings=_bindings(); namespaces=bind_generated_commands(_FakeClient())
 for cid in SLEEP_COMMAND_IDS:
  assert bindings[cid].status=="dormant"
  assert not hasattr(namespaces.pcg, bindings[cid].method)

def test_t52_non_hjson_commands_remain_active_named_sdk():
 bindings=_bindings(); namespaces=bind_generated_commands(_FakeClient())
 for cid in KEEP_COMMAND_IDS:
  assert bindings[cid].status=="active"
  assert hasattr(namespaces.pcg, bindings[cid].method)
