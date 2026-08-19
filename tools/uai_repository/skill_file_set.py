"""Deterministic file-set comparison for repository tooling."""

from __future__ import annotations

import codecs
import hashlib
import os
from dataclasses import dataclass
from pathlib import Path


EXCLUDED_DIR_NAMES = frozenset(
    {
        ".git",
        ".pytest_cache",
        "__pycache__",
        "deprecatedcommand",
        "generated",
        "runtimelogs",
        "tmp",
    }
)
EXCLUDED_FILE_NAMES = frozenset(
    {
        ".ds_store",
        "command_coverage_ledger.json",
        "smoke_coverage_ledger.json",
        "thumbs.db",
    }
)
DEFAULT_MAX_FILES = 250_000
DEFAULT_MAX_DIRECTORIES = 100_000
_READ_CHUNK_SIZE = 1024 * 1024


class FileSetScanError(RuntimeError):
    """Raised when a deterministic file-set scan cannot be completed safely."""


@dataclass(frozen=True)
class FileDigest:
    sha256: str
    content_mode: str
    size: int


@dataclass(frozen=True)
class FileSetComparison:
    source_files: tuple[Path, ...]
    target_files: tuple[Path, ...]
    missing: tuple[Path, ...]
    different: tuple[Path, ...]
    extra: tuple[Path, ...]
    type_mismatches: tuple[Path, ...]
    compared: int


def _path_sort_key(path: Path) -> tuple[str, str]:
    value = path.as_posix()
    return value.casefold(), value


def is_excluded(path: Path) -> bool:
    return (
        path.name.casefold() in EXCLUDED_DIR_NAMES
        or path.name.casefold() in EXCLUDED_FILE_NAMES
    )


def walk_relative_files(
    root: Path,
    *,
    max_files: int = DEFAULT_MAX_FILES,
    max_directories: int = DEFAULT_MAX_DIRECTORIES,
) -> tuple[Path, ...]:
    """Return a bounded, deterministic inventory relative to ``root``."""

    if max_files < 0 or max_directories < 0:
        raise ValueError("file-set limits must be non-negative")
    if not root.exists():
        return ()
    if not root.is_dir():
        raise FileSetScanError(f"not_a_directory:{root}")

    files: list[Path] = []
    directory_count = 0

    def raise_walk_error(error: OSError) -> None:
        raise FileSetScanError(
            f"walk_error:{root}:{error}"
        ) from error

    try:
        for dirpath, dirnames, filenames in os.walk(
            root,
            topdown=True,
            onerror=raise_walk_error,
            followlinks=False,
        ):
            directory_count += 1
            if directory_count > max_directories:
                raise FileSetScanError(
                    "directory_limit_exceeded:"
                    f"{root}:limit={max_directories}"
                )
            current = Path(dirpath)
            dirnames[:] = sorted(
                (
                    name
                    for name in dirnames
                    if name.casefold() not in EXCLUDED_DIR_NAMES
                ),
                key=lambda value: (value.casefold(), value),
            )
            for filename in sorted(
                filenames,
                key=lambda value: (value.casefold(), value),
            ):
                path = current / filename
                if is_excluded(path):
                    continue
                files.append(path.relative_to(root))
                if len(files) > max_files:
                    raise FileSetScanError(
                        "file_limit_exceeded:"
                        f"{root}:limit={max_files}"
                    )
    except FileSetScanError:
        raise
    except OSError as exc:
        raise FileSetScanError(
            f"walk_error:{root}:{exc}"
        ) from exc

    return tuple(sorted(files, key=_path_sort_key))


def file_digest(path: Path) -> FileDigest:
    """
    Hash text using the formal LF normalization and binary byte-exactly.

    A file is text only when the complete payload is valid UTF-8 and contains
    no NUL byte. CRLF and standalone CR are then normalized to LF.
    """

    raw_hasher = hashlib.sha256()
    text_hasher = hashlib.sha256()
    decoder = codecs.getincrementaldecoder("utf-8")("strict")
    is_text = True
    pending_cr = False
    size = 0

    with path.open("rb") as handle:
        for chunk in iter(
            lambda: handle.read(_READ_CHUNK_SIZE),
            b"",
        ):
            size += len(chunk)
            raw_hasher.update(chunk)
            if not is_text:
                continue
            if b"\0" in chunk:
                is_text = False
                continue
            try:
                decoder.decode(chunk, final=False)
            except UnicodeDecodeError:
                is_text = False
                continue

            normalized = (
                (b"\r" if pending_cr else b"") + chunk
            )
            pending_cr = False
            if normalized.endswith(b"\r"):
                normalized = normalized[:-1]
                pending_cr = True
            text_hasher.update(
                normalized.replace(b"\r\n", b"\n").replace(
                    b"\r",
                    b"\n",
                )
            )

    if is_text:
        try:
            decoder.decode(b"", final=True)
        except UnicodeDecodeError:
            is_text = False
        else:
            if pending_cr:
                text_hasher.update(b"\n")

    if is_text:
        return FileDigest(
            sha256=text_hasher.hexdigest(),
            content_mode="utf8_text_lf",
            size=size,
        )
    return FileDigest(
        sha256=raw_hasher.hexdigest(),
        content_mode="binary",
        size=size,
    )


def normalized_sha256(path: Path) -> str:
    return file_digest(path).sha256


def files_equal(source: Path, target: Path) -> bool:
    return normalized_sha256(source) == normalized_sha256(
        target
    )


def compare_file_sets(
    source_root: Path,
    target_root: Path,
    *,
    max_files: int = DEFAULT_MAX_FILES,
    max_directories: int = DEFAULT_MAX_DIRECTORIES,
) -> FileSetComparison:
    """Compare complete source/target file sets without mutating either root."""

    source_files = walk_relative_files(
        source_root,
        max_files=max_files,
        max_directories=max_directories,
    )
    target_files = walk_relative_files(
        target_root,
        max_files=max_files,
        max_directories=max_directories,
    )
    target_set = set(target_files)

    missing: list[Path] = []
    different: list[Path] = []
    type_mismatches: list[Path] = []
    compared = 0
    for relative in source_files:
        target_path = target_root / relative
        if not target_path.exists():
            missing.append(relative)
            continue
        if not target_path.is_file():
            different.append(relative)
            type_mismatches.append(relative)
            continue
        compared += 1
        if not files_equal(
            source_root / relative,
            target_path,
        ):
            different.append(relative)

    extra = [
        relative
        for relative in target_set
        if not (source_root / relative).is_file()
    ]
    return FileSetComparison(
        source_files=source_files,
        target_files=target_files,
        missing=tuple(sorted(missing, key=_path_sort_key)),
        different=tuple(
            sorted(different, key=_path_sort_key)
        ),
        extra=tuple(sorted(extra, key=_path_sort_key)),
        type_mismatches=tuple(
            sorted(type_mismatches, key=_path_sort_key)
        ),
        compared=compared,
    )
