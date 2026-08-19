from __future__ import annotations
from pathlib import Path
import re
from uai.commands import BINDING_CATALOG,bind_generated_commands
METHODS={
    "animation.ik_probe_candidate.apply": ("animation", "ik_probe_candidate_apply"),
    "animation.subject.morph_weights.update": ("animation", "subject_morph_weights_update"),
    "animation.subject.pose.update": ("animation", "subject_pose_update"),
    "rig.control.bake.animation": ("rig", "control_bake_animation"),
    "rig.control.bake.controls": ("rig", "control_bake_controls"),
    "rig.ik.definition.update": ("rig", "ik_definition_update"),
    "rig.retarget.assets.generate": ("rig", "retarget_assets_generate"),
    "rig.retarget.definition.update": ("rig", "retarget_definition_update"),
    "rig.retarget.pose.auto_align": ("rig", "retarget_pose_auto_align"),
    "rig.retarget.pose.update": ("rig", "retarget_pose_update"),
    "rig.skeleton.preview_mesh.bind": ("rig", "skeleton_preview_mesh_bind"),
    "rig.skeleton.socket.update": ("rig", "skeleton_socket_update"),
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
def test_exact_default_inventory():assert len(METHODS)==12;_bindings()
def test_default_named_method_forwards_one_exact_request():
 b=_bindings()["rig.retarget.pose.update"];c=_FakeClient();p=_params(b);getattr(getattr(bind_generated_commands(c),b.namespace),b.method)(**p);assert c.calls==[(b.command_id,p,b.binding_hash)]
def test_default_projection_has_no_transport_binding_or_rig_business():
 b=_bindings()["rig.retarget.pose.update"];m=getattr(getattr(bind_generated_commands(_FakeClient()),b.namespace),b.method);assert not {"requests","httpx","urllib","retry","sleep","registry","resolve","bind","fixture","save","reload","retarget"}&set(m.__func__.__code__.co_names)
def test_t58_legacy_binding_and_tutorial_authority_exit():
 _bindings();root=Path(__file__).resolve().parents[2];helper=root/"cli"/"uai"/"generated_commands"/"t58_rig_spatial_command_migration";docs=(root/"docs"/"active"/"t58_rig_spatial_command_migration.md",root.parent/"Plugins"/"UeAgentInterface"/"docs"/"active"/"t58_rig_spatial_command_migration.md");assert not helper.exists()
 for d in docs:
  text=d.read_text(encoding="utf-8")
  for ns,m in METHODS.values():assert f"client.{ns}.{m}" in text
  assert "command_search" in text and "command_detail" in text and "uai-cli" in text and "semantic_frame_id" in text
  assert "production binding" in text and "uai.generated_commands" not in text

