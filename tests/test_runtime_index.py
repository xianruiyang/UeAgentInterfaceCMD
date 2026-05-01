import tempfile
import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.runtime_index import read_index, record_report


class RuntimeIndexTests(unittest.TestCase):
    def test_record_report_creates_index(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            app_root = Path(temp_dir)
            report = app_root / "reports" / "sample.json"
            report.parent.mkdir()
            report.write_text("{}", encoding="utf-8")
            record_report(app_root, report, {"task_id": "t1", "success": True, "cli_version": "x"})
            data = read_index(app_root)
            self.assertEqual(data["entry_count"], 1)
            self.assertEqual(data["entries"][0]["task_id"], "t1")

    def test_read_index_filters_and_stats(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            app_root = Path(temp_dir)
            report = app_root / "reports" / "fail.json"
            report.parent.mkdir()
            report.write_text("{}", encoding="utf-8")
            record_report(
                app_root,
                report,
                {"task_id": "t2", "success": False, "phase": {"failed_command": "bad_cmd", "failed_error": "x"}},
            )
            data = read_index(app_root, failed_only=True, command="bad_cmd", stats=True)
            self.assertEqual(data["filtered_count"], 1)
            self.assertEqual(data["stats"]["failed_command_counts"]["bad_cmd"], 1)


if __name__ == "__main__":
    unittest.main()
