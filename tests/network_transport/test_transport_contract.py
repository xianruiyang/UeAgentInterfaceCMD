from __future__ import annotations

import dataclasses
import inspect
import unittest

from network_transport_test_support import (
    build_capabilities,
    build_frame,
    build_requirements,
    load_fixture,
    require_common_api,
)


class TransportContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = load_fixture()

    def test_frame_is_immutable_and_payload_is_opaque_bytes(self) -> None:
        api = require_common_api(self)
        frame = build_frame(api, self.fixture["frames"][0])

        self.assertTrue(dataclasses.is_dataclass(frame))
        self.assertTrue(type(frame).__dataclass_params__.frozen)
        self.assertIsInstance(frame.payload, bytes)
        self.assertEqual(
            frame.payload,
            bytes.fromhex(self.fixture["frames"][0]["payload_hex"]),
        )
        with self.assertRaises(
            (dataclasses.FrozenInstanceError, AttributeError, TypeError)
        ):
            frame.payload = b"changed"

    def test_capabilities_and_requirements_are_transport_only(self) -> None:
        api = require_common_api(self)
        capabilities = build_capabilities(
            api,
            self.fixture["capabilities"]["stream"],
        )
        requirements = build_requirements(
            api,
            self.fixture["requirements"]["portable"],
        )
        binding = api.bind_capabilities(capabilities, requirements)

        self.assertIsInstance(binding, api.CapabilityBinding)
        self.assertEqual(binding.capabilities, capabilities)
        self.assertEqual(binding.requirements, requirements)
        for value in (capabilities, requirements, binding):
            names = {
                field.name.casefold()
                for field in dataclasses.fields(value)
            }
            self.assertFalse(
                names
                & {
                    "command",
                    "descriptor",
                    "hjson",
                    "ticket",
                    "outcome",
                    "http_status",
                }
            )

    def test_delivery_states_do_not_claim_business_outcome(self) -> None:
        api = require_common_api(self)
        states = {
            state.value
            for state in api.TransportDeliveryState
        }

        self.assertEqual(
            states,
            set(self.fixture["delivery_states"]),
        )
        self.assertFalse(
            states
            & {
                "complete",
                "rolled_back",
                "state_unknown",
                "committed",
            }
        )
        delivery_fields = {
            field.name.casefold()
            for field in dataclasses.fields(api.TransportDelivery)
        }
        self.assertFalse(
            delivery_fields
            & {
                "outcome",
                "operation_result",
                "rollback",
                "mutation",
                "http_status",
            }
        )

    def test_ports_are_transport_neutral_and_have_exact_operations(
        self,
    ) -> None:
        api = require_common_api(self)

        self.assertTrue(
            getattr(api.ITransportClient, "_is_protocol", False),
            "ITransportClient must be a typing.Protocol",
        )

        self.assertEqual(
            tuple(inspect.signature(api.ITransportClient.send).parameters),
            ("self", "frame", "requirements"),
        )
        self.assertEqual(
            tuple(inspect.signature(api.ITransportClient.close).parameters),
            ("self",),
        )


if __name__ == "__main__":
    unittest.main()
