from __future__ import annotations
from pathlib import Path
import re
from uai.commands import BINDING_CATALOG,bind_generated_commands
METHODS={
    "animation.control_rig.asset.create": ("animation", "control_rig_asset_create"),
    "animation.control_rig.hierarchy_graph.apply": ("animation", "control_rig_hierarchy_graph_apply"),
    "animation.control_rig.shape_library.apply": ("animation", "control_rig_shape_library_apply"),
    "animation.control_rig.shape_library.asset.create": ("animation", "control_rig_shape_library_asset_create"),
    "animation.ik_retargeter.asset.create": ("animation", "ik_retargeter_asset_create"),
    "animation.ik_retargeter.definition.apply": ("animation", "ik_retargeter_definition_apply"),
    "animation.ik_retargeter.settings.apply": ("animation", "ik_retargeter_settings_apply"),
    "animation.ik_rig.asset.create": ("animation", "ik_rig_asset_create"),
    "animation.ik_rig.definition.apply": ("animation", "ik_rig_definition_apply"),
    "animation.ik_rig.definition.auto_generate": ("animation", "ik_rig_definition_auto_generate"),
    "animation.skeleton.compatibility.apply": ("animation", "skeleton_compatibility_apply"),
    "animation.skeleton.definition.apply": ("animation", "skeleton_definition_apply"),
    "animation.skeleton.slots.read": ("animation", "skeleton_slots_read"),
    "animation.skeleton.virtual_bone.apply": ("animation", "skeleton_virtual_bone_apply"),
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
def test_exact_default_inventory():assert len(METHODS)==14;_bindings()
def test_default_named_method_forwards_one_exact_request():
 b=_bindings()["animation.control_rig.hierarchy_graph.apply"];c=_FakeClient();p=_params(b);getattr(getattr(bind_generated_commands(c),b.namespace),b.method)(**p);assert c.calls==[(b.command_id,p,b.binding_hash)]
def test_default_projection_has_no_transport_or_rig_business():
 b=_bindings()["animation.control_rig.hierarchy_graph.apply"];m=getattr(getattr(bind_generated_commands(_FakeClient()),b.namespace),b.method);assert not {"requests","httpx","urllib","retry","sleep","registry","generate","save","reload","graph","hierarchy","retarget"}&set(m.__func__.__code__.co_names)
def test_t57_legacy_binding_and_tutorial_authority_exit():
 _bindings();root=Path(__file__).resolve().parents[2];helper=root/"cli"/"uai"/"generated_commands"/"t57_animation_rig_command_migration";docs=(root/"docs"/"active"/"t57_animation_rig_command_migration.md",root.parent/"Plugins"/"UeAgentInterface"/"docs"/"active"/"t57_animation_rig_command_migration.md");assert not helper.exists()
 for d in docs:
  text=d.read_text(encoding="utf-8")
  for ns,m in METHODS.values():assert f"client.{ns}.{m}" in text
  assert "command_search" in text and "command_detail" in text and "uai-cli" in text and "semantic_frame_id" in text and "uai.generated_commands" not in text

