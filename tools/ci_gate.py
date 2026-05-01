from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "cli"))

from uai_cli.quality_gate import run_quality_gate  # noqa: E402


def main() -> int:
    run_tests = "--run-tests" in sys.argv
    result = run_quality_gate(ROOT, run_tests=run_tests)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result.get("success") else 2


if __name__ == "__main__":
    raise SystemExit(main())
