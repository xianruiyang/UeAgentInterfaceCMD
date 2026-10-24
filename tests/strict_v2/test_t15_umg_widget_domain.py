from __future__ import annotations

import re

from uai.commands import _BINDING_CATALOG, bind_generated_commands


COMMAND_BINDINGS = {
    "content_graph.compound": ("content_graph", "compound"),
    "content_graph.diagnostics": ("content_graph", "diagnostics"),
    "content_graph.export_workspace": ("content_graph", "export_workspace"),
    "content_graph.import_workspace": ("content_graph", "import_workspace"),
    "content_graph.items": ("content_graph", "items"),
    "content_graph.properties": ("content_graph", "properties"),
    "content_graph.relations": ("content_graph", "relations"),
    "content_graph.structure": ("content_graph", "structure"),
    "content_graph.summary": ("content_graph", "summary"),
}


class _RecordingClient:
    def __init__(self):
        self.calls = []

    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id, params):
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            command_id, params, contract_hash=binding.binding_hash
        )


def test_t15_uses_only_default_umg_and_content_graph_bindings() -> None:
    for command_id, expected_projection in COMMAND_BINDINGS.items():
        binding = _BINDING_CATALOG.find(command_id)
        assert binding is not None
        assert (binding.namespace, binding.method) == expected_projection
        assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)


def test_t15_default_domain_ingress_forwards_exact_source_union() -> None:
    client = _RecordingClient()
    document = (
        '{schema:"uai.umg.edit/1",root:{type:"/Script/UMGEditor.WidgetBlueprint",'
        'document:{operation:update,target:{asset_path:"/Game/UAI/WBP_T15"},'
        'provider_extension:{widget_tree:{widgets:{}}}}}}'
    )
    bind_generated_commands(client).content_graph.import_workspace(
        "/Game/UAI/WBP_T15.WBP_T15",
        {"kind": "inline", "document": document},
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.import_workspace"
    assert params == {
        "target": "/Game/UAI/WBP_T15.WBP_T15",
        "source": {"kind": "inline", "document": document},
    }
    assert contract_hash == _BINDING_CATALOG.find(command_id).binding_hash


def test_t15_default_content_graph_readback_preserves_identity() -> None:
    client = _RecordingClient()
    bind_generated_commands(client).content_graph.structure(
        "/Game/UAI/WBP_T15.WBP_T15"
    )
    command_id, params, contract_hash = client.calls[0]
    assert command_id == "content_graph.structure"
    assert params == {"target": "/Game/UAI/WBP_T15.WBP_T15"}
    assert contract_hash == _BINDING_CATALOG.find(command_id).binding_hash


def test_t15_default_bindings_contain_no_umg_or_recursive_business() -> None:
    commands = bind_generated_commands(_RecordingClient())
    names = set(commands.content_graph.import_workspace.__func__.__code__.co_names)
    assert not {
        "uwidget",
        "widget_tree",
        "slot",
        "recursive",
        "initialization",
        "compile",
        "save",
        "unload",
        "reload",
        "cleanup",
    } & names
