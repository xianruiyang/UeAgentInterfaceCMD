from __future__ import annotations

import argparse
import json
import logging
import sys
import time
from pathlib import Path
from typing import Any

from .cleanup import cleanup_runtime_json
from .command_schema import validate_command_payloads
from .command_manifest import (
    build_command_manifest,
    command_names_from_batch,
    save_command_manifest,
    validate_command_names,
)
from .config import AppConfig, load_app_config
from .compatibility import build_compatibility_report
from .crash_capture import (
    build_crash_signature,
    collect_failure_artifacts,
    find_latest_crash,
    generate_batch_bisect_files,
    inspect_crash_dir,
    pack_crash_dir,
    replay_crash_dir,
)
from .e2e import run_local_e2e, run_ue_readonly_e2e
from .errors import ConfigError, HttpError, PlanError, UaiCliError
from .example_library import write_example_library
from .http_client import UaiHttpClient
from .logging_setup import setup_logging
from .naming import build_short_asset_name
from .release_verify import verify_pak_layout, write_coverage_matrix
from .reporting import build_report_file_path, save_report
from .runner import dry_run_output, execute_batch, execute_plan, load_and_resolve_plan
from .quality_gate import run_quality_gate
from .runtime_index import read_index, record_report
from .utils import load_json_file, mask_token, now_compact, parse_json_text
from .version import __version__


def _build_common_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="uai-cli", description="UeAgentInterface 外置命令行工具")
    parser.add_argument("--config", help="配置文件路径，默认读取 uai-cli.default.json")
    parser.add_argument("--base-url", help="覆盖配置中的 base_url")
    parser.add_argument("--token", help="覆盖配置中的 token")
    parser.add_argument("--timeout", type=int, help="覆盖配置中的 timeout_seconds")
    parser.add_argument("--allow-nonloopback", action="store_true", help="允许非本机地址")
    parser.add_argument("--json-output", action="store_true", help="输出 JSON 结果")
    parser.add_argument("--report-file", help="指定报告输出路径")
    parser.add_argument("--no-niagara-guard", action="store_true", help="关闭 Niagara 安全护栏（默认开启）")
    parser.add_argument("--allow-unsafe-niagara-mix", action="store_true", help="允许同批次 remove/add emitter（默认禁止）")
    parser.add_argument("--skip-compat-check", action="store_true", help="跳过 CLI/插件版本兼容检查")
    parser.add_argument("--no-crash-capture", action="store_true", help="本次执行失败时不生成 crash capture")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    return parser


def _add_common_overrides_to_subparser(sub_parser: argparse.ArgumentParser) -> None:
    sub_parser.add_argument("--config", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    sub_parser.add_argument("--base-url", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    sub_parser.add_argument("--token", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    sub_parser.add_argument("--timeout", type=int, default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    sub_parser.add_argument("--allow-nonloopback", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    sub_parser.add_argument("--json-output", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    sub_parser.add_argument("--report-file", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    sub_parser.add_argument("--no-niagara-guard", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    sub_parser.add_argument("--allow-unsafe-niagara-mix", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    sub_parser.add_argument("--skip-compat-check", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)
    sub_parser.add_argument("--no-crash-capture", action="store_true", default=argparse.SUPPRESS, help=argparse.SUPPRESS)


def _add_subcommands(parser: argparse.ArgumentParser) -> None:
    subparsers = parser.add_subparsers(dest="subcommand", required=True)

    doctor = subparsers.add_parser("doctor", help="检查服务端连通性和状态")
    _add_common_overrides_to_subparser(doctor)
    doctor.set_defaults(handler=handle_doctor)

    exec_cmd = subparsers.add_parser("exec", help="执行单条命令")
    _add_common_overrides_to_subparser(exec_cmd)
    exec_cmd.add_argument("--cmd", required=True, help="命令名")
    exec_cmd.add_argument("--params", help="JSON 字符串参数")
    exec_cmd.add_argument("--params-file", help="JSON 文件参数")
    exec_cmd.add_argument("--request-id", help="可选 request_id")
    exec_cmd.set_defaults(handler=handle_exec)

    batch = subparsers.add_parser("batch", help="执行批量命令文件")
    _add_common_overrides_to_subparser(batch)
    batch.add_argument("--file", required=True, help="batch JSON 文件路径")
    batch.set_defaults(handler=handle_batch)

    run = subparsers.add_parser("run", help="按 plan + vars 执行任务")
    _add_common_overrides_to_subparser(run)
    run.add_argument("--plan", required=True, help="plan.json 路径")
    run.add_argument("--vars", help="vars.json 路径")
    run.add_argument("--dry-run", action="store_true", help="仅展开计划，不调用服务端")
    run.add_argument("--continue-on-error", action="store_true", help="phase 失败后继续执行后续 phase")
    run.set_defaults(handler=handle_run)

    resume = subparsers.add_parser("resume", help="从报告恢复执行")
    _add_common_overrides_to_subparser(resume)
    resume.add_argument("--report", required=True, help="上次执行生成的 report.json")
    resume.add_argument("--retry-failed-phase", action="store_true", help="从失败 phase 重试")
    resume.add_argument("--continue-on-error", action="store_true", help="恢复时继续执行后续 phase")
    resume.set_defaults(handler=handle_resume)

    namegen = subparsers.add_parser("namegen", help="生成简短资产命名")
    _add_common_overrides_to_subparser(namegen)
    namegen.add_argument("--kind", required=True, help="类型：blueprint/niagara_system/niagara_emitter/material/umg")
    namegen.add_argument("--base", required=True, help="基础名称")
    namegen.add_argument("--max-len", type=int, default=20, help="最大长度（默认 20）")
    namegen.add_argument(
        "--tag-mode",
        choices=["none", "time", "date", "datetime"],
        default="none",
        help="后缀时间标签：none/time/date/datetime（默认 none）",
    )
    namegen.set_defaults(handler=handle_namegen)

    manifest = subparsers.add_parser("manifest", help="生成或查看插件命令清单")
    _add_common_overrides_to_subparser(manifest)
    manifest.add_argument("--output", help="写出 command manifest JSON")
    manifest.add_argument("--summary", action="store_true", help="只输出摘要")
    manifest.set_defaults(handler=handle_manifest)

    compat = subparsers.add_parser("compat", help="检查 CLI 与 UE 插件服务兼容性")
    _add_common_overrides_to_subparser(compat)
    compat.set_defaults(handler=handle_compat)

    crash = subparsers.add_parser("crash", help="收集、检查或打包失败现场")
    _add_common_overrides_to_subparser(crash)
    crash.add_argument("action", choices=["collect", "inspect", "pack", "signature", "replay", "bisect"], help="crash 操作")
    crash.add_argument("--path", help="指定 crash 目录；未指定时使用最新目录")
    crash.add_argument("--output", help="pack 输出 zip 路径")
    crash.add_argument("--execute", action="store_true", help="replay 时真实执行请求；默认只输出命令")
    crash.set_defaults(handler=handle_crash)

    index = subparsers.add_parser("index", help="查看 runtimeLogs 中的 CLI 报告索引")
    _add_common_overrides_to_subparser(index)
    index.add_argument("--limit", type=int, default=20, help="返回最近 N 条")
    index.add_argument("--failed-only", action="store_true", help="只看失败记录")
    index.add_argument("--command", help="按 failed_command 过滤")
    index.add_argument("--task-id", help="按 task_id 过滤")
    index.add_argument("--stats", action="store_true", help="输出统计摘要")
    index.set_defaults(handler=handle_index)

    release = subparsers.add_parser("release", help="生成覆盖矩阵或验证 Pak 分发布局")
    _add_common_overrides_to_subparser(release)
    release.add_argument("action", choices=["coverage", "pak-verify", "examples", "gate", "all"], help="release 检查动作")
    release.add_argument("--output-json", help="coverage 输出 JSON；默认写到 docs/generated")
    release.add_argument("--output-md", help="coverage 输出 Markdown；默认写到 docs/generated")
    release.add_argument("--run-tests", action="store_true", help="gate 时运行 CLI 单测")
    release.set_defaults(handler=handle_release)

    e2e = subparsers.add_parser("e2e", help="运行 golden E2E 检查")
    _add_common_overrides_to_subparser(e2e)
    e2e.add_argument("mode", choices=["local", "ue-readonly"], help="local 不需要 UE；ue-readonly 需要 UAI 服务")
    e2e.set_defaults(handler=handle_e2e)


def _resolve_config(args: argparse.Namespace) -> AppConfig:
    local_only_subcommands = {"namegen", "manifest", "crash", "index", "release"}
    if args.subcommand == "e2e" and getattr(args, "mode", "") == "local":
        local_only_subcommands.add("e2e")
    require_token = not (
        (args.subcommand == "run" and bool(getattr(args, "dry_run", False)))
        or args.subcommand in local_only_subcommands
    )
    guard_enabled_override: bool | None = None
    if bool(getattr(args, "no_niagara_guard", False)):
        guard_enabled_override = False
    guard_strict_override: bool | None = None
    if bool(getattr(args, "allow_unsafe_niagara_mix", False)):
        guard_strict_override = False
    return load_app_config(
        config_path=args.config,
        base_url=args.base_url,
        token=args.token,
        timeout_seconds=args.timeout,
        allow_nonloopback=args.allow_nonloopback,
        niagara_guard_enabled=guard_enabled_override,
        niagara_guard_strict=guard_strict_override,
        require_token=require_token,
    )


def _client_from_config(config: AppConfig) -> UaiHttpClient:
    return UaiHttpClient(config.base_url, config.token, config.timeout_seconds)


def _load_params(args: argparse.Namespace) -> dict:
    params: dict[str, Any] = {}
    if getattr(args, "params", None):
        params = parse_json_text(args.params)
    if getattr(args, "params_file", None):
        params = load_json_file(Path(args.params_file))
    return params


def _safe_print(payload: dict[str, Any], json_output: bool) -> None:
    if json_output:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return
    print(payload)


def _build_report_payload(config: AppConfig, content: dict[str, Any]) -> dict[str, Any]:
    report = dict(content)
    report["generated_at"] = now_compact()
    report["config_snapshot"] = {
        "base_url": config.base_url,
        "token_masked": mask_token(config.token),
        "timeout_seconds": config.timeout_seconds,
        "niagara_guard_enabled": config.niagara_guard_enabled,
        "niagara_guard_strict": config.niagara_guard_strict,
        "command_manifest_enabled": config.command_manifest_enabled,
        "compatibility_check_enabled": config.compatibility_check_enabled,
        "expected_plugin_version_tag": config.expected_plugin_version_tag,
        "crash_capture_enabled": config.crash_capture_enabled,
        "runtime_index_enabled": config.runtime_index_enabled,
        "param_validation_mode": config.param_validation_mode,
    }
    report["cli_version"] = __version__
    return report


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


def _write_report(config: AppConfig, args: argparse.Namespace, payload: dict[str, Any]) -> Path:
    report_path = Path(args.report_file) if getattr(args, "report_file", None) else build_report_file_path(
        config.reports_dir, str(payload.get("task_id", "task"))
    )
    save_report(report_path, payload)
    if config.runtime_index_enabled:
        try:
            record_report(config.app_root, report_path, payload)
        except Exception as error:
            logging.warning("runtime index 更新失败: %s", error)
    setattr(args, "_last_report_path", report_path)
    setattr(args, "_last_report_payload", payload)
    logging.info("报告已写入: %s", report_path)
    return report_path


def _run_cleanup_if_enabled(config: AppConfig, stage: str) -> None:
    if not config.auto_cleanup_enabled:
        return
    results = cleanup_runtime_json(
        app_root=config.app_root,
        reports_dir=config.reports_dir,
        cleanup_tmp_max=config.cleanup_tmp_max,
        cleanup_tmp_keep=config.cleanup_tmp_keep,
        cleanup_reports_max=config.cleanup_reports_max,
        cleanup_reports_keep=config.cleanup_reports_keep,
    )
    for result in results:
        if result.deleted_count > 0:
            logging.info(
                "自动清理(%s): %s before=%d deleted=%d after=%d",
                stage,
                result.target_dir,
                result.before_count,
                result.deleted_count,
                result.after_count,
            )


def _load_manifest_if_enabled(config: AppConfig) -> dict[str, Any] | None:
    if not config.command_manifest_enabled:
        return None
    return build_command_manifest()


def _validate_commands_with_manifest(config: AppConfig, command_names: list[str]) -> dict[str, Any] | None:
    manifest = _load_manifest_if_enabled(config)
    if manifest is None:
        return None
    unknown, warnings = validate_command_names(command_names, manifest)
    if unknown:
        raise PlanError(f"命令清单校验失败，未知命令: {', '.join(unknown)}")
    if warnings:
        logging.warning("命令清单警告: %s", "; ".join(warnings))
    return {
        "schema": manifest.get("schema", ""),
        "command_count": manifest.get("command_count", 0),
        "validated_command_count": len(command_names),
        "warnings": warnings,
    }


def _validate_payloads_with_manifest(
    config: AppConfig,
    commands: list[dict[str, Any]],
    manifest: dict[str, Any] | None,
) -> dict[str, Any] | None:
    if manifest is None or config.param_validation_mode == "off":
        return None
    validation = validate_command_payloads(
        commands,
        manifest,
        strict=config.param_validation_mode == "strict",
    )
    if not validation.get("success", True):
        issue_text = ", ".join(validation.get("issues", []) + validation.get("warnings", []))
        raise PlanError(f"命令参数 schema 校验失败: {issue_text}")
    warnings = validation.get("warnings", [])
    if warnings:
        logging.warning("命令参数 schema 警告: %s", "; ".join(warnings[:20]))
    return validation


def _compatibility_preflight(
    config: AppConfig,
    args: argparse.Namespace,
    client: UaiHttpClient,
    command_manifest: dict[str, Any] | None,
) -> dict[str, Any] | None:
    if not config.compatibility_check_enabled or bool(getattr(args, "skip_compat_check", False)):
        return None
    status = client.get("/api/status")
    report = build_compatibility_report(
        cli_version=__version__,
        status_payload=status.payload,
        command_manifest=command_manifest,
        expected_plugin_version_tag=config.expected_plugin_version_tag,
    )
    if not report["success"]:
        raise ConfigError(f"CLI/插件兼容检查失败: {', '.join(report.get('issues', []))}")
    return report


def _command_names_from_plan(resolved_plan: dict[str, Any]) -> list[str]:
    names: list[str] = []
    phases = resolved_plan.get("phases", [])
    if isinstance(phases, list):
        for phase in phases:
            if isinstance(phase, dict):
                commands = phase.get("commands", [])
                if isinstance(commands, list):
                    names.extend(command_names_from_batch(commands))
    asserts = resolved_plan.get("asserts", [])
    if isinstance(asserts, list):
        names.extend(command_names_from_batch(asserts))
    return names


def _request_files_from_args(args: argparse.Namespace) -> list[Path]:
    files: list[Path] = []
    for attr in ["file", "plan", "vars", "params_file", "report"]:
        value = getattr(args, attr, None)
        if value:
            files.append(Path(value))
    return files


def _build_replay_commands(args: argparse.Namespace, app_root: Path) -> list[list[str]]:
    subcommand = str(getattr(args, "subcommand", "") or "")
    if not subcommand or subcommand in {"crash", "manifest", "index"}:
        return []

    command: list[str] = [str(app_root / "run_uai_cli.py"), subcommand]
    for attr, flag in [
        ("config", "--config"),
        ("base_url", "--base-url"),
        ("timeout", "--timeout"),
    ]:
        value = getattr(args, attr, None)
        if value:
            command.extend([flag, str(value)])
    for attr, flag in [
        ("allow_nonloopback", "--allow-nonloopback"),
        ("json_output", "--json-output"),
        ("no_niagara_guard", "--no-niagara-guard"),
        ("allow_unsafe_niagara_mix", "--allow-unsafe-niagara-mix"),
        ("skip_compat_check", "--skip-compat-check"),
    ]:
        if bool(getattr(args, attr, False)):
            command.append(flag)
    command.append("--no-crash-capture")

    if subcommand == "exec":
        command.extend(["--cmd", str(args.cmd)])
        if getattr(args, "params_file", None):
            command.extend(["--params-file", str(args.params_file)])
        elif getattr(args, "params", None):
            command.extend(["--params", str(args.params)])
        if getattr(args, "request_id", None):
            command.extend(["--request-id", str(args.request_id)])
    elif subcommand == "batch":
        command.extend(["--file", str(args.file)])
    elif subcommand == "run":
        command.extend(["--plan", str(args.plan)])
        if getattr(args, "vars", None):
            command.extend(["--vars", str(args.vars)])
        if bool(getattr(args, "dry_run", False)):
            command.append("--dry-run")
        if bool(getattr(args, "continue_on_error", False)):
            command.append("--continue-on-error")
    elif subcommand == "resume":
        command.extend(["--report", str(args.report)])
        if bool(getattr(args, "retry_failed_phase", False)):
            command.append("--retry-failed-phase")
        if bool(getattr(args, "continue_on_error", False)):
            command.append("--continue-on-error")
    elif subcommand == "doctor":
        pass
    elif subcommand == "compat":
        pass
    elif subcommand == "e2e":
        command.append(str(args.mode))
    elif subcommand == "release":
        command.append(str(args.action))
        if getattr(args, "output_json", None):
            command.extend(["--output-json", str(args.output_json)])
        if getattr(args, "output_md", None):
            command.extend(["--output-md", str(args.output_md)])
        if bool(getattr(args, "run_tests", False)):
            command.append("--run-tests")
    else:
        return []
    return [command]


def _maybe_collect_failure(
    config: AppConfig | None,
    args: argparse.Namespace,
    *,
    exit_code: int,
    error: BaseException | None = None,
) -> None:
    if config is None or exit_code == 0:
        return
    if not config.crash_capture_enabled or bool(getattr(args, "no_crash_capture", False)):
        return
    if getattr(args, "subcommand", "") in {"crash", "manifest", "index"}:
        return
    try:
        result = collect_failure_artifacts(
            app_root=config.app_root,
            subcommand=str(getattr(args, "subcommand", "")),
            exit_code=exit_code,
            report_path=getattr(args, "_last_report_path", None),
            report_payload=getattr(args, "_last_report_payload", None),
            error=error,
            request_files=_request_files_from_args(args),
            replay_commands=_build_replay_commands(args, config.app_root),
        )
        logging.error("失败现场已收集: %s", result.get("crash_dir"))
        setattr(args, "_last_crash_dir", result.get("crash_dir"))
    except Exception as capture_error:
        logging.exception("失败现场收集失败: %s", capture_error)


def handle_doctor(args: argparse.Namespace, config: AppConfig) -> int:
    client = _client_from_config(config)
    started = time.perf_counter()
    ping = client.get("/api/ping")
    status = client.get("/api/status")
    elapsed = (time.perf_counter() - started) * 1000
    manifest = _load_manifest_if_enabled(config)
    compatibility = build_compatibility_report(
        cli_version=__version__,
        status_payload=status.payload,
        command_manifest=manifest,
        expected_plugin_version_tag=config.expected_plugin_version_tag,
    )
    payload = {
        "success": bool(compatibility.get("success", True)),
        "ping": ping.payload,
        "status": status.payload,
        "compatibility": compatibility,
        "metrics": {
            "t_ping_ms": ping.elapsed_ms,
            "t_status_ms": status.elapsed_ms,
            "t_total_ms": elapsed,
        },
    }
    _safe_print(payload, args.json_output)
    _write_report(config, args, _build_report_payload(config, {"task_id": "doctor", **payload}))
    return 0 if payload["success"] else 2


def handle_exec(args: argparse.Namespace, config: AppConfig) -> int:
    client = _client_from_config(config)
    manifest = _load_manifest_if_enabled(config)
    manifest_validation = None
    if manifest is not None:
        unknown, warnings = validate_command_names([args.cmd], manifest)
        if unknown:
            raise PlanError(f"命令清单校验失败，未知命令: {', '.join(unknown)}")
        manifest_validation = {
            "schema": manifest.get("schema", ""),
            "command_count": manifest.get("command_count", 0),
            "validated_command_count": 1,
            "warnings": warnings,
        }
    compatibility = _compatibility_preflight(config, args, client, manifest)
    params = _load_params(args)
    param_validation = _validate_payloads_with_manifest(
        config,
        [{"command": args.cmd, "params": params}],
        manifest,
    )
    request_payload = {
        "request_id": args.request_id or f"exec_{now_compact()}",
        "command": args.cmd,
        "params": params,
    }
    started = time.perf_counter()
    result = client.post_json("/api/exec", request_payload)
    elapsed = (time.perf_counter() - started) * 1000
    payload = {
        "success": _is_exec_success(result.payload),
        "request": request_payload,
        "response": result.payload,
        "command_manifest_validation": manifest_validation,
        "command_param_validation": param_validation,
        "compatibility": compatibility,
        "metrics": {"t_http_ms": result.elapsed_ms, "t_total_ms": elapsed},
    }
    _safe_print(payload, args.json_output)
    _write_report(config, args, _build_report_payload(config, {"task_id": "exec", **payload}))
    return 0 if payload["success"] else 2


def _parse_batch_file(file_path: Path) -> tuple[list[dict[str, Any]], bool]:
    raw_payload = load_json_file(file_path)
    if raw_payload.get("command") == "exec_batch":
        params = raw_payload.get("params")
        if not isinstance(params, dict):
            raise PlanError("exec_batch 缺少 params")
        commands = params.get("commands")
        if not isinstance(commands, list):
            raise PlanError("exec_batch.params 缺少 commands[]")
        stop_on_error = bool(params.get("stop_on_error", True))
        return commands, stop_on_error

    commands = raw_payload.get("commands")
    if not isinstance(commands, list):
        raise PlanError("batch 文件缺少 commands[]")
    stop_on_error = bool(raw_payload.get("stop_on_error", True))
    return commands, stop_on_error


def handle_batch(args: argparse.Namespace, config: AppConfig) -> int:
    client = _client_from_config(config)
    commands, stop_on_error = _parse_batch_file(Path(args.file))
    manifest = _load_manifest_if_enabled(config)
    manifest_validation = None
    if manifest is not None:
        command_names = command_names_from_batch(commands)
        unknown, warnings = validate_command_names(command_names, manifest)
        if unknown:
            raise PlanError(f"命令清单校验失败，未知命令: {', '.join(unknown)}")
        manifest_validation = {
            "schema": manifest.get("schema", ""),
            "command_count": manifest.get("command_count", 0),
            "validated_command_count": len(command_names),
            "warnings": warnings,
        }
    param_validation = _validate_payloads_with_manifest(config, commands, manifest)
    compatibility = _compatibility_preflight(config, args, client, manifest)
    started = time.perf_counter()
    phase_report = execute_batch(
        client=client,
        phase_name="batch",
        commands=commands,
        stop_on_error=stop_on_error,
        niagara_guard_enabled=config.niagara_guard_enabled,
        niagara_guard_strict=config.niagara_guard_strict,
    )
    elapsed = (time.perf_counter() - started) * 1000

    payload = {
        "success": phase_report.success,
        "request_file": str(Path(args.file)),
        "command_manifest_validation": manifest_validation,
        "command_param_validation": param_validation,
        "compatibility": compatibility,
        "phase": {
            "name": phase_report.name,
            "request_id": phase_report.request_id,
            "failed_index": phase_report.failed_index,
            "failed_command": phase_report.failed_command,
            "failed_request_id": phase_report.failed_request_id,
            "failed_error": phase_report.failed_error,
        },
        "response": phase_report.response,
        "metrics": {
            "t_prepare_ms": phase_report.metrics.t_prepare_ms,
            "t_http_ms": phase_report.metrics.t_http_ms,
            "t_parse_ms": phase_report.metrics.t_parse_ms,
            "t_verify_ms": phase_report.metrics.t_verify_ms,
            "t_total_ms": elapsed,
        },
    }
    _safe_print(payload, args.json_output)
    _write_report(config, args, _build_report_payload(config, {"task_id": "batch", **payload}))
    return 0 if payload["success"] else 2


def handle_run(args: argparse.Namespace, config: AppConfig) -> int:
    plan_path = Path(args.plan)
    vars_path = Path(args.vars) if args.vars else None

    prepare_started = time.perf_counter()
    resolved_plan = load_and_resolve_plan(plan_path, vars_path)
    t_prepare_ms = (time.perf_counter() - prepare_started) * 1000
    manifest = _load_manifest_if_enabled(config)
    manifest_validation = None
    if manifest is not None:
        command_names = _command_names_from_plan(resolved_plan)
        unknown, warnings = validate_command_names(command_names, manifest)
        if unknown:
            raise PlanError(f"命令清单校验失败，未知命令: {', '.join(unknown)}")
        manifest_validation = {
            "schema": manifest.get("schema", ""),
            "command_count": manifest.get("command_count", 0),
            "validated_command_count": len(command_names),
            "warnings": warnings,
        }
    plan_commands: list[dict[str, Any]] = []
    for phase in resolved_plan.get("phases", []):
        if isinstance(phase, dict) and isinstance(phase.get("commands"), list):
            plan_commands.extend(phase["commands"])
    if isinstance(resolved_plan.get("asserts"), list):
        plan_commands.extend(resolved_plan["asserts"])
    param_validation = _validate_payloads_with_manifest(config, plan_commands, manifest)

    if args.dry_run:
        expanded = dry_run_output(resolved_plan)
        print(expanded)
        payload = _build_report_payload(
            config,
            {
                "task_id": str(resolved_plan.get("task_id")),
                "success": True,
                "dry_run": True,
                "resolved_plan": resolved_plan,
                "command_manifest_validation": manifest_validation,
                "command_param_validation": param_validation,
                "metrics": {"t_prepare_ms": t_prepare_ms},
            },
        )
        _write_report(config, args, payload)
        return 0

    client = _client_from_config(config)
    compatibility = _compatibility_preflight(config, args, client, manifest)
    total_started = time.perf_counter()
    result = execute_plan(
        client=client,
        resolved_plan=resolved_plan,
        continue_on_error=bool(args.continue_on_error),
        start_phase_index=0,
        niagara_guard_enabled=config.niagara_guard_enabled,
        niagara_guard_strict=config.niagara_guard_strict,
    )
    t_total_ms = (time.perf_counter() - total_started) * 1000

    phase_payloads: list[dict[str, Any]] = []
    for phase in result.phases:
        phase_payloads.append(
            {
                "name": phase.name,
                "success": phase.success,
                "request_id": phase.request_id,
                "stop_on_error": phase.stop_on_error,
                "failed_index": phase.failed_index,
                "failed_command": phase.failed_command,
                "failed_request_id": phase.failed_request_id,
                "failed_error": phase.failed_error,
                "metrics": {
                    "t_prepare_ms": phase.metrics.t_prepare_ms,
                    "t_http_ms": phase.metrics.t_http_ms,
                    "t_parse_ms": phase.metrics.t_parse_ms,
                    "t_verify_ms": phase.metrics.t_verify_ms,
                    "t_total_ms": phase.metrics.t_total_ms,
                },
                "response": phase.response,
            }
        )

    payload = _build_report_payload(
        config,
        {
            "task_id": result.task_id,
            "success": result.success,
            "failed_phase_index": result.failed_phase_index,
            "phases": phase_payloads,
            "resolved_plan": result.resolved_plan,
            "command_manifest_validation": manifest_validation,
            "command_param_validation": param_validation,
            "compatibility": compatibility,
            "metrics": {"t_prepare_ms": t_prepare_ms, "t_total_ms": t_total_ms},
        },
    )
    _safe_print(
        {
            "success": result.success,
            "task_id": result.task_id,
            "failed_phase_index": result.failed_phase_index,
            "phase_count": len(result.phases),
            "t_prepare_ms": t_prepare_ms,
            "t_total_ms": t_total_ms,
        },
        args.json_output,
    )
    _write_report(config, args, payload)
    return 0 if result.success else 2


def handle_resume(args: argparse.Namespace, config: AppConfig) -> int:
    report = load_json_file(Path(args.report))
    resolved_plan = report.get("resolved_plan")
    if not isinstance(resolved_plan, dict):
        raise PlanError("报告中缺少 resolved_plan，无法 resume")

    failed_phase_index = report.get("failed_phase_index")
    if failed_phase_index is None:
        raise PlanError("报告显示没有失败 phase，无需 resume")
    if not isinstance(failed_phase_index, int):
        raise PlanError("报告中的 failed_phase_index 非法")

    start_phase_index = failed_phase_index if args.retry_failed_phase else failed_phase_index + 1
    manifest = _load_manifest_if_enabled(config)
    manifest_validation = None
    if manifest is not None:
        command_names = _command_names_from_plan(resolved_plan)
        unknown, warnings = validate_command_names(command_names, manifest)
        if unknown:
            raise PlanError(f"命令清单校验失败，未知命令: {', '.join(unknown)}")
        manifest_validation = {
            "schema": manifest.get("schema", ""),
            "command_count": manifest.get("command_count", 0),
            "validated_command_count": len(command_names),
            "warnings": warnings,
        }
    resume_commands: list[dict[str, Any]] = []
    for phase in resolved_plan.get("phases", []):
        if isinstance(phase, dict) and isinstance(phase.get("commands"), list):
            resume_commands.extend(phase["commands"])
    if isinstance(resolved_plan.get("asserts"), list):
        resume_commands.extend(resolved_plan["asserts"])
    param_validation = _validate_payloads_with_manifest(config, resume_commands, manifest)
    client = _client_from_config(config)
    compatibility = _compatibility_preflight(config, args, client, manifest)
    result = execute_plan(
        client=client,
        resolved_plan=resolved_plan,
        continue_on_error=bool(args.continue_on_error),
        start_phase_index=start_phase_index,
        niagara_guard_enabled=config.niagara_guard_enabled,
        niagara_guard_strict=config.niagara_guard_strict,
    )
    payload = _build_report_payload(
        config,
        {
            "task_id": f"{resolved_plan.get('task_id', 'task')}_resume",
            "success": result.success,
            "resume_from_phase_index": start_phase_index,
            "failed_phase_index": result.failed_phase_index,
            "command_manifest_validation": manifest_validation,
            "command_param_validation": param_validation,
            "compatibility": compatibility,
            "phases": [
                {
                    "name": phase.name,
                    "success": phase.success,
                    "request_id": phase.request_id,
                    "failed_index": phase.failed_index,
                    "failed_command": phase.failed_command,
                    "failed_request_id": phase.failed_request_id,
                    "failed_error": phase.failed_error,
                    "metrics": {
                        "t_prepare_ms": phase.metrics.t_prepare_ms,
                        "t_http_ms": phase.metrics.t_http_ms,
                        "t_parse_ms": phase.metrics.t_parse_ms,
                        "t_verify_ms": phase.metrics.t_verify_ms,
                        "t_total_ms": phase.metrics.t_total_ms,
                    },
                    "response": phase.response,
                }
                for phase in result.phases
            ],
            "resolved_plan": result.resolved_plan,
        },
    )
    _safe_print(
        {
            "success": result.success,
            "resume_from_phase_index": start_phase_index,
            "failed_phase_index": result.failed_phase_index,
            "phase_count": len(result.phases),
        },
        args.json_output,
    )
    _write_report(config, args, payload)
    return 0 if result.success else 2


def handle_namegen(args: argparse.Namespace, config: AppConfig) -> int:
    generated_name = build_short_asset_name(
        kind=args.kind,
        base=args.base,
        max_len=args.max_len,
        tag_mode=args.tag_mode,
    )
    payload = {
        "success": True,
        "kind": args.kind,
        "base": args.base,
        "max_len": args.max_len,
        "tag_mode": args.tag_mode,
        "generated_name": generated_name,
    }
    _safe_print(payload, args.json_output)
    _write_report(config, args, _build_report_payload(config, {"task_id": "namegen", **payload}))
    return 0


def handle_manifest(args: argparse.Namespace, config: AppConfig) -> int:
    output = Path(args.output) if getattr(args, "output", None) else None
    manifest = save_command_manifest(output) if output is not None else build_command_manifest()
    payload = {
        "success": True,
        "manifest_file": str(output or ""),
        "manifest": (
            {
                "schema": manifest.get("schema", ""),
                "command_count": manifest.get("command_count", 0),
                "documented_count": manifest.get("documented_count", 0),
                "implemented_count": manifest.get("implemented_count", 0),
                "smoke_tested_count": manifest.get("smoke_tested_count", 0),
                "warnings": manifest.get("warnings", []),
            }
            if args.summary
            else manifest
        ),
    }
    _safe_print(payload, args.json_output)
    _write_report(config, args, _build_report_payload(config, {"task_id": "manifest", **payload}))
    return 0


def handle_compat(args: argparse.Namespace, config: AppConfig) -> int:
    client = _client_from_config(config)
    status = client.get("/api/status")
    manifest = _load_manifest_if_enabled(config)
    compatibility = build_compatibility_report(
        cli_version=__version__,
        status_payload=status.payload,
        command_manifest=manifest,
        expected_plugin_version_tag=config.expected_plugin_version_tag,
    )
    payload = {"success": bool(compatibility["success"]), "status": status.payload, "compatibility": compatibility}
    _safe_print(payload, args.json_output)
    _write_report(config, args, _build_report_payload(config, {"task_id": "compat", **payload}))
    return 0 if payload["success"] else 2


def handle_crash(args: argparse.Namespace, config: AppConfig) -> int:
    crash_dir = Path(args.path) if getattr(args, "path", None) else find_latest_crash(config.app_root)
    if args.action == "collect":
        result = collect_failure_artifacts(
            app_root=config.app_root,
            subcommand="manual_collect",
            exit_code=2,
            request_files=[],
        )
        _safe_print(result, args.json_output)
        return 0 if result.get("success") else 2
    if crash_dir is None:
        raise PlanError("未找到 crash capture 目录")
    if args.action == "inspect":
        result = inspect_crash_dir(crash_dir)
        _safe_print(result, args.json_output)
        return 0 if result.get("success") else 2
    if args.action == "pack":
        output = Path(args.output) if getattr(args, "output", None) else None
        zip_path = pack_crash_dir(crash_dir, output)
        payload = {"success": True, "crash_dir": str(crash_dir), "zip_file": str(zip_path)}
        _safe_print(payload, args.json_output)
        return 0
    if args.action == "signature":
        payload = build_crash_signature(crash_dir)
        _safe_print(payload, args.json_output)
        return 0 if payload.get("success") else 2
    if args.action == "replay":
        payload = replay_crash_dir(crash_dir, app_root=config.app_root, dry_run=not bool(args.execute))
        _safe_print(payload, args.json_output)
        return 0 if payload.get("success") else 2
    if args.action == "bisect":
        payload = generate_batch_bisect_files(crash_dir)
        _safe_print(payload, args.json_output)
        return 0 if payload.get("success") else 2
    raise PlanError(f"未知 crash action: {args.action}")


def handle_index(args: argparse.Namespace, config: AppConfig) -> int:
    payload = {
        "success": True,
        "index": read_index(
            config.app_root,
            limit=max(1, args.limit),
            failed_only=bool(args.failed_only),
            command=args.command,
            task_id=args.task_id,
            stats=bool(args.stats),
        ),
    }
    _safe_print(payload, args.json_output)
    return 0


def handle_release(args: argparse.Namespace, config: AppConfig) -> int:
    payload: dict[str, Any] = {"success": True, "action": args.action}
    if args.action in {"coverage", "all", "gate"}:
        generated_dir = config.app_root / "docs" / "generated"
        output_json = Path(args.output_json) if getattr(args, "output_json", None) else generated_dir / "command_coverage_matrix.json"
        output_md = Path(args.output_md) if getattr(args, "output_md", None) else generated_dir / "command_coverage_matrix.md"
        coverage = write_coverage_matrix(output_json, output_md)
        payload["coverage"] = {
            "success": True,
            "json_file": str(output_json),
            "markdown_file": str(output_md),
            "command_count": coverage.get("command_count", 0),
            "missing_doc_count": len(coverage.get("missing_doc", [])),
            "missing_implementation_count": len(coverage.get("missing_implementation", [])),
            "missing_smoke_count": len(coverage.get("missing_smoke", [])),
            "smoke_actionable_missing_count": coverage.get("smoke_coverage", {}).get("actionable_missing_count", 0),
            "smoke_p0_count": coverage.get("smoke_coverage", {}).get("p0_count", 0),
            "smoke_p1_count": coverage.get("smoke_coverage", {}).get("p1_count", 0),
            "generated_doc_catalog_count": coverage.get("raw_generated_doc_count", 0),
            "generated_catalog_file": coverage.get("generated_catalog_file", ""),
            "smoke_debt_file": coverage.get("smoke_debt_file", ""),
        }
    if args.action in {"examples", "all", "gate"}:
        examples = write_example_library(config.app_root / "examples" / "generated")
        payload["examples"] = examples
        if not examples.get("success", False):
            payload["success"] = False
    if args.action in {"pak-verify", "all", "gate"}:
        pak = verify_pak_layout()
        payload["pak_verify"] = pak
        if not pak.get("success", False):
            payload["success"] = False
    if args.action == "gate":
        gate = run_quality_gate(config.app_root, run_tests=bool(args.run_tests))
        payload["gate"] = gate
        if not gate.get("success", False):
            payload["success"] = False
    _safe_print(payload, args.json_output)
    _write_report(config, args, _build_report_payload(config, {"task_id": f"release_{args.action}", **payload}))
    return 0 if payload["success"] else 2


def handle_e2e(args: argparse.Namespace, config: AppConfig) -> int:
    if args.mode == "local":
        payload = run_local_e2e(config.app_root)
    else:
        client = _client_from_config(config)
        compatibility = _compatibility_preflight(config, args, client, _load_manifest_if_enabled(config))
        payload = run_ue_readonly_e2e(client)
        payload["compatibility"] = compatibility
    _safe_print(payload, args.json_output)
    _write_report(config, args, _build_report_payload(config, {"task_id": f"e2e_{args.mode}", **payload}))
    return 0 if payload.get("success") else 2


def _service_offline_guidance(config: AppConfig, error: HttpError) -> str:
    return (
        f"无法连接到 UeAgentInterface 服务端（{config.base_url}）。\n"
        "请先确认：\n"
        "1) UE 编辑器已打开；\n"
        "2) 菜单 Window -> UeAgentInterface -> Start UeAgentInterface Server 已启动；\n"
        "3) token 配置正确。\n"
        f"原始错误: {error}"
    )


def main(argv: list[str] | None = None) -> int:
    parser = _build_common_parser()
    _add_subcommands(parser)
    args = parser.parse_args(argv)
    config: AppConfig | None = None

    try:
        config = _resolve_config(args)
        log_path = setup_logging(config.logs_dir, config.clear_log_on_start, config.log_level)
        logging.info("日志路径: %s", log_path)
        _run_cleanup_if_enabled(config, stage="startup")

        exit_code = int(args.handler(args, config))
        _maybe_collect_failure(config, args, exit_code=exit_code)
        _run_cleanup_if_enabled(config, stage="post_command")
        return exit_code
    except HttpError as error:
        message = str(error)
        if config is not None and "网络错误" in str(error):
            message = _service_offline_guidance(config, error)
        print(message)
        logging.error(message)
        _maybe_collect_failure(config, args, exit_code=3, error=error)
        return 3
    except (ConfigError, PlanError, UaiCliError, ValueError, FileNotFoundError, json.JSONDecodeError) as error:
        print(f"执行失败: {error}")
        logging.error("执行失败: %s", error)
        _maybe_collect_failure(config, args, exit_code=2, error=error)
        return 2
    except Exception as error:
        print(f"未预期异常: {error}")
        logging.exception("未预期异常")
        _maybe_collect_failure(config, args, exit_code=1, error=error)
        return 1


if __name__ == "__main__":
    sys.exit(main())
