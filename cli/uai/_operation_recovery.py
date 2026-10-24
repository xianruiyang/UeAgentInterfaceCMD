"""Atomic SDK-owned operation custody. No request replay or native cleanup."""

from __future__ import annotations

from contextlib import contextmanager
from copy import deepcopy
import json
import os
from pathlib import Path
import re
import tempfile

from .errors import UsageError
from .local_paths import find_project_root


def recovery_path(client, name: str) -> Path:
    if not isinstance(name, str) or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]*", name):
        raise UsageError(code="operation_recovery_name_invalid",
                         message="use a short operation name containing letters, digits, '_' or '-'")
    root = find_project_root(client._connection.source_path)
    return root / "Saved" / "UeAgentInterface" / "OperationRecovery" / (name + ".json")


@contextmanager
def _lock(directory):
    directory.mkdir(parents=True, exist_ok=True)
    # OS locks are released on process death; a stale file cannot block recovery.
    with (directory / ".custody.lock").open("a+b") as stream:
        if stream.tell() == 0:
            stream.write(b"\0")
            stream.flush()
        stream.seek(0)
        if os.name == "nt":
            import msvcrt
            msvcrt.locking(stream.fileno(), msvcrt.LK_LOCK, 1)
        else:
            import fcntl
            fcntl.flock(stream.fileno(), fcntl.LOCK_EX)
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == "nt":
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def load(client, name):
    path = recovery_path(client, name)
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict) or value.get("schema") not in {
            "uai.operation.custody/1", "uai.operation.custody/2"
        }:
            raise ValueError("invalid custody")
        return value
    except (OSError, ValueError, TypeError):
        raise UsageError(code="operation_recovery_unavailable",
                         message=f"no readable SDK custody was found for {name!r}") from None


def store(client, name, record, *, reserve=False, expected_ref=None, replace=False):
    path = recovery_path(client, name)
    temporary = None
    try:
        with _lock(path.parent):
            if path.exists():
                previous = json.loads(path.read_text(encoding="utf-8"))
                if reserve:
                    raise UsageError(code="operation_recovery_name_in_use",
                                     message=f"{name!r} already holds a request; recover it or use another name")
                old_ref = previous.get("state", {}).get("operation_ref")
                if not replace and old_ref is not None and old_ref != expected_ref:
                    raise UsageError(code="operation_custody_changed",
                                     message=f"custody for {name!r} changed; the newer recovery record was preserved")
            with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                             prefix=".checkpoint-", delete=False) as stream:
                temporary = Path(stream.name)
                json.dump(record, stream, ensure_ascii=False)
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, path)
            temporary = None
    except (OSError, ValueError, TypeError):
        raise UsageError(code="operation_checkpoint_failed",
                         message=f"could not save operation custody for {name!r}",
                         diagnostic={"recovery_name": name}) from None
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def request_record(command_id, request_id, subject_ref=None):
    return {
        "schema": "uai.operation.custody/2",
        "request": {"command_id": command_id, "request_id": request_id},
        "subject_ref": subject_ref if isinstance(subject_ref, str) else "",
        "state": {}, "phase": "submitted", "released": False,
    }


def with_observation(record, payload):
    updated = deepcopy(record)
    for field in ("phase", "lifecycle_status", "terminal", "cleanup_complete"):
        if field in payload:
            updated[field] = payload[field]
    return updated


def summary(name, record):
    return {
        "name": name,
        "command_id": record.get("request", {}).get("command_id", ""),
        "subject_ref": record.get("subject_ref", ""),
        "phase": "released" if record.get("released") else record.get("phase", "unknown"),
        "terminal": record.get("terminal", False),
        "cleanup_complete": record.get("cleanup_complete", False),
    }
