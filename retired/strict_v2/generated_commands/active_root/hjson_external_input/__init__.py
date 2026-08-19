"""Projection-only helpers for the T60 HJSON external-input domain."""

from __future__ import annotations

import json
from types import MappingProxyType

from uai.commands import bind_generated_commands


SCHEMA_ID = "uai.hjson.external_input/1"
ROOT_TYPES = MappingProxyType({
    "factory": "uai.external_input.factory",
    "skin_weight_profile": "uai.external_input.skin_weight_profile",
    "localization": "uai.external_input.localization",
})
IMPORTER_COMMANDS = MappingProxyType({
    "factory": frozenset({
        "asset.reimport_sound_wave",
        "asset.reimport_sparse_volume_texture",
        "asset.reimport_static_mesh",
        "asset.reimport_texture",
        "external.fbx.animation.import",
        "external.fbx.skeletal_mesh.import",
        "external.geometry_cache.import",
        "external.light_profile.import",
        "external.sound_wave.import",
        "external.sparse_volume_texture.import",
        "external.texture.import",
    }),
    "skin_weight_profile": frozenset({"external.skin_weight_profile.import"}),
    "localization": frozenset({"external.localization.po.import"}),
})


def build_document(
    *,
    family: str,
    source: dict[str, object],
    options: dict[str, object],
    target_policy: dict[str, object],
) -> str:
    root_type = ROOT_TYPES.get(family)
    if root_type is None:
        raise ValueError(f"hjson_external_input_family_unknown: {family}")
    command_id = target_policy.get("command_id")
    if command_id not in IMPORTER_COMMANDS[family]:
        raise ValueError(f"hjson_external_input_importer_unregistered: {command_id}")
    if set(source) - {"identity", "format", "content_sha256", "source_info"}:
        raise ValueError("hjson_external_input_source_field_unknown")
    required = ("identity", "format", "content_sha256")
    if any(not isinstance(source.get(key), str) or not source[key] for key in required):
        raise ValueError("hjson_external_input_source_invalid")
    digest = source["content_sha256"]
    if not isinstance(digest, str) or len(digest) != 71 or not digest.startswith("sha256:"):
        raise ValueError("hjson_external_input_source_digest_invalid")
    if not isinstance(options, dict) or not isinstance(target_policy.get("parameters"), dict):
        raise ValueError("hjson_external_input_target_policy_invalid")
    return json.dumps({
        "schema": SCHEMA_ID,
        "root": {
            "type": root_type,
            "external_input": {
                "source": dict(source),
                "options": dict(options),
                "target_policy": {
                    "command_id": command_id,
                    "parameters": dict(target_policy["parameters"]),
                },
            },
        },
    }, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def import_workspace(
    client,
    target: str,
    hjson_document: str,
    *,
    expected_revision: str,
    authorization_id: str,
    carrier: str = "inline",
    limits: dict[str, object] | None = None,
):
    commands = bind_generated_commands(client)
    kwargs: dict[str, object] = {}
    if limits is not None:
        kwargs["limits"] = limits
    return commands.content_graph.import_workspace(
        target,
        carrier,
        hjson_document,
        expected_revision,
        authorization_id,
        **kwargs,
    )


def export_workspace(
    client,
    target: str,
    workspace_path: str,
    *,
    profile_id: str | None = None,
):
    commands = bind_generated_commands(client)
    if profile_id is None:
        return commands.content_graph.export_workspace(target, workspace_path)
    return commands.content_graph.export_workspace(
        target, workspace_path, profile_id=profile_id
    )


__all__ = [
    "IMPORTER_COMMANDS",
    "ROOT_TYPES",
    "SCHEMA_ID",
    "build_document",
    "export_workspace",
    "import_workspace",
]
