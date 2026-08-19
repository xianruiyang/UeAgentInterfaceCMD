from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands

COMMAND_IDS = (
    "asset.delete", "asset.fixup_redirectors", "asset.move", "asset.object.clone",
    "modeling.actor.mesh.replace", "modeling.asset.material_slot.remove", "modeling.voxel.bounds.remove",
    "skeletal_mesh.remove_morph_target", "skeletal_mesh.remove_skin_weight_profile",
    "world.data_layer.delete", "world.level_content.delete_scope",
    "world.level_streaming.move_actors", "world.level_streaming.remove", "world.pcg.cleanup",
)

HISTORICAL_SUCCESSORS = {
    "asset_delete": ("asset.delete",),
    "asset_duplicate": ("asset.object.clone",),
    "asset_fixup_redirectors": ("asset.fixup_redirectors",),
    "asset_move": ("asset.move",),
    "level_streaming_move_actors": ("world.level_streaming.move_actors",),
    "level_streaming_remove": ("world.level_streaming.remove",),
}

class _Client:
    def __init__(self): self.calls: list[tuple[str, dict[str, Any], str]]=[]
    def execute_exact(self, command_id, params, *, contract_hash): self.calls.append((command_id,dict(params),contract_hash)); return {"ok":True}
    def execute(self, command_id, params):
        binding=BINDING_CATALOG.find(command_id); assert binding is not None
        return self.execute_exact(command_id,params,contract_hash=binding.binding_hash)

def _bindings():
    values={cid:BINDING_CATALOG.find(cid) for cid in COMMAND_IDS}
    assert len(values)==14
    assert all(v is not None and re.fullmatch(r"sha256:[0-9a-f]{64}",v.binding_hash) for v in values.values())
    return values

def test_t31_all_destructive_commands_have_one_default_binding() -> None:
    values=_bindings(); assert len({v.command_id for v in values.values()})==14

def test_t31_named_delete_forwards_one_exact_request() -> None:
    client=_Client(); bind_generated_commands(client).asset.delete("/Game/UAI/StrictV2/T31/Fixture")
    assert len(client.calls)==1 and client.calls[0][0]=="asset.delete"
    assert client.calls[0][1]=={"target_ref":"/Game/UAI/StrictV2/T31/Fixture"}

def test_t31_default_binding_contains_no_destructive_business() -> None:
    names=set(bind_generated_commands(_Client()).asset.delete.__func__.__code__.co_names)
    assert not {"authorize","delete","redirector","save","reload","rollback","cleanup"}&names

def test_t31_task_projection_and_tutorial_authority_exit() -> None:
    bindings=_bindings(); cmd_root=Path(__file__).resolve().parents[2]
    assert not (cmd_root/"cli/uai/generated_commands/destructive_content").exists()
    docs=(cmd_root/"docs/active/t31_destructive_content_ops.md",cmd_root.parent/"Plugins/UeAgentInterface/docs/active/t31_destructive_content_ops.md")
    methods={f"client.{v.namespace}.{v.method}" for v in bindings.values()}
    for document in docs:
        text=document.read_text(encoding="utf-8")
        assert all(method in text for method in methods)
        assert "command_search" in text and "command_detail" in text and "uai-cli" in text
        assert "authorization" in text and "preflight" in text and "cleanup" in text
        assert "uai.generated_commands" not in text


def test_t31_historical_successors_are_exact_and_row_complete() -> None:
    project_root = Path(__file__).resolve().parents[2].parent
    path = (
        project_root
        / "Plugins/UeAgentInterface/docs/active/successors/t31_destructive_content_ops.json"
    )
    payload = __import__("json").loads(path.read_text(encoding="utf-8"))
    assert payload["schema"] == "uai.historical_successor.v2"
    assert payload["owner_task_id"] == "T31-DESTRUCTIVE-CONTENT-OPS"
    rows = {row["historical_command_id"]: row for row in payload["commands"]}
    assert set(rows) == set(HISTORICAL_SUCCESSORS)
    for command_id, expected in HISTORICAL_SUCCESSORS.items():
        row = rows[command_id]
        assert row["successor"] == {
            "kind": "exact_command_set",
            "command_ids": list(expected),
        }
        assert all(
            row["semantic_coverage"][field]["status"] == "covered"
            for field in ("purpose", "inputs", "outputs")
        )
        assert row["old_id_exit"] == {
            "public_executable": False,
            "manifest_active": False,
            "sdk_binding_active": False,
            "compatibility_alias": False,
        }
