"""Compatibility alias for :mod:`uai_core.templating`."""

from __future__ import annotations

import sys

from uai_core import templating as _core_module

sys.modules[__name__] = _core_module
