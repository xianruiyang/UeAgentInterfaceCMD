from __future__ import annotations

from typing import Any, overload

from ._runtime import (
    CommandExecutor,
)

class AiCommands:

    def behavior_candidates(
        self,
        target: str,
        *,
        query: str = ...,
        parent: str = ...,
        attachment_kind: str = ...,
        graph_owner: str = ...,
        describe: dict[str, Any] = ...,
    ) -> Any: ...

    def behavior_tree_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def blackboard_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def eqs_asset_create(
        self,
        asset_name: str,
        package_path: str,
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

class AnimationCommands:

    def anim_blueprint_layer_interface_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def blend_space_asset_create(
        self,
        asset_name: str,
        *,
        axes: list[Any] = ...,
        dimension: int,
        package_path: str,
        samples: list[Any] = ...,
        skeleton_ref: str,
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

    def ik_rig_asset_create(
        self,
        asset_name: str,
        package_path: str,
        skeletal_mesh_ref: str,
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

    def sequence_pose_sample(
        self,
        target: str,
        input: dict[str, Any],
        *,
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

    def state_machine_candidates(
        self,
        target: str,
        surface: str,
        *,
        class_settings: dict[str, Any] = ...,
        query: str = ...,
        describe: dict[str, Any] = ...,
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
        describe: dict[str, Any] = ...,
    ) -> Any: ...

class AssetCommands:

    def collection(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def delete(
        self,
        targets: list[Any],
        *,
        recursive: bool = ...,
        confirm: bool = ...,
    ) -> Any: ...

    def factory_candidates(
        self,
        create_command: str,
        *,
        query: str = ...,
    ) -> Any: ...

    def fixup_redirectors(
        self,
        root_ref: str,
        *,
        confirm: bool = ...,
    ) -> Any: ...

    def folder_preview(
        self,
        folder: str,
        *,
        options: dict[str, Any] = ...,
    ) -> Any: ...

    def move(
        self,
        target_ref: str,
        destination_ref: str,
        *,
        confirm: bool = ...,
    ) -> Any: ...

    def object_clone(
        self,
        source_ref: str,
        target_ref: str,
        *,
        confirm: bool = ...,
    ) -> Any: ...

    def object_create(
        self,
        factory: Any,
        target_ref: str,
    ) -> Any: ...

    def owned_candidates(
        self,
        target: str,
        input: dict[str, Any],
        *,
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
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def sample(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def validation(
        self,
        target: str,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

class AudioCommands:

    def graph_candidates(
        self,
        target: str,
        *,
        query: str = ...,
        describe: dict[str, Any] = ...,
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
        *,
        parent: str = ...,
        query: str = ...,
    ) -> Any: ...

    def component_events_discover(
        self,
        asset_path: str,
        *,
        compile_before_query: bool = ...,
        component_name: str,
        include_hidden: bool = ...,
        only_unbound: bool = ...,
        query: str = ...,
    ) -> Any: ...

    def node_candidates(
        self,
        target: str,
        graph_name: str,
        *,
        query: str = ...,
        node_name: str = ...,
        node_occurrence: int = ...,
        pin_name: str = ...,
        pin_occurrence: int = ...,
    ) -> Any: ...

class CaptureCommands:

    @overload
    def image_execute(
        self,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ) -> Any: ...

    @overload
    def image_execute(
        self,
        subject_ref: str,
        *,
        policy_id: str = ...,
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
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def section(
        self,
        input: dict[str, Any],
        *,
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
        input: dict[str, Any],
        *,
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

    def save_resources(
        self,
        resource_refs: list[Any],
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
        target_ref: str,
    ) -> Any: ...

    def device_profile_update(
        self,
        changes: list[Any],
        target_ref: str,
    ) -> Any: ...

    def platform_config_update(
        self,
        changes: list[Any],
        target_ref: str,
    ) -> Any: ...

    def project_settings_update(
        self,
        changes: list[Any],
        target_ref: str,
    ) -> Any: ...

    def scalability_group_update(
        self,
        changes: list[Any],
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

    def fbx_static_mesh_import(
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

class FabCommands:

    def asset(
        self,
        *,
        scope: str = ...,
        name: str,
        select: dict[str, Any] = ...,
        listing_url: str = ...,
    ) -> Any: ...

    def categories(
        self,
        *,
        type: str = ...,
        parent: str = ...,
        depth: int = ...,
    ) -> Any: ...

    def download(
        self,
        *,
        scope: str = ...,
        name: str,
        select: dict[str, Any] = ...,
        format: str = ...,
        file: str = ...,
        file_select: dict[str, Any] = ...,
        save_as: str = ...,
    ) -> Any: ...

    def downloads(
        self,
        *,
        page: int = ...,
    ) -> Any: ...

    def files(
        self,
        download: str,
        *,
        query: str = ...,
        page: int = ...,
    ) -> Any: ...

    def import_asset(
        self,
        download: str,
        *,
        destination: str = ...,
        entry: str = ...,
    ) -> Any: ...

    def open(
        self,
        *,
        activate: bool = ...,
    ) -> Any: ...

    def search(
        self,
        *,
        scope: str = ...,
        query: str = ...,
        type: str = ...,
        category: str = ...,
        styles: list[Any] = ...,
        page: int = ...,
    ) -> Any: ...

    def status(
        self,
    ) -> Any: ...

class GraphCommands:

    def layout_apply(
        self,
        targets: list[Any],
        strategy: str,
        parameters: dict[str, Any],
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
        input: dict[str, Any],
        *,
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

    def expression_candidates(
        self,
        target: str,
        *,
        query: str = ...,
        graph_name: str = ...,
        pin_name: str = ...,
        describe: dict[str, Any] = ...,
    ) -> Any: ...

class MaterialInstanceCommands:

    def asset_create(
        self,
        asset_name: str,
        package_path: str,
        parent_material_ref: str,
    ) -> Any: ...

class MeshCommands:

    def attribute_normals_recompute(
        self,
        *,
        angle_degrees: float = ...,
        mode: str,
        preserve_existing_hard_edges: bool,
        target_ref: str,
    ) -> Any: ...

    def attribute_uv_auto(
        self,
        island_source: str,
        method: str,
        pack: bool,
        target_ref: str,
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
        uv_channel: int,
    ) -> Any: ...

    def collision_convex_generate(
        self,
        max_hulls: int,
        max_vertices_per_hull: int,
        mode: str,
        replace_existing: bool,
        target_ref: str,
    ) -> Any: ...

    def collision_simple_generate(
        self,
        max_shapes: int,
        method: str,
        replace_existing: bool,
        target_ref: str,
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

    def primitive_box_create(
        self,
        anchor: str,
        *,
        color: list[Any] = ...,
        material_ref: str = ...,
        placement: dict[str, Any],
        size_cm: list[Any],
        subdivisions: list[Any],
        target_ref: str,
    ) -> Any: ...

    def primitive_cylinder_create(
        self,
        anchor: str,
        cap_ends: bool,
        *,
        color: list[Any] = ...,
        height_cm: float,
        height_segments: int,
        material_ref: str = ...,
        placement: dict[str, Any],
        radial_segments: int,
        radius_cm: float,
        target_ref: str,
    ) -> Any: ...

    def primitive_plane_create(
        self,
        *,
        color: list[Any] = ...,
        double_sided: bool,
        material_ref: str = ...,
        placement: dict[str, Any],
        size_cm: list[Any],
        subdivisions: list[Any],
        target_ref: str,
    ) -> Any: ...

    def primitive_ramp_create(
        self,
        *,
        color: list[Any] = ...,
        material_ref: str = ...,
        placement: dict[str, Any],
        rise_direction: str,
        size_cm: list[Any],
        slope_axis: str,
        target_ref: str,
    ) -> Any: ...

    def primitive_ramp_corner_create(
        self,
        *,
        color: list[Any] = ...,
        high_corner: str,
        material_ref: str = ...,
        placement: dict[str, Any],
        size_cm: list[Any],
        target_ref: str,
    ) -> Any: ...

    def primitive_sphere_create(
        self,
        *,
        color: list[Any] = ...,
        latitude_segments: int,
        longitude_segments: int,
        material_ref: str = ...,
        placement: dict[str, Any],
        radius_cm: float,
        target_ref: str,
    ) -> Any: ...

    def primitive_stairs_create(
        self,
        *,
        color: list[Any] = ...,
        material_ref: str = ...,
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
        operand_to_target: dict[str, Any],
        operation: str,
        simplify_output: bool,
        space_contract: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def topology_components_remove(
        self,
        bounds_max_cm: list[Any],
        bounds_min_cm: list[Any],
        space_contract: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def topology_components_translate(
        self,
        bounds_max_cm: list[Any],
        bounds_min_cm: list[Any],
        space_contract: dict[str, Any],
        target_ref: str,
        translation_cm: list[Any],
    ) -> Any: ...

    def topology_edges_bevel(
        self,
        distance_cm: float,
        roundness: float,
        segments: int,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def topology_edges_weld(
        self,
        edge_pairs: list[Any],
        target_ref: str,
        tolerance_cm: float,
    ) -> Any: ...

    def topology_faces_duplicate(
        self,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
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
    ) -> Any: ...

    def topology_faces_inset(
        self,
        boundary_mode: str,
        distance_cm: float,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def topology_faces_offset(
        self,
        distance_cm: float,
        offset_mode: str,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
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
    ) -> Any: ...

    def topology_holes_fill(
        self,
        fill_mode: str,
        selection: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def topology_mesh_cut(
        self,
        fill_cut: bool,
        keep_sides: str,
        operand_ref: str,
        operand_to_target: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def topology_mirror(
        self,
        keep_original: bool,
        plane: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        weld_seam: bool,
    ) -> Any: ...

    def topology_plane_cut(
        self,
        fill_hole: bool,
        keep_side: str,
        plane: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def topology_remesh(
        self,
        iterations: int,
        preserve_boundaries: bool,
        preserve_sharp_edges: bool,
        space_contract: dict[str, Any],
        target_edge_length_cm: float,
        target_ref: str,
    ) -> Any: ...

    def topology_simplify(
        self,
        preserve_boundaries: bool,
        target_mode: str,
        target_ref: str,
        target_value: float,
    ) -> Any: ...

    def topology_subdivide(
        self,
        levels: int,
        scheme: str,
        target_ref: str,
    ) -> Any: ...

    def topology_trim(
        self,
        fill_hole: bool,
        keep_region: str,
        operand_ref: str,
        operand_to_target: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
    ) -> Any: ...

    def topology_voxel_boolean(
        self,
        adaptivity: float,
        operand_ref: str,
        operand_to_target: dict[str, Any],
        operation: str,
        space_contract: dict[str, Any],
        target_ref: str,
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

    def voxel_grid_begin(
        self,
        *,
        mode: str = ...,
        actor_ref: str = ...,
        label: str = ...,
        cell_size: float = ...,
        origin: dict[str, Any] = ...,
        rotation: dict[str, Any] = ...,
        anchor: dict[str, Any] = ...,
    ) -> Any: ...

class MetasoundCommands:

    def graph_compile_settle(
        self,
        registration_policy: str,
        target_ref: str,
    ) -> Any: ...

class ModelingCommands:

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
        confirm: bool = ...,
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
        emitter_name: str = ...,
        stage_name: str = ...,
        query: str = ...,
        describe: dict[str, Any] = ...,
    ) -> Any: ...

    def stack_issue_fix(
        self,
        emitter_handle_id: str,
        fix_id: str,
        issue_id: str,
        target_ref: str,
    ) -> Any: ...

    def system_asset_create(
        self,
        asset_name: str,
        package_path: str,
        source_ref: str,
    ) -> Any: ...

class OperationCommands:

    def plan_execute(
        self,
        steps: list[Any],
        on_error: str,
        atomicity: str,
    ) -> Any: ...

class PcgCommands:

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

    def graph_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def node_candidates(
        self,
        target: str,
        *,
        query: str = ...,
        describe: dict[str, Any] = ...,
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
        input: dict[str, Any],
        *,
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

    def command_search(
        self,
        intent: str,
    ) -> Any: ...

    def command_usage(
        self,
        commands: list[Any],
    ) -> Any: ...

    def content_search(
        self,
        *,
        query: str = ...,
        match_mode: str = ...,
        content_kinds: list[Any] = ...,
    ) -> Any: ...

class ReferenceCommands:

    def origin_resolve(
        self,
        input: dict[str, Any],
        *,
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

    def control_bake_context(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
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

    def retarget_assets_generate(
        self,
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

class SkeletalMeshCommands:

    def remove_morph_target(
        self,
        target_ref: str,
        name: str,
        *,
        confirm: bool = ...,
    ) -> Any: ...

    def remove_skin_weight_profile(
        self,
        target_ref: str,
        name: str,
        *,
        confirm: bool = ...,
    ) -> Any: ...

class SoundCueCommands:

    def graph_compile_settle(
        self,
        sync_policy: str,
        target_ref: str,
    ) -> Any: ...

class TextureGraphCommands:

    def artifact_bake(
        self,
        target: str,
        outputs: list[Any],
    ) -> Any: ...

    def artifact_capture(
        self,
        outputs: list[Any],
        target_ref: str,
    ) -> Any: ...

    def graph_validate_evaluate_settle(
        self,
        evaluation_policy: str,
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

    def track_candidates(
        self,
        target: str,
        *,
        animation_name: str = ...,
        binding_kind: str = ...,
        object_ref: str = ...,
        property_path: str = ...,
        query: str = ...,
    ) -> Any: ...

class UmgCommands:

    def asset_create(
        self,
        asset_name: str,
        package_path: str,
    ) -> Any: ...

    def widget_candidates(
        self,
        target: str,
        *,
        query: str = ...,
        describe: dict[str, Any] = ...,
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

    def actor_candidates(
        self,
        target: str,
        *,
        category: str = ...,
        query: str = ...,
    ) -> Any: ...

    def capsule_path(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def capsule_sweep(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def component_candidates(
        self,
        target: str,
        *,
        query: str = ...,
        describe: dict[str, Any] = ...,
    ) -> Any: ...

    def data_layers(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def geometry_overlap(
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
        confirm: bool = ...,
    ) -> Any: ...

    def mesh_closest_vertex(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def mesh_vertex_position(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def nav_connectivity(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def nav_find_path(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def nav_project_point(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def nearby_shapes(
        self,
        input: dict[str, Any],
        *,
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

    def overlap(
        self,
        input: dict[str, Any],
        *,
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
        confirm: bool = ...,
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

    def ray_trace(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def scene_context(
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

    def summary(
        self,
        *,
        input: dict[str, Any] = ...,
        context: dict[str, Any] = ...,
        projection: dict[str, Any] = ...,
    ) -> Any: ...

    def wall_create_with_opening(
        self,
        opening: dict[str, Any],
        plane: dict[str, Any],
        segment_template: dict[str, Any],
        wall: dict[str, Any],
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
    fab: FabCommands
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
    def fab(self) -> FabCommands: ...

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
