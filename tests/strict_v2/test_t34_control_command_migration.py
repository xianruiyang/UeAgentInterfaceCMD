from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = (
    "editor.safe_exit",
    "editor.session",
    "job.compile_build",
    "operation.plan.execute",
)

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
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_bindings():
    bindings = {
        command_id: _BINDING_CATALOG.find(command_id) for command_id in COMMAND_IDS
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


