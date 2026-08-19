from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

import pytest

from uai.commands import BINDING_CATALOG, bind_generated_commands
from tools.uai_repository.migration_evidence import (
    historical_obligation_fingerprint,
    load_active_command_snapshot,
    load_historical_owner_obligations,
    validate_historical_successor,
)


COMMAND_IDS = (
    "landscape.create",
    "landscape.height_delta",
)

HISTORICAL_SUCCESSORS = {
    "landscape_create": ["landscape.create"],
    "landscape_raise_circle": ["landscape.height_delta"],
}


class _FakeClient:
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


def _require_bindings():
    bindings = {
        command_id: BINDING_CATALOG.find(command_id) for command_id in COMMAND_IDS
    }
    assert all(
        binding is not None
        and binding.command_id == command_id
        and binding.namespace == "landscape"
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in bindings.items()
    )
    return bindings


def _height_delta_params() -> dict[str, Any]:
    return {
        "delta": {"samples": [1.0]},
        "region": {"x": 0, "y": 0, "width": 1, "height": 1},
        "space_contract": {
            "semantic_frame_id": "landscape-local-sample-grid",
            "unit": "height-sample",
        },
        "target_ref": "/Game/StrictV2/T41/Landscape_Default",
    }


def test_both_landscape_commands_have_exact_default_bindings() -> None:
    assert len(COMMAND_IDS) == 2
    _require_bindings()


def test_default_height_delta_preserves_the_exact_request() -> None:
    _require_bindings()
    client = _FakeClient()
    params = _height_delta_params()
    bind_generated_commands(client).landscape.height_delta(**params)
    assert client.calls[0][0] == "landscape.height_delta"
    assert client.calls[0][1] == params


def test_named_and_generic_height_delta_use_the_same_exact_binding() -> None:
    bindings = _require_bindings()
    named = _FakeClient()
    generic = _FakeClient()
    params = _height_delta_params()
    bind_generated_commands(named).landscape.height_delta(**params)
    generic.execute_exact(
        "landscape.height_delta",
        params,
        contract_hash=bindings["landscape.height_delta"].binding_hash,
    )
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_ue_business_logic() -> None:
    _require_bindings()
    method = bind_generated_commands(_FakeClient()).landscape.height_delta
    names = set(method.__func__.__code__.co_names)
    assert not {
        "requests",
        "httpx",
        "urllib",
        "retry",
        "sleep",
        "registry",
        "prepare",
        "settle",
        "save",
        "reload",
        "rollback",
    } & names


def test_t41_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _require_bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper_root = (
        cmd_root
        / "cli"
        / "uai"
        / "generated_commands"
        / "t41_landscape_operation"
    )
    task_doc = cmd_root / "docs" / "active" / "t41_landscape_operation.md"
    plugin_doc = (
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t41_landscape_operation.md"
    )
    assert not helper_root.exists()
    for document in (task_doc, plugin_doc):
        text = document.read_text(encoding="utf-8")
        assert "client.landscape.create" in text
        assert "client.landscape.height_delta" in text
        assert "command_search" in text
        assert "command_detail" in text
        assert "uai-cli" in text
        assert "semantic_frame_id" in text
        assert "uai.generated_commands" not in text


@pytest.mark.historical_evidence
def test_t41_current_successor_consumes_both_complete_inventory_rows_and_product_receipt() -> None:
    project_root = Path(__file__).resolve().parents[3]
    plan_root = (
        project_root
        / "docs"
        / "plan"
        / "20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
    )
    obligations = load_historical_owner_obligations(
        plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json",
        owner_task_id="T41-LANDSCAPE-OPERATION",
    )
    expected_fingerprint = (
        "sha256:6c9a87a49e65ac1806a0efcee264d151f3151ff4f354073df30d4f7dc30a7a49"
    )
    assert historical_obligation_fingerprint(obligations) == expected_fingerprint
    assert {row["historical_command_id"] for row in obligations} == set(
        HISTORICAL_SUCCESSORS
    )

    successor = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/docs/active/successors"
            / "t41_landscape_operation.json"
        ).read_text(encoding="utf-8")
    )
    for row in successor["commands"]:
        assert row["successor"] == {
            "kind": "exact_command_set",
            "command_ids": HISTORICAL_SUCCESSORS[row["historical_command_id"]],
        }

    evidence_ref = (
        "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT/evidence/"
        "T41-LANDSCAPE-OPERATION-current-verification.json"
    )
    evidence_path = project_root / evidence_ref
    active_commands = load_active_command_snapshot(
        project_root / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    report = validate_historical_successor(
        document=successor,
        expected_owner_task_id="T41-LANDSCAPE-OPERATION",
        expected_row_ids=tuple(HISTORICAL_SUCCESSORS),
        expected_obligations=obligations,
        expected_obligation_fingerprint=expected_fingerprint,
        active_commands=active_commands,
        project_root=project_root,
        receipt_bindings=(
            {
                "test_id": "UAI.DeliveryWorkflow.T41.LANDSCAPE.OPERATION",
                "ref": evidence_ref,
                "sha256": hashlib.sha256(evidence_path.read_bytes()).hexdigest(),
                "active_registry_hash": active_commands.registry_hash,
                "public_command_ids": list(COMMAND_IDS),
                "assertions": [
                    {"pointer": "/status", "equals": "passed"},
                    {"pointer": "/historical_obligation_count", "equals": 2},
                    {"pointer": "/claims/public_to_real_ue", "equals": True},
                    {"pointer": "/claims/create_persisted", "equals": True},
                    {"pointer": "/claims/circle_raise_preserved", "equals": True},
                    {
                        "pointer": "/claims/independent_readback",
                        "equals": True,
                    },
                    {"pointer": "/claims/old_public_ids_absent", "equals": True},
                    {"pointer": "/claims/cleanup_confirmed", "equals": True},
                ],
            },
        ),
    )
    assert report.row_count == 2
    assert report.obligation_fingerprint == expected_fingerprint
