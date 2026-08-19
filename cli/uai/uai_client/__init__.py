"""Single-command remote client boundary.

Business workflows, local selectors, and hidden multi-command calls are not
owned here.
"""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
import re
from typing import Protocol, runtime_checkable
import uuid

from ..commands import (
    BINDING_CATALOG,
    CommandBindingCatalog,
    GeneratedClientBindingsMixin,
    bind_generated_commands,
)
from ..connection_config import ConnectionSnapshot
from ..errors import TransportError, UsageError
from ..network_transport import ITransportClient
from ..uai_protocol import UaiCommandProtocolClient


@runtime_checkable
class _TransportProbe(Protocol):
    def probe(self) -> bool: ...


class Client(GeneratedClientBindingsMixin):
    """Owns one immutable connection snapshot and one Transport client."""

    __slots__ = (
        "_connection",
        "_binding_catalog",
        "_generated_commands",
        "_protocol_client",
        "_state",
        "_transport",
    )

    def __init__(
        self,
        *,
        connection: ConnectionSnapshot,
        transport: ITransportClient,
        protocol_client=None,
        binding_catalog: CommandBindingCatalog | None = None,
    ) -> None:
        self._connection = connection
        self._transport = transport
        self._protocol_client = (
            protocol_client
            if protocol_client is not None
            else UaiCommandProtocolClient(transport=transport)
        )
        self._binding_catalog = binding_catalog or BINDING_CATALOG
        self._generated_commands = bind_generated_commands(self)
        self._state = "open"

    @property
    def connection_state(self) -> str:
        return self._state

    def probe(self) -> bool:
        if self._state != "open":
            raise UsageError(
                code="connection_closed",
                message="connection is closed",
            )
        if not isinstance(self._transport, _TransportProbe):
            raise TransportError(
                code="transport_probe_unsupported",
                message="the selected transport does not support probing",
            )
        try:
            return bool(self._transport.probe())
        except (UsageError, TransportError):
            raise
        except Exception as exc:
            raise TransportError(
                code="transport_probe_failed",
                message=str(exc) or "transport probe failed",
            ) from exc

    def execute(self, command_id, params):
        if self._state != "open":
            raise UsageError(
                code="connection_closed",
                message="connection is closed",
            )
        if not isinstance(command_id, str) or not command_id.strip():
            raise UsageError(
                code="command_id_invalid",
                message="command_id must be a non-empty string",
            )
        binding = self._binding_catalog.find(command_id)
        if binding is None or binding.status != "active":
            raise UsageError(
                code="command_binding_unknown",
                message=f"command binding is unknown: {command_id}",
            )
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )

    def execute_exact(self, command_id, params, *, contract_hash):
        """Send one exact projected command without aliases or replay."""

        if self._state != "open":
            raise UsageError(
                code="connection_closed",
                message="connection is closed",
            )
        if (
            not isinstance(command_id, str)
            or not command_id.strip()
            or command_id != command_id.strip()
        ):
            raise UsageError(
                code="command_id_invalid",
                message="command_id must be one exact non-empty string",
            )
        if (
            not isinstance(contract_hash, str)
            or re.fullmatch(r"sha256:[0-9a-f]{64}", contract_hash) is None
        ):
            raise UsageError(
                code="command_contract_hash_invalid",
                message="contract_hash must be one exact sha256 identity",
            )
        if not isinstance(params, Mapping):
            raise UsageError(
                code="command_params_invalid",
                message="command params must be an object",
            )
        snapshot = deepcopy(dict(params))
        if any(not isinstance(key, str) for key in snapshot):
            raise UsageError(
                code="command_params_invalid",
                message="command parameter names must be strings",
            )
        return self._protocol_client.invoke(
            command_id=command_id,
            command_binding_hash=contract_hash,
            params=snapshot,
            correlation_id=f"corr-{uuid.uuid4()}",
            request_id=f"req-{uuid.uuid4()}",
        )

    def close(self) -> None:
        if self._state == "closed":
            return
        try:
            self._transport.close()
        except Exception as exc:
            raise TransportError(
                code="transport_close_failed",
                message=str(exc) or "transport close failed",
            ) from exc
        self._state = "closed"

    def __enter__(self) -> Client:
        if self._state != "open":
            raise UsageError(
                code="connection_closed",
                message="connection is closed",
            )
        return self

    def __exit__(
        self,
        _exc_type,
        _exc_value,
        _traceback,
    ) -> None:
        self.close()


__all__ = ["Client"]
