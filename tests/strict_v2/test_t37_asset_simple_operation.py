from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands


REQUIRED_PUBLIC_IDS = (
    "asset.object.create",
)

DORMANT_HJSON_IDS = (
    "asset.media_source.update",
    "asset.sound_class.update",
    "asset.texture_array.replace",
)

GENERIC_CREATE_SUCCESSORS = (
    "asset.audio_effect_preset.create",
    "asset.data_object.create",
    "asset.data_layer.create",
    "asset.input_action.create",
    "asset.input_mapping_context.create",
    "asset.media_player.create",
    "asset.media_source.create",
    "asset.media_texture.create",
    "asset.paper_flipbook.create",
    "asset.paper_sprite.create",
    "asset.render_target.create",
    "asset.runtime_virtual_texture.create",
    "asset.sound_attenuation.create",
    "asset.sound_class.create",
    "asset.sound_concurrency.create",
    "asset.sound_mix.create",
    "asset.sound_submix.create",
    "asset.subuv_animation.create",
    "asset.texture_array.create",
    "asset.texture_collection.create",
    "asset.texture_cube.create",
    "asset.texture_cube_array.create",
    "asset.volume_texture.create",
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
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_bindings():
    bindings = {
        command_id: _BINDING_CATALOG.find(command_id)
        for command_id in REQUIRED_PUBLIC_IDS
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


def test_hjson_primary_asset_operations_are_dormant_without_named_methods():
    namespaces = bind_generated_commands(_FakeClient())
    for command_id in DORMANT_HJSON_IDS:
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None and binding.status == "dormant"
        namespace = getattr(namespaces, binding.namespace, None)
        if namespace is not None:
            assert not hasattr(namespace, binding.method), command_id


def test_generic_create_successors_are_absent_from_public_sdk():
    namespaces = bind_generated_commands(_FakeClient())
    for command_id in GENERIC_CREATE_SUCCESSORS:
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is None, command_id
        namespace_name, _, method_name = command_id.partition(".")
        namespace = getattr(namespaces, namespace_name, None)
        if namespace is not None:
            assert not hasattr(
                namespace,
                method_name.replace(".", "_"),
            ), command_id
