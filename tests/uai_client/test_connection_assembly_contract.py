from __future__ import annotations

import importlib
import unittest


class _Snapshot:
    transport = "http"


class _Transport:
    def __init__(self) -> None:
        self.close_calls = 0

    def close(self) -> None:
        self.close_calls += 1


class ConnectionAssemblyContractTests(unittest.TestCase):
    def _assembler_type(self):
        try:
            module = importlib.import_module("uai.connection")
        except ModuleNotFoundError as exc:
            self.fail(f"connection_assembly_module_missing:{exc.name}")
        assembler_type = getattr(module, "ConnectionAssembler", None)
        self.assertIsNotNone(
            assembler_type,
            "connection_assembler_missing",
        )
        return assembler_type

    def test_selected_transport_is_passed_to_client_factory_once(self) -> None:
        assembler_type = self._assembler_type()
        snapshot = _Snapshot()
        transport = _Transport()
        calls: list[tuple[object, object]] = []
        client = object()

        def transport_factory(received_snapshot):
            self.assertIs(received_snapshot, snapshot)
            return transport

        def client_factory(received_snapshot, received_transport):
            calls.append((received_snapshot, received_transport))
            return client

        assembler = assembler_type(
            transport_factories={"http": transport_factory},
            client_factory=client_factory,
        )
        self.assertIs(assembler.connect(snapshot), client)
        self.assertEqual(calls, [(snapshot, transport)])
        self.assertEqual(transport.close_calls, 0)

    def test_transport_is_closed_if_client_construction_fails(self) -> None:
        assembler_type = self._assembler_type()
        transport = _Transport()

        def client_factory(_snapshot, _transport):
            raise RuntimeError("client-construction-failed")

        assembler = assembler_type(
            transport_factories={
                "http": lambda _snapshot: transport,
            },
            client_factory=client_factory,
        )
        with self.assertRaisesRegex(
            RuntimeError,
            "client-construction-failed",
        ):
            assembler.connect(_Snapshot())
        self.assertEqual(
            transport.close_calls,
            1,
            "half_initialized_transport_must_be_closed_once",
        )

    def test_adapter_registry_is_immutable_and_transport_neutral(self) -> None:
        assembler_type = self._assembler_type()
        factories = {"http": lambda _snapshot: _Transport()}
        assembler = assembler_type(
            transport_factories=factories,
            client_factory=lambda _snapshot, _transport: object(),
        )
        factories["tcp"] = lambda _snapshot: _Transport()
        self.assertEqual(
            tuple(assembler.transport_names),
            ("http",),
            "assembler_must_snapshot_adapter_registry",
        )
        with self.assertRaises(TypeError):
            assembler.transport_factories["udp"] = lambda _: _Transport()


if __name__ == "__main__":
    unittest.main()
