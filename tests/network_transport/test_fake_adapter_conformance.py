from __future__ import annotations

import unittest
from typing import Any

from network_transport_test_support import (
    build_capabilities,
    build_frame,
    build_requirements,
    load_fixture,
    require_common_api,
)


class _RecordingEndpoint:
    def __init__(self, api: Any) -> None:
        self.api = api
        self.frames: list[Any] = []

    def exchange(self, frame: Any) -> Any:
        self.frames.append(frame)
        reply_frame = self.api.TransportFrame(
            channel=frame.channel,
            payload=frame.payload,
            correlation_id=frame.correlation_id,
            peer=frame.peer,
        )
        return self.api.TransportReply(frame=reply_frame)


class _FakeAdapterBase:
    def __init__(
        self,
        api: Any,
        capabilities: Any,
        endpoint: _RecordingEndpoint,
    ) -> None:
        self.api = api
        self.capabilities = capabilities
        self.endpoint = endpoint
        self.send_attempts = 0
        self.next_failure_state: Any | None = None
        self.closed = False

    def send(self, frame: Any, requirements: Any) -> Any:
        self.api.bind_capabilities(
            self.capabilities,
            requirements,
        )
        self.send_attempts += 1
        if self.closed:
            return self._failure(
                frame,
                self.api.TransportDeliveryState.DISCONNECTED,
                "transport_closed",
            )
        if len(frame.payload) > self.capabilities.max_frame_bytes:
            return self._failure(
                frame,
                self.api.TransportDeliveryState.UNSUPPORTED,
                "frame_too_large",
            )
        if self.next_failure_state is not None:
            return self._failure(
                frame,
                self.next_failure_state,
                f"transport_{self.next_failure_state.value}",
            )
        return self._deliver(frame)

    def _deliver(self, frame: Any) -> Any:
        reply = self.endpoint.exchange(frame)
        return self.api.TransportDelivery(
            correlation_id=frame.correlation_id,
            state=self.api.TransportDeliveryState.DELIVERED,
            reply=reply,
            diagnostic=None,
            attempts=1,
        )

    def close(self) -> None:
        self.closed = True

    def _failure(
        self,
        frame: Any,
        state: Any,
        code: str,
    ) -> Any:
        diagnostic = self.api.TransportDiagnostic(
            code=code,
            message=code,
        )
        return self.api.TransportDelivery(
            correlation_id=frame.correlation_id,
            state=state,
            reply=None,
            diagnostic=diagnostic,
            attempts=1,
        )


class _FakeStreamAdapter(_FakeAdapterBase):
    def __init__(
        self,
        api: Any,
        capabilities: Any,
        endpoint: _RecordingEndpoint,
        chunk_sizes: list[int],
    ) -> None:
        super().__init__(api, capabilities, endpoint)
        self.chunk_sizes = chunk_sizes

    def _deliver(self, frame: Any) -> Any:
        payload = frame.payload
        chunks: list[bytes] = []
        offset = 0
        index = 0
        while offset < len(payload):
            width = self.chunk_sizes[index % len(self.chunk_sizes)]
            chunks.append(payload[offset : offset + width])
            offset += width
            index += 1
        reconstructed = self.api.TransportFrame(
            channel=frame.channel,
            payload=b"".join(chunks),
            correlation_id=frame.correlation_id,
            peer=frame.peer,
        )
        return super()._deliver(reconstructed)


class _FakeDatagramAdapter(_FakeAdapterBase):
    pass


class FakeAdapterConformanceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = load_fixture()

    def _build(
        self,
        kind: str,
    ) -> tuple[Any, Any, Any, _RecordingEndpoint]:
        api = require_common_api(self)
        endpoint = _RecordingEndpoint(api)
        capabilities = build_capabilities(
            api,
            self.fixture["capabilities"][kind],
        )
        if kind == "stream":
            adapter = _FakeStreamAdapter(
                api,
                capabilities,
                endpoint,
                self.fixture["stream_chunk_sizes"],
            )
        else:
            adapter = _FakeDatagramAdapter(
                api,
                capabilities,
                endpoint,
            )
        requirements = build_requirements(
            api,
            self.fixture["requirements"]["portable"],
        )
        return api, adapter, requirements, endpoint

    def test_same_frame_runs_through_fake_stream(self) -> None:
        api, adapter, requirements, endpoint = self._build("stream")
        frame = build_frame(api, self.fixture["frames"][0])

        delivery = adapter.send(frame, requirements)

        self.assertEqual(
            delivery.state,
            api.TransportDeliveryState.DELIVERED,
        )
        self.assertEqual(len(endpoint.frames), 1)
        self.assertEqual(endpoint.frames[0].payload, frame.payload)
        self.assertEqual(delivery.correlation_id, frame.correlation_id)

    def test_same_frame_runs_through_fake_datagram(self) -> None:
        api, adapter, requirements, endpoint = self._build("datagram")
        frame = build_frame(api, self.fixture["frames"][0])

        delivery = adapter.send(frame, requirements)

        self.assertEqual(
            delivery.state,
            api.TransportDeliveryState.DELIVERED,
        )
        self.assertEqual(len(endpoint.frames), 1)
        self.assertEqual(endpoint.frames[0].payload, frame.payload)
        self.assertEqual(delivery.correlation_id, frame.correlation_id)

    def test_stream_reassembles_partial_chunks_before_one_delivery(
        self,
    ) -> None:
        api, adapter, requirements, endpoint = self._build("stream")
        frame = build_frame(api, self.fixture["frames"][0])

        adapter.send(frame, requirements)

        self.assertEqual(adapter.send_attempts, 1)
        self.assertEqual(len(endpoint.frames), 1)
        self.assertEqual(endpoint.frames[0].payload, frame.payload)

    def test_incompatible_datagram_binding_fails_before_delivery(
        self,
    ) -> None:
        api, adapter, _, endpoint = self._build("datagram")
        strict = build_requirements(
            api,
            self.fixture["requirements"]["strict"],
        )
        frame = build_frame(api, self.fixture["frames"][0])

        with self.assertRaises(api.TransportBindingError):
            adapter.send(frame, strict)

        self.assertEqual(adapter.send_attempts, 0)
        self.assertEqual(endpoint.frames, [])

    def test_oversize_backpressure_timeout_disconnect_are_explicit(
        self,
    ) -> None:
        api, adapter, requirements, endpoint = self._build("stream")
        base = build_frame(api, self.fixture["frames"][0])
        oversize = api.TransportFrame(
            channel=base.channel,
            payload=b"x" * 65,
            correlation_id=base.correlation_id,
            peer=base.peer,
        )

        too_large = adapter.send(oversize, requirements)
        self.assertEqual(
            too_large.state,
            api.TransportDeliveryState.UNSUPPORTED,
        )
        for state in (
            api.TransportDeliveryState.BACKPRESSURED,
            api.TransportDeliveryState.TIMED_OUT,
            api.TransportDeliveryState.DISCONNECTED,
            api.TransportDeliveryState.FAILED,
        ):
            with self.subTest(state=state):
                adapter.next_failure_state = state
                delivery = adapter.send(base, requirements)
                self.assertEqual(delivery.state, state)
                self.assertIsNone(delivery.reply)
        self.assertEqual(endpoint.frames, [])

    def test_transport_never_retries_opaque_effectful_frame(self) -> None:
        api, adapter, requirements, endpoint = self._build("stream")
        frame = build_frame(api, self.fixture["frames"][1])
        adapter.next_failure_state = (
            api.TransportDeliveryState.DISCONNECTED
        )

        delivery = adapter.send(frame, requirements)

        self.assertEqual(
            delivery.state,
            api.TransportDeliveryState.DISCONNECTED,
        )
        self.assertEqual(delivery.attempts, 1)
        self.assertEqual(adapter.send_attempts, 1)
        self.assertEqual(endpoint.frames, [])

    def test_close_is_client_owned_idempotent_and_blocks_delivery(self) -> None:
        api, adapter, requirements, endpoint = self._build("stream")
        frame = build_frame(api, self.fixture["frames"][0])

        adapter.close()
        adapter.close()
        delivery = adapter.send(frame, requirements)

        self.assertTrue(adapter.closed)
        self.assertEqual(
            delivery.state,
            api.TransportDeliveryState.DISCONNECTED,
        )
        self.assertEqual(endpoint.frames, [])


if __name__ == "__main__":
    unittest.main()
