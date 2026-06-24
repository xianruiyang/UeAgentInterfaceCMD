"""Compatibility alias for :mod:`uai_core.quality_gate`."""

from __future__ import annotations

import sys

from uai_core import quality_gate as _core_module

sys.modules[__name__] = _core_module
