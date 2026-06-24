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

    def test_curated_required_params_fail_before_http(self):
        manifest = {
            "commands": {
                "asset_duplicate": {
                    "param_schema": build_param_schema(["source_asset_path", "destination_asset_path"]),
                }
            }
        }
        result = validate_command_payloads(
            [{"command": "asset_duplicate", "params": {"asset_path": "/Game/A", "destination_path": "/Game/B"}}],
            manifest,
        )

        self.assertFalse(result["success"])
        self.assertIn("param_alias:asset_path->source_asset_path", result["issues"])
        self.assertIn("param_alias:destination_path->destination_asset_path", result["issues"])
        self.assertIn("missing_required_param:source_asset_path:saw_alias:asset_path", result["issues"])
        self.assertIn("missing_required_param:destination_asset_path:saw_alias:destination_path", result["issues"])

    def test_curated_required_params_accept_canonical_names(self):
        manifest = {
            "commands": {
                "asset_duplicate": {
                    "param_schema": build_param_schema(["source_asset_path", "destination_asset_path"]),
                }
            }
        }
        result = validate_command_payloads(
            [{"command": "asset_duplicate", "params": {"source_asset_path": "/Game/A", "destination_asset_path": "/Game/B"}}],
            manifest,
        )

        self.assertTrue(result["success"])
        self.assertEqual(result["issues"], [])

    def test_unknown_param_warning_suggests_close_match(self):
        manifest = {
            "commands": {
                "sequence_apply_folder": {
                    "param_schema": build_param_schema(["asset_path", "save_after_apply"]),
                }
            }
        }
        result = validate_command_payloads(
            [{"command": "sequence_apply_folder", "params": {"asset_pat": "/Game/Seq"}}],
            manifest,
        )

        self.assertFalse(result["success"])
        self.assertIn("missing_required_param:asset_path", result["issues"])
        self.assertIn("unknown_param:asset_pat:did_you_mean:asset_path", result["warnings"])

    def test_control_rig_folder_commands_require_folder_path(self):
        manifest = {
            "commands": {
                "control_rig_apply_folder": {
                    "param_schema": build_param_schema(["folder_path", "asset_path", "compile_after_apply"]),
                }
            }
        }
        result = validate_command_payloads(
            [{"command": "control_rig_apply_folder", "params": {"asset_path": "/Game/CR_Test"}}],
            manifest,
        )

        self.assertFalse(result["success"])
        self.assertIn("param_alias:asset_path->folder_path", result["issues"])
        self.assertIn("missing_required_param:folder_path:saw_alias:asset_path", result["issues"])

    def test_probe_apply_candidate_accepts_documented_frame_index_selector(self):
        manifest = {
            "commands": {
                "probe_ik_goal_apply_candidate": {
                    "param_schema": build_param_schema(["frame_index", "selection", "candidate_index", "sequence_path", "control_name"]),
                }
            }
        }
        result = validate_command_payloads(
            [{"command": "probe_ik_goal_apply_candidate", "params": {"frame_index": 2, "sequence_path": "/Game/Seq", "control_name": "hand_r_ik_ctrl"}}],
            manifest,
        )

        self.assertTrue(result["success"])
        self.assertEqual(result["issues"], [])

    def test_probe_review_frames_accepts_documented_frames_array(self):
        manifest = {
            "commands": {
                "probe_ik_goal_review_frames": {
                    "param_schema": build_param_schema(["frames", "probe_request_id", "frame_sheet_max_size"]),
                }
            }
        }
        result = validate_command_payloads(
            [{"command": "probe_ik_goal_review_frames", "params": {"frames": [0, 20, 22], "probe_request_id": "probe-001"}}],
            manifest,
        )

        self.assertTrue(result["success"])
        self.assertEqual(result["issues"], [])

    def test_sequence_open_editor_paths_require_explicit_allow(self):
        manifest = {
            "commands": {
                "sequence_create_level_sequence": {
                    "param_schema": build_param_schema(["asset_path", "open_editor", "allow_editor_open"]),
                },
                "sequence_open_level_sequence": {
                    "param_schema": build_param_schema(["asset_path", "allow_editor_open"]),
                },
            }
        }
        result = validate_command_payloads(
            [
                {
                    "command": "sequence_create_level_sequence",
                    "params": {"asset_path": "/Game/Seq", "open_editor": True},
                },
                {
                    "command": "sequence_open_level_sequence",
                    "params": {"asset_path": "/Game/Seq"},
                },
            ],
            manifest,
        )

        self.assertFalse(result["success"])
        self.assertIn("open_editor_requires_allow_editor_open", result["issues"])
        self.assertIn("sequence_open_level_sequence_requires_allow_editor_open", result["issues"])

    def test_sequence_open_editor_paths_accept_explicit_allow(self):
        manifest = {
            "commands": {
                "sequence_create_level_sequence": {
                    "param_schema": build_param_schema(["asset_path", "open_editor", "allow_editor_open"]),
                },
                "sequence_open_level_sequence": {
                    "param_schema": build_param_schema(["asset_path", "allow_editor_open"]),
                },
            }
        }
        result = validate_command_payloads(
            [
                {
                    "command": "sequence_create_level_sequence",
                    "params": {"asset_path": "/Game/Seq", "open_editor": True, "allow_editor_open": True},
                },
                {
                    "command": "sequence_open_level_sequence",
                    "params": {"asset_path": "/Game/Seq", "allow_editor_open": True},
                },
            ],
            manifest,
        )

        self.assertTrue(result["success"])
        self.assertEqual(result["issues"], [])


if __name__ == "__main__":
    unittest.main()
