from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from types import MappingProxyType
from typing import Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .artifact import ArtifactHandle
    from .asset_durable import DurableJournalHandle
    from .operation import OperationHandle
    from .runtime_session import RuntimeSessionHandle
    from .voxel_grid import VoxelGridHandle
    from .rig_bake import RigBakeContextHandle

from .errors import ProtocolError, ServerCommandError


_OPERATION_PAYLOAD_FIELDS = frozenset(
    {
        "schema",
        "phase",
        "lifecycle_status",
        "stop_requested",
        "terminal",
        "cleanup_complete",
        "progress_diagnostic",
        "retry_safe",
        "error_code",
        "diagnostic",
        "warnings",
    }
)

_OPERATION_SIGNAL_FIELDS = frozenset({"type_id", "payload"})

_VOXEL_GRID_SESSION_FIELDS = frozenset(
    {
        "actor_ref",
        "actor_name",
        "actor_label",
        "cell_size",
        "occupied_cell_count",
        "geometry_representation",
        "solid_piece_count",
        "volume_cm3",
        "solid_bounds",
        "dirty",
        "committed",
        "state_unknown",
        "grid_origin",
        "grid_rotation",
        "anchor",
        "changed_cell_count",
        "changed_volume_cm3",
        "bounds",
        "shape",
        "collision_mode",
        "equivalent",
        "authoring_state_equivalent",
        "mesh_equivalent",
        "collision_exact_cover",
        "no_stale_owned_collision",
        "material_equivalent",
        "transform_equivalent",
        "vertex_count",
        "triangle_count",
        "collision_convex_count",
        "exposed_face_count",
        "collision_box_count",
        "covered_cell_count",
        "released",
        "actor_destroyed",
        "actor_release_confirmed",
        "durability_release_confirmed",
    }
)

# These fields belong to protocol, continuation, integrity, process, or local
# filesystem custody.  They may remain in the lossless SDK envelope, but are
# never part of the model-facing Result projection.  This is a semantic field
# policy rather than an entropy/length heuristic: business names and Unreal
# package/object refs remain readable.
_MACHINE_FIELDS = frozenset(
    {
        "binding_hash",
        "absolute_path",
        "additional_artifact_refs",
        "artifact_id",
        "artifact_ref",
        "binary_path",
        "build_version_path",
        "capture_evidence_id",
        "command_binding_hash",
        "config_file",
        "content_hash",
        "contract_hash",
        "contract_hashes",
        "correlation_id",
        "descriptor_id",
        "default_output_file",
        "digest",
        "digests",
        "editor_instance_id",
        "editor_process_identity",
        "evidence_id",
        "evidence_ids",
        "executable_path",
        "expected_fencing_token",
        "expected_generation",
        "expected_journal_owner_id",
        "expected_pause_epoch",
        "expected_revision",
        "expected_workspace_revision",
        "fencing_token",
        "fingerprint",
        "fingerprints",
        "guid",
        "guids",
        "hash",
        "hashes",
        "identities",
        "identity",
        "journal_id",
        "journal_owner_id",
        "launch_id",
        "locator",
        "manifest_file",
        "nonce",
        "operation_id",
        "operation_ref",
        "owner_lease_id",
        "output_directory",
        "output_file",
        "pause_epoch",
        "pie_instance_id",
        "project_instance_id",
        "project_file",
        "provider_id",
        "publisher_owner_id",
        "receipt",
        "receipts",
        "receipt_id",
        "receipt_path",
        "report_ref",
        "request_id",
        "revision",
        "revisions",
        "server_session_id",
        "session_ref",
        "source_batch_receipt_path",
        "startup_log_path",
        "ticket",
        "verification_id",
        "workspace_path",
        "workspace_revision",
        "workspace_root",
    }
)

_MACHINE_FIELD_SUFFIXES = (
    "_fingerprint",
    "_guid",
    "_hash",
    "_identity",
    "_identities",
    "_nonce",
    "_sha256",
)

# These objects are business dictionaries whose keys come from Unreal/user
# content, not protocol field names.  A property or parameter may legitimately
# be named ``Hash`` or ``Identity``; keep that semantic key while still
# projecting machine fields from the value stored below it. Typed authoring
# ``literal`` payloads are business data throughout, including nested members.
_BUSINESS_KEYED_MAP_FIELDS = frozenset(
    {
        "categories",
        "definitions",
        "entries",
        "fields",
        "parameters",
        "cvars",
        "merged_values",
        "properties",
        "settings",
        "values",
    }
)

def _is_machine_field(
    key: object,
    hidden_fields: frozenset[str] = frozenset(),
) -> bool:
    if not isinstance(key, str):
        return False
    normalized = key.casefold()
    return (
        normalized in _MACHINE_FIELDS
        or normalized in hidden_fields
        or normalized.endswith(_MACHINE_FIELD_SUFFIXES)
    )


def _project_public_value(
    value: Any,
    hidden_fields: frozenset[str] = frozenset(),
    *,
    preserve_mapping_keys: bool = False,
) -> Any:
    """Recursively remove SDK-owned machine custody from public values."""

    if isinstance(value, Mapping):
        return {
            key: deepcopy(item) if key == "literal" else _project_public_value(
                item,
                hidden_fields,
                preserve_mapping_keys=(
                    isinstance(key, str)
                    and key.casefold() in _BUSINESS_KEYED_MAP_FIELDS
                ),
            )
            for key, item in value.items()
            if preserve_mapping_keys or not _is_machine_field(key, hidden_fields)
        }
    if isinstance(value, list):
        return [_project_public_value(item, hidden_fields) for item in value]
    if isinstance(value, tuple):
        return tuple(_project_public_value(item, hidden_fields) for item in value)
    return deepcopy(value)


def _project_public_error(value: Any) -> Any:
    """Expose declared failure facts and recovery, keeping machine custody private."""

    if not isinstance(value, Mapping):
        return None
    allowed = {
        "code",
        "error_code",
        "recovery_action",
        "retry_safe",
        "terminal_status",
        "mutation_started",
        "mutation_may_have_started",
    }
    projected = {
        key: _project_public_value(item)
        for key, item in value.items()
        if key in allowed
    }
    # The server owns the public diagnostic contract. Preserve all declared
    # fields, including future extensions; private strings are never decoded.
    diagnostic = value.get("diagnostic")
    if isinstance(diagnostic, Mapping):
        projected["diagnostic"] = deepcopy(dict(diagnostic))
    return projected


def _project_declared_model_result(
    value: Any,
    fields: tuple[tuple[str, tuple[str, ...]], ...],
    hidden_fields: frozenset[str],
) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        return {}
    projected: dict[str, Any] = {}
    for name, source_path in fields:
        selected: Any = value
        for segment in source_path:
            if not isinstance(selected, Mapping) or segment not in selected:
                raise ProtocolError(
                    code="model_result_field_missing",
                    message=f"declared model result field is missing: {name}",
                )
            selected = selected[segment]
        projected[name] = _project_public_value(selected, hidden_fields)
    if "warnings" in value:
        projected["warnings"] = deepcopy(value["warnings"])
    return projected

_VOXEL_GRID_PAYLOAD_FIELDS = frozenset(
    {
        "action",
        "terminal_status",
        "occupied_cell_count",
        "volume_cm3",
        "session_closed",
        "mesh",
        "collision",
        "errors",
        "warnings",
    }
)

def _project_operation_payload(value: Any, hidden_fields: frozenset[str] = frozenset()) -> Any:
    if not isinstance(value, Mapping):
        return deepcopy(value)
    projected = {
            key: deepcopy(item) if key in {"diagnostic", "progress_diagnostic", "warnings"} else _project_public_value(item, hidden_fields)
            for key, item in value.items()
            if key in _OPERATION_PAYLOAD_FIELDS
    }
    signal = value.get("latest_signal")
    if isinstance(signal, Mapping):
        projected_signal = {
            key: _project_public_value(item, hidden_fields)
            for key, item in signal.items()
            if key in _OPERATION_SIGNAL_FIELDS
        }
        if projected_signal:
            projected["latest_signal"] = projected_signal
    return projected


def _project_voxel_grid_payload(value: Any) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        return {}
    projected = {
        key: deepcopy(item) if key == "warnings" else _project_public_value(item)
        for key, item in value.items()
        if key in _VOXEL_GRID_PAYLOAD_FIELDS
    }
    readback = value.get("readback")
    if isinstance(readback, Mapping):
        projected_readback = {
            key: _project_public_value(item)
            for key, item in readback.items()
            if key in _VOXEL_GRID_SESSION_FIELDS
        }
        if projected_readback:
            projected["readback"] = projected_readback
    return projected


class Result:
    """Read-only public projection with a private lossless SDK envelope."""

    __slots__ = (
        "_response",
        "_public_response",
        "_artifacts",
        "_primary_artifact",
        "_additional_artifacts",
        "_operation",
        "_durable_journals",
        "_runtime_session",
        "_voxel_grid",
        "_rig_bake_context",
    )

    def __init__(
        self,
        raw_response: Mapping[str, Any],
        *,
        long_running: bool = False,
        operation: "OperationHandle | None" = None,
        artifacts: "tuple[ArtifactHandle, ...]" = (),
        durable_journals: "tuple[DurableJournalHandle, ...]" = (),
        runtime_session: "RuntimeSessionHandle | None" = None,
        voxel_grid: "VoxelGridHandle | None" = None,
        rig_bake_context: "RigBakeContextHandle | None" = None,
        voxel_grid_projection: bool = False,
        hidden_fields: frozenset[str] = frozenset(),
        model_result_fields: tuple[
            tuple[str, tuple[str, ...]], ...
        ] = (),
    ) -> None:
        if not isinstance(raw_response, Mapping):
            raise ProtocolError(
                code="response_envelope_invalid",
                message="server response must be a mapping",
            )
        snapshot = deepcopy(dict(raw_response))
        if type(snapshot.get("ok")) is not bool:
            raise ProtocolError(
                code="response_ok_invalid",
                message="server response ok must be a boolean",
            )
        correlation = snapshot.get("correlation_id")
        if not isinstance(correlation, str) or not correlation.strip():
            raise ProtocolError(
                code="response_correlation_missing",
                message="server response correlation_id is required",
            )
        diagnostics = snapshot.get("diagnostics", [])
        if not isinstance(diagnostics, list):
            raise ProtocolError.at_source(
                code="command_result_diagnostics_invalid",
                message="command result diagnostics must be an array",
                facts={"json_pointer": "/diagnostics", "expected_value": "array",
                            "actual_value": type(diagnostics).__name__},
            )
        for index, diagnostic in enumerate(diagnostics):
            if not isinstance(diagnostic, dict):
                raise ProtocolError.at_source(
                    code="command_result_diagnostics_invalid",
                    message="each command result diagnostic must be an object",
                    facts={"json_pointer": f"/diagnostics/{index}", "expected_value": "object",
                                "actual_value": type(diagnostic).__name__},
                )
        self._response = MappingProxyType(snapshot)
        public_snapshot = {"error": _project_public_error(snapshot.get("error"))}
        # The producer has already separated public facts from private evidence.
        # Keep supplemental diagnostics outside domain payload projections.
        public_snapshot["diagnostics"] = deepcopy(snapshot.get("diagnostics", []))
        # Errors have one shared projection. Domain payload projections must
        # not re-filter its versioned diagnostics or mutation/recovery facts.
        if model_result_fields and snapshot["ok"]:
            public_snapshot["payload"] = _project_declared_model_result(
                snapshot.get("payload"), model_result_fields, hidden_fields
            )
        elif model_result_fields:
            raw_payload = snapshot.get("payload")
            public_snapshot["payload"] = ({"warnings": deepcopy(raw_payload["warnings"])}
                                          if isinstance(raw_payload, Mapping) and "warnings" in raw_payload else {})
        elif long_running:
            public_snapshot["payload"] = _project_operation_payload(
                snapshot.get("payload"), hidden_fields
            )
        elif voxel_grid_projection or voxel_grid is not None:
            public_snapshot["payload"] = _project_voxel_grid_payload(
                snapshot.get("payload")
            )
        else:
            raw_payload = snapshot.get("payload")
            if isinstance(raw_payload, Mapping):
                public_snapshot["payload"] = _project_public_value(
                    {key: item for key, item in raw_payload.items() if key != "warnings"}, hidden_fields)
                if "warnings" in raw_payload:
                    public_snapshot["payload"]["warnings"] = deepcopy(raw_payload["warnings"])
            else:
                public_snapshot["payload"] = _project_public_value(raw_payload, hidden_fields)
        self._public_response = MappingProxyType(public_snapshot)
        self._artifacts = tuple(artifacts)
        from .artifact import _roles_from_payload
        self._primary_artifact, self._additional_artifacts = _roles_from_payload(
            snapshot.get("payload"), self._artifacts
        )
        self._operation = operation
        self._durable_journals = tuple(durable_journals)
        self._runtime_session = runtime_session
        self._voxel_grid = voxel_grid
        self._rig_bake_context = rig_bake_context

    @property
    def ok(self) -> bool:
        return self._response["ok"]

    def __repr__(self) -> str:
        return f"Result(ok={self.ok!r})"

    @property
    def payload(self) -> Any:
        return deepcopy(self._public_response.get("payload"))

    @property
    def error(self) -> Any:
        return deepcopy(self._public_response.get("error"))

    @property
    def diagnostics(self) -> list[dict[str, Any]]:
        return deepcopy(self._public_response["diagnostics"])

    @property
    def operation(self) -> "OperationHandle | None":
        return self._operation

    @property
    def artifacts(self) -> "tuple[ArtifactHandle, ...]":
        return self._artifacts

    @property
    def primary_artifact(self) -> "ArtifactHandle | None":
        """The explicitly declared primary output, independent of artifact list order."""
        return self._primary_artifact

    @property
    def additional_artifacts(self) -> "tuple[ArtifactHandle, ...]":
        """Declared additional outputs in receipt index order, retaining repeated roles."""
        return self._additional_artifacts

    @property
    def durable_journals(self) -> "tuple[DurableJournalHandle, ...]":
        return self._durable_journals

    @property
    def runtime_session(self) -> "RuntimeSessionHandle | None":
        return self._runtime_session

    @property
    def voxel_grid(self) -> "VoxelGridHandle | None":
        return self._voxel_grid

    @property
    def rig_bake_context(self) -> "RigBakeContextHandle | None":
        return self._rig_bake_context

    @property
    def _machine_payload(self) -> Any:
        return deepcopy(self._response.get("payload"))

    @property
    def _machine_response(self) -> Mapping[str, Any]:
        return MappingProxyType(deepcopy(dict(self._response)))

    def raise_for_error(self) -> Result:
        if not self.ok:
            raise ServerCommandError(result=self)
        return self


__all__ = ["Result"]
