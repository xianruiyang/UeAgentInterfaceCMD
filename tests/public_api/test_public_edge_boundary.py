from __future__ import annotations

import ast
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
CLI_ROOT = REPO_ROOT / "cli"
PUBLIC_RUNTIME_ROOT = CLI_ROOT / "uai"
LEGACY_RUNTIME_ROOT = CLI_ROOT / "uai_core"

REMOVED_SECOND_OWNER_PATHS = (
    LEGACY_RUNTIME_ROOT,
    CLI_ROOT / "uai_cli" / "quality_gate.py",
    CLI_ROOT / "uai_cli" / "release_pipeline.py",
    CLI_ROOT / "uai_cli" / "release_verify.py",
    CLI_ROOT / "uai_cli" / "coverage_policy.py",
    CLI_ROOT / "uai_cli" / "command_manifest.py",
    CLI_ROOT / "uai_cli" / "command_schema.py",
)


def _python_files(root: Path) -> tuple[Path, ...]:
    return tuple(
        sorted(
            path
            for path in root.rglob("*.py")
            if "__pycache__" not in path.parts
        )
    )


def _imports(path: Path) -> tuple[str, ...]:
    tree = ast.parse(
        path.read_text(encoding="utf-8-sig"),
        filename=str(path),
    )
    modules: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.append(node.module)
    return tuple(modules)


class PythonPublicEdgeBoundaryTests(unittest.TestCase):
    def test_removed_python_business_and_combined_gate_owners_stay_absent(
        self,
    ) -> None:
        present = [
            path.relative_to(REPO_ROOT).as_posix()
            for path in REMOVED_SECOND_OWNER_PATHS
            if path.exists()
        ]
        self.assertEqual(
            present,
            [],
            "python_second_owner_present:" + ",".join(present),
        )

    def test_import_uai_has_no_connection_or_process_side_effects(self) -> None:
        probe = r'''
import json
import pathlib
import sys
import threading

events = []
def audit(event, args):
    if event.startswith("socket.") or event in {"subprocess.Popen", "os.system"}:
        events.append({"event": event, "value": str(args[0]) if args else ""})
    if event == "open" and args:
        value = str(args[0])
        if pathlib.Path(value).suffix.lower() in {".toml", ".hjson", ".uproject", ".ini"}:
            events.append({"event": event, "value": value})

sys.addaudithook(audit)
before_threads = {thread.ident for thread in threading.enumerate()}
error = None
try:
    import uai  # noqa: F401
except Exception as exc:
    error = f"{type(exc).__name__}:{exc}"
after_threads = {thread.ident for thread in threading.enumerate()}
print(json.dumps({
    "error": error,
    "events": events,
    "new_threads": sorted(
        item for item in after_threads - before_threads if item is not None
    ),
}, ensure_ascii=False))
'''
        env = os.environ.copy()
        env["PYTHONPATH"] = str(CLI_ROOT)
        completed = subprocess.run(
            [sys.executable, "-c", probe],
            cwd=REPO_ROOT,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=15,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        payload = json.loads(completed.stdout)
        self.assertIsNone(payload["error"], payload["error"])
        self.assertEqual(payload["events"], [])
        self.assertEqual(payload["new_threads"], [])

    def test_http_dependencies_exist_only_in_http_transport_adapter(self) -> None:
        violations: list[str] = []
        for path in _python_files(PUBLIC_RUNTIME_ROOT):
            relative = path.relative_to(PUBLIC_RUNTIME_ROOT)
            inside_http_adapter = relative.parts[:2] == (
                "network_transport",
                "http",
            )
            for module in _imports(path):
                if (
                    module == "http.client"
                    or module == "requests"
                    or module.startswith("urllib")
                ) and not inside_http_adapter:
                    violations.append(
                        f"{relative.as_posix()}=>{module}"
                    )
        self.assertEqual(
            violations,
            [],
            "direct_http_outside_adapter:" + ",".join(violations),
        )


if __name__ == "__main__":
    unittest.main()
