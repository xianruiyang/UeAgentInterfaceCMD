from __future__ import annotations

import hashlib
import os
import platform
import shutil
import zipfile
from pathlib import Path
from typing import Any

from .io import get_hostname, load_json_file, now_compact, save_json_file
from .project_paths import find_development_project_root, runtime_logs_dir
from .visual_validation import validate_visual_artifacts


CRASH_ROOT_NAME = "crashes"


def build_run_id(operation: str, task_id: str | None = None) -> str:
    prefix = task_id or operation or "uai"
    safe = "".join(
        char if char.isalnum() or char in {"_", "-"} else "_"
        for char in prefix
    )[:48]
    return f"{safe}_{now_compact()}_{get_hostname()}"


def classify_failure(
    *,
    exit_code: int,
    error: BaseException | None,
    report_payload: dict[str, Any] | None,
) -> str:
    if error is not None:
        message = str(error).casefold()
        if "timed out" in message or "timeout" in message:
            return "Timeout"
        if "connection" in message or "refused" in message:
            return "ServiceLost"
        return "ClientException"
    if report_payload:
        visuals = validate_visual_artifacts(report_payload)
        if any(
            result.get("success")
            and not result.get("appears_non_empty", False)
            for result in visuals
        ):
            return "BlackScreenshot"
    if exit_code != 0:
        return "CommandFailed"
    return "NoFailure"


def _latest_file(root: Path, patterns: tuple[str, ...]) -> Path | None:
    candidates: list[Path] = []
    for pattern in patterns:
        candidates.extend(
            path for path in root.glob(pattern) if path.is_file()
        )
    if not candidates:
        return None
    return max(candidates, key=lambda item: item.stat().st_mtime)


def _copy_if_exists(source: Path | None, target_dir: Path) -> str:
    if source is None or not source.is_file():
        return ""
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / source.name
    shutil.copy2(source, target)
    return str(target)


def _latest_ue_log(project_root: Path | None) -> Path | None:
    if project_root is None:
        return None
    return _latest_file(project_root / "Saved" / "Logs", ("*.log",))


def _latest_crash_context(project_root: Path | None) -> Path | None:
    if project_root is None:
        return None
    crash_root = project_root / "Saved" / "Crashes"
    if not crash_root.is_dir():
        return None
    return _latest_file(
        crash_root,
        (
            "**/CrashContext.runtime-xml",
            "**/*.dmp",
            "**/diagnostics.txt",
        ),
    )


def _process_snapshot() -> dict[str, Any]:
    return {
        "pid": os.getpid(),
        "platform": platform.platform(),
        "python": platform.python_version(),
        "hostname": get_hostname(),
    }


def collect_failure_artifacts(
    *,
    app_root: Path,
    operation: str,
    exit_code: int,
    report_path: Path | None = None,
    report_payload: dict[str, Any] | None = None,
    error: BaseException | None = None,
    request_files: list[Path] | None = None,
    run_id: str | None = None,
) -> dict[str, Any]:
    project_root = find_development_project_root(
        app_root,
        include_cwd=False,
    )
    crash_root = (
        runtime_logs_dir(app_root, project_root) / CRASH_ROOT_NAME
    )
    task_id = (
        str(report_payload.get("task_id"))
        if report_payload and report_payload.get("task_id")
        else None
    )
    crash_id = run_id or build_run_id(operation, task_id)
    crash_dir = crash_root / crash_id
    crash_dir.mkdir(parents=True, exist_ok=True)

    copied: dict[str, str] = {
        "report": _copy_if_exists(report_path, crash_dir),
        "ue_log": _copy_if_exists(
            _latest_ue_log(project_root),
            crash_dir / "ue",
        ),
        "ue_crash_context": _copy_if_exists(
            _latest_crash_context(project_root),
            crash_dir / "ue-crash",
        ),
    }
    copied_requests: list[str] = []
    for path in request_files or []:
        copied_path = _copy_if_exists(path, crash_dir / "requests")
        if copied_path:
            copied_requests.append(copied_path)
    if copied_requests:
        copied["requests"] = ";".join(copied_requests)

    manifest = {
        "schema": "ue_agent_interface.crash_capture.v2",
        "run_id": crash_id,
        "operation": operation,
        "classification": classify_failure(
            exit_code=exit_code,
            error=error,
            report_payload=report_payload,
        ),
        "exit_code": exit_code,
        "generated_at": now_compact(),
        "app_root": str(app_root),
        "project_root": str(project_root or ""),
        "report_path": str(report_path or ""),
        "error": str(error) if error is not None else "",
        "process": _process_snapshot(),
        "visual_artifacts": validate_visual_artifacts(
            report_payload or {}
        ),
        "copied_artifacts": copied,
    }
    save_json_file(crash_dir / "manifest.json", manifest)
    return {
        "success": True,
        "crash_dir": str(crash_dir),
        "manifest": manifest,
    }


def inspect_crash_dir(crash_dir: Path) -> dict[str, Any]:
    manifest_path = crash_dir / "manifest.json"
    if not manifest_path.is_file():
        return {
            "success": False,
            "error": "manifest_not_found",
            "crash_dir": str(crash_dir),
        }
    return {
        "success": True,
        "crash_dir": str(crash_dir),
        "manifest": load_json_file(manifest_path),
    }


def build_crash_signature(crash_dir: Path) -> dict[str, Any]:
    inspected = inspect_crash_dir(crash_dir)
    if not inspected.get("success"):
        return inspected
    manifest = inspected["manifest"]
    failed_command = ""
    report_value = str(manifest.get("report_path") or "")
    if report_value:
        report_path = Path(report_value)
        if report_path.is_file() and report_path.suffix.casefold() == ".json":
            try:
                report = load_json_file(report_path)
                failed_command = str(
                    report.get("failed_command") or ""
                )
            except (OSError, ValueError):
                failed_command = ""
    signature_text = "|".join(
        (
            str(manifest.get("classification", "")),
            str(manifest.get("operation", "")),
            str(manifest.get("error", ""))[:160],
            failed_command,
        )
    )
    signature = hashlib.sha256(
        signature_text.encode("utf-8")
    ).hexdigest()[:16]
    return {
        "success": True,
        "crash_dir": str(crash_dir),
        "signature": signature,
        "signature_text": signature_text,
        "failed_command": failed_command,
    }


def pack_crash_dir(
    crash_dir: Path,
    output_file: Path | None = None,
) -> Path:
    output = output_file or crash_dir.with_suffix(".zip")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        output,
        "w",
        compression=zipfile.ZIP_DEFLATED,
    ) as archive:
        for path in crash_dir.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(crash_dir.parent))
    return output
