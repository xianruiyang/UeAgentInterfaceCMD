from __future__ import annotations

from dataclasses import dataclass, field
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
        for param_name, param_value in params.items():
            prop = properties.get(param_name)
            if prop is None:
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
