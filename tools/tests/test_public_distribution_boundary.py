from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
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
PAK_SKILL_ROOT = PAK_SKILL.parent
PAK_AGENT = PAK_SKILL_ROOT / "agents" / "openai.yaml"
PACKAGED_CLI = PAK_SKILL_ROOT / "tools" / "uai-cli.exe"
PACKAGED_CLI_RELEASE = PAK_SKILL_ROOT / "tools" / "uai-cli.release.json"
CONNECTION_TEMPLATE = PAK_SKILL_ROOT / "templates" / "connection.http.toml"
STALE_DEFAULT_CONFIGS = (
    PAK_SKILL_ROOT / "tools" / "uai-cli.default.json",
    PAK_SKILL_ROOT / "templates" / "uai-cli.default.json",
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
        agent = PAK_AGENT.read_text(encoding="utf-8-sig")
        distributed_entry_text = f"{skill}\n{agent}"
        for forbidden in (
            "uai_core",
            "CommandSpec",
            "command search",
            "doctor|run|batch",
            "三态路由",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(
                    forbidden,
                    distributed_entry_text,
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

    def test_packaged_cli_records_public_runtime_provenance(self) -> None:
        for stale_path in STALE_DEFAULT_CONFIGS:
            with self.subTest(stale_path=stale_path):
                self.assertFalse(
                    stale_path.exists(),
                    f"legacy_cli_default_config_distributed:{stale_path}",
                )
        self.assertTrue(CONNECTION_TEMPLATE.is_file(), "connection_template_missing")
        self.assertTrue(PACKAGED_CLI.is_file(), "packaged_cli_missing")
        self.assertTrue(PACKAGED_CLI_RELEASE.is_file(), "packaged_cli_release_missing")

        release = json.loads(PACKAGED_CLI_RELEASE.read_text(encoding="utf-8"))
        self.assertEqual(release.get("schema"), "uai.packaged_cli.release")
        self.assertEqual(release.get("source_repository"), "UeAgentInterfaceCMD")
        self.assertEqual(release.get("artifact"), "uai-cli.exe")
        self.assertRegex(release.get("source_commit", ""), r"^[0-9a-f]{40}$")
        self.assertRegex(release.get("artifact_sha256", ""), r"^[0-9a-f]{64}$")

        version_source = (REPO_ROOT / "cli" / "uai" / "__init__.py").read_text(
            encoding="utf-8"
        )
        version_match = re.search(
            r'^__version__\s*=\s*"([^"]+)"',
            version_source,
            flags=re.MULTILINE,
        )
        self.assertIsNotNone(version_match, "public_sdk_version_missing")
        self.assertEqual(release.get("cli_version"), version_match.group(1))

        digest = hashlib.sha256(PACKAGED_CLI.read_bytes()).hexdigest()
        self.assertEqual(release.get("artifact_sha256"), digest)

    def test_public_discovery_examples_use_current_command_contract(self) -> None:
        for path in (PUBLIC_SDK_DOC, PUBLIC_PLAYBOOK, PAK_README):
            text = path.read_text(encoding="utf-8-sig")
            with self.subTest(path=path):
                for retired in (
                    "reference.catalog_search",
                    "catalog_kind",
                    "match_mode",
                    "materialization_policy",
                ):
                    self.assertNotIn(
                        retired,
                        text,
                        f"public_discovery_uses_retired_catalog:{retired}",
                    )
                self.assertIn(
                    "query.command_search(",
                    text,
                    "public_discovery_named_method_missing",
                )

    def test_skill_sync_uses_repository_tool_not_removed_runtime(self) -> None:
        text = SKILL_SYNC_SCRIPT.read_text(encoding="utf-8-sig")
        self.assertNotIn("cli\"\n        / \"uai_core", text)
        self.assertIn('"tools"\n        / "uai_repository"', text)


if __name__ == "__main__":
    unittest.main()
