import tempfile
import unittest
from pathlib import Path
import sys
from unittest.mock import patch

CURRENT = Path(__file__).resolve()
TOOLS_DIR = CURRENT.parents[1]
sys.path.insert(0, str(TOOLS_DIR))

from uai_repository.runtime_index import index_path, read_index, record_report


class RuntimeIndexTests(unittest.TestCase):
    def test_frozen_cli_uses_runtime_log_resolver_instead_of_executable_directory(self):
        app_root = Path("C:/installed-skill/tools")
        runtime_root = Path("C:/caller/runtimeLogs")
        with (
            patch.object(sys, "frozen", True, create=True),
            patch("uai_repository.runtime_index.find_development_project_root", return_value=None),
            patch("uai_repository.runtime_index.runtime_logs_dir", return_value=runtime_root) as resolver,
        ):
            self.assertEqual(index_path(app_root), runtime_root / "uai_cli_index.json")
        resolver.assert_called_once_with(app_root)

    def test_record_report_creates_index(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            app_root = Path(temp_dir)
            report = app_root / "reports" / "sample.json"
            report.parent.mkdir()
            report.write_text("{}", encoding="utf-8")
            record_report(app_root, report, {"task_id": "t1", "success": True, "cli_version": "x"})
            self.assertTrue((app_root / "runtimeLogs" / "uai_cli_index.json").exists())
            self.assertFalse((app_root / "runtimeLogs" / "uai_cli_index.hjson").exists())
            data = read_index(app_root)
            self.assertEqual(data["entry_count"], 1)
            self.assertEqual(data["entries"][0]["task_id"], "t1")

    def test_record_report_updates_existing_source_aware_index(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            app_root = Path(temp_dir)
            first = app_root / "reports" / "first.json"
            second = app_root / "reports" / "second.json"
            first.parent.mkdir()
            first.write_text("{}\n", encoding="utf-8")
            second.write_text("{}\n", encoding="utf-8")

            record_report(
                app_root,
                first,
                {"task_id": "first", "success": True, "cli_version": "x"},
            )
            record_report(
                app_root,
                second,
                {"task_id": "second", "success": True, "cli_version": "x"},
            )

            data = read_index(app_root)
            self.assertEqual(data["entry_count"], 2)
            self.assertEqual(
                [entry["task_id"] for entry in data["entries"]],
                ["first", "second"],
            )

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
