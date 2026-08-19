from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
from pathlib import Path

import pytest

TESTS_DIR = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(TESTS_DIR / "support"))

from migration_evidence import REPRESENTATIVE_CALIBRATIONS
from tools.uai_repository.migration_evidence import (
    EvidenceValidationError,
    LegacyReferenceSpec,
    build_historical_successor,
    historical_obligation_fingerprint,
    load_active_command_snapshot,
    load_historical_owner_obligations,
    scan_legacy_references,
    validate_historical_successor,
)


PLAN_ROOT = (
    PROJECT_ROOT
    / "docs"
    / "plan"
    / "20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT"
)
HISTORICAL_INVENTORY = PLAN_ROOT / "UAI_PRE_REFACTOR_COMMAND_TASK_INVENTORY.json"


def _load_successor(ref: str) -> dict[str, object]:
    return json.loads((PROJECT_ROOT / ref).read_text(encoding="utf-8"))


def _calibration(index: int = 0):
    return REPRESENTATIVE_CALIBRATIONS[index]


def _owner_obligations(index: int = 0):
    calibration = _calibration(index)
    return load_historical_owner_obligations(
        HISTORICAL_INVENTORY,
        owner_task_id=calibration.owner_task_id,
    )


def _current_fixture_bindings(
    index: int,
    fixture_root: Path,
) -> tuple[dict[str, object], ...]:
    document = _load_successor(_calibration(index).successor_ref)
    active_commands = load_active_command_snapshot(
        PROJECT_ROOT / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    by_test_id: dict[str, set[str]] = {}
    for command in document["commands"]:
        product = command["product_evidence"]
        by_test_id.setdefault(product["test_id"], set()).update(
            product["public_command_ids"]
        )
    bindings = []
    for ordinal, (test_id, command_ids) in enumerate(sorted(by_test_id.items())):
        receipt_ref = f"receipt-{ordinal}.json"
        receipt_path = fixture_root / receipt_ref
        receipt_path.write_text('{"status":"passed"}\n', encoding="utf-8")
        bindings.append(
            {
                "test_id": test_id,
                "ref": receipt_ref,
                "sha256": hashlib.sha256(receipt_path.read_bytes()).hexdigest(),
                "active_registry_hash": active_commands.registry_hash,
                "public_command_ids": sorted(command_ids),
                "assertions": [{"pointer": "/status", "equals": "passed"}],
            }
        )
    return tuple(bindings)


def _validate(index: int = 0, document: dict[str, object] | None = None):
    calibration = _calibration(index)
    active_commands = load_active_command_snapshot(
        PROJECT_ROOT / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    assert calibration.active_command_ids.issubset(active_commands.command_ids)
    with tempfile.TemporaryDirectory() as raw_fixture_root:
        fixture_root = Path(raw_fixture_root)
        return validate_historical_successor(
            document=document or _load_successor(calibration.successor_ref),
            expected_owner_task_id=calibration.owner_task_id,
            expected_row_ids=calibration.expected_row_ids,
            expected_obligations=_owner_obligations(index),
            expected_obligation_fingerprint=calibration.expected_obligation_fingerprint,
            active_commands=active_commands,
            project_root=fixture_root,
            receipt_bindings=_current_fixture_bindings(index, fixture_root),
        )


def _assert_code(code: str, action) -> None:
    with pytest.raises(EvidenceValidationError) as caught:
        action()
    assert caught.value.code == code


def test_representative_owner_documents_consume_exact_rows_and_current_receipts() -> None:
    counts = []
    for index, calibration in enumerate(REPRESENTATIVE_CALIBRATIONS):
        before = (PROJECT_ROOT / calibration.successor_ref).read_bytes()
        report = _validate(index)
        after = (PROJECT_ROOT / calibration.successor_ref).read_bytes()

        assert report.owner_task_id == calibration.owner_task_id
        assert report.row_count == len(calibration.expected_row_ids)
        assert report.obligation_fingerprint == calibration.expected_obligation_fingerprint
        assert report.current_product_receipt_count >= 1
        assert before == after
        counts.append(report.row_count)

    assert counts == [11, 15, 20]


def test_owner_row_fingerprint_and_inference_fail_independently() -> None:
    original = _load_successor(_calibration().successor_ref)

    wrong_owner = copy.deepcopy(original)
    wrong_owner["owner_task_id"] = "T99-FINAL-AUDIT"
    _assert_code("owner_mismatch", lambda: _validate(document=wrong_owner))

    missing_row = copy.deepcopy(original)
    missing_row["commands"] = missing_row["commands"][:-1]
    _assert_code("row_set_mismatch", lambda: _validate(document=missing_row))

    drifted_obligations = copy.deepcopy(list(_owner_obligations()))
    drifted_obligations[0]["historical_contract"]["purpose"] += " drift"
    calibration = _calibration()
    _assert_code(
        "obligation_fingerprint_mismatch",
        lambda: validate_historical_successor(
            document=original,
            expected_owner_task_id=calibration.owner_task_id,
            expected_row_ids=calibration.expected_row_ids,
            expected_obligations=drifted_obligations,
            expected_obligation_fingerprint=calibration.expected_obligation_fingerprint,
            active_commands=load_active_command_snapshot(
                PROJECT_ROOT / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
            ),
            project_root=PROJECT_ROOT,
            receipt_bindings=calibration.receipt_bindings,
        ),
    )

    drifted_projection = copy.deepcopy(original)
    drifted_projection["commands"][0]["historical_contract"]["purpose"] += " drift"
    _assert_code(
        "obligation_projection_mismatch",
        lambda: _validate(document=drifted_projection),
    )

    inferred = copy.deepcopy(original)
    inferred["commands"][0]["successor"]["inferred_by"] = "namespace"
    _assert_code("successor_inference_forbidden", lambda: _validate(document=inferred))


def test_placeholder_unknown_current_id_and_stale_receipt_fail_independently() -> None:
    original = _load_successor(_calibration().successor_ref)

    placeholder = copy.deepcopy(original)
    placeholder["commands"][0]["semantic_coverage"]["purpose"]["explanation"] = "TODO and/or fallback"
    _assert_code("placeholder_or_ambiguous_resolution", lambda: _validate(document=placeholder))

    unknown_id = copy.deepcopy(original)
    unknown_id["commands"][0]["successor"]["command_ids"] = ["content_graph.import_nearby"]
    unknown_id["commands"][0]["semantic_coverage"]["purpose"]["by"] = ["content_graph.import_nearby"]
    unknown_id["commands"][0]["semantic_coverage"]["inputs"]["by"] = ["content_graph.import_nearby"]
    unknown_id["commands"][0]["semantic_coverage"]["outputs"]["by"] = ["content_graph.import_nearby"]
    unknown_id["commands"][0]["product_evidence"]["public_command_ids"] = ["content_graph.import_nearby"]
    _assert_code("unknown_current_command", lambda: _validate(document=unknown_id))

    calibration = _calibration()
    active_commands = load_active_command_snapshot(
        PROJECT_ROOT / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    with tempfile.TemporaryDirectory() as raw_fixture_root:
        fixture_root = Path(raw_fixture_root)
        stale_bindings = [
            copy.deepcopy(item)
            for item in _current_fixture_bindings(0, fixture_root)
        ]
        stale_bindings[0]["sha256"] = "0" * 64
        _assert_code(
            "receipt_hash_mismatch",
            lambda: validate_historical_successor(
                document=original,
                expected_owner_task_id=calibration.owner_task_id,
                expected_row_ids=calibration.expected_row_ids,
                expected_obligations=_owner_obligations(),
                expected_obligation_fingerprint=calibration.expected_obligation_fingerprint,
                active_commands=active_commands,
                project_root=fixture_root,
                receipt_bindings=stale_bindings,
            ),
        )


def test_builder_requires_all_owner_rows_and_roundtrips_without_business_inference() -> None:
    calibration = _calibration(2)
    source = _load_successor(calibration.successor_ref)
    commands = copy.deepcopy(source["commands"])

    built = build_historical_successor(
        owner_task_id=calibration.owner_task_id,
        approval_authority=copy.deepcopy(source["approval_authority"]),
        expected_row_ids=calibration.expected_row_ids,
        expected_obligations=_owner_obligations(2),
        expected_obligation_fingerprint=calibration.expected_obligation_fingerprint,
        command_decisions=commands,
    )
    assert built == source
    assert built is not source

    _assert_code(
        "row_set_mismatch",
        lambda: build_historical_successor(
            owner_task_id=calibration.owner_task_id,
            approval_authority=copy.deepcopy(source["approval_authority"]),
            expected_row_ids=calibration.expected_row_ids,
            expected_obligations=_owner_obligations(2),
            expected_obligation_fingerprint=calibration.expected_obligation_fingerprint,
            command_decisions=commands[:-1],
        ),
    )


def test_active_command_validation_is_loaded_from_the_formal_manifest(tmp_path: Path) -> None:
    manifest_path = PROJECT_ROOT / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    snapshot = load_active_command_snapshot(manifest_path)
    raw = manifest_path.read_bytes()
    document = json.loads(raw.decode("utf-8-sig"))
    assert snapshot.registry_hash == document["registry_hash"]
    assert snapshot.manifest_sha256 == "sha256:" + hashlib.sha256(raw).hexdigest()
    assert snapshot.command_ids == frozenset(
        command["command_id"] for command in document["commands"]
    )

    broken = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    broken["commands"].append(copy.deepcopy(broken["commands"][0]))
    broken_path = tmp_path / "duplicate-manifest.json"
    broken_path.write_text(json.dumps(broken), encoding="utf-8")
    _assert_code("active_manifest_duplicate", lambda: load_active_command_snapshot(broken_path))


def test_exact_legacy_reference_scan_blocks_each_declared_active_surface(tmp_path: Path) -> None:
    active = tmp_path / "active"
    historical = tmp_path / "historical"
    active.mkdir()
    historical.mkdir()
    surfaces = ("command", "provider", "handler", "test", "gate", "doc")
    specs = []
    for surface in surfaces:
        token = f"legacy_{surface}_identity"
        suffix = ".md" if surface == "doc" else ".txt"
        (active / f"{surface}{suffix}").write_text(f"active {token}\n", encoding="utf-8")
        (historical / f"{surface}{suffix}").write_text(f"historical {token}\n", encoding="utf-8")
        specs.append(LegacyReferenceSpec(identity=token, surface=surface, exact_tokens=(token,)))

    report = scan_legacy_references(
        active_roots=(active, historical),
        specs=tuple(specs),
        allowed_historical_roots=(historical,),
    )
    assert {match.surface for match in report.active_matches} == set(surfaces)
    assert report.allowed_historical_match_count == len(surfaces)
    _assert_code("active_legacy_reference", report.require_zero_active_references)

    for path in active.iterdir():
        path.write_text(
            "\n".join(f"nearby{spec.identity}suffix" for spec in specs),
            encoding="utf-8",
        )
    clean = scan_legacy_references(active_roots=(active,), specs=tuple(specs))
    assert clean.active_matches == ()
    clean.require_zero_active_references()


def test_formal_schema_is_the_single_documented_v2_structure() -> None:
    schema_path = (
        PROJECT_ROOT
        / "Plugins/UeAgentInterface/docs/active/schemas/uai.historical_successor.v2.schema.json"
    )
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    assert schema["$id"] == "uai.historical_successor.v2"
    assert schema["properties"]["schema"]["const"] == "uai.historical_successor.v2"
    assert schema["required"] == ["schema", "owner_task_id", "approval_authority", "commands"]


def test_complete_inventory_rows_are_the_obligation_fingerprint_authority() -> None:
    for index, calibration in enumerate(REPRESENTATIVE_CALIBRATIONS):
        rows = _owner_obligations(index)
        assert {row["historical_command_id"] for row in rows} == set(
            calibration.expected_row_ids
        )
        assert (
            historical_obligation_fingerprint(rows)
            == calibration.expected_obligation_fingerprint
        )
