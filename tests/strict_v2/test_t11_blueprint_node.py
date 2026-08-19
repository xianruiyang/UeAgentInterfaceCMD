from __future__ import annotations

from pathlib import Path
from typing import Any
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands


COMMAND_ID = "blueprint.node.candidates"


class _RecordingClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(
        self,
        command_id: str,
        params: dict[str, Any],
        *,
        contract_hash: str,
    ) -> dict[str, object]:
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id: str, params: dict[str, Any]) -> dict[str, object]:
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


def _binding():
    binding = BINDING_CATALOG.find(COMMAND_ID)
    assert binding is not None
    assert binding.namespace == "blueprint"
    assert binding.method == "node_candidates"
    assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
    assert binding.binding_hash != "sha256:" + "0" * 64
    return binding


def _params() -> dict[str, Any]:
    return {
        "target": "/Game/UAI/StrictV2/T11/BP_NodeFixture.BP_NodeFixture",
        "graph_id": "graph:12345678-1234-1234-1234-123456789abc",
        "query": "branch",
    }


def test_candidate_default_binding_preserves_public_target_and_graph_identity() -> None:
    _binding()
    client = _RecordingClient()
    params = _params()
    bind_generated_commands(client).blueprint.node_candidates(**params)
    assert client.calls[0][0] == COMMAND_ID
    assert client.calls[0][1] == params


def test_named_and_generic_execution_use_the_same_exact_binding() -> None:
    binding = _binding()
    named = _RecordingClient()
    generic = _RecordingClient()
    params = _params()
    bind_generated_commands(named).blueprint.node_candidates(**params)
    generic.execute_exact(COMMAND_ID, params, contract_hash=binding.binding_hash)
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_ue_business() -> None:
    _binding()
    method = bind_generated_commands(_RecordingClient()).blueprint.node_candidates
    names = set(method.__func__.__code__.co_names)
    assert not {
        "requests",
        "httpx",
        "urllib",
        "retry",
        "sleep",
        "FBlueprintActionDatabase",
        "UBlueprintNodeSpawner",
        "compile",
        "save",
        "reload",
    } & names


def test_t11_has_one_default_binding_and_no_task_projection_authority() -> None:
    _binding()
    cmd_root = Path(__file__).resolve().parents[2]
    project_root = cmd_root.parent
    helper = cmd_root / "cli" / "uai" / "generated_commands" / "blueprint_node"
    assert not helper.exists()

    docs = (
        cmd_root / "docs" / "active" / "t11_blueprint_node.md",
        project_root
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t11_blueprint_node.md",
    )
    for document in docs:
        text = document.read_text(encoding="utf-8")
        assert "client.blueprint.node_candidates" in text
        assert "command_search" in text and "command_detail" in text
        assert "uai-cli" in text
        assert "uai.generated_commands" not in text

    registration = (
        project_root
        / "Plugins"
        / "UeAgentInterface"
        / "Source"
        / "UeAgentInterface"
        / "Private"
        / "Module"
        / "CommandRegistration"
        / "BlueprintNode"
        / "UeAgentBlueprintNodeRegistration.cpp"
    ).read_text(encoding="utf-8")
    assert 'Result.PythonNamespace = TEXT("blueprint")' in registration
    assert 'Result.PythonFunction = TEXT("node_candidates")' in registration
    assert "blueprint_node_candidates(client" not in registration
