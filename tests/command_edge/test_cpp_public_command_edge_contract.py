from __future__ import annotations

import json
from pathlib import Path
import re
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[3]
MANIFEST_PATH = (
    PROJECT_ROOT
    / "Plugins"
    / "UeAgentInterface"
    / "Resources"
    / "UaiCommandManifest.json"
)
SHA256_IDENTITY = re.compile(r"^sha256:[0-9a-f]{64}$")


class CppPublicCommandEdgeContractTests(unittest.TestCase):
    def test_formal_manifest_is_a_unique_cpp_registry_export(self) -> None:
        payload = json.loads(
            MANIFEST_PATH.read_text(encoding="utf-8-sig")
        )
        self.assertEqual(payload.get("schema"), "uai.command_manifest.v1")
        self.assertEqual(
            (payload.get("source") or {}).get("kind"),
            "cpp_immutable_command_registry_export",
        )
        commands = payload.get("commands")
        self.assertIsInstance(commands, list)
        self.assertTrue(commands, "cpp_command_manifest_is_empty")
        command_ids = [command.get("command_id") for command in commands]
        self.assertEqual(
            len(command_ids),
            len(set(command_ids)),
            "cpp_command_manifest_has_duplicate_command_id",
        )
        for command in commands:
            with self.subTest(command=command.get("command_id")):
                self.assertIn(
                    command.get("status"),
                    {"active", "dormant", "disabled"},
                )
                self.assertRegex(
                    str(command.get("binding_hash", "")),
                    SHA256_IDENTITY,
                )

    def test_required_public_search_read_effect_and_hjson_edges_exist(
        self,
    ) -> None:
        payload = json.loads(
            MANIFEST_PATH.read_text(encoding="utf-8-sig")
        )
        by_id = {
            command["command_id"]: command
            for command in payload["commands"]
        }
        self.assertTrue(
            {
                "query.command.search",
                "query.command.usage",
                "content_graph.export_workspace",
                "content_graph.import_workspace",
            }.issubset(by_id)
        )
        self.assertEqual(
            [
                parameter["name"]
                for parameter in by_id[
                    "content_graph.import_workspace"
                ]["parameters"]
            ],
            [
                "target",
                "source",
            ],
        )

    def test_public_manifest_exposes_only_wire_binding_fields(self) -> None:
        payload = json.loads(
            MANIFEST_PATH.read_text(encoding="utf-8-sig")
        )
        forbidden_fields = {
            "descriptor_id",
            "descriptor_hash",
            "route",
            "route_path",
            "default",
            "success_condition",
            "verification",
        }
        for command in payload["commands"]:
            with self.subTest(command=command.get("command_id")):
                self.assertEqual(
                    sorted(set(command) & forbidden_fields),
                    [],
                )


if __name__ == "__main__":
    unittest.main()
