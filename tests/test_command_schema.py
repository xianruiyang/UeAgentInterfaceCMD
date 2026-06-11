import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.command_schema import build_param_schema, validate_command_payloads


class CommandSchemaTests(unittest.TestCase):
    def test_build_param_schema_infers_basic_types(self):
        schema = build_param_schema(["asset_path", "save_after_apply", "max_results", "targets[]", "format", "warmup_frames", "invert"])
        self.assertEqual(schema["properties"]["asset_path"]["type"], "string")
        self.assertEqual(schema["properties"]["save_after_apply"]["type"], "bool")
        self.assertEqual(schema["properties"]["max_results"]["type"], "number")
        self.assertEqual(schema["properties"]["targets"]["type"], "array")
        self.assertEqual(schema["properties"]["format"]["type"], "string")
        self.assertEqual(schema["properties"]["warmup_frames"]["type"], "number")
        self.assertEqual(schema["properties"]["invert"]["type"], "bool")

    def test_validate_payload_warns_on_type_mismatch(self):
        manifest = {
            "commands": {
                "foo_command": {
                    "param_schema": build_param_schema(["asset_path", "save_after_apply"]),
                }
            }
        }
        result = validate_command_payloads(
            [{"command": "foo_command", "params": {"asset_path": 1, "save_after_apply": "yes"}}],
            manifest,
        )
        self.assertTrue(result["success"])
        self.assertIn("param_type:asset_path:expected_string", result["warnings"])
        self.assertIn("param_type:save_after_apply:expected_bool", result["warnings"])

    def test_strict_mode_fails_on_warnings(self):
        manifest = {"commands": {"foo_command": {"param_schema": build_param_schema(["asset_path"])}}}
        result = validate_command_payloads(
            [{"command": "foo_command", "params": {"asset_path": 1}}],
            manifest,
            strict=True,
        )
        self.assertFalse(result["success"])


if __name__ == "__main__":
    unittest.main()
