from __future__ import annotations
from pathlib import Path
import re
import pytest
from uai.commands import _BINDING_CATALOG,bind_generated_commands
METHODS={
    "animation.control_rig.asset.create": ("animation", "control_rig_asset_create"),
    "animation.control_rig.shape_library.asset.create": ("animation", "control_rig_shape_library_asset_create"),
    "animation.ik_retargeter.asset.create": ("animation", "ik_retargeter_asset_create"),
    "animation.ik_rig.asset.create": ("animation", "ik_rig_asset_create"),
    "animation.ik_rig.definition.auto_generate": ("animation", "ik_rig_definition_auto_generate"),
}
DORMANT_METHODS={
    "animation.control_rig.shape_library.apply": ("animation", "control_rig_shape_library_apply"),
    "animation.skeleton.slots.read": ("animation", "skeleton_slots_read"),
}
INTERNAL_HJSON_OPERATION_IDS={
    "animation.control_rig.hierarchy_graph.apply",
    "animation.ik_retargeter.definition.apply",
    "animation.ik_retargeter.settings.apply",
    "animation.ik_rig.definition.apply",
    "animation.skeleton.compatibility.apply",
    "animation.skeleton.definition.apply",
    "animation.skeleton.virtual_bone.apply",
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
