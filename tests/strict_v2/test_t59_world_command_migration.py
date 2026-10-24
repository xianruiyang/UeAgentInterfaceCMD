from __future__ import annotations
from pathlib import Path
from typing import Any
import hashlib
import json
import re

import pytest

from uai.commands import _BINDING_CATALOG,bind_generated_commands
METHODS={
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
SLEEP_COMMAND_IDS=set(METHODS)-{"world.wall.create_with_opening"}
KEEP_COMMAND_IDS={"world.wall.create_with_opening"}
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
  b=_BINDING_CATALOG.find(command_id);assert b is not None;return self.execute_exact(command_id,params,contract_hash=b.binding_hash)
def _bindings():
 v={cid:_BINDING_CATALOG.find(cid) for cid in METHODS};assert all(b is not None and (b.namespace,b.method)==METHODS[cid] and re.fullmatch(r"sha256:[0-9a-f]{64}",b.binding_hash) and b.binding_hash!="sha256:"+"0"*64 for cid,b in v.items());assert all(v[cid].status=="dormant" for cid in SLEEP_COMMAND_IDS);assert all(v[cid].status=="active" for cid in KEEP_COMMAND_IDS);return v
def _params(b):
 s={"string":"fixture","integer":1,"number":1.0,"boolean":True,"array":[],"object":{}};return {p.name:s.get(p.wire_type,{}) for p in b.parameters}

def test_t59_sleep_commands_are_dormant_and_not_named_sdk():
 bindings=_bindings(); namespaces=bind_generated_commands(_FakeClient())
 for cid in SLEEP_COMMAND_IDS:
  assert bindings[cid].status=="dormant"
  assert not hasattr(namespaces.world, bindings[cid].method)

def test_t59_whitebox_command_remains_active_named_sdk():
 bindings=_bindings(); namespaces=bind_generated_commands(_FakeClient())
 for cid in KEEP_COMMAND_IDS:
  assert bindings[cid].status=="active"
  assert hasattr(namespaces.world, bindings[cid].method)
