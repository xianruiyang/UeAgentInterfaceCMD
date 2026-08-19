from __future__ import annotations

import json
import socket
from datetime import datetime
from pathlib import Path
from typing import Any


def load_json_file(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        payload = json.load(handle)
    if not isinstance(payload, dict):
        raise ValueError(f"json_object_required:{path}")
    return payload


def save_json_file(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def now_compact() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S_%f")


def get_hostname() -> str:
    return socket.gethostname()
