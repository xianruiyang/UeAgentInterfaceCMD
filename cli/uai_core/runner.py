from __future__ import annotations

import copy
import json
import logging
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from .errors import PlanError
from .http_client import UaiHttpClient
from .niagara_guard import prepare_niagara_guarded_commands, verify_niagara_guard_response
from .reporting import PhaseReport, TimerMetrics
from .templating import deep_merge, normalize_phases, render_value
from .utils import load_json_file, now_compact


@dataclass(slots=True)
class PlanExecutionResult:
    success: bool
    task_id: str
    failed_phase_index: int | None
    phases: list[PhaseReport]
    resolved_plan: dict[str, Any]


def _is_exec_success(response_payload: dict[str, Any]) -> bool:
    if not isinstance(response_payload, dict):
        return False
    if not bool(response_payload.get("ok", False)):
        return False
    if str(response_payload.get("error", "")).strip():
        return False
    data = response_payload.get("data")
    if isinstance(data, dict) and "success" in data:
        return bool(data.get("success", False))
    return True


def _with_command_request_ids(commands: list[dict], phase_name: str) -> list[dict]:
    with_ids: list[dict] = []
    for index, command in enumerate(commands):
        command_copy = copy.deepcopy(command)
        command_copy.setdefault("request_id", f"{phase_name}_{index:03d}_{now_compact()}")
        with_ids.append(command_copy)
    return with_ids


def _extract_failed_fields(response_payload: dict[str, Any]) -> tuple[int | None, str | None, str | None, str | None]:
    data = response_payload.get("data")
    if not isinstance(data, dict):
        return None, None, None, None
    failed_index = data.get("failed_index")
    if not isinstance(failed_index, int):
        failed_index = None
    failed_command = data.get("failed_command")
    if not isinstance(failed_command, str):
        failed_command = None
    failed_request_id = data.get("failed_request_id")
    if not isinstance(failed_request_id, str):
        failed_request_id = None
    failed_error = data.get("failed_error")
    if not isinstance(failed_error, str):
        failed_error = None
    return failed_index, failed_command, failed_request_id, failed_error


def load_and_resolve_plan(plan_path: Path, vars_path: Path | None) -> dict:
    plan = load_json_file(plan_path)
    variables = {}
    if vars_path:
        variables = load_json_file(vars_path)

    now = datetime.now()
    auto_variables = {
        "short_tag": now.strftime("%m%d%H%M"),
        "short_date": now.strftime("%m%d"),
        "short_time": now.strftime("%H%M"),
        "short_tag_date": now.strftime("%m%d"),
        "short_tag_time": now.strftime("%H%M"),
        "short_tag_datetime": now.strftime("%m%d%H%M"),
    }
    defaults = plan.get("defaults", {})
    merged_variables = deep_merge(auto_variables, defaults)
    merged_variables = deep_merge(merged_variables, variables)

    resolved_plan = copy.deepcopy(plan)
    resolved_plan["phases"] = normalize_phases(plan.get("phases", []))
    resolved_plan["phases"] = render_value(resolved_plan["phases"], merged_variables)
    resolved_plan["asserts"] = render_value(plan.get("asserts", []), merged_variables)
    resolved_plan["resolved_variables"] = merged_variables
    resolved_plan.setdefault("task_id", f"task_{now_compact()}")
    return resolved_plan


def execute_batch(
    client: UaiHttpClient,
    phase_name: str,
    commands: list[dict],
    stop_on_error: bool,
    niagara_guard_enabled: bool = True,
    niagara_guard_strict: bool = True,
) -> PhaseReport:
    metrics = TimerMetrics()
    total_started = time.perf_counter()
    prepare_started = time.perf_counter()
    request_commands = _with_command_request_ids(commands, phase_name)
    guard_preparation = prepare_niagara_guarded_commands(
        commands=request_commands,
        phase_name=phase_name,
        guard_enabled=niagara_guard_enabled,
        strict_guard=niagara_guard_strict,
    )
    batch_request = {
        "request_id": f"batch_{phase_name}_{now_compact()}",
        "command": "exec_batch",
        "params": {
            "stop_on_error": stop_on_error,
            "commands": guard_preparation.commands,
        },
    }
    metrics.t_prepare_ms = (time.perf_counter() - prepare_started) * 1000

    http_result = client.post_json("/api/exec", batch_request)
    metrics.t_http_ms = http_result.elapsed_ms

    parse_started = time.perf_counter()
    response_payload = http_result.payload
    metrics.t_parse_ms = (time.perf_counter() - parse_started) * 1000

    verify_started = time.perf_counter()
    guard_verification = verify_niagara_guard_response(response_payload, guard_preparation)
    metrics.t_verify_ms = (time.perf_counter() - verify_started) * 1000
    metrics.t_total_ms = (time.perf_counter() - total_started) * 1000

    base_success = _is_exec_success(response_payload)
    success = base_success and guard_verification.success
    failed_index, failed_command, failed_request_id, failed_error = _extract_failed_fields(response_payload)

    if base_success and not guard_verification.success:
        failed_index = guard_verification.failed_index
        failed_command = guard_verification.failed_command
        failed_request_id = guard_verification.failed_request_id
        failed_error = guard_verification.failed_error
        response_payload = copy.deepcopy(response_payload)
        response_data = response_payload.setdefault("data", {})
        if isinstance(response_data, dict):
            response_data["failed_index"] = failed_index if failed_index is not None else -1
            response_data["failed_command"] = failed_command or ""
            response_data["failed_request_id"] = failed_request_id or ""
            response_data["failed_error"] = failed_error or ""
            response_data["guard_failed"] = True
            response_data["guard_injected_command_count"] = guard_preparation.injected_command_count
            response_data["guard_touched_system_paths"] = guard_preparation.touched_system_paths

    return PhaseReport(
        name=phase_name,
        success=success,
        request_id=batch_request["request_id"],
        stop_on_error=stop_on_error,
        failed_index=failed_index,
        failed_command=failed_command,
        failed_request_id=failed_request_id,
        failed_error=failed_error,
        response=response_payload,
        metrics=metrics,
    )


def execute_plan(
    client: UaiHttpClient,
    resolved_plan: dict,
    continue_on_error: bool = False,
    start_phase_index: int = 0,
    niagara_guard_enabled: bool = True,
    niagara_guard_strict: bool = True,
) -> PlanExecutionResult:
    phases_data: list[dict] = resolved_plan.get("phases", [])
    if not isinstance(phases_data, list):
        raise PlanError("resolved_plan.phases 必须是 list")

    phase_reports: list[PhaseReport] = []
    failed_phase_index: int | None = None

    for index, phase in enumerate(phases_data):
        if index < start_phase_index:
            continue

        phase_name = str(phase.get("name") or f"phase_{index}")
        stop_on_error = bool(phase.get("stop_on_error", True))
        commands = phase.get("commands")
        if not isinstance(commands, list):
            raise PlanError(f"phase `{phase_name}` 的 commands 必须是 list")

        logging.info("开始执行 phase=%s commands=%d", phase_name, len(commands))
        report = execute_batch(
            client=client,
            phase_name=phase_name,
            commands=commands,
            stop_on_error=stop_on_error,
            niagara_guard_enabled=niagara_guard_enabled,
            niagara_guard_strict=niagara_guard_strict,
        )
        phase_reports.append(report)

        if not report.success:
            failed_phase_index = index
            logging.error(
                "phase 失败: %s failed_index=%s failed_command=%s failed_error=%s",
                phase_name,
                report.failed_index,
                report.failed_command,
                report.failed_error,
            )
            if not continue_on_error:
                break

    overall_success = failed_phase_index is None

    if overall_success:
        asserts = resolved_plan.get("asserts", [])
        if isinstance(asserts, list) and asserts:
            logging.info("开始执行 asserts，数量=%d", len(asserts))
            assert_report = execute_batch(
                client=client,
                phase_name="asserts",
                commands=asserts,
                stop_on_error=True,
                niagara_guard_enabled=niagara_guard_enabled,
                niagara_guard_strict=niagara_guard_strict,
            )
            phase_reports.append(assert_report)
            if not assert_report.success:
                overall_success = False
                failed_phase_index = len(phases_data)

    return PlanExecutionResult(
        success=overall_success,
        task_id=str(resolved_plan.get("task_id")),
        failed_phase_index=failed_phase_index,
        phases=phase_reports,
        resolved_plan=resolved_plan,
    )


def dry_run_output(resolved_plan: dict) -> str:
    return json.dumps(resolved_plan, ensure_ascii=False, indent=2)
