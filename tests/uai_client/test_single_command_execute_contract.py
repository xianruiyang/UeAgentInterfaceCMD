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
except ImportError:
    CommandBinding = None
    CommandBindingCatalog = None


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


class SingleCommandExecuteContractTests(unittest.TestCase):
    def _client(self, result: uai.Result, *, status: str = "active"):
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
        self.assertIs(actual, expected)
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

    def test_server_failure_is_not_retried_or_rejudged(self) -> None:
        expected = _result(False)
        client, protocol = self._client(expected)
        actual = client.execute(
            "fixture.echo_exact",
            {"value": 1},
        )
        self.assertIs(actual, expected)
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

    def test_dormant_command_requires_explicit_user_confirmation(self) -> None:
        client, protocol = self._client(_result(True), status="dormant")
        with self.assertRaises(uai.UsageError) as exact_error:
            client.execute_exact(
                "fixture.echo_exact", {}, contract_hash=BINDING_HASH
            )
        self.assertEqual(
            exact_error.exception.code,
            "dormant_command_confirmation_required",
        )
        with self.assertRaises(uai.UsageError) as confirmation_error:
            client.execute_dormant(
                "fixture.echo_exact",
                {},
                contract_hash=BINDING_HASH,
                user_confirmed=False,
            )
        self.assertEqual(
            confirmation_error.exception.code,
            "dormant_command_confirmation_required",
        )
        self.assertEqual(protocol.calls, [])

    def test_confirmed_dormant_command_forwards_once(self) -> None:
        expected = _result(True)
        client, protocol = self._client(expected, status="dormant")
        actual = client.execute_dormant(
            "fixture.echo_exact",
            {"value": 1},
            contract_hash=BINDING_HASH,
            user_confirmed=True,
        )
        self.assertIs(actual, expected)
        self.assertEqual(len(protocol.calls), 1)
        self.assertEqual(protocol.calls[0]["command_id"], "fixture.echo_exact")


if __name__ == "__main__":
    unittest.main()
