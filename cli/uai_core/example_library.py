from __future__ import annotations

from pathlib import Path
from typing import Any

from .utils import save_json_file


SAFE_EXAMPLE_BATCHES: dict[str, dict[str, Any]] = {
    "core_readonly.batch.json": {
        "stop_on_error": True,
        "commands": [
            {"command": "get_world_state", "params": {}},
            {"command": "list_actors", "params": {"limit": 20}},
        ],
    },
    "navigation_readonly.batch.json": {
        "stop_on_error": True,
        "commands": [
            {"command": "navigation_get_info", "params": {"include_nav_data": True, "include_bounds": True}},
        ],
    },
    "texture_readonly.batch.json": {
        "stop_on_error": True,
        "commands": [
            {"command": "texture_usage_find_references", "params": {"asset_path": "/Game/Example/T_Texture"}},
        ],
    },
}


def write_example_library(output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    files: list[str] = []
    for name, payload in SAFE_EXAMPLE_BATCHES.items():
        path = output_dir / name
        save_json_file(path, payload)
        files.append(str(path))

    plan = {
        "task_id": "golden_readonly_e2e",
        "phases": [
            {
                "name": "readonly_world_probe",
                "stop_on_error": True,
                "commands": SAFE_EXAMPLE_BATCHES["core_readonly.batch.json"]["commands"],
            }
        ],
        "asserts": [],
    }
    plan_path = output_dir / "golden_readonly.plan.json"
    save_json_file(plan_path, plan)
    files.append(str(plan_path))

    vars_path = output_dir / "golden_readonly.vars.json"
    save_json_file(vars_path, {})
    files.append(str(vars_path))

    readme = output_dir / "README.md"
    readme.write_text(
        "# UAI Generated Example Library\n\n"
        "这些示例只覆盖外层 CLI 的标准调用形态。需要 UE 服务的示例默认是只读命令，适合 golden E2E smoke。\n\n"
        "- `core_readonly.batch.json`: 世界状态和 actor 列表只读探针。\n"
        "- `navigation_readonly.batch.json`: Navigation 只读摘要。\n"
        "- `golden_readonly.plan.json`: 可用于 `uai-cli run --plan ...` 的 golden E2E 计划。\n",
        encoding="utf-8",
    )
    files.append(str(readme))
    return {"success": True, "output_dir": str(output_dir), "files": files}
