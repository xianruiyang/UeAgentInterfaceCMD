"""Compatibility alias for :mod:`uai_core.project_paths`."""

from __future__ import annotations

import sys

from uai_core import project_paths as _core_module

sys.modules[__name__] = _core_module
