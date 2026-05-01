from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .command_schema import build_param_schema
from .project_paths import find_development_project_root, find_plugin_root
from .utils import now_compact, save_json_file


COMMAND_TOKEN_RE = re.compile(r"`([a-z][a-z0-9_]{2,})`")
IMPLEMENTED_COMMAND_PATTERNS = [
    re.compile(r'CommandLower\s*==\s*TEXT\("([a-z][a-z0-9_]+)"\)'),
    re.compile(r'\{\s*TEXT\("([a-z][a-z0-9_]+)"\)\s*,\s*&(?:Invoke|FUeAgentHttpServer::)'),
]
SMOKE_COMMAND_RE = re.compile(r'TEXT\("([a-z][a-z0-9_]+)"\)')
PARAM_TOKEN_RE = re.compile(r"`([^`]+)`")


@dataclass(slots=True)
class CommandDoc:
    name: str
    doc_file: str = ""
    section: str = ""
    description: str = ""
    params: list[str] = field(default_factory=list)
    returns: list[str] = field(default_factory=list)
    implemented: bool = False
    implementation_files: list[str] = field(default_factory=list)
    smoke_tested: bool = False
    smoke_files: list[str] = field(default_factory=list)

    def to_json(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "doc_file": self.doc_file,
            "section": self.section,
            "description": self.description,
            "params": self.params,
            "param_schema": build_param_schema(self.params),
            "returns": self.returns,
            "implemented": self.implemented,
            "implementation_files": self.implementation_files,
            "smoke_tested": self.smoke_tested,
            "smoke_files": self.smoke_files,
        }


def _split_markdown_row(line: str) -> list[str]:
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return []
    return [cell.strip() for cell in stripped.strip("|").split("|")]


def _extract_tokens(text: str) -> list[str]:
    seen: set[str] = set()
    values: list[str] = []
    for raw in PARAM_TOKEN_RE.findall(text):
        token = raw.strip()
        if not token or token in seen:
            continue
        seen.add(token)
        values.append(token)
    return values


def _parse_doc_file(path: Path, plugin_root: Path) -> dict[str, CommandDoc]:
    docs: dict[str, CommandDoc] = {}
    section = ""
    in_command_table = False
    relative_doc = path.relative_to(plugin_root).as_posix()
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("## "):
            section = line.lstrip("#").strip()
            in_command_table = False
            continue
        cells = _split_markdown_row(line)
        if len(cells) < 2:
            in_command_table = False
            continue
        first_cell = cells[0].strip()
        if first_cell in {"指令", "命令", "Command"}:
            in_command_table = True
            continue
        if set(first_cell) <= {"-", " "}:
            continue
        if not in_command_table:
            continue
        commands = [name for name in COMMAND_TOKEN_RE.findall(cells[0]) if "_" in name]
        if not commands:
            continue
        description = cells[1]
        params = _extract_tokens(cells[2]) if len(cells) >= 3 else []
        returns = _extract_tokens(cells[3]) if len(cells) >= 4 else []
        for name in commands:
            current = docs.get(name) or CommandDoc(name=name)
            current.doc_file = relative_doc
            current.section = section
            current.description = description
            current.params = sorted(set(current.params + params))
            current.returns = sorted(set(current.returns + returns))
            docs[name] = current
    return docs


def _scan_implemented_commands(plugin_root: Path) -> dict[str, list[str]]:
    source_root = plugin_root / "Source" / "UeAgentInterface" / "Private"
    results: dict[str, list[str]] = {}
    if not source_root.exists():
        return results
    for path in sorted(
        item
        for item in source_root.rglob("*")
        if item.is_file() and item.suffix.lower() in {".cpp", ".inl", ".h"}
    ):
        text = path.read_text(encoding="utf-8-sig", errors="ignore")
        relative = path.relative_to(plugin_root).as_posix()
        for pattern in IMPLEMENTED_COMMAND_PATTERNS:
            for command in pattern.findall(text):
                if command.endswith("_"):
                    continue
                results.setdefault(command, [])
                if relative not in results[command]:
                    results[command].append(relative)
    return results


def _scan_smoke_commands(plugin_root: Path) -> dict[str, list[str]]:
    source_root = plugin_root / "Source"
    results: dict[str, list[str]] = {}
    if not source_root.exists():
        return results
    for path in sorted(item for item in source_root.rglob("*Smoke*.cpp") if item.is_file()):
        text = path.read_text(encoding="utf-8-sig", errors="ignore")
        relative = path.relative_to(plugin_root).as_posix()
        for command in SMOKE_COMMAND_RE.findall(text):
            if "_" not in command:
                continue
            results.setdefault(command, [])
            if relative not in results[command]:
                results[command].append(relative)
    return results


def build_command_manifest(project_root: Path | None = None) -> dict[str, Any]:
    root = project_root or find_development_project_root(Path.cwd())
    if root is None:
        return {
            "schema": "ue_agent_interface.command_manifest.v1",
            "generated_at": now_compact(),
            "project_root": "",
            "plugin_root": "",
            "command_count": 0,
            "commands": {},
            "warnings": ["project_root_not_found"],
        }

    plugin_root = find_plugin_root(root)
    if plugin_root is None:
        return {
            "schema": "ue_agent_interface.command_manifest.v1",
            "generated_at": now_compact(),
            "project_root": str(root),
            "plugin_root": "",
            "command_count": 0,
            "commands": {},
            "warnings": ["plugin_root_not_found"],
        }

    command_docs: dict[str, CommandDoc] = {}
    docs_dir = plugin_root / "docs" / "commands"
    if docs_dir.exists():
        for path in sorted(docs_dir.glob("*.md")):
            if path.name == "README.md":
                continue
            for name, doc in _parse_doc_file(path, plugin_root).items():
                command_docs[name] = doc

    implemented = _scan_implemented_commands(plugin_root)
    smoked = _scan_smoke_commands(plugin_root)
    all_names = sorted(set(command_docs) | set(implemented))
    commands: dict[str, Any] = {}
    for name in all_names:
        item = command_docs.get(name) or CommandDoc(name=name)
        item.implemented = name in implemented
        item.implementation_files = sorted(implemented.get(name, []))
        item.smoke_tested = name in smoked
        item.smoke_files = sorted(smoked.get(name, []))
        commands[name] = item.to_json()

    warnings: list[str] = []
    missing_docs = [name for name, item in commands.items() if item["implemented"] and not item["doc_file"]]
    missing_impl = [name for name, item in commands.items() if item["doc_file"] and not item["implemented"]]
    if missing_docs:
        warnings.append(f"implemented_without_doc:{len(missing_docs)}")
    if missing_impl:
        warnings.append(f"documented_without_implementation:{len(missing_impl)}")

    return {
        "schema": "ue_agent_interface.command_manifest.v1",
        "generated_at": now_compact(),
        "project_root": str(root),
        "plugin_root": str(plugin_root),
        "command_count": len(commands),
        "documented_count": sum(1 for item in commands.values() if item["doc_file"]),
        "implemented_count": sum(1 for item in commands.values() if item["implemented"]),
        "smoke_tested_count": sum(1 for item in commands.values() if item["smoke_tested"]),
        "commands": commands,
        "warnings": warnings,
    }


def save_command_manifest(path: Path, project_root: Path | None = None) -> dict[str, Any]:
    manifest = build_command_manifest(project_root)
    save_json_file(path, manifest)
    return manifest


def command_names_from_batch(commands: list[dict[str, Any]]) -> list[str]:
    names: list[str] = []
    for command in commands:
        name = command.get("command")
        if isinstance(name, str) and name:
            names.append(name)
    return names


def validate_command_names(command_names: list[str], manifest: dict[str, Any]) -> tuple[list[str], list[str]]:
    known = manifest.get("commands")
    if not isinstance(known, dict) or not known:
        return [], ["command_manifest_unavailable"]
    unknown = sorted({name for name in command_names if name not in known})
    warnings: list[str] = []
    for name in command_names:
        item = known.get(name)
        if isinstance(item, dict) and item.get("doc_file") and not item.get("implemented"):
            warnings.append(f"documented_but_not_detected_in_dispatch:{name}")
    return unknown, warnings
