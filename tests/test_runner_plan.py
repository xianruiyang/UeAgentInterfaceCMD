import json
import tempfile
import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.runner import load_and_resolve_plan


class RunnerPlanTests(unittest.TestCase):
    def test_load_and_resolve_plan(self):
        plan_payload = {
            "task_id": "t1",
            "defaults": {"limit": 10},
            "phases": [
                {
                    "name": "A",
                    "commands": [
                        {"command": "list_actors", "params": {"limit": "{{limit}}"}},
                    ],
                }
            ],
            "asserts": [],
        }
        vars_payload = {"limit": 99}

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            plan_path = temp_path / "plan.json"
            vars_path = temp_path / "vars.json"
            plan_path.write_text(json.dumps(plan_payload, ensure_ascii=False), encoding="utf-8")
            vars_path.write_text(json.dumps(vars_payload, ensure_ascii=False), encoding="utf-8")

            resolved = load_and_resolve_plan(plan_path, vars_path)
            commands = resolved["phases"][0]["commands"]
            self.assertEqual(commands[0]["params"]["limit"], 99)
            self.assertIn("short_tag", resolved["resolved_variables"])


if __name__ == "__main__":
    unittest.main()
