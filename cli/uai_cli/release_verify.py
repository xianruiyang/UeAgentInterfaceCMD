"""Compatibility alias for :mod:`uai_core.release_verify`."""

from __future__ import annotations

import sys

from uai_core import release_verify as _core_module

sys.modules[__name__] = _core_module
