from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Any

from .network_transport.http import (
    build_http_transport,
    load_http_transport_options,
)


class UnsupportedTransportError(ValueError):
    pass


class TransportOptionsError(ValueError):
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
            "transport_options must be a table"
        )
    unknown = sorted(set(raw) - {transport})
    if unknown:
        raise TransportOptionsError(
            "transport_options contains unknown adapters: "
            + ",".join(unknown)
        )
    try:
        selected = raw[transport]
    except KeyError as exc:
        raise TransportOptionsError(
            f"transport_options.{transport} is required"
        ) from exc
    try:
        options = loader(selected, endpoint=endpoint)
    except (TypeError, ValueError) as exc:
        raise TransportOptionsError(str(exc)) from exc
    return MappingProxyType({transport: options})


def default_transport_factories() -> Mapping[str, Any]:
    return _TRANSPORT_FACTORIES


__all__ = [
    "TransportOptionsError",
    "UnsupportedTransportError",
    "default_transport_factories",
    "load_transport_options",
]
