from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

import pytest

from uai.commands import _BINDING_CATALOG, bind_generated_commands


METHODS = {
    "capture.image.execute": ("capture", "image_execute"),
    "capture.media.execute": ("capture", "media_execute"),
    "capture.render.execute": ("capture", "render_execute"),
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
        return self.execute_exact(command_id, params, contract_hash=binding.binding_hash)


def _bindings():
    values = {command_id: _BINDING_CATALOG.find(command_id) for command_id in METHODS}
    assert all(
        binding is not None
        and (binding.namespace, binding.method) == METHODS[command_id]
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in values.items()
    )
    return values


def _params(binding) -> dict[str, Any]:
    samples = {"string": "fixture", "integer": 1, "number": 1.0, "boolean": True, "array": [], "object": {}}
    return {item.name: samples.get(item.wire_type, {}) for item in binding.parameters}


def _named(client, binding, params) -> None:
    getattr(getattr(bind_generated_commands(client), binding.namespace), binding.method)(**params)


