from __future__ import annotations
from pathlib import Path
import re
import pytest
from uai.commands import _BINDING_CATALOG,bind_generated_commands
METHODS={
    "animation.ik_probe_candidate.apply": ("animation", "ik_probe_candidate_apply"),
    "animation.subject.morph_weights.update": ("animation", "subject_morph_weights_update"),
    "animation.subject.pose.update": ("animation", "subject_pose_update"),
    "rig.control.bake.animation": ("rig", "control_bake_animation"),
    "rig.control.bake.controls": ("rig", "control_bake_controls"),
    "rig.retarget.assets.generate": ("rig", "retarget_assets_generate"),
    "rig.retarget.pose.auto_align": ("rig", "retarget_pose_auto_align"),
}
DORMANT_METHODS={
    "rig.ik.definition.update": ("rig", "ik_definition_update"),
    "rig.retarget.definition.update": ("rig", "retarget_definition_update"),
    "rig.retarget.pose.update": ("rig", "retarget_pose_update"),
    "rig.skeleton.preview_mesh.bind": ("rig", "skeleton_preview_mesh_bind"),
    "rig.skeleton.socket.update": ("rig", "skeleton_socket_update"),
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
