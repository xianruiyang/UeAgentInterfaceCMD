from __future__ import annotations

from pathlib import Path
from typing import Any

from .example_library import write_example_library
from .http_client import UaiHttpClient
from .runner import execute_batch
from .utils import now_compact


def run_local_e2e(app_root: Path) -> dict[str, Any]:
    examples = write_example_library(app_root / "examples" / "generated")
    return {
        "schema": "ue_agent_interface.e2e.local.v1",
        "generated_at": now_compact(),
        "success": bool(examples.get("success", False)),
        "examples": examples,
    }


def run_ue_readonly_e2e(client: UaiHttpClient) -> dict[str, Any]:
    commands = [
        {"command": "get_world_state", "params": {}},
        {"command": "list_actors", "params": {"limit": 20}},
    ]
    phase = execute_batch(
        client=client,
        phase_name="golden_readonly_e2e",
        commands=commands,
        stop_on_error=True,
    )
    return {
        "schema": "ue_agent_interface.e2e.ue_readonly.v1",
        "generated_at": now_compact(),
        "success": phase.success,
        "phase": {
            "name": phase.name,
            "request_id": phase.request_id,
            "failed_index": phase.failed_index,
            "failed_command": phase.failed_command,
            "failed_error": phase.failed_error,
        },
        "response": phase.response,
    }
