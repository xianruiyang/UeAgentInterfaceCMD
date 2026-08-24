from __future__ import annotations

from typing import Any

from ._runtime import (
    CommandBindingCatalog,
    CommandExecutor,
)

GENERATED_MANIFEST_HASH: str
GENERATED_REGISTRY_HASH: str
BINDING_CATALOG: CommandBindingCatalog

class AiCommands:

    def behavior_candidates(
        self,
        target: str,
        *,
        query: str = ...,
        limit: int = ...,
        cursor: int = ...,
    ) -> Any: ...

    def behavior_tree_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def behavior_tree_graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ) -> Any: ...

    def blackboard_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def blackboard_schema_apply(
        self,
        entries: list[Any],
        target_ref: str,
    ) -> Any: ...

    def eqs_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def eqs_graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ) -> Any: ...

    def smart_object_definition_apply(
        self,
        slots: list[Any],
        target_ref: str,
    ) -> Any: ...

    def smart_object_definition_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def state_tree_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def state_tree_hierarchy_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ) -> Any: ...

class AnimationCommands:

    def anim_blueprint_asset_create(
        self,
        asset_name: str,
        package_path: str,
        parent_class_ref: str,
        skeleton_ref: str,
    ) -> Any: ...

    def anim_blueprint_graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ) -> Any: ...

    def anim_blueprint_layer_interface_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def blend_space_asset_create(
        self,
        asset_name: str,
        dimension: int,
        package_path: str,
        skeleton_ref: str,
    ) -> Any: ...

    def blend_space_definition_apply(
        self,
        axes: list[Any],
        samples: list[Any],
        target_ref: str,
    ) -> Any: ...

    def blend_space_sample(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def control_rig_asset_create(
        self,
        asset_name: str,
        package_path: str,
        skeleton_ref: str,
    ) -> Any: ...

    def control_rig_hierarchy_graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ) -> Any: ...

    def control_rig_shape_library_apply(
        self,
        shapes: list[Any],
        target_ref: str,
    ) -> Any: ...

    def control_rig_shape_library_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def deformer_graph_asset_create(
        self,
        asset_name: str,
        package_path: str,
        skeletal_mesh_ref: str,
    ) -> Any: ...

    def deformer_graph_topology_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ) -> Any: ...

    def deformer_source_library_asset_create(
        self,
        asset_name: str,
        concrete_class_ref: str,
        package_path: str,
    ) -> Any: ...

    def deformer_source_library_bindings_apply(
        self,
        bindings: list[Any],
        concrete_class_ref: str,
        target_ref: str,
    ) -> Any: ...

    def ik_probe_candidate_apply(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def ik_retargeter_asset_create(
        self,
        asset_name: str,
        package_path: str,
        source_ik_rig_ref: str,
        target_ik_rig_ref: str,
    ) -> Any: ...

    def ik_retargeter_definition_apply(
        self,
        chain_mappings: list[Any],
        source_ik_rig_ref: str,
        target_ik_rig_ref: str,
        target_ref: str,
    ) -> Any: ...

    def ik_retargeter_settings_apply(
        self,
        settings: list[Any],
        target_ref: str,
    ) -> Any: ...

    def ik_rig_asset_create(
        self,
        asset_name: str,
        package_path: str,
        skeletal_mesh_ref: str,
    ) -> Any: ...

    def ik_rig_definition_apply(
        self,
        chains: list[Any],
        goals: list[Any],
        retarget_root: str,
        solvers: list[Any],
        target_ref: str,
    ) -> Any: ...

    def ik_rig_definition_auto_generate(
        self,
        preset: str,
        skeletal_mesh_ref: str,
        target_ref: str,
    ) -> Any: ...

    def mesh_deformer_collection_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def mesh_deformer_collection_entries_apply(
        self,
        entries: list[Any],
        target_ref: str,
    ) -> Any: ...

    def ml_deformer_asset_create(
        self,
        asset_name: str,
        model_class_ref: str,
        package_path: str,
    ) -> Any: ...

    def ml_deformer_configuration_apply(
        self,
        animation_ref: str,
        concrete_model_class_ref: str,
        deformer_graph_ref: str,
        skeletal_mesh_ref: str,
        target_geometry_cache_ref: str,
        target_ref: str,
    ) -> Any: ...

    def montage_create(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def montage_read(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def montage_structure_replace(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def sequence_bone_tracks_replace(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def sequence_curves_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def sequence_events_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def sequence_metadata_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def sequence_pose_sample(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def sequence_read(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def sequence_root_motion_analyze(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def skeleton_compatibility_apply(
        self,
        changes: list[Any],
        target_ref: str,
    ) -> Any: ...

    def skeleton_definition_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ) -> Any: ...

    def skeleton_slots_read(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def skeleton_virtual_bone_apply(
        self,
        intent: str,
        name: str,
        source_bone: str,
        target_bone: str,
        target_ref: str,
    ) -> Any: ...

    def subject_morph_weights_update(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def subject_pose_update(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class AnimationRigGraphCommands:

    def candidates(
        self,
        target: str,
        *,
        query: str = ...,
        space_ref: str = ...,
        limit: int = ...,
        cursor: int = ...,
    ) -> Any: ...

class AssetCommands:

    def audio_effect_preset_create(
        self,
        factory_ref: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def audio_effect_preset_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def collection(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def curve_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def data_layer_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def data_object_create(
        self,
        factory_ref: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def data_object_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def data_table_replace(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def delete(
        self,
        target_ref: str,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def factory_candidates(
        self,
        create_command: str,
        *,
        query: str = ...,
        limit: int = ...,
        cursor: int = ...,
    ) -> Any: ...

    def fixup_redirectors(
        self,
        root_ref: str,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def input_action_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def input_action_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def input_mapping_context_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def input_mapping_context_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def media_player_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def media_player_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def media_source_create(
        self,
        factory_ref: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def media_source_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def media_texture_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def media_texture_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def move(
        self,
        target_ref: str,
        destination_ref: str,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def object_clone(
        self,
        *,
        destructive_authorization_id: str = ...,
        expected_source_revision: str,
        source_ref: str,
        target_ref: str,
    ) -> Any: ...

    def paper_flipbook_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def paper_flipbook_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def paper_sprite_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def paper_sprite_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def paper_tilemap_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def paper_tileset_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def properties(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def registry_record(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def registry_relations(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def reimport_sound_wave(
        self,
        source_ref: str,
        target_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def reimport_sparse_volume_texture(
        self,
        source_ref: str,
        target_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def reimport_static_mesh(
        self,
        source_ref: str,
        target_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def reimport_texture(
        self,
        source_ref: str,
        target_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def relations(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def render_target_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def render_target_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def runtime_virtual_texture_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def runtime_virtual_texture_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def sample(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def skeletal_mesh_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def sound_attenuation_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def sound_attenuation_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def sound_class_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def sound_class_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def sound_concurrency_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def sound_concurrency_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def sound_mix_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def sound_mix_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def sound_submix_create(
        self,
        factory_ref: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def sound_submix_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def sparse_volume_texture_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def static_mesh_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def subuv_animation_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def subuv_animation_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def summary(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def texture_array_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def texture_array_replace(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def texture_collection_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def texture_collection_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def texture_cube_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def texture_cube_replace(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def texture_cube_array_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def texture_cube_array_replace(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def validation(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def volume_texture_create(
        self,
        target_ref: str,
    ) -> Any: ...

    def volume_texture_replace(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

class AudioCommands:

    def graph_candidates(
        self,
        target: str,
        *,
        query: str = ...,
        limit: int = ...,
        cursor: int = ...,
    ) -> Any: ...

class AudioMediaCommands:

    def asset_create(
        self,
        asset_kind: str,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

class BlueprintCommands:

    def asset_create(
        self,
        asset_name: str,
        package_path: str,
        parent_class_ref: str,
    ) -> Any: ...

    def component_candidates(
        self,
        target: str,
        component_class: str,
        requested_name: str,
    ) -> Any: ...

    def component_events_discover(
        self,
        asset_path: str,
        *,
        compile_before_query: bool = ...,
        component_name: str,
        include_hidden: bool = ...,
        limit: int = ...,
        only_unbound: bool = ...,
        query: str = ...,
    ) -> Any: ...

    def node_candidates(
        self,
        target: str,
        graph_id: str,
        *,
        query: str = ...,
    ) -> Any: ...

class CaptureCommands:

    def image_execute(
        self,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ) -> Any: ...

    def media_execute(
        self,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ) -> Any: ...

    def render_execute(
        self,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ) -> Any: ...

class ConfigCommands:

    def resolved_value(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def section(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class ContentGraphCommands:

    def compound(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def diagnostics(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def export_workspace(
        self,
        target: str,
        workspace_path: str,
        *,
        profile_id: str = ...,
    ) -> Any: ...

    def import_workspace(
        self,
        target: str,
        source: dict[str, Any],
        expected_revision: str,
        authorization_id: str,
        *,
        limits: dict[str, Any] = ...,
    ) -> Any: ...

    def items(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def properties(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def relations(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def structure(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def summary(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class DeformerCommands:

    def evaluation_sample(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def geometry_sample(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def training_inputs_validate(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class EditorCommands:

    def dirty_resources(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def open_assets(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def safe_exit(
        self,
        dirty_resolution: dict[str, Any],
        external_witness: dict[str, Any],
    ) -> Any: ...

    def session(
        self,
        family_id: str,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ) -> Any: ...

class EditorProjectCommands:

    def config_section_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def device_profile_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def localization_target_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def platform_config_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def project_settings_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def scalability_group_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

    def string_table_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ) -> Any: ...

class ExternalCommands:

    def fbx_animation_import(
        self,
        source_ref: str,
        destination_ref: str,
        skeleton_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def fbx_skeletal_mesh_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def geometry_cache_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def light_profile_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def localization_po_import(
        self,
        source_ref: str,
        target_ref: str,
    ) -> Any: ...

    def skin_weight_profile_import(
        self,
        source_ref: str,
        target_ref: str,
        profile_name: str,
        lod_index: int,
    ) -> Any: ...

    def sound_wave_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def sparse_volume_texture_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def texture_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

class GraphCommands:

    def layout_apply(
        self,
        targets: list[Any],
        strategy: str,
        parameters: dict[str, Any],
        authorization_id: str,
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def view_read(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any],
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def view_update(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class JobCommands:

    def compile_build(
        self,
        family_id: str,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ) -> Any: ...

class LandscapeCommands:

    def create(
        self,
        initial_height: dict[str, Any],
        placement: dict[str, Any],
        sample_region: dict[str, Any],
        target_ref: str,
        topology: dict[str, Any],
    ) -> Any: ...

    def height_read(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def height_delta(
        self,
        delta: dict[str, Any],
        region: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

class MaterialCommands:

    def asset_create(
        self,
        asset_name: str,
        *,
        material_kind: str = ...,
        package_path: str,
    ) -> Any: ...

    def expression_candidates(
        self,
        target: str,
        *,
        query: str = ...,
        limit: int = ...,
        cursor: int = ...,
    ) -> Any: ...

    def function_graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ) -> Any: ...

class MaterialInstanceCommands:

    def asset_create(
        self,
        asset_name: str,
        package_path: str,
        parent_material_ref: str,
    ) -> Any: ...

    def parameters_apply(
        self,
        parameters: list[Any],
        target_ref: str,
    ) -> Any: ...

class MeshCommands:

    def attribute_material_slot_add(
        self,
        material_ref: str,
        slot_name: str,
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def attribute_material_slot_assign(
        self,
        selection: dict[str, Any],
        slot_index: int,
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def attribute_normals_recompute(
        self,
        *,
        angle_degrees: float = ...,
        mode: str,
        preserve_existing_hard_edges: bool,
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def attribute_uv_auto(
        self,
        island_source: str,
        method: str,
        pack: bool,
        target_ref: str,
        target_revision: dict[str, Any],
        texture_resolution: int,
        uv_channel: int,
    ) -> Any: ...

    def attribute_uv_project(
        self,
        dimensions_cm: list[Any],
        projection_frame: dict[str, Any],
        projection_type: str,
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
        uv_channel: int,
    ) -> Any: ...

    def collision_convex_generate(
        self,
        max_hulls: int,
        max_vertices_per_hull: int,
        mode: str,
        replace_existing: bool,
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def collision_simple_generate(
        self,
        max_shapes: int,
        method: str,
        replace_existing: bool,
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def element_select_by_ray(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def modeling_session(
        self,
        action: str,
        *,
        target: str = ...,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def pivot_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def primitive_box_create(
        self,
        anchor: str,
        placement: dict[str, Any],
        size_cm: list[Any],
        subdivisions: list[Any],
        target_ref: str,
    ) -> Any: ...

    def primitive_cylinder_create(
        self,
        anchor: str,
        cap_ends: bool,
        height_cm: float,
        height_segments: int,
        placement: dict[str, Any],
        radial_segments: int,
        radius_cm: float,
        target_ref: str,
    ) -> Any: ...

    def primitive_plane_create(
        self,
        double_sided: bool,
        placement: dict[str, Any],
        size_cm: list[Any],
        subdivisions: list[Any],
        target_ref: str,
    ) -> Any: ...

    def primitive_ramp_create(
        self,
        placement: dict[str, Any],
        rise_direction: str,
        size_cm: list[Any],
        slope_axis: str,
        target_ref: str,
    ) -> Any: ...

    def primitive_ramp_corner_create(
        self,
        high_corner: str,
        placement: dict[str, Any],
        size_cm: list[Any],
        target_ref: str,
    ) -> Any: ...

    def primitive_sphere_create(
        self,
        latitude_segments: int,
        longitude_segments: int,
        placement: dict[str, Any],
        radius_cm: float,
        target_ref: str,
    ) -> Any: ...

    def primitive_stairs_create(
        self,
        placement: dict[str, Any],
        rise_axis: str,
        rise_direction: str,
        step_count: int,
        step_depth_cm: float,
        step_height_cm: float,
        step_width_cm: float,
        target_ref: str,
    ) -> Any: ...

    def topology_boolean(
        self,
        operand_ref: str,
        operand_revision: dict[str, Any],
        operand_to_target: dict[str, Any],
        operation: str,
        simplify_output: bool,
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_edges_bevel(
        self,
        distance_cm: float,
        roundness: float,
        segments: int,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_edges_weld(
        self,
        edge_pairs: list[Any],
        target_ref: str,
        target_revision: dict[str, Any],
        tolerance_cm: float,
    ) -> Any: ...

    def topology_faces_duplicate(
        self,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
        translation_cm: list[Any],
    ) -> Any: ...

    def topology_faces_extrude(
        self,
        *,
        direction: dict[str, Any] = ...,
        direction_mode: str,
        distance_cm: float,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_faces_inset(
        self,
        boundary_mode: str,
        distance_cm: float,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_faces_offset(
        self,
        distance_cm: float,
        offset_mode: str,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_faces_push_pull(
        self,
        *,
        direction: dict[str, Any] = ...,
        direction_mode: str,
        distance_cm: float,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_holes_fill(
        self,
        fill_mode: str,
        selection: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_mesh_cut(
        self,
        fill_cut: bool,
        keep_sides: str,
        operand_ref: str,
        operand_revision: dict[str, Any],
        operand_to_target: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_mirror(
        self,
        keep_original: bool,
        plane: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
        weld_seam: bool,
    ) -> Any: ...

    def topology_plane_cut(
        self,
        fill_hole: bool,
        keep_side: str,
        plane: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_remesh(
        self,
        iterations: int,
        preserve_boundaries: bool,
        preserve_sharp_edges: bool,
        space_contract: dict[str, Any],
        target_edge_length_cm: float,
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_simplify(
        self,
        preserve_boundaries: bool,
        target_mode: str,
        target_ref: str,
        target_revision: dict[str, Any],
        target_value: float,
    ) -> Any: ...

    def topology_subdivide(
        self,
        levels: int,
        scheme: str,
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_trim(
        self,
        fill_hole: bool,
        keep_region: str,
        operand_ref: str,
        operand_revision: dict[str, Any],
        operand_to_target: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ) -> Any: ...

    def topology_voxel_boolean(
        self,
        adaptivity: float,
        operand_ref: str,
        operand_revision: dict[str, Any],
        operand_to_target: dict[str, Any],
        operation: str,
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
        voxel_size_cm: float,
    ) -> Any: ...

    def transform_bake(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def voxel_grid_apply(
        self,
        session_id: str,
        expected_revision: int,
        *,
        mesh_build: str = ...,
        collision: dict[str, Any] = ...,
        material_ref: str = ...,
        keep_session: bool = ...,
    ) -> Any: ...

    def voxel_grid_session(
        self,
        action: str,
        *,
        session_id: str = ...,
        expected_revision: int = ...,
        mode: str = ...,
        grid_id: str = ...,
        actor_ref: str = ...,
        label: str = ...,
        cell_size: float = ...,
        origin: dict[str, Any] = ...,
        rotation: dict[str, Any] = ...,
        anchor: dict[str, Any] = ...,
        bounds: dict[str, Any] = ...,
        max_operation_cells: int = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class MetasoundCommands:

    def graph_compile_settle(
        self,
        expected_document_revision: str,
        registration_policy: str,
        target_ref: str,
    ) -> Any: ...

    def graph_default_mutate(
        self,
        data_type_ref: str,
        intent: str,
        node_guid: str,
        target_ref: str,
        value: Any,
        vertex_guid: str,
    ) -> Any: ...

    def graph_interface_mutate(
        self,
        changes: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_link_mutate(
        self,
        links: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_node_mutate(
        self,
        nodes: list[Any],
        target_ref: str,
    ) -> Any: ...

class ModelingCommands:

    def actor_mesh_replace(
        self,
        actor_ref: str,
        mesh_ref: str,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def asset_material_slot_remove(
        self,
        target_ref: str,
        index: int,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def voxel_bounds_remove(
        self,
        actor_ref: str,
        component_name: str,
        space: str,
        min_x: int,
        min_y: int,
        min_z: int,
        max_x: int,
        max_y: int,
        max_z: int,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

class NiagaraCommands:

    def asset_duplicate(
        self,
        source_ref: str,
        target_ref: str,
    ) -> Any: ...

    def compile_refresh_settle(
        self,
        target_ref: str,
    ) -> Any: ...

    def compound_apply(
        self,
        emitter_handle_id: str,
        input_name: str,
        module_ref: str,
        stage_ref: str,
        target_ref: str,
        value: Any,
    ) -> Any: ...

    def emitter_asset_create(
        self,
        asset_name: str,
        package_path: str,
        source_ref: str,
    ) -> Any: ...

    def module_candidates(
        self,
        target: str,
        target_usage: str,
        *,
        query: str = ...,
        limit: int = ...,
        cursor: int = ...,
    ) -> Any: ...

    def renderer_event_parameter_apply(
        self,
        emitter_handle_id: str,
        parameter_name: str,
        renderer_ref: str,
        target_ref: str,
        type_ref: str,
        value: Any,
    ) -> Any: ...

    def stack_issue_fix(
        self,
        emitter_handle_id: str,
        fix_id: str,
        issue_id: str,
        target_ref: str,
    ) -> Any: ...

    def stack_reorder(
        self,
        emitter_handle_id: str,
        item_ref: str,
        predecessor_ref: str,
        stage_ref: str,
        target_ref: str,
    ) -> Any: ...

    def system_asset_create(
        self,
        asset_name: str,
        package_path: str,
        source_ref: str,
    ) -> Any: ...

class OperationCommands:

    def cancel(
        self,
        operation_ref: dict[str, Any],
        reason: str,
    ) -> Any: ...

    def plan_execute(
        self,
        steps: list[Any],
        on_error: str,
        atomicity: str,
    ) -> Any: ...

    def receipt(
        self,
        operation_ref: dict[str, Any],
    ) -> Any: ...

    def reconcile(
        self,
        operation_ref: dict[str, Any],
        expected_generation: int,
    ) -> Any: ...

    def release(
        self,
        operation_ref: dict[str, Any],
    ) -> Any: ...

    def resume(
        self,
        operation_ref: dict[str, Any],
        expected_generation: int,
    ) -> Any: ...

    def status(
        self,
        operation_ref: dict[str, Any],
    ) -> Any: ...

class PcgCommands:

    def component_apply(
        self,
        generation_policy: str,
        graph_ref: str,
        target_ref: str,
    ) -> Any: ...

    def component_world_binding_apply(
        self,
        actor_ref: str,
        component_ref: str,
        generation_policy: str,
        graph_ref: str,
    ) -> Any: ...

    def data_asset_apply(
        self,
        content_revision: str,
        data_type_ref: str,
        source_ref: str,
        target_ref: str,
        value: Any,
    ) -> Any: ...

    def data_asset_create_from_level(
        self,
        data_type_ref: str,
        source_level_ref: str,
        target_ref: str,
    ) -> Any: ...

    def generated_spatial_data_read(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def graph_instance_apply(
        self,
        graph_ref: str,
        overrides: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_parameters_apply(
        self,
        parameters: list[Any],
        target_ref: str,
    ) -> Any: ...

    def node_candidates(
        self,
        target: str,
        *,
        query: str = ...,
        limit: int = ...,
        cursor: int = ...,
    ) -> Any: ...

    def partition_spatial_state_read(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class PhysicsCommands:

    def asset_structure_replace(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def constraint_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def material_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def simulation_probe(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class ProjectCommands:

    def platform(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def settings(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def summary(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def validation(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class QueryCommands:

    def calibration_read(
        self,
        category: str,
        *,
        search_text: str = ...,
        limit: int = ...,
        cursor: int = ...,
    ) -> Any: ...

    def command_detail(
        self,
        command_id: str,
        contract_hash: str,
    ) -> Any: ...

    def command_search(
        self,
        intent: str,
        *,
        limit: int = ...,
        cursor: int = ...,
    ) -> Any: ...

    def content_search(
        self,
        *,
        query: str = ...,
        match_mode: str = ...,
        content_kinds: list[Any] = ...,
        class_path: str = ...,
        path_prefix: str = ...,
        owner_identity: str = ...,
        required_operations: list[Any] = ...,
        limit_per_provider: int = ...,
        cursor: dict[str, Any] = ...,
    ) -> Any: ...

class ReferenceCommands:

    def asset_apply(
        self,
        object_path: str,
        intent: str,
        *,
        proposed_text: str | None = ...,
    ) -> Any: ...

    def asset_read(
        self,
        object_path: str,
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def origin_resolve(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class RigCommands:

    def control_bake_animation(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def control_bake_controls(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def ik_definition_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def retarget_assets_generate(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def retarget_definition_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def retarget_pose_auto_align(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def retarget_pose_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def skeleton_preview_mesh_bind(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def skeleton_socket_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class SkeletalMeshCommands:

    def remove_morph_target(
        self,
        target_ref: str,
        name: str,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def remove_skin_weight_profile(
        self,
        target_ref: str,
        name: str,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

class SoundCueCommands:

    def graph_compile_settle(
        self,
        expected_graph_revision: str,
        sync_policy: str,
        target_ref: str,
    ) -> Any: ...

    def graph_node_mutate(
        self,
        nodes: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_relation_mutate(
        self,
        relations: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_root_mutate(
        self,
        intent: str,
        root_node_object_path: str,
        target_ref: str,
    ) -> Any: ...

class TextureGraphCommands:

    def artifact_bake(
        self,
        target: str,
        expected_revision: str,
        outputs: list[Any],
    ) -> Any: ...

    def artifact_capture(
        self,
        expected_settled_revision: str,
        outputs: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_link_mutate(
        self,
        links: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_node_mutate(
        self,
        nodes: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_parameter_mutate(
        self,
        parameters: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_validate_evaluate_settle(
        self,
        evaluation_policy: str,
        expected_graph_revision: str,
        target_ref: str,
    ) -> Any: ...

    def runtime_probe(
        self,
        target: str,
        *,
        render_output_index: int = ...,
        expected_stats: dict[str, Any] = ...,
    ) -> Any: ...

class TimelineCommands:

    def sequence_create(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def sequence_read(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def sequence_structure_replace(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def widget_animation_read(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class UmgCommands:

    def asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def widget_events_discover(
        self,
        owner_item_ref: str,
        target_ref: str,
    ) -> Any: ...

class ViewportCommands:

    def actor_pick(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def actor_select(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def camera_frame(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def instance_list(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def pixel_scale_read(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def ray_deproject(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def ray_trace(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def state_read(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any],
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def state_restore(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def state_update(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def view_mode_list(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any],
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def warning_list(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any],
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class WorldCommands:

    def actor_create(
        self,
        actor_class_ref: str,
        *,
        folder_path: str = ...,
        label: str,
        placement: dict[str, Any],
        tags: list[Any] = ...,
    ) -> Any: ...

    def actor_components(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def actor_hlod_layer_update(
        self,
        *,
        collection_ref: str = ...,
        mode: str,
        subject_refs: list[Any],
    ) -> Any: ...

    def actor_streaming_policy_update(
        self,
        changes: dict[str, Any],
        target_refs: list[Any],
    ) -> Any: ...

    def actors(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def capsule_path(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def capsule_sweep(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def content(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def data_layer_delete(
        self,
        layer: str,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def data_layer_instance_create(
        self,
        *,
        asset_ref: str = ...,
        initial_state: dict[str, Any] = ...,
        parent_ref: str = ...,
        private: bool = ...,
        short_name: str = ...,
    ) -> Any: ...

    def data_layer_relation_update(
        self,
        collection_refs: list[Any],
        mode: str,
        relation_kind: str,
        subject_refs: list[Any],
    ) -> Any: ...

    def data_layer_state_update(
        self,
        changes: dict[str, Any],
        target_refs: list[Any],
    ) -> Any: ...

    def data_layers(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def hlod_assignments(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def level_content_delete_scope(
        self,
        folder_path: str,
        *,
        managed_id: str = ...,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def level_game_mode_update(
        self,
        game_mode_class_ref: str,
    ) -> Any: ...

    def level_streaming_move_actors(
        self,
        actor_ref: str,
        level_package: str,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def level_streaming_remove(
        self,
        level_package: str,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def mesh_closest_vertex(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def mesh_vertex_position(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def nav_connectivity(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def nav_find_path(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def nav_project_point(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def nearby_shapes(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def object_align(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def object_snap_to_surface(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def object_transform_read(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def overlap(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def partition(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def partition_health(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def pcg_cleanup(
        self,
        actor_ref: str,
        component_name: str,
        *,
        destructive_authorization_id: str = ...,
    ) -> Any: ...

    def physics_component(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def physics_constraint(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def property(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def ray_trace(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def selection(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def streaming_levels(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def streaming_relation_create(
        self,
        level_asset_ref: str,
        *,
        placement: dict[str, Any] = ...,
        streaming_class_ref: str,
    ) -> Any: ...

    def streaming_relation_state_update(
        self,
        changes: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def summary(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def transform_candidates_evaluate(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def wall_create_with_opening(
        self,
        opening: dict[str, Any],
        plane: dict[str, Any],
        segment_template: dict[str, Any],
        wall: dict[str, Any],
    ) -> Any: ...

    def world_partition_streaming_update(
        self,
        enabled: bool,
    ) -> Any: ...

class GeneratedCommandNamespaces:

    ai: AiCommands
    animation: AnimationCommands
    animation_rig_graph: AnimationRigGraphCommands
    asset: AssetCommands
    audio: AudioCommands
    audio_media: AudioMediaCommands
    blueprint: BlueprintCommands
    capture: CaptureCommands
    config: ConfigCommands
    content_graph: ContentGraphCommands
    deformer: DeformerCommands
    editor: EditorCommands
    editor_project: EditorProjectCommands
    external: ExternalCommands
    graph: GraphCommands
    job: JobCommands
    landscape: LandscapeCommands
    material: MaterialCommands
    material_instance: MaterialInstanceCommands
    mesh: MeshCommands
    metasound: MetasoundCommands
    modeling: ModelingCommands
    niagara: NiagaraCommands
    operation: OperationCommands
    pcg: PcgCommands
    physics: PhysicsCommands
    project: ProjectCommands
    query: QueryCommands
    reference: ReferenceCommands
    rig: RigCommands
    skeletal_mesh: SkeletalMeshCommands
    sound_cue: SoundCueCommands
    texture_graph: TextureGraphCommands
    timeline: TimelineCommands
    umg: UmgCommands
    viewport: ViewportCommands
    world: WorldCommands
    def __init__(
        self,
        client: CommandExecutor,
    ) -> None: ...

class GeneratedClientBindingsMixin:

    @property
    def ai(self) -> AiCommands: ...

    @property
    def animation(self) -> AnimationCommands: ...

    @property
    def animation_rig_graph(self) -> AnimationRigGraphCommands: ...

    @property
    def asset(self) -> AssetCommands: ...

    @property
    def audio(self) -> AudioCommands: ...

    @property
    def audio_media(self) -> AudioMediaCommands: ...

    @property
    def blueprint(self) -> BlueprintCommands: ...

    @property
    def capture(self) -> CaptureCommands: ...

    @property
    def config(self) -> ConfigCommands: ...

    @property
    def content_graph(self) -> ContentGraphCommands: ...

    @property
    def deformer(self) -> DeformerCommands: ...

    @property
    def editor(self) -> EditorCommands: ...

    @property
    def editor_project(self) -> EditorProjectCommands: ...

    @property
    def external(self) -> ExternalCommands: ...

    @property
    def graph(self) -> GraphCommands: ...

    @property
    def job(self) -> JobCommands: ...

    @property
    def landscape(self) -> LandscapeCommands: ...

    @property
    def material(self) -> MaterialCommands: ...

    @property
    def material_instance(self) -> MaterialInstanceCommands: ...

    @property
    def mesh(self) -> MeshCommands: ...

    @property
    def metasound(self) -> MetasoundCommands: ...

    @property
    def modeling(self) -> ModelingCommands: ...

    @property
    def niagara(self) -> NiagaraCommands: ...

    @property
    def operation(self) -> OperationCommands: ...

    @property
    def pcg(self) -> PcgCommands: ...

    @property
    def physics(self) -> PhysicsCommands: ...

    @property
    def project(self) -> ProjectCommands: ...

    @property
    def query(self) -> QueryCommands: ...

    @property
    def reference(self) -> ReferenceCommands: ...

    @property
    def rig(self) -> RigCommands: ...

    @property
    def skeletal_mesh(self) -> SkeletalMeshCommands: ...

    @property
    def sound_cue(self) -> SoundCueCommands: ...

    @property
    def texture_graph(self) -> TextureGraphCommands: ...

    @property
    def timeline(self) -> TimelineCommands: ...

    @property
    def umg(self) -> UmgCommands: ...

    @property
    def viewport(self) -> ViewportCommands: ...

    @property
    def world(self) -> WorldCommands: ...

def bind_generated_commands(
    client: CommandExecutor,
) -> GeneratedCommandNamespaces: ...
