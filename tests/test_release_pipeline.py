import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path
import sys
from unittest.mock import patch

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.release_pipeline import (  # noqa: E402
    build_release_hygiene_check,
    build_release_sync_check,
    mirror_development_to_pak,
    run_formal_release_gate,
    verify_release_pipeline,
    write_release_manifest,
)


def _git(path: Path, *args: str) -> None:
    subprocess.run(["git", *args], cwd=path, check=True, text=True, capture_output=True, timeout=30)


@unittest.skipIf(shutil.which("git") is None, "git is required for release pipeline tests")
class ReleasePipelineTests(unittest.TestCase):
    def _init_repo(self, path: Path, files: dict[str, str]) -> None:
        path.mkdir(parents=True, exist_ok=True)
        _git(path, "init")
        _git(path, "config", "user.email", "uai-tests@example.invalid")
        _git(path, "config", "user.name", "UAI Tests")
        for relative, content in files.items():
            file_path = path / relative
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content, encoding="utf-8")
        _git(path, "add", ".")
        _git(path, "commit", "-m", "initial")

    def _clone_repo(self, source: Path, target: Path) -> None:
        target.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(["git", "clone", str(source), str(target)], check=True, text=True, capture_output=True, timeout=30)

    def _make_project(self) -> Path:
        root = Path(self.temp_dir.name)
        (root / "Test.uproject").write_text("{}", encoding="utf-8")
        self._init_repo(root, {"README.md": "# project\n"})
        dev_plugin = root / "Plugins" / "UeAgentInterface"
        dev_cli = root / "UeAgentInterfaceCMD"
        pak = root / "UeAgentInterfacePak"
        self._init_repo(dev_plugin, {"Source/Test.cpp": "plugin\n", "docs/commands/README.md": "# commands\n"})
        self._init_repo(dev_cli, {"cli/uai_cli/main.py": "print('cli')\n", "docs/USAGE.md": "# usage\n"})
        self._init_repo(pak, {"README.md": "# pak\n"})
        self._clone_repo(dev_plugin, pak / "UeAgentInterface")
        self._clone_repo(dev_cli, pak / "UeAgentInterfaceCMD")
        return root

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_sync_check_accepts_matching_dev_and_pak_trees(self):
        root = self._make_project()
        result = build_release_sync_check(root)
        self.assertTrue(result["success"])
        self.assertEqual([], result["issues"])
        self.assertEqual(
            result["tree_hashes"]["dev_plugin"]["sha256"],
            result["tree_hashes"]["pak_plugin"]["sha256"],
        )
        self.assertEqual(
            result["repos"]["dev_plugin"]["head"],
            result["repos"]["pak_plugin"]["head"],
        )

    def test_sync_check_detects_tree_hash_mismatch(self):
        root = self._make_project()
        (root / "Plugins" / "UeAgentInterface" / "Source" / "Test.cpp").write_text("plugin changed\n", encoding="utf-8")
        result = build_release_sync_check(root)
        self.assertFalse(result["success"])
        self.assertIn("plugin:tree_hash_mismatch", result["issues"])
        self.assertIn("dev_plugin:dirty_worktree", result["warnings"])

    def test_dev_mirror_blocks_submodule_content_write_by_default(self):
        root = self._make_project()
        source_file = root / "Plugins" / "UeAgentInterface" / "Source" / "Test.cpp"
        pak_file = root / "UeAgentInterfacePak" / "UeAgentInterface" / "Source" / "Test.cpp"
        source_file.write_text("plugin changed\n", encoding="utf-8")

        dry_run = mirror_development_to_pak(root, dry_run=True)
        self.assertTrue(dry_run["success"])
        self.assertEqual("plugin\n", pak_file.read_text(encoding="utf-8"))

        result = mirror_development_to_pak(root, dry_run=False)
        self.assertFalse(result["success"])
        self.assertIn("pak_plugin:submodule_content_write_blocked", result["issues"])
        self.assertIn("pak_cli:submodule_content_write_blocked", result["issues"])
        self.assertEqual("plugin\n", pak_file.read_text(encoding="utf-8"))

        result = mirror_development_to_pak(root, dry_run=False, allow_submodule_content_write=True)
        self.assertTrue(result["success"])
        self.assertFalse(result["formal_release_allowed"])
        self.assertEqual("plugin changed\n", pak_file.read_text(encoding="utf-8"))

    def test_release_verify_fails_on_dirty_worktrees_by_default(self):
        root = self._make_project()
        coverage = {
            "command_count": 1,
            "missing_doc": [],
            "missing_implementation": [],
            "missing_smoke": [],
            "raw_generated_doc_count": 0,
        }
        gate = {"success": True, "checks": []}
        with patch("uai_cli.release_pipeline.build_coverage_matrix", return_value=coverage), patch(
            "uai_cli.release_pipeline.run_quality_gate", return_value=gate
        ):
            result = verify_release_pipeline(root / "UeAgentInterfaceCMD", root, run_tests=False)
            self.assertFalse(result["success"])
            self.assertTrue(any(issue.startswith("dirty_worktree:") for issue in result["issues"]))

            allowed = verify_release_pipeline(root / "UeAgentInterfaceCMD", root, run_tests=False, allow_dirty=True)
            self.assertTrue(allowed["success"])

    def test_write_release_manifest_outputs_commits_and_coverage(self):
        root = self._make_project()
        output = root / "UeAgentInterfacePak" / "releases" / "test" / "manifest.json"
        result = write_release_manifest(root / "UeAgentInterfaceCMD", root, release_id="test", output_path=output)
        self.assertTrue(output.exists())
        self.assertEqual("ue_agent_interface.release_manifest.v1", result["schema"])
        self.assertEqual("test", result["release_id"])
        self.assertIn("dev_plugin", result["repos"])
        self.assertIn("coverage", result)

    def test_release_hygiene_detects_forbidden_runtime_logs_in_pak(self):
        root = self._make_project()
        log_file = root / "UeAgentInterfacePak" / "runtimeLogs" / "old.log"
        log_file.parent.mkdir(parents=True)
        log_file.write_text("old\n", encoding="utf-8")

        result = build_release_hygiene_check(root)
        self.assertFalse(result["success"])
        self.assertGreaterEqual(result["issue_count"], 1)
        self.assertTrue(any("runtimeLogs" in issue for issue in result["issues"]))

    def test_release_hygiene_allows_reports_gitkeep(self):
        root = self._make_project()
        gitkeep = root / "UeAgentInterfacePak" / "UeAgentInterfaceCMD" / "reports" / ".gitkeep"
        gitkeep.parent.mkdir(parents=True)
        gitkeep.write_text("", encoding="utf-8")

        result = build_release_hygiene_check(root)
        self.assertTrue(result["success"], result["issues"])

    def test_formal_release_gate_fails_on_hygiene_issue(self):
        root = self._make_project()
        (root / "UeAgentInterfacePak" / "runtimeLogs").mkdir()
        (root / "UeAgentInterfacePak" / "runtimeLogs" / "old.log").write_text("old\n", encoding="utf-8")
        coverage = {
            "command_count": 1,
            "missing_doc": [],
            "missing_implementation": [],
            "missing_smoke": [],
            "raw_generated_doc_count": 0,
            "smoke_coverage": {"actionable_missing_count": 0, "p0_count": 0, "p1_count": 0},
        }
        gate = {"success": True, "checks": []}
        pak = {"success": True, "issues": [], "warnings": []}
        with patch("uai_cli.release_pipeline.build_coverage_matrix", return_value=coverage), patch(
            "uai_cli.release_pipeline.verify_written_coverage_matrix", return_value={"success": True, "reason": "current"}
        ), patch("uai_cli.release_pipeline.run_quality_gate", return_value=gate), patch(
            "uai_cli.release_pipeline.verify_pak_layout", return_value=pak
        ):
            result = run_formal_release_gate(root / "UeAgentInterfaceCMD", root, run_tests=False, allow_dirty=True)

        self.assertFalse(result["success"])
        self.assertIn("release_hygiene_failed", result["issues"])

    def test_formal_release_gate_writes_ci_report(self):
        root = self._make_project()
        coverage = {
            "command_count": 1,
            "missing_doc": [],
            "missing_implementation": [],
            "missing_smoke": [],
            "raw_generated_doc_count": 0,
            "smoke_coverage": {"actionable_missing_count": 0, "p0_count": 0, "p1_count": 0},
        }
        gate = {"success": True, "checks": []}
        pak = {"success": True, "issues": [], "warnings": []}
        output = root / "reports" / "ci.json"
        with patch("uai_cli.release_pipeline.build_coverage_matrix", return_value=coverage), patch(
            "uai_cli.release_pipeline.verify_written_coverage_matrix", return_value={"success": True, "reason": "current"}
        ), patch("uai_cli.release_pipeline.run_quality_gate", return_value=gate), patch(
            "uai_cli.release_pipeline.verify_pak_layout", return_value=pak
        ):
            result = run_formal_release_gate(
                root / "UeAgentInterfaceCMD",
                root,
                run_tests=False,
                allow_dirty=True,
                ci_output=output,
            )

        self.assertTrue(result["success"], result["issues"])
        self.assertTrue(output.exists())
        self.assertEqual(str(output), result["ci_output"])

    def test_formal_release_gate_runs_pak_cli_quality_gate(self):
        root = self._make_project()
        coverage = {
            "command_count": 1,
            "missing_doc": [],
            "missing_implementation": [],
            "missing_smoke": [],
            "raw_generated_doc_count": 0,
            "smoke_coverage": {"actionable_missing_count": 0, "p0_count": 0, "p1_count": 0},
        }
        dev_gate = {"success": True, "checks": [{"name": "dev", "success": True}]}
        pak_gate = {"success": False, "checks": [{"name": "pak_tests", "success": False}]}
        pak = {"success": True, "issues": [], "warnings": []}
        with patch("uai_cli.release_pipeline.build_coverage_matrix", return_value=coverage), patch(
            "uai_cli.release_pipeline.verify_written_coverage_matrix", return_value={"success": True, "reason": "current"}
        ), patch("uai_cli.release_pipeline.run_quality_gate", side_effect=[dev_gate, pak_gate]), patch(
            "uai_cli.release_pipeline.verify_pak_layout", return_value=pak
        ):
            result = run_formal_release_gate(root / "UeAgentInterfaceCMD", root, run_tests=True, allow_dirty=True)

        self.assertFalse(result["success"])
        self.assertIn("pak_quality_gate_failed", result["issues"])
        self.assertEqual(pak_gate, result["pak_quality_gate"])

    def test_formal_release_gate_cleans_test_artifacts_before_final_hygiene(self):
        root = self._make_project()
        coverage = {
            "command_count": 1,
            "missing_doc": [],
            "missing_implementation": [],
            "missing_smoke": [],
            "raw_generated_doc_count": 0,
            "smoke_coverage": {"actionable_missing_count": 0, "p0_count": 0, "p1_count": 0},
        }
        pak = {"success": True, "issues": [], "warnings": []}
        pak_log = root / "UeAgentInterfacePak" / "UeAgentInterfaceCMD" / "logs" / "uai_cli_test.log"

        def fake_quality_gate(app_root: Path, *, run_tests: bool = False):
            if "UeAgentInterfacePak" in app_root.as_posix():
                pak_log.parent.mkdir(parents=True, exist_ok=True)
                pak_log.write_text("generated by tests\n", encoding="utf-8")
            return {"success": True, "checks": []}

        with patch("uai_cli.release_pipeline.build_coverage_matrix", return_value=coverage), patch(
            "uai_cli.release_pipeline.verify_written_coverage_matrix", return_value={"success": True, "reason": "current"}
        ), patch("uai_cli.release_pipeline.run_quality_gate", side_effect=fake_quality_gate), patch(
            "uai_cli.release_pipeline.verify_pak_layout", return_value=pak
        ):
            result = run_formal_release_gate(root / "UeAgentInterfaceCMD", root, run_tests=True, allow_dirty=True)

        self.assertTrue(result["success"], result["issues"])
        self.assertFalse(pak_log.exists())
        self.assertTrue(result["release_hygiene_after_tests"]["success"])
        self.assertTrue(any(item["removed_count"] > 0 for item in result["test_artifact_cleanup"]))


if __name__ == "__main__":
    unittest.main()
