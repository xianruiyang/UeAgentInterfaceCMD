"""Bounded repository file inventory."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from threading import RLock
from typing import Iterable


DEFAULT_EXCLUDED_DIR_NAMES = frozenset(
    {
        ".git",
        ".pytest_cache",
        "__pycache__",
        "Binaries",
        "DerivedDataCache",
        "Intermediate",
        "runtimeLogs",
    }
)


@dataclass(frozen=True, slots=True)
class FileInventoryEntry:
    path: Path
    size: int
    mtime_ns: int


class BoundedFileInventory:
    def __init__(self, entries: Iterable[FileInventoryEntry]) -> None:
        ordered = sorted(entries, key=lambda item: item.path.as_posix().casefold())
        self._entries = tuple(ordered)
        self._text_cache: dict[Path, str | None] = {}
        self._text_lock = RLock()

    @property
    def entries(self) -> tuple[FileInventoryEntry, ...]:
        return self._entries

    def files_under(
        self,
        root: Path,
        *,
        suffixes: set[str] | frozenset[str] | None = None,
    ) -> tuple[Path, ...]:
        resolved_root = root.resolve()
        normalized_suffixes = {suffix.lower() for suffix in suffixes} if suffixes is not None else None
        return tuple(
            entry.path
            for entry in self._entries
            if (entry.path.parent == resolved_root or resolved_root in entry.path.parents)
            and (normalized_suffixes is None or entry.path.suffix.lower() in normalized_suffixes)
        )

    def read_text(self, path: Path) -> str:
        resolved = path.resolve()
        with self._text_lock:
            if resolved in self._text_cache:
                cached = self._text_cache[resolved]
                if cached is None:
                    raise UnicodeDecodeError("utf-8", b"", 0, 1, "cached decode failure")
                return cached
        try:
            text = resolved.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            with self._text_lock:
                self._text_cache[resolved] = None
            raise
        with self._text_lock:
            self._text_cache[resolved] = text
        return text


def build_bounded_file_inventory(
    roots: Iterable[Path],
    *,
    explicit_files: Iterable[Path] = (),
    excluded_dir_names: frozenset[str] = DEFAULT_EXCLUDED_DIR_NAMES,
) -> BoundedFileInventory:
    resolved_roots = _minimal_roots(roots)
    seen: set[Path] = set()
    entries: list[FileInventoryEntry] = []

    for root in resolved_roots:
        if not root.is_dir():
            continue
        for path in root.rglob("*"):
            if not path.is_file():
                continue
            resolved = path.resolve()
            if resolved in seen or any(part in excluded_dir_names for part in resolved.parts):
                continue
            seen.add(resolved)
            stat = resolved.stat()
            entries.append(FileInventoryEntry(resolved, stat.st_size, stat.st_mtime_ns))

    for path in explicit_files:
        resolved = path.resolve()
        if resolved in seen or not resolved.is_file():
            continue
        seen.add(resolved)
        stat = resolved.stat()
        entries.append(FileInventoryEntry(resolved, stat.st_size, stat.st_mtime_ns))

    return BoundedFileInventory(entries)


def _minimal_roots(roots: Iterable[Path]) -> tuple[Path, ...]:
    unique = sorted({path.resolve() for path in roots}, key=lambda path: (len(path.parts), path.as_posix().casefold()))
    selected: list[Path] = []
    for candidate in unique:
        if any(parent == candidate or parent in candidate.parents for parent in selected):
            continue
        selected.append(candidate)
    return tuple(selected)
