"""Compatibility alias for :mod:`uai_core.utils`."""

from __future__ import annotations

import sys

from uai_core import utils as _core_module

sys.modules[__name__] = _core_module
