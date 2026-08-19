"""Development-repository path discovery."""

from __future__ import annotations

import os
from pathlib import Path


def find_project_root(start: Path | None = None) -> Path | None:
    current = (start or Path.cwd()).resolve()
    candidates = [current] + list(current.parents)
    for candidate in candidates:
        if any(candidate.glob("*.uproject")):
            return candidate
        if (candidate / "Plugins" / "UeAgentInterface").exists() and any(candidate.glob("*.uproject")):
            return candidate
    return None


def find_development_project_root(app_root: Path, *, include_cwd: bool = True) -> Path | None:
    candidates = [
        app_root,
        app_root.parent,
        app_root.parent.parent,
    ]
    if include_cwd:
        candidates.append(Path.cwd())
    for candidate in candidates:
        root = find_project_root(candidate)
        if root is not None:
            return root
    return None


def find_plugin_root(project_root: Path) -> Path | None:
    direct = project_root / "Plugins" / "UeAgentInterface"
    if direct.exists():
        return direct
    pak_plugin = project_root / "UeAgentInterfacePak" / "UeAgentInterface"
    if pak_plugin.exists():
        return pak_plugin
    return None


def find_pak_root(project_root: Path) -> Path | None:
    candidate = project_root / "UeAgentInterfacePak"
    if candidate.exists():
        return candidate
    return None


def runtime_logs_dir(app_root: Path, project_root: Path | None = None) -> Path:
    runtime_root_override = os.environ.get("UAI_RUNTIME_ROOT", "").strip()
    if runtime_root_override:
        return Path(runtime_root_override).expanduser().resolve()
    if project_root is not None:
        return project_root / "runtimeLogs"
    detected = find_development_project_root(app_root, include_cwd=True)
    if detected is not None:
        return detected / "runtimeLogs"
    return Path.cwd().resolve() / "runtimeLogs"
