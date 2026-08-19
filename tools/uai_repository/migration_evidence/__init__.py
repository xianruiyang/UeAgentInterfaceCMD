from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Mapping, Sequence


class EvidenceValidationError(ValueError):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


@dataclass(frozen=True)
class HistoricalSuccessorReport:
    owner_task_id: str
    row_count: int
    obligation_fingerprint: str
    current_product_receipt_count: int
    current_command_ids: tuple[str, ...]


@dataclass(frozen=True)
class ActiveCommandSnapshot:
    command_ids: frozenset[str]
    registry_hash: str
    manifest_sha256: str
    manifest_path: str


@dataclass(frozen=True)
class LegacyReferenceSpec:
    identity: str
    surface: str
    exact_tokens: tuple[str, ...]


@dataclass(frozen=True)
class LegacyReferenceMatch:
    identity: str
    surface: str
    path: str
    token: str
    line: int


@dataclass(frozen=True)
class LegacyReferenceReport:
    active_matches: tuple[LegacyReferenceMatch, ...]
    allowed_historical_match_count: int
    scanned_file_count: int

    def require_zero_active_references(self) -> None:
        if self.active_matches:
            first = self.active_matches[0]
            raise EvidenceValidationError(
                "active_legacy_reference",
                f"{first.surface} identity {first.identity!r} remains active in {first.path}:{first.line}",
            )


_OBLIGATION_FIELDS = (
    "historical_command_id",
    "approval",
    "historical_source",
    "historical_contract",
    "resolved_from_contract_id",
)
_COVERAGE_KEYS = ("purpose", "inputs", "outputs")
_INFERENCE_KEYS = {
    "inferred_by",
    "inference",
    "matched_by",
    "namespace_match",
    "name_match",
    "prefix_match",
}
_AMBIGUOUS_TEXT = ("todo", "tbd", "placeholder", "and/or", "and-or", "待定")
_EXIT_KEYS = ("public_executable", "manifest_active", "sdk_binding_active", "compatibility_alias")


def _fail(code: str, message: str) -> None:
    raise EvidenceValidationError(code, message)


def _canonical_sha256(value: object) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def historical_obligation_fingerprint(
    obligations: Sequence[Mapping[str, object]],
) -> str:
    """Fingerprint the complete frozen inventory rows assigned to one owner."""

    rows = [
        json.loads(json.dumps(row, ensure_ascii=False))
        for row in obligations
    ]
    rows.sort(key=lambda row: str(row["historical_command_id"]))
    return _canonical_sha256(rows)


def load_historical_owner_obligations(
    inventory_path: Path,
    *,
    owner_task_id: str,
) -> tuple[Mapping[str, object], ...]:
    try:
        document = json.loads(inventory_path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        _fail("historical_inventory_unreadable", f"historical inventory is unreadable: {exc}")
    if (
        not isinstance(document, Mapping)
        or document.get("schema") != "uai.pre_refactor_command_task_inventory.v1"
    ):
        _fail(
            "historical_inventory_schema_mismatch",
            "historical inventory must use uai.pre_refactor_command_task_inventory.v1",
        )
    commands = document.get("commands")
    if not isinstance(commands, list):
        _fail("historical_inventory_invalid", "historical inventory commands must be an array")
    rows = tuple(
        _require_mapping(
            row,
            code="historical_inventory_invalid",
            context="historical inventory row",
        )
        for row in commands
        if isinstance(row, Mapping)
        and row.get("target_task_id") == owner_task_id
        and row.get("historical_lifecycle") == "active"
    )
    if not rows:
        _fail(
            "historical_inventory_owner_missing",
            f"historical inventory has no active rows for owner {owner_task_id!r}",
        )
    row_ids = tuple(
        _require_non_empty_string(
            row.get("historical_command_id"),
            code="historical_inventory_invalid",
            context="historical command ID",
        )
        for row in rows
    )
    if len(row_ids) != len(set(row_ids)):
        _fail(
            "historical_inventory_duplicate",
            f"historical inventory duplicates owner rows for {owner_task_id!r}",
        )
    return rows


def _obligation_projection(obligation: Mapping[str, object]) -> dict[str, object]:
    resolution = _require_mapping(
        obligation.get("semantic_resolution"),
        code="historical_inventory_invalid",
        context="historical semantic_resolution",
    )
    return {
        "historical_command_id": obligation.get("historical_command_id"),
        "approval": obligation.get("approval"),
        "historical_source": obligation.get("historical_source"),
        "historical_contract": obligation.get("historical_contract"),
        "resolved_from_contract_id": resolution.get("contract_id"),
    }


def _validate_obligation_authority(
    *,
    expected_row_ids: Sequence[str],
    expected_obligations: Sequence[Mapping[str, object]],
    expected_obligation_fingerprint: str,
) -> tuple[str, dict[str, dict[str, object]]]:
    expected_rows = tuple(expected_row_ids)
    obligation_ids = tuple(
        _require_non_empty_string(
            row.get("historical_command_id"),
            code="historical_inventory_invalid",
            context="historical command ID",
        )
        for row in expected_obligations
    )
    if (
        len(obligation_ids) != len(set(obligation_ids))
        or set(obligation_ids) != set(expected_rows)
    ):
        _fail(
            "row_set_mismatch",
            f"frozen owner row set differs; expected={sorted(expected_rows)}, actual={sorted(obligation_ids)}",
        )
    obligation_fingerprint = historical_obligation_fingerprint(expected_obligations)
    if obligation_fingerprint != expected_obligation_fingerprint:
        _fail(
            "obligation_fingerprint_mismatch",
            f"complete frozen owner obligation changed: {obligation_fingerprint}",
        )
    projections = {
        str(row["historical_command_id"]): _obligation_projection(row)
        for row in expected_obligations
    }
    return obligation_fingerprint, projections


def _require_mapping(value: object, *, code: str, context: str) -> Mapping[str, object]:
    if not isinstance(value, Mapping):
        _fail(code, f"{context} must be an object")
    return value


def _require_non_empty_string(value: object, *, code: str, context: str) -> str:
    if not isinstance(value, str) or not value.strip():
        _fail(code, f"{context} must be a non-empty string")
    return value


def _walk_values(value: object) -> Iterable[tuple[str | None, object]]:
    if isinstance(value, Mapping):
        for key, child in value.items():
            yield str(key), child
            yield from _walk_values(child)
    elif isinstance(value, list):
        for child in value:
            yield None, child
            yield from _walk_values(child)


def _successor_command_ids(successor: Mapping[str, object]) -> tuple[str, ...]:
    kind = successor.get("kind")
    if kind == "exact_command_set":
        command_ids = successor.get("command_ids")
    elif kind == "architecture_contract":
        command_ids = successor.get("representative_command_ids")
        _require_non_empty_string(
            successor.get("contract_id"),
            code="invalid_successor",
            context="architecture successor contract_id",
        )
    else:
        _fail("invalid_successor", f"unsupported successor kind {kind!r}")
    if not isinstance(command_ids, list) or not command_ids:
        _fail("invalid_successor", "successor command IDs must be a non-empty list")
    result = tuple(
        _require_non_empty_string(item, code="invalid_successor", context="successor command ID")
        for item in command_ids
    )
    if len(result) != len(set(result)):
        _fail("invalid_successor", "successor command IDs must be unique")
    return result


def _successor_coverage_ids(successor: Mapping[str, object]) -> tuple[str, ...]:
    if successor.get("kind") == "architecture_contract":
        return (
            _require_non_empty_string(
                successor.get("contract_id"),
                code="invalid_successor",
                context="architecture successor contract_id",
            ),
        )
    return _successor_command_ids(successor)


def _resolve_pointer(document: object, pointer: str) -> object:
    if pointer == "":
        return document
    if not pointer.startswith("/"):
        _fail("invalid_receipt_assertion", f"JSON pointer must begin with '/': {pointer!r}")
    current = document
    for encoded in pointer[1:].split("/"):
        token = encoded.replace("~1", "/").replace("~0", "~")
        if isinstance(current, Mapping) and token in current:
            current = current[token]
        elif isinstance(current, list) and token.isdecimal() and int(token) < len(current):
            current = current[int(token)]
        else:
            _fail("receipt_assertion_failed", f"receipt pointer {pointer!r} does not exist")
    return current


def _validate_receipt_bindings(
    *,
    project_root: Path,
    receipt_bindings: Sequence[Mapping[str, object]],
    expected_product_pairs: set[tuple[str, tuple[str, ...]]],
    active_commands: ActiveCommandSnapshot,
) -> None:
    bound_pairs: list[tuple[str, frozenset[str]]] = []
    for binding in receipt_bindings:
        test_id = _require_non_empty_string(
            binding.get("test_id"), code="invalid_receipt_binding", context="receipt test_id"
        )
        command_ids_value = binding.get("public_command_ids")
        if not isinstance(command_ids_value, list) or not command_ids_value:
            _fail("invalid_receipt_binding", f"receipt {test_id!r} has no exact public command IDs")
        command_ids = tuple(sorted(str(item) for item in command_ids_value))
        if not set(command_ids).issubset(active_commands.command_ids):
            _fail("unknown_current_command", f"receipt {test_id!r} names an unknown current command")
        binding_registry_hash = _require_non_empty_string(
            binding.get("active_registry_hash"),
            code="invalid_receipt_binding",
            context="receipt active_registry_hash",
        )
        if binding_registry_hash != active_commands.registry_hash:
            _fail(
                "receipt_registry_mismatch",
                f"receipt {test_id!r} was not bound against the active registry",
            )
        receipt_ref = _require_non_empty_string(
            binding.get("ref"), code="invalid_receipt_binding", context="receipt ref"
        )
        receipt_path = (project_root / receipt_ref).resolve()
        project_resolved = project_root.resolve()
        if receipt_path != project_resolved and project_resolved not in receipt_path.parents:
            _fail("invalid_receipt_binding", f"receipt path escapes the project: {receipt_ref!r}")
        if not receipt_path.is_file():
            _fail("receipt_missing", f"receipt does not exist: {receipt_ref}")
        expected_hash = _require_non_empty_string(
            binding.get("sha256"), code="invalid_receipt_binding", context="receipt sha256"
        )
        actual_hash = hashlib.sha256(receipt_path.read_bytes()).hexdigest()
        if expected_hash.removeprefix("sha256:").lower() != actual_hash:
            _fail("receipt_hash_mismatch", f"receipt changed since owner binding: {receipt_ref}")
        try:
            receipt = json.loads(receipt_path.read_text(encoding="utf-8-sig"))
        except (OSError, json.JSONDecodeError) as exc:
            _fail("receipt_unreadable", f"receipt is not readable JSON: {receipt_ref}: {exc}")
        assertions = binding.get("assertions")
        if not isinstance(assertions, list) or not assertions:
            _fail("invalid_receipt_binding", f"receipt {test_id!r} needs explicit assertions")
        for assertion_value in assertions:
            assertion = _require_mapping(
                assertion_value, code="invalid_receipt_assertion", context=f"receipt {test_id!r} assertion"
            )
            pointer = _require_non_empty_string(
                assertion.get("pointer"), code="invalid_receipt_assertion", context="assertion pointer"
            )
            if "equals" not in assertion:
                _fail("invalid_receipt_assertion", f"assertion {pointer!r} has no exact expected value")
            actual = _resolve_pointer(receipt, pointer)
            if actual != assertion["equals"]:
                _fail(
                    "receipt_assertion_failed",
                    f"receipt {receipt_ref} pointer {pointer!r} was {actual!r}, expected {assertion['equals']!r}",
                )
        bound_pairs.append((test_id, frozenset(command_ids)))
    uncovered = [
        pair
        for pair in expected_product_pairs
        if not any(
            bound_test_id == pair[0] and set(pair[1]).issubset(bound_command_ids)
            for bound_test_id, bound_command_ids in bound_pairs
        )
    ]
    unused = [
        (test_id, tuple(sorted(command_ids)))
        for test_id, command_ids in bound_pairs
        if not any(
            expected_test_id == test_id and set(expected_ids).issubset(command_ids)
            for expected_test_id, expected_ids in expected_product_pairs
        )
    ]
    if uncovered or unused:
        _fail(
            "product_receipt_binding_mismatch",
            f"receipt bindings differ; uncovered={sorted(uncovered)}, unused={sorted(unused)}",
        )


def build_historical_successor(
    *,
    owner_task_id: str,
    approval_authority: Mapping[str, object],
    expected_row_ids: Sequence[str],
    expected_obligations: Sequence[Mapping[str, object]],
    expected_obligation_fingerprint: str,
    command_decisions: Sequence[Mapping[str, object]],
) -> dict[str, object]:
    _, obligation_projections = _validate_obligation_authority(
        expected_row_ids=expected_row_ids,
        expected_obligations=expected_obligations,
        expected_obligation_fingerprint=expected_obligation_fingerprint,
    )
    expected = tuple(expected_row_ids)
    actual = tuple(str(command.get("historical_command_id", "")) for command in command_decisions)
    if len(actual) != len(set(actual)) or set(actual) != set(expected):
        _fail("row_set_mismatch", f"owner row set differs; expected={sorted(expected)}, actual={sorted(actual)}")
    for command in command_decisions:
        row_id = str(command["historical_command_id"])
        projection = {key: command.get(key) for key in _OBLIGATION_FIELDS}
        if projection != obligation_projections[row_id]:
            _fail(
                "obligation_projection_mismatch",
                f"owner decision {row_id!r} differs from its frozen inventory projection",
            )
    decisions_by_id = {str(command["historical_command_id"]): command for command in command_decisions}
    return {
        "schema": "uai.historical_successor.v2",
        "owner_task_id": owner_task_id,
        "approval_authority": json.loads(json.dumps(approval_authority, ensure_ascii=False)),
        "commands": [
            json.loads(json.dumps(decisions_by_id[row_id], ensure_ascii=False))
            for row_id in actual
        ],
    }


def validate_historical_successor(
    *,
    document: Mapping[str, object],
    expected_owner_task_id: str,
    expected_row_ids: Sequence[str],
    expected_obligations: Sequence[Mapping[str, object]],
    expected_obligation_fingerprint: str,
    active_commands: ActiveCommandSnapshot,
    project_root: Path,
    receipt_bindings: Sequence[Mapping[str, object]],
) -> HistoricalSuccessorReport:
    obligation_fingerprint, obligation_projections = _validate_obligation_authority(
        expected_row_ids=expected_row_ids,
        expected_obligations=expected_obligations,
        expected_obligation_fingerprint=expected_obligation_fingerprint,
    )
    if document.get("schema") != "uai.historical_successor.v2":
        _fail("schema_mismatch", "historical successor document must use uai.historical_successor.v2")
    if document.get("owner_task_id") != expected_owner_task_id:
        _fail("owner_mismatch", "historical successor owner does not match the consuming task")
    approval = _require_mapping(
        document.get("approval_authority"), code="invalid_approval_authority", context="approval_authority"
    )
    _require_non_empty_string(approval.get("path"), code="invalid_approval_authority", context="approval path")
    _require_non_empty_string(approval.get("sha256"), code="invalid_approval_authority", context="approval sha256")
    commands_value = document.get("commands")
    if not isinstance(commands_value, list):
        _fail("row_set_mismatch", "commands must be an array")
    commands = [
        _require_mapping(command, code="invalid_row", context="historical command row")
        for command in commands_value
    ]
    expected_rows = tuple(expected_row_ids)
    actual_rows = tuple(
        _require_non_empty_string(
            command.get("historical_command_id"), code="invalid_row", context="historical command ID"
        )
        for command in commands
    )
    if len(actual_rows) != len(set(actual_rows)) or set(actual_rows) != set(expected_rows):
        _fail(
            "row_set_mismatch",
            f"owner row set differs; expected={sorted(expected_rows)}, actual={sorted(actual_rows)}",
        )
    for command in commands:
        for field in _OBLIGATION_FIELDS:
            if field not in command:
                _fail("invalid_row", f"{command.get('historical_command_id')!r} lacks obligation field {field}")
        row_id = str(command["historical_command_id"])
        projection = {key: command[key] for key in _OBLIGATION_FIELDS}
        if projection != obligation_projections[row_id]:
            _fail(
                "obligation_projection_mismatch",
                f"owner decision {row_id!r} differs from its frozen inventory projection",
            )

    expected_product_pairs: set[tuple[str, tuple[str, ...]]] = set()
    referenced_current_ids: set[str] = set()
    for command in commands:
        row_id = str(command["historical_command_id"])
        for key, value in _walk_values(command):
            if key is not None and key.lower() in _INFERENCE_KEYS:
                _fail("successor_inference_forbidden", f"{row_id!r} contains inference metadata {key!r}")
            if isinstance(value, str) and any(token in value.lower() for token in _AMBIGUOUS_TEXT):
                _fail("placeholder_or_ambiguous_resolution", f"{row_id!r} contains ambiguous text {value!r}")

        historical_contract = _require_mapping(
            command.get("historical_contract"), code="invalid_row", context=f"{row_id} historical_contract"
        )
        for field in _COVERAGE_KEYS:
            _require_non_empty_string(
                historical_contract.get(field), code="invalid_row", context=f"{row_id} historical {field}"
            )
        successor = _require_mapping(
            command.get("successor"), code="invalid_successor", context=f"{row_id} successor"
        )
        successor_ids = _successor_command_ids(successor)
        coverage_ids = _successor_coverage_ids(successor)
        if not set(successor_ids).issubset(active_commands.command_ids):
            _fail("unknown_current_command", f"{row_id!r} names an unknown current command")
        referenced_current_ids.update(successor_ids)

        coverage = _require_mapping(
            command.get("semantic_coverage"), code="invalid_semantic_coverage", context=f"{row_id} coverage"
        )
        for field in _COVERAGE_KEYS:
            field_coverage = _require_mapping(
                coverage.get(field),
                code="invalid_semantic_coverage",
                context=f"{row_id} {field} coverage",
            )
            if field_coverage.get("status") != "covered":
                _fail("invalid_semantic_coverage", f"{row_id!r} {field} is not covered")
            by = field_coverage.get("by")
            if not isinstance(by, list) or not by or set(str(item) for item in by) != set(coverage_ids):
                _fail("semantic_successor_mismatch", f"{row_id!r} {field} coverage differs from exact successor")
            _require_non_empty_string(
                field_coverage.get("explanation"),
                code="invalid_semantic_coverage",
                context=f"{row_id} {field} explanation",
            )

        product = _require_mapping(
            command.get("product_evidence"), code="invalid_product_evidence", context=f"{row_id} product_evidence"
        )
        test_id = _require_non_empty_string(
            product.get("test_id"), code="invalid_product_evidence", context=f"{row_id} product test_id"
        )
        product_commands = product.get("public_command_ids")
        if not isinstance(product_commands, list) or not product_commands:
            _fail("invalid_product_evidence", f"{row_id!r} has no exact public command set")
        product_ids = tuple(sorted(str(item) for item in product_commands))
        if not set(product_ids).issubset(active_commands.command_ids):
            _fail("unknown_current_command", f"{row_id!r} product evidence names unknown current commands")
        required_claims = product.get("required_claims")
        if not isinstance(required_claims, list) or not required_claims:
            _fail("invalid_product_evidence", f"{row_id!r} has no required claims")
        expected_product_pairs.add((test_id, product_ids))

        old_exit = _require_mapping(
            command.get("old_id_exit"), code="invalid_legacy_exit", context=f"{row_id} old_id_exit"
        )
        if any(old_exit.get(key) is not False for key in _EXIT_KEYS):
            _fail("legacy_exit_incomplete", f"{row_id!r} remains active on an old public surface")
        _require_non_empty_string(
            command.get("final_lifecycle"), code="invalid_legacy_exit", context=f"{row_id} final_lifecycle"
        )

    _validate_receipt_bindings(
        project_root=project_root,
        receipt_bindings=receipt_bindings,
        expected_product_pairs=expected_product_pairs,
        active_commands=active_commands,
    )
    return HistoricalSuccessorReport(
        owner_task_id=expected_owner_task_id,
        row_count=len(commands),
        obligation_fingerprint=obligation_fingerprint,
        current_product_receipt_count=len(receipt_bindings),
        current_command_ids=tuple(sorted(referenced_current_ids)),
    )


def load_active_command_snapshot(manifest_path: Path) -> ActiveCommandSnapshot:
    try:
        raw = manifest_path.read_bytes()
        document = json.loads(raw.decode("utf-8-sig"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        _fail("active_manifest_unreadable", f"active command manifest is unreadable: {exc}")
    if not isinstance(document, Mapping) or document.get("schema") != "uai.command_manifest.v1":
        _fail("active_manifest_schema_mismatch", "active command manifest schema is not uai.command_manifest.v1")
    registry_hash = _require_non_empty_string(
        document.get("registry_hash"), code="active_manifest_invalid", context="registry_hash"
    )
    if not registry_hash.startswith("sha256:") or len(registry_hash) != 71:
        _fail("active_manifest_invalid", "registry_hash is not a sha256 identity")
    commands = document.get("commands")
    if not isinstance(commands, list) or not commands:
        _fail("active_manifest_invalid", "active command manifest has no commands")
    command_ids: list[str] = []
    for command_value in commands:
        command = _require_mapping(
            command_value, code="active_manifest_invalid", context="active command entry"
        )
        command_id = _require_non_empty_string(
            command.get("command_id"), code="active_manifest_invalid", context="active command ID"
        )
        if command.get("status") != "active":
            _fail("active_manifest_invalid", f"manifest command {command_id!r} is not active")
        command_ids.append(command_id)
    if len(command_ids) != len(set(command_ids)):
        _fail("active_manifest_duplicate", "active command manifest contains duplicate command IDs")
    return ActiveCommandSnapshot(
        command_ids=frozenset(command_ids),
        registry_hash=registry_hash,
        manifest_sha256="sha256:" + hashlib.sha256(raw).hexdigest(),
        manifest_path=manifest_path.as_posix(),
    )
def _is_within(path: Path, roots: tuple[Path, ...]) -> bool:
    resolved = path.resolve()
    return any(resolved == root or root in resolved.parents for root in roots)


def scan_legacy_references(
    *,
    active_roots: Sequence[Path],
    specs: Sequence[LegacyReferenceSpec],
    allowed_historical_roots: Sequence[Path] = (),
) -> LegacyReferenceReport:
    resolved_historical = tuple(path.resolve() for path in allowed_historical_roots)
    matches: list[LegacyReferenceMatch] = []
    allowed_count = 0
    scanned_count = 0
    seen_paths: set[Path] = set()
    for root in active_roots:
        if root.is_file():
            candidates = (root,)
        elif root.is_dir():
            candidates = tuple(path for path in root.rglob("*") if path.is_file())
        else:
            continue
        for path in candidates:
            resolved = path.resolve()
            if resolved in seen_paths:
                continue
            seen_paths.add(resolved)
            try:
                text = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            scanned_count += 1
            is_allowed = _is_within(path, resolved_historical)
            for spec in specs:
                for token in spec.exact_tokens:
                    pattern = re.compile(rf"(?<![A-Za-z0-9_.]){re.escape(token)}(?![A-Za-z0-9_.])")
                    for line_number, line in enumerate(text.splitlines(), start=1):
                        if pattern.search(line) is None:
                            continue
                        if is_allowed:
                            allowed_count += 1
                        else:
                            matches.append(
                                LegacyReferenceMatch(
                                    identity=spec.identity,
                                    surface=spec.surface,
                                    path=path.as_posix(),
                                    token=token,
                                    line=line_number,
                                )
                            )
    matches.sort(key=lambda item: (item.surface, item.identity, item.path, item.line, item.token))
    return LegacyReferenceReport(
        active_matches=tuple(matches),
        allowed_historical_match_count=allowed_count,
        scanned_file_count=scanned_count,
    )


__all__ = [
    "ActiveCommandSnapshot",
    "EvidenceValidationError",
    "HistoricalSuccessorReport",
    "LegacyReferenceMatch",
    "LegacyReferenceReport",
    "LegacyReferenceSpec",
    "build_historical_successor",
    "historical_obligation_fingerprint",
    "load_active_command_snapshot",
    "load_historical_owner_obligations",
    "scan_legacy_references",
    "validate_historical_successor",
]
