"""Command-line entry package for UeAgentInterfaceCMD.

Reusable execution logic lives in :mod:`uai_core`. This package keeps the
installed ``uai-cli`` console entry point and backward-compatible imports.
"""

from uai_core.version import __version__

__all__ = ["__version__"]
