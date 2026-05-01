from __future__ import annotations

import hashlib
from pathlib import Path
from typing import Any

from .command_manifest import build_command_manifest
from .coverage_policy import classify_smoke_coverage, summarize_smoke_coverage
from .project_paths import find_development_project_root, find_pak_root, find_plugin_root
from .utils import now_compact, save_json_file


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def build_coverage_matrix(project_root: Path | None = None) -> dict[str, Any]:
    root = project_root or find_development_project_root(Path.cwd())
    manifest = build_command_manifest(root)
    rows: list[dict[str, Any]] = []
    commands = manifest.get("commands", {})
    if isinstance(commands, dict):
        for name in sorted(commands):
            item = commands[name]
            if not isinstance(item, dict):
                continue
            doc_file = str(item.get("doc_file", ""))
            doc_status = "explicit" if doc_file else ("generated_catalog" if item.get("implemented") else "missing")
            if not doc_file and item.get("implemented"):
                doc_file = "docs/generated/implemented_command_catalog.md"
            row = {
                "command": name,
                "doc_file": doc_file,
                "doc_status": doc_status,
                "implemented": bool(item.get("implemented", False)),
                "smoke_tested": bool(item.get("smoke_tested", False)),
                "implementation_files": item.get("implementation_files", []),
                "smoke_files": item.get("smoke_files", []),
            }
            smoke_classification = classify_smoke_coverage(row).to_json()
            row.update(
                {
                    "smoke_coverage_status": smoke_classification["status"],
                    "smoke_coverage_priority": smoke_classification["priority"],
                    "smoke_coverage_reason": smoke_classification["reason"],
                    "smoke_coverage_recommended_action": smoke_classification["recommended_action"],
                    "smoke_coverage_actionable": smoke_classification["actionable"],
                }
            )
            rows.append(row)
    missing_doc = [row["command"] for row in rows if row["implemented"] and row["doc_status"] == "missing"]
    missing_impl = [row["command"] for row in rows if row["doc_file"] and not row["implemented"]]
    missing_smoke = [row["command"] for row in rows if row["implemented"] and not row["smoke_tested"]]
    smoke_debt = [
        {
            "command": row["command"],
            "status": row["smoke_coverage_status"],
            "priority": row["smoke_coverage_priority"],
            "reason": row["smoke_coverage_reason"],
            "recommended_action": row["smoke_coverage_recommended_action"],
            "doc_file": row["doc_file"],
        }
        for row in rows
        if row["implemented"] and not row["smoke_tested"]
    ]
    smoke_summary = summarize_smoke_coverage(rows)
    return {
        "schema": "ue_agent_interface.coverage_matrix.v2",
        "generated_at": now_compact(),
        "project_root": str(root or ""),
        "command_count": len(rows),
        "missing_doc": missing_doc,
        "missing_implementation": missing_impl,
        "missing_smoke": missing_smoke,
        "smoke_debt": smoke_debt,
        "smoke_coverage": smoke_summary,
        "raw_generated_doc_count": sum(1 for row in rows if row["doc_status"] == "generated_catalog"),
        "rows": rows,
    }


def _write_generated_catalog(matrix: dict[str, Any], output_dir: Path) -> Path:
    path = output_dir / "implemented_command_catalog.md"
    lines = [
        "# Implemented Command Catalog",
        "",
        "本文件由 `uai-cli release coverage` 生成，用于补齐 dispatch 中已实现但未出现在显式命令表里的命令索引。",
        "",
        "| Command | Implementation | Smoke |",
        "| --- | --- | --- |",
    ]
    for row in matrix.get("rows", []):
        if not isinstance(row, dict) or row.get("doc_status") != "generated_catalog":
            continue
        impl = ", ".join(row.get("implementation_files", []))
        smoke = ", ".join(row.get("smoke_files", [])) if row.get("smoke_files") else ""
        lines.append(f"| `{row['command']}` | `{impl}` | `{smoke}` |")
    output_dir.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def _write_smoke_debt_report(matrix: dict[str, Any], output_dir: Path) -> Path:
    path = output_dir / "smoke_coverage_debt.md"
    smoke_coverage = matrix.get("smoke_coverage", {})
    status_counts = smoke_coverage.get("status_counts", {}) if isinstance(smoke_coverage, dict) else {}
    priority_counts = smoke_coverage.get("priority_counts", {}) if isinstance(smoke_coverage, dict) else {}
    rows = [row for row in matrix.get("rows", []) if isinstance(row, dict) and row.get("implemented") and not row.get("smoke_tested")]

    lines = [
        "# UAI Smoke Coverage Debt",
        "",
        "本文件由 `uai-cli release coverage` 生成，用于把 `missing_smoke` 拆成可执行的分类债务。",
        "",
        "## Summary",
        "",
        f"- generated_at: `{matrix.get('generated_at', '')}`",
        f"- command_count: `{matrix.get('command_count', 0)}`",
        f"- direct_smoke_missing: `{len(matrix.get('missing_smoke', []))}`",
        f"- actionable_missing: `{smoke_coverage.get('actionable_missing_count', 0) if isinstance(smoke_coverage, dict) else 0}`",
        f"- p0_count: `{smoke_coverage.get('p0_count', 0) if isinstance(smoke_coverage, dict) else 0}`",
        f"- p1_count: `{smoke_coverage.get('p1_count', 0) if isinstance(smoke_coverage, dict) else 0}`",
        "",
        "## Status Counts",
        "",
        "| Status | Count |",
        "| --- | --- |",
    ]
    for status, count in sorted(status_counts.items()):
        lines.append(f"| `{status}` | {count} |")
    lines.extend(
        [
            "",
            "## Priority Counts",
            "",
            "| Priority | Count |",
            "| --- | --- |",
        ]
    )
    for priority, count in sorted(priority_counts.items()):
        lines.append(f"| `{priority}` | {count} |")
    lines.extend(
        [
            "",
            "## Debt Items",
            "",
            "| Priority | Status | Command | Doc | Recommended Action |",
            "| --- | --- | --- | --- | --- |",
        ]
    )
    priority_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3, "covered": 4, "n/a": 5}
    for row in sorted(rows, key=lambda item: (priority_order.get(str(item.get("smoke_coverage_priority", "")), 99), str(item.get("command", "")))):
        lines.append(
            "| "
            f"`{row.get('smoke_coverage_priority', '')}` | "
            f"`{row.get('smoke_coverage_status', '')}` | "
            f"`{row.get('command', '')}` | "
            f"`{row.get('doc_file', '')}` | "
            f"{row.get('smoke_coverage_recommended_action', '')} |"
        )
    output_dir.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def write_coverage_matrix(output_json: Path, output_md: Path | None = None, project_root: Path | None = None) -> dict[str, Any]:
    matrix = build_coverage_matrix(project_root)
    save_json_file(output_json, matrix)
    catalog_file = _write_generated_catalog(matrix, output_json.parent)
    smoke_debt_file = _write_smoke_debt_report(matrix, output_json.parent)
    matrix["generated_catalog_file"] = str(catalog_file)
    matrix["smoke_debt_file"] = str(smoke_debt_file)
    save_json_file(output_json, matrix)
    if output_md is not None:
        smoke_coverage = matrix.get("smoke_coverage", {})
        lines = [
            "# UAI Command Coverage Matrix",
            "",
            f"- generated_at: `{matrix['generated_at']}`",
            f"- command_count: `{matrix['command_count']}`",
            f"- missing_doc: `{len(matrix['missing_doc'])}`",
            f"- missing_implementation: `{len(matrix['missing_implementation'])}`",
            f"- missing_smoke: `{len(matrix['missing_smoke'])}`",
            f"- smoke_actionable_missing: `{smoke_coverage.get('actionable_missing_count', 0) if isinstance(smoke_coverage, dict) else 0}`",
            f"- smoke_p0_count: `{smoke_coverage.get('p0_count', 0) if isinstance(smoke_coverage, dict) else 0}`",
            f"- smoke_p1_count: `{smoke_coverage.get('p1_count', 0) if isinstance(smoke_coverage, dict) else 0}`",
            f"- generated_doc_catalog_count: `{matrix['raw_generated_doc_count']}`",
            f"- generated_catalog_file: `{catalog_file}`",
            f"- smoke_debt_file: `{smoke_debt_file}`",
            "",
            "## Smoke Status Counts",
            "",
            "| Status | Count |",
            "| --- | --- |",
        ]
        status_counts = smoke_coverage.get("status_counts", {}) if isinstance(smoke_coverage, dict) else {}
        for status, count in sorted(status_counts.items()):
            lines.append(f"| `{status}` | {count} |")
        lines.extend(
            [
                "",
                "## Commands",
                "",
                "| Command | Doc | Implemented | Smoke | Smoke Status | Priority |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for row in matrix["rows"]:
            lines.append(
                f"| `{row['command']}` | `{row['doc_file']}` | {row['implemented']} | {row['smoke_tested']} | "
                f"`{row['smoke_coverage_status']}` | `{row['smoke_coverage_priority']}` |"
            )
        output_md.parent.mkdir(parents=True, exist_ok=True)
        output_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return matrix


def verify_pak_layout(project_root: Path | None = None) -> dict[str, Any]:
    root = project_root or find_development_project_root(Path.cwd())
    if root is None:
        return {"success": False, "issues": ["project_root_not_found"], "warnings": []}
    pak_root = find_pak_root(root)
    if pak_root is None:
        return {"success": False, "issues": ["pak_root_not_found"], "warnings": []}

    required_paths = [
        pak_root / "README.md",
        pak_root / "UeAgentInterface",
        pak_root / "UeAgentInterfaceCMD",
        pak_root / "skills" / "ue-agent-interface" / "SKILL.md",
        pak_root / "skills" / "ue-agent-interface" / "references" / "command-map.md",
    ]
    issues = [f"missing:{path.relative_to(pak_root).as_posix()}" for path in required_paths if not path.exists()]
    warnings: list[str] = []

    dev_plugin = find_plugin_root(root)
    pak_plugin = pak_root / "UeAgentInterface"
    if dev_plugin and pak_plugin.exists():
        dev_uplugin = dev_plugin / "UeAgentInterface.uplugin"
        pak_uplugin = pak_plugin / "UeAgentInterface.uplugin"
        if dev_uplugin.exists() and pak_uplugin.exists() and _sha256(dev_uplugin) != _sha256(pak_uplugin):
            warnings.append("uplugin_hash_diff")

    dev_cli = root / "UeAgentInterfaceCMD"
    pak_cli = pak_root / "UeAgentInterfaceCMD"
    for relative in ["cli/uai_cli/main.py", "docs/USAGE.md", "uai-cli.default.json"]:
        dev_file = dev_cli / relative
        pak_file = pak_cli / relative
        if dev_file.exists() and pak_file.exists():
            if _sha256(dev_file) != _sha256(pak_file):
                warnings.append(f"cli_hash_diff:{relative}")
        elif dev_file.exists() or pak_file.exists():
            issues.append(f"cli_file_presence_mismatch:{relative}")

    installed_skill = Path.home() / ".codex" / "skills" / "ue-agent-interface" / "SKILL.md"
    pak_skill = pak_root / "skills" / "ue-agent-interface" / "SKILL.md"
    if installed_skill.exists() and pak_skill.exists() and _sha256(installed_skill) != _sha256(pak_skill):
        warnings.append("installed_skill_hash_diff")

    manifest_files: list[dict[str, Any]] = []
    for path in required_paths:
        if path.is_file():
            manifest_files.append(
                {
                    "path": path.relative_to(pak_root).as_posix(),
                    "sha256": _sha256(path),
                    "size": path.stat().st_size,
                }
            )

    return {
        "schema": "ue_agent_interface.pak_verify.v1",
        "generated_at": now_compact(),
        "success": not issues,
        "project_root": str(root),
        "pak_root": str(pak_root),
        "issues": issues,
        "warnings": warnings,
        "files": manifest_files,
    }
