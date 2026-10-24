from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

import pytest

from uai.commands import _BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = (
    "texture_graph.artifact.capture",
    "texture_graph.artifact.bake",
    "texture_graph.graph.link.mutate",
    "texture_graph.graph.node.mutate",
    "texture_graph.graph.parameter.mutate",
    "texture_graph.graph.validate_evaluate_settle",
    "texture_graph.runtime.probe",
)

SLEEP_COMMAND_IDS = (
    "texture_graph.graph.link.mutate",
    "texture_graph.graph.node.mutate",
    "texture_graph.graph.parameter.mutate",
)
KEEP_COMMAND_IDS = (
    "texture_graph.artifact.bake",
    "texture_graph.artifact.capture",
    "texture_graph.graph.validate_evaluate_settle",
    "texture_graph.runtime.probe",
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
        and binding.namespace == "texture_graph"
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    assert all(bindings[command_id].status == "dormant" for command_id in SLEEP_COMMAND_IDS)
    assert all(bindings[command_id].status == "active" for command_id in KEEP_COMMAND_IDS)
    return bindings


def test_t40_sleep_commands_are_dormant_and_not_named_sdk() -> None:
    bindings = _require_bindings()
    namespaces = bind_generated_commands(_FakeClient())
    for command_id in SLEEP_COMMAND_IDS:
        binding = bindings[command_id]
        assert binding.status == "dormant"
        assert not hasattr(namespaces.texture_graph, binding.method)


def test_t40_non_hjson_commands_remain_active_named_sdk() -> None:
    bindings = _require_bindings()
    namespaces = bind_generated_commands(_FakeClient())
    for command_id in KEEP_COMMAND_IDS:
        binding = bindings[command_id]
        assert binding.status == "active"
        assert hasattr(namespaces.texture_graph, binding.method)


def _capture_params() -> dict[str, Any]:
    return {
        "expected_settled_revision": "fixture-revision",
        "outputs": ["base_color"],
        "target_ref": "/Game/StrictV2/T40/TG_Default.TG_Default",
    }
