from __future__ import annotations
from pathlib import Path
from typing import Any
import hashlib
import json
import re

import pytest

from uai.commands import BINDING_CATALOG,bind_generated_commands
from tools.uai_repository.migration_evidence import (
    historical_obligation_fingerprint,
    load_active_command_snapshot,
    load_historical_owner_obligations,
    validate_historical_successor,
)
METHODS={
    "world.actor.create": ("world", "actor_create"),
    "world.actor_hlod_layer.update": ("world", "actor_hlod_layer_update"),
    "world.actor_streaming_policy.update": ("world", "actor_streaming_policy_update"),
    "world.data_layer_instance.create": ("world", "data_layer_instance_create"),
    "world.data_layer_relation.update": ("world", "data_layer_relation_update"),
    "world.data_layer_state.update": ("world", "data_layer_state_update"),
    "world.level_game_mode.update": ("world", "level_game_mode_update"),
    "world.streaming_relation.create": ("world", "streaming_relation_create"),
    "world.streaming_relation.state.update": ("world", "streaming_relation_state_update"),
    "world.wall.create_with_opening": ("world", "wall_create_with_opening"),
    "world.world_partition_streaming.update": ("world", "world_partition_streaming_update"),
}
PRODUCT_COMMAND_IDS=tuple(METHODS)+(
    "content_graph.import_workspace",
    "content_graph.export_workspace",
    "content_graph.summary",
    "world.hlod_assignments",
    "world.streaming_levels",
    "world.partition",
    "world.partition_health",
    "job.compile_build",
    "editor.session",
    "operation.status",
    "operation.resume",
    "operation.cancel",
    "operation.release",
)
class _FakeClient:
 def __init__(self):self.calls=[]
 def execute_exact(self,command_id,params,*,contract_hash):self.calls.append((command_id,dict(params),contract_hash));return {"ok":True}
 def execute(self,command_id,params):
  b=BINDING_CATALOG.find(command_id);assert b is not None;return self.execute_exact(command_id,params,contract_hash=b.binding_hash)
def _bindings():
 v={cid:BINDING_CATALOG.find(cid) for cid in METHODS};assert all(b is not None and (b.namespace,b.method)==METHODS[cid] and re.fullmatch(r"sha256:[0-9a-f]{64}",b.binding_hash) and b.binding_hash!="sha256:"+"0"*64 for cid,b in v.items());return v
def _params(b):
 s={"string":"fixture","integer":1,"number":1.0,"boolean":True,"array":[],"object":{}};return {p.name:s.get(p.wire_type,{}) for p in b.parameters}
def test_exact_default_inventory():assert len(METHODS)==11;_bindings()
def test_default_named_method_forwards_one_exact_request():
 b=_bindings()["world.wall.create_with_opening"];c=_FakeClient();p=_params(b);getattr(getattr(bind_generated_commands(c),b.namespace),b.method)(**p);assert c.calls==[(b.command_id,p,b.binding_hash)]
def test_default_projection_has_no_transport_or_world_business():
 b=_bindings()["world.wall.create_with_opening"];m=getattr(getattr(bind_generated_commands(_FakeClient()),b.namespace),b.method);assert not {"requests","httpx","urllib","retry","sleep","registry","spawn","save","reload","wall","streaming","partition"}&set(m.__func__.__code__.co_names)
def test_t59_legacy_binding_and_tutorial_authority_exit():
 _bindings();root=Path(__file__).resolve().parents[2];helper=root/"cli"/"uai"/"generated_commands"/"t59_world_command_migration";docs=(root/"docs"/"active"/"t59_world_command_migration.md",root.parent/"Plugins"/"UeAgentInterface"/"docs"/"active"/"t59_world_command_migration.md");assert not helper.exists()
 for d in docs:
  text=d.read_text(encoding="utf-8")
  for ns,m in METHODS.values():assert f"client.{ns}.{m}" in text
  assert "command_search" in text and "command_detail" in text and "uai-cli" in text and "semantic_frame_id" in text and "uai.generated_commands" not in text

@pytest.mark.historical_evidence
def test_t59_current_successor_consumes_all_26_frozen_rows_and_product_receipt():
 project_root=Path(__file__).resolve().parents[3]
 plan_root=project_root/"docs"/"plan"/"20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
 obligations=load_historical_owner_obligations(plan_root/"UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json",owner_task_id="T59-WORLD-COMMAND-MIGRATION")
 expected_fingerprint="sha256:c24b63ef3dfad4aabdf3d92f4dbce0ab3cf2e86fba7824718ec5d97526ce9023"
 assert len(obligations)==26
 assert historical_obligation_fingerprint(obligations)==expected_fingerprint
 old_ids={str(row["historical_command_id"]) for row in obligations}
 successor=json.loads((project_root/"Plugins/UeAgentInterface/docs/active/successors/t59_world_command_migration.json").read_text(encoding="utf-8"))
 evidence_ref="docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT/evidence/T59-WORLD-COMMAND-MIGRATION-current-verification.json"
 evidence_path=project_root/evidence_ref
 active_commands=load_active_command_snapshot(project_root/"Plugins/UeAgentInterface/Resources/UaiCommandManifest.json")
 assert old_ids.isdisjoint(active_commands.command_ids)
 assert all(BINDING_CATALOG.find(command_id) is None for command_id in old_ids)
 report=validate_historical_successor(
  document=successor,
  expected_owner_task_id="T59-WORLD-COMMAND-MIGRATION",
  expected_row_ids=tuple(str(row["historical_command_id"]) for row in obligations),
  expected_obligations=obligations,
  expected_obligation_fingerprint=expected_fingerprint,
  active_commands=active_commands,
  project_root=project_root,
  receipt_bindings=({
   "test_id":"UAI.DeliveryWorkflow.T59.WORLD.COMMAND.MIGRATION",
   "ref":evidence_ref,
   "sha256":hashlib.sha256(evidence_path.read_bytes()).hexdigest(),
   "active_registry_hash":active_commands.registry_hash,
   "public_command_ids":list(PRODUCT_COMMAND_IDS),
   "assertions":[
    {"pointer":"/status","equals":"passed"},
    {"pointer":"/historical_obligation_count","equals":26},
    {"pointer":"/claims/public_to_real_ue","equals":True},
    {"pointer":"/claims/persistence","equals":True},
    {"pointer":"/claims/independent_readback","equals":True},
    {"pointer":"/claims/historical_semantics_covered","equals":True},
    {"pointer":"/claims/old_public_ids_absent","equals":True},
    {"pointer":"/claims/cleanup_confirmed","equals":True},
   ],
  },),
 )
 assert report.row_count==26
 assert report.obligation_fingerprint==expected_fingerprint
