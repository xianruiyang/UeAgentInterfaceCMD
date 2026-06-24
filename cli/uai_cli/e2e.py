"""Compatibility alias for :mod:`uai_core.e2e`."""

from __future__ import annotations

import sys

from uai_core import e2e as _core_module

sys.modules[__name__] = _core_module
