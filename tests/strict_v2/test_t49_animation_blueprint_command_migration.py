from __future__ import annotations
from pathlib import Path
from typing import Any
import re
import pytest
from uai.commands import _BINDING_CATALOG,bind_generated_commands
METHODS={
    "animation.anim_blueprint.layer_interface.asset.create": ("animation", "anim_blueprint_layer_interface_asset_create"),
}
DORMANT_METHODS={
    "animation.anim_blueprint.asset.create": ("animation", "anim_blueprint_asset_create"),
}
INTERNAL_ONLY={
    "animation.anim_blueprint.graph.apply",
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

def test_hjson_create_is_dormant_and_has_no_named_sdk_method():
 v={cid:_BINDING_CATALOG.find(cid) for cid in DORMANT_METHODS};assert all(b is not None and b.status=="dormant" for b in v.values())
 generated=bind_generated_commands(_FakeClient())
 for b in v.values():
  with pytest.raises(AttributeError): getattr(getattr(generated,b.namespace),b.method)
