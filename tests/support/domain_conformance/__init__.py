from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable


class ConformanceError(ValueError):
    pass


@dataclass(frozen=True)
class DomainFixture:
    fixture_id: str
    domain_id: str
    target_identity: str
    base_revision: str
    entry_file: str
    document: str
    workspace_root: Path
    mechanics_family: str
    public_route_id: str
    public_test_ids: tuple[str, ...]

    def validate(self) -> None:
        identities = (
            self.fixture_id,
            self.domain_id,
            self.target_identity,
            self.base_revision,
            self.entry_file,
            self.mechanics_family,
            self.public_route_id,
        )
        if any(not item or item != item.strip() for item in identities):
            raise ConformanceError(f"domain_conformance_fixture_invalid:{self.fixture_id}")
        if not self.document or not self.workspace_root.is_absolute():
            raise ConformanceError(f"domain_conformance_fixture_invalid:{self.fixture_id}")
        if not self.public_test_ids or any(
            not item or item != item.strip() for item in self.public_test_ids
        ):
            raise ConformanceError(
                f"domain_conformance_public_test_id_missing:{self.fixture_id}"
            )
        entry = Path(self.entry_file)
        if entry.is_absolute() or ".." in entry.parts or entry.suffix.lower() != ".hjson":
            raise ConformanceError(
                f"domain_conformance_entry_file_invalid:{self.entry_file}"
            )


@dataclass(frozen=True)
class LayerEvidence:
    static_contract: str | None
    domain_adapter: str | None


@dataclass(frozen=True)
class ProductEvidence:
    route_id: str
    receipt_ref: str
    receipt_exists: bool
    synthetic: bool
    public_route_observed: bool
    independent_readback_observed: bool
    cleanup_observed: bool


def _sha256_text(value: str) -> str:
    return "sha256:" + hashlib.sha256(value.encode("utf-8")).hexdigest()


def build_equivalent_sources(fixture: DomainFixture) -> list[dict[str, str]]:
    fixture.validate()
    single_file = fixture.workspace_root / "single_file" / fixture.entry_file
    directory_root = fixture.workspace_root / "directory"
    directory_entry = directory_root / fixture.entry_file
    manifest_path = directory_root / ".uai" / "workspace.hjson"
    single_file.parent.mkdir(parents=True, exist_ok=True)
    directory_entry.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    single_file.write_text(fixture.document, encoding="utf-8", newline="")
    directory_entry.write_text(fixture.document, encoding="utf-8", newline="")
    manifest = {
        "workspace_schema": "uai.content_graph.workspace/1",
        "format_version": 1,
        "target_identity": fixture.target_identity,
        "base_revision": fixture.base_revision,
        "entry_file": fixture.entry_file.replace("\\", "/"),
        "files": [
            {
                "path": fixture.entry_file.replace("\\", "/"),
                "content_hash": _sha256_text(fixture.document),
            }
        ],
        "references": [],
    }
    manifest_path.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
        newline="",
    )
    return [
        {"kind": "inline", "document": fixture.document},
        {"kind": "single_file", "path": str(single_file.resolve())},
        {"kind": "directory", "path": str(directory_root.resolve())},
    ]


def build_owned_worker_plan(
    fixtures: Iterable[DomainFixture],
    evidence: LayerEvidence,
    runtime_root: Path,
) -> dict[str, Any]:
    fixtures = list(fixtures)
    if not evidence.static_contract:
        raise ConformanceError(
            "domain_conformance_low_cost_layer_incomplete:static_contract"
        )
    if not evidence.domain_adapter:
        raise ConformanceError(
            "domain_conformance_low_cost_layer_incomplete:domain_adapter"
        )
    if not fixtures:
        raise ConformanceError("domain_conformance_fixture_set_empty")
    grouped: dict[str, list[DomainFixture]] = {}
    for fixture in fixtures:
        fixture.validate()
        grouped.setdefault(fixture.mechanics_family, []).append(fixture)
    batches: list[dict[str, Any]] = []
    for index, mechanics_family in enumerate(sorted(grouped), start=1):
        group = sorted(grouped[mechanics_family], key=lambda item: item.fixture_id)
        test_ids = sorted(
            {
                test_id
                for item in group
                for test_id in item.public_test_ids
            }
        )
        batches.append(
            {
                "batch_id": f"domain-conformance-{index:03d}-{mechanics_family}",
                "tier": "public_product",
                "domain": ",".join(item.domain_id for item in group),
                "expected_wall_budget": 600,
                "max_silence_budget": 120,
                "requires_headless": True,
                "requires_rhi": False,
                "automation_filter": "Engine",
                "test_modules": ["UeAgentInterfaceTests"],
                "map": "",
                "cleanup_policy": "owned_processes_and_temp_artifacts",
                "output_receipt_path": (
                    f"receipts/domain-conformance-{index:03d}.json"
                ),
                "cases": [
                    {"test_id": test_id, "filter": test_id}
                    for test_id in test_ids
                ],
                "fixture_ids": [item.fixture_id for item in group],
                "mechanics_family": mechanics_family,
                "low_cost_evidence": {
                    "static_contract": evidence.static_contract,
                    "domain_adapter": evidence.domain_adapter,
                },
            }
        )
    return {
        "schema": "uai.ue_test_plan.v1",
        "plan_id": "domain-conformance-owned-worker",
        "runtime_root": str(runtime_root.resolve()),
        "preserve_main_editor": True,
        "batches": batches,
    }


def validate_product_evidence(
    fixture: DomainFixture,
    evidence: ProductEvidence,
) -> None:
    fixture.validate()
    if evidence.route_id != fixture.public_route_id or not evidence.receipt_ref:
        raise ConformanceError(
            f"domain_conformance_product_evidence_identity_invalid:{evidence.receipt_ref}"
        )
    if evidence.synthetic:
        raise ConformanceError(
            f"domain_conformance_synthetic_product_evidence:{evidence.receipt_ref}"
        )
    if not all(
        (
            evidence.receipt_exists,
            evidence.public_route_observed,
            evidence.independent_readback_observed,
            evidence.cleanup_observed,
        )
    ):
        raise ConformanceError(
            f"domain_conformance_public_product_evidence_incomplete:{evidence.receipt_ref}"
        )


def _resolve_path(value: Any, dotted_path: str) -> Any:
    current = value
    for part in dotted_path.split("."):
        if isinstance(current, list):
            current = current[int(part)]
        elif isinstance(current, dict) and part in current:
            current = current[part]
        else:
            raise ConformanceError(
                f"domain_conformance_calibration_path_missing:{dotted_path}"
            )
    return current


def validate_representative_calibrations(
    project_root: Path,
    calibration_path: Path,
) -> list[dict[str, Any]]:
    payload = json.loads(calibration_path.read_text(encoding="utf-8"))
    if payload.get("schema") != "uai.domain_conformance.calibration.v1":
        raise ConformanceError("domain_conformance_calibration_schema_invalid")
    calibrations = payload.get("calibrations")
    if not isinstance(calibrations, list) or not calibrations:
        raise ConformanceError("domain_conformance_calibration_empty")
    domain_ids: set[str] = set()
    for item in calibrations:
        domain_id = item.get("domain_id")
        if not isinstance(domain_id, str) or not domain_id or domain_id in domain_ids:
            raise ConformanceError(
                f"domain_conformance_calibration_domain_invalid:{domain_id}"
            )
        domain_ids.add(domain_id)
        if item.get("public_route_id") != "content_graph.import_workspace":
            raise ConformanceError(
                f"domain_conformance_calibration_route_invalid:{domain_id}"
            )
        if not item.get("bounded_claim"):
            raise ConformanceError(
                f"domain_conformance_calibration_unbounded:{domain_id}"
            )
        evidence_ref = item.get("evidence_ref")
        evidence_path = project_root / evidence_ref
        if not isinstance(evidence_ref, str) or not evidence_path.is_file():
            raise ConformanceError(
                f"domain_conformance_calibration_evidence_missing:{domain_id}"
            )
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        for assertion in item.get("required_equals", []):
            observed = _resolve_path(evidence, assertion["path"])
            if observed != assertion["value"]:
                raise ConformanceError(
                    "domain_conformance_calibration_assertion_failed:"
                    f"{domain_id}:{assertion['path']}"
                )
        for assertion in item.get("required_contains", []):
            observed = _resolve_path(evidence, assertion["path"])
            if not isinstance(observed, list) or not any(
                assertion["value"] in str(value) for value in observed
            ):
                raise ConformanceError(
                    "domain_conformance_calibration_assertion_failed:"
                    f"{domain_id}:{assertion['path']}"
                )
    return calibrations


__all__ = [
    "ConformanceError",
    "DomainFixture",
    "LayerEvidence",
    "ProductEvidence",
    "build_equivalent_sources",
    "build_owned_worker_plan",
    "validate_product_evidence",
    "validate_representative_calibrations",
]
