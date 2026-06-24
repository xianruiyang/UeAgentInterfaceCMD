from __future__ import annotations

from dataclasses import dataclass, field
from difflib import get_close_matches
from typing import Any


PATH_LIKE_PARAMS = {
    "asset_path",
    "blueprint_asset",
    "blackboard_asset",
    "folder_path",
    "json_file",
    "output_file",
    "source_file",
    "source_filename",
    "destination_path",
    "destination_name",
}

STRING_LIKE_PARAMS = {
    "buffer",
    "capture_mode",
    "depth_mode",
    "format",
    "method",
    "target",
}

BOOL_LIKE_PARAMS = {
    "save_after_create",
    "save_after_apply",
    "dry_run",
    "validate_only",
    "strict",
    "allow_destructive",
    "clean_output_dir",
    "include_validation",
    "include_raw_properties",
    "invert",
    "open_editor",
    "open_editor_if_needed",
    "bring_to_front",
    "require_non_black",
}

NUMBER_LIKE_PARAMS = {
    "max_results",
    "max_size",
    "width",
    "height",
    "depth",
    "slices",
    "view_x",
    "view_y",
    "zoom",
    "quality",
    "warmup_frames",
    "render_warmup_frames",
    "depth_near_cm",
    "depth_far_cm",
    "depth_auto_pct_low",
    "depth_auto_pct_high",
}

REQUIRED_PARAM_GROUPS_BY_COMMAND: dict[str, tuple[tuple[str, ...], ...]] = {
    "asset_duplicate": (("source_asset_path",), ("destination_asset_path",)),
    "asset_move": (("source_asset_path", "asset_path"), ("destination_asset_path", "destination_folder")),
    "asset_rename": (("asset_path",), ("new_name", "destination_name")),
    "sequence_create_level_sequence": (("asset_path",),),
    "sequence_open_level_sequence": (("asset_path",),),
    "sequence_apply_folder": (("asset_path",),),
    "sequence_export_folder": (("asset_path",),),
    "sequence_get_level_sequence_info": (("asset_path",),),
    "sequence_screenshot": (("asset_path",),),
    "control_rig_apply_folder": (("folder_path",),),
    "control_rig_bake_to_animation": (("sequence_path",), ("binding_id", "binding_guid"), ("output_anim_sequence",)),
    "control_rig_bake_to_control_rig": (("sequence_path",), ("binding_id", "binding_guid"), ("control_rig_class",)),
    "control_rig_compile": (("asset_path",),),
    "control_rig_create": (("asset_path",),),
    "control_rig_export_folder": (("asset_path",),),
    "control_rig_get_compile_log": (("asset_path",),),
    "control_rig_get_info": (("asset_path",),),
    "control_rig_runtime_probe": (("asset_path",),),
    "control_rig_screenshot": (("asset_path",),),
    "control_rig_validate_folder": (("folder_path",),),
    "probe_ik_goal_candidates": (("sequence_path",), ("control_name",), ("candidates",)),
    "probe_ik_goal_review_frames": (("frames", "frame_indices", "frame_indexes", "numbers", "selections", "frame_index", "frame_number", "number", "index", "selection"),),
    "probe_ik_goal_apply_candidate": (("selection", "frame_index", "frame_number", "number", "candidate_index", "index"),),
}

PARAM_ALIASES_BY_COMMAND: dict[str, dict[str, str]] = {
    "asset_duplicate": {
        "asset_path": "source_asset_path",
        "source_asset": "source_asset_path",
        "source_path": "source_asset_path",
        "target_asset_path": "destination_asset_path",
        "destination_path": "destination_asset_path",
        "target_path": "destination_asset_path",
    },
    "sequence_apply_folder": {
        "sequence_path": "asset_path",
        "level_sequence": "asset_path",
    },
    "sequence_create_level_sequence": {
        "sequence_path": "asset_path",
        "level_sequence": "asset_path",
    },
    "sequence_export_folder": {
        "sequence_path": "asset_path",
        "level_sequence": "asset_path",
    },
    "sequence_get_level_sequence_info": {
        "sequence_path": "asset_path",
        "level_sequence": "asset_path",
    },
    "sequence_open_level_sequence": {
        "sequence_path": "asset_path",
        "level_sequence": "asset_path",
    },
    "sequence_screenshot": {
        "sequence_path": "asset_path",
        "level_sequence": "asset_path",
    },
    "control_rig_get_info": {
        "control_rig": "asset_path",
        "control_rig_path": "asset_path",
        "rig_path": "asset_path",
    },
    "control_rig_export_folder": {
        "control_rig": "asset_path",
        "control_rig_path": "asset_path",
        "rig_path": "asset_path",
    },
    "control_rig_compile": {
        "control_rig": "asset_path",
        "control_rig_path": "asset_path",
        "rig_path": "asset_path",
    },
    "control_rig_runtime_probe": {
        "control_rig": "asset_path",
        "control_rig_path": "asset_path",
        "rig_path": "asset_path",
    },
    "control_rig_apply_folder": {
        "asset_path": "folder_path",
        "json_file": "folder_path",
    },
    "control_rig_validate_folder": {
        "asset_path": "folder_path",
        "json_file": "folder_path",
    },
    "probe_ik_goal_candidates": {
        "asset_path": "sequence_path",
        "goal_name": "control_name",
        "transforms": "candidates",
        "candidate_transforms": "candidates",
    },
}


@dataclass(slots=True)
class CommandValidationResult:
    command: str
    index: int
    issues: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_json(self) -> dict[str, Any]:
        return {
            "command": self.command,
            "index": self.index,
            "issues": self.issues,
            "warnings": self.warnings,
        }


def infer_param_type(param_name: str) -> str:
    name = param_name.strip()
    if name in BOOL_LIKE_PARAMS or name.startswith("include_") or name.startswith("allow_"):
        return "bool"
    if name in NUMBER_LIKE_PARAMS or name.endswith("_count") or name.endswith("_index"):
        return "number"
    if name in STRING_LIKE_PARAMS:
        return "string"
    if name.endswith("[]") or name.endswith("s[]"):
        return "array"
    if name.endswith("_path") or name.endswith("_file") or name in PATH_LIKE_PARAMS:
        return "string"
    return "any"


def build_param_schema(params: list[str]) -> dict[str, Any]:
    properties: dict[str, Any] = {}
    for raw in params:
        name = raw.strip()
        if not name or "/" in name or " " in name:
            continue
        if name.endswith("[]"):
            clean_name = name[:-2]
            properties[clean_name] = {"type": "array", "source": name}
        else:
            properties[name] = {"type": infer_param_type(name), "source": name}
    return {
        "schema": "ue_agent_interface.command_params.v1",
        "properties": properties,
        "required": [],
        "required_policy": "not_inferred_from_docs",
    }


def _param_has_value(params: dict[str, Any], names: tuple[str, ...]) -> bool:
    for name in names:
        if name not in params:
            continue
        value = params[name]
        if value is None:
            continue
        if isinstance(value, str) and not value.strip():
            continue
        return True
    return False


def _validate_curated_required_params(command_name: str, params: dict[str, Any], result: CommandValidationResult) -> None:
    alias_map = PARAM_ALIASES_BY_COMMAND.get(command_name, {})
    for alias, canonical in alias_map.items():
        if alias in params and canonical not in params:
            result.issues.append(f"param_alias:{alias}->{canonical}")

    for group in REQUIRED_PARAM_GROUPS_BY_COMMAND.get(command_name, ()):
        if _param_has_value(params, group):
            continue
        if len(group) == 1:
            required_name = group[0]
            aliases = sorted(alias for alias, canonical in alias_map.items() if canonical == required_name and alias in params)
            if aliases:
                result.issues.append(f"missing_required_param:{required_name}:saw_alias:{'|'.join(aliases)}")
            else:
                result.issues.append(f"missing_required_param:{required_name}")
        else:
            result.issues.append(f"missing_required_one_of:{'|'.join(group)}")


def _is_true_bool(value: Any) -> bool:
    return isinstance(value, bool) and value


def _validate_editor_open_guard(command_name: str, params: dict[str, Any], result: CommandValidationResult) -> None:
    if command_name == "sequence_create_level_sequence":
        if _is_true_bool(params.get("open_editor")) and not _is_true_bool(params.get("allow_editor_open")):
            result.issues.append("open_editor_requires_allow_editor_open")
    elif command_name == "sequence_open_level_sequence":
        if not _is_true_bool(params.get("allow_editor_open")):
            result.issues.append("sequence_open_level_sequence_requires_allow_editor_open")


def validate_command_payloads(
    commands: list[dict[str, Any]],
    manifest: dict[str, Any],
    *,
    strict: bool = False,
) -> dict[str, Any]:
    known = manifest.get("commands")
    if not isinstance(known, dict):
        return {"success": True, "issues": [], "warnings": ["command_manifest_unavailable"], "results": []}

    results: list[CommandValidationResult] = []
    for index, command_payload in enumerate(commands):
        command_name = command_payload.get("command")
        result = CommandValidationResult(command=str(command_name or ""), index=index)
        if not isinstance(command_name, str) or not command_name:
            result.issues.append("command_missing_or_not_string")
            results.append(result)
            continue
        command_info = known.get(command_name)
        if not isinstance(command_info, dict):
            result.issues.append("unknown_command")
            results.append(result)
            continue
        params = command_payload.get("params", {})
        if params is None:
            params = {}
        if not isinstance(params, dict):
            result.issues.append("params_must_be_object")
            results.append(result)
            continue
        schema = command_info.get("param_schema")
        if not isinstance(schema, dict):
            result.warnings.append("param_schema_unavailable")
            results.append(result)
            continue
        properties = schema.get("properties")
        if not isinstance(properties, dict):
            result.warnings.append("param_schema_properties_unavailable")
            results.append(result)
            continue
        _validate_curated_required_params(command_name, params, result)
        _validate_editor_open_guard(command_name, params, result)
        known_param_names = [str(name) for name in properties.keys()]
        for param_name, param_value in params.items():
            prop = properties.get(param_name)
            if prop is None:
                suggestion = get_close_matches(str(param_name), known_param_names, n=1, cutoff=0.76)
                if suggestion:
                    result.warnings.append(f"unknown_param:{param_name}:did_you_mean:{suggestion[0]}")
                else:
                    result.warnings.append(f"unknown_param:{param_name}")
                continue
            expected_type = prop.get("type")
            if expected_type == "bool" and not isinstance(param_value, bool):
                result.warnings.append(f"param_type:{param_name}:expected_bool")
            elif expected_type == "number" and not isinstance(param_value, (int, float)):
                result.warnings.append(f"param_type:{param_name}:expected_number")
            elif expected_type == "array" and not isinstance(param_value, list):
                result.warnings.append(f"param_type:{param_name}:expected_array")
            elif expected_type == "string" and not isinstance(param_value, str):
                result.warnings.append(f"param_type:{param_name}:expected_string")
        results.append(result)

    issues = [issue for result in results for issue in result.issues]
    warnings = [warning for result in results for warning in result.warnings]
    success = not issues and (not strict or not warnings)
    return {
        "success": success,
        "strict": strict,
        "issues": issues,
        "warnings": warnings,
        "results": [result.to_json() for result in results],
    }
