import unittest
from types import SimpleNamespace
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli import main as cli_main


class MainParserTests(unittest.TestCase):
    def _parse(self, argv: list[str]):
        parser = cli_main._build_common_parser()
        cli_main._add_subcommands(parser)
        return parser.parse_args(argv)

    def test_token_before_subcommand_kept(self):
        args = self._parse(["--token", "abc123", "doctor"])
        self.assertEqual(args.token, "abc123")

    def test_token_after_subcommand_kept(self):
        args = self._parse(["doctor", "--token", "abc123"])
        self.assertEqual(args.token, "abc123")

    def test_namegen_tag_mode_parse(self):
        args = self._parse(["namegen", "--kind", "blueprint", "--base", "Door", "--tag-mode", "none"])
        self.assertEqual(args.tag_mode, "none")

    def test_namegen_defaults_short_and_simple(self):
        args = self._parse(["namegen", "--kind", "blueprint", "--base", "Door"])
        self.assertEqual(args.tag_mode, "none")
        self.assertEqual(args.max_len, 20)

    def test_manifest_parse(self):
        args = self._parse(["manifest", "--summary"])
        self.assertEqual(args.subcommand, "manifest")
        self.assertTrue(args.summary)

    def test_release_parse(self):
        args = self._parse(["release", "all"])
        self.assertEqual(args.action, "all")

    def test_release_gate_parse(self):
        args = self._parse(["release", "gate", "--run-tests"])
        self.assertEqual(args.action, "gate")
        self.assertTrue(args.run_tests)

    def test_release_pipeline_actions_parse(self):
        args = self._parse(
            [
                "release",
                "dev-mirror",
                "--dry-run",
                "--delete-extra",
                "--release-id",
                "2026.05.02",
                "--manifest-output",
                "manifest.json",
            ]
        )
        self.assertEqual(args.action, "dev-mirror")
        self.assertTrue(args.dry_run)
        self.assertTrue(args.delete_extra)
        self.assertEqual(args.release_id, "2026.05.02")
        self.assertEqual(args.manifest_output, "manifest.json")

    def test_release_verify_parse(self):
        args = self._parse(["release", "verify", "--run-tests", "--allow-dirty"])
        self.assertEqual(args.action, "verify")
        self.assertTrue(args.run_tests)
        self.assertTrue(args.allow_dirty)

    def test_crash_parse(self):
        args = self._parse(["crash", "replay", "--execute"])
        self.assertEqual(args.action, "replay")
        self.assertTrue(args.execute)

    def test_e2e_parse(self):
        args = self._parse(["e2e", "local"])
        self.assertEqual(args.mode, "local")

    def test_resolve_config_namegen_without_token(self):
        args = SimpleNamespace(
            subcommand="namegen",
            dry_run=False,
            config=None,
            base_url=None,
            token=None,
            timeout=None,
            allow_nonloopback=False,
            no_niagara_guard=False,
            allow_unsafe_niagara_mix=False,
            skip_compat_check=False,
            no_crash_capture=False,
        )
        config = cli_main._resolve_config(args)
        self.assertEqual(config.base_url, "http://127.0.0.1:17777")


if __name__ == "__main__":
    unittest.main()
