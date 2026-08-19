from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_ID = "external.skin_weight_profile.import"


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


def _require_binding():
    binding = BINDING_CATALOG.find(COMMAND_ID)
    assert binding is not None
    assert binding.command_id == COMMAND_ID
    assert binding.namespace == "external"
    assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
    assert binding.binding_hash != "sha256:" + "0" * 64
    return binding


def test_skin_weight_import_has_one_exact_default_binding() -> None:
    _require_binding()


def test_default_method_preserves_source_target_profile_and_lod() -> None:
    _require_binding()
    client = _RecordingClient()
    bind_generated_commands(client).external.skin_weight_profile_import(
        "D:/fixture.fbx",
        "/Game/StrictV2/T29/Target.Target",
        "Alternate",
        0,
    )
    assert client.calls[0][0] == COMMAND_ID
    assert client.calls[0][1] == {
        "source_ref": "D:/fixture.fbx",
        "target_ref": "/Game/StrictV2/T29/Target.Target",
        "profile_name": "Alternate",
        "lod_index": 0,
    }


def test_named_and_generic_execution_use_the_same_exact_binding() -> None:
    binding = _require_binding()
    named = _RecordingClient()
    generic = _RecordingClient()
    params = {
        "source_ref": "D:/fixture.fbx",
        "target_ref": "/Game/StrictV2/T29/Target.Target",
        "profile_name": "Alternate",
        "lod_index": 1,
    }
    bind_generated_commands(named).external.skin_weight_profile_import(
        params["source_ref"],
        params["target_ref"],
        params["profile_name"],
        params["lod_index"],
    )
    generic.execute_exact(
        COMMAND_ID,
        params,
        contract_hash=binding.binding_hash,
    )
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_ue_business_logic() -> None:
    _require_binding()
    method = bind_generated_commands(_RecordingClient()).external.skin_weight_profile_import
    names = set(method.__func__.__code__.co_names)
    assert "requests" not in names
    assert "httpx" not in names
    assert "urllib" not in names
    assert "retry" not in names
    assert "save" not in names
    assert "reload" not in names
    assert "ImportAlternateSkinWeight" not in names


def test_t29_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_binding()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = (
        cmd_root
        / "cli"
        / "uai"
        / "generated_commands"
        / "t29_external_skin_weight_import"
    )
    task_doc = cmd_root / "docs" / "active" / "t29_external_skin_weight_import.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t29_external_skin_weight_import.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.external.skin_weight_profile_import" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text
