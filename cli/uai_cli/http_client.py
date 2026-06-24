"""Compatibility alias for :mod:`uai_core.http_client`."""

from __future__ import annotations

import sys

from uai_core import http_client as _core_module

sys.modules[__name__] = _core_module
