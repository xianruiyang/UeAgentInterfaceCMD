from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RepresentativeCalibration:
    owner_task_id: str
    successor_ref: str
    expected_row_ids: tuple[str, ...]
    expected_obligation_fingerprint: str
    active_command_ids: frozenset[str]
    receipt_bindings: tuple[dict[str, object], ...]


REPRESENTATIVE_CALIBRATIONS = (
    RepresentativeCalibration(
        owner_task_id="T27-DATATABLE-CURVETABLE-DOMAIN",
        successor_ref="Plugins/UeAgentInterface/docs/active/successors/t27_datatable_curvetable_domain.json",
        expected_row_ids=(
            "curve_apply_json",
            "curve_export_json",
            "data_asset_apply_json",
            "data_asset_create",
            "data_asset_diff_json",
            "data_asset_export_json",
            "data_asset_validate_json",
            "data_table_apply_json",
            "data_table_diff_json",
            "data_table_export_json",
            "data_table_validate_json",
        ),
        expected_obligation_fingerprint="sha256:d1a5f4230b986ea5630efa31272e4344c7c8268c54c6decb3955f17a4be0c05e",
        active_command_ids=frozenset(
            {
                "content_graph.export_workspace",
                "content_graph.import_workspace",
                "content_graph.structure",
            }
        ),
        receipt_bindings=(
            {
                "test_id": "UAI.DeliveryWorkflow.T27.DATATABLE.CURVETABLE.DOMAIN",
                "ref": "runtimeLogs/delivery_workflow/T27/public_verification/public_vertical_receipt.json",
                "sha256": "e90e9261ff247e5d8c06649af2f504515aac1eabfee76b7d04363d29c0596ca5",
                "active_registry_hash": "sha256:25ac62facdce964fcc84d0780e812790fa514a4603d4625f69b696df9969cef0",
                "public_command_ids": [
                    "content_graph.export_workspace",
                    "content_graph.import_workspace",
                    "content_graph.structure",
                ],
                "assertions": [
                    {"pointer": "/status", "equals": "passed"},
                    {"pointer": "/cleanup_status", "equals": "passed"},
                    {"pointer": "/historical_obligation_count", "equals": 11},
                    {"pointer": "/legacy_exit_four_surfaces", "equals": True},
                ],
            },
            {
                "test_id": "UAI.StrictV2.T13.UOBJECT.RECURSIVE.INIT",
                "ref": "runtimeLogs/strict_v2_r26/T13/verification/public_vertical_receipt.json",
                "sha256": "fa375f07988c393aacb73e139d6b060c83f0174d40a9a7356dfe4378d3ea4ed4",
                "active_registry_hash": "sha256:25ac62facdce964fcc84d0780e812790fa514a4603d4625f69b696df9969cef0",
                "public_command_ids": [
                    "content_graph.export_workspace",
                    "content_graph.import_workspace",
                    "content_graph.structure",
                ],
                "assertions": [
                    {"pointer": "/status", "equals": "passed"},
                    {"pointer": "/cleanup_status", "equals": "passed"},
                    {"pointer": "/cases/1/test_id", "equals": "UAI.StrictV2.T13.UOBJECT.RECURSIVE.INIT"},
                    {"pointer": "/cases/1/public_entry/command_id", "equals": "content_graph.import_workspace"},
                    {"pointer": "/cases/1/readback/independent", "equals": True},
                ],
            },
        ),
    ),
    RepresentativeCalibration(
        owner_task_id="T30-EXTERNAL-LOCALIZATION-IMPORT",
        successor_ref="Plugins/UeAgentInterface/docs/active/successors/t30_external_localization_import.json",
        expected_row_ids=(
            "localization_apply_json",
            "localization_compile_text",
            "localization_diff_json",
            "localization_export_json",
            "localization_export_po",
            "localization_gather_text",
            "localization_import_po",
            "localization_preview_culture",
            "localization_query_targets",
            "localization_report",
            "localization_validate_json",
            "string_table_apply_json",
            "string_table_diff_json",
            "string_table_export_json",
            "string_table_validate_json",
        ),
        expected_obligation_fingerprint="sha256:2f484f43963c1070e130ffb286c4eed56bf94edef53223d1e668c4824bef2daf",
        active_command_ids=frozenset(
            {
                "content_graph.compound",
                "content_graph.export_workspace",
                "content_graph.import_workspace",
                "editor.session",
                "external.localization.po.import",
                "job.compile_build",
                "operation.receipt",
                "operation.release",
                "operation.status",
            }
        ),
        receipt_bindings=(
            {
                "test_id": "UAI.StrictV2.T30.EXTERNAL.LOCALIZATION.IMPORT",
                "ref": "docs/plan/20260806_UAI_REQUIREMENT_DESIGN_REALIGNMENT/evidence/T30-EXTERNAL-LOCALIZATION-IMPORT-current-verification.json",
                "sha256": "291dc50920a8a6d07166eeb5468273c4cc94bd6dbddbb7f3ffbc3368c72f8345",
                "active_registry_hash": "sha256:25ac62facdce964fcc84d0780e812790fa514a4603d4625f69b696df9969cef0",
                "public_command_ids": [
                    "content_graph.compound",
                    "content_graph.export_workspace",
                    "content_graph.import_workspace",
                    "editor.session",
                    "external.localization.po.import",
                    "job.compile_build",
                    "operation.receipt",
                    "operation.release",
                    "operation.status",
                ],
                "assertions": [
                    {"pointer": "/task_id", "equals": "T30-EXTERNAL-LOCALIZATION-IMPORT"},
                    {"pointer": "/build/result", "equals": "succeeded"},
                    {"pointer": "/python/result", "equals": "7 passed"},
                    {"pointer": "/historical_contract/frozen_row_count", "equals": 15},
                    {"pointer": "/cleanup/temporary_test_asset_active", "equals": False},
                ],
            },
        ),
    ),
    RepresentativeCalibration(
        owner_task_id="T39-EDITOR-PROJECT-OPERATION",
        successor_ref="Plugins/UeAgentInterface/docs/active/successors/t39_editor_project_operation.json",
        expected_row_ids=(
            "config_apply_section",
            "device_profile_apply_json",
            "device_profile_diff_json",
            "device_profile_export_json",
            "device_profile_query",
            "device_profile_resolve_cvars",
            "device_profile_validate_json",
            "platform_config_apply_json",
            "platform_config_export_json",
            "platform_config_validate_json",
            "platform_profile_validate_packaging",
            "project_settings_apply_page",
            "project_settings_diff_page",
            "project_settings_export_index",
            "project_settings_export_page",
            "project_settings_validate_page",
            "scalability_apply_json",
            "scalability_export_json",
            "scalability_validate_json",
            "target_platform_query",
        ),
        expected_obligation_fingerprint="sha256:2492a65213a4de38e7157bbffe35419e3587029ca15278bfa06596d34ebd7071",
        active_command_ids=frozenset(
            {
                "config.resolved_value",
                "config.section",
                "editor_project.config_section.update",
                "editor_project.device_profile.update",
                "editor_project.platform_config.update",
                "editor_project.project_settings.update",
                "editor_project.scalability_group.update",
                "project.platform",
                "project.settings",
                "project.validation",
            }
        ),
        receipt_bindings=(
            {
                "test_id": "UAI.DeliveryWorkflow.T39.EDITOR.PROJECT.OPERATION",
                "ref": "runtimeLogs/delivery_workflow/T39/t39_product_evidence.json",
                "sha256": "98d46cfc3ba7d71cfc8dbfc15a4df43c74a63514f252b4a1e7f8b0989b913911",
                "active_registry_hash": "sha256:25ac62facdce964fcc84d0780e812790fa514a4603d4625f69b696df9969cef0",
                "public_command_ids": [
                    "config.resolved_value",
                    "config.section",
                    "editor_project.config_section.update",
                    "editor_project.device_profile.update",
                    "editor_project.platform_config.update",
                    "editor_project.project_settings.update",
                    "editor_project.scalability_group.update",
                    "project.platform",
                    "project.settings",
                    "project.validation",
                ],
                "assertions": [
                    {"pointer": "/status", "equals": "passed"},
                    {"pointer": "/historical_disposition_count", "equals": 20},
                    {"pointer": "/claims/public_to_real_ue", "equals": True},
                    {"pointer": "/claims/persistence_and_restart_readback", "equals": True},
                    {"pointer": "/claims/old_public_ids_absent", "equals": True},
                    {"pointer": "/claims/cleanup_confirmed_after_restart", "equals": True},
                ],
            },
        ),
    ),
)


__all__ = ["REPRESENTATIVE_CALIBRATIONS", "RepresentativeCalibration"]
