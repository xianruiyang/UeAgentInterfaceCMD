from __future__ import annotations

from pathlib import Path
from typing import Any
import hashlib
import json
import re

from uai.commands import BINDING_CATALOG, bind_generated_commands
from tools.uai_repository.migration_evidence import (
    historical_obligation_fingerprint,
    load_active_command_snapshot,
    load_historical_owner_obligations,
    validate_historical_successor,
)


METHODS = {
    "capture.image.execute": ("capture", "image_execute"),
    "capture.media.execute": ("capture", "media_execute"),
    "capture.render.execute": ("capture", "render_execute"),
}

HISTORICAL_IMAGE_POLICIES = {
    "anim_blueprint_screenshot": "policy:image-capture:anim-blueprint/v1",
    "anim_sequence_screenshot": "policy:image-capture:anim-sequence/v1",
    "behavior_tree_screenshot": "policy:image-capture:behavior-tree/v1",
    "blueprint_screenshot": "policy:image-capture:blueprint/v1",
    "control_rig_screenshot": "policy:image-capture:control-rig/v1",
    "metasound_screenshot": "policy:image-capture:metasound/v1",
    "niagara_screenshot": "policy:image-capture:niagara/v1",
    "pcg_screenshot": "policy:image-capture:pcg-viewport/v1",
    "screenshot_viewport": "policy:image-capture:viewport/v1",
    "screenshot_viewport_buffer": "policy:image-capture:viewport-buffer/v1",
    "sequence_screenshot": "policy:image-capture:level-sequence/v1",
    "sound_cue_screenshot": "policy:image-capture:sound-cue/v1",
    "state_tree_screenshot": "policy:image-capture:state-tree/v1",
    "texture_screenshot": "policy:image-capture:texture/v1",
    "umg_screenshot": "policy:image-capture:umg/v1",
}

EXPECTED_OBLIGATION_FINGERPRINT = (
    "sha256:59dcff08ce40dcad3637a73007809426c55a1bf4812855957b28a66fed3a8772"
)


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


def _bindings():
    values = {command_id: BINDING_CATALOG.find(command_id) for command_id in METHODS}
    assert all(
        binding is not None
        and (binding.namespace, binding.method) == METHODS[command_id]
        and re.fullmatch(r"sha256:[0-9a-f]{64}", binding.binding_hash)
        and binding.binding_hash != "sha256:" + "0" * 64
        for command_id, binding in values.items()
    )
    return values


def _params(binding) -> dict[str, Any]:
    samples = {"string": "fixture", "integer": 1, "number": 1.0, "boolean": True, "array": [], "object": {}}
    return {item.name: samples.get(item.wire_type, {}) for item in binding.parameters}


def _named(client, binding, params) -> None:
    getattr(getattr(bind_generated_commands(client), binding.namespace), binding.method)(**params)


def test_all_three_capture_commands_have_exact_default_bindings() -> None:
    assert len(METHODS) == 3
    _bindings()


def test_default_capture_method_preserves_one_exact_request() -> None:
    binding = _bindings()["capture.image.execute"]
    client = _FakeClient()
    params = _params(binding)
    _named(client, binding, params)
    assert client.calls == [(binding.command_id, params, binding.binding_hash)]


def test_named_and_generic_capture_use_the_same_exact_binding() -> None:
    binding = _bindings()["capture.render.execute"]
    named, generic = _FakeClient(), _FakeClient()
    params = _params(binding)
    _named(named, binding, params)
    generic.execute_exact(binding.command_id, params, contract_hash=binding.binding_hash)
    assert named.calls == generic.calls


def test_default_projection_contains_no_transport_or_capture_business_logic() -> None:
    binding = _bindings()["capture.media.execute"]
    method = getattr(getattr(bind_generated_commands(_FakeClient()), binding.namespace), binding.method)
    names = set(method.__func__.__code__.co_names)
    assert not {"requests", "httpx", "urllib", "retry", "sleep", "registry", "capture", "render", "cancel", "poll"} & names


def test_t44_has_no_task_specific_binding_or_tutorial_authority() -> None:
    _bindings()
    cmd_root = Path(__file__).resolve().parents[2]
    helper = cmd_root / "cli" / "uai" / "generated_commands" / "capture_media"
    docs = (
        cmd_root / "docs" / "active" / "t44_capture_media_operation.md",
        cmd_root.parent / "Plugins" / "UeAgentInterface" / "docs" / "active" / "t44_capture_media_operation.md",
    )
    assert not helper.exists()
    for document in docs:
        text = document.read_text(encoding="utf-8")
        for _, method in METHODS.values():
            assert f"client.capture.{method}" in text
        assert "command_search" in text and "command_detail" in text and "uai-cli" in text
        assert "uai.generated_commands" not in text


def test_t44_docs_name_every_historical_image_policy_and_exact_parameter_route() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    docs = (
        cmd_root / "docs" / "active" / "t44_capture_media_operation.md",
        cmd_root.parent
        / "Plugins"
        / "UeAgentInterface"
        / "docs"
        / "active"
        / "t44_capture_media_operation.md",
    )
    for document in docs:
        text = document.read_text(encoding="utf-8")
        assert "subject_ref" in text and "policy_id" in text and "parameters" in text
        for historical_id, policy_id in HISTORICAL_IMAGE_POLICIES.items():
            assert historical_id in text
            assert policy_id in text


def test_t44_historical_successor_consumes_all_15_frozen_rows_exactly() -> None:
    project_root = Path(__file__).resolve().parents[3]
    plan_root = (
        project_root
        / "docs"
        / "plan"
        / "20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
    )
    annex = plan_root / "UAI_PRE_REFACTOR_COMMAND_APPROVAL.md"
    assert hashlib.sha256(annex.read_bytes()).hexdigest() == (
        "3972f62273a13c8c8a971d7e31924e08c8fc59dad9f35abbb87089728c1c265e"
    )
    inventory = json.loads(
        (plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json").read_text(
            encoding="utf-8"
        )
    )
    frozen_rows = [
        row
        for row in inventory["commands"]
        if row.get("target_task_id") == "T44-CAPTURE-MEDIA-OPERATION"
    ]
    assert len(frozen_rows) == 15
    assert {row["historical_command_id"] for row in frozen_rows} == set(
        HISTORICAL_IMAGE_POLICIES
    )

    successor = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/docs/active/successors"
            / "t44_capture_media_operation.json"
        ).read_text(encoding="utf-8")
    )
    assert successor["schema"] == "uai.historical_successor.v2"
    assert successor["owner_task_id"] == "T44-CAPTURE-MEDIA-OPERATION"
    rows = {row["historical_command_id"]: row for row in successor["commands"]}
    assert set(rows) == set(HISTORICAL_IMAGE_POLICIES)
    for frozen in frozen_rows:
        historical_id = frozen["historical_command_id"]
        row = rows[historical_id]
        assert row["historical_contract"] == frozen["historical_contract"]
        assert row["resolved_from_contract_id"] == frozen["semantic_resolution"][
            "contract_id"
        ]
        assert row["successor"] == {
            "kind": "exact_command_set",
            "command_ids": ["capture.image.execute"],
            "policy_id": HISTORICAL_IMAGE_POLICIES[historical_id],
        }
        assert all(
            row["semantic_coverage"][axis]["status"] == "covered"
            for axis in ("purpose", "inputs", "outputs")
        )
        assert set(row["old_id_exit"].values()) == {False}


def test_t44_old_ids_are_absent_from_current_manifest_and_sdk() -> None:
    project_root = Path(__file__).resolve().parents[3]
    active = load_active_command_snapshot(
        project_root / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    assert set(HISTORICAL_IMAGE_POLICIES).isdisjoint(active.command_ids)
    assert all(
        BINDING_CATALOG.find(command_id) is None
        for command_id in HISTORICAL_IMAGE_POLICIES
    )


def test_t44_current_successor_consumes_fingerprint_and_product_receipt() -> None:
    project_root = Path(__file__).resolve().parents[3]
    plan_root = (
        project_root
        / "docs"
        / "plan"
        / "20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
    )
    obligations = load_historical_owner_obligations(
        plan_root / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json",
        owner_task_id="T44-CAPTURE-MEDIA-OPERATION",
    )
    assert historical_obligation_fingerprint(obligations) == (
        EXPECTED_OBLIGATION_FINGERPRINT
    )
    successor = json.loads(
        (
            project_root
            / "Plugins/UeAgentInterface/docs/active/successors"
            / "t44_capture_media_operation.json"
        ).read_text(encoding="utf-8")
    )
    evidence_ref = (
        "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT/evidence/"
        "T44-CAPTURE-MEDIA-OPERATION-current-verification.json"
    )
    evidence_path = project_root / evidence_ref
    active_commands = load_active_command_snapshot(
        project_root / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    report = validate_historical_successor(
        document=successor,
        expected_owner_task_id="T44-CAPTURE-MEDIA-OPERATION",
        expected_row_ids=tuple(HISTORICAL_IMAGE_POLICIES),
        expected_obligations=obligations,
        expected_obligation_fingerprint=EXPECTED_OBLIGATION_FINGERPRINT,
        active_commands=active_commands,
        project_root=project_root,
        receipt_bindings=(
            {
                "test_id": "UAI.DeliveryWorkflow.T44.CAPTURE.MEDIA.OPERATION",
                "ref": evidence_ref,
                "sha256": hashlib.sha256(evidence_path.read_bytes()).hexdigest(),
                "active_registry_hash": active_commands.registry_hash,
                "public_command_ids": [
                    "capture.image.execute",
                    "operation.cancel",
                    "operation.release",
                    "operation.status",
                ],
                "assertions": [
                    {"pointer": "/status", "equals": "passed"},
                    {"pointer": "/historical_obligation_count", "equals": 15},
                    {"pointer": "/claims/public_to_real_ue", "equals": True},
                    {"pointer": "/claims/real_image_capture", "equals": True},
                    {"pointer": "/claims/independent_readback", "equals": True},
                    {"pointer": "/claims/reattach_cancel_release", "equals": True},
                    {"pointer": "/claims/old_public_ids_absent", "equals": True},
                    {"pointer": "/claims/cleanup_confirmed", "equals": True},
                    {"pointer": "/claims/editor_preserved", "equals": True},
                ],
            },
        ),
    )
    assert report.row_count == 15
    assert report.obligation_fingerprint == EXPECTED_OBLIGATION_FINGERPRINT
