from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .project_paths import find_development_project_root, runtime_logs_dir
from .utils import now_compact, save_json_file


INDEX_FILE_NAME = "uai_cli_index.json"


def index_path(app_root: Path) -> Path:
    project_root = find_development_project_root(app_root, include_cwd=False)
    return runtime_logs_dir(app_root, project_root) / INDEX_FILE_NAME


def _load_index(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"schema": "ue_agent_interface.runtime_index.v1", "entries": []}
    with path.open("r", encoding="utf-8-sig") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        return {"schema": "ue_agent_interface.runtime_index.v1", "entries": []}
    entries = data.get("entries")
    if not isinstance(entries, list):
        data["entries"] = []
    return data


def summarize_report(report_path: Path, payload: dict[str, Any]) -> dict[str, Any]:
    phase = payload.get("phase")
    failed_command = ""
    failed_error = ""
    if isinstance(phase, dict):
        failed_command = str(phase.get("failed_command") or "")
        failed_error = str(phase.get("failed_error") or "")
    phases = payload.get("phases")
    if isinstance(phases, list):
        for item in phases:
            if isinstance(item, dict) and item.get("failed_command"):
                failed_command = str(item.get("failed_command") or "")
                failed_error = str(item.get("failed_error") or "")
                break
    return {
        "indexed_at": now_compact(),
        "generated_at": payload.get("generated_at", ""),
        "task_id": payload.get("task_id", ""),
        "success": bool(payload.get("success", False)),
        "cli_version": payload.get("cli_version", ""),
        "report_file": str(report_path),
        "failed_phase_index": payload.get("failed_phase_index"),
        "failed_command": failed_command,
        "failed_error": failed_error,
    }


def record_report(app_root: Path, report_path: Path, payload: dict[str, Any], *, max_entries: int = 500) -> Path:
    path = index_path(app_root)
    data = _load_index(path)
    entries = data.setdefault("entries", [])
    if not isinstance(entries, list):
        entries = []
        data["entries"] = entries
    entry = summarize_report(report_path, payload)
    entries[:] = [item for item in entries if not isinstance(item, dict) or item.get("report_file") != str(report_path)]
    entries.append(entry)
    if len(entries) > max_entries:
        del entries[: len(entries) - max_entries]
    data["updated_at"] = now_compact()
    data["entry_count"] = len(entries)
    save_json_file(path, data)
    return path


def _build_stats(entries: list[dict[str, Any]]) -> dict[str, Any]:
    by_command: dict[str, int] = {}
    success_count = 0
    failure_count = 0
    for entry in entries:
        if entry.get("success"):
            success_count += 1
        else:
            failure_count += 1
        command = str(entry.get("failed_command") or "")
        if command:
            by_command[command] = by_command.get(command, 0) + 1
    return {
        "success_count": success_count,
        "failure_count": failure_count,
        "failed_command_counts": dict(sorted(by_command.items(), key=lambda item: item[1], reverse=True)),
    }


def read_index(
    app_root: Path,
    limit: int = 20,
    *,
    failed_only: bool = False,
    command: str | None = None,
    task_id: str | None = None,
    stats: bool = False,
) -> dict[str, Any]:
    path = index_path(app_root)
    data = _load_index(path)
    entries = data.get("entries", [])
    if isinstance(entries, list):
        filtered = [entry for entry in entries if isinstance(entry, dict)]
        if failed_only:
            filtered = [entry for entry in filtered if not entry.get("success")]
        if command:
            filtered = [entry for entry in filtered if entry.get("failed_command") == command]
        if task_id:
            filtered = [entry for entry in filtered if entry.get("task_id") == task_id]
        if stats:
            data["stats"] = _build_stats(filtered)
        data["entries"] = filtered[-limit:]
        data["filtered_count"] = len(filtered)
    data["index_file"] = str(path)
    return data
