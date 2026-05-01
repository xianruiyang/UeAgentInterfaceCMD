import tempfile
import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.e2e import run_local_e2e
from uai_cli.example_library import write_example_library
from uai_cli.quality_gate import run_quality_gate


class ExampleQualityE2ETests(unittest.TestCase):
    def test_write_example_library(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = write_example_library(Path(temp_dir))
            self.assertTrue(result["success"])
            self.assertTrue((Path(temp_dir) / "golden_readonly.plan.json").exists())

    def test_local_e2e_writes_examples(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            result = run_local_e2e(Path(temp_dir))
            self.assertTrue(result["success"])
            self.assertTrue((Path(temp_dir) / "examples" / "generated" / "README.md").exists())

    def test_quality_gate_returns_checks(self):
        result = run_quality_gate(CURRENT.parents[1], run_tests=False)
        self.assertIn("checks", result)
        self.assertTrue(any(check["name"] == "coverage_matrix" for check in result["checks"]))


if __name__ == "__main__":
    unittest.main()
