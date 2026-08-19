from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


EXPECTED_COMMAND_IDS = {
    "content_graph.compound",
    "content_graph.diagnostics",
    "content_graph.export_workspace",
    "content_graph.import_workspace",
    "content_graph.items",
    "content_graph.properties",
    "content_graph.relations",
    "content_graph.structure",
    "content_graph.summary",
}


class _RecordedResult:
    ok = True


class _RecordingClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(
        self,
        command_id: str,
        params: dict[str, Any],
        *,
        contract_hash: str,
    ) -> _RecordedResult:
        self.calls.append((command_id, dict(params), contract_hash))
        return _RecordedResult()

    def execute(
        self,
        command_id: str,
        params: dict[str, Any],
    ) -> _RecordedResult:
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _require_bindings():
    bindings = {
        command_id: BINDING_CATALOG.find(command_id)
        for command_id in EXPECTED_COMMAND_IDS
    }
    assert all(binding is not None for binding in bindings.values())
    assert all(
        binding is not None
        and binding.command_id == command_id
        and binding.namespace == "content_graph"
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def test_all_audited_content_graph_commands_have_exact_default_bindings() -> None:
    _require_bindings()


def test_query_method_preserves_exact_target_input_context_and_projection() -> None:
    _require_bindings()
    client = _RecordingClient()
    target = "/Game/StrictV2/T13/DA_Recursive.DA_Recursive"
    bind_generated_commands(client).content_graph.compound(
        target,
        input={"sections": ["summary", "structure", "items"]},
        context={"state_plane": "persisted"},
        projection={"max_items": 50},
    )
    assert client.calls[0][0] == "content_graph.compound"
    assert client.calls[0][1] == {
        "target": target,
        "input": {"sections": ["summary", "structure", "items"]},
        "context": {"state_plane": "persisted"},
        "projection": {"max_items": 50},
    }


def test_import_method_forwards_each_source_variant_without_mapping() -> None:
    _require_bindings()
    target = "/Game/StrictV2/T13/DA_Recursive.DA_Recursive"
    document = '{"schema":"uai.uobject_dataasset.recursive/1","root":{"id":"root"}}'
    sources = (
        {"kind": "inline", "document": document},
        {"kind": "single_file", "path": "D:/uai/t13/workspace.hjson"},
        {"kind": "directory", "path": "D:/uai/t13/workspace"},
    )
    for source in sources:
        client = _RecordingClient()
        bind_generated_commands(client).content_graph.import_workspace(
            target,
            source,
            expected_revision="absent",
            authorization_id="auth:t13:test",
            limits={"max_nodes": 64, "max_work_units": 4096},
        )
        assert client.calls == [
            (
                "content_graph.import_workspace",
                {
                    "target": target,
                    "source": source,
                    "expected_revision": "absent",
                    "authorization_id": "auth:t13:test",
                    "limits": {"max_nodes": 64, "max_work_units": 4096},
                },
                BINDING_CATALOG.find(
                    "content_graph.import_workspace"
                ).binding_hash,
            )
        ]


def test_export_method_forwards_exact_workspace_and_profile() -> None:
    _require_bindings()
    client = _RecordingClient()
    bind_generated_commands(client).content_graph.export_workspace(
        "/Game/StrictV2/T13/DA_Recursive.DA_Recursive",
        "D:/program/UE/GptProjectTest/Saved/StrictV2/T13/export",
        profile_id="llm_authoring",
    )
    assert client.calls[0][0] == "content_graph.export_workspace"
    assert client.calls[0][1]["profile_id"] == "llm_authoring"


def test_named_and_generic_execution_use_the_same_exact_binding() -> None:
    bindings = _require_bindings()
    named = _RecordingClient()
    generic = _RecordingClient()
    target = "/Game/StrictV2/T13/DA_Recursive.DA_Recursive"
    bind_generated_commands(named).content_graph.summary(target)
    generic.execute_exact(
        "content_graph.summary",
        {"target": target},
        contract_hash=bindings["content_graph.summary"].binding_hash,
    )
    assert named.calls == generic.calls


def test_t13_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = cmd_root / "cli" / "uai" / "generated_commands" / "uobject_dataasset"
    task_doc = cmd_root / "docs" / "active" / "t13_uobject_recursive_init.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t13_uobject_recursive_init.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.content_graph.compound" in text
        assert "client.content_graph.import_workspace" in text
        assert "client.content_graph.export_workspace" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text
