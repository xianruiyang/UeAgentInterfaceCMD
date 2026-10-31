"""PIE flow orchestration. UE owns execution; SDK owns continuation custody."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from copy import deepcopy

from .errors import Error, UsageError
from .operation import _recovery_path
from .result import Result
from .artifact import _from_payload as _artifacts_from_payload


def _flow_result(client, result, diagnostics=()):
    raw = deepcopy(dict(result._machine_response))
    operation_payload = raw.get("payload", {})
    signal = operation_payload.get("latest_signal", {}).get("payload", {})
    flow = deepcopy(signal.get("flow"))
    if not isinstance(flow, dict):
        flow = {
            "execution": {"status": "state_unknown"},
            "results": [],
            "snapshot": {"paused": False, "updated": False},
            "diagnostics": ["flow result unavailable; recover the session without replaying"],
        }
    flow.setdefault("diagnostics", []).extend(diagnostics)
    artifacts = _artifacts_from_payload(client, flow)
    locators = {}

    def associate(value):
        if isinstance(value, dict):
            artifact = value.get("artifact_ref")
            if isinstance(artifact, Mapping) and isinstance(artifact.get("locator"), str):
                locator = artifact["locator"]
                value["artifact_index"] = locators.setdefault(locator, len(locators))
            for child in tuple(value.values()):
                associate(child)
        elif isinstance(value, list):
            for child in value:
                associate(child)

    associate(flow)
    raw["payload"] = flow
    raw["ok"] = (result.ok and flow.get("execution", {}).get("status") == "succeeded"
                 and flow.get("snapshot", {}).get("paused") is True
                 and flow.get("snapshot", {}).get("updated") is True
                 and not flow.get("diagnostics"))
    if not raw["ok"] and not raw.get("error"):
        # A successful receipt call can report a failed operation. Preserve its
        # actual failure code; flow diagnostics/results already retain details.
        raw["error"] = {"code": operation_payload.get("error_code") or "pie_flow_incomplete",
                        "retry_safe": operation_payload.get("retry_safe", False)}
        if isinstance(operation_payload.get("diagnostic"), Mapping):
            raw["error"]["diagnostic"] = deepcopy(operation_payload["diagnostic"])
    return Result(raw, artifacts=artifacts)


class PieSession:
    """A paused PIE with automatic per-flow lifecycle and durable recovery."""

    def __init__(self, client, operation, name):
        self._client = client
        self._operation = operation
        self._name = name
        self._flow_name = name + "-flow"

    @property
    def snapshot(self):
        result = self._operation.status()
        if not result.ok:
            return result
        from .runtime_session import _runtime_fields
        fields = _runtime_fields(result._machine_payload) or {}
        return {"path": fields.get("workspace_path"),
                "session_active": fields.get("phase") == "active"}

    def run(self, steps: Sequence[Mapping], *, limits=None, watch_refs=(), unwatch_refs=()):
        """Run once, pause, return ordered results. Never replay a pending flow."""
        if _recovery_path(self._client, self._flow_name).exists():
            raise UsageError(code="pie_flow_pending", message="use session.resume() to collect the pending flow; do not replay it")
        parameters = {"steps": deepcopy(list(steps))}
        if limits is not None:
            parameters["limits"] = deepcopy(limits)
        if watch_refs:
            parameters["watch_refs"] = deepcopy(list(watch_refs))
        if unwatch_refs:
            parameters["unwatch_refs"] = deepcopy(list(unwatch_refs))
        runtime = self._operation.runtime_session
        if runtime is None:
            raise UsageError(code="pie_session_not_ready", message="PIE has no paused runtime session")
        with self._client.operation.named(self._flow_name):
            result = runtime.scenario_execute(parameters=parameters)
        if result.operation is None:
            return result
        return self._finish_flow(result.operation)

    def _finish_flow(self, operation, *, closing=False):
        result = (operation.close("PIE session close") if closing else operation.finish())
        diagnostics = []
        if operation.runtime_session is not None:
            self._operation._set_runtime_session(operation.runtime_session)
        if operation.released:
            self._client.operation.forget_checkpoint(self._flow_name)
        else:
            diagnostics.append("flow completion is unconfirmed; recovery custody retained")
        return _flow_result(self._client, result, diagnostics)

    def resume(self):
        """Collect an interrupted flow without resubmitting its actions."""
        return self._finish_flow(self._client.operation.recover(self._flow_name))

    def close(self):
        """Cancel any pending flow and end this PIE session through its owner."""
        if _recovery_path(self._client, self._flow_name).exists():
            flow = self._client.operation.recover(self._flow_name)
            result = self._finish_flow(flow, closing=True)
            if _recovery_path(self._client, self._flow_name).exists():
                return result
        result = self._operation.close("PIE session close")
        if self._operation.released:
            self._client.operation.forget_checkpoint(self._name)
        return result


class PieNamespace:
    def __init__(self, client):
        self._client = client

    def start(self, name="pie-current", *, instance=0, local_player_index=0,
              viewport_width=None, viewport_height=None):
        """Start paused PIE with optional viewport dimensions in pixels (default 1280x720)."""
        if _recovery_path(self._client, name).exists():
            raise UsageError(code="pie_session_exists", message="recover the existing PIE session or choose another name")
        parameters = {"local_player_index": local_player_index}
        if viewport_width is not None:
            parameters["viewport_width"] = viewport_width
        if viewport_height is not None:
            parameters["viewport_height"] = viewport_height
        with self._client.operation.named(name):
            result = self._client.editor.session(
                "runtime_preview", f"runtime-subject:pie:{instance}",
                "policy:runtime-session:pie-debug/v2", parameters)
        if result.operation is None:
            result.raise_for_error()
            raise UsageError.at_source(code="pie_start_failed", message="The session reply did not provide an operation handle.",
                             facts={"stage": "session_start", "actual_present": False})
        operation = result.operation
        ready = operation.wait(until=lambda observation:
                               observation.payload.get("latest_signal", {}).get("payload", {}).get("phase") == "active")
        terminal = ready.payload.get("schema") == "uai.long_running.receipt.v1"
        if not ready.ok or operation.runtime_session is None or terminal:
            ready.raise_for_error()
            diagnostic = ready.payload.get("diagnostic")
            if terminal and isinstance(diagnostic, Mapping) and diagnostic:
                raise Error(
                    code=ready.payload.get("error_code") or diagnostic.get("code") or "pie_start_failed",
                    message=f"PIE launch failed; inspect or close the saved result with client.pie.recover({name!r})",
                    diagnostic=diagnostic,
                )
            raise UsageError.at_source(code="pie_start_not_ready", message="PIE did not become ready; recover the saved session to inspect or close it",
                             facts={"stage": "session_ready", "terminal_status": "terminal" if terminal else "pending",
                                         "recovery_action": f"client.pie.recover({name!r})"})
        return PieSession(self._client, operation, name)

    def recover(self, name="pie-current"):
        return PieSession(self._client, self._client.operation.recover(name), name)
