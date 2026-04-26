from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class CleanupResult:
    target_dir: Path
    before_count: int
    deleted_count: int
    after_count: int


def _trim_json_files(target_dir: Path, max_count: int, keep_count: int) -> CleanupResult:
    target_dir.mkdir(parents=True, exist_ok=True)
    json_files = sorted(
        target_dir.glob("*.json"),
        key=lambda path: path.stat().st_mtime,
        reverse=True,
    )
    before_count = len(json_files)
    if before_count <= max_count:
        return CleanupResult(
            target_dir=target_dir,
            before_count=before_count,
            deleted_count=0,
            after_count=before_count,
        )

    deleted = 0
    for stale_file in json_files[keep_count:]:
        try:
            stale_file.unlink(missing_ok=True)
            deleted += 1
        except OSError:
            continue

    after_count = before_count - deleted
    return CleanupResult(
        target_dir=target_dir,
        before_count=before_count,
        deleted_count=deleted,
        after_count=after_count,
    )


def cleanup_runtime_json(
    app_root: Path,
    reports_dir: Path,
    cleanup_tmp_max: int,
    cleanup_tmp_keep: int,
    cleanup_reports_max: int,
    cleanup_reports_keep: int,
) -> list[CleanupResult]:
    tmp_targets: list[Path] = [app_root / "tmp"]
    if app_root.name.lower() == "dist":
        source_tmp = app_root.parent / "tmp"
        if source_tmp.exists():
            tmp_targets.append(source_tmp)

    results: list[CleanupResult] = []
    seen: set[Path] = set()
    for tmp_target in tmp_targets:
        resolved = tmp_target.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        results.append(_trim_json_files(tmp_target, cleanup_tmp_max, cleanup_tmp_keep))

    results.append(_trim_json_files(reports_dir, cleanup_reports_max, cleanup_reports_keep))
    return results
