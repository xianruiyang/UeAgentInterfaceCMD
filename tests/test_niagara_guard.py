import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.errors import PlanError
from uai_cli.niagara_guard import prepare_niagara_guarded_commands, verify_niagara_guard_response


class NiagaraGuardTests(unittest.TestCase):
    def test_block_remove_add_same_batch_when_strict(self):
        commands = [
            {
                "command": "niagara_system_remove_emitter",
                "params": {"system_asset_path": "/Game/AutoTests/Niagara/NS_Test", "emitter_name": "A"},
            },
            {
                "command": "niagara_system_add_emitter",
                "params": {"system_asset_path": "/Game/AutoTests/Niagara/NS_Test", "emitter_asset_path": "/Game/E/E_A"},
            },
        ]
        with self.assertRaises(PlanError):
            prepare_niagara_guarded_commands(
                commands=commands,
                phase_name="p1",
                guard_enabled=True,
                strict_guard=True,
            )

    def test_inject_guard_commands_for_mutation(self):
        commands = [
            {
                "command": "niagara_system_add_emitter",
                "params": {"system_asset_path": "/Game/AutoTests/Niagara/NS_Test", "emitter_asset_path": "/Game/E/E_A"},
            }
        ]
        prepared = prepare_niagara_guarded_commands(
            commands=commands,
            phase_name="p1",
            guard_enabled=True,
            strict_guard=False,
        )
        self.assertGreater(prepared.injected_command_count, 0)
        self.assertEqual(prepared.commands[0]["command"], "editor_prepare_exit")
        self.assertIn("/Game/AutoTests/Niagara/NS_Test", prepared.touched_system_paths)

    def test_create_emitter_does_not_register_system_postcheck(self):
        commands = [
            {
                "command": "niagara_create_emitter",
                "params": {"asset_path": "/Game/AutoTests/Niagara/NE_Test"},
            }
        ]
        prepared = prepare_niagara_guarded_commands(
            commands=commands,
            phase_name="p1",
            guard_enabled=True,
            strict_guard=False,
        )
        self.assertEqual(prepared.touched_system_paths, [])
        self.assertEqual(prepared.commands[0]["command"], "editor_prepare_exit")
        self.assertEqual(len(prepared.commands), 2)

    def test_deleted_system_does_not_register_postcheck(self):
        commands = [
            {
                "command": "niagara_create_system",
                "params": {"asset_path": "/Game/AutoTests/Niagara/NS_Temp"},
            },
            {
                "command": "niagara_compile_system",
                "params": {"asset_path": "/Game/AutoTests/Niagara/NS_Temp"},
            },
            {
                "command": "niagara_delete_asset",
                "params": {"asset_path": "/Game/AutoTests/Niagara/NS_Temp", "force_delete": True},
            },
        ]
        prepared = prepare_niagara_guarded_commands(
            commands=commands,
            phase_name="p1",
            guard_enabled=True,
            strict_guard=False,
        )
        self.assertEqual(prepared.touched_system_paths, [])
        self.assertEqual(prepared.injected_command_count, 1)
        self.assertEqual(prepared.commands[0]["command"], "editor_prepare_exit")

    def test_verify_fail_on_unknown_emitter(self):
        prepared = prepare_niagara_guarded_commands(
            commands=[
                {
                    "command": "niagara_system_add_emitter",
                    "params": {"system_asset_path": "/Game/AutoTests/Niagara/NS_Test", "emitter_asset_path": "/Game/E/E_A"},
                }
            ],
            phase_name="p1",
            guard_enabled=True,
            strict_guard=False,
        )
        payload = {
            "ok": True,
            "error": "",
            "data": {
                "success": True,
                "results": [
                    {
                        "index": 10,
                        "request_id": "x1",
                        "command": "niagara_system_list_emitters",
                        "data": {
                            "emitters": [
                                {"id": "123", "name": "Unknown Emitter"},
                            ]
                        },
                    }
                ],
            },
        }
        verify = verify_niagara_guard_response(payload, prepared)
        self.assertFalse(verify.success)
        self.assertEqual(verify.failed_error, "niagara_unknown_emitter_detected:Unknown Emitter")


if __name__ == "__main__":
    unittest.main()
