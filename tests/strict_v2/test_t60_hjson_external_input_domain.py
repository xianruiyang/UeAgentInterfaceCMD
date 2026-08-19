from __future__ import annotations

from pathlib import Path
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_IDS = ("content_graph.import_workspace", "content_graph.export_workspace")


class FakeClient:
    def __init__(self):
        self.calls = []

    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id, params):
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            command_id, params, contract_hash=binding.binding_hash
        )


def _bindings():
    bindings = {command_id: BINDING_CATALOG.find(command_id) for command_id in COMMAND_IDS}
    assert all(
        binding is not None
        and binding.namespace == "content_graph"
        and binding.method in {"import_workspace", "export_workspace"}
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        for binding in bindings.values()
    )
    return bindings


def test_t60_uses_default_content_graph_bindings() -> None:
    _bindings()


def test_t60_import_forwards_one_caller_authored_exact_document() -> None:
    client = FakeClient()
    document = (
        '{schema:"uai.hjson.external_input/1",root:{'
        'type:"uai.external_input.factory",external_input:{'
        'source:{identity:"D:/fixtures/t60.png",format:"png",'
        'content_sha256:"sha256:aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"},'
        'options:{replace_existing:false},target_policy:{'
        'command_id:"external.texture.import",parameters:{'
        'destination_ref:"/Game/UAI_StrictV2/T60_Texture.T60_Texture"}}}}}'
    )
    bind_generated_commands(client).content_graph.import_workspace(
        "/Game/UAI_StrictV2/T60_Texture.T60_Texture",
        {"kind": "inline", "document": document},
        "absent",
        "auth:t60",
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.import_workspace"
    assert params["source"] == {"kind": "inline", "document": document}
    assert "hjson_document" not in params and "carrier" not in params
    assert contract_hash == _bindings()[command_id].binding_hash


def test_t60_export_forwards_exact_workspace_path() -> None:
    client = FakeClient()
    bind_generated_commands(client).content_graph.export_workspace(
        "/Game/UAI_StrictV2/T60_Texture.T60_Texture",
        "D:/workspace/t60",
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.export_workspace"
    assert params == {
        "target": "/Game/UAI_StrictV2/T60_Texture.T60_Texture",
        "workspace_path": "D:/workspace/t60",
    }
    assert contract_hash == _bindings()[command_id].binding_hash


def test_t60_task_helper_exits_and_tutorial_points_to_unified_t13() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    assert not (cmd_root / "cli/uai/generated_commands/hjson_external_input").exists()
    docs = (
        cmd_root / "docs/active/t60_hjson_external_input_domain.md",
        cmd_root.parent
        / "Plugins/UeAgentInterface/docs/active/t60_hjson_external_input_domain.md",
    )
    for document in docs:
        text = document.read_text(encoding="utf-8")
        assert "client.content_graph.import_workspace" in text
        assert "client.content_graph.export_workspace" in text
        assert "command_search" in text and "command_detail" in text
        assert "uai-cli" in text
        assert "T13" in text and "recursive" in text and "initialization" in text
        assert "uai.generated_commands" not in text
