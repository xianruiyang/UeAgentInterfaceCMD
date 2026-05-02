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
    build_release_sync_check,
    mirror_development_to_pak,
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

    def test_dev_mirror_copies_dirty_development_changes_to_pak(self):
        root = self._make_project()
        source_file = root / "Plugins" / "UeAgentInterface" / "Source" / "Test.cpp"
        pak_file = root / "UeAgentInterfacePak" / "UeAgentInterface" / "Source" / "Test.cpp"
        source_file.write_text("plugin changed\n", encoding="utf-8")

        dry_run = mirror_development_to_pak(root, dry_run=True)
        self.assertTrue(dry_run["success"])
        self.assertEqual("plugin\n", pak_file.read_text(encoding="utf-8"))

        result = mirror_development_to_pak(root, dry_run=False)
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


if __name__ == "__main__":
    unittest.main()
