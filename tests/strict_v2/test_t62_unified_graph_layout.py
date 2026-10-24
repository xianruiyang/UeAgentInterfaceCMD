from __future__ import annotations

from pathlib import Path

from uai.commands import _BINDING_CATALOG, bind_generated_commands


class _RecordingClient:
    def __init__(self) -> None:
        self.calls = []

    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id, params):
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(command_id, params, contract_hash=binding.binding_hash)


