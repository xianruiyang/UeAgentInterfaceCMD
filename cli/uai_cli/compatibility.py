from __future__ import annotations

from typing import Any


def _status_data(status_payload: dict[str, Any]) -> dict[str, Any]:
    data = status_payload.get("data")
    return data if isinstance(data, dict) else {}


def build_compatibility_report(
    *,
    cli_version: str,
    status_payload: dict[str, Any],
    command_manifest: dict[str, Any] | None = None,
    expected_plugin_version_tag: str = "",
) -> dict[str, Any]:
    data = _status_data(status_payload)
    plugin_version_tag = str(data.get("version_tag") or "")
    server_running = bool(data.get("running", False))
    issues: list[str] = []
    warnings: list[str] = []

    if not bool(status_payload.get("ok", False)):
        issues.append("status_not_ok")
    if not server_running:
        issues.append("server_not_running")
    if not plugin_version_tag:
        warnings.append("plugin_version_tag_missing")
    if expected_plugin_version_tag and plugin_version_tag != expected_plugin_version_tag:
        issues.append("plugin_version_tag_mismatch")

    manifest_summary: dict[str, Any] = {}
    if command_manifest:
        manifest_summary = {
            "schema": command_manifest.get("schema", ""),
            "command_count": command_manifest.get("command_count", 0),
            "documented_count": command_manifest.get("documented_count", 0),
            "implemented_count": command_manifest.get("implemented_count", 0),
            "smoke_tested_count": command_manifest.get("smoke_tested_count", 0),
            "warnings": command_manifest.get("warnings", []),
        }
    else:
        warnings.append("command_manifest_not_loaded")

    return {
        "success": not issues,
        "cli_version": cli_version,
        "plugin_version_tag": plugin_version_tag,
        "expected_plugin_version_tag": expected_plugin_version_tag,
        "server_running": server_running,
        "issues": issues,
        "warnings": warnings,
        "command_manifest": manifest_summary,
    }
