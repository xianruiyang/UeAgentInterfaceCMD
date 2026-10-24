from __future__ import annotations

from pathlib import Path
from typing import Any
import re
import pytest

from uai.commands import _BINDING_CATALOG, bind_generated_commands


METHODS = {
    "timeline.sequence.create": ("timeline", "sequence_create"),
}
DORMANT_METHODS = {
    "timeline.sequence.read": ("timeline", "sequence_read"),
    "timeline.sequence.structure.replace": ("timeline", "sequence_structure_replace"),
    "timeline.widget_animation.read": ("timeline", "widget_animation_read"),
}


class _FakeClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id, params):
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _bindings():
    bindings = {command_id: _BINDING_CATALOG.find(command_id) for command_id in METHODS}
    assert all(
        binding is not None
        and (binding.namespace, binding.method) == METHODS[command_id]
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def _dormant_bindings():
    bindings = {
        command_id: _BINDING_CATALOG.find(command_id)
        for command_id in DORMANT_METHODS
    }
    assert all(binding is not None and binding.status == "dormant" for binding in bindings.values())
    generated = bind_generated_commands(_FakeClient())
    for command_id, binding in bindings.items():
        namespace = getattr(generated, binding.namespace)
        with pytest.raises(AttributeError):
            getattr(namespace, binding.method)
    return bindings


def _params(binding):
    samples = {
        "string": "fixture",
        "integer": 1,
        "number": 1.0,
        "boolean": True,
        "array": [],
        "object": {},
    }
    return {
        parameter.name: samples.get(parameter.wire_type, {})
        for parameter in binding.parameters
    }


def test_hjson_operations_are_dormant_and_have_no_named_sdk_method() -> None:
    _dormant_bindings()
