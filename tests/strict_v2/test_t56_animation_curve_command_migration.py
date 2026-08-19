from __future__ import annotations
from pathlib import Path
import re
from uai.commands import BINDING_CATALOG,bind_generated_commands
METHODS={
    "animation.blend_space.asset.create": ("animation", "blend_space_asset_create"),
    "animation.blend_space.definition.apply": ("animation", "blend_space_definition_apply"),
    "animation.blend_space.sample": ("animation", "blend_space_sample"),
    "animation.montage.create": ("animation", "montage_create"),
    "animation.montage.read": ("animation", "montage_read"),
    "animation.montage.structure.replace": ("animation", "montage_structure_replace"),
    "animation.sequence.bone_tracks.replace": ("animation", "sequence_bone_tracks_replace"),
    "animation.sequence.curves.update": ("animation", "sequence_curves_update"),
    "animation.sequence.events.update": ("animation", "sequence_events_update"),
    "animation.sequence.metadata.update": ("animation", "sequence_metadata_update"),
    "animation.sequence.pose.sample": ("animation", "sequence_pose_sample"),
    "animation.sequence.read": ("animation", "sequence_read"),
    "animation.sequence.root_motion.analyze": ("animation", "sequence_root_motion_analyze"),
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
def test_exact_default_inventory():assert len(METHODS)==13;_bindings()
def test_default_named_method_forwards_one_exact_request():
 b=_bindings()["animation.sequence.curves.update"];c=_FakeClient();p=_params(b);getattr(getattr(bind_generated_commands(c),b.namespace),b.method)(**p);assert c.calls==[(b.command_id,p,b.binding_hash)]
def test_default_projection_has_no_transport_or_animation_business():
 b=_bindings()["animation.sequence.curves.update"];m=getattr(getattr(bind_generated_commands(_FakeClient()),b.namespace),b.method);assert not {"requests","httpx","urllib","retry","sleep","registry","sample","save","reload","curve","sequence"}&set(m.__func__.__code__.co_names)
def test_t56_legacy_binding_and_tutorial_authority_exit():
 _bindings();root=Path(__file__).resolve().parents[2];helper=root/"cli"/"uai"/"generated_commands"/"t56_animation_curve_command_migration";docs=(root/"docs"/"active"/"t56_animation_curve_command_migration.md",root.parent/"Plugins"/"UeAgentInterface"/"docs"/"active"/"t56_animation_curve_command_migration.md");assert not helper.exists()
 for d in docs:
  text=d.read_text(encoding="utf-8")
  for ns,m in METHODS.values():assert f"client.{ns}.{m}" in text
  assert "command_search" in text and "command_detail" in text and "uai-cli" in text and "semantic_frame_id" in text and "uai.generated_commands" not in text

