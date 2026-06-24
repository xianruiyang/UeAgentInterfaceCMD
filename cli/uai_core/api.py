from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .command_manifest import (
    build_command_manifest,
    command_names_from_batch,
    format_command_lifecycle_error,
    validate_command_lifecycle,
    validate_command_names,
)
from .command_schema import validate_command_payloads
from .compatibility import build_compatibility_report
from .config import AppConfig, load_app_config
from .errors import ConfigError
from .http_client import UaiHttpClient
from .runner import execute_batch
from .utils import now_compact
from .version import __version__


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


@dataclass(slots=True)
class CommandResult:
    success: bool
    request: dict[str, Any]
    response: dict[str, Any]
    compatibility: dict[str, Any] | None = None
    command_manifest_validation: dict[str, Any] | None = None
    command_param_validation: dict[str, Any] | None = None
    elapsed_ms: float = 0

    def raise_for_failure(self) -> None:
        if self.success:
            return
        data = self.response.get("data") if isinstance(self.response, dict) else None
        if isinstance(data, dict):
            failed_error = data.get("failed_error")
            failed_command = data.get("failed_command")
            if failed_error or failed_command:
                raise RuntimeError(f"UAI command failed: {failed_command or '<unknown>'}: {failed_error or ''}")
        error = self.response.get("error") if isinstance(self.response, dict) else ""
        raise RuntimeError(f"UAI command failed: {error or self.request.get('command')}")


@dataclass(slots=True)
class BatchResult:
    success: bool
    phase_name: str
    request_id: str
    response: dict[str, Any]
    failed_index: int | None = None
    failed_command: str | None = None
    failed_request_id: str | None = None
    failed_error: str | None = None
    compatibility: dict[str, Any] | None = None
    command_manifest_validation: dict[str, Any] | None = None
    command_param_validation: dict[str, Any] | None = None
    metrics: dict[str, float] | None = None

    @property
    def results(self) -> list[dict[str, Any]]:
        data = self.response.get("data") if isinstance(self.response, dict) else None
        if not isinstance(data, dict):
            return []
        results = data.get("results")
        return results if isinstance(results, list) else []

    def result_by_request_id(self, request_id: str) -> dict[str, Any] | None:
        for result in self.results:
            if isinstance(result, dict) and result.get("request_id") == request_id:
                return result
        return None

    def raise_for_failure(self) -> None:
        if self.success:
            return
        raise RuntimeError(
            "UAI batch failed: "
            f"index={self.failed_index} command={self.failed_command or '<unknown>'} "
            f"request_id={self.failed_request_id or ''} error={self.failed_error or ''}"
        )


class UaiCore:
    """Library-facing UAI client.

    This class is intentionally thin: it keeps the CLI's manifest, compat,
    Niagara guard and HTTP behavior in one reusable place while exposing a
    Python-first API for future generated command wrappers.
    """

    def __init__(self, config: AppConfig, *, manifest: dict[str, Any] | None = None) -> None:
        self.config = config
        self.client = UaiHttpClient(config.base_url, config.token, config.timeout_seconds)
        self._manifest = manifest

    @classmethod
    def from_config(
        cls,
        *,
        config_path: str | None = None,
        base_url: str | None = None,
        token: str | None = None,
        timeout_seconds: int | None = None,
        allow_nonloopback: bool = False,
        niagara_guard_enabled: bool | None = None,
        niagara_guard_strict: bool | None = None,
        require_token: bool = True,
    ) -> UaiCore:
        config = load_app_config(
            config_path=config_path,
            base_url=base_url,
            token=token,
            timeout_seconds=timeout_seconds,
            allow_nonloopback=allow_nonloopback,
            niagara_guard_enabled=niagara_guard_enabled,
            niagara_guard_strict=niagara_guard_strict,
            require_token=require_token,
        )
        return cls(config)

    @property
    def manifest(self) -> dict[str, Any] | None:
        if not self.config.command_manifest_enabled:
            return None
        if self._manifest is None:
            self._manifest = build_command_manifest()
        return self._manifest

    def compatibility_report(self) -> dict[str, Any]:
        status = self.client.get("/api/status")
        return build_compatibility_report(
            cli_version=__version__,
            status_payload=status.payload,
            expected_plugin_version_tag=self.config.expected_plugin_version_tag,
            command_manifest=self.manifest,
        )

    def ensure_compatible(self) -> dict[str, Any] | None:
        if not self.config.compatibility_check_enabled:
            return None
        report = self.compatibility_report()
        if not report.get("success", False):
            issues = ", ".join(str(issue) for issue in report.get("issues", []))
            raise ConfigError(f"CLI/插件兼容检查失败: {issues}")
        return report

    def validate_command_names(
        self,
        command_names: list[str],
        *,
        allow_deprecated: bool = False,
        deprecated_use_case: str | None = None,
    ) -> dict[str, Any] | None:
        manifest = self.manifest
        if manifest is None:
            return None
        unknown, warnings = validate_command_names(command_names, manifest)
        if unknown:
            raise ConfigError(f"未知 UAI 指令: {', '.join(unknown)}")
        lifecycle_validation = validate_command_lifecycle(
            command_names,
            manifest,
            allow_deprecated=allow_deprecated,
            deprecated_use_case=deprecated_use_case,
        )
        if not lifecycle_validation.get("success", True):
            raise ConfigError(format_command_lifecycle_error(lifecycle_validation))
        lifecycle_warnings = lifecycle_validation.get("warnings", [])
        if isinstance(lifecycle_warnings, list):
            warnings.extend(str(warning) for warning in lifecycle_warnings)
        return {
            "schema": manifest.get("schema", ""),
            "command_count": manifest.get("command_count", 0),
            "validated_command_count": len(command_names),
            "warnings": warnings,
            "command_lifecycle_validation": lifecycle_validation,
        }

    def validate_payloads(self, commands: list[dict[str, Any]]) -> dict[str, Any] | None:
        manifest = self.manifest
        if manifest is None or self.config.param_validation_mode == "off":
            return None
        result = validate_command_payloads(
            commands,
            manifest,
            strict=self.config.param_validation_mode == "strict",
        )
        if not result.get("success", True):
            issues = ", ".join(str(issue) for issue in result.get("issues", []))
            warnings = ", ".join(str(warning) for warning in result.get("warnings", []))
            detail = issues or warnings
            raise ConfigError(f"UAI 参数校验失败: {detail}")
        return result

    def doctor(self) -> dict[str, Any]:
        ping = self.client.get("/api/ping")
        status = self.client.get("/api/status")
        compatibility = self.compatibility_report()
        return {
            "success": bool(ping.payload.get("ok")) and bool(status.payload.get("ok")) and compatibility["success"],
            "ping": ping.payload,
            "status": status.payload,
            "compatibility": compatibility,
            "metrics": {
                "t_ping_ms": ping.elapsed_ms,
                "t_status_ms": status.elapsed_ms,
                "t_total_ms": ping.elapsed_ms + status.elapsed_ms,
            },
        }

    def exec(
        self,
        command: str,
        params: dict[str, Any] | None = None,
        *,
        request_id: str | None = None,
        preflight: bool = True,
        allow_deprecated: bool = False,
        deprecated_use_case: str | None = None,
    ) -> CommandResult:
        request_payload = {
            "request_id": request_id or f"exec_{now_compact()}",
            "command": command,
            "params": params or {},
        }
        manifest_validation = (
            self.validate_command_names(
                [command],
                allow_deprecated=allow_deprecated,
                deprecated_use_case=deprecated_use_case,
            )
            if preflight
            else None
        )
        param_validation = self.validate_payloads([request_payload]) if preflight else None
        compatibility = self.ensure_compatible() if preflight else None
        result = self.client.post_json("/api/exec", request_payload)
        return CommandResult(
            success=_is_exec_success(result.payload),
            request=request_payload,
            response=result.payload,
            compatibility=compatibility,
            command_manifest_validation=manifest_validation,
            command_param_validation=param_validation,
            elapsed_ms=result.elapsed_ms,
        )

    def batch(
        self,
        commands: list[dict[str, Any]],
        *,
        stop_on_error: bool = True,
        phase_name: str = "batch",
        preflight: bool = True,
        allow_deprecated: bool = False,
        deprecated_use_case: str | None = None,
    ) -> BatchResult:
        manifest_validation = None
        param_validation = None
        compatibility = None
        if preflight:
            manifest_validation = self.validate_command_names(
                command_names_from_batch(commands),
                allow_deprecated=allow_deprecated,
                deprecated_use_case=deprecated_use_case,
            )
            param_validation = self.validate_payloads(commands)
            compatibility = self.ensure_compatible()

        phase_report = execute_batch(
            client=self.client,
            phase_name=phase_name,
            commands=commands,
            stop_on_error=stop_on_error,
            niagara_guard_enabled=self.config.niagara_guard_enabled,
            niagara_guard_strict=self.config.niagara_guard_strict,
        )
        return BatchResult(
            success=phase_report.success,
            phase_name=phase_report.name,
            request_id=phase_report.request_id,
            response=phase_report.response,
            failed_index=phase_report.failed_index,
            failed_command=phase_report.failed_command,
            failed_request_id=phase_report.failed_request_id,
            failed_error=phase_report.failed_error,
            compatibility=compatibility,
            command_manifest_validation=manifest_validation,
            command_param_validation=param_validation,
            metrics={
                "t_prepare_ms": phase_report.metrics.t_prepare_ms,
                "t_http_ms": phase_report.metrics.t_http_ms,
                "t_parse_ms": phase_report.metrics.t_parse_ms,
                "t_verify_ms": phase_report.metrics.t_verify_ms,
                "t_total_ms": phase_report.metrics.t_total_ms,
            },
        )

    def save_request(self, path: Path, payload: dict[str, Any]) -> None:
        from .utils import save_json_file

        save_json_file(path, payload)
