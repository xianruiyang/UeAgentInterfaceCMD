from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


CURRENT = Path(__file__).resolve()
TOOLS_DIR = CURRENT.parents[1]
sys.path.insert(0, str(TOOLS_DIR))

from uai_repository.crash_capture import (  # noqa: E402
    build_crash_signature,
    classify_failure,
    collect_failure_artifacts,
    inspect_crash_dir,
    pack_crash_dir,
)


class CrashCaptureTests(unittest.TestCase):
    def test_collect_inspect_and_pack_uses_repository_json(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            app_root = Path(temp_dir)
            report = app_root / "reports" / "fail.json"
            report.parent.mkdir()
            report.write_text("{}", encoding="utf-8")

            result = collect_failure_artifacts(
                app_root=app_root,
                operation="exec",
                exit_code=2,
                report_path=report,
                report_payload={
                    "task_id": "t1",
                    "success": False,
                    "failed_command": "asset.query",
                },
            )

            crash_dir = Path(result["crash_dir"])
            self.assertTrue((crash_dir / "manifest.json").exists())
            self.assertFalse((crash_dir / "manifest.hjson").exists())
            inspected = inspect_crash_dir(crash_dir)
            self.assertEqual(
                inspected["manifest"]["classification"],
                "CommandFailed",
            )
            packed = pack_crash_dir(crash_dir)
            self.assertTrue(packed.exists())

    def test_classification_is_diagnostic_not_business_outcome(self) -> None:
        self.assertEqual(
            classify_failure(
                exit_code=1,
                error=TimeoutError("timed out"),
                report_payload=None,
            ),
            "Timeout",
        )
        self.assertEqual(
            classify_failure(
                exit_code=1,
                error=ConnectionError("connection refused"),
                report_payload=None,
            ),
            "ServiceLost",
        )
        self.assertEqual(
            classify_failure(
                exit_code=3,
                error=None,
                report_payload={"success": False},
            ),
            "CommandFailed",
        )

    def test_signature_uses_persisted_evidence_without_replay_logic(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            app_root = Path(temp_dir)
            report = app_root / "reports" / "failure.json"
            report.parent.mkdir()
            report.write_text(
                json.dumps(
                    {
                        "success": False,
                        "failed_command": "asset.query",
                    }
                ),
                encoding="utf-8",
            )
            result = collect_failure_artifacts(
                app_root=app_root,
                operation="exec",
                exit_code=2,
                report_path=report,
                report_payload={
                    "success": False,
                    "failed_command": "asset.query",
                },
                error=RuntimeError("server returned an error"),
            )

            first = build_crash_signature(Path(result["crash_dir"]))
            second = build_crash_signature(Path(result["crash_dir"]))

            self.assertTrue(first["success"])
            self.assertEqual(first["signature"], second["signature"])
            self.assertEqual(first["failed_command"], "asset.query")


if __name__ == "__main__":
    unittest.main()
