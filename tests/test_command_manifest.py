import tempfile
import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.command_manifest import build_command_manifest, validate_command_names


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
            (source / "UeAgentHttpServer_Test.cpp").write_text(
                'if (CommandLower == TEXT("foo_command")) return CmdFoo(Ctx, OutData, OutError);\n',
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

    def test_validate_unknown_command(self):
        manifest = {"commands": {"known_command": {}}}
        unknown, warnings = validate_command_names(["known_command", "missing_command"], manifest)
        self.assertEqual(unknown, ["missing_command"])
        self.assertEqual(warnings, [])


if __name__ == "__main__":
    unittest.main()
