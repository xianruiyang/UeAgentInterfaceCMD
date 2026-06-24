import json
import tempfile
import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli import main as cli_main


class MainLocalE2ETests(unittest.TestCase):
    def test_manifest_command_writes_report(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            config = Path(temp_dir) / "config.json"
            config.write_text('{"runtime_index_enabled": false}', encoding="utf-8")
            report = Path(temp_dir) / "manifest_report.json"
            exit_code = cli_main.main(
                ["--config", str(config), "manifest", "--summary", "--report-file", str(report), "--json-output"]
            )
            self.assertEqual(exit_code, 0)
            self.assertTrue(report.exists())
            payload = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(payload["task_id"], "manifest")

    def test_dry_run_rejects_unknown_command_before_http(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            config = Path(temp_dir) / "config.json"
            config.write_text('{"runtime_index_enabled": false}', encoding="utf-8")
            plan = Path(temp_dir) / "bad.plan.json"
            plan.write_text(
                json.dumps(
                    {
                        "task_id": "bad_command",
                        "phases": [{"name": "bad", "commands": [{"command": "definitely_missing_command"}]}],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            exit_code = cli_main.main(
                ["--config", str(config), "run", "--plan", str(plan), "--dry-run", "--no-crash-capture"]
            )
            self.assertEqual(exit_code, 2)

    def test_dry_run_rejects_deprecated_command_by_default(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            config = Path(temp_dir) / "config.json"
            config.write_text('{"runtime_index_enabled": false}', encoding="utf-8")
            plan = Path(temp_dir) / "deprecated.plan.json"
            plan.write_text(
                json.dumps(
                    {
                        "task_id": "deprecated_command",
                        "phases": [{"name": "bad", "commands": [{"command": "spawn_actor"}]}],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            exit_code = cli_main.main(
                ["--config", str(config), "run", "--plan", str(plan), "--dry-run", "--no-crash-capture"]
            )
            self.assertEqual(exit_code, 2)

    def test_dry_run_allows_deprecated_command_when_explicit(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            config = Path(temp_dir) / "config.json"
            config.write_text('{"runtime_index_enabled": false}', encoding="utf-8")
            report = Path(temp_dir) / "deprecated_report.json"
            plan = Path(temp_dir) / "deprecated.plan.json"
            plan.write_text(
                json.dumps(
                    {
                        "task_id": "deprecated_command",
                        "phases": [{"name": "allowed", "commands": [{"command": "spawn_actor"}]}],
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            exit_code = cli_main.main(
                [
                    "--config",
                    str(config),
                    "run",
                    "--plan",
                    str(plan),
                    "--dry-run",
                    "--allow-deprecated-command",
                    "--deprecated-use-case",
                    "migration",
                    "--report-file",
                    str(report),
                    "--no-crash-capture",
                ]
            )
            self.assertEqual(exit_code, 0)
            payload = json.loads(report.read_text(encoding="utf-8"))
            lifecycle = payload["command_manifest_validation"]["command_lifecycle_validation"]
            self.assertTrue(lifecycle["success"])


if __name__ == "__main__":
    unittest.main()
