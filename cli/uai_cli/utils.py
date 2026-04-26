from __future__ import annotations

import ipaddress
import json
import os
import socket
import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


def detect_app_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / "uai-cli.default.json").exists():
            return parent
    return current.parents[3]


def load_json_file(path: Path) -> dict:
    with path.open("r", encoding="utf-8-sig") as file:
        return json.load(file)


def save_json_file(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as file:
        json.dump(payload, file, ensure_ascii=False, indent=2)


def now_compact() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S_%f")


def get_hostname() -> str:
    return socket.gethostname()


def parse_json_text(text: str | None) -> dict:
    if not text:
        return {}
    return json.loads(text)


def is_loopback_url(url: str) -> bool:
    parsed = urlparse(url)
    host = parsed.hostname
    if not host:
        return False
    if host in {"localhost", "127.0.0.1", "::1"}:
        return True
    try:
        return ipaddress.ip_address(host).is_loopback
    except ValueError:
        return False


def mask_token(token: str) -> str:
    if not token:
        return ""
    if len(token) <= 8:
        return "*" * len(token)
    return f"{token[:4]}***{token[-4:]}"


def env_or_default(env_name: str, default: str) -> str:
    return os.getenv(env_name, default)
