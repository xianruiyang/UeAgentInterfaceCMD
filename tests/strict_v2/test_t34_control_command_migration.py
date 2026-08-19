from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = (
    "editor.safe_exit",
    "editor.session",
    "job.compile_build",
    "operation.plan.execute",
)

HISTORICAL_SUCCESSOR = (
    Path(__file__).resolve().parents[2].parent
    / "Plugins/UeAgentInterface/docs/active/successors/t34_control_command_migration.json"
)

EXPECTED_HISTORICAL_IDS = {
    "editor_close", "editor_console_exec", "editor_prepare_exit",
    "editor_resolve_dirty_resources", "exec_batch", "open_asset_editor",
    "packaging_cancel_task", "packaging_clean_artifacts",
    "packaging_diff_profile_json", "packaging_export_profile_json",
    "packaging_parse_log", "packaging_plan_build",
    "packaging_query_environment", "packaging_report_artifacts",
    "packaging_run_build", "packaging_task_status",
    "packaging_validate_profile_json", "redo", "undo",
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

    def execute(self, command_id: str, params: dict[str, Any]) -> _RecordedResult:
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
    assert all(binding is not None for binding in bindings.values())
    assert all(
        binding is not None
        and binding.command_id == command_id
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    assert bindings["editor.safe_exit"].namespace == "editor"
    assert bindings["editor.session"].namespace == "editor"
    assert bindings["job.compile_build"].namespace == "job"
    assert bindings["operation.plan.execute"].namespace == "operation"
    return bindings


def test_control_commands_have_exact_default_bindings() -> None:
    _require_bindings()


def test_t34_historical_successor_v2_closes_all_frozen_contracts() -> None:
    payload = json.loads(HISTORICAL_SUCCESSOR.read_text(encoding="utf-8"))
    assert payload["schema"] == "uai.historical_successor.v2"
    assert payload["owner_task_id"] == "T34-CONTROL-COMMAND-MIGRATION"
    rows = {row["historical_command_id"]: row for row in payload["commands"]}
    assert set(rows) == EXPECTED_HISTORICAL_IDS
    for historical_id, row in rows.items():
        assert row["resolved_from_contract_id"].endswith(f".{historical_id}/1")
        assert row["successor"]["kind"] == "exact_command_set"
        command_ids = row["successor"]["command_ids"]
        assert command_ids and set(command_ids) <= set(COMMAND_IDS) | {
            "operation.cancel", "operation.status", "operation.receipt",
            "operation.release",
        }
        assert all(
            row["semantic_coverage"][dimension]["status"] == "covered"
            and row["semantic_coverage"][dimension]["by"]
            for dimension in ("purpose", "inputs", "outputs")
        )
        assert row["old_id_exit"] == {
            "public_executable": False,
            "manifest_active": False,
            "sdk_binding_active": False,
            "compatibility_alias": False,
        }


def test_editor_session_preserves_family_subject_policy_and_parameters() -> None:
    _require_bindings()
    client = _RecordingClient()
    bind_generated_commands(client).editor.session(
        "world_context",
        "/Game/Maps/WB_WhiteBox01.WB_WhiteBox01",
        "editor-session-world-context-v1",
        {},
    )
    assert client.calls[0][0] == "editor.session"
    assert client.calls[0][1] == {
        "family_id": "world_context",
        "subject_ref": "/Game/Maps/WB_WhiteBox01.WB_WhiteBox01",
        "policy_id": "editor-session-world-context-v1",
        "parameters": {},
    }


def test_safe_exit_and_compile_build_preserve_exact_params() -> None:
    _require_bindings()
    client = _RecordingClient()
    commands = bind_generated_commands(client)
    commands.editor.safe_exit({"mode": "reject_if_dirty"})
    commands.job.compile_build(
        "plugin_editor",
        "UeAgentInterface",
        "development-editor-v1",
        {"live_coding": False},
    )
    assert client.calls[0][0:2] == (
        "editor.safe_exit",
        {"dirty_resolution": {"mode": "reject_if_dirty"}},
    )
    assert client.calls[1][0:2] == (
        "job.compile_build",
        {
            "family_id": "plugin_editor",
            "subject_ref": "UeAgentInterface",
            "policy_id": "development-editor-v1",
            "parameters": {"live_coding": False},
        },
    )


def test_named_and_generic_session_use_the_same_exact_binding() -> None:
    bindings = _require_bindings()
    named = _RecordingClient()
    generic = _RecordingClient()
    params = {
        "family_id": "world_context",
        "subject_ref": "/Game/Maps/WB_WhiteBox01.WB_WhiteBox01",
        "policy_id": "editor-session-world-context-v1",
        "parameters": {},
    }
    bind_generated_commands(named).editor.session(
        params["family_id"],
        params["subject_ref"],
        params["policy_id"],
        params["parameters"],
    )
    generic.execute_exact(
        "editor.session",
        params,
        contract_hash=bindings["editor.session"].binding_hash,
    )
    assert named.calls == generic.calls


def test_operation_plan_named_binding_preserves_server_plan() -> None:
    _require_bindings()
    client = _RecordingClient()
    steps = [{
        "step_id": "step-1",
        "kind": "transaction_history",
        "action": "undo",
        "subject_ref": "editor:transaction-history",
        "policy_id": "policy:transaction-history:standard/v1",
        "expected_revision": 7,
        "parameters": {},
    }]
    bind_generated_commands(client).operation.plan_execute(
        steps, "stop", "reject_non_atomic"
    )
    assert client.calls[0][0:2] == (
        "operation.plan.execute",
        {
            "steps": steps,
            "on_error": "stop",
            "atomicity": "reject_non_atomic",
        },
    )


def test_default_projection_contains_no_transport_or_lifecycle_business() -> None:
    _require_bindings()
    commands = bind_generated_commands(_RecordingClient())
    names = (
        set(commands.editor.session.__func__.__code__.co_names)
        | set(commands.editor.safe_exit.__func__.__code__.co_names)
        | set(commands.job.compile_build.__func__.__code__.co_names)
        | set(commands.operation.plan_execute.__func__.__code__.co_names)
    )
    assert not {
        "requests",
        "httpx",
        "urllib",
        "retry",
        "sleep",
        "registry",
        "poll",
        "terminate",
    } & names


def test_t34_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = cmd_root / "cli" / "uai" / "generated_commands" / "editor_session_build"
    task_doc = cmd_root / "docs" / "active" / "t34_control_command_migration.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t34_control_command_migration.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.editor.session" in text
        assert "client.editor.safe_exit" in text
        assert "client.job.compile_build" in text
        assert "client.operation.plan_execute" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text
