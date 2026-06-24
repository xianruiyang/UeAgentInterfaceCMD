import tempfile
import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.command_manifest import build_command_manifest, validate_command_lifecycle, validate_command_names


class CommandManifestTests(unittest.TestCase):
    def test_build_manifest_from_docs_and_dispatch(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "Test.uproject").write_text("{}", encoding="utf-8")
            plugin = root / "Plugins" / "UeAgentInterface"
            docs = plugin / "docs" / "commands"
            source = plugin / "Source" / "UeAgentInterface" / "Private" / "Commands" / "Test"
            smoke_source = plugin / "Source" / "UeAgentInterfaceTests" / "Private" / "Smoke"
            docs.mkdir(parents=True)
            source.mkdir(parents=True)
            smoke_source.mkdir(parents=True)
            (docs / "01_Test.md").write_text(
                "# Test\n\n"
                "| 指令 | 用途 | 关键参数 | 关键返回 |\n"
                "| --- | --- | --- | --- |\n"
                "| `foo_command` | do foo | `asset_path` | `ok` |\n",
                encoding="utf-8",
            )
            deprecated_docs = docs / "deprecatedCommand"
            deprecated_docs.mkdir(parents=True)
            (deprecated_docs / "01_Test.md").write_text(
                "# Deprecated Test\n\n"
                "| 指令 | 废弃说明 | 新流程 |\n"
                "| --- | --- | --- |\n"
                "| `foo_old_command` | **Deprecated for authoring** | `foo_command` |\n",
                encoding="utf-8",
            )
            (source / "UeAgentHttpServer_Test.cpp").write_text(
                'if (CommandLower == TEXT("foo_command")) return CmdFoo(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_old_command")) return CmdFoo(Ctx, OutData, OutError);\n',
                encoding="utf-8",
            )
            (smoke_source / "UeAgentInterfaceSmoke_Test.cpp").write_text(
                'TestTrue(TEXT("foo"), ExecSmokeCommand(this, ServerScope, TEXT("foo-label"), TEXT("foo_command"), TEXT("{}"), Data));\n',
                encoding="utf-8",
            )

            manifest = build_command_manifest(root)
            command = manifest["commands"]["foo_command"]
            self.assertEqual(command["params"], ["asset_path"])
            self.assertTrue(command["implemented"])
            self.assertTrue(command["smoke_tested"])
            self.assertEqual(
                command["implementation_files"],
                ["Source/UeAgentInterface/Private/Commands/Test/UeAgentHttpServer_Test.cpp"],
            )
            self.assertEqual(
                command["smoke_files"],
                ["Source/UeAgentInterfaceTests/Private/Smoke/UeAgentInterfaceSmoke_Test.cpp"],
            )
            deprecated = manifest["commands"]["foo_old_command"]
            self.assertTrue(deprecated["deprecated"])
            self.assertEqual(deprecated["lifecycle"], "deprecated")
            self.assertEqual(deprecated["deprecated_scope"], "authoring")
            self.assertEqual(deprecated["replacement"], ["foo_command"])
            self.assertIn("migration", deprecated["allowed_use_cases"])

    def test_heading_parser_ignores_descriptive_tokens_after_command_prefix(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "Test.uproject").write_text("{}", encoding="utf-8")
            plugin = root / "Plugins" / "UeAgentInterface"
            docs = plugin / "docs" / "commands"
            source = plugin / "Source" / "UeAgentInterface" / "Private" / "Commands" / "Test"
            docs.mkdir(parents=True)
            source.mkdir(parents=True)
            (docs / "01_Test.md").write_text(
                "# Test\n\n"
                "### `level_create_blank` / `level_open`\n\n"
                "### `sequence_apply_folder` 的 `control_rig` 轨道\n\n",
                encoding="utf-8",
            )
            (source / "UeAgentHttpServer_Test.cpp").write_text(
                'if (CommandLower == TEXT("level_create_blank")) return CmdCreate(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("level_open")) return CmdOpen(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("sequence_apply_folder")) return CmdSequence(Ctx, OutData, OutError);\n',
                encoding="utf-8",
            )

            manifest = build_command_manifest(root)

            self.assertIn("level_create_blank", manifest["commands"])
            self.assertIn("level_open", manifest["commands"])
            self.assertIn("sequence_apply_folder", manifest["commands"])
            self.assertNotIn("control_rig", manifest["commands"])

    def test_smoke_coverage_ledger_marks_command_as_smoke_tested(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "Test.uproject").write_text("{}", encoding="utf-8")
            plugin = root / "Plugins" / "UeAgentInterface"
            docs = plugin / "docs" / "commands"
            source = plugin / "Source" / "UeAgentInterface" / "Private" / "Commands" / "Test"
            docs.mkdir(parents=True)
            source.mkdir(parents=True)
            (docs / "01_Test.md").write_text(
                "# Test\n\n"
                "| 指令 | 用途 | 关键参数 | 关键返回 |\n"
                "| --- | --- | --- | --- |\n"
                "| `foo_indirect` | do foo | `asset_path` | `ok` |\n",
                encoding="utf-8",
            )
            (plugin / "docs" / "smoke_coverage_ledger.json").write_text(
                "{\n"
                "  \"schema\": \"ue_agent_interface.smoke_coverage_ledger.v1\",\n"
                "  \"entries\": [\n"
                "    {\"command\": \"foo_indirect\", \"coverage\": \"workflow_smoke\", \"evidence\": \"runtimeLogs/foo.json\"}\n"
                "  ]\n"
                "}\n",
                encoding="utf-8",
            )
            (source / "UeAgentHttpServer_Test.cpp").write_text(
                'if (CommandLower == TEXT("foo_indirect")) return CmdFoo(Ctx, OutData, OutError);\n',
                encoding="utf-8",
            )

            manifest = build_command_manifest(root)
            command = manifest["commands"]["foo_indirect"]

            self.assertTrue(command["implemented"])
            self.assertTrue(command["smoke_tested"])
            self.assertEqual(command["smoke_files"], ["docs/smoke_coverage_ledger.json"])

    def test_validate_unknown_command(self):
        manifest = {"commands": {"known_command": {}}}
        unknown, warnings = validate_command_names(["known_command", "missing_command"], manifest)
        self.assertEqual(unknown, ["missing_command"])
        self.assertEqual(warnings, [])

    def test_validate_lifecycle_blocks_deprecated_by_default(self):
        manifest = {
            "commands": {
                "known_command": {"deprecated": False},
                "old_command": {
                    "deprecated": True,
                    "lifecycle": "deprecated",
                    "allowed_use_cases": ["migration"],
                    "replacement": ["known_command"],
                },
            }
        }

        result = validate_command_lifecycle(["known_command", "old_command"], manifest)

        self.assertFalse(result["success"])
        self.assertEqual(result["issues"], ["deprecated_command_blocked:old_command"])
        self.assertEqual(result["deprecated_commands"][0]["replacement"], ["known_command"])

    def test_validate_lifecycle_allows_explicit_use_case(self):
        manifest = {
            "commands": {
                "old_command": {
                    "deprecated": True,
                    "lifecycle": "deprecated",
                    "allowed_use_cases": ["migration"],
                },
            }
        }

        result = validate_command_lifecycle(
            ["old_command"],
            manifest,
            allow_deprecated=True,
            deprecated_use_case="migration",
        )

        self.assertTrue(result["success"])
        self.assertEqual(result["warnings"], ["deprecated_command_allowed:old_command:migration"])


if __name__ == "__main__":
    unittest.main()
