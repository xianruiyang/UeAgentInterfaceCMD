from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands


COMMAND_ID = "blueprint.node.candidates"


class _RecordingClient:
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


def _binding():
    binding = _BINDING_CATALOG.find(COMMAND_ID)
    assert binding is not None
    assert binding.namespace == "blueprint"
    assert binding.method == "node_candidates"
    assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
    assert binding.binding_hash != "sha256:" + "0" * 64
    return binding


def _params() -> dict[str, Any]:
    return {
        "target": "/Game/UAI/StrictV2/T11/BP_NodeFixture.BP_NodeFixture",
        "graph_name": "EventGraph",
        "query": "branch",
    }


