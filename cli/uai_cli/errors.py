"""Compatibility alias for :mod:`uai_core.errors`."""

from __future__ import annotations

import sys

from uai_core import errors as _core_module

sys.modules[__name__] = _core_module
