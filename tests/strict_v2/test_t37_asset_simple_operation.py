from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = (
    "asset.audio_effect_preset.create", "asset.audio_effect_preset.update",
    "asset.curve.update", "asset.data_layer.create", "asset.data_object.create",
    "asset.data_object.update", "asset.data_table.replace",
    "asset.input_action.create", "asset.input_action.update",
    "asset.input_mapping_context.create", "asset.input_mapping_context.update",
    "asset.media_player.create", "asset.media_player.update",
    "asset.media_source.create", "asset.media_source.update",
    "asset.media_texture.create", "asset.media_texture.update",
    "asset.paper_flipbook.create", "asset.paper_flipbook.update",
    "asset.paper_sprite.create", "asset.paper_sprite.update",
    "asset.paper_tilemap.update", "asset.paper_tileset.update",
    "asset.render_target.create", "asset.render_target.update",
    "asset.runtime_virtual_texture.create", "asset.runtime_virtual_texture.update",
    "asset.skeletal_mesh.update", "asset.sound_attenuation.create",
    "asset.sound_attenuation.update", "asset.sound_class.create",
    "asset.sound_class.update", "asset.sound_concurrency.create",
    "asset.sound_concurrency.update", "asset.sound_mix.create",
    "asset.sound_mix.update", "asset.sound_submix.create",
    "asset.sound_submix.update", "asset.sparse_volume_texture.update",
    "asset.static_mesh.update", "asset.subuv_animation.create",
    "asset.subuv_animation.update", "asset.texture_array.create",
    "asset.texture_array.replace", "asset.texture_collection.create",
    "asset.texture_collection.update", "asset.texture_cube.create",
    "asset.texture_cube.replace", "asset.texture_cube_array.create",
    "asset.texture_cube_array.replace", "asset.volume_texture.create",
    "asset.volume_texture.replace",
)


class _FakeClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(
        self,
        command_id: str,
        params: dict[str, Any],
        *,
        contract_hash: str,
    ) -> dict[str, object]:
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id: str, params: dict[str, Any]) -> dict[str, object]:
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_bindings():
    bindings = {
        command_id: BINDING_CATALOG.find(command_id) for command_id in COMMAND_IDS
    }
    assert all(
        binding is not None
        and binding.command_id == command_id
        and binding.namespace == "asset"
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def test_all_52_asset_commands_have_exact_default_bindings() -> None:
    assert len(COMMAND_IDS) == 52
    _require_bindings()


def test_default_create_preserves_the_exact_target() -> None:
    _require_bindings()
    client = _FakeClient()
    bind_generated_commands(client).asset.sound_class_create(
        "/Game/StrictV2/T37/SC_Default.SC_Default"
    )
    assert client.calls[0][0] == "asset.sound_class.create"
    assert client.calls[0][1] == {
        "target_ref": "/Game/StrictV2/T37/SC_Default.SC_Default"
    }


def test_named_and_generic_create_use_the_same_exact_binding() -> None:
    bindings = _require_bindings()
    named = _FakeClient()
    generic = _FakeClient()
    params = {"target_ref": "/Game/StrictV2/T37/SC_Default.SC_Default"}
    bind_generated_commands(named).asset.sound_class_create(params["target_ref"])
    generic.execute_exact(
        "asset.sound_class.create",
        params,
        contract_hash=bindings["asset.sound_class.create"].binding_hash,
    )
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_ue_business_logic() -> None:
    _require_bindings()
    method = bind_generated_commands(_FakeClient()).asset.sound_class_create
    names = set(method.__func__.__code__.co_names)
    assert not {
        "requests",
        "httpx",
        "urllib",
        "retry",
        "sleep",
        "registry",
        "save",
        "reload",
        "rollback",
    } & names


def test_t37_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = (
        cmd_root
        / "cli"
        / "uai"
        / "generated_commands"
        / "t37_asset_simple_operation"
    )
    task_doc = cmd_root / "docs" / "active" / "t37_asset_simple_operation.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t37_asset_simple_operation.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.asset.sound_class_create" in text
        assert "client.asset.render_target_create" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text
