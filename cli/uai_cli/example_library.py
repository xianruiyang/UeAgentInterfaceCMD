"""Compatibility alias for :mod:`uai_core.example_library`."""

from __future__ import annotations

import sys

from uai_core import example_library as _core_module

sys.modules[__name__] = _core_module
