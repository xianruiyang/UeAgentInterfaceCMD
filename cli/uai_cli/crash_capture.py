"""Compatibility alias for :mod:`uai_core.crash_capture`."""

from __future__ import annotations

import sys

from uai_core import crash_capture as _core_module

sys.modules[__name__] = _core_module
