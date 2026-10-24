from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Any
from .network_transport import TransportOptionsError

from .network_transport.http import (
    build_http_transport,
    load_http_transport_options,
)


class UnsupportedTransportError(ValueError):
    pass


_OPTION_LOADERS = MappingProxyType(
    {
        "http": load_http_transport_options,
    }
)

_TRANSPORT_FACTORIES = MappingProxyType(
    {
        "http": build_http_transport,
    }
)


def load_transport_options(
    transport: str,
    raw: Any,
    *,
    endpoint: str,
) -> Mapping[str, Mapping[str, Any]]:
    loader = _OPTION_LOADERS.get(transport)
    if loader is None:
        raise UnsupportedTransportError(transport)
    if not isinstance(raw, Mapping):
        raise TransportOptionsError(
            "transport_options must be a table", property_path="transport_options",
            expected_value="table", actual_type=type(raw).__name__,
        )
    unknown = sorted(set(raw) - {transport})
    if unknown:
        raise TransportOptionsError(
            "transport_options contains unknown adapters: "
            + ",".join(unknown), property_path="transport_options",
            actual_value=unknown, expected_value=[transport],
        )
    try:
        selected = raw[transport]
    except KeyError:
        raise TransportOptionsError(
            f"transport_options.{transport} is required", property_path=f"transport_options.{transport}",
            actual_present=False, expected_value="table",
        ) from None
    options = loader(selected, endpoint=endpoint)
    return MappingProxyType({transport: options})


def default_transport_factories() -> Mapping[str, Any]:
    return _TRANSPORT_FACTORIES


__all__ = [
    "TransportOptionsError",
    "UnsupportedTransportError",
    "default_transport_factories",
    "load_transport_options",
]
