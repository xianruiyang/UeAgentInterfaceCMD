from __future__ import annotations

import dataclasses
from pathlib import Path
import unittest
from unittest import mock
from typing import Any

from network_transport_test_support import (
    build_frame,
    build_requirements,
    load_fixture,
    require_common_api,
    require_http_adapter_module,
)


class _FakeHttpExchange:
    def __init__(self, response: Any) -> None:
        self.response = response
        self.requests: list[Any] = []
        self.closed = False

    def exchange(self, request: Any) -> Any:
        self.requests.append(request)
        return self.response

    def close(self) -> None:
        self.closed = True


class _FakeSocket:
    def __init__(self) -> None:
        self.timeout: float | None = None

    def settimeout(self, value: float) -> None:
        self.timeout = value


class _FakeStdlibResponse:
    status = 200

    def getheaders(self) -> tuple[tuple[str, str], ...]:
        return ()

    def read(self) -> bytes:
        return b"reply"


class _FakeStdlibConnection:
    def __init__(self) -> None:
        self.sock: _FakeSocket | None = None
        self.events: list[str] = []

    def connect(self) -> None:
        self.events.append("connect")
        self.sock = _FakeSocket()

    def request(
        self,
        _method: str,
        _target: str,
        *,
        body: bytes | None,
        headers: dict[str, str],
    ) -> None:
        del body, headers
        self.events.append("request")
        if self.sock is None or self.sock.timeout != 19.0:
            raise AssertionError("io_timeout_not_set_before_request")

    def getresponse(self) -> _FakeStdlibResponse:
        self.events.append("response")
        return _FakeStdlibResponse()

    def close(self) -> None:
        self.events.append("close")


class HttpAdapterContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = load_fixture()

    def _build(
        self,
        *,
        status_code: int,
        body: bytes,
        headers: tuple[tuple[str, str], ...] = (
            ("Content-Type", "application/octet-stream"),
        ),
    ) -> tuple[Any, Any, Any, _FakeHttpExchange, Any]:
        api = require_common_api(self)
        http = require_http_adapter_module(self)
        response = http.HttpResponse(
            status_code=status_code,
            headers=headers,
            body=body,
        )
        exchange = _FakeHttpExchange(response)
        config = http.HttpAdapterConfig(
            base_url="http://127.0.0.1:17777",
            method="POST",
            route_path="/rpc",
            probe_path="/probe",
            auth_header="X-Transport-Token",
            auth_token="fixture-secret",
            connect_timeout_seconds=1.0,
            io_timeout_seconds=2.0,
        )
        adapter = http.HttpTransportAdapter(
            config=config,
            exchange=exchange,
        )
        frame = build_frame(api, self.fixture["frames"][0])
        requirements = build_requirements(
            api,
            self.fixture["requirements"]["portable"],
        )
        return api, http, adapter, exchange, (frame, requirements)

    def test_http_adapter_maps_private_exchange_to_common_delivery(
        self,
    ) -> None:
        api, _, adapter, exchange, inputs = self._build(
            status_code=200,
            body=b"\x10\x00reply",
        )
        frame, requirements = inputs

        delivery = adapter.send(frame, requirements)

        self.assertEqual(
            delivery.state,
            api.TransportDeliveryState.DELIVERED,
        )
        self.assertEqual(delivery.reply.frame.payload, b"\x10\x00reply")
        self.assertEqual(delivery.correlation_id, frame.correlation_id)
        self.assertEqual(len(exchange.requests), 1)
        request = exchange.requests[0]
        self.assertEqual(request.method, "POST")
        self.assertEqual(request.route_path, "/rpc")
        self.assertEqual(request.body, frame.payload)
        self.assertIn(
            ("X-Transport-Token", "fixture-secret"),
            request.headers,
        )
        public_fields = {
            field.name.casefold()
            for field in dataclasses.fields(delivery)
        }
        self.assertNotIn("status_code", public_fields)
        self.assertNotIn("headers", public_fields)

    def test_http_adapter_does_not_interpret_uai_or_leak_status(
        self,
    ) -> None:
        api, http, adapter, _, inputs = self._build(
            status_code=503,
            body=b'{"ok":false,"opaque":"unchanged"}',
        )
        frame, requirements = inputs

        delivery = adapter.send(frame, requirements)

        self.assertEqual(
            delivery.state,
            api.TransportDeliveryState.FAILED,
        )
        self.assertEqual(
            delivery.reply.frame.payload,
            b'{"ok":false,"opaque":"unchanged"}',
        )
        self.assertEqual(
            delivery.diagnostic.code,
            "remote_rejected",
        )
        self.assertFalse(hasattr(delivery, "status_code"))
        source = Path(http.__file__).read_text(encoding="utf-8")
        for forbidden in (
            "/api/exec",
            "json.loads",
            'get("ok")',
            '["command"]',
            "uai_core.contract",
            "OperationRequest",
            "Outcome",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(forbidden, source)

    def test_http_adapter_preserves_stable_transport_diagnostic_header(
        self,
    ) -> None:
        api, _, adapter, _, inputs = self._build(
            status_code=401,
            body=b"transport credential was rejected",
            headers=(
                ("content-type", "text/plain; charset=utf-8"),
                (
                    "x-transport-diagnostic",
                    "transport_authentication_failed",
                ),
            ),
        )
        frame, requirements = inputs

        delivery = adapter.send(frame, requirements)

        self.assertEqual(
            delivery.state,
            api.TransportDeliveryState.FAILED,
        )
        self.assertEqual(
            delivery.diagnostic.code,
            "transport_authentication_failed",
        )
        self.assertEqual(
            delivery.reply.frame.payload,
            b"transport credential was rejected",
        )

    def test_http_adapter_closes_only_its_owned_exchange(self) -> None:
        _, _, adapter, exchange, _ = self._build(
            status_code=200,
            body=b"reply",
        )

        adapter.close()
        adapter.close()

        self.assertTrue(exchange.closed)

    def test_no_auth_omits_secret_header_and_probe_stays_http_private(
        self,
    ) -> None:
        http = require_http_adapter_module(self)
        exchange = _FakeHttpExchange(
            http.HttpResponse(
                status_code=200,
                headers=(),
                body=b'{"ok":true}',
            )
        )
        adapter = http.HttpTransportAdapter(
            config=http.HttpAdapterConfig(
                base_url="http://127.0.0.1:17777",
                method="POST",
                route_path="/rpc",
                probe_path="/probe",
                connect_timeout_seconds=1.0,
                io_timeout_seconds=2.0,
                auth_header=None,
                auth_token=None,
            ),
            exchange=exchange,
        )

        self.assertTrue(adapter.probe())
        self.assertEqual(len(exchange.requests), 1)
        request = exchange.requests[0]
        self.assertEqual(request.method, "GET")
        self.assertEqual(request.route_path, "/probe")
        self.assertEqual(request.body, b"")
        self.assertFalse(
            any("token" in name.casefold() for name, _ in request.headers)
        )

    def test_connect_and_io_timeouts_remain_distinct(self) -> None:
        http = require_http_adapter_module(self)
        config = http.HttpAdapterConfig(
            base_url="http://127.0.0.1:17777",
            method="POST",
            route_path="/rpc",
            probe_path="/probe",
            connect_timeout_seconds=3.0,
            io_timeout_seconds=19.0,
        )
        self.assertEqual(config.connect_timeout_seconds, 3.0)
        self.assertEqual(config.io_timeout_seconds, 19.0)

    def test_stdlib_exchange_applies_timeout_by_lifecycle_phase(
        self,
    ) -> None:
        http = require_http_adapter_module(self)
        connection = _FakeStdlibConnection()
        with mock.patch.object(
            http.http.client,
            "HTTPConnection",
            return_value=connection,
        ) as constructor:
            exchange = http.StdlibHttpExchange(
                3.0,
                19.0,
            )
            response = exchange.exchange(
                http.HttpRequest(
                    base_url="http://127.0.0.1:17777",
                    method="POST",
                    route_path="/rpc",
                    headers=(),
                    body=b"request",
                )
            )

        constructor.assert_called_once_with(
            "127.0.0.1",
            17777,
            timeout=3.0,
        )
        self.assertEqual(
            connection.events,
            ["connect", "request", "response", "close"],
        )
        self.assertEqual(response.body, b"reply")


if __name__ == "__main__":
    unittest.main()
