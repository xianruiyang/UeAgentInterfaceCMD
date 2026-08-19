from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PROJECT_ROOT = REPO_ROOT.parent
MANIFEST_PATH = (
    PROJECT_ROOT
    / "Plugins"
    / "UeAgentInterface"
    / "Resources"
    / "UaiCommandManifest.json"
)
GENERATED_PATH = REPO_ROOT / "cli" / "uai" / "commands" / "generated.py"


def _manifest() -> dict[str, object]:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def test_read_export_commands_are_cpp_manifest_owned_and_generated() -> None:
    manifest = _manifest()
    commands = manifest["commands"]
    assert isinstance(commands, list)
    by_id = {str(command["command_id"]): command for command in commands}

    required_ids = {
        "reference.catalog_search",
        "reference.asset_read",
        "content_graph.export_workspace",
    }
    assert required_ids.issubset(by_id)
    assert "/api/uai/export" not in by_id
    assert manifest["source"]["kind"] == "cpp_command_registry_export"

    generated = GENERATED_PATH.read_text(encoding="utf-8")
    for command_id in sorted(required_ids):
        assert f'"{command_id}"' in generated
    assert "/api/uai/export" not in generated

    assert [
        parameter["name"]
        for parameter in by_id["content_graph.export_workspace"]["parameters"]
    ] == [
        "target",
        "workspace_path",
        "input",
        "context",
        "projection",
        "profile_id",
    ]


def test_public_read_shape_does_not_expose_internal_dispatch() -> None:
    manifest = _manifest()
    commands = manifest["commands"]
    by_id = {str(command["command_id"]): command for command in commands}
    for command_id in (
        "reference.catalog_search",
        "reference.asset_read",
        "content_graph.export_workspace",
    ):
        command = by_id[command_id]
        names = {str(parameter["name"]) for parameter in command["parameters"]}
        assert "descriptor_id" not in names
        assert "provider_binding" not in names
        assert "route" not in names
        assert "http_path" not in names
