from __future__ import annotations

import json
from pathlib import Path

from uai.commands.generated import BINDING_CATALOG


REPO_ROOT = Path(__file__).resolve().parents[2]
MANIFEST = (
    REPO_ROOT.parent
    / "Plugins"
    / "UeAgentInterface"
    / "Resources"
    / "UaiCommandManifest.json"
)


def test_complete_production_manifest_is_publicly_bound() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    commands = manifest["commands"]
    assert isinstance(commands, list)
    assert len(commands) == len(
        {str(command["command_id"]) for command in commands}
    ), "production_manifest_command_ids_must_be_unique"

    forbidden = {
        "descriptor_id",
        "descriptor_hash",
        "family",
        "provider_binding",
        "route",
        "hjson",
        "ticket",
        "session",
    }
    for command in commands:
        assert not forbidden.intersection(command)

    manifest_ids = {str(command["command_id"]) for command in commands}
    assert "content_graph.import_workspace" in manifest_ids
    assert "asset.delete" in manifest_ids
    assert "world.data_layer.delete" in manifest_ids
    assert "external.texture.import" in manifest_ids
    assert set(BINDING_CATALOG.command_ids) == manifest_ids
