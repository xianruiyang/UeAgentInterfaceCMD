from __future__ import annotations

from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = REPO_ROOT.parent
BUILD_SCRIPT = REPO_ROOT / "tools" / "build.ps1"
BUILD_README = REPO_ROOT / "build" / "README.md"
PAK_SKILL = (
    PROJECT_ROOT
    / "UeAgentInterfacePak"
    / "skills"
    / "ue-agent-interface"
    / "SKILL.md"
)
PUBLIC_PLAYBOOK = (
    PAK_SKILL.parent
    / "references"
    / "public-sdk-playbook.md"
)
PUBLIC_SDK_DOC = REPO_ROOT / "docs" / "PYTHON_SDK_AND_CLI.md"
PAK_README = PROJECT_ROOT / "UeAgentInterfacePak" / "README.md"
SKILL_SYNC_SCRIPT = (
    PROJECT_ROOT / "scripts" / "skills" / "sync_codex_skills.py"
)


class PublicDistributionBoundaryTests(unittest.TestCase):
    def test_packaged_cli_build_uses_only_public_runtime(self) -> None:
        text = BUILD_SCRIPT.read_text(encoding="utf-8-sig")
        for forbidden in (
            "uai_core",
            "command_specs",
            "uai-cli.default.json",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(
                    forbidden,
                    text,
                    f"packaged_cli_build_contains_legacy:{forbidden}",
                )
        self.assertIn('--paths "$Root\\cli"', text)
        self.assertIn('"$Root\\build_entry.py"', text)
        readme = BUILD_README.read_text(encoding="utf-8-sig")
        self.assertNotIn("uai-cli.default.json", readme)

    def test_distributed_skill_routes_only_to_public_sdk(self) -> None:
        skill = PAK_SKILL.read_text(encoding="utf-8-sig")
        for forbidden in (
            "uai_core",
            "CommandSpec",
            "command search",
            "doctor|run|batch",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(
                    forbidden,
                    skill,
                    f"distributed_skill_contains_legacy:{forbidden}",
                )
        for required in (
            "import uai",
            "uai.connect",
            "uai.command.v1",
            "public-sdk-playbook.md",
        ):
            with self.subTest(required=required):
                self.assertIn(
                    required,
                    skill,
                    f"distributed_skill_public_boundary_missing:{required}",
                )
        self.assertTrue(
            PUBLIC_PLAYBOOK.is_file(),
            "public_sdk_playbook_missing",
        )

    def test_public_catalog_examples_use_server_supported_values(self) -> None:
        for path in (PUBLIC_SDK_DOC, PUBLIC_PLAYBOOK, PAK_README):
            text = path.read_text(encoding="utf-8-sig")
            with self.subTest(path=path):
                self.assertNotIn(
                    'match_mode="contains"',
                    text,
                    "catalog_example_uses_unsupported_match_mode",
                )
                self.assertNotIn(
                    'materialization_policy="none"',
                    text,
                    "catalog_example_uses_unsupported_materialization_policy",
                )
                self.assertNotIn(
                    'catalog_kind="asset"',
                    text,
                    "catalog_example_uses_unregistered_catalog_source",
                )
                self.assertNotIn(
                    '"catalog_kind": "asset"',
                    text,
                    "dynamic_catalog_example_uses_unregistered_catalog_source",
                )
                self.assertIn('catalog_kind="uai_reference"', text)
                self.assertIn('match_mode="broad"', text)
                self.assertIn(
                    'materialization_policy="index_only"',
                    text,
                )

    def test_skill_sync_uses_repository_tool_not_removed_runtime(self) -> None:
        text = SKILL_SYNC_SCRIPT.read_text(encoding="utf-8-sig")
        self.assertNotIn("cli\"\n        / \"uai_core", text)
        self.assertIn('"tools"\n        / "uai_repository"', text)


if __name__ == "__main__":
    unittest.main()
