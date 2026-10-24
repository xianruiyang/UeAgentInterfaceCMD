"""Private local-path resolution shared by model-facing SDK handles."""

from __future__ import annotations

from pathlib import Path, PurePosixPath
from typing import Any

from .errors import UsageError


def find_project_root(connection_source: Path) -> Path:
    candidates = (connection_source.parent, *connection_source.parents, Path.cwd())
    failures = []
    for candidate_index, candidate in enumerate(dict.fromkeys(candidates)):
        try:
            if any(candidate.glob("*.uproject")):
                return candidate.resolve()
        except OSError as exc:
            facts = {"stage": "sdk", "phase": "project_root_search", "candidate_index": candidate_index,
                     "code": "project_root_candidate_unreadable", "exception_type": type(exc).__name__,
                     "message": exc.strerror or "The project-root candidate could not be inspected."}
            for name in ("errno", "winerror"):
                value = getattr(exc, name, None)
                if isinstance(value, int):
                    facts[name] = value
            failures.append(facts)
            continue
    raise UsageError.at_source(
        code="uai_project_root_missing",
        message="the SDK could not locate the current Unreal project root",
        facts={"phase": "project_root_search", "expected_value": "a directory containing a .uproject file",
               **({"diagnostics": failures} if failures else {})},
    )


def resolve_project_relative(
    client: Any,
    value: str | PurePosixPath,
) -> tuple[Path, PurePosixPath]:
    raw = str(value).replace("\\", "/")
    relative = PurePosixPath(raw)
    if not raw or relative.is_absolute():
        raise UsageError.at_source(
            code="project_relative_path_invalid",
            message="use one short project-relative path",
            facts={"property_path": "path", "expected_value": "non-empty project-relative path", "actual_value": raw},
        )
    root = find_project_root(client._connection.source_path)
    absolute = (root / Path(relative)).resolve()
    try:
        absolute.relative_to(root)
    except ValueError:
        raise UsageError.at_source(
            code="project_relative_path_invalid",
            message="project-relative path escapes the current project",
            facts={"property_path": "path", "actual_value": raw},
        ) from None
    return absolute, PurePosixPath(absolute.relative_to(root).as_posix())


__all__ = ["find_project_root", "resolve_project_relative"]
