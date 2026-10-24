from __future__ import annotations

from pathlib import Path

from uai.commands import _BINDING_CATALOG, bind_generated_commands


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
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_projection():
    bindings = {
        command_id: _BINDING_CATALOG.find(command_id)
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


