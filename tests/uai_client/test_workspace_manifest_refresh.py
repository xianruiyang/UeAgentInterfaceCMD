from __future__ import annotations

from pathlib import Path

import pytest

from uai.workspace import ContentGraphNamespace, HjsonWorkspaceHandle
from uai.local_paths import resolve_project_relative
from uai.errors import UsageError


class _Connection:
    def __init__(self, source_path: Path) -> None:
        self.source_path = source_path


class _Client:
    def __init__(self, source_path: Path) -> None:
        self._connection = _Connection(source_path)
        self.calls: list[tuple[str, dict[str, object]]] = []

    def _import_hjson_workspace(self, target, source):
        self.calls.append((target, source))
        return "imported"


def test_project_path_normalizes_internal_parent_segments(tmp_path: Path) -> None:
    (tmp_path / "Fixture.uproject").write_text("{}", encoding="utf-8")
    client = _Client(tmp_path / "connection.toml")
    absolute, relative = resolve_project_relative(client, "Content/../Source Input.json")
    assert absolute == tmp_path / "Source Input.json"
    assert relative.as_posix() == "Source Input.json"
    with pytest.raises(UsageError) as caught:
        resolve_project_relative(client, "../outside.json")
    assert caught.value.diagnostic["code"] == "project_relative_path_invalid"
    assert caught.value.diagnostic["message"] == "project-relative path escapes the current project"
    assert caught.value.diagnostic["property_path"] == "path"
    assert caught.value.diagnostic["actual_value"] == "../outside.json"


@pytest.mark.parametrize("name", ["..", "../outside", "sub/name", "sub\\name", "C:outside", "工作区", "Workspace", "work space"])
def test_workspace_name_preserves_ascii_policy_and_directory_boundary(tmp_path: Path, name: str) -> None:
    with pytest.raises(UsageError):
        HjsonWorkspaceHandle(_Client(tmp_path / "connection.toml"),
                             target="/Game/Test.Asset", name=name, result="exported")


def _handle(tmp_path: Path, manifest: bytes) -> tuple[_Client, Path, HjsonWorkspaceHandle]:
    project = tmp_path / "project"
    project.mkdir()
    (project / "GptProjectTest.uproject").write_text("{}", encoding="utf-8")
    workspace = project / "tmp" / "uai-workspaces" / "sample"
    (workspace / ".uai").mkdir(parents=True)
    (workspace / ".uai" / "workspace.hjson").write_bytes(manifest)
    client = _Client(project / "connection.toml")
    handle = HjsonWorkspaceHandle(
        client,
        target="/Game/Test/Asset.Asset",
        name="sample",
        result="exported",
    )
    return client, workspace, handle


def test_import_changes_forwards_edited_directory_without_rewriting_manifest(
    tmp_path: Path,
) -> None:
    manifest = b"{ unit_inventory: [] }\n"
    client, workspace, handle = _handle(tmp_path, manifest)
    document = workspace / "graphs" / "main.hjson"
    document.parent.mkdir()
    document.write_text("{ value: edited }\n", encoding="utf-8")

    assert handle.import_changes() == "imported"
    assert (workspace / ".uai" / "workspace.hjson").read_bytes() == manifest
    assert client.calls == [
        (
            "/Game/Test/Asset.Asset",
            {"kind": "directory", "path": str(workspace.resolve())},
        )
    ]


def test_import_changes_preserves_manifest_with_multiple_units_in_one_document(
    tmp_path: Path,
) -> None:
    manifest = (
        b"{\n"
        b"  unit_inventory: [\n"
        b"    { unit_id: one, document_path: \"properties.hjson\", "
        b"unit_pointer: \"/categories/A\", content_hash: \"sha256:unit-one\" }\n"
        b"    { unit_id: two, document_path: \"properties.hjson\", "
        b"unit_pointer: \"/categories/B\", content_hash: \"sha256:unit-two\" }\n"
        b"  ]\n"
        b"}\n"
    )
    client, workspace, handle = _handle(tmp_path, manifest)
    (workspace / "properties.hjson").write_text(
        "{ categories: { A: { x: 1 }, B: { y: 2 } } }\n", encoding="utf-8"
    )

    assert handle.import_changes() == "imported"
    assert (workspace / ".uai" / "workspace.hjson").read_bytes() == manifest
    assert client.calls[0][1] == {
        "kind": "directory",
        "path": str(workspace.resolve()),
    }


def test_open_existing_workspace_preserves_external_edits_across_clients(tmp_path: Path) -> None:
    manifest = b"opaque server-owned manifest; not parsed by SDK"
    original, workspace, _ = _handle(tmp_path, manifest)
    document = workspace / "properties.hjson"
    edited = b"{ value: 42 }\n"
    document.write_bytes(edited)
    fresh_client = _Client(original._connection.source_path)
    reopened = ContentGraphNamespace(fresh_client, object()).open_workspace(
        "/Game/Test/Asset.Asset", name="sample"
    )
    assert reopened.result is None
    assert fresh_client.calls == []
    assert reopened.path.as_posix() == "tmp/uai-workspaces/sample"
    assert document.read_bytes() == edited
    assert reopened.import_changes() == "imported"
    assert document.read_bytes() == edited
    assert (workspace / ".uai" / "workspace.hjson").read_bytes() == manifest
    assert fresh_client.calls == [("/Game/Test/Asset.Asset", {
        "kind": "directory", "path": str(workspace.resolve())
    })]


def test_prepare_workspace_forwards_source_without_rewriting_it(tmp_path: Path) -> None:
    project = tmp_path / "project"
    project.mkdir()
    (project / "GptProjectTest.uproject").write_text("{}", encoding="utf-8")

    class ExportClient(_Client):
        def _export_hjson_workspace(self, target, path, **options):
            self.exported = (target, path, options)
            return "prepared"

    client = ExportClient(project / "connection.toml")
    source = {"kind": "inline", "document": "{ external_input: { options: {} } }"}
    name = "prepared-workspace-with-a-name-longer-than-thirty-two-characters"
    handle = ContentGraphNamespace(client, object()).export_workspace(
        "/Game/Test/Prepared.Prepared", name=name, source=source
    )

    assert handle.result == "prepared"
    assert handle.path.as_posix() == f"tmp/uai-workspaces/{name}"
    assert client.exported[0] == "/Game/Test/Prepared.Prepared"
    assert Path(client.exported[1]) == (project / handle.path).resolve()
    assert client.exported[2]["source"] is source
    assert not (project / handle.path).exists()
