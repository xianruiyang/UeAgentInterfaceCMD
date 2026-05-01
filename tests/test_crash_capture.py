import tempfile
import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.crash_capture import (
    build_crash_signature,
    collect_failure_artifacts,
    generate_batch_bisect_files,
    inspect_crash_dir,
    pack_crash_dir,
    replay_crash_dir,
)


class CrashCaptureTests(unittest.TestCase):
    def test_collect_inspect_and_pack(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            app_root = Path(temp_dir)
            report = app_root / "reports" / "fail.json"
            report.parent.mkdir()
            report.write_text("{}", encoding="utf-8")
            result = collect_failure_artifacts(
                app_root=app_root,
                subcommand="batch",
                exit_code=2,
                report_path=report,
                report_payload={"task_id": "t1", "success": False, "phase": {"failed_command": "x"}},
            )
            crash_dir = Path(result["crash_dir"])
            self.assertTrue((crash_dir / "manifest.json").exists())
            inspected = inspect_crash_dir(crash_dir)
            self.assertEqual(inspected["manifest"]["classification"], "CommandFailed")
            packed = pack_crash_dir(crash_dir)
            self.assertTrue(packed.exists())

    def test_signature_replay_and_bisect(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            app_root = Path(temp_dir)
            request = app_root / "request.json"
            request.write_text(
                '{"stop_on_error": true, "commands": [{"command": "a"}, {"command": "b"}]}',
                encoding="utf-8",
            )
            result = collect_failure_artifacts(
                app_root=app_root,
                subcommand="batch",
                exit_code=2,
                report_payload={"task_id": "t2", "success": False, "phase": {"failed_command": "a"}},
                request_files=[request],
                replay_commands=[[str(app_root / "run_uai_cli.py"), "batch", "--file", str(request), "--json-output"]],
            )
            crash_dir = Path(result["crash_dir"])
            self.assertTrue(build_crash_signature(crash_dir)["success"])
            replay = replay_crash_dir(crash_dir, app_root=app_root, dry_run=True)
            self.assertTrue(replay["success"])
            self.assertEqual(len(replay["commands"]), 1)
            bisect = generate_batch_bisect_files(crash_dir)
            self.assertEqual(len(bisect["generated_files"]), 2)

    def test_replay_reports_missing_replay_commands(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            app_root = Path(temp_dir)
            result = collect_failure_artifacts(
                app_root=app_root,
                subcommand="doctor",
                exit_code=3,
                report_payload={"task_id": "doctor", "success": False},
            )
            replay = replay_crash_dir(Path(result["crash_dir"]), app_root=app_root, dry_run=True)
            self.assertFalse(replay["success"])
            self.assertEqual(replay["error"], "no_replay_commands")


if __name__ == "__main__":
    unittest.main()
