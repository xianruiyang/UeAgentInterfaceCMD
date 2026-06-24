from __future__ import annotations

import re
from datetime import datetime
from typing import Literal


_KIND_PREFIX_MAP = {
    "blueprint": "BP",
    "actor_blueprint": "BP",
    "umg": "WBP",
    "widget": "WBP",
    "material": "M",
    "material_instance": "MI",
    "niagara_system": "NS",
    "niagara_emitter": "NE",
    "sequence": "LS",
    "level_sequence": "LS",
}


def _sanitize_token(raw: str) -> str:
    token = re.sub(r"[^0-9a-zA-Z_]+", "_", str(raw).strip())
    token = re.sub(r"_+", "_", token).strip("_")
    return token or "Asset"


TagMode = Literal["none", "time", "date", "datetime"]


def _resolve_tag(now: datetime, tag_mode: TagMode) -> str:
    if tag_mode == "none":
        return ""
    if tag_mode == "time":
        return now.strftime("%H%M")
    if tag_mode == "date":
        return now.strftime("%m%d")
    if tag_mode == "datetime":
        return now.strftime("%m%d%H%M")
    return now.strftime("%m%d")


def build_short_asset_name(
    kind: str,
    base: str,
    max_len: int = 20,
    now: datetime | None = None,
    tag_mode: TagMode = "none",
) -> str:
    if max_len < 12:
        max_len = 12

    prefix = _KIND_PREFIX_MAP.get(str(kind).strip().lower(), "A")
    base_token = _sanitize_token(base)
    tag = _resolve_tag(now or datetime.now(), tag_mode)

    reserved_len = len(prefix) + 1
    if tag:
        reserved_len += len(tag) + 1
    max_base_len = max(3, max_len - reserved_len)
    if len(base_token) > max_base_len:
        base_token = base_token[:max_base_len]

    if tag:
        return f"{prefix}_{base_token}_{tag}"
    return f"{prefix}_{base_token}"
