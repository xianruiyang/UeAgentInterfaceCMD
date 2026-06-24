from __future__ import annotations

import json
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
SMOKE_SINGLE_WORD_COMMANDS = {"redo", "undo"}
DOC_SINGLE_WORD_COMMANDS = {"redo", "undo"}
DEPRECATED_ALLOWED_USE_CASES = [
    "bootstrap",
    "compatibility",
    "diagnostic",
    "migration",
    "repair",
    "schema_boundary",
    "smoke",
]


@dataclass(slots=True)
class CommandDoc:
    name: str
    doc_file: str = ""
    section: str = ""
    description: str = ""
    params: list[str] = field(default_factory=list)
    returns: list[str] = field(default_factory=list)
    deprecated: bool = False
    deprecated_scope: str = ""
    deprecated_reason: str = ""
    replacement: list[str] = field(default_factory=list)
    implemented: bool = False
    implementation_files: list[str] = field(default_factory=list)
    smoke_tested: bool = False
    smoke_files: list[str] = field(default_factory=list)

    def to_json(self) -> dict[str, Any]:
        lifecycle = "deprecated" if self.deprecated else "active"
        return {
            "name": self.name,
            "lifecycle": lifecycle,
            "doc_file": self.doc_file,
            "section": self.section,
            "description": self.description,
            "params": self.params,
            "param_schema": build_param_schema(self.params),
            "returns": self.returns,
            "deprecated": self.deprecated,
            "deprecated_scope": self.deprecated_scope,
            "deprecated_reason": self.deprecated_reason,
            "allowed_use_cases": list(DEPRECATED_ALLOWED_USE_CASES) if self.deprecated else [],
            "replacement": self.replacement,
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


def _extract_command_replacements(text: str) -> list[str]:
    values: list[str] = []
    seen: set[str] = set()
    for name in COMMAND_TOKEN_RE.findall(text):
        if name in seen:
            continue
        seen.add(name)
        values.append(name)
    return values


def _extract_heading_commands(line: str) -> list[str]:
    heading = line.lstrip("#").strip()
    values: list[str] = []
    previous_end = 0
    for match in COMMAND_TOKEN_RE.finditer(heading):
        separator = heading[previous_end : match.start()]
        if separator.strip(" \t/、,，&+()") != "":
            break
        name = match.group(1)
        if "_" in name or name in DOC_SINGLE_WORD_COMMANDS:
            values.append(name)
        previous_end = match.end()
    return values


def _parse_doc_file(path: Path, plugin_root: Path, *, deprecated: bool = False) -> dict[str, CommandDoc]:
    docs: dict[str, CommandDoc] = {}
    section = ""
    in_command_table = False
    relative_doc = path.relative_to(plugin_root).as_posix()
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line.startswith("### "):
            section = line.lstrip("#").strip()
            in_command_table = False
            commands = _extract_heading_commands(line)
            for name in commands:
                current = docs.get(name) or CommandDoc(name=name)
                current.doc_file = relative_doc
                current.section = section
                current.deprecated = deprecated
                docs[name] = current
            continue
        if line.startswith("## "):
            section = line.lstrip("#").strip()
            in_command_table = False
            continue
        cells = _split_markdown_row(line)
        if len(cells) < 2:
            if deprecated and "Deprecated" in line:
                commands = [name for name in COMMAND_TOKEN_RE.findall(line) if "_" in name or name in DOC_SINGLE_WORD_COMMANDS]
                for name in commands:
                    current = docs.get(name) or CommandDoc(name=name)
                    current.doc_file = relative_doc
                    current.section = section
                    current.description = line.strip()
                    current.deprecated = True
                    current.deprecated_scope = "authoring"
                    current.deprecated_reason = line.strip()
                    current.replacement = sorted(set(current.replacement + _extract_command_replacements(line)))
                    docs[name] = current
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
        commands = [name for name in COMMAND_TOKEN_RE.findall(cells[0]) if "_" in name or name in DOC_SINGLE_WORD_COMMANDS]
        if not commands:
            continue
        description = cells[1]
        params = _extract_tokens(cells[2]) if len(cells) >= 3 else []
        returns = _extract_tokens(cells[3]) if len(cells) >= 4 else []
        replacements = _extract_command_replacements(cells[2]) if deprecated and len(cells) >= 3 else []
        for name in commands:
            current = docs.get(name) or CommandDoc(name=name)
            current.doc_file = relative_doc
            current.section = section
            current.description = description
            current.params = sorted(set(current.params + params))
            current.returns = sorted(set(current.returns + returns))
            current.deprecated = deprecated
            if deprecated:
                current.deprecated_scope = "authoring"
                current.deprecated_reason = description
                current.replacement = sorted(set(current.replacement + replacements))
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
            if "_" not in command and command not in SMOKE_SINGLE_WORD_COMMANDS:
                continue
            results.setdefault(command, [])
            if relative not in results[command]:
                results[command].append(relative)
    return results


def _scan_smoke_coverage_ledger(plugin_root: Path) -> dict[str, list[str]]:
    ledger_path = plugin_root / "docs" / "smoke_coverage_ledger.json"
    if not ledger_path.exists():
        return {}

    try:
        payload = json.loads(ledger_path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {}

    entries = payload.get("entries") if isinstance(payload, dict) else None
    if not isinstance(entries, list):
        return {}

    relative = ledger_path.relative_to(plugin_root).as_posix()
    results: dict[str, list[str]] = {}
    for entry in entries:
        if not isinstance(entry, dict):
            continue
        command = str(entry.get("command", "")).strip()
        if not command or ("_" not in command and command not in SMOKE_SINGLE_WORD_COMMANDS):
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
        deprecated_dir = docs_dir / "deprecatedCommand"
        if deprecated_dir.exists():
            for path in sorted(deprecated_dir.glob("*.md")):
                if path.name == "README.md":
                    continue
                for name, doc in _parse_doc_file(path, plugin_root, deprecated=True).items():
                    command_docs.setdefault(name, doc)

    implemented = _scan_implemented_commands(plugin_root)
    smoked = _scan_smoke_commands(plugin_root)
    for name, files in _scan_smoke_coverage_ledger(plugin_root).items():
        smoked.setdefault(name, [])
        for file in files:
            if file not in smoked[name]:
                smoked[name].append(file)
    all_names = sorted(set(command_docs) | set(implemented))
    commands: dict[str, Any] = {}
    for name in all_names:
        item = command_docs.get(name) or CommandDoc(name=name)
        item.replacement = sorted(replacement for replacement in item.replacement if replacement in all_names and replacement != name)
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
        "deprecated_doc_count": sum(1 for item in commands.values() if item.get("deprecated")),
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


def _normalize_deprecated_use_case(use_case: str | None) -> str:
    normalized = str(use_case or "").strip().lower().replace("-", "_")
    return normalized or "authoring"


def validate_command_lifecycle(
    command_names: list[str],
    manifest: dict[str, Any],
    *,
    allow_deprecated: bool = False,
    deprecated_use_case: str | None = None,
) -> dict[str, Any]:
    known = manifest.get("commands")
    if not isinstance(known, dict) or not known:
        return {
            "success": True,
            "allow_deprecated": allow_deprecated,
            "deprecated_use_case": _normalize_deprecated_use_case(deprecated_use_case),
            "deprecated_commands": [],
            "issues": [],
            "warnings": ["command_manifest_unavailable"],
        }

    use_case = _normalize_deprecated_use_case(deprecated_use_case)
    deprecated_commands: list[dict[str, Any]] = []
    seen: set[str] = set()
    for name in command_names:
        if name in seen:
            continue
        seen.add(name)
        item = known.get(name)
        if not isinstance(item, dict) or not bool(item.get("deprecated")):
            continue
        allowed_use_cases = item.get("allowed_use_cases")
        if not isinstance(allowed_use_cases, list) or not allowed_use_cases:
            allowed_use_cases = list(DEPRECATED_ALLOWED_USE_CASES)
        replacement = item.get("replacement")
        deprecated_commands.append(
            {
                "command": name,
                "lifecycle": item.get("lifecycle", "deprecated"),
                "deprecated_scope": item.get("deprecated_scope", "authoring"),
                "deprecated_reason": item.get("deprecated_reason") or item.get("description", ""),
                "allowed_use_cases": allowed_use_cases,
                "replacement": replacement if isinstance(replacement, list) else [],
                "doc_file": item.get("doc_file", ""),
            }
        )

    issues: list[str] = []
    warnings: list[str] = []
    for item in deprecated_commands:
        command = str(item["command"])
        allowed_use_cases = {str(value) for value in item.get("allowed_use_cases", [])}
        if not allow_deprecated:
            issues.append(f"deprecated_command_blocked:{command}")
        elif use_case not in allowed_use_cases:
            issues.append(f"deprecated_command_use_case_not_allowed:{command}:{use_case}")
        else:
            warnings.append(f"deprecated_command_allowed:{command}:{use_case}")

    return {
        "success": not issues,
        "allow_deprecated": allow_deprecated,
        "deprecated_use_case": use_case,
        "deprecated_commands": deprecated_commands,
        "issues": issues,
        "warnings": warnings,
    }


def format_command_lifecycle_error(validation: dict[str, Any]) -> str:
    deprecated_commands = validation.get("deprecated_commands")
    if not isinstance(deprecated_commands, list) or not deprecated_commands:
        return "命令生命周期校验失败"
    names = [str(item.get("command")) for item in deprecated_commands if isinstance(item, dict)]
    use_case = validation.get("deprecated_use_case", "authoring")
    lines = [
        f"废弃 UAI 指令被阻断: {', '.join(names)}",
        f"当前用途: {use_case}",
        "如确需兼容、迁移、诊断或修复，显式传入 --allow-deprecated-command 和 --deprecated-use-case。",
    ]
    for item in deprecated_commands[:5]:
        if not isinstance(item, dict):
            continue
        command = str(item.get("command", ""))
        replacement = item.get("replacement")
        replacement_text = ", ".join(str(value) for value in replacement) if isinstance(replacement, list) else ""
        reason = str(item.get("deprecated_reason") or "").strip()
        detail = f"- {command}"
        if replacement_text:
            detail += f"；替代流程: {replacement_text}"
        if reason:
            detail += f"；原因: {reason}"
        lines.append(detail)
    return "\n".join(lines)
