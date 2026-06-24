"""Compatibility alias for :mod:`uai_core.logging_setup`."""

from __future__ import annotations

import sys

from uai_core import logging_setup as _core_module

sys.modules[__name__] = _core_module
