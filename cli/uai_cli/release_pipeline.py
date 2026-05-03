from __future__ import annotations

import hashlib
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .project_paths import find_development_project_root, find_pak_root
from .quality_gate import run_quality_gate
from .release_verify import build_coverage_matrix, verify_pak_layout, write_coverage_matrix
from .utils import now_compact, save_json_file


TREE_EXCLUDED_DIRS = {
    ".git",
    ".vs",
    "__pycache__",
    ".pytest_cache",
    "Binaries",
    "DerivedDataCache",
    "Intermediate",
    "Saved",
    "dist",
    "logs",
    "reports",
    "runtimeLogs",
    "tmp",
}
TREE_EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".log", ".tmp"}

RELEASE_FORBIDDEN_DIRS = {
    ".pytest_cache",
    "__pycache__",
    "Binaries",
    "DerivedDataCache",
    "Intermediate",
    "Saved",
    "build_tmp",
    "logs",
    "reports",
    "runtimeLogs",
    "tmp",
}

RELEASE_FORBIDDEN_SUFFIXES = {".log", ".tmp", ".pyc", ".pyo"}

RELEASE_ALLOWED_FORBIDDEN_FILES = {
    "UeAgentInterfaceCMD/reports/.gitkeep",
}


def _run_git(path: Path, args: list[str], *, timeout: int = 30) -> dict[str, Any]:
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=path,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return {"returncode": 1, "stdout": "", "stderr": str(error)}
    return {
        "returncode": proc.returncode,
        "stdout": proc.stdout.strip(),
        "stderr": proc.stderr.strip(),
    }


def _git_state(name: str, path: Path) -> dict[str, Any]:
    state: dict[str, Any] = {
        "name": name,
        "path": str(path),
        "exists": path.exists(),
        "is_git_worktree": False,
        "head": "",
        "short_head": "",
        "branch": "",
        "dirty": False,
        "status": [],
        "error": "",
    }
    if not path.exists():
        state["error"] = "path_missing"
        return state

    inside = _run_git(path, ["rev-parse", "--is-inside-work-tree"])
    if inside["returncode"] != 0 or inside["stdout"].lower() != "true":
        state["error"] = "not_a_git_worktree"
        return state

    state["is_git_worktree"] = True
    head = _run_git(path, ["rev-parse", "HEAD"])
    if head["returncode"] == 0:
        state["head"] = head["stdout"]
        state["short_head"] = head["stdout"][:12]
    else:
        state["error"] = head["stderr"] or "head_unavailable"

    branch = _run_git(path, ["rev-parse", "--abbrev-ref", "HEAD"])
    if branch["returncode"] == 0:
        state["branch"] = branch["stdout"]

    status = _run_git(path, ["status", "--porcelain"])
    if status["returncode"] == 0:
        lines = [line for line in status["stdout"].splitlines() if line.strip()]
        state["status"] = lines
        state["dirty"] = bool(lines)
    elif not state["error"]:
        state["error"] = status["stderr"] or "status_unavailable"

    return state


def _should_skip(path: Path, root: Path) -> bool:
    relative_parts = path.relative_to(root).parts
    if any(part in TREE_EXCLUDED_DIRS for part in relative_parts):
        return True
    return path.suffix in TREE_EXCLUDED_SUFFIXES


def _iter_tree_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    files: list[Path] = []
    for path in root.rglob("*"):
        if path.is_dir():
            continue
        if _should_skip(path, root):
            continue
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(root).as_posix())


def _working_tree_hash(root: Path) -> dict[str, Any]:
    digest = hashlib.sha256()
    files = _iter_tree_files(root)
    for path in files:
        relative = path.relative_to(root).as_posix()
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
        digest.update(b"\0")
    return {
        "path": str(root),
        "file_count": len(files),
        "sha256": digest.hexdigest(),
    }


def _tracked_tree_hash(root: Path) -> dict[str, Any]:
    listed = _run_git(root, ["ls-files", "-z"])
    if listed["returncode"] != 0:
        fallback = _working_tree_hash(root)
        fallback["mode"] = "working_tree_fallback"
        fallback["error"] = listed["stderr"] or "git_ls_files_failed"
        return fallback

    digest = hashlib.sha256()
    rel_files = []
    for raw in listed["stdout"].split("\0"):
        relative = raw.strip()
        if not relative:
            continue
        path = root / relative
        if _should_skip(path, root):
            continue
        rel_files.append(relative.replace("\\", "/"))

    missing: list[str] = []
    for relative in sorted(rel_files):
        path = root / relative
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        if not path.exists():
            missing.append(relative)
            digest.update(b"MISSING")
            digest.update(b"\0")
            continue
        blob = _run_git(root, ["hash-object", f"--path={relative}", relative])
        if blob["returncode"] == 0:
            digest.update(blob["stdout"].encode("ascii"))
        else:
            digest.update(hashlib.sha256(path.read_bytes()).hexdigest().encode("ascii"))
        digest.update(b"\0")

    result = {
        "path": str(root),
        "file_count": len(rel_files),
        "sha256": digest.hexdigest(),
        "mode": "git_tracked_clean_filter",
    }
    if missing:
        result["missing"] = missing[:50]
        result["missing_count"] = len(missing)
    return result


def _tree_hash(root: Path) -> dict[str, Any]:
    inside = _run_git(root, ["rev-parse", "--is-inside-work-tree"])
    if inside["returncode"] == 0 and inside["stdout"].lower() == "true":
        return _tracked_tree_hash(root)
    fallback = _working_tree_hash(root)
    fallback["mode"] = "working_tree"
    return fallback


def _is_release_forbidden_path(path: Path, release_root: Path) -> str:
    relative = path.relative_to(release_root).as_posix()
    if relative in RELEASE_ALLOWED_FORBIDDEN_FILES:
        return ""
    parts = set(path.relative_to(release_root).parts)
    forbidden_dirs = sorted(parts.intersection(RELEASE_FORBIDDEN_DIRS))
    if forbidden_dirs:
        return f"forbidden_dir:{forbidden_dirs[0]}:{relative}"
    if path.suffix in RELEASE_FORBIDDEN_SUFFIXES:
        return f"forbidden_suffix:{path.suffix}:{relative}"
    return ""


def build_release_hygiene_check(project_root: Path | None = None) -> dict[str, Any]:
    root = project_root or find_development_project_root(Path.cwd())
    if root is None:
        return {
            "schema": "ue_agent_interface.release_hygiene.v1",
            "generated_at": now_compact(),
            "success": False,
            "issues": ["project_root_not_found"],
            "scanned_file_count": 0,
        }

    pak_root = find_pak_root(root) or (root / "UeAgentInterfacePak")
    if not pak_root.exists():
        return {
            "schema": "ue_agent_interface.release_hygiene.v1",
            "generated_at": now_compact(),
            "success": False,
            "project_root": str(root),
            "pak_root": str(pak_root),
            "issues": ["pak_root_not_found"],
            "scanned_file_count": 0,
        }

    issues: list[str] = []
    scanned_file_count = 0
    for path in sorted(pak_root.rglob("*"), key=lambda item: item.as_posix()):
        if ".git" in path.relative_to(pak_root).parts:
            continue
        if path.is_dir():
            continue
        scanned_file_count += 1
        issue = _is_release_forbidden_path(path, pak_root)
        if issue:
            issues.append(issue)

    return {
        "schema": "ue_agent_interface.release_hygiene.v1",
        "generated_at": now_compact(),
        "success": not issues,
        "project_root": str(root),
        "pak_root": str(pak_root),
        "issues": issues[:500],
        "issue_count": len(issues),
        "scanned_file_count": scanned_file_count,
        "forbidden_dirs": sorted(RELEASE_FORBIDDEN_DIRS),
        "forbidden_suffixes": sorted(RELEASE_FORBIDDEN_SUFFIXES),
        "allowed_exceptions": sorted(RELEASE_ALLOWED_FORBIDDEN_FILES),
    }


def _cleanup_cli_gate_artifacts(cli_root: Path, *, keep_logs: bool = False) -> list[str]:
    removed: list[str] = []
    if not cli_root.exists():
        return removed

    names = ["tmp", "build_tmp", ".pytest_cache"]
    if not keep_logs:
        names.insert(0, "logs")
    for name in names:
        target = cli_root / name
        if target.exists():
            if target.is_dir():
                try:
                    shutil.rmtree(target)
                except OSError as error:
                    removed.append(f"skipped:{target}:{error}")
                    continue
            else:
                try:
                    target.unlink()
                except OSError as error:
                    removed.append(f"skipped:{target}:{error}")
                    continue
            removed.append(str(target))

    reports_dir = cli_root / "reports"
    if reports_dir.exists():
        for path in sorted(reports_dir.rglob("*"), key=lambda item: len(item.parts), reverse=True):
            if path == reports_dir:
                continue
            if path.name == ".gitkeep" and path.parent == reports_dir:
                continue
            if path.is_dir():
                try:
                    path.rmdir()
                except OSError:
                    continue
            else:
                path.unlink()
                removed.append(str(path))
        try:
            reports_dir.rmdir()
            removed.append(str(reports_dir))
        except OSError:
            pass

    for cache_dir in sorted(cli_root.rglob("__pycache__"), key=lambda item: len(item.parts), reverse=True):
        if ".git" in cache_dir.parts:
            continue
        shutil.rmtree(cache_dir)
        removed.append(str(cache_dir))

    for cache_file in sorted(cli_root.rglob("*.py[co]"), key=lambda item: item.as_posix()):
        if ".git" in cache_file.parts:
            continue
        cache_file.unlink()
        removed.append(str(cache_file))

    return removed


def _release_paths(project_root: Path) -> dict[str, Path]:
    pak_root = find_pak_root(project_root) or (project_root / "UeAgentInterfacePak")
    return {
        "project": project_root,
        "dev_plugin": project_root / "Plugins" / "UeAgentInterface",
        "dev_cli": project_root / "UeAgentInterfaceCMD",
        "pak": pak_root,
        "pak_plugin": pak_root / "UeAgentInterface",
        "pak_cli": pak_root / "UeAgentInterfaceCMD",
    }


def build_release_sync_check(project_root: Path | None = None) -> dict[str, Any]:
    root = project_root or find_development_project_root(Path.cwd())
    if root is None:
        return {
            "schema": "ue_agent_interface.release_sync_check.v1",
            "generated_at": now_compact(),
            "success": False,
            "issues": ["project_root_not_found"],
            "warnings": [],
            "repos": {},
            "tree_hashes": {},
        }

    paths = _release_paths(root)
    repo_names = ["project", "dev_plugin", "dev_cli", "pak", "pak_plugin", "pak_cli"]
    repos = {name: _git_state(name, paths[name]) for name in repo_names}
    issues: list[str] = []
    warnings: list[str] = []

    for name, state in repos.items():
        if not state["exists"]:
            issues.append(f"{name}:path_missing")
            continue
        if not state["is_git_worktree"]:
            issues.append(f"{name}:not_a_git_worktree")
            continue
        if state["dirty"]:
            warnings.append(f"{name}:dirty_worktree")

    for dev_name, pak_name, label in [
        ("dev_plugin", "pak_plugin", "plugin"),
        ("dev_cli", "pak_cli", "cli"),
    ]:
        dev_head = str(repos.get(dev_name, {}).get("head", ""))
        pak_head = str(repos.get(pak_name, {}).get("head", ""))
        if dev_head and pak_head and dev_head != pak_head:
            issues.append(f"{label}:commit_mismatch")

    tree_hashes: dict[str, Any] = {}
    for dev_name, pak_name, label in [
        ("dev_plugin", "pak_plugin", "plugin"),
        ("dev_cli", "pak_cli", "cli"),
    ]:
        dev_hash = _tree_hash(paths[dev_name])
        pak_hash = _tree_hash(paths[pak_name])
        tree_hashes[dev_name] = dev_hash
        tree_hashes[pak_name] = pak_hash
        if dev_hash["sha256"] != pak_hash["sha256"]:
            issues.append(f"{label}:tree_hash_mismatch")

    return {
        "schema": "ue_agent_interface.release_sync_check.v1",
        "generated_at": now_compact(),
        "success": not issues,
        "project_root": str(root),
        "issues": sorted(set(issues)),
        "warnings": sorted(set(warnings)),
        "mirror_dirty_worktree": any(
            bool(repos.get(name, {}).get("dirty", False)) for name in ["dev_plugin", "dev_cli"]
        ),
        "repos": repos,
        "tree_hashes": tree_hashes,
    }


def _copy_tree(src: Path, dst: Path, *, dry_run: bool, delete_extra: bool) -> dict[str, Any]:
    src_files = _iter_tree_files(src)
    dst_files = _iter_tree_files(dst)
    src_relatives = {path.relative_to(src).as_posix(): path for path in src_files}
    dst_relatives = {path.relative_to(dst).as_posix(): path for path in dst_files}

    copy_relatives: list[str] = []
    for relative, src_file in sorted(src_relatives.items()):
        dst_file = dst / relative
        if not dst_file.exists() or hashlib.sha256(src_file.read_bytes()).digest() != hashlib.sha256(
            dst_file.read_bytes()
        ).digest():
            copy_relatives.append(relative)

    delete_relatives = sorted(set(dst_relatives) - set(src_relatives)) if delete_extra else []

    if not dry_run:
        for relative in copy_relatives:
            src_file = src_relatives[relative]
            dst_file = dst / relative
            dst_file.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src_file, dst_file)
        for relative in delete_relatives:
            target = dst / relative
            if target.exists() and target.is_file():
                target.unlink()

    return {
        "source": str(src),
        "target": str(dst),
        "dry_run": dry_run,
        "delete_extra": delete_extra,
        "copied_count": len(copy_relatives),
        "deleted_count": len(delete_relatives),
        "copied": copy_relatives[:200],
        "deleted": delete_relatives[:200],
        "truncated": len(copy_relatives) > 200 or len(delete_relatives) > 200,
    }


def mirror_development_to_pak(
    project_root: Path | None = None,
    *,
    dry_run: bool = False,
    delete_extra: bool = False,
) -> dict[str, Any]:
    root = project_root or find_development_project_root(Path.cwd())
    if root is None:
        return {
            "schema": "ue_agent_interface.release_dev_mirror.v1",
            "generated_at": now_compact(),
            "success": False,
            "issues": ["project_root_not_found"],
            "mirrors": [],
        }

    before = build_release_sync_check(root)
    paths = _release_paths(root)
    issues: list[str] = []
    mirrors: list[dict[str, Any]] = []
    for src_name, dst_name in [("dev_plugin", "pak_plugin"), ("dev_cli", "pak_cli")]:
        src = paths[src_name]
        dst = paths[dst_name]
        if not src.exists():
            issues.append(f"{src_name}:path_missing")
            continue
        if not dst.exists():
            issues.append(f"{dst_name}:path_missing")
            continue
        mirrors.append(_copy_tree(src, dst, dry_run=dry_run, delete_extra=delete_extra))

    after = build_release_sync_check(root) if not dry_run else None
    return {
        "schema": "ue_agent_interface.release_dev_mirror.v1",
        "generated_at": now_compact(),
        "success": not issues,
        "project_root": str(root),
        "mode": "dev-mirror",
        "formal_release_allowed": False,
        "mirror_dirty_worktree": bool(before.get("mirror_dirty_worktree", False)),
        "dry_run": dry_run,
        "delete_extra": delete_extra,
        "issues": issues,
        "before": before,
        "after": after,
        "mirrors": mirrors,
    }


def verify_release_pipeline(
    app_root: Path,
    project_root: Path | None = None,
    *,
    run_tests: bool = False,
    allow_dirty: bool = False,
) -> dict[str, Any]:
    root = project_root or find_development_project_root(app_root)
    if root is None:
        return {
            "schema": "ue_agent_interface.release_verify.v1",
            "generated_at": now_compact(),
            "success": False,
            "issues": ["project_root_not_found"],
        }

    sync_check = build_release_sync_check(root)
    coverage = build_coverage_matrix(root)
    gate = run_quality_gate(app_root, run_tests=run_tests)
    issues: list[str] = []

    issues.extend(f"sync:{issue}" for issue in sync_check.get("issues", []))
    if not allow_dirty:
        for name, state in sync_check.get("repos", {}).items():
            if isinstance(state, dict) and state.get("dirty"):
                issues.append(f"dirty_worktree:{name}")

    if coverage.get("missing_doc"):
        issues.append("coverage:missing_doc")
    if coverage.get("missing_implementation"):
        issues.append("coverage:missing_implementation")
    if coverage.get("missing_smoke"):
        issues.append("coverage:missing_smoke")
    if int(coverage.get("raw_generated_doc_count", 0) or 0) > 0:
        issues.append("coverage:generated_doc_catalog")
    if not gate.get("success", False):
        issues.append("quality_gate_failed")

    return {
        "schema": "ue_agent_interface.release_verify.v1",
        "generated_at": now_compact(),
        "success": not issues,
        "project_root": str(root),
        "allow_dirty": allow_dirty,
        "run_tests": run_tests,
        "issues": sorted(set(issues)),
        "sync_check": sync_check,
        "coverage_summary": {
            "command_count": coverage.get("command_count", 0),
            "missing_doc_count": len(coverage.get("missing_doc", [])),
            "missing_implementation_count": len(coverage.get("missing_implementation", [])),
            "missing_smoke_count": len(coverage.get("missing_smoke", [])),
            "generated_doc_catalog_count": coverage.get("raw_generated_doc_count", 0),
        },
        "quality_gate": gate,
    }


def _coverage_summary(coverage: dict[str, Any]) -> dict[str, Any]:
    smoke_coverage = coverage.get("smoke_coverage", {})
    return {
        "command_count": coverage.get("command_count", 0),
        "missing_doc_count": len(coverage.get("missing_doc", [])),
        "missing_implementation_count": len(coverage.get("missing_implementation", [])),
        "missing_smoke_count": len(coverage.get("missing_smoke", [])),
        "generated_doc_catalog_count": coverage.get("raw_generated_doc_count", 0),
        "smoke_actionable_missing_count": smoke_coverage.get("actionable_missing_count", 0)
        if isinstance(smoke_coverage, dict)
        else 0,
        "smoke_p0_count": smoke_coverage.get("p0_count", 0) if isinstance(smoke_coverage, dict) else 0,
        "smoke_p1_count": smoke_coverage.get("p1_count", 0) if isinstance(smoke_coverage, dict) else 0,
    }


def run_formal_release_gate(
    app_root: Path,
    project_root: Path | None = None,
    *,
    run_tests: bool = True,
    allow_dirty: bool = False,
    write_coverage: bool = False,
    ci_output: Path | None = None,
) -> dict[str, Any]:
    root = project_root or find_development_project_root(app_root)
    if root is None:
        return {
            "schema": "ue_agent_interface.release_ci_gate.v1",
            "generated_at": now_compact(),
            "success": False,
            "issues": ["project_root_not_found"],
        }

    coverage_output: dict[str, Any] = {"written": False}
    if write_coverage:
        generated_dir = app_root / "docs" / "generated"
        coverage = write_coverage_matrix(
            generated_dir / "command_coverage_matrix.json",
            generated_dir / "command_coverage_matrix.md",
            root,
        )
        coverage_output = {
            "written": True,
            "json_file": str(generated_dir / "command_coverage_matrix.json"),
            "markdown_file": str(generated_dir / "command_coverage_matrix.md"),
            "generated_catalog_file": coverage.get("generated_catalog_file", ""),
            "smoke_debt_file": coverage.get("smoke_debt_file", ""),
        }
    else:
        coverage = build_coverage_matrix(root)

    sync_check = build_release_sync_check(root)
    pak_verify = verify_pak_layout(root)
    hygiene = build_release_hygiene_check(root)
    pak_cli_root = root / "UeAgentInterfacePak" / "UeAgentInterfaceCMD"
    quality_gate = run_quality_gate(app_root, run_tests=run_tests)
    if pak_cli_root.exists():
        pak_quality_gate = run_quality_gate(pak_cli_root, run_tests=run_tests)
    else:
        pak_quality_gate = {
            "success": False,
            "checks": [
                {
                    "name": "pak_cli_root",
                    "success": False,
                    "details": {"path": str(pak_cli_root), "error": "missing"},
                }
            ],
        }

    test_artifact_cleanup: list[dict[str, Any]] = []
    if run_tests:
        dev_removed = _cleanup_cli_gate_artifacts(app_root, keep_logs=True)
        test_artifact_cleanup.append(
            {"path": str(app_root), "removed": dev_removed, "removed_count": len(dev_removed), "kept_logs": True}
        )
        pak_removed = _cleanup_cli_gate_artifacts(pak_cli_root)
        test_artifact_cleanup.append(
            {"path": str(pak_cli_root), "removed": pak_removed, "removed_count": len(pak_removed), "kept_logs": False}
        )
    hygiene_after_tests = build_release_hygiene_check(root)

    issues: list[str] = []
    for issue in sync_check.get("issues", []):
        issues.append(f"sync:{issue}")
    if not allow_dirty:
        for name, state in sync_check.get("repos", {}).items():
            if isinstance(state, dict) and state.get("dirty"):
                issues.append(f"dirty_worktree:{name}")

    if coverage.get("missing_doc"):
        issues.append("coverage:missing_doc")
    if coverage.get("missing_implementation"):
        issues.append("coverage:missing_implementation")
    if coverage.get("missing_smoke"):
        issues.append("coverage:missing_smoke")
    if int(coverage.get("raw_generated_doc_count", 0) or 0) > 0:
        issues.append("coverage:generated_doc_catalog")

    if not pak_verify.get("success", False):
        issues.append("pak_verify_failed")
    for warning in pak_verify.get("warnings", []):
        issues.append(f"pak_warning:{warning}")

    if not hygiene.get("success", False):
        issues.append("release_hygiene_failed")
    if not hygiene_after_tests.get("success", False):
        issues.append("release_hygiene_after_tests_failed")

    if not quality_gate.get("success", False):
        issues.append("quality_gate_failed")
    if not pak_quality_gate.get("success", False):
        issues.append("pak_quality_gate_failed")

    result = {
        "schema": "ue_agent_interface.release_ci_gate.v1",
        "generated_at": now_compact(),
        "success": not issues,
        "project_root": str(root),
        "app_root": str(app_root),
        "run_tests": run_tests,
        "allow_dirty": allow_dirty,
        "write_coverage": write_coverage,
        "issues": sorted(set(issues)),
        "coverage_output": coverage_output,
        "coverage_summary": _coverage_summary(coverage),
        "sync_check": sync_check,
        "pak_verify": pak_verify,
        "release_hygiene": hygiene,
        "release_hygiene_after_tests": hygiene_after_tests,
        "test_artifact_cleanup": test_artifact_cleanup,
        "quality_gate": quality_gate,
        "pak_quality_gate": pak_quality_gate,
    }
    if ci_output is not None:
        save_json_file(ci_output, result)
        result["ci_output"] = str(ci_output)
    return result


def write_release_manifest(
    app_root: Path,
    project_root: Path | None = None,
    *,
    release_id: str | None = None,
    output_path: Path | None = None,
) -> dict[str, Any]:
    root = project_root or find_development_project_root(app_root)
    if root is None:
        return {
            "schema": "ue_agent_interface.release_manifest.v1",
            "generated_at": now_compact(),
            "success": False,
            "issues": ["project_root_not_found"],
            "manifest_file": "",
        }

    effective_release_id = release_id or now_compact()
    pak_root = find_pak_root(root) or (root / "UeAgentInterfacePak")
    manifest_path = output_path or (pak_root / "releases" / effective_release_id / "manifest.json")
    sync_check = build_release_sync_check(root)
    coverage = build_coverage_matrix(root)
    manifest = {
        "schema": "ue_agent_interface.release_manifest.v1",
        "generated_at": now_compact(),
        "success": True,
        "release_id": effective_release_id,
        "project_root": str(root),
        "manifest_file": str(manifest_path),
        "repos": sync_check.get("repos", {}),
        "tree_hashes": sync_check.get("tree_hashes", {}),
        "sync": {
            "success": sync_check.get("success", False),
            "issues": sync_check.get("issues", []),
            "warnings": sync_check.get("warnings", []),
            "mirror_dirty_worktree": sync_check.get("mirror_dirty_worktree", False),
        },
        "coverage": {
            "command_count": coverage.get("command_count", 0),
            "missing_doc_count": len(coverage.get("missing_doc", [])),
            "missing_implementation_count": len(coverage.get("missing_implementation", [])),
            "missing_smoke_count": len(coverage.get("missing_smoke", [])),
            "generated_doc_catalog_count": coverage.get("raw_generated_doc_count", 0),
        },
    }
    save_json_file(manifest_path, manifest)
    return manifest
