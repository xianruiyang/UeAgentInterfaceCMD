from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


EXPECTED_COMMAND_IDS = {
    "asset.reimport_sound_wave",
    "asset.reimport_sparse_volume_texture",
    "asset.reimport_static_mesh",
    "asset.reimport_texture",
    "external.fbx.animation.import",
    "external.fbx.skeletal_mesh.import",
    "external.geometry_cache.import",
    "external.light_profile.import",
    "external.sound_wave.import",
    "external.sparse_volume_texture.import",
    "external.texture.import",
}

HISTORICAL_SUCCESSORS = {
    "asset_import_fbx_animation": ["external.fbx.animation.import"],
    "asset_import_fbx_skeletal_mesh": ["external.fbx.skeletal_mesh.import"],
    "asset_import_geometry_cache": ["external.geometry_cache.import"],
    "asset_import_texture": ["external.texture.import"],
    "light_profile_texture_import": ["external.light_profile.import"],
    "sound_wave_import": ["external.sound_wave.import"],
    "sound_wave_reimport": ["asset.reimport_sound_wave"],
    "sparse_volume_texture_import": ["external.sparse_volume_texture.import"],
    "sparse_volume_texture_reimport": ["asset.reimport_sparse_volume_texture"],
    "static_mesh_reimport": ["asset.reimport_static_mesh"],
    "texture_reimport": ["asset.reimport_texture"],
}


class _RecordedResult:
    ok = True


class _RecordingClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(
        self,
        command_id: str,
        params: dict[str, Any],
        *,
        contract_hash: str,
    ) -> _RecordedResult:
        self.calls.append((command_id, dict(params), contract_hash))
        return _RecordedResult()

    def execute(
        self,
        command_id: str,
        params: dict[str, Any],
    ) -> _RecordedResult:
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_bindings():
    bindings = {
        command_id: BINDING_CATALOG.find(command_id)
        for command_id in EXPECTED_COMMAND_IDS
    }
    assert all(binding is not None for binding in bindings.values())
    assert all(
        binding is not None
        and binding.command_id == command_id
        and binding.namespace in {"asset", "external"}
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def test_all_audited_factory_import_commands_have_exact_default_bindings() -> None:
    _require_bindings()


def test_active_historical_imports_have_exact_successors_and_old_ids_exit() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    project_root = cmd_root.parent
    successor_path = (
        project_root
        / "Plugins/UeAgentInterface/docs/active/successors/t28_external_factory_import.json"
    )
    successor = json.loads(successor_path.read_text(encoding="utf-8"))
    assert successor["schema"] == "uai.historical_successor.v2"
    assert successor["owner_task_id"] == "T28-EXTERNAL-FACTORY-IMPORT"
    rows = {
        row["historical_command_id"]: row for row in successor["commands"]
    }
    assert set(rows) == set(HISTORICAL_SUCCESSORS)
    for historical_id, command_ids in HISTORICAL_SUCCESSORS.items():
        row = rows[historical_id]
        assert row["successor"] == {
            "kind": "exact_command_set",
            "command_ids": command_ids,
        }
        assert row["resolved_from_contract_id"].startswith(
            "uai.historical_capability.t28.external.factory.import."
        )
        assert set(row["semantic_coverage"]) == {"purpose", "inputs", "outputs"}
        assert all(
            item["status"] == "covered"
            and item["by"] == command_ids
            and item["explanation"]
            for item in row["semantic_coverage"].values()
        )
        assert row["product_evidence"]["test_id"] == (
            "UAI.StrictV2.T28.EXTERNAL.FACTORY.IMPORT"
        )
        assert all(row["old_id_exit"].values()) is False
        assert BINDING_CATALOG.find(historical_id) is None


def test_successor_contract_documents_legacy_option_coverage() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    successor_path = (
        cmd_root.parent
        / "Plugins/UeAgentInterface/docs/active/successors/t28_external_factory_import.json"
    )
    rows = {
        row["historical_command_id"]: row
        for row in json.loads(successor_path.read_text(encoding="utf-8"))["commands"]
    }
    texture = rows["asset_import_texture"]
    assert all(
        field in texture["historical_contract"]["inputs"]
        for field in ("srgb", "compression_settings", "mip_gen_settings", "lod_group")
    )
    skeletal = rows["asset_import_fbx_skeletal_mesh"]
    assert all(
        field in skeletal["historical_contract"]["inputs"]
        for field in (
            "skeleton_path",
            "import_morph_targets",
            "update_skeleton_reference_pose",
            "validate_after_import",
            "expected_*",
        )
    )


def test_import_method_preserves_source_destination_skeleton_and_options() -> None:
    _require_bindings()
    client = _RecordingClient()
    source = "D:/fixtures/Walk.fbx"
    destination = "/Game/StrictV2/T28/Walk"
    skeleton = "/Game/Characters/SK_Mannequin_Skeleton.SK_Mannequin_Skeleton"
    options = {
        "import_materials": False,
        "import_textures": False,
        "create_physics_asset": False,
    }
    bind_generated_commands(client).external.fbx_animation_import(
        source,
        destination,
        skeleton,
        options=options,
    )
    assert client.calls[0][0] == "external.fbx.animation.import"
    assert client.calls[0][1] == {
        "source_ref": source,
        "destination_ref": destination,
        "skeleton_ref": skeleton,
        "options": options,
    }


def test_reimport_method_preserves_source_target_and_options() -> None:
    _require_bindings()
    client = _RecordingClient()
    target = "/Game/StrictV2/T28/OwnedTexture.OwnedTexture"
    source = "D:/fixtures/OwnedTexture.png"
    options = {"replace_existing": True}
    bind_generated_commands(client).asset.reimport_texture(
        source,
        target,
        options=options,
    )
    assert client.calls[0][0] == "asset.reimport_texture"
    assert client.calls[0][1] == {
        "source_ref": source,
        "target_ref": target,
        "options": options,
    }


def test_named_and_generic_execution_use_the_same_exact_binding() -> None:
    bindings = _require_bindings()
    named = _RecordingClient()
    generic = _RecordingClient()
    params = {
        "source_ref": "D:/fixtures/OwnedSound.wav",
        "destination_ref": "/Game/StrictV2/T28/OwnedSound",
        "options": {},
    }
    bind_generated_commands(named).external.sound_wave_import(
        params["source_ref"],
        params["destination_ref"],
        options=params["options"],
    )
    generic.execute_exact(
        "external.sound_wave.import",
        params,
        contract_hash=bindings["external.sound_wave.import"].binding_hash,
    )
    assert named.calls == generic.calls


def test_t28_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = (
        cmd_root
        / "cli"
        / "uai"
        / "generated_commands"
        / "t28_external_factory_import"
    )
    task_doc = cmd_root / "docs" / "active" / "t28_external_factory_import.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t28_external_factory_import.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.external.fbx_animation_import" in text
        assert "client.external.sound_wave_import" in text
        assert "client.asset.reimport_texture" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text
