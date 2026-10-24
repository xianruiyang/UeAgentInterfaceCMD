from __future__ import annotations

from collections.abc import Callable, Mapping
from types import MappingProxyType
from typing import Any

from .connection_config import (
    ConnectionSnapshot,
    load_connection_toml,
)
from .errors import Error, TransportError, UsageError
from .network_transport import ITransportClient, TransportExchangeError
from .transport_catalog import default_transport_factories
from .uai_client import Client


TransportFactory = Callable[[ConnectionSnapshot], ITransportClient]
ClientFactory = Callable[[ConnectionSnapshot, ITransportClient], Any]


class ConnectionAssembler:
    """Selects one Transport Adapter and atomically builds one client."""

    def __init__(
        self,
        *,
        transport_factories: Mapping[str, TransportFactory],
        client_factory: ClientFactory,
    ) -> None:
        if not transport_factories:
            raise UsageError.at_source(
                code="connection_transport_factories_missing",
                message="At least one transport factory is required to assemble a connection.",
                facts={"property_path": "transport_factories", "expected_value": "non-empty mapping", "actual_value": {}},
            )
        self._transport_factories = MappingProxyType(
            dict(transport_factories)
        )
        self._client_factory = client_factory

    @property
    def transport_names(self) -> tuple[str, ...]:
        return tuple(sorted(self._transport_factories))

    @property
    def transport_factories(self) -> Mapping[str, TransportFactory]:
        return self._transport_factories

    def connect(self, snapshot: ConnectionSnapshot) -> Any:
        factory = self._transport_factories.get(snapshot.transport)
        if factory is None:
            raise UsageError.at_source(
                code="connection_transport_unsupported",
                message=(
                    "connection transport is unsupported: "
                    f"{snapshot.transport}"
                ),
                facts={"property_path": "connection.transport", "actual_value": snapshot.transport,
                       "expected_value": list(self.transport_names)},
            )
        transport = factory(snapshot)
        try:
            return self._client_factory(snapshot, transport)
        except BaseException as construction_exc:
            try:
                transport.close()
            except BaseException as cleanup_exc:
                construction = (construction_exc.diagnostic if isinstance(construction_exc, Error)
                                else TransportExchangeError.from_exception(
                                    construction_exc, phase="client_construction").diagnostic.as_dict())
                cleanup = (cleanup_exc.diagnostic if isinstance(cleanup_exc, Error)
                           else TransportExchangeError.from_exception(
                               cleanup_exc, phase="connection_cleanup").diagnostic.as_dict())
                raise TransportError.at_source(
                    code="connection_cleanup_failed",
                    message=(
                        "client construction failed and the transport "
                        "could not be closed"
                    ),
                    facts={"phase": "connection_cleanup", "cause": construction, "diagnostics": [cleanup]},
                ) from cleanup_exc
            raise


def _build_client(
    snapshot: ConnectionSnapshot,
    transport: ITransportClient,
) -> Client:
    return Client(
        connection=snapshot,
        transport=transport,
    )


_DEFAULT_ASSEMBLER = ConnectionAssembler(
    transport_factories=default_transport_factories(),
    client_factory=_build_client,
)


def connect(connection: str) -> Client:
    snapshot = load_connection_toml(connection)
    return _DEFAULT_ASSEMBLER.connect(snapshot)


__all__ = [
    "ConnectionAssembler",
    "connect",
]
