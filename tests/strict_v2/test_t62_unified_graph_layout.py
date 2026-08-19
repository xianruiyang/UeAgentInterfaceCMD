from __future__ import annotations

from pathlib import Path

from uai.commands import BINDING_CATALOG, bind_generated_commands


class _RecordingClient:
    def __init__(self) -> None:
        self.calls = []

    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id, params):
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(command_id, params, contract_hash=binding.binding_hash)


def test_t62_has_one_multi_target_public_contract() -> None:
    binding = BINDING_CATALOG.find("graph.layout.apply")
    assert binding is not None
    assert (binding.namespace, binding.method) == ("graph", "layout_apply")
    assert [item.name for item in binding.parameters] == [
        "targets",
        "strategy",
        "parameters",
        "authorization_id",
        "projection",
    ]


def test_t62_named_sdk_forwards_one_exact_multi_target_request() -> None:
    client = _RecordingClient()
    targets = [
        {
            "graph_identity": "/Game/UAI/T62/BP_A.BP_A:EventGraph",
            "expected_revision": "graph-layout:fixture",
        }
    ]
    bind_generated_commands(client).graph.layout_apply(
        targets,
        "hierarchical_left_to_right",
        {"horizontal_spacing": 320, "vertical_spacing": 160},
        "auth:t62:test",
    )
    binding = BINDING_CATALOG.find("graph.layout.apply")
    assert client.calls == [
        (
            "graph.layout.apply",
            {
                "targets": targets,
                "strategy": "hierarchical_left_to_right",
                "parameters": {
                    "horizontal_spacing": 320,
                    "vertical_spacing": 160,
                },
                "authorization_id": "auth:t62:test",
            },
            binding.binding_hash,
        )
    ]


def test_t62_has_no_domain_layout_aliases_or_task_helper() -> None:
    ids = {binding.command_id for binding in BINDING_CATALOG.bindings}
    forbidden = {
        "blueprint.layout.graph",
        "blueprint.layout.all_graphs",
        "animation_blueprint.layout.graph",
        "material.layout.graph",
        "niagara.layout.graph",
        "pcg.layout.graph",
    }
    assert not (ids & forbidden)
    root = Path(__file__).resolve().parents[2]
    assert not (root / "cli/uai/generated_commands/unified_graph_layout").exists()
    for path in (
        root / "docs/active/t62_unified_graph_layout.md",
        root.parent / "Plugins/UeAgentInterface/docs/active/t62_unified_graph_layout.md",
    ):
        text = path.read_text(encoding="utf-8")
        assert "client.graph.layout_apply" in text
        assert "targets" in text and "expected_revision" in text
        assert "command_search" in text and "command_detail" in text
