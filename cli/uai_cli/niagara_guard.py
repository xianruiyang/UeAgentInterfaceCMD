"""Compatibility alias for :mod:`uai_core.niagara_guard`."""

from __future__ import annotations

import sys

from uai_core import niagara_guard as _core_module

sys.modules[__name__] = _core_module
