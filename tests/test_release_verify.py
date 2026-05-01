import tempfile
import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.release_verify import build_coverage_matrix, verify_pak_layout, write_coverage_matrix


class ReleaseVerifyTests(unittest.TestCase):
    def test_coverage_matrix_classifies_smoke_debt(self):
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
                "| `foo_apply_folder` | workflow | `folder_path` | `ok` |\n"
                "| `foo_screenshot` | visual | `asset_path` | `file` |\n"
                "| `asset_import_fbx_animation` | fixture | `source_file` | `asset_path` |\n"
                "| `foo_get_info` | readonly | `asset_path` | `info` |\n"
                "| `foo_smoked` | covered | `asset_path` | `ok` |\n",
                encoding="utf-8",
            )
            (source / "UeAgentHttpServer_Test.cpp").write_text(
                'if (CommandLower == TEXT("foo_apply_folder")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_screenshot")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("asset_import_fbx_animation")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_get_info")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_smoked")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_add_node")) return Cmd(Ctx, OutData, OutError);\n',
                encoding="utf-8",
            )
            (smoke_source / "UeAgentInterfaceSmoke_Test.cpp").write_text(
                'TestTrue(TEXT("foo"), ExecSmokeCommand(this, ServerScope, TEXT("foo-label"), TEXT("foo_smoked"), TEXT("{}"), Data));\n',
                encoding="utf-8",
            )

            matrix = build_coverage_matrix(root)
            rows = {row["command"]: row for row in matrix["rows"]}
            self.assertEqual(matrix["schema"], "ue_agent_interface.coverage_matrix.v2")
            self.assertEqual(rows["foo_smoked"]["smoke_coverage_status"], "direct")
            self.assertEqual(rows["foo_apply_folder"]["smoke_coverage_status"], "needs_direct_smoke")
            self.assertEqual(rows["foo_apply_folder"]["smoke_coverage_priority"], "P0")
            self.assertEqual(rows["foo_screenshot"]["smoke_coverage_status"], "needs_ui_smoke")
            self.assertEqual(rows["asset_import_fbx_animation"]["smoke_coverage_status"], "needs_fixture_smoke")
            self.assertEqual(rows["foo_get_info"]["smoke_coverage_status"], "needs_readonly_smoke")
            self.assertEqual(rows["foo_add_node"]["smoke_coverage_status"], "indirect_workflow_candidate")
            self.assertIn("foo_apply_folder", matrix["smoke_coverage"]["p0_commands"])

    def test_write_coverage_matrix_writes_smoke_debt_report(self):
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
                "| `foo_apply_folder` | workflow | `folder_path` | `ok` |\n",
                encoding="utf-8",
            )
            (source / "UeAgentHttpServer_Test.cpp").write_text(
                'if (CommandLower == TEXT("foo_apply_folder")) return Cmd(Ctx, OutData, OutError);\n',
                encoding="utf-8",
            )

            output_json = root / "out" / "command_coverage_matrix.json"
            output_md = root / "out" / "command_coverage_matrix.md"
            matrix = write_coverage_matrix(output_json, output_md, root)
            self.assertTrue(output_json.exists())
            self.assertTrue(output_md.exists())
            debt_file = Path(matrix["smoke_debt_file"])
            self.assertTrue(debt_file.exists())
            debt_text = debt_file.read_text(encoding="utf-8")
            self.assertIn("foo_apply_folder", debt_text)

    def test_verify_pak_layout_minimal(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "Test.uproject").write_text("{}", encoding="utf-8")
            pak = root / "UeAgentInterfacePak"
            (pak / "UeAgentInterface").mkdir(parents=True)
            (pak / "UeAgentInterfaceCMD").mkdir()
            (pak / "README.md").write_text("# pak\n", encoding="utf-8")
            skill_ref = pak / "skills" / "ue-agent-interface" / "references"
            skill_ref.mkdir(parents=True)
            (skill_ref.parent / "SKILL.md").write_text("# skill\n", encoding="utf-8")
            (skill_ref / "command-map.md").write_text("# commands\n", encoding="utf-8")
            result = verify_pak_layout(root)
            self.assertTrue(result["success"])


if __name__ == "__main__":
    unittest.main()
