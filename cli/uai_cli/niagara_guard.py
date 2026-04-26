from __future__ import annotations

import copy
from dataclasses import dataclass
from typing import Any

from .errors import PlanError
from .utils import now_compact

_NIAGARA_PREFIX = "niagara_"

_NIAGARA_MUTATION_KEYWORDS = (
    "_add_",
    "_set_",
    "_remove_",
    "_move_",
    "_delete_",
    "_duplicate_",
    "_create_",
)

_NIAGARA_READONLY_COMMANDS = {
    "niagara_list_assets",
    "niagara_open_editor",
    "niagara_get_info",
    "niagara_system_get_property",
    "niagara_get_compile_log",
    "niagara_system_list_emitters",
    "niagara_emitter_get_property",
    "niagara_emitter_list_renderers",
    "niagara_emitter_get_renderer_property",
    "niagara_emitter_list_event_handlers",
    "niagara_emitter_get_event_handler_property",
    "niagara_emitter_parameter_list",
    "niagara_emitter_parameter_get",
    "niagara_emitter_list_stages",
    "niagara_emitter_list_stage_modules",
    "niagara_emitter_list_stage_nodes",
    "niagara_emitter_get_stage_node_property",
    "niagara_emitter_list_module_inputs",
    "niagara_user_parameter_list",
    "niagara_user_parameter_get",
}

_UNKNOWN_EMITTER_MARKERS = ("unknown emitter", "unknown em")

_REMOVE_EMITTER_COMMAND = "niagara_system_remove_emitter"
_ADD_EMITTER_COMMAND = "niagara_system_add_emitter"


@dataclass(slots=True)
class NiagaraGuardPreparation:
    commands: list[dict[str, Any]]
    has_niagara_commands: bool
    has_mutation_commands: bool
    touched_system_paths: list[str]
    injected_command_count: int


@dataclass(slots=True)
class NiagaraGuardVerification:
    success: bool
    failed_index: int | None = None
    failed_command: str | None = None
    failed_request_id: str | None = None
    failed_error: str | None = None


def _normalize_command_name(command: dict[str, Any]) -> str:
    return str(command.get("command", "")).strip().lower()


def _normalize_system_path(system_path: str) -> str:
    path = str(system_path or "").strip()
    if "." in path:
        path = path.split(".", 1)[0]
    return path


def _extract_system_path(command: dict[str, Any]) -> str:
    command_name = _normalize_command_name(command)
    params = command.get("params")
    if not isinstance(params, dict):
        return ""

    direct = params.get("system_asset_path")
    if isinstance(direct, str) and direct.strip():
        return _normalize_system_path(direct)

    asset_path = params.get("asset_path")
    if isinstance(asset_path, str) and asset_path.strip():
        normalized = _normalize_system_path(asset_path)
        if normalized.endswith(".uasset"):
            normalized = normalized.removesuffix(".uasset")
        if command_name == "niagara_create_emitter":
            return ""
        if command_name == "niagara_create_system":
            return normalized
        if command_name.startswith("niagara_system_"):
            return normalized
        if command_name in {"niagara_compile_system", "niagara_get_compile_log"}:
            return normalized
        if command_name.startswith("niagara_user_parameter_"):
            return normalized
        if command_name.startswith("niagara_emitter_"):
            return normalized if "." in asset_path else ""
        if command_name in {"niagara_set_property", "niagara_get_info", "niagara_open_editor", "niagara_duplicate_asset", "niagara_delete_asset"}:
            asset_name = normalized.rsplit("/", 1)[-1]
            if "." in asset_path or asset_name.startswith("NS_"):
                return normalized
            return ""
    return ""


def _is_niagara_command(command_name: str) -> bool:
    return command_name.startswith(_NIAGARA_PREFIX)


def _is_niagara_mutation_command(command_name: str) -> bool:
    if command_name in _NIAGARA_READONLY_COMMANDS:
        return False
    if command_name == "niagara_compile_system":
        return True
    return any(keyword in command_name for keyword in _NIAGARA_MUTATION_KEYWORDS)


def _detect_remove_add_mix(commands: list[dict[str, Any]]) -> list[str]:
    by_system: dict[str, dict[str, bool]] = {}
    for command in commands:
        command_name = _normalize_command_name(command)
        if command_name not in {_REMOVE_EMITTER_COMMAND, _ADD_EMITTER_COMMAND}:
            continue
        system_path = _extract_system_path(command)
        if not system_path:
            continue
        flags = by_system.setdefault(system_path, {"add": False, "remove": False})
        if command_name == _ADD_EMITTER_COMMAND:
            flags["add"] = True
        if command_name == _REMOVE_EMITTER_COMMAND:
            flags["remove"] = True

    mixed: list[str] = []
    for system_path, flags in by_system.items():
        if flags["add"] and flags["remove"]:
            mixed.append(system_path)
    return mixed


def _extract_deleted_system_paths(commands: list[dict[str, Any]]) -> set[str]:
    deleted: set[str] = set()
    for command in commands:
        if _normalize_command_name(command) != "niagara_delete_asset":
            continue
        system_path = _extract_system_path(command)
        if system_path:
            deleted.add(system_path)
    return deleted


def _build_preflight_command(phase_name: str) -> dict[str, Any]:
    return {
        "request_id": f"{phase_name}_guard_preflight_{now_compact()}",
        "command": "editor_prepare_exit",
        "params": {
            "request_exit": False,
            "close_all_asset_editors": True,
            "save_all_dirty": False,
            "discard_all_dirty": False,
            "save_current_level": False,
            "discard_current_level": False,
            "only_save_dirty": True,
        },
    }


def _build_postcheck_commands(phase_name: str, system_path: str, index: int) -> list[dict[str, Any]]:
    safe_tag = f"{index:02d}"
    return [
        {
            "request_id": f"{phase_name}_guard_compile_{safe_tag}_{now_compact()}",
            "command": "niagara_compile_system",
            "params": {
                "asset_path": system_path,
                "force_compile": True,
                "wait_for_complete": True,
                "save_after_compile": False,
            },
        },
        {
            "request_id": f"{phase_name}_guard_log_{safe_tag}_{now_compact()}",
            "command": "niagara_get_compile_log",
            "params": {
                "asset_path": system_path,
                "compile_before_read": False,
                "wait_for_complete": True,
                "severity_filter": "warning_or_error",
                "include_events": True,
                "max_events_per_script": 200,
            },
        },
        {
            "request_id": f"{phase_name}_guard_emitters_{safe_tag}_{now_compact()}",
            "command": "niagara_system_list_emitters",
            "params": {
                "asset_path": system_path,
                "include_disabled": True,
            },
        },
    ]


def prepare_niagara_guarded_commands(
    commands: list[dict[str, Any]],
    phase_name: str,
    guard_enabled: bool,
    strict_guard: bool,
) -> NiagaraGuardPreparation:
    copied_commands = copy.deepcopy(commands)
    niagara_commands = [cmd for cmd in copied_commands if _is_niagara_command(_normalize_command_name(cmd))]
    has_niagara = bool(niagara_commands)
    has_mutation = any(_is_niagara_mutation_command(_normalize_command_name(cmd)) for cmd in niagara_commands)
    if not guard_enabled or not has_mutation:
        return NiagaraGuardPreparation(
            commands=copied_commands,
            has_niagara_commands=has_niagara,
            has_mutation_commands=has_mutation,
            touched_system_paths=[],
            injected_command_count=0,
        )

    if strict_guard:
        mixed = _detect_remove_add_mix(niagara_commands)
        if mixed:
            mixed_joined = ",".join(mixed)
            raise PlanError(
                f"niagara_guard_blocked_remove_add_same_batch:{mixed_joined}. "
                "请拆分为两个 phase（先 remove 并编译保存，再 add 并编译保存）。"
            )

    deleted_system_paths = _extract_deleted_system_paths(niagara_commands)
    touched_system_paths: list[str] = []
    touched_set: set[str] = set()
    for command in niagara_commands:
        system_path = _extract_system_path(command)
        if not system_path or system_path in deleted_system_paths or system_path in touched_set:
            continue
        touched_set.add(system_path)
        touched_system_paths.append(system_path)

    output_commands: list[dict[str, Any]] = []
    output_commands.append(_build_preflight_command(phase_name))
    output_commands.extend(copied_commands)
    for index, system_path in enumerate(touched_system_paths):
        output_commands.extend(_build_postcheck_commands(phase_name, system_path, index))

    return NiagaraGuardPreparation(
        commands=output_commands,
        has_niagara_commands=True,
        has_mutation_commands=True,
        touched_system_paths=touched_system_paths,
        injected_command_count=len(output_commands) - len(copied_commands),
    )


def verify_niagara_guard_response(
    response_payload: dict[str, Any],
    guard_preparation: NiagaraGuardPreparation,
) -> NiagaraGuardVerification:
    if not guard_preparation.has_mutation_commands:
        return NiagaraGuardVerification(success=True)

    data = response_payload.get("data")
    if not isinstance(data, dict):
        return NiagaraGuardVerification(success=True)
    results = data.get("results")
    if not isinstance(results, list):
        return NiagaraGuardVerification(success=True)

    for result in results:
        if not isinstance(result, dict):
            continue
        command_name = str(result.get("command", "")).strip().lower()
        command_index = result.get("index")
        failed_index = command_index if isinstance(command_index, int) else None
        request_id = str(result.get("request_id", "")).strip() or None
        data_obj = result.get("data")
        if not isinstance(data_obj, dict):
            continue

        if command_name == "niagara_get_compile_log":
            has_error = bool(data_obj.get("has_error", False))
            error_script_count = int(data_obj.get("error_script_count", 0) or 0)
            if has_error or error_script_count > 0:
                return NiagaraGuardVerification(
                    success=False,
                    failed_index=failed_index,
                    failed_command=result.get("command"),
                    failed_request_id=request_id,
                    failed_error="niagara_compile_log_has_error",
                )

        if command_name == "niagara_system_list_emitters":
            emitters = data_obj.get("emitters")
            if not isinstance(emitters, list):
                continue
            for emitter in emitters:
                if not isinstance(emitter, dict):
                    continue
                emitter_name = str(emitter.get("name", "")).strip()
                emitter_id = str(emitter.get("id", "")).strip()
                lower_name = emitter_name.lower()
                if not emitter_id:
                    return NiagaraGuardVerification(
                        success=False,
                        failed_index=failed_index,
                        failed_command=result.get("command"),
                        failed_request_id=request_id,
                        failed_error="niagara_emitter_missing_id",
                    )
                if any(marker in lower_name for marker in _UNKNOWN_EMITTER_MARKERS):
                    return NiagaraGuardVerification(
                        success=False,
                        failed_index=failed_index,
                        failed_command=result.get("command"),
                        failed_request_id=request_id,
                        failed_error=f"niagara_unknown_emitter_detected:{emitter_name}",
                    )

    return NiagaraGuardVerification(success=True)
