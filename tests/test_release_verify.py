import json
import tempfile
import unittest
from pathlib import Path
import sys
from unittest.mock import patch

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.quality_gate import run_quality_gate
from uai_cli.project_paths import find_development_project_root
from uai_cli.release_verify import (
    build_coverage_matrix,
    default_coverage_output_dir,
    verify_pak_layout,
    verify_written_coverage_matrix,
    write_coverage_matrix,
)


class ReleaseVerifyTests(unittest.TestCase):
    def current_project_root(self) -> Path:
        project_root = find_development_project_root(CURRENT.parents[1])
        self.assertIsNotNone(project_root)
        return project_root

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
                "| `foo_smoked` | covered | `asset_path` | `ok` |\n"
                "| `undo` | lifecycle | | `ok` |\n",
                encoding="utf-8",
            )
            (source / "UeAgentHttpServer_Test.cpp").write_text(
                'if (CommandLower == TEXT("foo_apply_folder")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_screenshot")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("asset_import_fbx_animation")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_get_info")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_smoked")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_add_node")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("undo")) return Cmd(Ctx, OutData, OutError);\n',
                encoding="utf-8",
            )
            (smoke_source / "UeAgentInterfaceSmoke_Test.cpp").write_text(
                'TestTrue(TEXT("foo"), ExecSmokeCommand(this, ServerScope, TEXT("foo-label"), TEXT("foo_smoked"), TEXT("{}"), Data));\n'
                'TestTrue(TEXT("undo"), ExecSmokeCommand(this, ServerScope, TEXT("undo-label"), TEXT("undo"), TEXT("{}"), Data));\n',
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
            self.assertEqual(rows["undo"]["smoke_coverage_status"], "direct")
            self.assertEqual(rows["undo"]["doc_status"], "explicit")
            self.assertIn("foo_apply_folder", matrix["smoke_coverage"]["p0_commands"])

    def test_deprecated_commands_are_documented_only_in_deprecated_docs(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "Test.uproject").write_text("{}", encoding="utf-8")
            plugin = root / "Plugins" / "UeAgentInterface"
            docs = plugin / "docs" / "commands"
            deprecated_docs = docs / "deprecatedCommand"
            source = plugin / "Source" / "UeAgentInterface" / "Private" / "Commands" / "Test"
            deprecated_docs.mkdir(parents=True)
            source.mkdir(parents=True)
            (docs / "01_Test.md").write_text(
                "# Test\n\n"
                "| 指令 | 用途 | 关键参数 | 关键返回 |\n"
                "| --- | --- | --- | --- |\n"
                "| `foo_apply_folder` | workflow | `folder_path` | `ok` |\n",
                encoding="utf-8",
            )
            (deprecated_docs / "01_Test.md").write_text(
                "# Deprecated Test\n\n"
                "| 指令 | 废弃说明 | 新流程 |\n"
                "| --- | --- | --- |\n"
                "| `foo_old_write` | **Deprecated for authoring** | `foo_apply_folder` |\n",
                encoding="utf-8",
            )
            (source / "UeAgentHttpServer_Test.cpp").write_text(
                'if (CommandLower == TEXT("foo_apply_folder")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_old_write")) return Cmd(Ctx, OutData, OutError);\n',
                encoding="utf-8",
            )

            matrix = build_coverage_matrix(root)
            rows = {row["command"]: row for row in matrix["rows"]}
            self.assertEqual("explicit", rows["foo_apply_folder"]["doc_status"])
            self.assertEqual("deprecated", rows["foo_old_write"]["doc_status"])
            self.assertTrue(rows["foo_old_write"]["deprecated"])
            self.assertEqual("docs/commands/deprecatedCommand/01_Test.md", rows["foo_old_write"]["doc_file"])
            self.assertNotIn("foo_old_write", matrix["missing_doc"])
            self.assertEqual(1, matrix["deprecated_doc_count"])

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

    def test_written_coverage_matrix_detects_stale_generated_file(self):
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
                "| `foo_existing` | existing | `asset_path` | `ok` |\n"
                "| `foo_new_event_query` | event query | `asset_path` | `events` |\n",
                encoding="utf-8",
            )
            (source / "UeAgentHttpServer_Test.cpp").write_text(
                'if (CommandLower == TEXT("foo_existing")) return Cmd(Ctx, OutData, OutError);\n'
                'if (CommandLower == TEXT("foo_new_event_query")) return Cmd(Ctx, OutData, OutError);\n',
                encoding="utf-8",
            )
            (smoke_source / "UeAgentInterfaceSmoke_Test.cpp").write_text(
                'TestTrue(TEXT("existing"), ExecSmokeCommand(this, ServerScope, TEXT("existing"), TEXT("foo_existing"), TEXT("{}"), Data));\n'
                'TestTrue(TEXT("event"), ExecSmokeCommand(this, ServerScope, TEXT("event"), TEXT("foo_new_event_query"), TEXT("{}"), Data));\n',
                encoding="utf-8",
            )
            generated_dir = default_coverage_output_dir(root, root)
            generated_dir.mkdir(parents=True)
            stale = {
                "schema": "ue_agent_interface.coverage_matrix.v2",
                "command_count": 1,
                "missing_doc": [],
                "missing_implementation": [],
                "missing_smoke": [],
                "raw_generated_doc_count": 0,
                "deprecated_doc_count": 0,
                "rows": [
                    {
                        "command": "foo_existing",
                        "doc_file": "docs/commands/01_Test.md",
                        "doc_status": "explicit",
                        "deprecated": False,
                        "implemented": True,
                        "smoke_tested": True,
                        "implementation_files": ["Source/UeAgentInterface/Private/Commands/Test/UeAgentHttpServer_Test.cpp"],
                        "smoke_files": ["Source/UeAgentInterfaceTests/Private/Smoke/UeAgentInterfaceSmoke_Test.cpp"],
                        "smoke_coverage_status": "direct",
                        "smoke_coverage_priority": "covered",
                    }
                ],
            }
            (generated_dir / "command_coverage_matrix.json").write_text(json.dumps(stale), encoding="utf-8")

            stale_result = verify_written_coverage_matrix(root)
            self.assertFalse(stale_result["success"])
            self.assertIn("foo_new_event_query", stale_result["missing_in_file"])

            write_coverage_matrix(
                generated_dir / "command_coverage_matrix.json",
                generated_dir / "command_coverage_matrix.md",
                root,
            )
            current_result = verify_written_coverage_matrix(root)
            self.assertTrue(current_result["success"], current_result)

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
            ue_kb = pak / "skills" / "ue-kb"
            (ue_kb / "references").mkdir(parents=True)
            (ue_kb / "indexes").mkdir()
            (ue_kb / "SKILL.md").write_text("# ue kb\n", encoding="utf-8")
            (ue_kb / "kb-manifest.json").write_text("{}\n", encoding="utf-8")
            (ue_kb / "references" / "index.md").write_text("# index\n", encoding="utf-8")
            (ue_kb / "indexes" / "fts.sqlite").write_bytes(b"sqlite")
            result = verify_pak_layout(root)
            self.assertTrue(result["success"])

    def test_verify_pak_layout_rejects_obsolete_skills(self):
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
            ue_kb = pak / "skills" / "ue-kb"
            (ue_kb / "references").mkdir(parents=True)
            (ue_kb / "indexes").mkdir()
            (ue_kb / "SKILL.md").write_text("# ue kb\n", encoding="utf-8")
            (ue_kb / "kb-manifest.json").write_text("{}\n", encoding="utf-8")
            (ue_kb / "references" / "index.md").write_text("# index\n", encoding="utf-8")
            (ue_kb / "indexes" / "fts.sqlite").write_bytes(b"sqlite")
            (pak / "skills" / "leveldesign").mkdir()

            result = verify_pak_layout(root)

            self.assertFalse(result["success"])
            self.assertIn("obsolete_skill_present:skills/leveldesign", result["issues"])

    def test_current_project_has_no_smoke_debt(self):
        project_root = self.current_project_root()
        matrix = build_coverage_matrix(project_root)
        self.assertEqual([], matrix["missing_smoke"])
        self.assertEqual(0, matrix["smoke_coverage"]["actionable_missing_count"])

    def test_current_project_has_no_generated_catalog_docs(self):
        project_root = self.current_project_root()
        matrix = build_coverage_matrix(project_root)
        self.assertEqual(0, matrix["raw_generated_doc_count"])

    def test_quality_gate_fails_on_smoke_debt(self):
        with patch("uai_cli.quality_gate.build_command_manifest") as manifest_mock, patch(
            "uai_cli.quality_gate.build_coverage_matrix"
        ) as coverage_mock, patch("uai_cli.quality_gate.verify_written_coverage_matrix") as written_coverage_mock, patch(
            "uai_cli.quality_gate.verify_pak_layout"
        ) as pak_mock:
            manifest_mock.return_value = {"command_count": 1, "warnings": []}
            coverage_mock.return_value = {
                "command_count": 1,
                "missing_doc": [],
                "missing_implementation": [],
                "missing_smoke": ["foo_apply_folder"],
                "raw_generated_doc_count": 0,
                "smoke_coverage": {"actionable_missing_count": 1, "p0_count": 1, "p1_count": 0},
            }
            written_coverage_mock.return_value = {"success": True, "reason": "current"}
            pak_mock.return_value = {"success": True, "issues": [], "warnings": []}

            result = run_quality_gate(CURRENT.parents[1], run_tests=False)
            coverage_check = next(check for check in result["checks"] if check["name"] == "coverage_matrix")
            self.assertFalse(result["success"])
            self.assertFalse(coverage_check["success"])
            self.assertEqual(1, coverage_check["missing_smoke_count"])

    def test_quality_gate_fails_on_generated_catalog_docs(self):
        with patch("uai_cli.quality_gate.build_command_manifest") as manifest_mock, patch(
            "uai_cli.quality_gate.build_coverage_matrix"
        ) as coverage_mock, patch("uai_cli.quality_gate.verify_written_coverage_matrix") as written_coverage_mock, patch(
            "uai_cli.quality_gate.verify_pak_layout"
        ) as pak_mock:
            manifest_mock.return_value = {"command_count": 1, "warnings": []}
            coverage_mock.return_value = {
                "command_count": 1,
                "missing_doc": [],
                "missing_implementation": [],
                "missing_smoke": [],
                "raw_generated_doc_count": 1,
                "smoke_coverage": {"actionable_missing_count": 0, "p0_count": 0, "p1_count": 0},
            }
            written_coverage_mock.return_value = {"success": True, "reason": "current"}
            pak_mock.return_value = {"success": True, "issues": [], "warnings": []}

            result = run_quality_gate(CURRENT.parents[1], run_tests=False)
            coverage_check = next(check for check in result["checks"] if check["name"] == "coverage_matrix")
            self.assertFalse(result["success"])
            self.assertFalse(coverage_check["success"])
            self.assertEqual(1, coverage_check["generated_doc_catalog_count"])

    def test_quality_gate_fails_on_stale_generated_coverage(self):
        with patch("uai_cli.quality_gate.build_command_manifest") as manifest_mock, patch(
            "uai_cli.quality_gate.build_coverage_matrix"
        ) as coverage_mock, patch("uai_cli.quality_gate.verify_written_coverage_matrix") as written_coverage_mock, patch(
            "uai_cli.quality_gate.verify_pak_layout"
        ) as pak_mock:
            manifest_mock.return_value = {"command_count": 1, "warnings": []}
            coverage_mock.return_value = {
                "command_count": 1,
                "missing_doc": [],
                "missing_implementation": [],
                "missing_smoke": [],
                "raw_generated_doc_count": 0,
                "smoke_coverage": {"actionable_missing_count": 0, "p0_count": 0, "p1_count": 0},
            }
            written_coverage_mock.return_value = {
                "success": False,
                "reason": "generated_coverage_stale",
                "missing_in_file": ["foo_new_event_query"],
                "extra_in_file": [],
                "changed_command_count": 0,
            }
            pak_mock.return_value = {"success": True, "issues": [], "warnings": []}

            result = run_quality_gate(CURRENT.parents[1], run_tests=False)
            generated_check = next(check for check in result["checks"] if check["name"] == "generated_coverage_current")
            self.assertFalse(result["success"])
            self.assertFalse(generated_check["success"])
            self.assertEqual(1, generated_check["missing_in_file_count"])

    def test_quality_gate_disables_python_bytecode_for_unit_tests(self):
        with patch("uai_cli.quality_gate.build_command_manifest", return_value={"command_count": 1, "warnings": []}), patch(
            "uai_cli.quality_gate.build_coverage_matrix",
            return_value={
                "command_count": 1,
                "missing_doc": [],
                "missing_implementation": [],
                "missing_smoke": [],
                "raw_generated_doc_count": 0,
                "smoke_coverage": {"actionable_missing_count": 0, "p0_count": 0, "p1_count": 0},
            },
        ), patch("uai_cli.quality_gate.verify_written_coverage_matrix", return_value={"success": True, "reason": "current"}), patch(
            "uai_cli.quality_gate.verify_pak_layout", return_value={"success": True, "issues": [], "warnings": []}
        ), patch(
            "uai_cli.quality_gate.subprocess.run"
        ) as run_mock:
            run_mock.return_value.returncode = 0
            run_mock.return_value.stdout = ""
            run_mock.return_value.stderr = ""

            result = run_quality_gate(CURRENT.parents[1], run_tests=True)

        self.assertTrue(result["success"])
        self.assertEqual("1", run_mock.call_args.kwargs["env"]["PYTHONDONTWRITEBYTECODE"])


if __name__ == "__main__":
    unittest.main()
