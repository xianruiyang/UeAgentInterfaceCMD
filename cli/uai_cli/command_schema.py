"""Compatibility alias for :mod:`uai_core.command_schema`."""

from __future__ import annotations

import sys

from uai_core import command_schema as _core_module

sys.modules[__name__] = _core_module
