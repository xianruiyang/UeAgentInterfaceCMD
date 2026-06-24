from __future__ import annotations

import re
from typing import Any

from .errors import PlanError

VAR_PATTERN = re.compile(r"\{\{\s*([a-zA-Z0-9_.-]+)\s*\}\}")


def deep_merge(base: dict, override: dict) -> dict:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def _resolve_variable(name: str, variables: dict) -> Any:
    if name not in variables:
        raise PlanError(f"模板变量未提供: {name}")
    return variables[name]


def render_value(value: Any, variables: dict, path: str = "$") -> Any:
    if isinstance(value, dict):
        return {k: render_value(v, variables, f"{path}.{k}") for k, v in value.items()}
    if isinstance(value, list):
        return [render_value(v, variables, f"{path}[{i}]") for i, v in enumerate(value)]
    if isinstance(value, str):
        full = VAR_PATTERN.fullmatch(value)
        if full:
            return _resolve_variable(full.group(1), variables)

        def replace_match(match: re.Match[str]) -> str:
            name = match.group(1)
            resolved = _resolve_variable(name, variables)
            return str(resolved)

        return VAR_PATTERN.sub(replace_match, value)
    return value


def normalize_phases(raw_phases: Any) -> list[dict]:
    if isinstance(raw_phases, list):
        return raw_phases
    if isinstance(raw_phases, dict):
        normalized: list[dict] = []
        for phase_name, phase_body in raw_phases.items():
            if isinstance(phase_body, list):
                normalized.append(
                    {
                        "name": phase_name,
                        "stop_on_error": True,
                        "commands": phase_body,
                    }
                )
            elif isinstance(phase_body, dict):
                phase_copy = dict(phase_body)
                phase_copy.setdefault("name", phase_name)
                phase_copy.setdefault("stop_on_error", True)
                phase_copy.setdefault("commands", [])
                normalized.append(phase_copy)
            else:
                raise PlanError(f"phase `{phase_name}` 格式非法，应为 list 或 dict")
        return normalized
    raise PlanError("plan.phases 格式非法，应为 list 或 dict")

