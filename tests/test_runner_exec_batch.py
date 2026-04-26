import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.http_client import HttpResult
from uai_cli.runner import execute_batch


class _FakeClient:
    def __init__(self, payload):
        self.payload = payload

    def post_json(self, _path, _payload):
        return HttpResult(payload=self.payload, elapsed_ms=12.3, status_code=200)


class RunnerExecBatchTests(unittest.TestCase):
    def test_execute_batch_success_from_ok(self):
        payload = {
            "ok": True,
            "error": "",
            "data": {
                "mode": "exec_batch",
                "success": True,
                "failed_index": -1,
            },
        }
        report = execute_batch(_FakeClient(payload), "phase_a", [{"command": "get_world_state"}], stop_on_error=True)
        self.assertTrue(report.success)

    def test_execute_batch_fail_when_data_success_false(self):
        payload = {
            "ok": True,
            "error": "",
            "data": {
                "mode": "exec_batch",
                "success": False,
                "failed_index": 0,
                "failed_error": "x",
            },
        }
        report = execute_batch(_FakeClient(payload), "phase_a", [{"command": "bad_cmd"}], stop_on_error=True)
        self.assertFalse(report.success)


if __name__ == "__main__":
    unittest.main()

