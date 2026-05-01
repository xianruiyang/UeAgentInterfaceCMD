from __future__ import annotations

import json
import os
import platform
import subprocess
import shutil
import sys
import zipfile
from pathlib import Path
from typing import Any

from .project_paths import find_development_project_root, runtime_logs_dir
from .utils import get_hostname, now_compact, save_json_file
from .visual_validation import validate_visual_artifacts


CRASH_ROOT_NAME = "crashes"


def build_run_id(subcommand: str, task_id: str | None = None) -> str:
    prefix = task_id or subcommand or "uai"
    safe = "".join(ch if ch.isalnum() or ch in {"_", "-"} else "_" for ch in prefix)[:48]
    return f"{safe}_{now_compact()}_{get_hostname()}"


def classify_failure(*, exit_code: int, error: BaseException | None, report_payload: dict[str, Any] | None) -> str:
    if error is not None:
        message = str(error).lower()
        if "请求超时" in message or "timed out" in message or "timeout" in message:
            return "Timeout"
        if "网络错误" in message or "connection" in message or "refused" in message:
            return "ServiceLost"
        return "CliException"
    if report_payload:
        visuals = validate_visual_artifacts(report_payload)
        if any(result.get("success") and not result.get("appears_non_empty", False) for result in visuals):
            return "BlackScreenshot"
        phase = report_payload.get("phase")
        if isinstance(phase, dict) and phase.get("failed_command"):
            return "CommandFailed"
        if report_payload.get("failed_phase_index") is not None:
            return "CommandFailed"
    if exit_code != 0:
        return "CommandFailed"
    return "NoFailure"


def _latest_file(root: Path, patterns: list[str]) -> Path | None:
    candidates: list[Path] = []
    for pattern in patterns:
        candidates.extend(path for path in root.glob(pattern) if path.is_file())
    if not candidates:
        return None
    return max(candidates, key=lambda item: item.stat().st_mtime)


def _copy_if_exists(source: Path | None, target_dir: Path) -> str:
    if source is None or not source.exists() or not source.is_file():
        return ""
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / source.name
    shutil.copy2(source, target)
    return str(target)


def _latest_ue_log(project_root: Path | None) -> Path | None:
    if project_root is None:
        return None
    return _latest_file(project_root / "Saved" / "Logs", ["*.log"])


def _latest_crash_context(project_root: Path | None) -> Path | None:
    if project_root is None:
        return None
    crash_root = project_root / "Saved" / "Crashes"
    if not crash_root.exists():
        return None
    return _latest_file(crash_root, ["**/CrashContext.runtime-xml", "**/*.dmp", "**/diagnostics.txt"])


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
    subcommand: str,
    exit_code: int,
    report_path: Path | None = None,
    report_payload: dict[str, Any] | None = None,
    error: BaseException | None = None,
    request_files: list[Path] | None = None,
    replay_commands: list[list[str]] | None = None,
    run_id: str | None = None,
) -> dict[str, Any]:
    project_root = find_development_project_root(app_root, include_cwd=False)
    crash_root = runtime_logs_dir(app_root, project_root) / CRASH_ROOT_NAME
    crash_id = run_id or build_run_id(subcommand, str(report_payload.get("task_id")) if report_payload else None)
    crash_dir = crash_root / crash_id
    crash_dir.mkdir(parents=True, exist_ok=True)

    classification = classify_failure(exit_code=exit_code, error=error, report_payload=report_payload)
    copied: dict[str, str] = {}
    copied["report"] = _copy_if_exists(report_path, crash_dir)
    copied["ue_log"] = _copy_if_exists(_latest_ue_log(project_root), crash_dir / "ue")
    copied["ue_crash_context"] = _copy_if_exists(_latest_crash_context(project_root), crash_dir / "ue-crash")
    for path in request_files or []:
        copied.setdefault("requests", "")
        copied_path = _copy_if_exists(path, crash_dir / "requests")
        if copied_path:
            copied["requests"] = f"{copied.get('requests', '')};{copied_path}".strip(";")

    visual_results = validate_visual_artifacts(report_payload or {})
    manifest = {
        "schema": "ue_agent_interface.crash_capture.v1",
        "run_id": crash_id,
        "subcommand": subcommand,
        "classification": classification,
        "exit_code": exit_code,
        "generated_at": now_compact(),
        "app_root": str(app_root),
        "project_root": str(project_root or ""),
        "report_path": str(report_path or ""),
        "error": str(error) if error is not None else "",
        "process": _process_snapshot(),
        "visual_artifacts": visual_results,
        "copied_artifacts": copied,
        "replay_commands": replay_commands or [],
    }
    save_json_file(crash_dir / "manifest.json", manifest)

    summary = _build_summary_markdown(manifest)
    (crash_dir / "crash-summary.md").write_text(summary, encoding="utf-8")
    return {"success": True, "crash_dir": str(crash_dir), "manifest": manifest}


def _build_summary_markdown(manifest: dict[str, Any]) -> str:
    visuals = manifest.get("visual_artifacts") if isinstance(manifest.get("visual_artifacts"), list) else []
    invalid_visuals = [
        item for item in visuals if isinstance(item, dict) and item.get("success") and not item.get("appears_non_empty", False)
    ]
    lines = [
        "# UAI Crash Capture Summary",
        "",
        "## 结论",
        f"- 类型: `{manifest.get('classification', '')}`",
        f"- exit_code: `{manifest.get('exit_code', '')}`",
        f"- error: `{manifest.get('error', '')}`",
        "",
        "## 触发信息",
        f"- run_id: `{manifest.get('run_id', '')}`",
        f"- subcommand: `{manifest.get('subcommand', '')}`",
        f"- report: `{manifest.get('report_path', '')}`",
        "",
        "## 视觉输出",
        f"- visual_count: `{len(visuals)}`",
        f"- invalid_visual_count: `{len(invalid_visuals)}`",
        "",
        "## 关键日志",
    ]
    copied = manifest.get("copied_artifacts", {})
    if isinstance(copied, dict):
        for key, value in copied.items():
            if value:
                lines.append(f"- {key}: `{value}`")
    lines.extend(
        [
            "",
            "## 根因",
            "- 未经人工确认前保持为空；先用 manifest.json 与 report 定位命令、参数和 UE 日志。",
            "",
            "## 修复方案",
            "- 修复后必须补对应 CLI/UE 回归测试，并保留新的验证报告。",
        ]
    )
    return "\n".join(lines) + "\n"


def inspect_crash_dir(crash_dir: Path) -> dict[str, Any]:
    manifest_path = crash_dir / "manifest.json"
    if not manifest_path.exists():
        return {"success": False, "error": "manifest_not_found", "crash_dir": str(crash_dir)}
    with manifest_path.open("r", encoding="utf-8-sig") as file:
        manifest = json.load(file)
    return {"success": True, "crash_dir": str(crash_dir), "manifest": manifest}


def build_crash_signature(crash_dir: Path) -> dict[str, Any]:
    inspected = inspect_crash_dir(crash_dir)
    if not inspected.get("success"):
        return inspected
    manifest = inspected["manifest"]
    parts = [
        str(manifest.get("classification", "")),
        str(manifest.get("subcommand", "")),
        str(manifest.get("error", ""))[:160],
    ]
    report_path = Path(str(manifest.get("report_path") or ""))
    failed_command = ""
    if report_path.exists():
        try:
            report = json.loads(report_path.read_text(encoding="utf-8-sig"))
            phase = report.get("phase")
            if isinstance(phase, dict):
                failed_command = str(phase.get("failed_command") or "")
            phases = report.get("phases")
            if isinstance(phases, list):
                for item in phases:
                    if isinstance(item, dict) and item.get("failed_command"):
                        failed_command = str(item.get("failed_command") or "")
                        break
        except Exception:
            failed_command = ""
    parts.append(failed_command)
    signature_text = "|".join(parts)
    import hashlib

    signature = hashlib.sha256(signature_text.encode("utf-8")).hexdigest()[:16]
    return {
        "success": True,
        "crash_dir": str(crash_dir),
        "signature": signature,
        "signature_text": signature_text,
        "failed_command": failed_command,
    }


def _request_files(crash_dir: Path) -> list[Path]:
    request_root = crash_dir / "requests"
    if not request_root.exists():
        return []
    return sorted(path for path in request_root.rglob("*.json") if path.is_file())


def replay_crash_dir(crash_dir: Path, *, app_root: Path, dry_run: bool = True) -> dict[str, Any]:
    inspected = inspect_crash_dir(crash_dir)
    manifest = inspected.get("manifest") if inspected.get("success") else {}
    files = _request_files(crash_dir)
    commands: list[list[str]] = []
    replay_commands = manifest.get("replay_commands") if isinstance(manifest, dict) else None
    if isinstance(replay_commands, list):
        for item in replay_commands:
            if isinstance(item, list) and all(isinstance(value, str) for value in item):
                commands.append(item)
    if not commands:
        for path in files:
            payload = json.loads(path.read_text(encoding="utf-8-sig"))
            if isinstance(payload, dict) and "phases" in payload:
                commands.append([str(app_root / "run_uai_cli.py"), "run", "--plan", str(path), "--json-output"])
            elif isinstance(payload, dict) and ("commands" in payload or payload.get("command") == "exec_batch"):
                commands.append([str(app_root / "run_uai_cli.py"), "batch", "--file", str(path), "--json-output"])
    deduped: list[list[str]] = []
    seen: set[tuple[str, ...]] = set()
    for command in commands:
        key = tuple(command)
        if key in seen:
            continue
        seen.add(key)
        deduped.append(command)
    commands = deduped
    if not commands:
        return {"success": False, "dry_run": dry_run, "crash_dir": str(crash_dir), "error": "no_replay_commands"}
    if dry_run:
        return {"success": True, "dry_run": True, "crash_dir": str(crash_dir), "commands": commands}
    results: list[dict[str, Any]] = []
    for command in commands:
        proc = subprocess.run([sys.executable, *command], cwd=app_root, text=True, capture_output=True, timeout=300)
        results.append(
            {
                "command": command,
                "returncode": proc.returncode,
                "stdout_tail": proc.stdout[-4000:],
                "stderr_tail": proc.stderr[-4000:],
            }
        )
        if proc.returncode != 0:
            break
    return {"success": all(item["returncode"] == 0 for item in results), "dry_run": False, "results": results}


def generate_batch_bisect_files(crash_dir: Path) -> dict[str, Any]:
    files = _request_files(crash_dir)
    generated: list[str] = []
    for path in files:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        commands = payload.get("commands") if isinstance(payload, dict) else None
        if payload.get("command") == "exec_batch" and isinstance(payload.get("params"), dict):
            commands = payload["params"].get("commands")
        if not isinstance(commands, list) or len(commands) < 2:
            continue
        out_dir = crash_dir / "bisect"
        out_dir.mkdir(parents=True, exist_ok=True)
        midpoint = len(commands) // 2
        for label, subset in [("first_half", commands[:midpoint]), ("second_half", commands[midpoint:])]:
            out_path = out_dir / f"{path.stem}_{label}.json"
            out_payload = {"stop_on_error": True, "commands": subset}
            out_path.write_text(json.dumps(out_payload, ensure_ascii=False, indent=2), encoding="utf-8")
            generated.append(str(out_path))
    return {"success": True, "crash_dir": str(crash_dir), "generated_files": generated}


def find_latest_crash(app_root: Path) -> Path | None:
    project_root = find_development_project_root(app_root, include_cwd=False)
    crash_root = runtime_logs_dir(app_root, project_root) / CRASH_ROOT_NAME
    if not crash_root.exists():
        return None
    candidates = [path for path in crash_root.iterdir() if path.is_dir()]
    if not candidates:
        return None
    return max(candidates, key=lambda item: item.stat().st_mtime)


def pack_crash_dir(crash_dir: Path, output_file: Path | None = None) -> Path:
    output = output_file or crash_dir.with_suffix(".zip")
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in crash_dir.rglob("*"):
            if path.is_file():
                archive.write(path, path.relative_to(crash_dir.parent))
    return output
