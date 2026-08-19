"""Public entry package for the UAI remote client SDK.

Importing this package intentionally performs no I/O.
"""

from .errors import (
    Error,
    ProtocolError,
    SerializationError,
    ServerCommandError,
    TransportError,
    UsageError,
)
from .connection import connect
from .result import Result
from .uai_client import Client


__version__ = "0.2.0"

__all__ = [
    "__version__",
    "connect",
    "Client",
    "Result",
    "Error",
    "UsageError",
    "SerializationError",
    "TransportError",
    "ProtocolError",
    "ServerCommandError",
]
