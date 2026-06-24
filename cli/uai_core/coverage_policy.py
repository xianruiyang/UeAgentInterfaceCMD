from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class SmokeCoverageClassification:
    status: str
    priority: str
    reason: str
    recommended_action: str
    actionable: bool

    def to_json(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "priority": self.priority,
            "reason": self.reason,
            "recommended_action": self.recommended_action,
            "actionable": self.actionable,
        }


DIRECT = SmokeCoverageClassification(
    status="direct",
    priority="covered",
    reason="command is directly referenced by an automation smoke test",
    recommended_action="keep existing smoke coverage",
    actionable=False,
)

NOT_IMPLEMENTED = SmokeCoverageClassification(
    status="not_implemented",
    priority="n/a",
    reason="command is documented but not detected in dispatch",
    recommended_action="implement the command or remove the documentation entry",
    actionable=True,
)

STRUCTURED_WORKFLOW_SUFFIXES = (
    "_apply_folder",
    "_export_folder",
    "_validate_folder",
    "_apply_json",
    "_export_json",
    "_validate_json",
)
VISUAL_UI_TOKENS = (
    "screenshot",
    "open_asset_editor",
    "open_editor",
    "_open_",
    "viewport_",
    "graph_get_view",
    "graph_set_view",
    "viewport_get_camera",
    "viewport_set_camera",
    "preview",
)
FIXTURE_TOKENS = (
    "asset_import_fbx",
    "asset_import_geometry_cache",
    "import_openvdb",
    "import_fbx",
    "import_ies",
)
LIFECYCLE_TOKENS = (
    "editor_prepare_exit",
    "editor_get_open_assets",
    "save_",
    "undo",
    "redo",
    "accept_tool",
    "cancel_tool",
)
READONLY_VERBS = (
    "get",
    "list",
    "query",
    "inspect",
    "info",
    "snapshot",
)
RUNTIME_TOKENS = (
    "runtime_probe",
    "training_log",
)
ATOMIC_TOKENS = (
    "_add_",
    "_remove_",
    "_set_",
    "_connect_",
    "_disconnect_",
    "_clear_",
    "_rename_",
    "_reparent",
    "_assign_",
)
AUTHORING_VERBS = (
    "add",
    "align",
    "apply",
    "attach",
    "bake",
    "build",
    "capture",
    "clear",
    "cleanup",
    "compile",
    "connect",
    "convert",
    "copy",
    "create",
    "delete",
    "detach",
    "duplicate",
    "draw",
    "generate",
    "import",
    "record",
    "refresh",
    "reimport",
    "remove",
    "rename",
    "set",
    "spawn",
    "train",
    "validate",
)


def _command_tail_verb(command: str) -> str:
    parts = command.split("_")
    if not parts:
        return ""
    if len(parts) >= 2 and parts[0] in {"ai", "ml"}:
        return parts[1]
    return parts[-1] if len(parts) == 1 else parts[1]


def _contains_any(command: str, tokens: tuple[str, ...]) -> bool:
    return any(token in command for token in tokens)


def _has_segment(command: str, segments: tuple[str, ...]) -> bool:
    parts = command.split("_")
    return any(part in segments for part in parts)


def classify_smoke_coverage(row: dict[str, Any]) -> SmokeCoverageClassification:
    command = str(row.get("command", ""))
    if bool(row.get("smoke_tested", False)):
        return DIRECT
    if not bool(row.get("implemented", False)):
        return NOT_IMPLEMENTED

    doc_status = str(row.get("doc_status", ""))
    if command.endswith(STRUCTURED_WORKFLOW_SUFFIXES) or (command.endswith("_json") and _has_segment(command, ("apply", "export", "validate"))):
        return SmokeCoverageClassification(
            status="needs_direct_smoke",
            priority="P0",
            reason="structured folder/json workflow command changes asset state and should be directly asserted",
            recommended_action="add the command to the relevant workflow smoke with create/readback/validate assertions",
            actionable=True,
        )

    if _contains_any(command, RUNTIME_TOKENS):
        return SmokeCoverageClassification(
            status="needs_runtime_smoke",
            priority="P1",
            reason="command probes runtime or generated diagnostic state and should lock response semantics",
            recommended_action="add a focused runtime smoke with cleanup and deterministic response assertions",
            actionable=True,
        )

    if _contains_any(command, FIXTURE_TOKENS):
        return SmokeCoverageClassification(
            status="needs_fixture_smoke",
            priority="P1",
            reason="command depends on external fixture assets or import formats",
            recommended_action="add a small checked-in fixture or a clean failure-path smoke when a real fixture is not distributable",
            actionable=True,
        )

    if _contains_any(command, VISUAL_UI_TOKENS):
        return SmokeCoverageClassification(
            status="needs_ui_smoke",
            priority="P1",
            reason="command exercises editor UI, viewport, preview, or screenshot behavior",
            recommended_action="cover with a minimized editor/UI smoke and visual-output validation where applicable",
            actionable=True,
        )

    if _contains_any(command, LIFECYCLE_TOKENS):
        return SmokeCoverageClassification(
            status="needs_isolated_lifecycle_smoke",
            priority="P2",
            reason="command mutates editor lifecycle, selection, transaction, or tool state",
            recommended_action="cover in an isolated shard that cleans dirty state and verifies no residual editor process",
            actionable=True,
        )

    if _has_segment(command, READONLY_VERBS) or _command_tail_verb(command) in READONLY_VERBS:
        return SmokeCoverageClassification(
            status="needs_readonly_smoke",
            priority="P2",
            reason="read-only command should have a lightweight smoke to lock response shape",
            recommended_action="add a readonly smoke assertion or document an accepted indirect workflow assertion",
            actionable=True,
        )

    if _contains_any(command, ATOMIC_TOKENS):
        return SmokeCoverageClassification(
            status="indirect_workflow_candidate",
            priority="P2",
            reason="low-level atomic authoring command may be exercised through higher-level folder/workflow smoke but lacks a direct trace",
            recommended_action="either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it",
            actionable=True,
        )

    if _has_segment(command, AUTHORING_VERBS) or _command_tail_verb(command) in AUTHORING_VERBS:
        return SmokeCoverageClassification(
            status="needs_direct_smoke",
            priority="P1",
            reason="authoring command mutates assets or level state and lacks direct smoke coverage",
            recommended_action="add focused smoke coverage with readback or validation",
            actionable=True,
        )

    if doc_status == "generated_catalog":
        return SmokeCoverageClassification(
            status="generated_catalog_triage",
            priority="P3",
            reason="command is implemented but only documented by the generated catalog",
            recommended_action="decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage",
            actionable=True,
        )

    return SmokeCoverageClassification(
        status="needs_triage",
        priority="P3",
        reason="implemented command lacks direct smoke coverage and did not match a known policy bucket",
        recommended_action="triage manually and either add smoke coverage or document why indirect coverage is accepted",
        actionable=True,
    )


def summarize_smoke_coverage(rows: list[dict[str, Any]]) -> dict[str, Any]:
    status_counts: dict[str, int] = {}
    priority_counts: dict[str, int] = {}
    actionable_missing: list[str] = []
    p0: list[str] = []
    p1: list[str] = []
    for row in rows:
        status = str(row.get("smoke_coverage_status", ""))
        priority = str(row.get("smoke_coverage_priority", ""))
        status_counts[status] = status_counts.get(status, 0) + 1
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
        if bool(row.get("smoke_coverage_actionable", False)):
            command = str(row.get("command", ""))
            actionable_missing.append(command)
            if priority == "P0":
                p0.append(command)
            elif priority == "P1":
                p1.append(command)
    return {
        "status_counts": dict(sorted(status_counts.items())),
        "priority_counts": dict(sorted(priority_counts.items())),
        "actionable_missing": actionable_missing,
        "p0_commands": p0,
        "p1_commands": p1,
        "actionable_missing_count": len(actionable_missing),
        "p0_count": len(p0),
        "p1_count": len(p1),
    }
