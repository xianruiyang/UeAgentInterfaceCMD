"""Model-facing display: indented fields, inline scalar lists and TSV records.

This is a display format, not a replacement for the SDK or JSON interchange.
Selection depends only on JSON shape, never on a command or asset type.
"""
from __future__ import annotations

from collections.abc import Mapping
import json
import re
from typing import Any


_KEY = re.compile(r"[A-Za-z_][A-Za-z0-9_.]*\Z")
_NUMERIC_TEXT = re.compile(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?\Z")
_LITERALS = {"true", "false", "null", "NaN", "Infinity", "-Infinity"}


def json_output(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def _quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False).replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")


def _key(value: str) -> str:
    return value if _KEY.fullmatch(value) else _quoted(value)


def _scalar(value: Any) -> str:
    if not isinstance(value, str):
        return json_output(value)
    if (
        not value or value != value.strip() or value in _LITERALS
        or _NUMERIC_TEXT.fullmatch(value) or value.startswith(("-", "#"))
        or any(c in value for c in '\\"[]{}:\t\r\n\u2028\u2029')
        or any(ord(c) < 32 or ord(c) == 127 for c in value)
    ):
        return _quoted(value)
    return value


def _container(value: Any) -> bool:
    return isinstance(value, (Mapping, list, tuple))


def compact_output(value: Any) -> str:
    """Retain every field, value, type and array order without repeated table keys."""
    lines: list[str] = []

    def emit(current: Any, label: str, depth: int) -> None:
        pad = "  " * depth
        if isinstance(current, Mapping):
            if not current:
                lines.append(pad + (label + ": " if label else "") + "{}")
                return
            if label:
                lines.append(pad + label + ":")
                depth += 1
            for name, child in current.items():
                emit(child, _key(name), depth)
            return
        if isinstance(current, (list, tuple)):
            if not current:
                lines.append(pad + (label + ": " if label else "") + "[]")
                return
            header = pad + label + f"[{len(current)}]"
            if all(not _container(child) for child in current):
                lines.append(header + ": " + "\t".join(_scalar(child) for child in current))
                return
            first = current[0]
            if isinstance(first, Mapping) and first and all(
                isinstance(row, Mapping) and row.keys() == first.keys()
                and all(not _container(cell) for cell in row.values())
                for row in current
            ):
                columns = list(first)
                lines.append(header + "{" + "\t".join(_key(name) for name in columns) + "}:")
                lines.extend("  " * (depth + 1) + "\t".join(_scalar(row[name]) for name in columns) for row in current)
                return
            lines.append(header + ":")
            for child in current:
                child_pad = "  " * (depth + 1)
                if _container(child) and child:
                    lines.append(child_pad + "-")
                    emit(child, "", depth + 2)
                else:
                    lines.append(child_pad + "- " + _scalar(child))
            return
        lines.append(pad + (label + ": " if label else "") + _scalar(current))

    emit(value, "", 0)
    return "\n".join(lines)


def render_output(value: Any, output_format: str) -> str:
    return json_output(value) if output_format == "json" else compact_output(value)
