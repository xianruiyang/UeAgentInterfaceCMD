from __future__ import annotations
from pathlib import Path
import re
from uai.commands import BINDING_CATALOG,bind_generated_commands
METHODS={
    "audio_media.asset.create": ("audio_media", "asset_create"),
    "metasound.graph.compile_settle": ("metasound", "graph_compile_settle"),
    "metasound.graph.default.mutate": ("metasound", "graph_default_mutate"),
    "metasound.graph.interface.mutate": ("metasound", "graph_interface_mutate"),
    "metasound.graph.link.mutate": ("metasound", "graph_link_mutate"),
    "metasound.graph.node.mutate": ("metasound", "graph_node_mutate"),
    "sound_cue.graph.compile_settle": ("sound_cue", "graph_compile_settle"),
    "sound_cue.graph.node.mutate": ("sound_cue", "graph_node_mutate"),
    "sound_cue.graph.relation.mutate": ("sound_cue", "graph_relation_mutate"),
    "sound_cue.graph.root.mutate": ("sound_cue", "graph_root_mutate"),
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
def test_exact_default_inventory():assert len(METHODS)==10;_bindings()
def test_default_named_method_forwards_one_exact_request():
 b=_bindings()["metasound.graph.node.mutate"];c=_FakeClient();p=_params(b);getattr(getattr(bind_generated_commands(c),b.namespace),b.method)(**p);assert c.calls==[(b.command_id,p,b.binding_hash)]
def test_default_projection_has_no_transport_or_audio_business():
 b=_bindings()["metasound.graph.node.mutate"];m=getattr(getattr(bind_generated_commands(_FakeClient()),b.namespace),b.method);assert not {"requests","httpx","urllib","retry","sleep","registry","compile","save","reload","graph","audio"}&set(m.__func__.__code__.co_names)
def test_t54_legacy_binding_and_tutorial_authority_exit():
 _bindings();root=Path(__file__).resolve().parents[2];helper=root/"cli"/"uai"/"generated_commands"/"t54_audio_command_migration";docs=(root/"docs"/"active"/"t54_audio_command_migration.md",root.parent/"Plugins"/"UeAgentInterface"/"docs"/"active"/"t54_audio_command_migration.md");assert not helper.exists()
 for d in docs:
  text=d.read_text(encoding="utf-8")
  for ns,m in METHODS.values():assert f"client.{ns}.{m}" in text
  assert "command_search" in text and "command_detail" in text and "uai-cli" in text and "uai.generated_commands" not in text

