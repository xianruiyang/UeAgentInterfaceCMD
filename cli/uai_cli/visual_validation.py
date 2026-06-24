"""Compatibility alias for :mod:`uai_core.visual_validation`."""

from __future__ import annotations

import sys

from uai_core import visual_validation as _core_module

sys.modules[__name__] = _core_module
