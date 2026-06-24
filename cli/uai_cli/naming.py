"""Compatibility alias for :mod:`uai_core.naming`."""

from __future__ import annotations

import sys

from uai_core import naming as _core_module

sys.modules[__name__] = _core_module
