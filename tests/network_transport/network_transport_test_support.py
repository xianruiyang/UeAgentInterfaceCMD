from __future__ import annotations

import hashlib
import importlib
import importlib.util
import json
from pathlib import Path
from types import ModuleType, SimpleNamespace
from typing import Any


TEST_ROOT = Path(__file__).resolve().parent
CLI_ROOT = TEST_ROOT.parents[1]
PROJECT_ROOT = CLI_ROOT.parent
FIXTURE_PATH = TEST_ROOT / "fixtures" / "network_transport_cases.json"
PYTHON_PRODUCTION_ROOT = CLI_ROOT / "cli" / "uai" / "network_transport"
PLUGIN_PRODUCTION_ROOT = (
    PROJECT_ROOT
    / "Plugins"
    / "UeAgentInterface"
    / "Source"
    / "UeAgentInterface"
    / "Private"
    / "NetworkTransport"
)


COMMON_SYMBOLS = (
    "TransportPrincipal",
    "TransportPeer",
    "TransportFrame",
    "TransportCapabilities",
    "DeliveryRequirements",
    "CapabilityBinding",
    "TransportBindingError",
    "TransportDeliveryState",
    "TransportDiagnostic",
    "TransportDelivery",
    "TransportReply",
    "ITransportClient",
    "bind_capabilities",
)


def load_fixture() -> dict[str, Any]:
    return json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))


def fixture_sha256() -> str:
    return "sha256:" + hashlib.sha256(FIXTURE_PATH.read_bytes()).hexdigest()


def require_network_transport_module(test_case: Any) -> ModuleType:
    try:
        spec = importlib.util.find_spec("uai.network_transport")
    except ModuleNotFoundError:
        spec = None
    test_case.assertIsNotNone(
        spec,
        "n0_network_transport_module_missing:uai.network_transport",
    )
    return importlib.import_module("uai.network_transport")


def require_symbol(test_case: Any, name: str) -> Any:
    module = require_network_transport_module(test_case)
    test_case.assertTrue(
        hasattr(module, name),
        f"n0_network_transport_symbol_missing:{name}",
    )
    return getattr(module, name)


def require_common_api(test_case: Any) -> SimpleNamespace:
    return SimpleNamespace(
        **{
            name: require_symbol(test_case, name)
            for name in COMMON_SYMBOLS
        }
    )


def require_http_adapter_module(test_case: Any) -> ModuleType:
    require_network_transport_module(test_case)
    spec = importlib.util.find_spec("uai.network_transport.http")
    test_case.assertIsNotNone(
        spec,
        "n0_http_adapter_module_missing:uai.network_transport.http",
    )
    return importlib.import_module("uai.network_transport.http")


def build_frame(api: SimpleNamespace, row: dict[str, Any]) -> Any:
    principal = api.TransportPrincipal(
        subject=row["principal_subject"],
        authentication_method=row["authentication_method"],
    )
    peer = api.TransportPeer(
        peer_id=row["peer_id"],
        principal=principal,
    )
    return api.TransportFrame(
        channel=row["channel"],
        payload=bytes.fromhex(row["payload_hex"]),
        correlation_id=row["correlation_id"],
        peer=peer,
    )


def build_capabilities(
    api: SimpleNamespace,
    row: dict[str, Any],
) -> Any:
    return api.TransportCapabilities(**row)


def build_requirements(
    api: SimpleNamespace,
    row: dict[str, Any],
) -> Any:
    return api.DeliveryRequirements(**row)
