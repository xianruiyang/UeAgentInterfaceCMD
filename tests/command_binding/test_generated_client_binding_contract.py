from __future__ import annotations

import inspect
import json
from pathlib import Path
import unittest

import uai
from uai.commands import _BINDING_CATALOG

from uai.commands.generated import GeneratedCommandNamespaces


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

    def test_generated_catalog_matches_current_cpp_manifest(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        manifest_commands = {
            command["command_id"]: command
            for command in manifest["commands"]
        }
        self.assertEqual(
            set(_BINDING_CATALOG.command_ids),
            set(manifest_commands),
            "generated_binding_catalog_is_stale",
        )
        for binding in _BINDING_CATALOG.bindings:
            self.assertEqual(
                binding.status,
                manifest_commands[binding.command_id]["status"],
            )
        self.assertTrue(GENERATED_PYI.is_file())
        stub = GENERATED_PYI.read_text(encoding="utf-8-sig")
        self.assertIn("class QueryCommands", stub)
        self.assertIn("def command_search", stub)
        self.assertIn("def command_usage", stub)
        self.assertNotIn("def command_detail", stub)
        self.assertIn("def content_search", stub)
        self.assertIn("class ReferenceCommands", stub)
        self.assertIn("def origin_resolve", stub)
        self.assertIn("class ContentGraphCommands", stub)
        self.assertNotIn("def import_workspace", stub)
        self.assertNotIn("class RuntimeCommands", stub)

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

    def test_dormant_commands_remain_in_catalog_without_named_methods(self) -> None:
        namespaces, _client = self._namespaces()
        dormant = [
            binding
            for binding in _BINDING_CATALOG.bindings
            if binding.status == "dormant"
        ]
        self.assertTrue(dormant)
        for binding in dormant:
            namespace = getattr(namespaces, binding.namespace, None)
            if namespace is not None:
                self.assertFalse(
                    hasattr(namespace, binding.method),
                    binding.command_id,
                )

    def test_command_search_forwards_intent(self) -> None:
        namespaces, client = self._namespaces()
        namespaces.query.command_search("asset edit")
        self.assertEqual(
            client.calls,
            [
                (
                    "query.command.search",
                    {"intent": "asset edit"},
                ),
            ],
        )

    def test_content_search_forwards_only_compact_discovery_filters(self) -> None:
        namespaces, client = self._namespaces()
        namespaces.query.content_search(
            query="Cube",
            match_mode="text",
            content_kinds=["asset"],
        )
        self.assertEqual(
            client.calls,
            [
                (
                    "query.content.search",
                    {
                        "query": "Cube",
                        "match_mode": "text",
                        "content_kinds": ["asset"],
                    },
                )
            ],
        )

    def test_asset_relations_requires_and_forwards_nested_input(self) -> None:
        namespaces, client = self._namespaces()
        signature = inspect.signature(namespaces.asset.relations)
        self.assertIs(
            signature.parameters["input"].default,
            inspect.Parameter.empty,
            "asset_relations_input_must_not_be_optional",
        )
        target = "/Game/Test.Test"
        query_input = {"direction": "dependencies", "max_depth": 3}
        namespaces.asset.relations(target, query_input)
        self.assertEqual(
            client.calls,
            [
                (
                    "asset.relations",
                    {"target": target, "input": query_input},
                )
            ],
        )

    def test_voxel_grid_public_binding_forwards_only_begin_business_data(self) -> None:
        namespaces, client = self._namespaces()
        namespaces.mesh.voxel_grid_begin(
            mode="create",
            label="Blockout",
            cell_size=100.0,
        )
        self.assertEqual(
            client.calls,
            [
                (
                    "mesh.voxel_grid.begin",
                    {
                        "mode": "create",
                        "label": "Blockout",
                        "cell_size": 100.0,
                    },
                ),
            ],
        )
        self.assertFalse(hasattr(namespaces.mesh, "voxel_grid_session"))
        self.assertFalse(hasattr(namespaces.mesh, "voxel_grid_apply"))


if __name__ == "__main__":
    unittest.main()
