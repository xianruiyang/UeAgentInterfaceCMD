"""Compatibility alias for :mod:`uai_core.config`."""

from __future__ import annotations

import sys

from uai_core import config as _core_module

sys.modules[__name__] = _core_module
