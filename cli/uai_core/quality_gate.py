from __future__ import annotations

import subprocess
import sys
from pathlib import Path
import os
from typing import Any

from .command_manifest import build_command_manifest
from .release_verify import build_coverage_matrix, verify_pak_layout, verify_written_coverage_matrix
from .utils import now_compact


def run_quality_gate(app_root: Path, *, run_tests: bool = False) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []

    manifest = build_command_manifest()
    manifest_warnings = manifest.get("warnings", [])
    checks.append(
        {
            "name": "command_manifest",
            "success": bool(manifest.get("command_count", 0)),
            "command_count": manifest.get("command_count", 0),
            "warnings": manifest_warnings,
        }
    )

    coverage = build_coverage_matrix()
    missing_smoke = coverage.get("missing_smoke", [])
    generated_doc_catalog_count = int(coverage.get("raw_generated_doc_count", 0) or 0)
    checks.append(
        {
            "name": "coverage_matrix",
            "success": (
                len(coverage.get("missing_implementation", [])) == 0
                and len(missing_smoke) == 0
                and generated_doc_catalog_count == 0
            ),
            "command_count": coverage.get("command_count", 0),
            "missing_doc_count": len(coverage.get("missing_doc", [])),
            "missing_implementation_count": len(coverage.get("missing_implementation", [])),
            "missing_smoke_count": len(missing_smoke),
            "generated_doc_catalog_count": generated_doc_catalog_count,
            "smoke_actionable_missing_count": coverage.get("smoke_coverage", {}).get("actionable_missing_count", 0),
            "smoke_p0_count": coverage.get("smoke_coverage", {}).get("p0_count", 0),
            "smoke_p1_count": coverage.get("smoke_coverage", {}).get("p1_count", 0),
        }
    )
    generated_coverage = verify_written_coverage_matrix()
    checks.append(
        {
            "name": "generated_coverage_current",
            "success": bool(generated_coverage.get("success", False)),
            "reason": generated_coverage.get("reason", ""),
            "json_file": generated_coverage.get("json_file", ""),
            "missing_in_file_count": len(generated_coverage.get("missing_in_file", [])),
            "extra_in_file_count": len(generated_coverage.get("extra_in_file", [])),
            "changed_command_count": generated_coverage.get("changed_command_count", 0),
            "top_level_changed": generated_coverage.get("top_level_changed", []),
            "missing_in_file": generated_coverage.get("missing_in_file", [])[:20],
            "extra_in_file": generated_coverage.get("extra_in_file", [])[:20],
            "changed_commands": generated_coverage.get("changed_commands", [])[:20],
        }
    )

    pak = verify_pak_layout()
    checks.append(
        {
            "name": "pak_verify",
            "success": bool(pak.get("success", False)) and not pak.get("warnings"),
            "issues": pak.get("issues", []),
            "warnings": pak.get("warnings", []),
        }
    )

    if run_tests:
        env = dict(os.environ)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        proc = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
            cwd=app_root,
            text=True,
            capture_output=True,
            timeout=120,
            env=env,
        )
        checks.append(
            {
                "name": "unit_tests",
                "success": proc.returncode == 0,
                "returncode": proc.returncode,
                "stdout_tail": proc.stdout[-4000:],
                "stderr_tail": proc.stderr[-4000:],
            }
        )

    return {
        "schema": "ue_agent_interface.quality_gate.v1",
        "generated_at": now_compact(),
        "success": all(bool(check.get("success", False)) for check in checks),
        "checks": checks,
    }
