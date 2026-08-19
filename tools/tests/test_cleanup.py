import tempfile
import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
TOOLS_DIR = CURRENT.parents[1]
sys.path.insert(0, str(TOOLS_DIR))

from uai_repository.cleanup import cleanup_runtime_json


class CleanupTests(unittest.TestCase):
    def test_cleanup_runtime_json(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            tmp_dir = root / "tmp"
            reports_dir = root / "reports"
            tmp_dir.mkdir(parents=True, exist_ok=True)
            reports_dir.mkdir(parents=True, exist_ok=True)

            for index in range(10):
                (tmp_dir / f"tmp_{index}.json").write_text("{}", encoding="utf-8")
            for index in range(12):
                (reports_dir / f"report_{index}.json").write_text("{}", encoding="utf-8")

            results = cleanup_runtime_json(
                app_root=root,
                reports_dir=reports_dir,
                cleanup_tmp_max=5,
                cleanup_tmp_keep=3,
                cleanup_reports_max=8,
                cleanup_reports_keep=4,
            )
            self.assertEqual(len(results), 2)
            self.assertLessEqual(results[0].after_count, 3)
            self.assertLessEqual(results[1].after_count, 4)

    def test_cleanup_dist_mode_also_trims_source_tmp_when_exists(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            dist_dir = root / "dist"
            dist_tmp_dir = dist_dir / "tmp"
            source_tmp_dir = root / "tmp"
            reports_dir = dist_dir / "reports"
            dist_tmp_dir.mkdir(parents=True, exist_ok=True)
            source_tmp_dir.mkdir(parents=True, exist_ok=True)
            reports_dir.mkdir(parents=True, exist_ok=True)

            for index in range(6):
                (source_tmp_dir / f"src_{index}.json").write_text("{}", encoding="utf-8")
            for index in range(6):
                (dist_tmp_dir / f"dist_{index}.json").write_text("{}", encoding="utf-8")

            results = cleanup_runtime_json(
                app_root=dist_dir,
                reports_dir=reports_dir,
                cleanup_tmp_max=5,
                cleanup_tmp_keep=3,
                cleanup_reports_max=8,
                cleanup_reports_keep=4,
            )
            self.assertEqual(len(results), 3)
            source_result = next(result for result in results if result.target_dir.resolve() == source_tmp_dir.resolve())
            dist_result = next(result for result in results if result.target_dir.resolve() == dist_tmp_dir.resolve())
            self.assertLessEqual(source_result.after_count, 3)
            self.assertLessEqual(dist_result.after_count, 3)


if __name__ == "__main__":
    unittest.main()
