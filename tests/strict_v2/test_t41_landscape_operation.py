from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

import pytest

from uai.commands import _BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = (
    "landscape.create",
    "landscape.height_delta",
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
        command_id: _BINDING_CATALOG.find(command_id) for command_id in COMMAND_IDS
    }
    assert all(
        binding is not None
        and binding.command_id == command_id
        and binding.namespace == "landscape"
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def _height_delta_params() -> dict[str, Any]:
    return {
        "delta": {"samples": [1.0]},
        "region": {"x": 0, "y": 0, "width": 1, "height": 1},
        "space_contract": {
            "semantic_frame_id": "landscape-local-sample-grid",
            "unit": "height-sample",
        },
        "target_ref": "/Game/StrictV2/T41/Landscape_Default",
    }


