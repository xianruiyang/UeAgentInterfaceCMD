from __future__ import annotations

import sys
from pathlib import Path


TESTS_DIR = Path(__file__).resolve().parent
TOOLS_ROOT = TESTS_DIR.parent
CLI_ROOT = TOOLS_ROOT.parent
sys.path.insert(0, str(TOOLS_ROOT))

from uai_repository.project_paths import find_development_project_root


PROJECT_ROOT = find_development_project_root(CLI_ROOT, include_cwd=False) or CLI_ROOT.parent
