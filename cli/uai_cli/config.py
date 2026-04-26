from __future__ import annotations

import configparser
from dataclasses import dataclass
from pathlib import Path

from .errors import ConfigError
from .utils import detect_app_root, env_or_default, is_loopback_url, load_json_file


@dataclass(slots=True)
class AppConfig:
    base_url: str
    token: str
    timeout_seconds: int
    clear_log_on_start: bool
    log_level: str
    allow_nonloopback: bool
    niagara_guard_enabled: bool
    niagara_guard_strict: bool
    auto_cleanup_enabled: bool
    cleanup_tmp_max: int
    cleanup_tmp_keep: int
    cleanup_reports_max: int
    cleanup_reports_keep: int
    app_root: Path
    reports_dir: Path
    logs_dir: Path


def _try_load_token_from_ue_ini(app_root: Path) -> str:
    candidate_paths: list[Path] = [
        app_root.parent / "Saved/Config/WindowsEditor/UeAgentInterface.ini",
        app_root.parent.parent / "Saved/Config/WindowsEditor/UeAgentInterface.ini",
        Path.cwd() / "Saved/Config/WindowsEditor/UeAgentInterface.ini",
    ]

    seen: set[Path] = set()
    for candidate in candidate_paths:
        resolved = candidate.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        if not candidate.exists():
            continue

        parser = configparser.ConfigParser()
        try:
            parser.read(candidate, encoding="utf-8")
        except (OSError, UnicodeError):
            continue

        if parser.has_option("/Script/UeAgentInterface.UeAgentInterfaceSettings", "AuthToken"):
            token = parser.get("/Script/UeAgentInterface.UeAgentInterfaceSettings", "AuthToken", fallback="").strip()
            if token:
                return token

    return ""


def _merge(base: dict, override: dict) -> dict:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def _validate_cleanup_values(
    cleanup_tmp_max: int,
    cleanup_tmp_keep: int,
    cleanup_reports_max: int,
    cleanup_reports_keep: int,
) -> None:
    if cleanup_tmp_max <= 0 or cleanup_tmp_keep <= 0:
        raise ConfigError("cleanup_tmp_max 和 cleanup_tmp_keep 必须 > 0")
    if cleanup_reports_max <= 0 or cleanup_reports_keep <= 0:
        raise ConfigError("cleanup_reports_max 和 cleanup_reports_keep 必须 > 0")
    if cleanup_tmp_keep > cleanup_tmp_max:
        raise ConfigError("cleanup_tmp_keep 不能大于 cleanup_tmp_max")
    if cleanup_reports_keep > cleanup_reports_max:
        raise ConfigError("cleanup_reports_keep 不能大于 cleanup_reports_max")


def load_app_config(
    config_path: str | None,
    base_url: str | None,
    token: str | None,
    timeout_seconds: int | None,
    allow_nonloopback: bool,
    niagara_guard_enabled: bool | None = None,
    niagara_guard_strict: bool | None = None,
    require_token: bool = True,
) -> AppConfig:
    app_root = detect_app_root()
    default_cfg_path = app_root / "uai-cli.default.json"
    if not default_cfg_path.exists():
        raise ConfigError(f"默认配置不存在: {default_cfg_path}")

    config_data = load_json_file(default_cfg_path)
    if config_path:
        external_cfg = load_json_file(Path(config_path))
        config_data = _merge(config_data, external_cfg)

    final_base_url = (base_url or config_data.get("base_url") or "").strip().rstrip("/")
    final_token = (token or env_or_default("UAI_TOKEN", config_data.get("token", ""))).strip()
    if not final_token:
        final_token = _try_load_token_from_ue_ini(app_root)
    final_timeout = int(timeout_seconds or config_data.get("timeout_seconds", 60))
    final_clear_log = bool(config_data.get("clear_log_on_start", True))
    final_log_level = str(config_data.get("log_level", "info")).lower()

    final_niagara_guard_enabled = (
        bool(niagara_guard_enabled)
        if niagara_guard_enabled is not None
        else bool(config_data.get("niagara_guard_enabled", True))
    )
    final_niagara_guard_strict = (
        bool(niagara_guard_strict)
        if niagara_guard_strict is not None
        else bool(config_data.get("niagara_guard_strict", True))
    )

    final_auto_cleanup_enabled = bool(config_data.get("auto_cleanup_enabled", True))
    final_cleanup_tmp_max = int(config_data.get("cleanup_tmp_max", 120))
    final_cleanup_tmp_keep = int(config_data.get("cleanup_tmp_keep", 40))
    final_cleanup_reports_max = int(config_data.get("cleanup_reports_max", 200))
    final_cleanup_reports_keep = int(config_data.get("cleanup_reports_keep", 120))
    _validate_cleanup_values(
        cleanup_tmp_max=final_cleanup_tmp_max,
        cleanup_tmp_keep=final_cleanup_tmp_keep,
        cleanup_reports_max=final_cleanup_reports_max,
        cleanup_reports_keep=final_cleanup_reports_keep,
    )

    if not final_base_url:
        raise ConfigError("base_url 为空，请在配置文件或参数中提供")
    if not allow_nonloopback and not is_loopback_url(final_base_url):
        raise ConfigError(f"检测到非本机地址: {final_base_url}，如确需使用请加 --allow-nonloopback")
    if require_token and not final_token:
        raise ConfigError("token 为空，请在配置文件、参数或 UAI_TOKEN 中提供")
    if final_timeout <= 0:
        raise ConfigError("timeout_seconds 必须 > 0")

    reports_dir = app_root / "reports"
    logs_dir = app_root / "logs"

    return AppConfig(
        base_url=final_base_url,
        token=final_token,
        timeout_seconds=final_timeout,
        clear_log_on_start=final_clear_log,
        log_level=final_log_level,
        allow_nonloopback=allow_nonloopback,
        niagara_guard_enabled=final_niagara_guard_enabled,
        niagara_guard_strict=final_niagara_guard_strict,
        auto_cleanup_enabled=final_auto_cleanup_enabled,
        cleanup_tmp_max=final_cleanup_tmp_max,
        cleanup_tmp_keep=final_cleanup_tmp_keep,
        cleanup_reports_max=final_cleanup_reports_max,
        cleanup_reports_keep=final_cleanup_reports_keep,
        app_root=app_root,
        reports_dir=reports_dir,
        logs_dir=logs_dir,
    )
