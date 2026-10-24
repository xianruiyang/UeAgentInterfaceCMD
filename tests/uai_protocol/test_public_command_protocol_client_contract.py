from __future__ import annotations

import json
from pathlib import Path
import unittest

import uai
from uai.network_transport import (
    TransportDelivery,
    TransportDeliveryState,
    TransportDiagnostic,
    TransportFrame,
    TransportReply,
)

try:
    from uai.uai_protocol import UaiCommandProtocolClient
except ImportError:
    UaiCommandProtocolClient = None


FIXTURE_PATH = (
    Path(__file__).resolve().parent
    / "fixtures"
    / "uai_command_v1_vectors.json"
)


class _Transport:
    def __init__(self, delivery_factory) -> None:
        self.delivery_factory = delivery_factory
        self.calls: list[tuple[TransportFrame, object]] = []

    def send(self, frame, requirements):
        self.calls.append((frame, requirements))
        return self.delivery_factory(frame)

    def close(self) -> None:
        pass


class PublicCommandProtocolClientContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(
            FIXTURE_PATH.read_text(encoding="utf-8")
        )

    def _client(self, delivery_factory):
        self.assertIsNotNone(
            UaiCommandProtocolClient,
            "public_command_protocol_client_missing",
        )
        transport = _Transport(delivery_factory)
        return UaiCommandProtocolClient(transport=transport), transport

    def _invoke(self, client):
        model = self.fixture["request"]["model"]
        return client.invoke(
            command_id=model["command_id"],
            command_binding_hash=model["command_binding_hash"],
            params=model["params"],
            correlation_id=model["correlation_id"],
            request_id=model["request_id"],
        )

    def test_one_transport_frame_round_trips_one_result(self) -> None:
        response = self.fixture["success"]["canonical"].encode("utf-8")

        def delivered(frame: TransportFrame) -> TransportDelivery:
            return TransportDelivery(
                correlation_id=frame.correlation_id,
                state=TransportDeliveryState.DELIVERED,
                reply=TransportReply(
                    frame=TransportFrame(
                        channel=frame.channel,
                        payload=response,
                        correlation_id=frame.correlation_id,
                        peer=frame.peer,
                    )
                ),
                diagnostic=None,
                attempts=1,
            )

        client, transport = self._client(delivered)
        result = self._invoke(client)
        self.assertTrue(result.ok)
        self.assertEqual(len(transport.calls), 1)
        frame, requirements = transport.calls[0]
        self.assertEqual(frame.channel, "uai.command")
        self.assertEqual(
            json.loads(frame.payload.decode("utf-8")),
            self.fixture["request"]["model"],
        )
        self.assertTrue(requirements.require_ordered)
        self.assertTrue(requirements.require_reliable)
        self.assertTrue(requirements.require_message_boundaries)
        self.assertTrue(requirements.require_request_reply)
        self.assertFalse(requirements.require_duplicate_suppression)

    def test_delivery_without_reply_is_transport_error_and_not_retried(
        self,
    ) -> None:
        def disconnected(frame: TransportFrame) -> TransportDelivery:
            return TransportDelivery(
                correlation_id=frame.correlation_id,
                state=TransportDeliveryState.DISCONNECTED,
                reply=None,
                diagnostic=TransportDiagnostic(
                    code="fixture_disconnected",
                    message="fixture disconnected",
                ),
                attempts=1,
            )

        client, transport = self._client(disconnected)
        with self.assertRaises(uai.TransportError) as raised:
            self._invoke(client)
        self.assertEqual(raised.exception.code, "fixture_disconnected")
        self.assertEqual(len(transport.calls), 1)

    def test_protocol_error_reply_remains_protocol_error(self) -> None:
        request = self.fixture["request"]["model"]
        diagnostic = {
            "code": "command_binding_mismatch", "message": "binding mismatch", "stage": "command_protocol",
            "name": "fixture.echo_exact", "json_pointer": "/command_id",
            "cause": {"code": "fixture_cause", "message": "Specific cause", "line": 7,
                      "actual_value": {"identity": "business identity", "hash": "business hash"}},
            "unchecked": [{"stage": "dispatch", "reason": "request rejected"}],
        }
        response = json.dumps(
            {
                "schema": "uai.command.v1",
                "version": 1,
                "message_kind": "protocol_error",
                "correlation_id": request["correlation_id"],
                "request_id": request["request_id"],
                "command_id": request["command_id"],
                "command_binding_hash": request[
                    "command_binding_hash"
                ],
                "error": {
                    "code": "command_binding_mismatch",
                    "diagnostic": diagnostic,
                },
            },
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")

        def rejected(frame: TransportFrame) -> TransportDelivery:
            return TransportDelivery(
                correlation_id=frame.correlation_id,
                state=TransportDeliveryState.FAILED,
                reply=TransportReply(
                    frame=TransportFrame(
                        channel=frame.channel,
                        payload=response,
                        correlation_id=frame.correlation_id,
                        peer=frame.peer,
                    )
                ),
                diagnostic=TransportDiagnostic(
                    code="remote_rejected",
                    message="remote rejected",
                ),
                attempts=1,
            )

        client, transport = self._client(rejected)
        with self.assertRaises(uai.ProtocolError) as raised:
            self._invoke(client)
        self.assertEqual(
            raised.exception.code,
            "command_binding_mismatch",
        )
        self.assertEqual(len(transport.calls), 1)

        self.assertEqual(raised.exception.diagnostic, diagnostic)
        self.assertNotIn("request_id", raised.exception.diagnostic)
        self.assertNotIn("command_binding_hash", raised.exception.diagnostic)

    def test_failed_delivery_with_non_protocol_reply_remains_transport_error(
        self,
    ) -> None:
        def rejected(frame: TransportFrame) -> TransportDelivery:
            return TransportDelivery(
                correlation_id=frame.correlation_id,
                state=TransportDeliveryState.FAILED,
                reply=TransportReply(
                    frame=TransportFrame(
                        channel=frame.channel,
                        payload=b"transport credential was rejected",
                        correlation_id=frame.correlation_id,
                        peer=frame.peer,
                    )
                ),
                diagnostic=TransportDiagnostic(
                    code="transport_authentication_failed",
                    message="remote transport rejected credentials",
                ),
                attempts=1,
            )

        client, transport = self._client(rejected)
        with self.assertRaises(uai.TransportError) as raised:
            self._invoke(client)
        self.assertEqual(
            raised.exception.code,
            "transport_authentication_failed",
        )
        self.assertEqual(len(transport.calls), 1)


if __name__ == "__main__":
    unittest.main()
