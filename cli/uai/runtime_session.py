"""Typed SDK custody for one paused PIE runtime session."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any, TYPE_CHECKING

from .errors import UsageError

if TYPE_CHECKING:
    from .result import Result


_POLICY_ID = "policy:runtime-scenario:bounded/v2"


def _runtime_fields(payload: object) -> Mapping | None:
    if not isinstance(payload, Mapping):
        return None
    signal = payload.get("latest_signal")
    if not isinstance(signal, Mapping):
        return None
    fields = signal.get("payload")
    if not isinstance(fields, Mapping):
        return None
    details = fields.get("details")
    if isinstance(details, Mapping):
        return {**fields, **details}
    return fields


class RuntimeSessionHandle:
    """Own machine session/fence values without exposing them to callers."""

    __slots__ = (
        "_client",
        "_session_ref",
        "_pause_epoch",
        "_workspace_revision",
        "_ended",
    )

    def __repr__(self) -> str:
        return "RuntimeSessionHandle()"

    def __init__(
        self,
        client: Any,
        *,
        session_ref: str,
        pause_epoch: int,
        workspace_revision: int,
    ) -> None:
        self._client = client
        self._session_ref = ""
        self._pause_epoch = 0
        self._workspace_revision = 0
        self._ended = False
        self._update_values(
            session_ref=session_ref,
            pause_epoch=pause_epoch,
            workspace_revision=workspace_revision,
        )

    def _update_values(
        self,
        *,
        session_ref: object,
        pause_epoch: object,
        workspace_revision: object,
    ) -> None:
        if not isinstance(session_ref, str) or not session_ref.strip():
            raise UsageError.at_source(
                code="runtime_session_invalid",
                message="runtime session_ref must be a non-empty string",
                facts={"property_path": "session_ref", "expected_value": "non-empty string",
                       "actual_type": type(session_ref).__name__},
            )
        for field_name, value in (
            ("pause_epoch", pause_epoch),
            ("workspace_revision", workspace_revision),
        ):
            if isinstance(value, float) and value.is_integer():
                value = int(value)
            if isinstance(value, bool) or not isinstance(value, int) or value < 1:
                raise UsageError.at_source(
                    code="runtime_session_invalid",
                    message=f"runtime session {field_name} must be a positive integer",
                    facts={"property_path": field_name, "expected_value": "positive integer",
                           "actual_type": type(value).__name__},
                )
        if self._session_ref:
            if session_ref != self._session_ref:
                raise UsageError.at_source(
                    code="runtime_session_identity_mismatch",
                    message="cannot merge snapshots from different runtime sessions",
                    facts={"property_path": "session_ref", "expected_value": "the current session identity",
                           "actual_value": "a different session identity"},
                )
            # A parent operation can still return its pre-scenario snapshot.
            # It must not replace the newer fence observed by the shared handle.
            if pause_epoch < self._pause_epoch or workspace_revision < self._workspace_revision:
                return
        self._session_ref = session_ref
        self._pause_epoch = int(pause_epoch)
        self._workspace_revision = int(workspace_revision)

    def _machine_state(self) -> dict[str, Any]:
        return {
            "session_ref": self._session_ref,
            "pause_epoch": self._pause_epoch,
            "workspace_revision": self._workspace_revision,
            "ended": self._ended,
        }

    @classmethod
    def _from_machine_state(cls, client: Any, state: Mapping) -> "RuntimeSessionHandle":
        handle = cls(
            client,
            session_ref=state.get("session_ref"),
            pause_epoch=state.get("pause_epoch"),
            workspace_revision=state.get("workspace_revision"),
        )
        ended = state.get("ended", False)
        if not isinstance(ended, bool):
            raise UsageError.at_source(
                code="runtime_session_invalid", message="runtime session ended must be a boolean",
                facts={"property_path": "ended", "expected_value": "boolean", "actual_type": type(ended).__name__},
            )
        handle._ended = ended
        return handle

    def _update_from_payload(self, payload: object) -> None:
        if self._ended:
            return
        if isinstance(payload, Mapping):
            signal = payload.get("latest_signal")
            if isinstance(signal, Mapping) and signal.get("type_id") == "uai.editor_session.runtime_preview.state/v1":
                fields = signal.get("payload")
                if isinstance(fields, Mapping) and fields.get("phase") != "active":
                    if fields.get("phase") in ("exited", "failed"):
                        self._ended = True
                    return
        details = _runtime_fields(payload)
        if not isinstance(details, Mapping) or "session_ref" not in details:
            return
        self._update_values(
            session_ref=details.get("session_ref"),
            pause_epoch=details.get("pause_epoch"),
            workspace_revision=details.get("workspace_revision"),
        )

    def scenario_execute(self, *, parameters: Mapping[str, Any]) -> "Result":
        if self._ended:
            raise UsageError.at_source(
                code="runtime_session_ended",
                message="runtime session has ended",
                facts={"property_path": "ended", "expected_value": False, "actual_value": True},
            )
        if not isinstance(parameters, Mapping):
            raise UsageError.at_source(
                code="runtime_scenario_parameters_invalid",
                message="runtime scenario parameters must be an object",
                facts={"property_path": "parameters", "expected_value": "object", "actual_type": type(parameters).__name__},
            )
        projected = deepcopy(dict(parameters))
        forbidden = {
            "expected_pause_epoch",
            "expected_workspace_revision",
            "session_ref",
            "subject_ref",
        }
        supplied = sorted(forbidden.intersection(projected))
        if supplied:
            raise UsageError.at_source(
                code="runtime_session_custody_owned_by_sdk",
                message="runtime continuation fields are SDK-owned",
                facts={"property_path": "parameters", "supplied_fields": supplied,
                       "expected_value": "business parameters without SDK-owned continuation fields"},
            )
        projected["expected_pause_epoch"] = self._pause_epoch
        projected["expected_workspace_revision"] = self._workspace_revision
        return self._client._execute_runtime_scenario(
            session=self,
            subject_ref=self._session_ref,
            policy_id=_POLICY_ID,
            parameters=projected,
        )


def _from_operation_payload(
    client: Any,
    payload: object,
) -> RuntimeSessionHandle | None:
    details = _runtime_fields(payload)
    if not isinstance(details, Mapping):
        return None
    if not all(
        field in details
        for field in ("session_ref", "pause_epoch", "workspace_revision")
    ):
        return None
    return RuntimeSessionHandle(
        client,
        session_ref=details["session_ref"],
        pause_epoch=details["pause_epoch"],
        workspace_revision=details["workspace_revision"],
    )


__all__ = ["RuntimeSessionHandle"]
