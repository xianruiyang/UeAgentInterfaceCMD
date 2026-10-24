from __future__ import annotations

from pathlib import Path
import inspect
import unittest

import uai
from uai.connection_config import (
    AuthenticationSnapshot,
    ConnectionSnapshot,
)

try:
    from uai.commands import (
        CommandBinding,
        CommandBindingCatalog,
    )
    from uai.commands._runtime import ModelResultFieldBinding
except ImportError:
    CommandBinding = None
    CommandBindingCatalog = None
    ModelResultFieldBinding = None


BINDING_HASH = (
    "sha256:"
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
)


class _Transport:
    def __init__(self) -> None:
        self.closed = False

    def close(self) -> None:
        self.closed = True


class _ProtocolClient:
    def __init__(self, result: uai.Result) -> None:
        self.result = result
        self.calls: list[dict[str, object]] = []

    def invoke(self, **kwargs):
        self.calls.append(kwargs)
        return self.result


class _QueuedProtocolClient:
    def __init__(self, results: list[uai.Result]) -> None:
        self.results = list(results)
        self.calls: list[dict[str, object]] = []

    def invoke(self, **kwargs):
        self.calls.append(kwargs)
        return self.results.pop(0)


def _snapshot() -> ConnectionSnapshot:
    return ConnectionSnapshot(
        source_path=Path("fixture.toml"),
        format_version=1,
        transport="http",
        endpoint="http://127.0.0.1:8090",
        protocol_version="current",
        connect_timeout_seconds=1.0,
        io_timeout_seconds=2.0,
        authentication=AuthenticationSnapshot(mode="none"),
        transport_options={"http": {}},
    )


def _result(ok: bool) -> uai.Result:
    return uai.Result(
        {
            "schema": "uai.command.v1",
            "version": 1,
            "message_kind": "command_result",
            "correlation_id": "corr-returned",
            "request_id": "req-returned",
            "command_id": "fixture.echo_exact",
            "command_binding_hash": BINDING_HASH,
            "ok": ok,
            "payload": {"preserved": True},
            "error": (
                None
                if ok
                else {
                    "code": "fixture_failed",
                    "message": "fixture failed",
                }
            ),
        }
    )


def _operation_result(*, generation: int, terminal: bool = False) -> uai.Result:
    return uai.Result(
        {
            "schema": "uai.command.v1",
            "version": 1,
            "message_kind": "command_result",
            "correlation_id": "corr-operation",
            "request_id": "req-operation",
            "command_id": "fixture.operation",
            "command_binding_hash": BINDING_HASH,
            "ok": True,
            "payload": {
                "schema": "uai.long_running.snapshot.v1",
                "operation_ref": {
                    "operation_id": "operation",
                    "owner_lease_id": "lease",
                    "server_session_id": "session",
                },
                "descriptor_id": "descriptor",
                "binding_hash": "binding",
                "generation": generation,
                "phase": "terminal" if terminal else "running",
                "lifecycle_status": "released" if terminal else "running",
                "stop_requested": False,
                "terminal": terminal,
                "retry_safe": False,
                "latest_signal": {
                    "type_id": "fixture.signal",
                    "revision": generation,
                    "payload": {"value": generation, "content_hash": "business"},
                },
            },
            "error": None,
        }
    )


class SingleCommandExecuteContractTests(unittest.TestCase):
    def _client(
        self,
        result: uai.Result,
        *,
        status: str = "active",
        model_result_fields=(),
    ):
        self.assertIsNotNone(
            CommandBinding,
            "command_binding_model_missing",
        )
        self.assertIsNotNone(
            CommandBindingCatalog,
            "command_binding_catalog_missing",
        )
        binding = CommandBinding(
            command_id="fixture.echo_exact",
            binding_hash=BINDING_HASH,
            status=status,
            model_result_fields=model_result_fields,
        )
        catalog = CommandBindingCatalog((binding,))
        transport = _Transport()
        protocol = _ProtocolClient(result)
        try:
            client = uai.Client(
                connection=_snapshot(),
                transport=transport,
                protocol_client=protocol,
                binding_catalog=catalog,
            )
        except TypeError as exc:
            self.fail(f"client_protocol_injection_missing:{exc}")
        return client, protocol

    def test_native_observation_preserves_business_dictionary_keys(self) -> None:
        raw = dict(_result(True)._machine_response)
        entries = {"Hash": "business", "Identity": "value", "Asset_guid": ["first", "second"]}
        raw["payload"] = {
            "observation": {
                "entries": entries,
                "cvars": {"Hash": "console-value"},
                "merged_values": {
                    "Identity": {"values": {"Hash": "config-value"}, "binding_hash": "custody"},
                },
                "binding_hash": "custody",
                "default_output_file": "private/settings.hjson",
                "project_file": "private/project.uproject",
            },
            "binding_hash": "custody",
        }
        client, _protocol = self._client(uai.Result(raw))
        actual = client.execute("fixture.echo_exact", {})
        self.assertEqual(actual.payload, {
            "observation": {
                "entries": entries,
                "cvars": {"Hash": "console-value"},
                "merged_values": {"Identity": {"values": {"Hash": "config-value"}}},
            },
        })
        self.assertEqual(actual._machine_response, raw)

    def test_typed_literal_preserves_nested_members_without_exposing_custody(self) -> None:
        raw = dict(_result(True)._machine_response)
        literal = {"Hash": 7.5, "Identity": {"guid": "business-guid"}, "value_hash": [1, 2]}
        raw["payload"] = {
            "properties": {"State": {"value": {"literal": literal}, "binding_hash": "custody"}},
        }
        client, _protocol = self._client(uai.Result(raw))
        actual = client.execute("fixture.echo_exact", {})
        self.assertEqual(actual.payload, {"properties": {"State": {"value": {"literal": literal}}}})
        self.assertEqual(actual._machine_response, raw)
        actual.payload["properties"]["State"]["value"]["literal"]["Hash"] = 0
        self.assertEqual(actual.payload["properties"]["State"]["value"]["literal"]["Hash"], 7.5)

    def test_declared_model_result_fields_flatten_nested_payload(self) -> None:
        self.assertIsNotNone(ModelResultFieldBinding)
        raw = dict(_result(True)._machine_response)
        raw["payload"] = {
            "operation_id": "opaque-operation",
            "warnings": [{"code": "native_readback_differs", "severity": "warning"}],
            "projection": {
                "profile_id": "opaque-profile",
                "payload": {
                    "target_ref": "/Game/Test/Test.Test",
                    "outcome": "created",
                    "structure": {"keys": list(range(20))},
                    "verification": {
                        "observed_revision": 7,
                        "evidence_refs": ["opaque-evidence"],
                    },
                    "details": {
                        "label": "created asset",
                        "binding_hash": "opaque-binding",
                    },
                },
            },
        }
        result = uai.Result(raw)
        fields = (
            ModelResultFieldBinding(
                name="target",
                source_path=("projection", "payload", "target_ref"),
            ),
            ModelResultFieldBinding(
                name="outcome",
                source_path=("projection", "payload", "outcome"),
            ),
            ModelResultFieldBinding(
                name="details",
                source_path=("projection", "payload", "details"),
            ),
        )
        client, _protocol = self._client(
            result,
            model_result_fields=fields,
        )

        actual = client.execute("fixture.echo_exact", {})

        self.assertEqual(
            actual.payload,
            {
                "target": "/Game/Test/Test.Test",
                "outcome": "created",
                "details": {"label": "created asset"},
                "warnings": [{"code": "native_readback_differs", "severity": "warning"}],
            },
        )
        self.assertEqual(actual._machine_response, raw)

    def test_success_missing_declared_model_result_fails_closed(self) -> None:
        self.assertIsNotNone(ModelResultFieldBinding)
        result = _result(True)
        fields = (
            ModelResultFieldBinding(
                name="target",
                source_path=("projection", "payload", "target_ref"),
            ),
        )
        client, _protocol = self._client(
            result,
            model_result_fields=fields,
        )

        with self.assertRaises(uai.ProtocolError) as caught:
            client.execute("fixture.echo_exact", {})

        self.assertEqual(caught.exception.code, "model_result_field_missing")

    def test_failure_does_not_require_success_model_result_fields(self) -> None:
        self.assertIsNotNone(ModelResultFieldBinding)
        result = _result(False)
        fields = (
            ModelResultFieldBinding(
                name="target",
                source_path=("projection", "payload", "target_ref"),
            ),
        )
        client, _protocol = self._client(
            result,
            model_result_fields=fields,
        )

        actual = client.execute("fixture.echo_exact", {})

        self.assertFalse(actual.ok)
        self.assertEqual(actual.payload, {})
        self.assertEqual(actual.error, {"code": "fixture_failed"})

    def test_public_execute_signature_is_only_command_and_params(
        self,
    ) -> None:
        method = inspect.getattr_static(
            uai.Client,
            "execute",
            None,
        )
        self.assertIsNotNone(
            method,
            "client_execute_missing",
        )
        parameters = tuple(
            inspect.signature(method).parameters.values()
        )
        self.assertEqual(
            tuple(item.name for item in parameters),
            ("self", "command_id", "params"),
            "client_execute_public_signature_mismatch",
        )

    def test_execute_submits_exact_params_once(self) -> None:
        expected = _result(True)
        client, protocol = self._client(expected)
        params = {
            "unicode": "协议/蓝图",
            "large_integer": 9007199254740993,
            "nullable": None,
            "empty": {},
        }
        actual = client.execute("fixture.echo_exact", params)
        self.assertIsNot(actual, expected)
        self.assertEqual(actual.ok, expected.ok)
        self.assertEqual(actual.payload, expected.payload)
        self.assertEqual(actual.error, expected.error)
        self.assertEqual(len(protocol.calls), 1)
        call = protocol.calls[0]
        self.assertEqual(call["command_id"], "fixture.echo_exact")
        self.assertEqual(
            call["command_binding_hash"],
            BINDING_HASH,
        )
        self.assertEqual(call["params"], params)
        self.assertEqual(
            set(call),
            {
                "command_id",
                "command_binding_hash",
                "params",
                "correlation_id",
                "request_id",
            },
        )

    def test_operation_execute_and_lifecycle_use_owner_projection(self) -> None:
        self.assertIsNotNone(CommandBinding)
        self.assertIsNotNone(CommandBindingCatalog)
        initial = _operation_result(generation=0)
        status = _operation_result(generation=1, terminal=True)
        catalog = CommandBindingCatalog(
            (
                CommandBinding(
                    command_id="fixture.operation",
                    binding_hash=BINDING_HASH,
                    status="active",
                ),
                CommandBinding(
                    command_id="operation.status",
                    binding_hash=BINDING_HASH,
                    status="dormant",
                ),
            )
        )
        protocol = _QueuedProtocolClient([initial, status])
        client = uai.Client(
            connection=_snapshot(),
            transport=_Transport(),
            protocol_client=protocol,
            binding_catalog=catalog,
        )

        started = client.execute("fixture.operation", {})
        self.assertIsNotNone(started.operation)
        self.assertEqual(started.payload["lifecycle_status"], "running")
        self.assertNotIn("operation_ref", started.payload)
        self.assertNotIn("generation", started.payload)
        self.assertEqual(
            started.payload["latest_signal"],
            {
                "type_id": "fixture.signal",
                "payload": {"value": 0},
            },
        )

        observed = started.operation.status()
        self.assertIsNone(observed.operation)
        self.assertEqual(observed.payload["lifecycle_status"], "released")
        self.assertEqual(observed.payload["latest_signal"]["payload"]["value"], 1)
        self.assertNotIn("generation", observed.payload)
        self.assertEqual(protocol.calls[1]["command_id"], "operation.status")

    def test_server_failure_is_not_retried_or_rejudged(self) -> None:
        expected = _result(False)
        client, protocol = self._client(expected)
        actual = client.execute(
            "fixture.echo_exact",
            {"value": 1},
        )
        self.assertIsNot(actual, expected)
        self.assertEqual(actual.ok, expected.ok)
        self.assertEqual(actual.payload, expected.payload)
        self.assertEqual(actual.error, expected.error)
        self.assertFalse(actual.ok)
        self.assertEqual(len(protocol.calls), 1)

    def test_unknown_command_is_usage_error_without_delivery(
        self,
    ) -> None:
        client, protocol = self._client(_result(True))
        with self.assertRaises(uai.UsageError) as raised:
            client.execute("fixture.unknown", {})
        self.assertEqual(
            raised.exception.code,
            "command_binding_unknown",
        )
        self.assertEqual(protocol.calls, [])

if __name__ == "__main__":
    unittest.main()
