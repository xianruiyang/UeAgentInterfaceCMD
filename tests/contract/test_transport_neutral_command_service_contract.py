from __future__ import annotations

import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[3]
PLUGIN_PRIVATE = (
    PROJECT_ROOT
    / "Plugins"
    / "UeAgentInterface"
    / "Source"
    / "UeAgentInterface"
    / "Private"
)


class TransportNeutralCommandServiceContractTest(unittest.TestCase):
    def test_command_service_owns_no_http_surface(self) -> None:
        header = (
            PLUGIN_PRIVATE
            / "ServiceComposition"
            / "CommandService"
            / "UeAgentCommandService.h"
        ).read_text(encoding="utf-8-sig")
        source = (
            PLUGIN_PRIVATE
            / "ServiceComposition"
            / "CommandService"
            / "UeAgentCommandService.cpp"
        ).read_text(encoding="utf-8-sig")

        self.assertIn("NetworkTransport/UeAgentNetworkTransport.h", header)
        self.assertIn("GetIngressHandler", header)
        for forbidden in (
            "UeAgentHttpTransportAdapter",
            "IUeAgentHttpRouteHost",
            "GetUaiCommandRoutePath",
            "AuthToken",
            "RoutePath",
            "StatusCode",
        ):
            self.assertNotIn(forbidden, header)
            self.assertNotIn(forbidden, source)

    def test_http_adapter_is_composed_outside_command_service(self) -> None:
        source = (
            PLUGIN_PRIVATE
            / "Module"
            / "UeAgentInterfaceModule.cpp"
        ).read_text(encoding="utf-8-sig")
        self.assertIn("TryCreateQueryCommandIngress", source)
        self.assertIn("FUeAgentCommandService::TryCreate", source)
        self.assertIn("FUeAgentHttpTransportAdapter", source)
        self.assertIn("GetUaiHttpCommandRoutePath", source)
        self.assertIn("NewCommandService->GetIngressHandler()", source)
        self.assertNotIn("FUeAgentQueryServiceComposition", source)


if __name__ == "__main__":
    unittest.main()
