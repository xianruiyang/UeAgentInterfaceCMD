from __future__ import annotations
from pathlib import Path
import re
from uai.commands import BINDING_CATALOG,bind_generated_commands
METHODS={
    "pcg.component.apply": ("pcg", "component_apply"),
    "pcg.component.world_binding.apply": ("pcg", "component_world_binding_apply"),
    "pcg.data_asset.apply": ("pcg", "data_asset_apply"),
    "pcg.data_asset.create_from_level": ("pcg", "data_asset_create_from_level"),
    "pcg.generated_spatial_data.read": ("pcg", "generated_spatial_data_read"),
    "pcg.graph.apply": ("pcg", "graph_apply"),
    "pcg.graph_instance.apply": ("pcg", "graph_instance_apply"),
    "pcg.graph_parameters.apply": ("pcg", "graph_parameters_apply"),
    "pcg.partition.spatial_state.read": ("pcg", "partition_spatial_state_read"),
}
class _FakeClient:
 def __init__(self):self.calls=[]
 def execute_exact(self,command_id,params,*,contract_hash):self.calls.append((command_id,dict(params),contract_hash));return {"ok":True}
 def execute(self,command_id,params):
  b=BINDING_CATALOG.find(command_id);assert b is not None;return self.execute_exact(command_id,params,contract_hash=b.binding_hash)
def _bindings():
 v={cid:BINDING_CATALOG.find(cid) for cid in METHODS};assert all(b is not None and (b.namespace,b.method)==METHODS[cid] and re.fullmatch(r"sha256:[0-9a-f]{64}",b.binding_hash) and b.binding_hash!="sha256:"+"0"*64 for cid,b in v.items());return v
def _params(b):
 s={"string":"fixture","integer":1,"number":1.0,"boolean":True,"array":[],"object":{}};return {p.name:s.get(p.wire_type,{}) for p in b.parameters}
def test_exact_default_inventory():assert len(METHODS)==9;_bindings()
def test_default_named_method_forwards_one_exact_request():
 b=_bindings()["pcg.graph.apply"];c=_FakeClient();p=_params(b);getattr(getattr(bind_generated_commands(c),b.namespace),b.method)(**p);assert c.calls==[(b.command_id,p,b.binding_hash)]
def test_default_projection_has_no_transport_or_pcg_business():
 b=_bindings()["pcg.graph.apply"];m=getattr(getattr(bind_generated_commands(_FakeClient()),b.namespace),b.method);assert not {"requests","httpx","urllib","retry","sleep","registry","generate","save","reload","graph","partition"}&set(m.__func__.__code__.co_names)
def test_t52_legacy_binding_and_tutorial_authority_exit():
 _bindings();root=Path(__file__).resolve().parents[2];helper=root/"cli"/"uai"/"generated_commands"/"t52_pcg_command_migration";docs=(root/"docs"/"active"/"t52_pcg_command_migration.md",root.parent/"Plugins"/"UeAgentInterface"/"docs"/"active"/"t52_pcg_command_migration.md");assert not helper.exists()
 for d in docs:
  text=d.read_text(encoding="utf-8")
  for ns,m in METHODS.values():assert f"client.{ns}.{m}" in text
  assert "command_search" in text and "command_detail" in text and "uai-cli" in text and "semantic_frame_id" in text and "uai.generated_commands" not in text

