from __future__ import annotations

import inspect
import json
from pathlib import Path
import unittest

import uai
from uai.commands import BINDING_CATALOG

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
        self.assertIn("def content_search", stub)
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

    def test_dormant_commands_remain_in_catalog_without_named_methods(self) -> None:
        dormant = (
            ("world.actors", "actors"),
            ("world.actor_components", "actor_components"),
            ("world.property", "property"),
            ("world.object_transform.read", "object_transform_read"),
            ("world.object_transform.update", "object_transform_update"),
        )
        namespaces, _client = self._namespaces()
        for command_id, method in dormant:
            binding = BINDING_CATALOG.find(command_id)
            self.assertIsNotNone(binding)
            self.assertEqual(binding.status, "dormant")
            self.assertFalse(hasattr(namespaces.world, method))

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

    def test_content_search_forwards_exact_filters_and_cursor_once(self) -> None:
        namespaces, client = self._namespaces()
        cursor = {
            "request_fingerprint": "sha1:fixture",
            "providers": [
                {
                    "provider_id": "editor.asset_registry.content",
                    "revision": "sha1:revision",
                    "offset": 20,
                }
            ],
        }
        namespaces.query.content_search(
            query="Cube",
            match_mode="text",
            content_kinds=["asset"],
            path_prefix="/Game",
            required_operations=["query"],
            limit_per_provider=20,
            cursor=cursor,
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
                        "path_prefix": "/Game",
                        "required_operations": ["query"],
                        "limit_per_provider": 20,
                        "cursor": cursor,
                    },
                )
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

    def test_asset_registry_relations_requires_and_forwards_nested_input(self) -> None:
        namespaces, client = self._namespaces()
        signature = inspect.signature(namespaces.asset.registry_relations)
        self.assertIs(
            signature.parameters["input"].default,
            inspect.Parameter.empty,
            "registry_relations_input_must_not_be_optional",
        )
        target = "/Game/Test.Test"
        query_input = {"direction": "dependencies"}
        namespaces.asset.registry_relations(target, query_input)
        self.assertEqual(
            client.calls,
            [
                (
                    "asset.registry_relations",
                    {"target": target, "input": query_input},
                )
            ],
        )

    def test_voxel_grid_bindings_forward_only_explicit_session_data(self) -> None:
        namespaces, client = self._namespaces()
        namespaces.mesh.voxel_grid_session(
            "begin",
            mode="create",
            grid_id="VG_PY_PUBLIC",
            cell_size=100.0,
        )
        namespaces.mesh.voxel_grid_apply(
            "VGS_PY_PUBLIC",
            2,
            collision={"mode": "exact_box_components"},
            keep_session=True,
        )
        self.assertEqual(
            client.calls,
            [
                (
                    "mesh.voxel_grid.session",
                    {
                        "action": "begin",
                        "mode": "create",
                        "grid_id": "VG_PY_PUBLIC",
                        "cell_size": 100.0,
                    },
                ),
                (
                    "mesh.voxel_grid.apply",
                    {
                        "session_id": "VGS_PY_PUBLIC",
                        "expected_revision": 2,
                        "collision": {"mode": "exact_box_components"},
                        "keep_session": True,
                    },
                ),
            ],
        )


if __name__ == "__main__":
    unittest.main()
