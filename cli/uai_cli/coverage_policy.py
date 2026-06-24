"""Compatibility alias for :mod:`uai_core.coverage_policy`."""

from __future__ import annotations

import sys

from uai_core import coverage_policy as _core_module

sys.modules[__name__] = _core_module
