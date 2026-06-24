import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_core import UaiCore
from uai_core.config import AppConfig
from uai_core.errors import ConfigError
from uai_core.http_client import HttpResult
from uai_cli.runner import execute_batch as compat_execute_batch
from uai_core.runner import execute_batch as core_execute_batch


def _test_config(*, command_manifest_enabled: bool = False, param_validation_mode: str = "off") -> AppConfig:
    return AppConfig(
        base_url="http://127.0.0.1:17777",
        token="token",
        timeout_seconds=1,
        clear_log_on_start=False,
        log_level="info",
        allow_nonloopback=False,
        niagara_guard_enabled=False,
        niagara_guard_strict=True,
        auto_cleanup_enabled=False,
        cleanup_tmp_max=120,
        cleanup_tmp_keep=40,
        cleanup_reports_max=200,
        cleanup_reports_keep=120,
        command_manifest_enabled=command_manifest_enabled,
        compatibility_check_enabled=False,
        expected_plugin_version_tag="",
        crash_capture_enabled=False,
        runtime_index_enabled=False,
        param_validation_mode=param_validation_mode,
        app_root=Path("."),
        reports_dir=Path("reports"),
        logs_dir=Path("logs"),
    )


class _FakeClient:
    def __init__(self, payload):
        self.payload = payload
        self.requests = []

    def post_json(self, path, payload):
        self.requests.append((path, payload))
        return HttpResult(payload=self.payload, elapsed_ms=5.0, status_code=200)


class _FakeDoctorClient:
    def get(self, path):
        if path == "/api/ping":
            return HttpResult(payload={"ok": True}, elapsed_ms=1.0, status_code=200)
        if path == "/api/status":
            return HttpResult(
                payload={"ok": True, "data": {"running": True, "version_tag": "test-plugin"}},
                elapsed_ms=2.0,
                status_code=200,
            )
        raise AssertionError(path)


class CoreApiTests(unittest.TestCase):
    def test_compat_runner_reexports_core_runner(self):
        self.assertIs(compat_execute_batch, core_execute_batch)

    def test_exec_returns_command_result(self):
        core = UaiCore(_test_config())
        core.client = _FakeClient({"ok": True, "error": "", "data": {"result": 1}})

        result = core.exec("get_world_state", preflight=False)

        self.assertTrue(result.success)
        self.assertEqual(result.request["command"], "get_world_state")
        self.assertEqual(core.client.requests[0][0], "/api/exec")

    def test_batch_result_indexes_request_ids(self):
        core = UaiCore(_test_config())
        core.client = _FakeClient(
            {
                "ok": True,
                "error": "",
                "data": {
                    "success": True,
                    "results": [
                        {"request_id": "world", "ok": True, "data": {"map_name": "TestMap"}},
                    ],
                },
            }
        )

        result = core.batch(
            [{"request_id": "world", "command": "get_world_state", "params": {}}],
            preflight=False,
        )

        self.assertTrue(result.success)
        self.assertEqual(result.result_by_request_id("world")["data"]["map_name"], "TestMap")

    def test_doctor_uses_status_payload_for_compatibility(self):
        core = UaiCore(_test_config())
        core.client = _FakeDoctorClient()

        result = core.doctor()

        self.assertTrue(result["success"])
        self.assertTrue(result["compatibility"]["server_running"])
        self.assertEqual(result["compatibility"]["plugin_version_tag"], "test-plugin")

    def test_exec_blocks_deprecated_command_before_http_by_default(self):
        manifest = {
            "commands": {
                "old_command": {
                    "deprecated": True,
                    "lifecycle": "deprecated",
                    "allowed_use_cases": ["migration"],
                }
            }
        }
        core = UaiCore(_test_config(command_manifest_enabled=True), manifest=manifest)
        core.client = _FakeClient({"ok": True, "error": "", "data": {"result": 1}})

        with self.assertRaises(ConfigError):
            core.exec("old_command")

        self.assertEqual(core.client.requests, [])

    def test_exec_allows_deprecated_command_with_explicit_use_case(self):
        manifest = {
            "commands": {
                "old_command": {
                    "deprecated": True,
                    "lifecycle": "deprecated",
                    "allowed_use_cases": ["migration"],
                }
            }
        }
        core = UaiCore(_test_config(command_manifest_enabled=True), manifest=manifest)
        core.client = _FakeClient({"ok": True, "error": "", "data": {"result": 1}})

        result = core.exec("old_command", allow_deprecated=True, deprecated_use_case="migration")

        self.assertTrue(result.success)
        lifecycle = result.command_manifest_validation["command_lifecycle_validation"]
        self.assertTrue(lifecycle["success"])
        self.assertEqual(lifecycle["warnings"], ["deprecated_command_allowed:old_command:migration"])

    def test_exec_blocks_curated_param_alias_before_http(self):
        manifest = {
            "commands": {
                "asset_duplicate": {
                    "param_schema": {
                        "properties": {
                            "source_asset_path": {"type": "string"},
                            "destination_asset_path": {"type": "string"},
                        }
                    }
                }
            }
        }
        core = UaiCore(_test_config(command_manifest_enabled=True, param_validation_mode="warn"), manifest=manifest)
        core.client = _FakeClient({"ok": True, "error": "", "data": {"result": 1}})

        with self.assertRaises(ConfigError):
            core.exec("asset_duplicate", {"asset_path": "/Game/A", "destination_asset_path": "/Game/B"})

        self.assertEqual(core.client.requests, [])


if __name__ == "__main__":
    unittest.main()
