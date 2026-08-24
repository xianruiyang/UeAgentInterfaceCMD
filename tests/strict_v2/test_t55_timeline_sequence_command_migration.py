from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


METHODS = {
    "timeline.sequence.create": ("timeline", "sequence_create"),
    "timeline.sequence.read": ("timeline", "sequence_read"),
    "timeline.sequence.settings.update": ("timeline", "sequence_settings_update"),
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
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _bindings():
    bindings = {command_id: BINDING_CATALOG.find(command_id) for command_id in METHODS}
    assert all(
        binding is not None
        and (binding.namespace, binding.method) == METHODS[command_id]
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
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


def test_exact_default_inventory() -> None:
    assert len(METHODS) == 5
    _bindings()


def test_settings_update_named_method_forwards_one_exact_request() -> None:
    binding = _bindings()["timeline.sequence.settings.update"]
    client = _FakeClient()
    params = _params(binding)
    method = getattr(
        getattr(bind_generated_commands(client), binding.namespace),
        binding.method,
    )
    method(**params)
    assert client.calls == [(binding.command_id, params, binding.binding_hash)]


def test_settings_update_projection_has_no_transport_or_timeline_business() -> None:
    binding = _bindings()["timeline.sequence.settings.update"]
    method = getattr(
        getattr(bind_generated_commands(_FakeClient()), binding.namespace),
        binding.method,
    )
    assert not {
        "requests",
        "httpx",
        "urllib",
        "retry",
        "sleep",
        "registry",
        "save",
        "reload",
        "sequence",
        "timeline",
    } & set(method.__func__.__code__.co_names)


def test_t55_legacy_binding_and_tutorial_authority_exit() -> None:
    _bindings()
    root = Path(__file__).resolve().parents[2]
    helper = root / "cli/uai/generated_commands/t55_timeline_sequence_command_migration"
    docs = (
        root / "docs/active/t55_timeline_sequence_command_migration.md",
        root.parent
        / "Plugins/UeAgentInterface/docs/active/t55_timeline_sequence_command_migration.md",
    )
    assert not helper.exists()
    for document in docs:
        text = document.read_text(encoding="utf-8")
        for namespace, method in METHODS.values():
            assert f"client.{namespace}.{method}" in text
        assert "client.query.command_search" in text
        assert "client.query.command_detail" in text
        assert "content_graph.authoring_schema" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text
