"""Typed client-side custody for long-running operation continuations."""

from __future__ import annotations

from collections.abc import Mapping
from contextlib import contextmanager
from contextvars import ContextVar
from copy import deepcopy
import hashlib
import math
import time
import uuid
from typing import Any, TYPE_CHECKING

from .errors import UsageError
from . import _operation_recovery as custody
from ._operation_recovery import recovery_path as _recovery_path

if TYPE_CHECKING:
    from .result import Result


_REF_FIELDS = ("operation_id", "owner_lease_id", "server_session_id")


def _require_ref(value: object) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        raise UsageError.at_source(
            code="operation_ref_invalid",
            message="operation continuation is not a mapping",
            facts={"property_path": "continuation", "expected_value": "mapping", "actual_value": type(value).__name__},
        )
    result = deepcopy(dict(value))
    if any(
        not isinstance(result.get(field), str) or not result[field].strip()
        for field in _REF_FIELDS
    ):
        raise UsageError.at_source(
            code="operation_ref_invalid",
            message="operation continuation is incomplete",
            facts={"property_path": "continuation", "invalid_fields": [field for field in _REF_FIELDS if not isinstance(result.get(field), str) or not result[field].strip()]},
        )
    return result


class OperationHandle:
    """Owns an opaque operation reference and its latest generation."""

    __slots__ = (
        "_client",
        "_operation_ref",
        "_generation",
        "_released",
        "_runtime_session",
        "_terminal_receipt",
        "_recovery_records",
    )

    def __init__(
        self,
        client: Any,
        operation_ref: Mapping[str, Any],
        generation: int | None = None,
    ) -> None:
        self._client = client
        self._operation_ref = _require_ref(operation_ref)
        self._generation = None
        self._released = False
        self._runtime_session = None
        self._terminal_receipt = None
        self._recovery_records = {}
        if generation is not None:
            self._set_generation(generation)

    @property
    def released(self) -> bool:
        return self._released

    def __repr__(self) -> str:
        return f"OperationHandle(name={self.recovery_name!r}, released={self._released!r})"

    @property
    def recovery_name(self) -> str | None:
        return next(iter(self._recovery_records), None)

    def _persist(self, payload=None):
        for name, saved in tuple(self._recovery_records.items()):
            updated = custody.with_observation(saved, payload or {})
            updated["state"] = self._machine_state()
            updated["released"] = self._released
            custody.store(self._client, name, updated,
                          expected_ref=saved.get("state", {}).get("operation_ref"))
            self._recovery_records[name] = updated

    @property
    def runtime_session(self):
        return self._runtime_session

    def _set_runtime_session(self, session) -> None:
        self._runtime_session = session
        self._persist()

    def _machine_state(self) -> dict[str, Any]:
        state = {
            "operation_ref": deepcopy(self._operation_ref),
            "generation": self._generation,
        }
        if self._runtime_session is not None:
            state["runtime_session"] = self._runtime_session._machine_state()
        if self._terminal_receipt is not None:
            state["terminal_receipt"] = deepcopy(self._terminal_receipt)
        return state

    def _set_generation(self, value: object) -> None:
        if isinstance(value, bool) or not isinstance(value, int):
            raise UsageError(
                code="operation_generation_invalid",
                message="operation generation must be an integer",
            )
        self._generation = value

    def _update(self, result: "Result") -> "Result":
        payload = result._machine_payload
        if isinstance(payload, Mapping):
            ref = payload.get("operation_ref")
            if ref is not None:
                self._operation_ref = _require_ref(ref)
            if "generation" in payload:
                self._set_generation(payload["generation"])
            if self._runtime_session is not None:
                self._runtime_session._update_from_payload(payload)
            else:
                from .runtime_session import _from_operation_payload

                self._runtime_session = _from_operation_payload(self._client, payload)
            if result.ok:
                self._persist(payload)
        return result

    def _execute(self, command_id: str, params: Mapping[str, Any]) -> "Result":
        if self._released:
            raise UsageError(
                code="operation_handle_released",
                message="operation handle has already been released",
            )
        return self._update(
            self._client._execute_operation_lifecycle(command_id, dict(params))
        )

    def status(self) -> "Result":
        return self._execute(
            "operation.status", {"operation_ref": self._operation_ref}
        )

    def checkpoint(self, name: str) -> str:
        """Add a readable recovery alias; custody is already saved automatically."""
        if self._released:
            raise UsageError(code="operation_handle_released",
                             message="cannot checkpoint a released operation")
        record = deepcopy(next(iter(self._recovery_records.values()), {
            "schema": "uai.operation.custody/2", "state": {}, "released": False,
        }))
        record["state"] = self._machine_state()
        custody.store(self._client, name, record, expected_ref=self._operation_ref)
        self._recovery_records[name] = record
        return name

    def resume(self) -> "Result":
        if self._generation is None:
            raise UsageError(
                code="operation_generation_missing",
                message="operation generation is not available",
            )
        return self._execute(
            "operation.resume",
            {
                "operation_ref": self._operation_ref,
                "expected_generation": self._generation,
            },
        )

    def cancel(self, reason: str) -> "Result":
        if not isinstance(reason, str) or not reason.strip():
            raise UsageError(
                code="operation_cancel_reason_missing",
                message="operation cancellation reason is required",
            )
        return self._execute(
            "operation.cancel",
            {"operation_ref": self._operation_ref, "reason": reason},
        )

    def receipt(self) -> "Result":
        if self._released and self._terminal_receipt is not None:
            from .result import Result
            from .artifact import _from_payload
            return Result(deepcopy(self._terminal_receipt), long_running=True,
                          artifacts=_from_payload(self._client, self._terminal_receipt.get("payload", {})),
                          runtime_session=self._runtime_session)
        result = self._execute(
            "operation.receipt", {"operation_ref": self._operation_ref}
        )
        if result.ok and result._machine_payload.get("schema") == "uai.long_running.receipt.v1":
            self._terminal_receipt = deepcopy(dict(result._machine_response))
            self._persist(result._machine_payload)
        return result

    def reconcile(self) -> "Result":
        if self._generation is None:
            raise UsageError(
                code="operation_generation_missing",
                message="operation generation is not available",
            )
        return self._execute(
            "operation.reconcile",
            {
                "operation_ref": self._operation_ref,
                "expected_generation": self._generation,
            },
        )

    def release(self) -> "Result":
        if self._released:
            return self.receipt()
        # Keep the business receipt before the server removes its record.
        if self._terminal_receipt is None:
            receipt = self.receipt()
            if not receipt.ok:
                return receipt
        result = self._execute(
            "operation.release", {"operation_ref": self._operation_ref}
        )
        if result.ok:
            self._released = True
            self._persist(result._machine_payload)
        return result

    def wait(self, *, timeout=None, poll_seconds=0.1, until=None, on_observation=None):
        """Start accepted work once, then collect progress without replaying it.

        ``until`` can observe a domain readiness condition for a persistent
        session. Completion returns the terminal receipt, including failures.
        A timeout retains custody and does not cancel native work.
        """
        if timeout is not None and (isinstance(timeout, bool) or not isinstance(timeout, (int, float))
                                    or not math.isfinite(timeout) or timeout <= 0):
            raise UsageError(code="operation_timeout_invalid", message="timeout must be positive or None")
        if (isinstance(poll_seconds, bool) or not isinstance(poll_seconds, (int, float))
                or not math.isfinite(poll_seconds) or poll_seconds <= 0):
            raise UsageError(code="operation_poll_interval_invalid", message="poll_seconds must be positive")
        if self._released:
            return self.receipt()
        deadline = None if timeout is None else time.monotonic() + timeout
        result = self.status()
        while result.ok:
            payload = result._machine_payload
            if on_observation is not None:
                on_observation(result)
            if payload.get("terminal"):
                return self.receipt()
            if until is not None and until(result):
                return result
            if deadline is not None and time.monotonic() >= deadline:
                raise UsageError(code="operation_wait_timeout",
                                 message="the operation is still pending; recover the saved operation to continue",
                                 diagnostic={"recovery_name": self.recovery_name, "retry_safe": False})
            if payload.get("error_code") == "native_stop_pending_deadline_exceeded":
                return result
            result = self.resume()
            if result.ok and not result._machine_payload.get("terminal"):
                time.sleep(poll_seconds)
        return result

    def finish(self, *, timeout=None, poll_seconds=0.1, on_observation=None):
        """Collect the terminal receipt and release this operation's resources."""
        receipt = self.wait(timeout=timeout, poll_seconds=poll_seconds, on_observation=on_observation)
        if not receipt.ok or receipt._machine_payload.get("schema") != "uai.long_running.receipt.v1":
            return receipt
        released = self.release()
        return receipt if released.ok else released

    def close(self, reason="operation close", *, timeout=None, poll_seconds=0.1, on_observation=None):
        """Cancel owned work, drain it, preserve its receipt and release custody."""
        if not self._released:
            current = self.status()
            if not current.ok:
                return current
            if not current._machine_payload.get("terminal"):
                stopped = self.cancel(reason)
                if not stopped.ok:
                    return stopped
        return self.finish(timeout=timeout, poll_seconds=poll_seconds, on_observation=on_observation)


class OperationNamespace:
    """Model-facing operation namespace with typed continuation custody."""

    __slots__ = ("_client", "_generated", "_requested_name")

    def __init__(self, client: Any, generated: Any) -> None:
        self._client = client
        self._generated = generated
        self._requested_name = ContextVar("uai_operation_recovery_name", default=None)

    @contextmanager
    def named(self, name):
        """Choose a readable name before submitting an operation-producing call."""
        _recovery_path(self._client, name)
        token = self._requested_name.set(name)
        try:
            yield
        finally:
            self._requested_name.reset(token)

    def _begin_request(self, command_id, request_id, params):
        name = self._requested_name.get() or "operation-" + uuid.uuid4().hex[:16]
        record = custody.request_record(command_id, request_id, params.get("subject_ref", params.get("target")))
        custody.store(self._client, name, record, reserve=True)
        return name, record

    def _accept_result(self, name, record, result):
        if result.operation is None:
            record["phase"] = "completed"
            record["released"] = True
            record["response"] = deepcopy(dict(result._machine_response))
            custody.store(self._client, name, record)
            return
        result.operation._recovery_records[name] = record
        result.operation._persist(result._machine_payload)

    def from_result(self, result: "Result") -> OperationHandle:
        if not isinstance(result, object) or not hasattr(result, "_machine_payload"):
            raise UsageError(
                code="operation_result_invalid",
                message="result must be a UAI SDK Result",
            )
        existing = result.operation
        if existing is not None:
            return existing
        payload = result._machine_payload
        if not isinstance(payload, Mapping):
            raise UsageError(
                code="operation_result_invalid",
                message="result does not contain an operation snapshot",
            )
        return OperationHandle(
            self._client,
            _require_ref(payload.get("operation_ref")),
            payload.get("generation"),
        )

    def _from_machine_state(self, state: Mapping[str, Any]) -> OperationHandle:
        if not isinstance(state, Mapping):
            raise UsageError(
                code="operation_state_invalid",
                message="operation machine state must be a mapping",
            )
        handle = OperationHandle(
            self._client,
            _require_ref(state.get("operation_ref")),
            state.get("generation"),
        )
        runtime_state = state.get("runtime_session")
        if runtime_state is not None:
            if not isinstance(runtime_state, Mapping):
                raise UsageError(code="operation_state_invalid", message="invalid runtime session custody")
            from .runtime_session import RuntimeSessionHandle

            handle._set_runtime_session(RuntimeSessionHandle._from_machine_state(self._client, runtime_state))
        receipt = state.get("terminal_receipt")
        if isinstance(receipt, Mapping):
            payload = receipt.get("payload", {})
            if (receipt.get("ok") is True and isinstance(payload, Mapping)
                    and payload.get("schema") == "uai.long_running.receipt.v1"
                    and payload.get("operation_ref") == handle._operation_ref):
                handle._terminal_receipt = deepcopy(dict(receipt))
        return handle

    def recover(self, name: str) -> OperationHandle:
        """Recover the original operation, including a lost initial response."""
        saved = custody.load(self._client, name)
        state = saved.get("state", {})
        if not isinstance(state, Mapping) or not state.get("operation_ref"):
            request = saved.get("request", {})
            if not request.get("request_id"):
                raise UsageError(code="operation_takeover_required",
                                 message=f"{name!r} was discovered without custody; explicitly take it over")
            if saved.get("released"):
                raise UsageError(code="operation_request_completed",
                                 message="this request completed without a retained operation")
            result = self._client._execute_operation_lifecycle("operation.recover", request)
            if not result.ok:
                self._raise_recovery_error(name, result)
            state = result._machine_payload
        handle = self._from_machine_state(state)
        handle._recovery_records[name] = saved
        if saved.get("released") and handle._terminal_receipt is not None:
            handle._released = True
            return handle
        result = handle.status()
        if not result.ok:
            if (result._machine_response.get("error", {}).get("code") == "operation_not_found"
                    and handle._terminal_receipt is not None
                    and handle._terminal_receipt.get("payload", {}).get("cleanup_complete") is True):
                handle._released = True
                handle._persist()
                return handle
            self._raise_recovery_error(name, result)
        return handle

    @staticmethod
    def _raise_recovery_error(name, result):
        diagnostic = deepcopy((result.error or {}).get("diagnostic", {}))
        diagnostic.update(recovery_name=name, recovery_status="unconfirmed",
                          retry_safe=False, cause_code=(result.error or {}).get("code"))
        raise UsageError(code="operation_recovery_unconfirmed",
                         message="the server could not confirm this custody; no action was replayed",
                         diagnostic=diagnostic)

    def pending(self):
        """List readable local recovery names, including requests with no reply."""
        directory = _recovery_path(self._client, "unused").parent
        entries = []
        for path in sorted(directory.glob("*.json")):
            record = custody.load(self._client, path.stem)
            if not record.get("released"):
                entries.append(custody.summary(path.stem, record))
        return entries

    def discover(self):
        """Find retained operations for the authenticated local principal.

        Discovery does not acquire custody or restart any work. This principal
        is shared by authenticated local clients, not a per-agent identity.
        """
        result = self._client._execute_operation_lifecycle("operation.discover", {})
        result.raise_for_error()
        entries = []
        for entry in result._machine_payload.get("operations", []):
            operation_id = entry["operation_id"]
            name = "discovered-" + hashlib.sha256(operation_id.encode("utf-8")).hexdigest()[:16]
            path = _recovery_path(self._client, name)
            record = custody.load(self._client, name) if path.exists() else {
                "schema": "uai.operation.custody/2", "state": {}, "released": False,
                "request": {"command_id": entry.get("command_id", "")},
            }
            if record.get("discovered_operation_id", operation_id) != operation_id:
                raise UsageError(code="operation_discovery_name_collision",
                                 message="the local discovery name belongs to another operation")
            record["discovered_operation_id"] = operation_id
            record["subject_ref"] = entry.get("subject_ref", "")
            record = custody.with_observation(record, entry)
            custody.store(self._client, name, record,
                          expected_ref=record.get("state", {}).get("operation_ref"))
            entries.append(custody.summary(name, record))
        return entries

    def takeover(self, name):
        """Explicitly replace custody; the previous handle can no longer mutate."""
        saved = custody.load(self._client, name)
        operation_id = saved.get("discovered_operation_id") or saved.get("state", {}).get("operation_ref", {}).get("operation_id")
        if not operation_id:
            raise UsageError(code="operation_takeover_unavailable",
                             message="recover the pending request or discover its operation first")
        result = self._client._execute_operation_lifecycle("operation.takeover", {"operation_id": operation_id})
        result.raise_for_error()
        handle = result.operation or self.from_result(result)
        updated = custody.with_observation(saved, result._machine_payload)
        updated["state"] = handle._machine_state()
        updated["released"] = False
        custody.store(self._client, name, updated, replace=True)
        handle._recovery_records[name] = updated
        return handle

    def forget_checkpoint(self, name: str) -> None:
        """Remove local custody only; does not cancel or release the server operation."""
        _recovery_path(self._client, name).unlink(missing_ok=True)

    def plan_execute(self, steps, on_error, atomicity):
        return self._generated.plan_execute(steps, on_error, atomicity)

__all__ = ["OperationHandle", "OperationNamespace"]
