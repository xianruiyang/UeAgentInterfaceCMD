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
    _BINDING_CATALOG,
    CommandBindingCatalog,
    GeneratedClientBindingsMixin,
    OMITTED,
    bind_generated_commands,
)
from ..asset_durable import AssetDurableNamespace, _from_payload as _durable_from_payload
from ..artifact import _from_payload as _artifacts_from_payload
from ..connection_config import ConnectionSnapshot
from ..errors import TransportError, UsageError
from ..external_source import (
    ExternalSourceNamespace,
    is_file_source_command,
    prepare_public_params,
)
from ..network_transport import ITransportClient, TransportExchangeError
from ..operation import OperationHandle, OperationNamespace
from ..pie import PieNamespace
from ..result import Result
from ..runtime_session import _from_operation_payload
from ..workspace import ContentGraphNamespace, _finish_hjson_import
from ..uai_protocol import UaiCommandProtocolClient
from ..voxel_grid import VoxelGridHandle


@runtime_checkable
class _TransportProbe(Protocol):
    def probe(self) -> bool: ...


class _QueryProjection:
    """Small model-facing query surface with no wire identity arguments."""

    __slots__ = ("_client", "_generated")

    def __init__(self, client, generated) -> None:
        self._client = client
        self._generated = generated

    def command_search(self, intent):
        params = {"intent": intent}
        return self._client.execute("query.command.search", params)

    def command_usage(self, commands):
        if isinstance(commands, str):
            commands = [commands]
        return self._client.execute(
            "query.command.usage", {"commands": list(commands)}
        )

    def __getattr__(self, name):
        return getattr(self._generated, name)


class Client(GeneratedClientBindingsMixin):
    """Owns one immutable connection snapshot and one Transport client."""

    __slots__ = (
        "_connection",
        "_content_graph_namespace",
        "_binding_catalog",
        "_asset_durable_namespace",
        "_generated_commands",
        "_external_source_namespace",
        "_operation_namespace",
        "_pie_namespace",
        "_query_projection",
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
        self._binding_catalog = binding_catalog or _BINDING_CATALOG
        self._generated_commands = bind_generated_commands(self)
        self._asset_durable_namespace = AssetDurableNamespace(self)
        self._external_source_namespace = ExternalSourceNamespace(self)
        self._content_graph_namespace = ContentGraphNamespace(
            self, self._generated_commands.content_graph
        )
        self._operation_namespace = OperationNamespace(
            self, self._generated_commands.operation
        )
        self._query_projection = _QueryProjection(
            self, self._generated_commands.query
        )
        self._state = "open"
        self._pie_namespace = PieNamespace(self)

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
            failure = TransportExchangeError.from_exception(exc, phase="probe")
            diagnostic = failure.diagnostic.as_dict()
            diagnostic["code"] = "transport_probe_failed"
            raise TransportError(
                code="transport_probe_failed",
                message=failure.diagnostic.message,
                diagnostic=diagnostic,
            ) from None

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
        if binding is None or binding.status not in {"active", "dormant"}:
            raise UsageError(
                code="command_binding_unknown",
                message=f"command binding is unknown: {command_id}",
            )
        return self.execute_exact(
            binding.command_id,
            params,
        )

    def execute_exact(self, command_id, params):
        """Send one exact projected command without aliases or replay."""

        binding = self._binding_catalog.find(command_id)
        if binding is not None and binding.status in {"disabled", "deprecated"}:
            raise UsageError(
                code="command_binding_disabled",
                message=f"command binding is disabled: {command_id}",
            )
        if binding is None:
            raise UsageError(
                code="command_binding_unknown",
                message=f"command binding is unknown: {command_id}",
            )
        projected = prepare_public_params(self, command_id, params)
        return self._send_exact(
            command_id, projected, contract_hash=binding.binding_hash
        )

    def execute_dormant(
        self,
        command_id,
        params,
        *,
        user_confirmed=None,
    ):
        """Compatibility alias for :meth:`execute`.

        ``user_confirmed`` is ignored; dormant commands use the ordinary exact
        command path.
        """

        return self.execute(command_id, params)

    def _send_exact(
        self, command_id, params, *, contract_hash, allow_operation_handle=True
    ):
        """Validate and send one exact projected command."""

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
        request_id = f"req-{uuid.uuid4()}"
        binding = self._binding_catalog.find(command_id)
        recovery = (self.operation._begin_request(command_id, request_id, snapshot)
                    if binding is not None and binding.supports_operation_recovery else None)
        try:
            result = self._protocol_client.invoke(
                command_id=command_id,
                command_binding_hash=contract_hash,
                params=snapshot,
                correlation_id=f"corr-{uuid.uuid4()}",
                request_id=request_id,
            )
            wrapped = self._wrap_result(command_id, result,
                                        allow_operation_handle=allow_operation_handle or recovery is not None)
            if recovery is not None:
                self.operation._accept_result(*recovery, wrapped)
            return wrapped
        except BaseException as error:
            if recovery is not None and isinstance(getattr(error, "diagnostic", None), dict):
                error.diagnostic.update(recovery_name=recovery[0], retry_safe=False,
                                        recovery_action=f"client.operation.recover({recovery[0]!r})")
            raise

    def _wrap_result(self, command_id, result, *, allow_operation_handle=True):
        """Apply the same public projection to direct and recovered command replies."""
        payload = result._machine_payload
        hidden_fields = (
            frozenset({"source_ref"})
            if is_file_source_command(command_id)
            else frozenset()
        )
        binding = self._binding_catalog.find(command_id)
        model_result_fields = (
            tuple(
                (field.name, field.source_path)
                for field in binding.model_result_fields
            )
            if binding is not None
            else ()
        )
        durable_journals = _durable_from_payload(self, payload)
        artifacts = _artifacts_from_payload(self, payload)
        if (
            allow_operation_handle
            and isinstance(payload, Mapping)
            and payload.get("operation_ref") is not None
        ):
            operation = OperationHandle(
                self,
                payload["operation_ref"],
                payload.get("generation"),
            )
            runtime_session = _from_operation_payload(self, payload)
            if runtime_session is not None:
                operation._set_runtime_session(runtime_session)
            return Result(
                result._machine_response,
                long_running=True,
                operation=operation,
                artifacts=artifacts,
                durable_journals=durable_journals,
                runtime_session=runtime_session,
                hidden_fields=hidden_fields,
                model_result_fields=model_result_fields,
            )
        if command_id == "mesh.voxel_grid.begin":
            handle = (
                VoxelGridHandle(self, payload)
                if result.ok and isinstance(payload, Mapping)
                else None
            )
            return Result(
                result._machine_response,
                durable_journals=durable_journals,
                artifacts=artifacts,
                voxel_grid=handle,
                voxel_grid_projection=True,
                hidden_fields=hidden_fields,
                model_result_fields=model_result_fields,
            )
        return Result(
            result._machine_response,
            artifacts=artifacts,
            durable_journals=durable_journals,
            hidden_fields=hidden_fields,
            model_result_fields=model_result_fields,
        )

    def _execute_voxel_grid_lifecycle(self, command_id, params, handle):
        if not isinstance(handle, VoxelGridHandle) or command_id not in {
            "mesh.voxel_grid.session",
            "mesh.voxel_grid.apply",
        }:
            raise UsageError(
                code="voxel_grid_lifecycle_binding_unknown",
                message=f"voxel-grid lifecycle binding is unknown: {command_id}",
            )
        binding = self._binding_catalog.find(command_id)
        if binding is None or binding.status != "dormant":
            raise UsageError(
                code="voxel_grid_lifecycle_binding_unknown",
                message=f"voxel-grid lifecycle binding is unknown: {command_id}",
            )
        result = self._send_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )
        return Result(
            result._machine_response,
            artifacts=result.artifacts,
            voxel_grid=handle,
        )

    def _execute_operation_lifecycle(self, command_id, params):
        binding = self._binding_catalog.find(command_id)
        if binding is None or command_id not in {
            "operation.status",
            "operation.resume",
            "operation.cancel",
            "operation.receipt",
            "operation.reconcile",
            "operation.release",
            "operation.discover",
            "operation.recover",
            "operation.takeover",
        }:
            raise UsageError(
                code="operation_lifecycle_binding_unknown",
                message=f"operation lifecycle binding is unknown: {command_id}",
            )
        result = self._send_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
            allow_operation_handle=False,
        )
        return Result(
            result._machine_response,
            artifacts=result.artifacts,
            long_running=True,
            operation=result.operation,
        )

    def _execute_runtime_scenario(
        self,
        *,
        session,
        subject_ref,
        policy_id,
        parameters,
    ):
        command_id = "runtime.scenario.execute"
        binding = self._binding_catalog.find(command_id)
        if binding is None or binding.status not in {"active", "dormant"}:
            raise UsageError(
                code="runtime_scenario_binding_unknown",
                message="runtime scenario binding is unavailable",
            )
        result = self._send_exact(
            command_id,
            {
                "subject_ref": subject_ref,
                "policy_id": policy_id,
                "parameters": parameters,
            },
            contract_hash=binding.binding_hash,
        )
        if result.operation is not None:
            result.operation._set_runtime_session(session)
        session._update_from_payload(result._machine_payload)
        return Result(
            result._machine_response,
            artifacts=result.artifacts,
            long_running=True,
            operation=result.operation,
            runtime_session=session,
        )

    def _execute_asset_durable(self, command_id, params, *, handle):
        binding = self._binding_catalog.find(command_id)
        if binding is None or binding.status not in {"active", "dormant"}:
            raise UsageError(
                code="asset_durable_binding_unknown",
                message="asset durable maintenance binding is unavailable",
            )
        result = self._send_exact(
            command_id,
            params,
            contract_hash=binding.binding_hash,
            allow_operation_handle=False,
        )
        return Result(
            result._machine_response,
            artifacts=result.artifacts,
            durable_journals=(handle,),
        )

    def _import_hjson_workspace(self, target, source):
        params = {"target": target, "source": dict(source)}
        binding = self._binding_catalog.find("content_graph.import_workspace")
        if binding is None or binding.status not in {"active", "dormant"}:
            raise UsageError(
                code="content_graph_binding_unknown",
                message="content graph import binding is unavailable",
            )
        result = self._send_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )
        return _finish_hjson_import(self, result)

    def _export_hjson_workspace(
        self,
        target,
        workspace_path,
        *,
        profile_id=OMITTED,
        source=OMITTED,
    ):
        binding = self._binding_catalog.find("content_graph.export_workspace")
        if binding is None or binding.status not in {"active", "dormant"}:
            raise UsageError(
                code="content_graph_binding_unknown",
                message="content graph export binding is unavailable",
            )
        params = {"target": target, "workspace_path": workspace_path}
        if profile_id is not OMITTED:
            params["profile_id"] = profile_id
        if source is not OMITTED:
            params["source"] = source
        return self._send_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )

    def close(self) -> None:
        if self._state == "closed":
            return
        try:
            self._transport.close()
        except (UsageError, TransportError):
            raise
        except Exception as exc:
            failure = TransportExchangeError.from_exception(exc, phase="close")
            diagnostic = failure.diagnostic.as_dict()
            diagnostic["code"] = "transport_close_failed"
            raise TransportError(
                code="transport_close_failed",
                message=failure.diagnostic.message,
                diagnostic=diagnostic,
            ) from None
        self._state = "closed"

    @property
    def query(self):
        return self._query_projection

    @property
    def asset_durable(self) -> AssetDurableNamespace:
        return self._asset_durable_namespace

    @property
    def content_graph(self) -> ContentGraphNamespace:
        return self._content_graph_namespace

    @property
    def external_source(self) -> ExternalSourceNamespace:
        return self._external_source_namespace

    @property
    def operation(self) -> OperationNamespace:
        return self._operation_namespace

    @property
    def pie(self) -> PieNamespace:
        return self._pie_namespace

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
