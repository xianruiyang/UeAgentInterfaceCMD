from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import unittest

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - Python 3.10 fallback
    import tomli as tomllib


REPO_ROOT = Path(__file__).resolve().parents[2]
CLI_ROOT = REPO_ROOT / "cli"


class CliEntrypointContractTests(unittest.TestCase):
    def test_console_entry_has_one_thin_cli_owner(self) -> None:
        payload = tomllib.loads(
            (REPO_ROOT / "pyproject.toml").read_text(encoding="utf-8")
        )
        self.assertEqual(
            payload["project"]["scripts"],
            {"uai-cli": "uai_cli.main:main"},
        )

    def test_source_module_entry_is_available_without_installation(self) -> None:
        env = os.environ.copy()
        env["PYTHONPATH"] = str(CLI_ROOT)
        completed = subprocess.run(
            [sys.executable, "-m", "uai_cli", "--help"],
            cwd=REPO_ROOT,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=15,
            check=False,
        )
        self.assertEqual(completed.returncode, 0, completed.stderr)
        self.assertIn("connection", completed.stdout)
        self.assertIn("exec", completed.stdout)
        self.assertNotIn("release", completed.stdout)


if __name__ == "__main__":
    unittest.main()
