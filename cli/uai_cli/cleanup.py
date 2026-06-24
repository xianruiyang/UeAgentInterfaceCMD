"""Compatibility alias for :mod:`uai_core.cleanup`."""

from __future__ import annotations

import sys

from uai_core import cleanup as _core_module

sys.modules[__name__] = _core_module
