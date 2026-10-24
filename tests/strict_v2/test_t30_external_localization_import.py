from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands


COMMAND_ID = "external.localization.po.import"

SUCCESSOR_COMMANDS = {
    "localization_apply_json": (
        "content_graph.import_workspace",
    ),
    "localization_compile_text": (
        "job.compile_build",
        "operation.status",
        "operation.receipt",
        "operation.release",
    ),
    "localization_diff_json": ("content_graph.compound",),
    "localization_export_json": ("content_graph.export_workspace",),
    "localization_export_po": (
        "job.compile_build",
        "operation.status",
        "operation.receipt",
        "operation.release",
    ),
    "localization_gather_text": (
        "job.compile_build",
        "operation.status",
        "operation.receipt",
        "operation.release",
    ),
    "localization_import_po": (
        "external.localization.po.import",
        "content_graph.compound",
    ),
    "localization_preview_culture": (
        "content_graph.compound",
        "editor.session",
        "operation.status",
        "operation.receipt",
        "operation.release",
    ),
    "localization_query_targets": ("content_graph.compound",),
    "localization_report": ("content_graph.compound",),
    "localization_validate_json": ("content_graph.compound",),
    "string_table_apply_json": (
        "content_graph.import_workspace",
    ),
    "string_table_diff_json": ("content_graph.compound",),
    "string_table_export_json": ("content_graph.export_workspace",),
    "string_table_validate_json": ("content_graph.compound",),
}

CONTENT_GRAPH_ACTIONS = {
    "localization_diff_json": "localization.diff",
    "localization_import_po": "localization.target.read",
    "localization_preview_culture": "localization.culture.read",
    "localization_query_targets": "localization.query_targets",
    "localization_report": "localization.report",
    "localization_validate_json": "localization.validate",
    "string_table_diff_json": "string_table.diff",
    "string_table_validate_json": "string_table.validate",
}

HJSON_PROVIDER_ROWS = {
    "localization_apply_json",
    "localization_export_json",
    "string_table_apply_json",
    "string_table_export_json",
}

LONG_RUNNING_POLICIES = {
    "localization_compile_text": "policy:owned-tool:localization-compile-text/v1",
    "localization_export_po": "policy:owned-tool:localization-export-po/v1",
    "localization_gather_text": "policy:owned-tool:localization-gather-text/v1",
    "localization_preview_culture": "policy:runtime-session:culture-preview/v1",
}


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


def _require_binding():
    binding = _BINDING_CATALOG.find(COMMAND_ID)
    assert binding is not None
    assert binding.command_id == COMMAND_ID
    assert binding.namespace == "external"
    assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
    assert binding.binding_hash != "sha256:" + "0" * 64
    return binding


