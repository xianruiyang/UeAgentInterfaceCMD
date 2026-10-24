from __future__ import annotations
from pathlib import Path
import re
from uai.commands import _BINDING_CATALOG,bind_generated_commands
METHODS={
    "audio_media.asset.create": ("audio_media", "asset_create"),
    "metasound.graph.compile_settle": ("metasound", "graph_compile_settle"),
    "sound_cue.graph.compile_settle": ("sound_cue", "graph_compile_settle"),
}
INTERNAL_HJSON_OPERATION_IDS={
 "metasound.graph.default.mutate",
 "metasound.graph.interface.mutate",
 "metasound.graph.link.mutate",
 "metasound.graph.node.mutate",
 "sound_cue.graph.node.mutate",
 "sound_cue.graph.relation.mutate",
 "sound_cue.graph.root.mutate",
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
