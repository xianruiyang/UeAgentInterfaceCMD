# UAI Smoke Coverage Debt

本文件由 `uai-cli release coverage` 生成，用于把 `missing_smoke` 拆成可执行的分类债务。

## Summary

- generated_at: `20260502_005249_706404`
- command_count: `739`
- direct_smoke_missing: `231`
- actionable_missing: `231`
- p0_count: `19`
- p1_count: `85`

## Status Counts

| Status | Count |
| --- | --- |
| `direct` | 508 |
| `generated_catalog_triage` | 12 |
| `indirect_workflow_candidate` | 66 |
| `needs_direct_smoke` | 54 |
| `needs_fixture_smoke` | 3 |
| `needs_isolated_lifecycle_smoke` | 8 |
| `needs_readonly_smoke` | 41 |
| `needs_runtime_smoke` | 3 |
| `needs_ui_smoke` | 44 |

## Priority Counts

| Priority | Count |
| --- | --- |
| `P0` | 19 |
| `P1` | 85 |
| `P2` | 115 |
| `P3` | 12 |
| `covered` | 508 |

## Debt Items

| Priority | Status | Command | Doc | Recommended Action |
| --- | --- | --- | --- | --- |
| `P0` | `needs_direct_smoke` | `asset_export_property_json` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `blendspace_apply_json` | `docs/commands/13_AnimationAssets_Skeleton.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `control_rig_apply_folder` | `docs/commands/17_ControlRig_FolderFormat.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `control_rig_export_folder` | `docs/commands/17_ControlRig_FolderFormat.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `control_rig_shape_library_apply_json` | `docs/commands/17_ControlRig_FolderFormat.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `control_rig_shape_library_export_json` | `docs/commands/17_ControlRig_FolderFormat.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `control_rig_shape_library_validate_json` | `docs/commands/17_ControlRig_FolderFormat.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `control_rig_validate_folder` | `docs/commands/17_ControlRig_FolderFormat.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `curve_apply_json` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `curve_export_json` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `deformer_graph_apply_folder` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `deformer_source_library_export_json` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `deformer_source_library_validate_json` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `mesh_deformer_collection_apply_json` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `mesh_deformer_collection_export_json` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `ml_deformer_apply_json` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `ml_deformer_export_json` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `ml_deformer_validate_json` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P0` | `needs_direct_smoke` | `static_mesh_apply_folder` | `docs/commands/04_StaticMesh_EnhancedInput.md` | add the command to the relevant workflow smoke with create/readback/validate assertions |
| `P1` | `needs_ui_smoke` | `anim_blueprint_graph_get_view` | `docs/commands/11_AnimBlueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `anim_blueprint_graph_set_view` | `docs/commands/11_AnimBlueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `anim_blueprint_open_editor` | `docs/commands/11_AnimBlueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `anim_blueprint_screenshot` | `docs/commands/11_AnimBlueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `anim_blueprint_viewport_get_camera` | `docs/commands/11_AnimBlueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `anim_blueprint_viewport_set_camera` | `docs/commands/11_AnimBlueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `anim_sequence_screenshot` | `docs/commands/13_AnimationAssets_Skeleton.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_fixture_smoke` | `asset_import_fbx_animation` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add a small checked-in fixture or a clean failure-path smoke when a real fixture is not distributable |
| `P1` | `needs_fixture_smoke` | `asset_import_fbx_skeletal_mesh` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add a small checked-in fixture or a clean failure-path smoke when a real fixture is not distributable |
| `P1` | `needs_fixture_smoke` | `asset_import_geometry_cache` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add a small checked-in fixture or a clean failure-path smoke when a real fixture is not distributable |
| `P1` | `needs_direct_smoke` | `asset_import_texture` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `behavior_tree_open_editor` | `docs/commands/19_AI_Behavior_Blackboard_StateTree_EQS_Navigation_SmartObject.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `behavior_tree_screenshot` | `docs/commands/19_AI_Behavior_Blackboard_StateTree_EQS_Navigation_SmartObject.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `blendspace_preview_sample` | `docs/commands/13_AnimationAssets_Skeleton.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `blueprint_graph_get_view` | `docs/commands/02_Blueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `blueprint_graph_set_view` | `docs/commands/02_Blueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `blueprint_screenshot` | `docs/commands/02_Blueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `blueprint_viewport_get_camera` | `docs/commands/02_Blueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `blueprint_viewport_set_camera` | `docs/commands/02_Blueprint.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `control_rig_bake_to_animation` | `docs/commands/17_ControlRig_FolderFormat.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `control_rig_bake_to_control_rig` | `docs/commands/17_ControlRig_FolderFormat.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `control_rig_compile` | `docs/commands/17_ControlRig_FolderFormat.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `control_rig_create` | `docs/commands/17_ControlRig_FolderFormat.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `control_rig_graph_get_view` | `docs/commands/17_ControlRig_FolderFormat.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `control_rig_graph_set_view` | `docs/commands/17_ControlRig_FolderFormat.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `control_rig_open_editor` | `docs/commands/17_ControlRig_FolderFormat.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_runtime_smoke` | `control_rig_runtime_probe` | `docs/commands/17_ControlRig_FolderFormat.md` | add a focused runtime smoke with cleanup and deterministic response assertions |
| `P1` | `needs_ui_smoke` | `control_rig_screenshot` | `docs/commands/17_ControlRig_FolderFormat.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `control_rig_shape_library_create` | `docs/commands/17_ControlRig_FolderFormat.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `control_rig_viewport_get_camera` | `docs/commands/17_ControlRig_FolderFormat.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `control_rig_viewport_set_camera` | `docs/commands/17_ControlRig_FolderFormat.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `deformer_graph_compile` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `deformer_source_library_create` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `editor_get_open_assets` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `geometry_cache_validate_against_skeletal_mesh` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `ik_retargeter_auto_align_pose` | `docs/commands/14_IKRig_IKRetargeter.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `ik_rig_preview_solve` | `docs/commands/14_IKRig_IKRetargeter.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `ik_rig_set_preview_mesh` | `docs/generated/implemented_command_catalog.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `level_align_actor_by_bounds` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `level_align_actor_vertex_to_vertex` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `level_align_face_to_face` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `level_attach_actor` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `level_cleanup_empty_folders` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `level_detach_actor` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `level_generate_probes` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `level_spawn_wall_with_opening` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `material_open_editor` | `docs/commands/05_Material.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `mesh_deformer_collection_create` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `ml_deformer_create` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_runtime_smoke` | `ml_deformer_get_training_log` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add a focused runtime smoke with cleanup and deterministic response assertions |
| `P1` | `needs_direct_smoke` | `modeling_duplicate_faces` | `docs/generated/implemented_command_catalog.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `montage_open_editor` | `docs/commands/12_Montage.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `navmesh_spawn_bounds_volume` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `niagara_apply_stack_issue_fix` | `docs/commands/07_Niagara_System.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `niagara_compile_system` | `docs/commands/07_Niagara_System.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `niagara_duplicate_asset` | `docs/commands/07_Niagara_System.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `niagara_emitter_parameter_add` | `docs/generated/implemented_command_catalog.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `niagara_emitter_parameter_remove` | `docs/generated/implemented_command_catalog.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `niagara_emitter_parameter_set` | `docs/generated/implemented_command_catalog.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `niagara_open_editor` | `docs/commands/07_Niagara_System.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `niagara_preview_advance` | `docs/commands/07_Niagara_System.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `niagara_refresh_system` | `docs/commands/07_Niagara_System.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `niagara_screenshot` | `docs/commands/07_Niagara_System.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_runtime_smoke` | `niagara_system_runtime_probe` | `docs/commands/07_Niagara_System.md` | add a focused runtime smoke with cleanup and deterministic response assertions |
| `P1` | `needs_direct_smoke` | `niagara_user_parameter_remove` | `docs/generated/implemented_command_catalog.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `niagara_user_parameter_set` | `docs/generated/implemented_command_catalog.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `open_asset_editor` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `screenshot_viewport` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `screenshot_viewport_buffer` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `sequence_open_level_sequence` | `docs/commands/06_Sequence.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `state_tree_open_editor` | `docs/commands/19_AI_Behavior_Blackboard_StateTree_EQS_Navigation_SmartObject.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `state_tree_screenshot` | `docs/commands/19_AI_Behavior_Blackboard_StateTree_EQS_Navigation_SmartObject.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `static_mesh_build` | `docs/commands/04_StaticMesh_EnhancedInput.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `static_mesh_open_editor` | `docs/commands/04_StaticMesh_EnhancedInput.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `static_mesh_reimport` | `docs/commands/04_StaticMesh_EnhancedInput.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `static_mesh_set_preview_view` | `docs/commands/04_StaticMesh_EnhancedInput.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_direct_smoke` | `static_mesh_validate_geometry` | `docs/commands/04_StaticMesh_EnhancedInput.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_direct_smoke` | `static_mesh_validate_uvs` | `docs/commands/04_StaticMesh_EnhancedInput.md` | add focused smoke coverage with readback or validation |
| `P1` | `needs_ui_smoke` | `viewport_focus_actor` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `viewport_focus_actor_safe` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `viewport_frame_actors` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `viewport_frame_selection` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `viewport_set_game_view` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `viewport_set_realtime` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P1` | `needs_ui_smoke` | `viewport_trace_screen_point` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover with a minimized editor/UI smoke and visual-output validation where applicable |
| `P2` | `needs_readonly_smoke` | `actor_list_components` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `indirect_workflow_candidate` | `actor_set_property` | `docs/commands/01_Core_Level_Assets_Landscape.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `anim_blueprint_add_event_dispatcher` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `anim_blueprint_add_event_node` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `anim_blueprint_add_macro_graph` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `anim_blueprint_remove_node` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `anim_blueprint_remove_variable` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `blendspace_get_info` | `docs/commands/13_AnimationAssets_Skeleton.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `indirect_workflow_candidate` | `blueprint_add_component_bound_event` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `blueprint_add_dynamic_cast_node` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `blueprint_add_enhanced_input_action_event` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `blueprint_add_enhanced_input_add_mapping_context_node` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `blueprint_add_enhanced_input_local_player_subsystem_node` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `blueprint_add_event_node` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `blueprint_add_variable_node` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `blueprint_disconnect_pins` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `blueprint_get_compile_log` | `docs/commands/02_Blueprint.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `indirect_workflow_candidate` | `blueprint_reparent` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `blueprint_set_cdo_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `component_set_property` | `docs/commands/01_Core_Level_Assets_Landscape.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `control_rig_get_compile_log` | `docs/commands/17_ControlRig_FolderFormat.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `control_rig_get_info` | `docs/commands/17_ControlRig_FolderFormat.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `control_rig_shape_library_get_info` | `docs/commands/17_ControlRig_FolderFormat.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `deformer_graph_get_compile_log` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `deformer_graph_get_info` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_isolated_lifecycle_smoke` | `editor_prepare_exit` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover in an isolated shard that cleans dirty state and verifies no residual editor process |
| `P2` | `indirect_workflow_candidate` | `enhanced_input_clear_mappings` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `enhanced_input_set_action_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `enhanced_input_set_mapping_context_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `level_add_actor_tag` | `docs/commands/01_Core_Level_Assets_Landscape.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `level_get_actor_property` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `level_get_component_property` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `level_get_selection` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `level_list_actor_components` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `indirect_workflow_candidate` | `level_set_actor_property` | `docs/commands/01_Core_Level_Assets_Landscape.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `level_set_actor_scale` | `docs/commands/01_Core_Level_Assets_Landscape.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `level_set_component_property` | `docs/commands/01_Core_Level_Assets_Landscape.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `level_set_skeletal_mesh_morph_target` | `docs/commands/01_Core_Level_Assets_Landscape.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `material_connect_expressions` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `material_get_compile_log` | `docs/commands/05_Material.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `indirect_workflow_candidate` | `material_set_instance_parent` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `material_set_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `material_set_scalar_parameter` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `material_set_texture_parameter` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `material_set_vector_parameter` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `mesh_get_closest_vertex` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `mesh_get_vertex_world_position` | `docs/commands/01_Core_Level_Assets_Landscape.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `ml_deformer_get_info` | `docs/commands/18_Deformer_MLDeformer_GeometryCache.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_isolated_lifecycle_smoke` | `modeling_accept_tool` | `docs/generated/implemented_command_catalog.md` | cover in an isolated shard that cleans dirty state and verifies no residual editor process |
| `P2` | `needs_isolated_lifecycle_smoke` | `modeling_cancel_tool` | `docs/generated/implemented_command_catalog.md` | cover in an isolated shard that cleans dirty state and verifies no residual editor process |
| `P2` | `indirect_workflow_candidate` | `modeling_clear_mesh_selection` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `modeling_get_active_tool_properties` | `docs/generated/implemented_command_catalog.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_isolated_lifecycle_smoke` | `modeling_save_mesh_asset` | `docs/generated/implemented_command_catalog.md` | cover in an isolated shard that cleans dirty state and verifies no residual editor process |
| `P2` | `indirect_workflow_candidate` | `modeling_set_active_tool_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `modeling_set_mesh_selection_mode` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `modeling_set_selection` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_add_event_handler` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_add_simulation_stage` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_add_stage_module` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_add_stage_node` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_clear_module_input` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_clear_parent` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_connect_stage_nodes` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_disconnect_stage_nodes` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_get_event_handler_property` | `docs/commands/08_Niagara_Emitter.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_get_property` | `docs/commands/08_Niagara_Emitter.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_get_renderer_property` | `docs/commands/08_Niagara_Emitter.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_get_stage_node_property` | `docs/commands/09_Niagara_StageGraph.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_list_event_handlers` | `docs/commands/08_Niagara_Emitter.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_list_module_inputs` | `docs/commands/09_Niagara_StageGraph.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_list_stage_modules` | `docs/commands/09_Niagara_StageGraph.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_list_stage_nodes` | `docs/commands/09_Niagara_StageGraph.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_list_stages` | `docs/commands/09_Niagara_StageGraph.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_parameter_get` | `docs/commands/08_Niagara_Emitter.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_emitter_parameter_list` | `docs/commands/08_Niagara_Emitter.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_remove_event_handler` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_remove_renderer` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_remove_stage` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_remove_stage_module` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_remove_stage_node` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_set_event_handler_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_set_module_input` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_set_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_set_renderer_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_set_stage_module_enabled` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_set_stage_node_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_emitter_set_stage_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `niagara_get_compile_log` | `docs/commands/07_Niagara_System.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_get_stack_issues` | `docs/commands/08_Niagara_Emitter.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_list_assets` | `docs/commands/07_Niagara_System.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_list_module_library` | `docs/generated/implemented_command_catalog.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `indirect_workflow_candidate` | `niagara_set_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `niagara_system_get_property` | `docs/commands/07_Niagara_System.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_system_list_emitters` | `docs/commands/07_Niagara_System.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_system_list_module_inputs` | `docs/generated/implemented_command_catalog.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_system_list_stage_modules` | `docs/generated/implemented_command_catalog.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `indirect_workflow_candidate` | `niagara_system_remove_emitter` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_system_set_emitter_enabled` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_system_set_emitter_version` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `niagara_system_set_module_input` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `niagara_user_parameter_get` | `docs/commands/07_Niagara_System.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `niagara_user_parameter_list` | `docs/commands/07_Niagara_System.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_isolated_lifecycle_smoke` | `redo` | `docs/generated/implemented_command_catalog.md` | cover in an isolated shard that cleans dirty state and verifies no residual editor process |
| `P2` | `needs_isolated_lifecycle_smoke` | `save_asset` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover in an isolated shard that cleans dirty state and verifies no residual editor process |
| `P2` | `needs_isolated_lifecycle_smoke` | `save_current_level` | `docs/commands/01_Core_Level_Assets_Landscape.md` | cover in an isolated shard that cleans dirty state and verifies no residual editor process |
| `P2` | `indirect_workflow_candidate` | `sequence_add_umg_widget_float_key` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `sequence_add_umg_widget_translation_key` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `skeletal_mesh_get_morph_targets` | `docs/commands/16_SkeletalMesh_FolderFormat.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `indirect_workflow_candidate` | `skeletal_mesh_remove_morph_target` | `docs/commands/16_SkeletalMesh_FolderFormat.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `skeletal_mesh_remove_skin_weight_profile` | `docs/commands/16_SkeletalMesh_FolderFormat.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_readonly_smoke` | `static_mesh_get_bounds` | `docs/commands/04_StaticMesh_EnhancedInput.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `needs_readonly_smoke` | `static_mesh_get_local_corners` | `docs/commands/04_StaticMesh_EnhancedInput.md` | add a readonly smoke assertion or document an accepted indirect workflow assertion |
| `P2` | `indirect_workflow_candidate` | `static_mesh_set_collision_boxes` | `docs/commands/04_StaticMesh_EnhancedInput.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `indirect_workflow_candidate` | `static_mesh_set_property` | `docs/generated/implemented_command_catalog.md` | either add a direct atomic smoke or annotate the workflow smoke that intentionally covers it |
| `P2` | `needs_isolated_lifecycle_smoke` | `undo` | `docs/generated/implemented_command_catalog.md` | cover in an isolated shard that cleans dirty state and verifies no residual editor process |
| `P3` | `generated_catalog_triage` | `modeling_bevel_edges` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `modeling_inset_faces` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `modeling_invoke_active_tool_action` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `modeling_push_pull` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `modeling_replace_actor_mesh` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `modeling_select_mesh_elements_via_screen` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `modeling_select_mesh_elements_via_world_ray` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `modeling_snap_to_ground` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `modeling_start_tool` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `niagara_emitter_move_renderer` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `niagara_emitter_move_stage_module` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
| `P3` | `generated_catalog_triage` | `niagara_system_move_emitter` | `docs/generated/implemented_command_catalog.md` | decide whether to promote it to formal docs, mark it internal/deprecated, or add focused smoke coverage |
