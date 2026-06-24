"""Compatibility alias for :mod:`uai_core.command_manifest`."""

from __future__ import annotations

import sys

from uai_core import command_manifest as _core_module

sys.modules[__name__] = _core_module
