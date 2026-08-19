from __future__ import annotations

from pathlib import Path

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = (
    "operation.status",
    "operation.receipt",
    "operation.cancel",
    "operation.resume",
    "operation.reconcile",
    "operation.release",
)


class _FakeClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, object], str]] = []

    def execute_exact(
        self,
        command_id: str,
        params: dict[str, object],
        *,
        contract_hash: str,
    ) -> dict[str, object]:
        self.calls.append((command_id, params, contract_hash))
        return {"ok": True}

    def execute(
        self,
        command_id: str,
        params: dict[str, object],
    ) -> dict[str, object]:
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_projection():
    bindings = {
        command_id: BINDING_CATALOG.find(command_id)
        for command_id in COMMAND_IDS
    }
    assert all(item is not None for item in bindings.values())
    return bindings


def _operation_ref() -> dict[str, str]:
    return {
        "operation_id": "operation-1",
        "owner_lease_id": "lease-1",
        "server_session_id": "server-session-1",
    }


def test_default_catalog_publishes_the_six_t32_lifecycle_bindings() -> None:
    bindings = _require_projection()
    for command_id, binding in bindings.items():
        assert binding is not None
        assert binding.command_id == command_id
        assert binding.binding_hash.startswith("sha256:")
        assert len(binding.binding_hash) == len("sha256:") + 64
        assert binding.namespace == "operation"


def test_status_receipt_and_release_preserve_the_exact_operation_ref() -> None:
    _require_projection()
    client = _FakeClient()
    commands = bind_generated_commands(client).operation
    operation_ref = _operation_ref()
    commands.status(operation_ref)
    commands.receipt(operation_ref)
    commands.release(operation_ref)
    assert [call[0] for call in client.calls] == [
        "operation.status",
        "operation.receipt",
        "operation.release",
    ]
    assert all(call[1] == {"operation_ref": operation_ref} for call in client.calls)


def test_generation_and_cancel_fences_are_forwarded_without_replay() -> None:
    _require_projection()
    client = _FakeClient()
    commands = bind_generated_commands(client).operation
    operation_ref = _operation_ref()
    commands.resume(operation_ref, 7)
    commands.reconcile(operation_ref, 7)
    commands.cancel(operation_ref, "user_cancelled")
    assert client.calls[0][1] == {
        "operation_ref": operation_ref,
        "expected_generation": 7,
    }
    assert client.calls[1][1] == {
        "operation_ref": operation_ref,
        "expected_generation": 7,
    }
    assert client.calls[2][1] == {
        "operation_ref": operation_ref,
        "reason": "user_cancelled",
    }
    assert len(client.calls) == 3


def test_t32_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_projection()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = cmd_root / "cli" / "uai" / "generated_commands" / "long_running"
    task_doc = cmd_root / "docs" / "active" / "t32_long_running.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t32_long_running.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.operation.status" in text
        assert "client.operation.resume" in text
        assert "client.operation.cancel" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text
