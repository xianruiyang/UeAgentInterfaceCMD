"""Compatibility alias for :mod:`uai_core.runtime_index`."""

from __future__ import annotations

import sys

from uai_core import runtime_index as _core_module

sys.modules[__name__] = _core_module
