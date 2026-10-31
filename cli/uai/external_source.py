"""Typed custody for project-local files consumed by import/reimport commands."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import PurePosixPath
from typing import Any

from .errors import UsageError
from .local_paths import resolve_project_relative


_FILE_SOURCE_COMMANDS = frozenset(
    {
        "asset.reimport_sound_wave",
        "asset.reimport_sparse_volume_texture",
        "asset.reimport_static_mesh",
        "asset.reimport_texture",
        "external.fbx.animation.import",
        "external.fbx.skeletal_mesh.import",
        "external.fbx.static_mesh.import",
        "external.geometry_cache.import",
        "external.light_profile.import",
        "external.localization.po.import",
        "external.skin_weight_profile.import",
        "external.sound_wave.import",
        "external.sparse_volume_texture.import",
        "external.texture.import",
    }
)


class ProjectFileHandle:
    """Expose a short project path while privately retaining its wire path."""

    __slots__ = ("_absolute_path", "_path")

    def __init__(self, client: Any, path: str | PurePosixPath) -> None:
        absolute, relative = resolve_project_relative(client, path)
        self._absolute_path = absolute
        self._path = relative

    @property
    def path(self) -> PurePosixPath:
        return self._path

    def __repr__(self) -> str:
        return f"ProjectFileHandle(path={self._path.as_posix()!r})"

    def _wire_value(self) -> str:
        return str(self._absolute_path)


class ExternalSourceNamespace:
    """Create project-file handles without exposing an absolute path."""

    __slots__ = ("_client",)

    def __init__(self, client: Any) -> None:
        self._client = client

    def from_project(self, path: str | PurePosixPath) -> ProjectFileHandle:
        return ProjectFileHandle(self._client, path)


def prepare_public_params(client: Any, command_id: str, params: object) -> object:
    """Resolve supported readable paths and reject machine-owned inputs."""

    if not isinstance(params, Mapping):
        return params
    projected = dict(params)

    def resolve_path(path: str | PurePosixPath, pointer: str) -> str:
        try:
            return ProjectFileHandle(client, path)._wire_value()
        except UsageError as exc:
            exc.diagnostic["property_path"] = pointer
            raise

    def resolve_owned_outputs(value: object, pointer: str = "") -> object:
        if isinstance(value, Mapping):
            resolved = {}
            for key, item in value.items():
                item_pointer = pointer + "/" + str(key).replace("~", "~0").replace("/", "~1")
                if key in {"output_dir", "output_file"}:
                    if isinstance(item, ProjectFileHandle):
                        resolved[key] = item._wire_value()
                    elif isinstance(item, (str, PurePosixPath)):
                        resolved[key] = resolve_path(item, item_pointer)
                    else:
                        raise UsageError.at_source(
                            code="project_output_path_invalid",
                            message=(
                                "output paths must be short project-relative paths "
                                "or ProjectFileHandle values"
                            ),
                            facts={"property_path": item_pointer, "expected_value": "project-relative path or ProjectFileHandle",
                                        "actual_value": {"type": type(item).__name__}},
                        )
                else:
                    resolved[key] = resolve_owned_outputs(item, item_pointer)
            return resolved
        if isinstance(value, list):
            return [resolve_owned_outputs(item, pointer + "/" + str(index)) for index, item in enumerate(value)]
        if isinstance(value, tuple):
            return tuple(resolve_owned_outputs(item, pointer + "/" + str(index)) for index, item in enumerate(value))
        return value

    projected = resolve_owned_outputs(projected)
    if command_id in _FILE_SOURCE_COMMANDS:
        source = projected.get("source_ref")
        if isinstance(source, ProjectFileHandle):
            projected["source_ref"] = source._wire_value()
        elif isinstance(source, (str, PurePosixPath)):
            projected["source_ref"] = resolve_path(source, "/source_ref")
        else:
            raise UsageError.at_source(
                code="project_file_source_required",
                message=(
                    "source_ref must be one short project-relative path "
                    "or ProjectFileHandle"
                ),
                facts={"property_path": "/source_ref", "expected_value": "project-relative path or ProjectFileHandle",
                            "actual_value_present": "source_ref" in projected, "actual_value": {"type": type(source).__name__}},
            )
    if command_id in {
        "asset_durable.journal.read",
        "asset_durable.journal.reconcile",
    }:
        raise UsageError(
            code="asset_durable_custody_owned_by_sdk",
            message="use client.asset_durable.from_result(result)",
        )
    if command_id == "runtime.scenario.execute":
        raise UsageError(
            code="runtime_session_custody_owned_by_sdk",
            message="use operation.runtime_session.scenario_execute(parameters=...)",
        )
    if command_id == "content_graph.export_workspace":
        raise UsageError(
            code="workspace_path_owned_by_sdk",
            message="use client.content_graph.export_workspace(target, name=...)",
        )
    if command_id == "content_graph.import_workspace":
        source = projected.get("source")
        if isinstance(source, Mapping) and source.get("kind") in {
            "directory",
            "single_file",
        }:
            raise UsageError(
                code="workspace_path_owned_by_sdk",
                message="use HjsonWorkspaceHandle.import_changes() for file-backed edits",
            )
    return projected


def is_file_source_command(command_id: str) -> bool:
    return command_id in _FILE_SOURCE_COMMANDS


__all__ = ["ExternalSourceNamespace", "ProjectFileHandle"]
