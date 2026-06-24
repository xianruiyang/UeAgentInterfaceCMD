"""Compatibility alias for :mod:`uai_core.release_pipeline`."""

from __future__ import annotations

import sys

from uai_core import release_pipeline as _core_module

sys.modules[__name__] = _core_module
