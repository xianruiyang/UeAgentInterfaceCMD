from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

import pytest

from uai.commands import BINDING_CATALOG, bind_generated_commands
from tools.uai_repository.migration_evidence import (
    LegacyReferenceSpec,
    load_active_command_snapshot,
    scan_legacy_references,
)


COMMAND_ID = "reference.asset_apply"
DEFAULT_METHOD = ("reference", "asset_apply")


class _FakeClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(self, command_id, params, *, contract_hash):
        self.calls.append((command_id, dict(params), contract_hash))
        return {"ok": True}

    def execute(self, command_id, params):
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(command_id, params, contract_hash=binding.binding_hash)


def _binding():
    binding = BINDING_CATALOG.find(COMMAND_ID)
    assert binding is not None
    assert (binding.namespace, binding.method) == DEFAULT_METHOD
    assert re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
    assert binding.binding_hash != "sha256:" + "0" * 64
    return binding


def _params(binding) -> dict[str, Any]:
    values = {"string": "fixture", "integer": 1, "number": 1.0, "boolean": True, "array": [], "object": {}}
    return {item.name: values.get(item.wire_type, {}) for item in binding.parameters}


def _named(client: _FakeClient, binding, params: dict[str, Any]) -> None:
    getattr(getattr(bind_generated_commands(client), binding.namespace), binding.method)(**params)


def test_reference_command_has_one_exact_default_binding() -> None:
    _binding()


def test_default_named_method_preserves_one_exact_request() -> None:
    binding = _binding()
    client = _FakeClient()
    params = _params(binding)
    _named(client, binding, params)
    assert client.calls == [(COMMAND_ID, params, binding.binding_hash)]


def test_named_and_generic_methods_use_the_same_exact_binding() -> None:
    binding = _binding()
    named, generic = _FakeClient(), _FakeClient()
    params = _params(binding)
    _named(named, binding, params)
    generic.execute_exact(COMMAND_ID, params, contract_hash=binding.binding_hash)
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_ue_business_logic() -> None:
    binding = _binding()
    method = getattr(getattr(bind_generated_commands(_FakeClient()), binding.namespace), binding.method)
    names = set(method.__func__.__code__.co_names)
    assert not {"requests", "httpx", "urllib", "retry", "sleep", "registry", "save", "reload", "rollback"} & names


def test_t43_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _binding()
    cmd_root = Path(__file__).resolve().parents[2]
    helper = cmd_root / "cli" / "uai" / "generated_commands" / "t43_reference_operation"
    docs = (
        cmd_root / "docs" / "active" / "t43_reference_operation.md",
        cmd_root.parent / "Plugins" / "UeAgentInterface" / "docs" / "active" / "t43_reference_operation.md",
    )
    assert not helper.exists()
    for document in docs:
        text = document.read_text(encoding="utf-8")
        assert "client.reference.asset_apply" in text
        assert "reference.asset_read" in text
        assert "BlueprintDisplayName" in text
        assert "/Game/UAI/Owned/" not in text
        assert "command_search" in text and "command_detail" in text and "uai-cli" in text
        assert "uai.generated_commands" not in text


@pytest.mark.historical_evidence
def test_t43_consumes_current_manifest_receipt_and_legacy_exit_adapter() -> None:
    project_root = Path(__file__).resolve().parents[3]
    active = load_active_command_snapshot(
        project_root / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    assert {"reference.asset_apply", "reference.asset_read"} <= active.command_ids

    evidence_path = (
        project_root
        / "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT/evidence"
        / "T43-REFERENCE-OPERATION-current-verification.json"
    )
    evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    assert evidence["status"] == "passed"
    assert evidence["active_registry_hash"] == active.registry_hash
    assert evidence["claims"]["public_to_real_ue"] is True
    assert evidence["claims"]["independent_readback"] is True
    assert evidence["claims"]["legacy_public_owner_inactive"] is True
    for receipt in evidence["receipts"]:
        path = project_root / receipt["ref"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == receipt["sha256"]

    report = scan_legacy_references(
        active_roots=(
            project_root / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json",
            project_root / "Plugins/UeAgentInterface/docs/active/t43_reference_operation.md",
            project_root / "UeAgentInterfaceCMD/docs/active/t43_reference_operation.md",
            project_root
            / "Plugins/UeAgentInterface/Source/UeAgentInterface/Private"
            / "Module/CommandRegistration/Reference",
        ),
        specs=(
            LegacyReferenceSpec(
                identity="legacy-reference-apply-handler",
                surface="active-product-authority",
                exact_tokens=("FAssetApplyHandler", "TryCreateReferenceCommandHandlers"),
            ),
        ),
    )
    report.require_zero_active_references()
