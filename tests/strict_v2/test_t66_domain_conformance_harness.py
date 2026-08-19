from __future__ import annotations

import json
from pathlib import Path

import pytest

from tests.support.domain_conformance import (
    ConformanceError,
    DomainFixture,
    LayerEvidence,
    ProductEvidence,
    build_equivalent_sources,
    build_owned_worker_plan,
    validate_product_evidence,
    validate_representative_calibrations,
)


def fixture(tmp_path: Path) -> DomainFixture:
    return DomainFixture(
        fixture_id="fixture:t66:python",
        domain_id="fixture-python-domain",
        target_identity="/Game/UAI/T66/Python.Python",
        base_revision="absent",
        entry_file="asset.hjson",
        document=(
            "{\n"
            "  schema: uai.fixture.python/1\n"
            "  target_identity: /Game/UAI/T66/Python.Python\n"
            "  values: { label: Python }\n"
            "}\n"
        ),
        workspace_root=tmp_path,
        mechanics_family="fixture_python_mechanics",
        public_route_id="content_graph.import_workspace",
        public_test_ids=("UAI.Fixture.Python.Public",),
    )


def test_equivalent_sources_write_public_union_and_integrity_manifest(
    tmp_path: Path,
) -> None:
    sources = build_equivalent_sources(fixture(tmp_path))
    assert [source["kind"] for source in sources] == [
        "inline",
        "single_file",
        "directory",
    ]
    assert sources[0]["document"] == fixture(tmp_path).document
    assert Path(sources[1]["path"]).read_text(encoding="utf-8") == sources[0]["document"]
    manifest = json.loads(
        (Path(sources[2]["path"]) / ".uai" / "workspace.hjson").read_text(
            encoding="utf-8"
        )
    )
    assert manifest["workspace_schema"] == "uai.content_graph.workspace/1"
    assert manifest["target_identity"] == fixture(tmp_path).target_identity
    assert manifest["entry_file"] == fixture(tmp_path).entry_file
    assert manifest["files"][0]["content_hash"].startswith("sha256:")


def test_owned_worker_plan_requires_both_low_cost_layers(tmp_path: Path) -> None:
    current = fixture(tmp_path)
    with pytest.raises(ConformanceError, match="domain_adapter"):
        build_owned_worker_plan(
            [current],
            LayerEvidence(static_contract="static.json", domain_adapter=None),
            tmp_path / "runtime",
        )
    plan = build_owned_worker_plan(
        [current],
        LayerEvidence(static_contract="static.json", domain_adapter="adapter.json"),
        tmp_path / "runtime",
    )
    assert plan["schema"] == "uai.ue_test_plan.v1"
    assert plan["preserve_main_editor"] is True
    assert len(plan["batches"]) == 1
    batch = plan["batches"][0]
    assert batch["requires_headless"] is True
    assert batch["requires_rhi"] is False
    assert batch["cleanup_policy"] == "owned_processes_and_temp_artifacts"
    assert batch["cases"] == [
        {"test_id": "UAI.Fixture.Python.Public", "filter": "UAI.Fixture.Python.Public"}
    ]


def test_synthetic_or_incomplete_receipt_cannot_become_product_ready(
    tmp_path: Path,
) -> None:
    current = fixture(tmp_path)
    with pytest.raises(ConformanceError, match="synthetic"):
        validate_product_evidence(
            current,
            ProductEvidence(
                route_id=current.public_route_id,
                receipt_ref="receipt.json",
                receipt_exists=True,
                synthetic=True,
                public_route_observed=False,
                independent_readback_observed=False,
                cleanup_observed=False,
            ),
        )
    with pytest.raises(ConformanceError, match="incomplete"):
        validate_product_evidence(
            current,
            ProductEvidence(
                route_id=current.public_route_id,
                receipt_ref="receipt.json",
                receipt_exists=True,
                synthetic=False,
                public_route_observed=True,
                independent_readback_observed=False,
                cleanup_observed=True,
            ),
        )


def test_representative_calibration_is_bounded_and_current() -> None:
    project_root = Path(__file__).resolve().parents[3]
    calibration_path = (
        project_root
        / "Plugins/UeAgentInterface/Source/UeAgentInterfaceTests/Private/Fixtures/DomainConformance/t13_t27_t30.json"
    )
    calibrated = validate_representative_calibrations(project_root, calibration_path)
    assert [item["domain_id"] for item in calibrated] == [
        "uobject-dataasset",
        "datatable-curvetable",
        "localization-string-table",
    ]
    assert all(item["bounded_claim"] for item in calibrated)
