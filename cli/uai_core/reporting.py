from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .utils import now_compact, save_json_file


@dataclass(slots=True)
class TimerMetrics:
    t_prepare_ms: float = 0
    t_http_ms: float = 0
    t_parse_ms: float = 0
    t_verify_ms: float = 0
    t_total_ms: float = 0


@dataclass(slots=True)
class PhaseReport:
    name: str
    success: bool
    request_id: str
    stop_on_error: bool
    failed_index: int | None = None
    failed_command: str | None = None
    failed_request_id: str | None = None
    failed_error: str | None = None
    response: dict = field(default_factory=dict)
    metrics: TimerMetrics = field(default_factory=TimerMetrics)


def build_report_file_path(reports_dir: Path, task_id: str) -> Path:
    reports_dir.mkdir(parents=True, exist_ok=True)
    return reports_dir / f"{task_id}_{now_compact()}.json"


def save_report(path: Path, payload: dict[str, Any]) -> None:
    save_json_file(path, payload)

