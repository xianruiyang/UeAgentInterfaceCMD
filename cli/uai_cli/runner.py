"""Compatibility alias for :mod:`uai_core.runner`."""

from __future__ import annotations

import sys

from uai_core import runner as _core_module

sys.modules[__name__] = _core_module
