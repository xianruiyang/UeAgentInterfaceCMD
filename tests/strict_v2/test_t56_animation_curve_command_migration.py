from __future__ import annotations
from pathlib import Path
import re
import pytest
from uai.commands import _BINDING_CATALOG,bind_generated_commands
METHODS={
    "animation.blend_space.asset.create": ("animation", "blend_space_asset_create"),
    "animation.blend_space.sample": ("animation", "blend_space_sample"),
    "animation.montage.create": ("animation", "montage_create"),
    "animation.sequence.pose.sample": ("animation", "sequence_pose_sample"),
    "animation.sequence.root_motion.analyze": ("animation", "sequence_root_motion_analyze"),
}
DORMANT_METHODS={
    "animation.blend_space.definition.apply": ("animation", "blend_space_definition_apply"),
    "animation.montage.read": ("animation", "montage_read"),
    "animation.montage.structure.replace": ("animation", "montage_structure_replace"),
    "animation.sequence.bone_tracks.replace": ("animation", "sequence_bone_tracks_replace"),
    "animation.sequence.curves.update": ("animation", "sequence_curves_update"),
    "animation.sequence.events.update": ("animation", "sequence_events_update"),
    "animation.sequence.metadata.update": ("animation", "sequence_metadata_update"),
    "animation.sequence.read": ("animation", "sequence_read"),
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

def _dormant_bindings():
 v={cid:_BINDING_CATALOG.find(cid) for cid in DORMANT_METHODS};assert all(b is not None and b.status=="dormant" for b in v.values())
 generated=bind_generated_commands(_FakeClient())
 for b in v.values():
  with pytest.raises(AttributeError): getattr(getattr(generated,b.namespace),b.method)
 return v

def test_hjson_operations_are_dormant_and_have_no_named_sdk_method():
 _dormant_bindings()
