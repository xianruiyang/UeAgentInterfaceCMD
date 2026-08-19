from __future__ import annotations

import inspect
import json
from pathlib import Path
import unittest

import uai

try:
    from uai.commands.generated import (
        GENERATED_REGISTRY_HASH,
        GeneratedCommandNamespaces,
    )
except ImportError:
    GENERATED_REGISTRY_HASH = None
    GeneratedCommandNamespaces = None


REPO_ROOT = Path(__file__).resolve().parents[2]
MANIFEST = (
    REPO_ROOT.parent
    / "Plugins"
    / "UeAgentInterface"
    / "Resources"
    / "UaiCommandManifest.json"
)
GENERATED_PYI = (
    REPO_ROOT / "cli" / "uai" / "commands" / "generated.pyi"
)


class _Client:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, object]]] = []

    def execute(
        self,
        command_id: str,
        params: dict[str, object],
    ):
        self.calls.append((command_id, params))
        return object()


class GeneratedClientBindingContractTests(unittest.TestCase):
    def _namespaces(self):
        self.assertIsNotNone(
            GeneratedCommandNamespaces,
            "generated_command_namespaces_missing",
        )
        client = _Client()
        return GeneratedCommandNamespaces(client), client

    def test_generated_source_is_bound_to_current_cpp_manifest(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(
            GENERATED_REGISTRY_HASH,
            manifest["registry_hash"],
            "generated_binding_registry_hash_is_stale",
        )
        self.assertTrue(GENERATED_PYI.is_file())
        stub = GENERATED_PYI.read_text(encoding="utf-8-sig")
        self.assertIn("class QueryCommands", stub)
        self.assertIn("def command_search", stub)
        self.assertIn("def command_detail", stub)
        self.assertIn("class ReferenceCommands", stub)
        self.assertIn("def asset_read", stub)
        self.assertIn("def asset_apply", stub)
        self.assertIn("class ContentGraphCommands", stub)
        self.assertIn("def import_workspace", stub)

    def test_client_has_static_reference_namespace(self) -> None:
        member = inspect.getattr_static(
            uai.Client,
            "reference",
            None,
        )
        self.assertIsNotNone(
            member,
            "client_reference_namespace_missing",
        )

    def test_command_search_omits_only_the_omission_sentinel(self) -> None:
        namespaces, client = self._namespaces()
        namespaces.query.command_search("查找资产编辑指令")
        namespaces.query.command_search("查找资产编辑指令", cursor=None)
        self.assertEqual(
            client.calls,
            [
                (
                    "query.command.search",
                    {"intent": "查找资产编辑指令"},
                ),
                (
                    "query.command.search",
                    {
                        "intent": "查找资产编辑指令",
                        "cursor": None,
                    },
                ),
            ],
        )

    def test_asset_apply_forwards_once_without_business_defaults(self) -> None:
        namespaces, client = self._namespaces()
        namespaces.reference.asset_apply(
            "/Game/UAI/PY007",
            "delete",
        )
        self.assertEqual(
            client.calls,
            [
                (
                    "reference.asset_apply",
                    {
                        "object_path": "/Game/UAI/PY007",
                        "intent": "delete",
                    },
                )
            ],
        )

    def test_asset_read_forwards_one_object_path_once(self) -> None:
        namespaces, client = self._namespaces()
        namespaces.reference.asset_read(
            "/Game/UAI/Reference/PY008.PY008",
        )
        self.assertEqual(
            client.calls,
            [
                (
                    "reference.asset_read",
                    {
                        "object_path": (
                            "/Game/UAI/Reference/PY008.PY008"
                        ),
                    },
                )
            ],
        )


if __name__ == "__main__":
    unittest.main()
