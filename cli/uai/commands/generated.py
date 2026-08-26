"""Generated from the C++ command registry manifest. Do not edit."""

from __future__ import annotations

from typing import Any

from ._runtime import (
    CommandBinding,
    CommandBindingCatalog,
    CommandExecutor,
    CommandParameterBinding,
    OMITTED,
)

GENERATED_MANIFEST_HASH = "sha256:1504a65d392c6c97f8d8e9d50f8f1fe24917afffdf1e1e0bc31a6d8a05428621"
GENERATED_REGISTRY_HASH = "sha256:fc8bb2f208d74d8e4368c867e9ba9c062cdc1fc4c95099f3c8d3fb83fab39c6f"

class AiCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def behavior_candidates(
        self,
        target: str,
        *,
        query: str | object = OMITTED,
        id: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if id is not OMITTED:
            params["id"] = id
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "ai.behavior.candidates",
            params,
        )

    def behavior_tree_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "ai.behavior_tree.asset.create",
            params,
        )

    def behavior_tree_graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["edits"] = edits
        params["target_ref"] = target_ref
        return self._client.execute(
            "ai.behavior_tree.graph.apply",
            params,
        )

    def blackboard_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "ai.blackboard.asset.create",
            params,
        )

    def blackboard_schema_apply(
        self,
        entries: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["entries"] = entries
        params["target_ref"] = target_ref
        return self._client.execute(
            "ai.blackboard.schema.apply",
            params,
        )

    def eqs_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "ai.eqs.asset.create",
            params,
        )

    def eqs_graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["edits"] = edits
        params["target_ref"] = target_ref
        return self._client.execute(
            "ai.eqs.graph.apply",
            params,
        )

    def smart_object_definition_apply(
        self,
        slots: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["slots"] = slots
        params["target_ref"] = target_ref
        return self._client.execute(
            "ai.smart_object_definition.apply",
            params,
        )

    def smart_object_definition_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "ai.smart_object_definition.asset.create",
            params,
        )

    def state_tree_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "ai.state_tree.asset.create",
            params,
        )

    def state_tree_hierarchy_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["edits"] = edits
        params["target_ref"] = target_ref
        return self._client.execute(
            "ai.state_tree.hierarchy.apply",
            params,
        )

class AnimationCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def anim_blueprint_asset_create(
        self,
        asset_name: str,
        package_path: str,
        parent_class_ref: str,
        skeleton_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        params["parent_class_ref"] = parent_class_ref
        params["skeleton_ref"] = skeleton_ref
        return self._client.execute(
            "animation.anim_blueprint.asset.create",
            params,
        )

    def anim_blueprint_graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["edits"] = edits
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.anim_blueprint.graph.apply",
            params,
        )

    def anim_blueprint_layer_interface_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "animation.anim_blueprint.layer_interface.asset.create",
            params,
        )

    def blend_space_asset_create(
        self,
        asset_name: str,
        dimension: int,
        package_path: str,
        skeleton_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["dimension"] = dimension
        params["package_path"] = package_path
        params["skeleton_ref"] = skeleton_ref
        return self._client.execute(
            "animation.blend_space.asset.create",
            params,
        )

    def blend_space_definition_apply(
        self,
        axes: list[Any],
        samples: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["axes"] = axes
        params["samples"] = samples
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.blend_space.definition.apply",
            params,
        )

    def blend_space_sample(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.blend_space.sample",
            params,
        )

    def control_rig_asset_create(
        self,
        asset_name: str,
        package_path: str,
        skeleton_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        params["skeleton_ref"] = skeleton_ref
        return self._client.execute(
            "animation.control_rig.asset.create",
            params,
        )

    def control_rig_hierarchy_graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["edits"] = edits
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.control_rig.hierarchy_graph.apply",
            params,
        )

    def control_rig_shape_library_apply(
        self,
        shapes: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["shapes"] = shapes
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.control_rig.shape_library.apply",
            params,
        )

    def control_rig_shape_library_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "animation.control_rig.shape_library.asset.create",
            params,
        )

    def deformer_graph_asset_create(
        self,
        asset_name: str,
        package_path: str,
        skeletal_mesh_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        params["skeletal_mesh_ref"] = skeletal_mesh_ref
        return self._client.execute(
            "animation.deformer_graph.asset.create",
            params,
        )

    def deformer_graph_topology_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["edits"] = edits
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.deformer_graph.topology.apply",
            params,
        )

    def deformer_source_library_asset_create(
        self,
        asset_name: str,
        concrete_class_ref: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["concrete_class_ref"] = concrete_class_ref
        params["package_path"] = package_path
        return self._client.execute(
            "animation.deformer_source_library.asset.create",
            params,
        )

    def deformer_source_library_bindings_apply(
        self,
        bindings: list[Any],
        concrete_class_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["bindings"] = bindings
        params["concrete_class_ref"] = concrete_class_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.deformer_source_library.bindings.apply",
            params,
        )

    def ik_probe_candidate_apply(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.ik_probe_candidate.apply",
            params,
        )

    def ik_retargeter_asset_create(
        self,
        asset_name: str,
        package_path: str,
        source_ik_rig_ref: str,
        target_ik_rig_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        params["source_ik_rig_ref"] = source_ik_rig_ref
        params["target_ik_rig_ref"] = target_ik_rig_ref
        return self._client.execute(
            "animation.ik_retargeter.asset.create",
            params,
        )

    def ik_retargeter_definition_apply(
        self,
        chain_mappings: list[Any],
        source_ik_rig_ref: str,
        target_ik_rig_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["chain_mappings"] = chain_mappings
        params["source_ik_rig_ref"] = source_ik_rig_ref
        params["target_ik_rig_ref"] = target_ik_rig_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.ik_retargeter.definition.apply",
            params,
        )

    def ik_retargeter_settings_apply(
        self,
        settings: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["settings"] = settings
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.ik_retargeter.settings.apply",
            params,
        )

    def ik_rig_asset_create(
        self,
        asset_name: str,
        package_path: str,
        skeletal_mesh_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        params["skeletal_mesh_ref"] = skeletal_mesh_ref
        return self._client.execute(
            "animation.ik_rig.asset.create",
            params,
        )

    def ik_rig_definition_apply(
        self,
        chains: list[Any],
        goals: list[Any],
        retarget_root: str,
        solvers: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["chains"] = chains
        params["goals"] = goals
        params["retarget_root"] = retarget_root
        params["solvers"] = solvers
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.ik_rig.definition.apply",
            params,
        )

    def ik_rig_definition_auto_generate(
        self,
        preset: str,
        skeletal_mesh_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["preset"] = preset
        params["skeletal_mesh_ref"] = skeletal_mesh_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.ik_rig.definition.auto_generate",
            params,
        )

    def mesh_deformer_collection_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "animation.mesh_deformer_collection.asset.create",
            params,
        )

    def mesh_deformer_collection_entries_apply(
        self,
        entries: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["entries"] = entries
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.mesh_deformer_collection.entries.apply",
            params,
        )

    def ml_deformer_asset_create(
        self,
        asset_name: str,
        model_class_ref: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["model_class_ref"] = model_class_ref
        params["package_path"] = package_path
        return self._client.execute(
            "animation.ml_deformer.asset.create",
            params,
        )

    def ml_deformer_configuration_apply(
        self,
        animation_ref: str,
        concrete_model_class_ref: str,
        deformer_graph_ref: str,
        skeletal_mesh_ref: str,
        target_geometry_cache_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["animation_ref"] = animation_ref
        params["concrete_model_class_ref"] = concrete_model_class_ref
        params["deformer_graph_ref"] = deformer_graph_ref
        params["skeletal_mesh_ref"] = skeletal_mesh_ref
        params["target_geometry_cache_ref"] = target_geometry_cache_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.ml_deformer.configuration.apply",
            params,
        )

    def montage_create(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.montage.create",
            params,
        )

    def montage_read(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.montage.read",
            params,
        )

    def montage_structure_replace(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.montage.structure.replace",
            params,
        )

    def sequence_bone_tracks_replace(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.sequence.bone_tracks.replace",
            params,
        )

    def sequence_curves_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.sequence.curves.update",
            params,
        )

    def sequence_events_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.sequence.events.update",
            params,
        )

    def sequence_metadata_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.sequence.metadata.update",
            params,
        )

    def sequence_pose_sample(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.sequence.pose.sample",
            params,
        )

    def sequence_read(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.sequence.read",
            params,
        )

    def sequence_root_motion_analyze(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.sequence.root_motion.analyze",
            params,
        )

    def skeleton_compatibility_apply(
        self,
        changes: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.skeleton.compatibility.apply",
            params,
        )

    def skeleton_definition_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["edits"] = edits
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.skeleton.definition.apply",
            params,
        )

    def skeleton_slots_read(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.skeleton.slots.read",
            params,
        )

    def skeleton_virtual_bone_apply(
        self,
        intent: str,
        name: str,
        source_bone: str,
        target_bone: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["intent"] = intent
        params["name"] = name
        params["source_bone"] = source_bone
        params["target_bone"] = target_bone
        params["target_ref"] = target_ref
        return self._client.execute(
            "animation.skeleton.virtual_bone.apply",
            params,
        )

    def state_machine_candidates(
        self,
        target: str,
        surface: str,
        *,
        class_settings: dict[str, Any] | object = OMITTED,
        query: str | object = OMITTED,
        id: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["surface"] = surface
        if class_settings is not OMITTED:
            params["class_settings"] = class_settings
        if query is not OMITTED:
            params["query"] = query
        if id is not OMITTED:
            params["id"] = id
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "animation.state_machine.candidates",
            params,
        )

    def subject_morph_weights_update(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.subject.morph_weights.update",
            params,
        )

    def subject_pose_update(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "animation.subject.pose.update",
            params,
        )

class AnimationRigGraphCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def candidates(
        self,
        target: str,
        *,
        query: str | object = OMITTED,
        id: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if id is not OMITTED:
            params["id"] = id
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "animation_rig_graph.candidates",
            params,
        )

class AssetCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def audio_effect_preset_create(
        self,
        factory_ref: dict[str, Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["factory_ref"] = factory_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.audio_effect_preset.create",
            params,
        )

    def audio_effect_preset_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.audio_effect_preset.update",
            params,
        )

    def collection(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "asset.collection",
            params,
        )

    def curve_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.curve.update",
            params,
        )

    def data_layer_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.data_layer.create",
            params,
        )

    def data_object_create(
        self,
        factory_ref: dict[str, Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["factory_ref"] = factory_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.data_object.create",
            params,
        )

    def data_object_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.data_object.update",
            params,
        )

    def data_table_replace(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.data_table.replace",
            params,
        )

    def delete(
        self,
        target_ref: str,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "asset.delete",
            params,
        )

    def factory_candidates(
        self,
        create_command: str,
        *,
        query: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["create_command"] = create_command
        if query is not OMITTED:
            params["query"] = query
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "asset.factory.candidates",
            params,
        )

    def fixup_redirectors(
        self,
        root_ref: str,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["root_ref"] = root_ref
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "asset.fixup_redirectors",
            params,
        )

    def input_action_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.input_action.create",
            params,
        )

    def input_action_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.input_action.update",
            params,
        )

    def input_mapping_context_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.input_mapping_context.create",
            params,
        )

    def input_mapping_context_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.input_mapping_context.update",
            params,
        )

    def media_player_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.media_player.create",
            params,
        )

    def media_player_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.media_player.update",
            params,
        )

    def media_source_create(
        self,
        factory_ref: dict[str, Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["factory_ref"] = factory_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.media_source.create",
            params,
        )

    def media_source_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.media_source.update",
            params,
        )

    def media_texture_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.media_texture.create",
            params,
        )

    def media_texture_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.media_texture.update",
            params,
        )

    def move(
        self,
        target_ref: str,
        destination_ref: str,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        params["destination_ref"] = destination_ref
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "asset.move",
            params,
        )

    def object_clone(
        self,
        *,
        destructive_authorization_id: str | object = OMITTED,
        expected_source_revision: str,
        source_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        params["expected_source_revision"] = expected_source_revision
        params["source_ref"] = source_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.object.clone",
            params,
        )

    def paper_flipbook_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.paper_flipbook.create",
            params,
        )

    def paper_flipbook_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.paper_flipbook.update",
            params,
        )

    def paper_sprite_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.paper_sprite.create",
            params,
        )

    def paper_sprite_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.paper_sprite.update",
            params,
        )

    def paper_tilemap_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.paper_tilemap.update",
            params,
        )

    def paper_tileset_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.paper_tileset.update",
            params,
        )

    def properties(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "asset.properties",
            params,
        )

    def registry_record(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "asset.registry_record",
            params,
        )

    def registry_relations(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "asset.registry_relations",
            params,
        )

    def reimport_sound_wave(
        self,
        source_ref: str,
        target_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["target_ref"] = target_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "asset.reimport_sound_wave",
            params,
        )

    def reimport_sparse_volume_texture(
        self,
        source_ref: str,
        target_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["target_ref"] = target_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "asset.reimport_sparse_volume_texture",
            params,
        )

    def reimport_static_mesh(
        self,
        source_ref: str,
        target_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["target_ref"] = target_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "asset.reimport_static_mesh",
            params,
        )

    def reimport_texture(
        self,
        source_ref: str,
        target_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["target_ref"] = target_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "asset.reimport_texture",
            params,
        )

    def relations(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "asset.relations",
            params,
        )

    def render_target_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.render_target.create",
            params,
        )

    def render_target_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.render_target.update",
            params,
        )

    def runtime_virtual_texture_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.runtime_virtual_texture.create",
            params,
        )

    def runtime_virtual_texture_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.runtime_virtual_texture.update",
            params,
        )

    def sample(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "asset.sample",
            params,
        )

    def skeletal_mesh_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.skeletal_mesh.update",
            params,
        )

    def sound_attenuation_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sound_attenuation.create",
            params,
        )

    def sound_attenuation_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sound_attenuation.update",
            params,
        )

    def sound_class_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sound_class.create",
            params,
        )

    def sound_class_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sound_class.update",
            params,
        )

    def sound_concurrency_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sound_concurrency.create",
            params,
        )

    def sound_concurrency_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sound_concurrency.update",
            params,
        )

    def sound_mix_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sound_mix.create",
            params,
        )

    def sound_mix_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sound_mix.update",
            params,
        )

    def sound_submix_create(
        self,
        factory_ref: dict[str, Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["factory_ref"] = factory_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sound_submix.create",
            params,
        )

    def sound_submix_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sound_submix.update",
            params,
        )

    def sparse_volume_texture_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.sparse_volume_texture.update",
            params,
        )

    def static_mesh_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.static_mesh.update",
            params,
        )

    def subuv_animation_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.subuv_animation.create",
            params,
        )

    def subuv_animation_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.subuv_animation.update",
            params,
        )

    def summary(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "asset.summary",
            params,
        )

    def texture_array_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.texture_array.create",
            params,
        )

    def texture_array_replace(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.texture_array.replace",
            params,
        )

    def texture_collection_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.texture_collection.create",
            params,
        )

    def texture_collection_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.texture_collection.update",
            params,
        )

    def texture_cube_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.texture_cube.create",
            params,
        )

    def texture_cube_replace(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.texture_cube.replace",
            params,
        )

    def texture_cube_array_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.texture_cube_array.create",
            params,
        )

    def texture_cube_array_replace(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.texture_cube_array.replace",
            params,
        )

    def validation(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "asset.validation",
            params,
        )

    def volume_texture_create(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.volume_texture.create",
            params,
        )

    def volume_texture_replace(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.volume_texture.replace",
            params,
        )

class AssetDurableCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def journal_read(
        self,
        journal_id: str,
    ):
        params: dict[str, Any] = {}
        params["journal_id"] = journal_id
        return self._client.execute(
            "asset_durable.journal.read",
            params,
        )

    def journal_reconcile(
        self,
        journal_id: str,
        expected_journal_owner_id: str,
        expected_fencing_token: int,
        verification_id: str,
    ):
        params: dict[str, Any] = {}
        params["journal_id"] = journal_id
        params["expected_journal_owner_id"] = expected_journal_owner_id
        params["expected_fencing_token"] = expected_fencing_token
        params["verification_id"] = verification_id
        return self._client.execute(
            "asset_durable.journal.reconcile",
            params,
        )

class AudioCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def graph_candidates(
        self,
        target: str,
        *,
        query: str | object = OMITTED,
        id: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if id is not OMITTED:
            params["id"] = id
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "audio.graph.candidates",
            params,
        )

class AudioMediaCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def asset_create(
        self,
        asset_kind: str,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_kind"] = asset_kind
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "audio_media.asset.create",
            params,
        )

class BlueprintCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def asset_create(
        self,
        asset_name: str,
        package_path: str,
        parent_class_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        params["parent_class_ref"] = parent_class_ref
        return self._client.execute(
            "blueprint.asset.create",
            params,
        )

    def component_candidates(
        self,
        target: str,
        *,
        parent: str | object = OMITTED,
        query: str | object = OMITTED,
        id: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if parent is not OMITTED:
            params["parent"] = parent
        if query is not OMITTED:
            params["query"] = query
        if id is not OMITTED:
            params["id"] = id
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "blueprint.component.candidates",
            params,
        )

    def component_events_discover(
        self,
        asset_path: str,
        *,
        compile_before_query: bool | object = OMITTED,
        component_name: str,
        include_hidden: bool | object = OMITTED,
        limit: int | object = OMITTED,
        only_unbound: bool | object = OMITTED,
        query: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["asset_path"] = asset_path
        if compile_before_query is not OMITTED:
            params["compile_before_query"] = compile_before_query
        params["component_name"] = component_name
        if include_hidden is not OMITTED:
            params["include_hidden"] = include_hidden
        if limit is not OMITTED:
            params["limit"] = limit
        if only_unbound is not OMITTED:
            params["only_unbound"] = only_unbound
        if query is not OMITTED:
            params["query"] = query
        return self._client.execute(
            "blueprint.component.events.discover",
            params,
        )

    def node_candidates(
        self,
        target: str,
        graph_id: str,
        *,
        query: str | object = OMITTED,
        id: str | object = OMITTED,
        node_guid: str | object = OMITTED,
        pin_guid: str | object = OMITTED,
        pin_name: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["graph_id"] = graph_id
        if query is not OMITTED:
            params["query"] = query
        if id is not OMITTED:
            params["id"] = id
        if node_guid is not OMITTED:
            params["node_guid"] = node_guid
        if pin_guid is not OMITTED:
            params["pin_guid"] = pin_guid
        if pin_name is not OMITTED:
            params["pin_name"] = pin_name
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "blueprint.node.candidates",
            params,
        )

class CaptureCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def image_execute(
        self,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["subject_ref"] = subject_ref
        params["policy_id"] = policy_id
        params["parameters"] = parameters
        return self._client.execute(
            "capture.image.execute",
            params,
        )

    def media_execute(
        self,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["subject_ref"] = subject_ref
        params["policy_id"] = policy_id
        params["parameters"] = parameters
        return self._client.execute(
            "capture.media.execute",
            params,
        )

    def render_execute(
        self,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["subject_ref"] = subject_ref
        params["policy_id"] = policy_id
        params["parameters"] = parameters
        return self._client.execute(
            "capture.render.execute",
            params,
        )

class ConfigCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def resolved_value(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "config.resolved_value",
            params,
        )

    def section(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "config.section",
            params,
        )

class ContentGraphCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def authoring_schema(
        self,
        target: str,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        return self._client.execute(
            "content_graph.authoring_schema",
            params,
        )

    def compound(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "content_graph.compound",
            params,
        )

    def diagnostics(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "content_graph.diagnostics",
            params,
        )

    def export_workspace(
        self,
        target: str,
        workspace_path: str,
        *,
        profile_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["workspace_path"] = workspace_path
        if profile_id is not OMITTED:
            params["profile_id"] = profile_id
        return self._client.execute(
            "content_graph.export_workspace",
            params,
        )

    def import_workspace(
        self,
        target: str,
        source: dict[str, Any],
        expected_revision: str,
        authorization_id: str,
        *,
        limits: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["source"] = source
        params["expected_revision"] = expected_revision
        params["authorization_id"] = authorization_id
        if limits is not OMITTED:
            params["limits"] = limits
        return self._client.execute(
            "content_graph.import_workspace",
            params,
        )

    def items(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "content_graph.items",
            params,
        )

    def properties(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "content_graph.properties",
            params,
        )

    def relations(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "content_graph.relations",
            params,
        )

    def structure(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "content_graph.structure",
            params,
        )

    def summary(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "content_graph.summary",
            params,
        )

class DeformerCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def evaluation_sample(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "deformer.evaluation.sample",
            params,
        )

    def geometry_sample(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "deformer.geometry.sample",
            params,
        )

    def training_inputs_validate(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "deformer.training_inputs.validate",
            params,
        )

class EditorCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def dirty_resources(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "editor.dirty_resources",
            params,
        )

    def open_assets(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "editor.open_assets",
            params,
        )

    def safe_exit(
        self,
        dirty_resolution: dict[str, Any],
        external_witness: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["dirty_resolution"] = dirty_resolution
        params["external_witness"] = external_witness
        return self._client.execute(
            "editor.safe_exit",
            params,
        )

    def session(
        self,
        family_id: str,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["family_id"] = family_id
        params["subject_ref"] = subject_ref
        params["policy_id"] = policy_id
        params["parameters"] = parameters
        return self._client.execute(
            "editor.session",
            params,
        )

class EditorProjectCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def config_section_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.config_section.update",
            params,
        )

    def device_profile_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.device_profile.update",
            params,
        )

    def localization_target_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.localization_target.update",
            params,
        )

    def platform_config_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.platform_config.update",
            params,
        )

    def project_settings_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.project_settings.update",
            params,
        )

    def scalability_group_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.scalability_group.update",
            params,
        )

    def string_table_update(
        self,
        changes: list[Any],
        expected_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["expected_revision"] = expected_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.string_table.update",
            params,
        )

class ExternalCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def fbx_animation_import(
        self,
        source_ref: str,
        destination_ref: str,
        skeleton_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["destination_ref"] = destination_ref
        params["skeleton_ref"] = skeleton_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "external.fbx.animation.import",
            params,
        )

    def fbx_skeletal_mesh_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["destination_ref"] = destination_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "external.fbx.skeletal_mesh.import",
            params,
        )

    def geometry_cache_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["destination_ref"] = destination_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "external.geometry_cache.import",
            params,
        )

    def light_profile_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["destination_ref"] = destination_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "external.light_profile.import",
            params,
        )

    def localization_po_import(
        self,
        source_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "external.localization.po.import",
            params,
        )

    def skin_weight_profile_import(
        self,
        source_ref: str,
        target_ref: str,
        profile_name: str,
        lod_index: int,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["target_ref"] = target_ref
        params["profile_name"] = profile_name
        params["lod_index"] = lod_index
        return self._client.execute(
            "external.skin_weight_profile.import",
            params,
        )

    def sound_wave_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["destination_ref"] = destination_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "external.sound_wave.import",
            params,
        )

    def sparse_volume_texture_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["destination_ref"] = destination_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "external.sparse_volume_texture.import",
            params,
        )

    def texture_import(
        self,
        source_ref: str,
        destination_ref: str,
        *,
        options: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["destination_ref"] = destination_ref
        if options is not OMITTED:
            params["options"] = options
        return self._client.execute(
            "external.texture.import",
            params,
        )

class GraphCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def layout_apply(
        self,
        targets: list[Any],
        strategy: str,
        parameters: dict[str, Any],
        authorization_id: str,
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["targets"] = targets
        params["strategy"] = strategy
        params["parameters"] = parameters
        params["authorization_id"] = authorization_id
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "graph.layout.apply",
            params,
        )

    def view_read(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any],
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "graph.view.read",
            params,
        )

    def view_update(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "graph.view.update",
            params,
        )

class JobCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def compile_build(
        self,
        family_id: str,
        subject_ref: str,
        policy_id: str,
        parameters: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["family_id"] = family_id
        params["subject_ref"] = subject_ref
        params["policy_id"] = policy_id
        params["parameters"] = parameters
        return self._client.execute(
            "job.compile_build",
            params,
        )

class LandscapeCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def create(
        self,
        initial_height: dict[str, Any],
        placement: dict[str, Any],
        sample_region: dict[str, Any],
        target_ref: str,
        topology: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["initial_height"] = initial_height
        params["placement"] = placement
        params["sample_region"] = sample_region
        params["target_ref"] = target_ref
        params["topology"] = topology
        return self._client.execute(
            "landscape.create",
            params,
        )

    def height_read(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "landscape.height.read",
            params,
        )

    def height_delta(
        self,
        delta: dict[str, Any],
        region: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["delta"] = delta
        params["region"] = region
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        return self._client.execute(
            "landscape.height_delta",
            params,
        )

class MaterialCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def asset_create(
        self,
        asset_name: str,
        *,
        material_kind: str | object = OMITTED,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        if material_kind is not OMITTED:
            params["material_kind"] = material_kind
        params["package_path"] = package_path
        return self._client.execute(
            "material.asset.create",
            params,
        )

    def expression_candidates(
        self,
        target: str,
        *,
        query: str | object = OMITTED,
        graph_name: str | object = OMITTED,
        node_guid: str | object = OMITTED,
        pin_guid: str | object = OMITTED,
        pin_name: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if graph_name is not OMITTED:
            params["graph_name"] = graph_name
        if node_guid is not OMITTED:
            params["node_guid"] = node_guid
        if pin_guid is not OMITTED:
            params["pin_guid"] = pin_guid
        if pin_name is not OMITTED:
            params["pin_name"] = pin_name
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "material.expression.candidates",
            params,
        )

    def function_graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["edits"] = edits
        params["target_ref"] = target_ref
        return self._client.execute(
            "material.function.graph.apply",
            params,
        )

    def graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["edits"] = edits
        params["target_ref"] = target_ref
        return self._client.execute(
            "material.graph.apply",
            params,
        )

class MaterialInstanceCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def asset_create(
        self,
        asset_name: str,
        package_path: str,
        parent_material_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        params["parent_material_ref"] = parent_material_ref
        return self._client.execute(
            "material_instance.asset.create",
            params,
        )

    def parameters_apply(
        self,
        parameters: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["parameters"] = parameters
        params["target_ref"] = target_ref
        return self._client.execute(
            "material_instance.parameters.apply",
            params,
        )

class MeshCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def attribute_material_slot_add(
        self,
        material_ref: str,
        slot_name: str,
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["material_ref"] = material_ref
        params["slot_name"] = slot_name
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.attribute.material_slot.add",
            params,
        )

    def attribute_material_slot_assign(
        self,
        selection: dict[str, Any],
        slot_index: int,
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["selection"] = selection
        params["slot_index"] = slot_index
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.attribute.material_slot.assign",
            params,
        )

    def attribute_normals_recompute(
        self,
        *,
        angle_degrees: float | object = OMITTED,
        mode: str,
        preserve_existing_hard_edges: bool,
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        if angle_degrees is not OMITTED:
            params["angle_degrees"] = angle_degrees
        params["mode"] = mode
        params["preserve_existing_hard_edges"] = preserve_existing_hard_edges
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.attribute.normals.recompute",
            params,
        )

    def attribute_uv_auto(
        self,
        island_source: str,
        method: str,
        pack: bool,
        target_ref: str,
        target_revision: dict[str, Any],
        texture_resolution: int,
        uv_channel: int,
    ):
        params: dict[str, Any] = {}
        params["island_source"] = island_source
        params["method"] = method
        params["pack"] = pack
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        params["texture_resolution"] = texture_resolution
        params["uv_channel"] = uv_channel
        return self._client.execute(
            "mesh.attribute.uv.auto",
            params,
        )

    def attribute_uv_project(
        self,
        dimensions_cm: list[Any],
        projection_frame: dict[str, Any],
        projection_type: str,
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
        uv_channel: int,
    ):
        params: dict[str, Any] = {}
        params["dimensions_cm"] = dimensions_cm
        params["projection_frame"] = projection_frame
        params["projection_type"] = projection_type
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        params["uv_channel"] = uv_channel
        return self._client.execute(
            "mesh.attribute.uv.project",
            params,
        )

    def collision_convex_generate(
        self,
        max_hulls: int,
        max_vertices_per_hull: int,
        mode: str,
        replace_existing: bool,
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["max_hulls"] = max_hulls
        params["max_vertices_per_hull"] = max_vertices_per_hull
        params["mode"] = mode
        params["replace_existing"] = replace_existing
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.collision.convex.generate",
            params,
        )

    def collision_simple_generate(
        self,
        max_shapes: int,
        method: str,
        replace_existing: bool,
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["max_shapes"] = max_shapes
        params["method"] = method
        params["replace_existing"] = replace_existing
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.collision.simple.generate",
            params,
        )

    def element_select_by_ray(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "mesh.element.select_by_ray",
            params,
        )

    def modeling_session(
        self,
        action: str,
        *,
        target: str | object = OMITTED,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["action"] = action
        if target is not OMITTED:
            params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "mesh.modeling_session",
            params,
        )

    def pivot_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "mesh.pivot.update",
            params,
        )

    def primitive_box_create(
        self,
        anchor: str,
        placement: dict[str, Any],
        size_cm: list[Any],
        subdivisions: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["anchor"] = anchor
        params["placement"] = placement
        params["size_cm"] = size_cm
        params["subdivisions"] = subdivisions
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.primitive.box.create",
            params,
        )

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
    ):
        params: dict[str, Any] = {}
        params["anchor"] = anchor
        params["cap_ends"] = cap_ends
        params["height_cm"] = height_cm
        params["height_segments"] = height_segments
        params["placement"] = placement
        params["radial_segments"] = radial_segments
        params["radius_cm"] = radius_cm
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.primitive.cylinder.create",
            params,
        )

    def primitive_plane_create(
        self,
        double_sided: bool,
        placement: dict[str, Any],
        size_cm: list[Any],
        subdivisions: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["double_sided"] = double_sided
        params["placement"] = placement
        params["size_cm"] = size_cm
        params["subdivisions"] = subdivisions
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.primitive.plane.create",
            params,
        )

    def primitive_ramp_create(
        self,
        placement: dict[str, Any],
        rise_direction: str,
        size_cm: list[Any],
        slope_axis: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["placement"] = placement
        params["rise_direction"] = rise_direction
        params["size_cm"] = size_cm
        params["slope_axis"] = slope_axis
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.primitive.ramp.create",
            params,
        )

    def primitive_ramp_corner_create(
        self,
        high_corner: str,
        placement: dict[str, Any],
        size_cm: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["high_corner"] = high_corner
        params["placement"] = placement
        params["size_cm"] = size_cm
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.primitive.ramp_corner.create",
            params,
        )

    def primitive_sphere_create(
        self,
        latitude_segments: int,
        longitude_segments: int,
        placement: dict[str, Any],
        radius_cm: float,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["latitude_segments"] = latitude_segments
        params["longitude_segments"] = longitude_segments
        params["placement"] = placement
        params["radius_cm"] = radius_cm
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.primitive.sphere.create",
            params,
        )

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
    ):
        params: dict[str, Any] = {}
        params["placement"] = placement
        params["rise_axis"] = rise_axis
        params["rise_direction"] = rise_direction
        params["step_count"] = step_count
        params["step_depth_cm"] = step_depth_cm
        params["step_height_cm"] = step_height_cm
        params["step_width_cm"] = step_width_cm
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.primitive.stairs.create",
            params,
        )

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
    ):
        params: dict[str, Any] = {}
        params["operand_ref"] = operand_ref
        params["operand_revision"] = operand_revision
        params["operand_to_target"] = operand_to_target
        params["operation"] = operation
        params["simplify_output"] = simplify_output
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.boolean",
            params,
        )

    def topology_edges_bevel(
        self,
        distance_cm: float,
        roundness: float,
        segments: int,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["distance_cm"] = distance_cm
        params["roundness"] = roundness
        params["segments"] = segments
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.edges.bevel",
            params,
        )

    def topology_edges_weld(
        self,
        edge_pairs: list[Any],
        target_ref: str,
        target_revision: dict[str, Any],
        tolerance_cm: float,
    ):
        params: dict[str, Any] = {}
        params["edge_pairs"] = edge_pairs
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        params["tolerance_cm"] = tolerance_cm
        return self._client.execute(
            "mesh.topology.edges.weld",
            params,
        )

    def topology_faces_duplicate(
        self,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
        translation_cm: list[Any],
    ):
        params: dict[str, Any] = {}
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        params["translation_cm"] = translation_cm
        return self._client.execute(
            "mesh.topology.faces.duplicate",
            params,
        )

    def topology_faces_extrude(
        self,
        *,
        direction: dict[str, Any] | object = OMITTED,
        direction_mode: str,
        distance_cm: float,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        if direction is not OMITTED:
            params["direction"] = direction
        params["direction_mode"] = direction_mode
        params["distance_cm"] = distance_cm
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.faces.extrude",
            params,
        )

    def topology_faces_inset(
        self,
        boundary_mode: str,
        distance_cm: float,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["boundary_mode"] = boundary_mode
        params["distance_cm"] = distance_cm
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.faces.inset",
            params,
        )

    def topology_faces_offset(
        self,
        distance_cm: float,
        offset_mode: str,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["distance_cm"] = distance_cm
        params["offset_mode"] = offset_mode
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.faces.offset",
            params,
        )

    def topology_faces_push_pull(
        self,
        *,
        direction: dict[str, Any] | object = OMITTED,
        direction_mode: str,
        distance_cm: float,
        selection: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        if direction is not OMITTED:
            params["direction"] = direction
        params["direction_mode"] = direction_mode
        params["distance_cm"] = distance_cm
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.faces.push_pull",
            params,
        )

    def topology_holes_fill(
        self,
        fill_mode: str,
        selection: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["fill_mode"] = fill_mode
        params["selection"] = selection
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.holes.fill",
            params,
        )

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
    ):
        params: dict[str, Any] = {}
        params["fill_cut"] = fill_cut
        params["keep_sides"] = keep_sides
        params["operand_ref"] = operand_ref
        params["operand_revision"] = operand_revision
        params["operand_to_target"] = operand_to_target
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.mesh_cut",
            params,
        )

    def topology_mirror(
        self,
        keep_original: bool,
        plane: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
        weld_seam: bool,
    ):
        params: dict[str, Any] = {}
        params["keep_original"] = keep_original
        params["plane"] = plane
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        params["weld_seam"] = weld_seam
        return self._client.execute(
            "mesh.topology.mirror",
            params,
        )

    def topology_plane_cut(
        self,
        fill_hole: bool,
        keep_side: str,
        plane: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["fill_hole"] = fill_hole
        params["keep_side"] = keep_side
        params["plane"] = plane
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.plane_cut",
            params,
        )

    def topology_remesh(
        self,
        iterations: int,
        preserve_boundaries: bool,
        preserve_sharp_edges: bool,
        space_contract: dict[str, Any],
        target_edge_length_cm: float,
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["iterations"] = iterations
        params["preserve_boundaries"] = preserve_boundaries
        params["preserve_sharp_edges"] = preserve_sharp_edges
        params["space_contract"] = space_contract
        params["target_edge_length_cm"] = target_edge_length_cm
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.remesh",
            params,
        )

    def topology_simplify(
        self,
        preserve_boundaries: bool,
        target_mode: str,
        target_ref: str,
        target_revision: dict[str, Any],
        target_value: float,
    ):
        params: dict[str, Any] = {}
        params["preserve_boundaries"] = preserve_boundaries
        params["target_mode"] = target_mode
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        params["target_value"] = target_value
        return self._client.execute(
            "mesh.topology.simplify",
            params,
        )

    def topology_subdivide(
        self,
        levels: int,
        scheme: str,
        target_ref: str,
        target_revision: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["levels"] = levels
        params["scheme"] = scheme
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.subdivide",
            params,
        )

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
    ):
        params: dict[str, Any] = {}
        params["fill_hole"] = fill_hole
        params["keep_region"] = keep_region
        params["operand_ref"] = operand_ref
        params["operand_revision"] = operand_revision
        params["operand_to_target"] = operand_to_target
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        return self._client.execute(
            "mesh.topology.trim",
            params,
        )

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
    ):
        params: dict[str, Any] = {}
        params["adaptivity"] = adaptivity
        params["operand_ref"] = operand_ref
        params["operand_revision"] = operand_revision
        params["operand_to_target"] = operand_to_target
        params["operation"] = operation
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        params["target_revision"] = target_revision
        params["voxel_size_cm"] = voxel_size_cm
        return self._client.execute(
            "mesh.topology.voxel_boolean",
            params,
        )

    def transform_bake(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "mesh.transform.bake",
            params,
        )

    def voxel_grid_apply(
        self,
        session_id: str,
        expected_revision: int,
        *,
        mesh_build: str | object = OMITTED,
        collision: dict[str, Any] | object = OMITTED,
        material_ref: str | object = OMITTED,
        keep_session: bool | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["session_id"] = session_id
        params["expected_revision"] = expected_revision
        if mesh_build is not OMITTED:
            params["mesh_build"] = mesh_build
        if collision is not OMITTED:
            params["collision"] = collision
        if material_ref is not OMITTED:
            params["material_ref"] = material_ref
        if keep_session is not OMITTED:
            params["keep_session"] = keep_session
        return self._client.execute(
            "mesh.voxel_grid.apply",
            params,
        )

    def voxel_grid_session(
        self,
        action: str,
        *,
        session_id: str | object = OMITTED,
        expected_revision: int | object = OMITTED,
        mode: str | object = OMITTED,
        grid_id: str | object = OMITTED,
        actor_ref: str | object = OMITTED,
        label: str | object = OMITTED,
        cell_size: float | object = OMITTED,
        origin: dict[str, Any] | object = OMITTED,
        rotation: dict[str, Any] | object = OMITTED,
        anchor: dict[str, Any] | object = OMITTED,
        bounds: dict[str, Any] | object = OMITTED,
        max_operation_cells: int | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["action"] = action
        if session_id is not OMITTED:
            params["session_id"] = session_id
        if expected_revision is not OMITTED:
            params["expected_revision"] = expected_revision
        if mode is not OMITTED:
            params["mode"] = mode
        if grid_id is not OMITTED:
            params["grid_id"] = grid_id
        if actor_ref is not OMITTED:
            params["actor_ref"] = actor_ref
        if label is not OMITTED:
            params["label"] = label
        if cell_size is not OMITTED:
            params["cell_size"] = cell_size
        if origin is not OMITTED:
            params["origin"] = origin
        if rotation is not OMITTED:
            params["rotation"] = rotation
        if anchor is not OMITTED:
            params["anchor"] = anchor
        if bounds is not OMITTED:
            params["bounds"] = bounds
        if max_operation_cells is not OMITTED:
            params["max_operation_cells"] = max_operation_cells
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "mesh.voxel_grid.session",
            params,
        )

class MetasoundCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def graph_compile_settle(
        self,
        expected_document_revision: str,
        registration_policy: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["expected_document_revision"] = expected_document_revision
        params["registration_policy"] = registration_policy
        params["target_ref"] = target_ref
        return self._client.execute(
            "metasound.graph.compile_settle",
            params,
        )

    def graph_default_mutate(
        self,
        data_type_ref: str,
        intent: str,
        node_guid: str,
        target_ref: str,
        value: Any,
        vertex_guid: str,
    ):
        params: dict[str, Any] = {}
        params["data_type_ref"] = data_type_ref
        params["intent"] = intent
        params["node_guid"] = node_guid
        params["target_ref"] = target_ref
        params["value"] = value
        params["vertex_guid"] = vertex_guid
        return self._client.execute(
            "metasound.graph.default.mutate",
            params,
        )

    def graph_interface_mutate(
        self,
        changes: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["target_ref"] = target_ref
        return self._client.execute(
            "metasound.graph.interface.mutate",
            params,
        )

    def graph_link_mutate(
        self,
        links: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["links"] = links
        params["target_ref"] = target_ref
        return self._client.execute(
            "metasound.graph.link.mutate",
            params,
        )

    def graph_node_mutate(
        self,
        nodes: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["nodes"] = nodes
        params["target_ref"] = target_ref
        return self._client.execute(
            "metasound.graph.node.mutate",
            params,
        )

class ModelingCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def actor_mesh_replace(
        self,
        actor_ref: str,
        mesh_ref: str,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["actor_ref"] = actor_ref
        params["mesh_ref"] = mesh_ref
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "modeling.actor.mesh.replace",
            params,
        )

    def asset_material_slot_remove(
        self,
        target_ref: str,
        index: int,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        params["index"] = index
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "modeling.asset.material_slot.remove",
            params,
        )

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
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["actor_ref"] = actor_ref
        params["component_name"] = component_name
        params["space"] = space
        params["min_x"] = min_x
        params["min_y"] = min_y
        params["min_z"] = min_z
        params["max_x"] = max_x
        params["max_y"] = max_y
        params["max_z"] = max_z
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "modeling.voxel.bounds.remove",
            params,
        )

class NiagaraCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def asset_duplicate(
        self,
        source_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "niagara.asset.duplicate",
            params,
        )

    def compile_refresh_settle(
        self,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        return self._client.execute(
            "niagara.compile_refresh_settle",
            params,
        )

    def compound_apply(
        self,
        emitter_handle_id: str,
        input_name: str,
        module_ref: str,
        stage_ref: str,
        target_ref: str,
        value: Any,
    ):
        params: dict[str, Any] = {}
        params["emitter_handle_id"] = emitter_handle_id
        params["input_name"] = input_name
        params["module_ref"] = module_ref
        params["stage_ref"] = stage_ref
        params["target_ref"] = target_ref
        params["value"] = value
        return self._client.execute(
            "niagara.compound.apply",
            params,
        )

    def emitter_asset_create(
        self,
        asset_name: str,
        package_path: str,
        source_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        params["source_ref"] = source_ref
        return self._client.execute(
            "niagara.emitter.asset.create",
            params,
        )

    def module_candidates(
        self,
        target: str,
        target_usage: str,
        *,
        target_usage_id: str | object = OMITTED,
        emitter_handle_id: str | object = OMITTED,
        query: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["target_usage"] = target_usage
        if target_usage_id is not OMITTED:
            params["target_usage_id"] = target_usage_id
        if emitter_handle_id is not OMITTED:
            params["emitter_handle_id"] = emitter_handle_id
        if query is not OMITTED:
            params["query"] = query
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "niagara.module.candidates",
            params,
        )

    def renderer_event_parameter_apply(
        self,
        emitter_handle_id: str,
        parameter_name: str,
        renderer_ref: str,
        target_ref: str,
        type_ref: str,
        value: Any,
    ):
        params: dict[str, Any] = {}
        params["emitter_handle_id"] = emitter_handle_id
        params["parameter_name"] = parameter_name
        params["renderer_ref"] = renderer_ref
        params["target_ref"] = target_ref
        params["type_ref"] = type_ref
        params["value"] = value
        return self._client.execute(
            "niagara.renderer_event_parameter.apply",
            params,
        )

    def stack_issue_fix(
        self,
        emitter_handle_id: str,
        fix_id: str,
        issue_id: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["emitter_handle_id"] = emitter_handle_id
        params["fix_id"] = fix_id
        params["issue_id"] = issue_id
        params["target_ref"] = target_ref
        return self._client.execute(
            "niagara.stack.issue_fix",
            params,
        )

    def stack_reorder(
        self,
        emitter_handle_id: str,
        item_ref: str,
        predecessor_ref: str,
        stage_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["emitter_handle_id"] = emitter_handle_id
        params["item_ref"] = item_ref
        params["predecessor_ref"] = predecessor_ref
        params["stage_ref"] = stage_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "niagara.stack.reorder",
            params,
        )

    def system_asset_create(
        self,
        asset_name: str,
        package_path: str,
        source_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        params["source_ref"] = source_ref
        return self._client.execute(
            "niagara.system.asset.create",
            params,
        )

class OperationCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def cancel(
        self,
        operation_ref: dict[str, Any],
        reason: str,
    ):
        params: dict[str, Any] = {}
        params["operation_ref"] = operation_ref
        params["reason"] = reason
        return self._client.execute(
            "operation.cancel",
            params,
        )

    def plan_execute(
        self,
        steps: list[Any],
        on_error: str,
        atomicity: str,
    ):
        params: dict[str, Any] = {}
        params["steps"] = steps
        params["on_error"] = on_error
        params["atomicity"] = atomicity
        return self._client.execute(
            "operation.plan.execute",
            params,
        )

    def receipt(
        self,
        operation_ref: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["operation_ref"] = operation_ref
        return self._client.execute(
            "operation.receipt",
            params,
        )

    def reconcile(
        self,
        operation_ref: dict[str, Any],
        expected_generation: int,
    ):
        params: dict[str, Any] = {}
        params["operation_ref"] = operation_ref
        params["expected_generation"] = expected_generation
        return self._client.execute(
            "operation.reconcile",
            params,
        )

    def release(
        self,
        operation_ref: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["operation_ref"] = operation_ref
        return self._client.execute(
            "operation.release",
            params,
        )

    def resume(
        self,
        operation_ref: dict[str, Any],
        expected_generation: int,
    ):
        params: dict[str, Any] = {}
        params["operation_ref"] = operation_ref
        params["expected_generation"] = expected_generation
        return self._client.execute(
            "operation.resume",
            params,
        )

    def status(
        self,
        operation_ref: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["operation_ref"] = operation_ref
        return self._client.execute(
            "operation.status",
            params,
        )

class PcgCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def component_apply(
        self,
        generation_policy: str,
        graph_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["generation_policy"] = generation_policy
        params["graph_ref"] = graph_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "pcg.component.apply",
            params,
        )

    def component_world_binding_apply(
        self,
        actor_ref: str,
        component_ref: str,
        generation_policy: str,
        graph_ref: str,
    ):
        params: dict[str, Any] = {}
        params["actor_ref"] = actor_ref
        params["component_ref"] = component_ref
        params["generation_policy"] = generation_policy
        params["graph_ref"] = graph_ref
        return self._client.execute(
            "pcg.component.world_binding.apply",
            params,
        )

    def data_asset_apply(
        self,
        content_revision: str,
        data_type_ref: str,
        source_ref: str,
        target_ref: str,
        value: Any,
    ):
        params: dict[str, Any] = {}
        params["content_revision"] = content_revision
        params["data_type_ref"] = data_type_ref
        params["source_ref"] = source_ref
        params["target_ref"] = target_ref
        params["value"] = value
        return self._client.execute(
            "pcg.data_asset.apply",
            params,
        )

    def data_asset_create_from_level(
        self,
        data_type_ref: str,
        source_level_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["data_type_ref"] = data_type_ref
        params["source_level_ref"] = source_level_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "pcg.data_asset.create_from_level",
            params,
        )

    def generated_spatial_data_read(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "pcg.generated_spatial_data.read",
            params,
        )

    def graph_apply(
        self,
        edits: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["edits"] = edits
        params["target_ref"] = target_ref
        return self._client.execute(
            "pcg.graph.apply",
            params,
        )

    def graph_asset_create(
        self,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "pcg.graph.asset.create",
            params,
        )

    def graph_instance_apply(
        self,
        graph_ref: str,
        overrides: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["graph_ref"] = graph_ref
        params["overrides"] = overrides
        params["target_ref"] = target_ref
        return self._client.execute(
            "pcg.graph_instance.apply",
            params,
        )

    def graph_parameters_apply(
        self,
        parameters: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["parameters"] = parameters
        params["target_ref"] = target_ref
        return self._client.execute(
            "pcg.graph_parameters.apply",
            params,
        )

    def node_candidates(
        self,
        target: str,
        *,
        query: str | object = OMITTED,
        id: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if id is not OMITTED:
            params["id"] = id
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "pcg.node.candidates",
            params,
        )

    def partition_spatial_state_read(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "pcg.partition.spatial_state.read",
            params,
        )

class PhysicsCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def asset_structure_replace(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "physics.asset.structure.replace",
            params,
        )

    def constraint_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "physics.constraint.update",
            params,
        )

    def material_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "physics.material.update",
            params,
        )

    def simulation_probe(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "physics.simulation.probe",
            params,
        )

class ProjectCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def platform(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "project.platform",
            params,
        )

    def settings(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "project.settings",
            params,
        )

    def summary(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "project.summary",
            params,
        )

    def validation(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "project.validation",
            params,
        )

class QueryCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def calibration_read(
        self,
        category: str,
        *,
        search_text: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["category"] = category
        if search_text is not OMITTED:
            params["search_text"] = search_text
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "query.calibration.read",
            params,
        )

    def command_detail(
        self,
        command_id: str,
        contract_hash: str,
        *,
        variant_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["command_id"] = command_id
        params["contract_hash"] = contract_hash
        if variant_id is not OMITTED:
            params["variant_id"] = variant_id
        return self._client.execute(
            "query.command.detail",
            params,
        )

    def command_search(
        self,
        intent: str,
        *,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["intent"] = intent
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "query.command.search",
            params,
        )

    def content_search(
        self,
        *,
        query: str | object = OMITTED,
        match_mode: str | object = OMITTED,
        content_kinds: list[Any] | object = OMITTED,
        class_path: str | object = OMITTED,
        path_prefix: str | object = OMITTED,
        owner_identity: str | object = OMITTED,
        required_operations: list[Any] | object = OMITTED,
        limit_per_provider: int | object = OMITTED,
        cursor: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if query is not OMITTED:
            params["query"] = query
        if match_mode is not OMITTED:
            params["match_mode"] = match_mode
        if content_kinds is not OMITTED:
            params["content_kinds"] = content_kinds
        if class_path is not OMITTED:
            params["class_path"] = class_path
        if path_prefix is not OMITTED:
            params["path_prefix"] = path_prefix
        if owner_identity is not OMITTED:
            params["owner_identity"] = owner_identity
        if required_operations is not OMITTED:
            params["required_operations"] = required_operations
        if limit_per_provider is not OMITTED:
            params["limit_per_provider"] = limit_per_provider
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "query.content.search",
            params,
        )

class ReferenceCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def asset_apply(
        self,
        object_path: str,
        intent: str,
        *,
        proposed_text: str | None | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["object_path"] = object_path
        params["intent"] = intent
        if proposed_text is not OMITTED:
            params["proposed_text"] = proposed_text
        return self._client.execute(
            "reference.asset_apply",
            params,
        )

    def asset_read(
        self,
        object_path: str,
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["object_path"] = object_path
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "reference.asset_read",
            params,
        )

    def origin_resolve(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "reference.origin.resolve",
            params,
        )

class RigCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def control_bake_animation(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "rig.control.bake.animation",
            params,
        )

    def control_bake_controls(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "rig.control.bake.controls",
            params,
        )

    def ik_definition_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "rig.ik.definition.update",
            params,
        )

    def retarget_assets_generate(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "rig.retarget.assets.generate",
            params,
        )

    def retarget_definition_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "rig.retarget.definition.update",
            params,
        )

    def retarget_pose_auto_align(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "rig.retarget.pose.auto_align",
            params,
        )

    def retarget_pose_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "rig.retarget.pose.update",
            params,
        )

    def skeleton_preview_mesh_bind(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "rig.skeleton.preview_mesh.bind",
            params,
        )

    def skeleton_socket_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "rig.skeleton.socket.update",
            params,
        )

class SkeletalMeshCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def remove_morph_target(
        self,
        target_ref: str,
        name: str,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        params["name"] = name
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "skeletal_mesh.remove_morph_target",
            params,
        )

    def remove_skin_weight_profile(
        self,
        target_ref: str,
        name: str,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        params["name"] = name
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "skeletal_mesh.remove_skin_weight_profile",
            params,
        )

class SoundCueCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def graph_compile_settle(
        self,
        expected_graph_revision: str,
        sync_policy: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["expected_graph_revision"] = expected_graph_revision
        params["sync_policy"] = sync_policy
        params["target_ref"] = target_ref
        return self._client.execute(
            "sound_cue.graph.compile_settle",
            params,
        )

    def graph_node_mutate(
        self,
        nodes: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["nodes"] = nodes
        params["target_ref"] = target_ref
        return self._client.execute(
            "sound_cue.graph.node.mutate",
            params,
        )

    def graph_relation_mutate(
        self,
        relations: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["relations"] = relations
        params["target_ref"] = target_ref
        return self._client.execute(
            "sound_cue.graph.relation.mutate",
            params,
        )

    def graph_root_mutate(
        self,
        intent: str,
        root_node_object_path: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["intent"] = intent
        params["root_node_object_path"] = root_node_object_path
        params["target_ref"] = target_ref
        return self._client.execute(
            "sound_cue.graph.root.mutate",
            params,
        )

class TextureGraphCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def artifact_bake(
        self,
        target: str,
        expected_revision: str,
        outputs: list[Any],
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["expected_revision"] = expected_revision
        params["outputs"] = outputs
        return self._client.execute(
            "texture_graph.artifact.bake",
            params,
        )

    def artifact_capture(
        self,
        expected_settled_revision: str,
        outputs: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["expected_settled_revision"] = expected_settled_revision
        params["outputs"] = outputs
        params["target_ref"] = target_ref
        return self._client.execute(
            "texture_graph.artifact.capture",
            params,
        )

    def graph_link_mutate(
        self,
        links: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["links"] = links
        params["target_ref"] = target_ref
        return self._client.execute(
            "texture_graph.graph.link.mutate",
            params,
        )

    def graph_node_mutate(
        self,
        nodes: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["nodes"] = nodes
        params["target_ref"] = target_ref
        return self._client.execute(
            "texture_graph.graph.node.mutate",
            params,
        )

    def graph_parameter_mutate(
        self,
        parameters: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["parameters"] = parameters
        params["target_ref"] = target_ref
        return self._client.execute(
            "texture_graph.graph.parameter.mutate",
            params,
        )

    def graph_validate_evaluate_settle(
        self,
        evaluation_policy: str,
        expected_graph_revision: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["evaluation_policy"] = evaluation_policy
        params["expected_graph_revision"] = expected_graph_revision
        params["target_ref"] = target_ref
        return self._client.execute(
            "texture_graph.graph.validate_evaluate_settle",
            params,
        )

    def runtime_probe(
        self,
        target: str,
        *,
        render_output_index: int | object = OMITTED,
        expected_stats: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if render_output_index is not OMITTED:
            params["render_output_index"] = render_output_index
        if expected_stats is not OMITTED:
            params["expected_stats"] = expected_stats
        return self._client.execute(
            "texture_graph.runtime.probe",
            params,
        )

class TimelineCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def sequence_create(
        self,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "timeline.sequence.create",
            params,
        )

    def sequence_read(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "timeline.sequence.read",
            params,
        )

    def sequence_settings_update(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "timeline.sequence.settings.update",
            params,
        )

    def sequence_structure_replace(
        self,
        target: str,
        input: dict[str, Any],
        *,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "timeline.sequence.structure.replace",
            params,
        )

    def widget_animation_read(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "timeline.widget_animation.read",
            params,
        )

class UmgCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def asset_create(
        self,
        asset_name: str,
        package_path: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        params["package_path"] = package_path
        return self._client.execute(
            "umg.asset.create",
            params,
        )

    def widget_candidates(
        self,
        target: str,
        *,
        query: str | object = OMITTED,
        id: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if id is not OMITTED:
            params["id"] = id
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "umg.widget.candidates",
            params,
        )

    def widget_events_discover(
        self,
        owner_item_ref: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["owner_item_ref"] = owner_item_ref
        params["target_ref"] = target_ref
        return self._client.execute(
            "umg.widget.events.discover",
            params,
        )

class ViewportCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def actor_pick(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.actor.pick",
            params,
        )

    def actor_select(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.actor.select",
            params,
        )

    def camera_frame(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.camera.frame",
            params,
        )

    def instance_list(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.instance.list",
            params,
        )

    def pixel_scale_read(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.pixel_scale.read",
            params,
        )

    def ray_deproject(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.ray.deproject",
            params,
        )

    def ray_trace(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.ray.trace",
            params,
        )

    def state_read(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any],
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.state.read",
            params,
        )

    def state_restore(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.state.restore",
            params,
        )

    def state_update(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.state.update",
            params,
        )

    def view_mode_list(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any],
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.view_mode.list",
            params,
        )

    def warning_list(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any],
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "viewport.warning.list",
            params,
        )

class WorldCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def actor_candidates(
        self,
        target: str,
        *,
        category: str | object = OMITTED,
        query: str | object = OMITTED,
        id: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if category is not OMITTED:
            params["category"] = category
        if query is not OMITTED:
            params["query"] = query
        if id is not OMITTED:
            params["id"] = id
        if limit is not OMITTED:
            params["limit"] = limit
        if cursor is not OMITTED:
            params["cursor"] = cursor
        return self._client.execute(
            "world.actor.candidates",
            params,
        )

    def actor_create(
        self,
        actor_class_ref: str,
        *,
        folder_path: str | object = OMITTED,
        label: str,
        placement: dict[str, Any],
        tags: list[Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["actor_class_ref"] = actor_class_ref
        if folder_path is not OMITTED:
            params["folder_path"] = folder_path
        params["label"] = label
        params["placement"] = placement
        if tags is not OMITTED:
            params["tags"] = tags
        return self._client.execute(
            "world.actor.create",
            params,
        )

    def actor_components(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.actor_components",
            params,
        )

    def actor_hlod_layer_update(
        self,
        *,
        collection_ref: str | object = OMITTED,
        mode: str,
        subject_refs: list[Any],
    ):
        params: dict[str, Any] = {}
        if collection_ref is not OMITTED:
            params["collection_ref"] = collection_ref
        params["mode"] = mode
        params["subject_refs"] = subject_refs
        return self._client.execute(
            "world.actor_hlod_layer.update",
            params,
        )

    def actor_streaming_policy_update(
        self,
        changes: dict[str, Any],
        target_refs: list[Any],
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["target_refs"] = target_refs
        return self._client.execute(
            "world.actor_streaming_policy.update",
            params,
        )

    def actors(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.actors",
            params,
        )

    def capsule_path(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.capsule_path",
            params,
        )

    def capsule_sweep(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.capsule_sweep",
            params,
        )

    def content(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.content",
            params,
        )

    def data_layer_delete(
        self,
        layer: str,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["layer"] = layer
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "world.data_layer.delete",
            params,
        )

    def data_layer_instance_create(
        self,
        *,
        asset_ref: str | object = OMITTED,
        initial_state: dict[str, Any] | object = OMITTED,
        parent_ref: str | object = OMITTED,
        private: bool | object = OMITTED,
        short_name: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if asset_ref is not OMITTED:
            params["asset_ref"] = asset_ref
        if initial_state is not OMITTED:
            params["initial_state"] = initial_state
        if parent_ref is not OMITTED:
            params["parent_ref"] = parent_ref
        if private is not OMITTED:
            params["private"] = private
        if short_name is not OMITTED:
            params["short_name"] = short_name
        return self._client.execute(
            "world.data_layer_instance.create",
            params,
        )

    def data_layer_relation_update(
        self,
        collection_refs: list[Any],
        mode: str,
        relation_kind: str,
        subject_refs: list[Any],
    ):
        params: dict[str, Any] = {}
        params["collection_refs"] = collection_refs
        params["mode"] = mode
        params["relation_kind"] = relation_kind
        params["subject_refs"] = subject_refs
        return self._client.execute(
            "world.data_layer_relation.update",
            params,
        )

    def data_layer_state_update(
        self,
        changes: dict[str, Any],
        target_refs: list[Any],
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["target_refs"] = target_refs
        return self._client.execute(
            "world.data_layer_state.update",
            params,
        )

    def data_layers(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.data_layers",
            params,
        )

    def hlod_assignments(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.hlod_assignments",
            params,
        )

    def level_content_delete_scope(
        self,
        folder_path: str,
        *,
        managed_id: str | object = OMITTED,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["folder_path"] = folder_path
        if managed_id is not OMITTED:
            params["managed_id"] = managed_id
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "world.level_content.delete_scope",
            params,
        )

    def level_game_mode_update(
        self,
        game_mode_class_ref: str,
    ):
        params: dict[str, Any] = {}
        params["game_mode_class_ref"] = game_mode_class_ref
        return self._client.execute(
            "world.level_game_mode.update",
            params,
        )

    def level_streaming_move_actors(
        self,
        actor_ref: str,
        level_package: str,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["actor_ref"] = actor_ref
        params["level_package"] = level_package
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "world.level_streaming.move_actors",
            params,
        )

    def level_streaming_remove(
        self,
        level_package: str,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["level_package"] = level_package
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "world.level_streaming.remove",
            params,
        )

    def mesh_closest_vertex(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.mesh_closest_vertex",
            params,
        )

    def mesh_vertex_position(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.mesh_vertex_position",
            params,
        )

    def nav_connectivity(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.nav_connectivity",
            params,
        )

    def nav_find_path(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.nav_find_path",
            params,
        )

    def nav_project_point(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.nav_project_point",
            params,
        )

    def nearby_shapes(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.nearby_shapes",
            params,
        )

    def object_align(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.object_align",
            params,
        )

    def object_snap_to_surface(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.object_snap_to_surface",
            params,
        )

    def object_transform_read(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.object_transform.read",
            params,
        )

    def object_transform_update(
        self,
        target: str,
        input: dict[str, Any],
        context: dict[str, Any],
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["input"] = input
        params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.object_transform.update",
            params,
        )

    def overlap(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.overlap",
            params,
        )

    def partition(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.partition",
            params,
        )

    def partition_health(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.partition_health",
            params,
        )

    def pcg_cleanup(
        self,
        actor_ref: str,
        component_name: str,
        *,
        destructive_authorization_id: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["actor_ref"] = actor_ref
        params["component_name"] = component_name
        if destructive_authorization_id is not OMITTED:
            params["destructive_authorization_id"] = destructive_authorization_id
        return self._client.execute(
            "world.pcg.cleanup",
            params,
        )

    def physics_component(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.physics_component",
            params,
        )

    def physics_constraint(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.physics_constraint",
            params,
        )

    def property(
        self,
        target: str,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.property",
            params,
        )

    def ray_trace(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.ray_trace",
            params,
        )

    def selection(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.selection",
            params,
        )

    def streaming_levels(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.streaming_levels",
            params,
        )

    def streaming_relation_create(
        self,
        level_asset_ref: str,
        *,
        placement: dict[str, Any] | object = OMITTED,
        streaming_class_ref: str,
    ):
        params: dict[str, Any] = {}
        params["level_asset_ref"] = level_asset_ref
        if placement is not OMITTED:
            params["placement"] = placement
        params["streaming_class_ref"] = streaming_class_ref
        return self._client.execute(
            "world.streaming_relation.create",
            params,
        )

    def streaming_relation_state_update(
        self,
        changes: dict[str, Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["target_ref"] = target_ref
        return self._client.execute(
            "world.streaming_relation.state.update",
            params,
        )

    def summary(
        self,
        *,
        input: dict[str, Any] | object = OMITTED,
        context: dict[str, Any] | object = OMITTED,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if input is not OMITTED:
            params["input"] = input
        if context is not OMITTED:
            params["context"] = context
        if projection is not OMITTED:
            params["projection"] = projection
        return self._client.execute(
            "world.summary",
            params,
        )

    def wall_create_with_opening(
        self,
        opening: dict[str, Any],
        plane: dict[str, Any],
        segment_template: dict[str, Any],
        wall: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["opening"] = opening
        params["plane"] = plane
        params["segment_template"] = segment_template
        params["wall"] = wall
        return self._client.execute(
            "world.wall.create_with_opening",
            params,
        )

    def world_partition_streaming_update(
        self,
        enabled: bool,
    ):
        params: dict[str, Any] = {}
        params["enabled"] = enabled
        return self._client.execute(
            "world.world_partition_streaming.update",
            params,
        )

BINDING_CATALOG = CommandBindingCatalog(
    (
        CommandBinding(
            command_id="ai.behavior.candidates",
            binding_hash="sha256:d7d5d374557bf2cf7bf0fc5536603bca6e9df3c6ac42aae78305c4d9e9d4760c",
            namespace="ai",
            method="behavior_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.behavior_tree.asset.create",
            binding_hash="sha256:14b58f20f9eb153956508bd0bdcfa6badc3f9fbde991e75585a79e5a5c6f9872",
            namespace="ai",
            method="behavior_tree_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.behavior_tree.graph.apply",
            binding_hash="sha256:2af81cf3ef6f77be4a0510ea1989d49f0ceb863e8a39cdd4bd465d725a3f70a2",
            namespace="ai",
            method="behavior_tree_graph_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.blackboard.asset.create",
            binding_hash="sha256:f43c0684f45b9e04feca9bc15ad7bf370d9d302f18f81d33cf70f97526c28d85",
            namespace="ai",
            method="blackboard_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.blackboard.schema.apply",
            binding_hash="sha256:864eeeb753d70b253acf8d262313eed93339f1165ef89d77324e37bb9f2928b5",
            namespace="ai",
            method="blackboard_schema_apply",
            parameters=(
                CommandParameterBinding(
                    name="entries",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.eqs.asset.create",
            binding_hash="sha256:3b56aa6fca152aeb07d17d45f7b1d4efcf5c7fbf904dcd25d6e890252645df2f",
            namespace="ai",
            method="eqs_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.eqs.graph.apply",
            binding_hash="sha256:875cf8ada7d8c90a0055ec826369d05b63b76687e6b5ebe21c954b45ffe52ee3",
            namespace="ai",
            method="eqs_graph_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.smart_object_definition.apply",
            binding_hash="sha256:d6c40ac2fa8de9c9be1edf2443bec9e2be40baa0504db61340ef94c9e5b74e8e",
            namespace="ai",
            method="smart_object_definition_apply",
            parameters=(
                CommandParameterBinding(
                    name="slots",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.smart_object_definition.asset.create",
            binding_hash="sha256:751365a5b1ce523eb91d766f92d03a7384894b8114de6b963741b86cfe3e0480",
            namespace="ai",
            method="smart_object_definition_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.state_tree.asset.create",
            binding_hash="sha256:68adf861ce29c4233f03b55091cb6feb5fb65df54f059c297deb57904287b177",
            namespace="ai",
            method="state_tree_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.state_tree.hierarchy.apply",
            binding_hash="sha256:807bf1983262dc3d9a26f8ebbaabeb1f74aafedcc06b38564985d2165753d5e7",
            namespace="ai",
            method="state_tree_hierarchy_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.anim_blueprint.asset.create",
            binding_hash="sha256:c8974c8f060d80294075708465dc6cefac179a984d38619affa1e91b157d7d46",
            namespace="animation",
            method="anim_blueprint_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parent_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="skeleton_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.anim_blueprint.graph.apply",
            binding_hash="sha256:85eb916b381192bfb2e5a959005806218abb1971e55ae3304d3932c520e5f805",
            namespace="animation",
            method="anim_blueprint_graph_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.anim_blueprint.layer_interface.asset.create",
            binding_hash="sha256:6c160335935c80615825e4481f32ab0c4fa9366a7e9b19c1e328ccf1000d7c4f",
            namespace="animation",
            method="anim_blueprint_layer_interface_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.blend_space.asset.create",
            binding_hash="sha256:916a6e16b925db78ae0150d73b31f7c451dd6b418dc31ded11ea0c2e1d34d486",
            namespace="animation",
            method="blend_space_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="dimension",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="skeleton_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.blend_space.definition.apply",
            binding_hash="sha256:8a39be59e094b012c8f7f89a781c74e9066597ac20b70a345d317d532544bb9f",
            namespace="animation",
            method="blend_space_definition_apply",
            parameters=(
                CommandParameterBinding(
                    name="axes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="samples",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.blend_space.sample",
            binding_hash="sha256:fc91a1b122a80fb031132d7a9a4388a2bea56eb6639ad8a16f19f559c827b990",
            namespace="animation",
            method="blend_space_sample",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.control_rig.asset.create",
            binding_hash="sha256:59c642c70af404d1c0f0869c2358d8522d09f4b3b292ecb9a1b0abb511abaa37",
            namespace="animation",
            method="control_rig_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="skeleton_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.control_rig.hierarchy_graph.apply",
            binding_hash="sha256:6c10480aff7a96a332f6346bd124743aa1ba4bd9a44dfb689faa5bcfc44f623b",
            namespace="animation",
            method="control_rig_hierarchy_graph_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.control_rig.shape_library.apply",
            binding_hash="sha256:79c26d76e18a08f63076d1ceb94625ff659bbf6d5cdcad864773819ee0f83bd0",
            namespace="animation",
            method="control_rig_shape_library_apply",
            parameters=(
                CommandParameterBinding(
                    name="shapes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.control_rig.shape_library.asset.create",
            binding_hash="sha256:059197e74fddce438939b0700d463f56eef7b3b11624ce52287ca437eb47c973",
            namespace="animation",
            method="control_rig_shape_library_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.deformer_graph.asset.create",
            binding_hash="sha256:eeec1c1a86fae195531ba3c62b03b9cc588c0c00d60901cdf50e80da627f2623",
            namespace="animation",
            method="deformer_graph_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="skeletal_mesh_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.deformer_graph.topology.apply",
            binding_hash="sha256:ad902a0f03ba07cdc9d19124856d122cda2b70471a079a9ceda006ac8fe2f8dc",
            namespace="animation",
            method="deformer_graph_topology_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.deformer_source_library.asset.create",
            binding_hash="sha256:4854bae54a5f454cf2751d90cb011d2084e2ac691e1e1a862e4ab2f8cd71d775",
            namespace="animation",
            method="deformer_source_library_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="concrete_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.deformer_source_library.bindings.apply",
            binding_hash="sha256:d1884af169c064ab0d87d349ff26d361fbea23243c850c56947fc66f00767a6e",
            namespace="animation",
            method="deformer_source_library_bindings_apply",
            parameters=(
                CommandParameterBinding(
                    name="bindings",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="concrete_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ik_probe_candidate.apply",
            binding_hash="sha256:5cf7aa1bfd9c717527df93c06106d675a4d27700c1e38db38de59a3dc9c37274",
            namespace="animation",
            method="ik_probe_candidate_apply",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ik_retargeter.asset.create",
            binding_hash="sha256:4c3955ab392d7de95b64550f57315e8f334e4e8ed366edfcb3aabdb43fc37b37",
            namespace="animation",
            method="ik_retargeter_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="source_ik_rig_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ik_rig_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ik_retargeter.definition.apply",
            binding_hash="sha256:5dc06209103258c3fb63971540bd370057815abb846aa4d5ab3256a8dc447f05",
            namespace="animation",
            method="ik_retargeter_definition_apply",
            parameters=(
                CommandParameterBinding(
                    name="chain_mappings",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="source_ik_rig_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ik_rig_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ik_retargeter.settings.apply",
            binding_hash="sha256:ca527ec9be42d53b4ffca8454a81d2810e77ccfe8db170bdf9ff2743d20bf6a0",
            namespace="animation",
            method="ik_retargeter_settings_apply",
            parameters=(
                CommandParameterBinding(
                    name="settings",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ik_rig.asset.create",
            binding_hash="sha256:4e12fd35d0493d1575d6ae23bf270223dd77673f9c8c6ed88e48995475a38a58",
            namespace="animation",
            method="ik_rig_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="skeletal_mesh_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ik_rig.definition.apply",
            binding_hash="sha256:c0b12178294eb6cb2145ac0755b6310fd1d6645469109cbeb0c713bf9d3eaf44",
            namespace="animation",
            method="ik_rig_definition_apply",
            parameters=(
                CommandParameterBinding(
                    name="chains",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="goals",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="retarget_root",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="solvers",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ik_rig.definition.auto_generate",
            binding_hash="sha256:8a343c2cf30fefff621114548d30495b52ad1fdc91e07c028520b576ded07c57",
            namespace="animation",
            method="ik_rig_definition_auto_generate",
            parameters=(
                CommandParameterBinding(
                    name="preset",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="skeletal_mesh_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.mesh_deformer_collection.asset.create",
            binding_hash="sha256:8c165c49277d4265a79841134301894436c65514749925c2a2a3150d83d41ca8",
            namespace="animation",
            method="mesh_deformer_collection_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.mesh_deformer_collection.entries.apply",
            binding_hash="sha256:7d13093a5a38f3e93c93d322add23d3c5c0f2dc08aee21236f44e9727473441b",
            namespace="animation",
            method="mesh_deformer_collection_entries_apply",
            parameters=(
                CommandParameterBinding(
                    name="entries",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ml_deformer.asset.create",
            binding_hash="sha256:e65ef13d0572d867cb8d788672430f6e794476e09afe61af484b5f863a1b7889",
            namespace="animation",
            method="ml_deformer_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="model_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ml_deformer.configuration.apply",
            binding_hash="sha256:97150bc9c252906bac65cdba2a5ec5c809b5f974ea177937a4c9fd1d208c77e1",
            namespace="animation",
            method="ml_deformer_configuration_apply",
            parameters=(
                CommandParameterBinding(
                    name="animation_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="concrete_model_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="deformer_graph_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="skeletal_mesh_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_geometry_cache_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.montage.create",
            binding_hash="sha256:e2ffe694f5bcfc2cc2d54921016b6069e0aa32e15367b5313610f6e48f22ace0",
            namespace="animation",
            method="montage_create",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.montage.read",
            binding_hash="sha256:fabaf78664287eb14822eb8d2bf62887f220593872c6389908c7e659e25f393e",
            namespace="animation",
            method="montage_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.montage.structure.replace",
            binding_hash="sha256:3126e484fc212665ff46f95ba47ff0ce937b70d3c945afc2d75fafd0bebaba9e",
            namespace="animation",
            method="montage_structure_replace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.sequence.bone_tracks.replace",
            binding_hash="sha256:64e63cc4080c4770e531742a7a3528ef96f0a96e19c631ad556f6161129c5918",
            namespace="animation",
            method="sequence_bone_tracks_replace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.sequence.curves.update",
            binding_hash="sha256:ac0cc40eeb2d58a42155349932ecad70af353c1971c30bc497fc98d1ac0c99a1",
            namespace="animation",
            method="sequence_curves_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.sequence.events.update",
            binding_hash="sha256:d1f4cec3930da9d51e083518f08fcfb347573d4d2a8becd6d2a9d4cdeb3c69b5",
            namespace="animation",
            method="sequence_events_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.sequence.metadata.update",
            binding_hash="sha256:a77bf68e7d629bce610703d0f66bf14fef99975da00749571840cbb5ecda71eb",
            namespace="animation",
            method="sequence_metadata_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.sequence.pose.sample",
            binding_hash="sha256:99011555fd6bdb739e75cef2796667f1bdfc37ddb8702fb3a7ad8085e26891f4",
            namespace="animation",
            method="sequence_pose_sample",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.sequence.read",
            binding_hash="sha256:8f02a0e0f528c34bf8ab07201b588576fd38aa293038515dd2c8396d45974c64",
            namespace="animation",
            method="sequence_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.sequence.root_motion.analyze",
            binding_hash="sha256:7aa49e6725b1cc42aa61df7cd04616aa8290d4be763283c2ad10ed28eaccab51",
            namespace="animation",
            method="sequence_root_motion_analyze",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.skeleton.compatibility.apply",
            binding_hash="sha256:4ac5a6d77b9cdc17a0cdc533d87b75a60ddb465e9bdedc9462b693ec8a0ecf16",
            namespace="animation",
            method="skeleton_compatibility_apply",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.skeleton.definition.apply",
            binding_hash="sha256:69d2d60168c9c1285731c6f99479b46c47d000e4ada0788a8ef027ff5e7241b5",
            namespace="animation",
            method="skeleton_definition_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.skeleton.slots.read",
            binding_hash="sha256:b45df2a63aa4705eaf8c15a760c9febe957738c8b6fa27e8fa619e5ef238a513",
            namespace="animation",
            method="skeleton_slots_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.skeleton.virtual_bone.apply",
            binding_hash="sha256:4c795b641f0076de17c7da17179594719ba52d8485822e835b0fcb13355ddd69",
            namespace="animation",
            method="skeleton_virtual_bone_apply",
            parameters=(
                CommandParameterBinding(
                    name="intent",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="source_bone",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_bone",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.state_machine.candidates",
            binding_hash="sha256:ec17e0886395b5b7fd95e6749f0111d6f92a26e247dfe25c8d2444883def5ea2",
            namespace="animation",
            method="state_machine_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="surface",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="class_settings",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.subject.morph_weights.update",
            binding_hash="sha256:6ddc2835c2a4edfc74e23c0a96437ec8e76ed3b5d25bd96b1feccc2a886cd9fa",
            namespace="animation",
            method="subject_morph_weights_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.subject.pose.update",
            binding_hash="sha256:fc19a453d13d2522db089d48c7fec50d203ffd042c02e849d6c2155f26a86d51",
            namespace="animation",
            method="subject_pose_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation_rig_graph.candidates",
            binding_hash="sha256:54fef1513c22bc5ae060937474db0ff1eeb19ebc1773e5b52fb396c45370c018",
            namespace="animation_rig_graph",
            method="candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.audio_effect_preset.create",
            binding_hash="sha256:a21f0a2875bba4ad7bfa3c23ec9deb489b70eeef4efc431548194803872721fe",
            namespace="asset",
            method="audio_effect_preset_create",
            parameters=(
                CommandParameterBinding(
                    name="factory_ref",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.audio_effect_preset.update",
            binding_hash="sha256:f1009a81eedc35fc4135e66c002d0e914001850945dc0cbd42371408737c2f68",
            namespace="asset",
            method="audio_effect_preset_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.collection",
            binding_hash="sha256:3157b05ee9eb5c41cd62a8607717d8db649d0dabfd5d77534aba88e0730dea20",
            namespace="asset",
            method="collection",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.curve.update",
            binding_hash="sha256:5f5a757788c489c3ee0c9163668006763df80e8b9518bac9be5ce0d03bb7ffa5",
            namespace="asset",
            method="curve_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.data_layer.create",
            binding_hash="sha256:b3f4e15b58cb1c7ee8b7096b585ae8f0fc683f2ec0523c6d40f7136726380cc8",
            namespace="asset",
            method="data_layer_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.data_object.create",
            binding_hash="sha256:5282a9d3b6b0cb371aa97457765229e1e48745a65892335c38929c5fbfd56a00",
            namespace="asset",
            method="data_object_create",
            parameters=(
                CommandParameterBinding(
                    name="factory_ref",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.data_object.update",
            binding_hash="sha256:4cf302291e27dd3ee7e13c7e454545e3fcb2710f160440d617de8516c638c05f",
            namespace="asset",
            method="data_object_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.data_table.replace",
            binding_hash="sha256:d1c1c1cb38aac797fb08e350c494f0119c80ed43bd70b334c143a07bbb1d6a04",
            namespace="asset",
            method="data_table_replace",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.delete",
            binding_hash="sha256:ec6632a71d7fc39fd28dec02d7a586d4d3b1f5cede587f8c339e0cec9109684a",
            namespace="asset",
            method="delete",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.factory.candidates",
            binding_hash="sha256:1ebd825f576154de4db84262888a37f191f6e4f06d1c8e780f42de6e37d34cd6",
            namespace="asset",
            method="factory_candidates",
            parameters=(
                CommandParameterBinding(
                    name="create_command",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.fixup_redirectors",
            binding_hash="sha256:64150e2c4b7d3193ad1292eac22da03012a0a5be2b6025d4974a314d1551c733",
            namespace="asset",
            method="fixup_redirectors",
            parameters=(
                CommandParameterBinding(
                    name="root_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.input_action.create",
            binding_hash="sha256:fec4ac02ea58b128884766e21fc76932fccedd8830eb274008634db428f76ab6",
            namespace="asset",
            method="input_action_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.input_action.update",
            binding_hash="sha256:e766a5049b4cda19a11460f651a88dfbd8794762ccb36b7bc206425abc9f536c",
            namespace="asset",
            method="input_action_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.input_mapping_context.create",
            binding_hash="sha256:8a08ec649fafa9200c4241e15a4cd70ad27e03f2cf50a1663709bc0862e8fd7e",
            namespace="asset",
            method="input_mapping_context_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.input_mapping_context.update",
            binding_hash="sha256:235f3a4935b0f1c6c98114c6e202c1e5328fa61d0fca840bf482bde7115434dd",
            namespace="asset",
            method="input_mapping_context_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.media_player.create",
            binding_hash="sha256:662bf0c90404d4af46cb9524daca35b5f1ba155e7178deba697850ec619d3e27",
            namespace="asset",
            method="media_player_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.media_player.update",
            binding_hash="sha256:86d1d0d3ad56000c701b078718b34cc54f4692ab8d5ab4964df54043d5f4a111",
            namespace="asset",
            method="media_player_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.media_source.create",
            binding_hash="sha256:f8b8248bb22ba445e163f8775b389b09d8101da8e4228b3f9cabc33922d2aba4",
            namespace="asset",
            method="media_source_create",
            parameters=(
                CommandParameterBinding(
                    name="factory_ref",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.media_source.update",
            binding_hash="sha256:cb3abaca5ad535e0097f1710e787953550ff2a29f39f656a6accfd2a5347cf5e",
            namespace="asset",
            method="media_source_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.media_texture.create",
            binding_hash="sha256:ce366ac9190090b484bae8d17af3c64488f0a914b06ef04635e8bb9029ab1f4b",
            namespace="asset",
            method="media_texture_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.media_texture.update",
            binding_hash="sha256:9e5cdfc7290dcbd405810f0723512b57f718bd1bc99d005a6eedcd4c32ff0289",
            namespace="asset",
            method="media_texture_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.move",
            binding_hash="sha256:50e4d50f182c73fd24cb05d0a4863b395231e84e2a1c19c22269e6e3dc1b29ad",
            namespace="asset",
            method="move",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destination_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.object.clone",
            binding_hash="sha256:62becf16ff4ae99f07a7868ea59d9bc37ea50a9a80279ff2c700369f39a35968",
            namespace="asset",
            method="object_clone",
            parameters=(
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_source_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.paper_flipbook.create",
            binding_hash="sha256:8a5a76829a55e920afc576dffa27fc86802e631319595e69196586f534e94f46",
            namespace="asset",
            method="paper_flipbook_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.paper_flipbook.update",
            binding_hash="sha256:3255c29382211dceaecffa5fd0ab733f155fc6708286df9517bc2c3fc2a82d96",
            namespace="asset",
            method="paper_flipbook_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.paper_sprite.create",
            binding_hash="sha256:544b74b3e0adecba2b658ad2619aaa3acab1a05f35f9c1f78c66ff35b731dbd4",
            namespace="asset",
            method="paper_sprite_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.paper_sprite.update",
            binding_hash="sha256:a95780bb25f1a96078e8cdeec6e1b4e869e73ddc3b27af81bbe31dad9a5d51be",
            namespace="asset",
            method="paper_sprite_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.paper_tilemap.update",
            binding_hash="sha256:38cb488d5ffa931d00896615da53278e059ca9fd3400881e6dc5abc9eb1c00ec",
            namespace="asset",
            method="paper_tilemap_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.paper_tileset.update",
            binding_hash="sha256:91322319b971d1bd1d70a1e8379f0e5bb53f357118e8c954479d58c277dfc8b0",
            namespace="asset",
            method="paper_tileset_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.properties",
            binding_hash="sha256:30f10d97a4e7637b355f668761eb037101285f7cfa863bc4caf64e255bf38fbd",
            namespace="asset",
            method="properties",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.registry_record",
            binding_hash="sha256:657a069073f0886d9075e0c71f9cf719da9e721ad7ae956efe169a0d61e8667e",
            namespace="asset",
            method="registry_record",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.registry_relations",
            binding_hash="sha256:a193b8fc3a9541910eebacd0289e51bf106e49847399d58c95f192b59f870075",
            namespace="asset",
            method="registry_relations",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.reimport_sound_wave",
            binding_hash="sha256:48844aa170106aed831d2354331d433dcb2f63a2d0f4f567d6b801045a05ce31",
            namespace="asset",
            method="reimport_sound_wave",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.reimport_sparse_volume_texture",
            binding_hash="sha256:47725d0f1f9256af8ac4f1d8c00c13eaca85a35abd54ca69db7f67b22a991d65",
            namespace="asset",
            method="reimport_sparse_volume_texture",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.reimport_static_mesh",
            binding_hash="sha256:4ebb44fae0ca4668d7410555d27671d5a4947c49b89f780c38d7c4d05bd6d86d",
            namespace="asset",
            method="reimport_static_mesh",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.reimport_texture",
            binding_hash="sha256:42b8e3ef9e4e424d1078d694925d8f3af04754bb976847dade913c601c1d7101",
            namespace="asset",
            method="reimport_texture",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.relations",
            binding_hash="sha256:555b9829c31fad5b642c8fb64bdac68a0abeec4161d9d8dae5ec1553962ae043",
            namespace="asset",
            method="relations",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.render_target.create",
            binding_hash="sha256:239a7a8fbd0f127778de0c49f7ba7b98dca72034ec4d1ab4e8760eb2dd9f350a",
            namespace="asset",
            method="render_target_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.render_target.update",
            binding_hash="sha256:66862b39070dcbfff70a03bfc9b1eb016b54ff58d23aa1aa5b2ca1d25fac761d",
            namespace="asset",
            method="render_target_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.runtime_virtual_texture.create",
            binding_hash="sha256:9a7582222dc9c5b81d366d024b431e613cf9d461135f3d344696d6fe02a5038d",
            namespace="asset",
            method="runtime_virtual_texture_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.runtime_virtual_texture.update",
            binding_hash="sha256:3646b3543c715e9551867bd5822eb053126430e664b70513c46b5e3908e0f20a",
            namespace="asset",
            method="runtime_virtual_texture_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sample",
            binding_hash="sha256:94b4a6485f63b0e0e6c5ffa2ab8946a0cad56c7d214f8db67927eb602e6b3a10",
            namespace="asset",
            method="sample",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.skeletal_mesh.update",
            binding_hash="sha256:51272bbbbe60c05c49f978d2e342bc5bbd4a49846d5a9da8ed38d24605731688",
            namespace="asset",
            method="skeletal_mesh_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sound_attenuation.create",
            binding_hash="sha256:43fe77940d759faea8710526575f06c38a0bdb71f97ef023abda0ecd92509db6",
            namespace="asset",
            method="sound_attenuation_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sound_attenuation.update",
            binding_hash="sha256:7eb74b5f1b4eeca8363f04f8174a07e7f872e0f27bd3ecc0453a753679a30227",
            namespace="asset",
            method="sound_attenuation_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sound_class.create",
            binding_hash="sha256:87cf6585bcafc3374eda4af53f2c8d7bbe6ac4e93824aed42894df01c66923a4",
            namespace="asset",
            method="sound_class_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sound_class.update",
            binding_hash="sha256:f1c4c31be49545fa0c2b188635f7c746ef86594a81d3b248ebb5e0ed808783ff",
            namespace="asset",
            method="sound_class_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sound_concurrency.create",
            binding_hash="sha256:15d4c9beb18416cd98419566d8faf615b6bde1fdfcc9d1b760d6c7ece36365e6",
            namespace="asset",
            method="sound_concurrency_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sound_concurrency.update",
            binding_hash="sha256:e17c31de50e08ca3c870031699d9f3625ac989d98e60b8dcb8acd05c24b27ddf",
            namespace="asset",
            method="sound_concurrency_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sound_mix.create",
            binding_hash="sha256:a4a8594616de9c7a224eb96fa1cf1f889d86390ce1f81c7e1e005400e84783f2",
            namespace="asset",
            method="sound_mix_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sound_mix.update",
            binding_hash="sha256:56f63cb2bbed69fdacb7c4e614ac8f7f02deca2c69d29718d87628f2ddff0794",
            namespace="asset",
            method="sound_mix_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sound_submix.create",
            binding_hash="sha256:27820c78a77c0af04e71db573b58cbf6095ad527f84db37af3f2ebc6770b40d6",
            namespace="asset",
            method="sound_submix_create",
            parameters=(
                CommandParameterBinding(
                    name="factory_ref",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sound_submix.update",
            binding_hash="sha256:430bb1562e93800c2636cee6aac53c4e67875f9499f1f9707c2a295332d38ad5",
            namespace="asset",
            method="sound_submix_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.sparse_volume_texture.update",
            binding_hash="sha256:c184fe0ac2f74d56f0646b2ab39def0458a3280fc23d8f397cbf2a6c1db654d7",
            namespace="asset",
            method="sparse_volume_texture_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.static_mesh.update",
            binding_hash="sha256:d8e7fc5d3e7ff697f94629d184b407a6eddbfd4b461c26e7215cbd724a08743b",
            namespace="asset",
            method="static_mesh_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.subuv_animation.create",
            binding_hash="sha256:5725b59b5ef964865bf728013492029fe4576f19cd336c3f32fc9249e0ef10b4",
            namespace="asset",
            method="subuv_animation_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.subuv_animation.update",
            binding_hash="sha256:4d07b81f0d3700c19c1feffc799c70e8db3f12f4387c8d6fb87b068af66f2087",
            namespace="asset",
            method="subuv_animation_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.summary",
            binding_hash="sha256:5b1b53ac8accbc593d1df51f57815ae7111c7eeffc2ed10aaff30c46dd160be3",
            namespace="asset",
            method="summary",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.texture_array.create",
            binding_hash="sha256:7cca87014014264759471c10c57851a2b2c079033604a2d22bfc2d7f3c2a5ca2",
            namespace="asset",
            method="texture_array_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.texture_array.replace",
            binding_hash="sha256:d508e87e00a34632f42b4049780a9ec4d8156ea0b48e523428b998eb399ed8f6",
            namespace="asset",
            method="texture_array_replace",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.texture_collection.create",
            binding_hash="sha256:c13f327ae0ed97b9c811ea1fcc4671412214fe0baa5c0f3e82b10eadd4ce8d04",
            namespace="asset",
            method="texture_collection_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.texture_collection.update",
            binding_hash="sha256:284a63e2789cd8b8f2bb16b0b447cdab0332825a203bbdb2ed4efe1d2fcbf964",
            namespace="asset",
            method="texture_collection_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.texture_cube.create",
            binding_hash="sha256:967378643c26e53fe81b9f58db4610b9f43b395ef1d5b7c7971e26604bbfad92",
            namespace="asset",
            method="texture_cube_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.texture_cube.replace",
            binding_hash="sha256:0f85d329074bdf2fbe6b66c58d7f6ee787dc42e1ae03c70cdb6a30bde18357b1",
            namespace="asset",
            method="texture_cube_replace",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.texture_cube_array.create",
            binding_hash="sha256:e6f708da1e710d8f427ea4ad468ef5613d1b51299d33c3cdffd9e0d5c8cdad97",
            namespace="asset",
            method="texture_cube_array_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.texture_cube_array.replace",
            binding_hash="sha256:a29a7b12a94cfd6b0f5f4cade7d55b3ab68444fce8e22c860a87730d232341ad",
            namespace="asset",
            method="texture_cube_array_replace",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.validation",
            binding_hash="sha256:845c80cba1a4966aa53287e652f9ba6f25d1a61d0aa6163a885f9810c116c21d",
            namespace="asset",
            method="validation",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.volume_texture.create",
            binding_hash="sha256:786ab9e8c80ea883a660ad2d553bffd17b382d08f7564234027b58c075acb60c",
            namespace="asset",
            method="volume_texture_create",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.volume_texture.replace",
            binding_hash="sha256:5f085ed85c9ac0240a3ae44d72db069afb33e9f69477308a12072ccdbe9be4ca",
            namespace="asset",
            method="volume_texture_replace",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset_durable.journal.read",
            binding_hash="sha256:e2f54b7d5c49a2ca2a001317d2ded7e20e280d02d578353a11c6d73757b5e72d",
            namespace="asset_durable",
            method="journal_read",
            parameters=(
                CommandParameterBinding(
                    name="journal_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset_durable.journal.reconcile",
            binding_hash="sha256:98aa59ac187978dc6c65e3a6df3fb5d066b20309b6d7d121fafee2db26ccbb9e",
            namespace="asset_durable",
            method="journal_reconcile",
            parameters=(
                CommandParameterBinding(
                    name="journal_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_journal_owner_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_fencing_token",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="verification_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="audio.graph.candidates",
            binding_hash="sha256:0b84a5beaf8866f067b1104b60dd7606208d584c3f6ce2246b4e947ad14fb7b1",
            namespace="audio",
            method="graph_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="audio_media.asset.create",
            binding_hash="sha256:3c8d9ef2aa5d989be4bad7e25238b6de4a9ba01884cbfb4334928498a7197e7b",
            namespace="audio_media",
            method="asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_kind",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="blueprint.asset.create",
            binding_hash="sha256:bcc989441be9818f49e9da0cdd40ee3f4b0c4c724d6068eab2beff2061dea256",
            namespace="blueprint",
            method="asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parent_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="blueprint.component.candidates",
            binding_hash="sha256:e57d646ac260ac6797a394eaa51f14835a62d9c32c608f997fca9187483e7cbc",
            namespace="blueprint",
            method="component_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parent",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="blueprint.component.events.discover",
            binding_hash="sha256:f042875c127cb2cc07d965d9b0cde94e68136ae79b22de971c3b09b407b0600e",
            namespace="blueprint",
            method="component_events_discover",
            parameters=(
                CommandParameterBinding(
                    name="asset_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="compile_before_query",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="component_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="include_hidden",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="only_unbound",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="blueprint.node.candidates",
            binding_hash="sha256:81331916cf83c71a8c75f98f1adce8691ca8c15f298be70bdf6eae15af4b8115",
            namespace="blueprint",
            method="node_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="graph_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="node_guid",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="pin_guid",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="pin_name",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="capture.image.execute",
            binding_hash="sha256:72a6ba207b479413291cd5395930f138fbb8864cb6ef179af0b31513054d1469",
            namespace="capture",
            method="image_execute",
            parameters=(
                CommandParameterBinding(
                    name="subject_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="policy_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parameters",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="capture.media.execute",
            binding_hash="sha256:4d17277ffb6001615d6a6d9cd2fe232f0cc6a383b9b1b24a0c38f8d308f86782",
            namespace="capture",
            method="media_execute",
            parameters=(
                CommandParameterBinding(
                    name="subject_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="policy_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parameters",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="capture.render.execute",
            binding_hash="sha256:bbecf32cb504fbec6ba8bc068026c9e5cf2c19220c8d186eacdca0660fbd58e5",
            namespace="capture",
            method="render_execute",
            parameters=(
                CommandParameterBinding(
                    name="subject_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="policy_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parameters",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="config.resolved_value",
            binding_hash="sha256:78079f50cfbd9b67c0538daae337a4e92cbef60c34777350750cd18e265c61c9",
            namespace="config",
            method="resolved_value",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="config.section",
            binding_hash="sha256:90841c87e995e6a3a01e333a00ae6c7606802837c300bc582976c8bb40e9cd62",
            namespace="config",
            method="section",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.authoring_schema",
            binding_hash="sha256:b35f922464eadb8c510d04bb3e36dca809361054972a595a03f7e700e375f32a",
            namespace="content_graph",
            method="authoring_schema",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.compound",
            binding_hash="sha256:8b3b285a29deac307f658285b43c77ffb9d15045725d2cf10566bf751a552fbe",
            namespace="content_graph",
            method="compound",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.diagnostics",
            binding_hash="sha256:83aab79207e515bd348ba6457abbfe989663d86a68db03316678a55ffe7d119d",
            namespace="content_graph",
            method="diagnostics",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.export_workspace",
            binding_hash="sha256:2a70bbdde96152b8a02f6319e1f3d5aecad316da172a05417d1c3a5a37c8134a",
            namespace="content_graph",
            method="export_workspace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="workspace_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="profile_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.import_workspace",
            binding_hash="sha256:1977b5bc60f6bba75cdc69f2543c0985684c3cd83b2f9adcec31aacf52b5621f",
            namespace="content_graph",
            method="import_workspace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="source",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="authorization_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limits",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.items",
            binding_hash="sha256:4e51c350b0ba6d844fc67d87fe55a6a30d9bcee3c389c3b4750f8748ee6f8c27",
            namespace="content_graph",
            method="items",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.properties",
            binding_hash="sha256:b00919c210e87d481c78f487ff523ef5ec9147d233e5255ca2810ab8ff9eef0b",
            namespace="content_graph",
            method="properties",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.relations",
            binding_hash="sha256:598b0ff2d85007ef0ac956b5202b031cead3bd73c08b7cd97e8565498efa34f3",
            namespace="content_graph",
            method="relations",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.structure",
            binding_hash="sha256:4caeb02b3910f6dc9374bb8c7dc169cf6a74c18ab0bd9b79cf300bee8df597fc",
            namespace="content_graph",
            method="structure",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.summary",
            binding_hash="sha256:2a2ec5f3c9253f221c395644076fdce54b65d227a39b93e9d23bc8b33ce58700",
            namespace="content_graph",
            method="summary",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="deformer.evaluation.sample",
            binding_hash="sha256:20b45af88a92fc133a0cb51be7c0f9834118145134bc7205581fc19e486f2aeb",
            namespace="deformer",
            method="evaluation_sample",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="deformer.geometry.sample",
            binding_hash="sha256:1e468c267eedf342c2351b62737c2fbd0806d20001fbfc15a0f61aae2aff167b",
            namespace="deformer",
            method="geometry_sample",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="deformer.training_inputs.validate",
            binding_hash="sha256:b6a24997c0b08b04ad83cd7fb8a28b1ddec537f74e259b4e1bab1cec8add6ecc",
            namespace="deformer",
            method="training_inputs_validate",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor.dirty_resources",
            binding_hash="sha256:c58253d6cc742d78e53c878b15cd6f887328e4b5a87708ef7569b226024c7cbb",
            namespace="editor",
            method="dirty_resources",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor.open_assets",
            binding_hash="sha256:bf45a9cf9cc001291fd4d6aba1028e3124b617e934a50d745db0cf7503a93aa7",
            namespace="editor",
            method="open_assets",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor.safe_exit",
            binding_hash="sha256:0e4315974a86be813b2cefd4b3559e635c744266239abb1fdf4579ab087934a6",
            namespace="editor",
            method="safe_exit",
            parameters=(
                CommandParameterBinding(
                    name="dirty_resolution",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="external_witness",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor.session",
            binding_hash="sha256:5901187b24e0acd44a9d14277a2920eec8c39e3ecb5e2db4071043c41125f9dd",
            namespace="editor",
            method="session",
            parameters=(
                CommandParameterBinding(
                    name="family_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="subject_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="policy_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parameters",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.config_section.update",
            binding_hash="sha256:4a9737a256981aedd5f84533c52e44db658643116556db1fe236793d44043140",
            namespace="editor_project",
            method="config_section_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.device_profile.update",
            binding_hash="sha256:5a3d734837a15125c97b59b8ee8f4ef8cdeb067e744ade2b18709bb2f7f519c1",
            namespace="editor_project",
            method="device_profile_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.localization_target.update",
            binding_hash="sha256:e20ad8d37ad079b433b93f1b997b3b6fdb401dc451e5d66bfc0b0a7995008439",
            namespace="editor_project",
            method="localization_target_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.platform_config.update",
            binding_hash="sha256:8ffa0708dd2cc0ee43f823de11a5d9b51e293852335d4507b4be23fed723d31e",
            namespace="editor_project",
            method="platform_config_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.project_settings.update",
            binding_hash="sha256:001e57cd02c66b3b8c004269c46c5d4027b31bdd21fb67a4e83f19f318adadbf",
            namespace="editor_project",
            method="project_settings_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.scalability_group.update",
            binding_hash="sha256:c3b809ff2933d31a7a4546de805a49740af7c94abdd9351cee6f9f49efd36cc2",
            namespace="editor_project",
            method="scalability_group_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.string_table.update",
            binding_hash="sha256:22763f3c68633cc059546d950c37fa31f7ab93d09e0763aa36638b0463548610",
            namespace="editor_project",
            method="string_table_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="external.fbx.animation.import",
            binding_hash="sha256:f3520ce942a9ab2a700c79d34c96dde4d58baa61567794fc27bcd22ed6fb7579",
            namespace="external",
            method="fbx_animation_import",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destination_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="skeleton_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="external.fbx.skeletal_mesh.import",
            binding_hash="sha256:663d08901ef8994652d6f8c152bf4a0c1eda008a32f03aacab52a2e6e5d662c9",
            namespace="external",
            method="fbx_skeletal_mesh_import",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destination_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="external.geometry_cache.import",
            binding_hash="sha256:3e1592d119f3bf2298e8e8b7b9d6d1509d9d60acd154dded687384ece751daa6",
            namespace="external",
            method="geometry_cache_import",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destination_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="external.light_profile.import",
            binding_hash="sha256:ca2b98f22fdaa928f6a059250a150c28cd96d2dfbfda3e0a66aeb477e015f2d2",
            namespace="external",
            method="light_profile_import",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destination_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="external.localization.po.import",
            binding_hash="sha256:a447447374de98871b9bb2722403cfb3322630a4d13b6f3cbf10f66a25f63e6a",
            namespace="external",
            method="localization_po_import",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="external.skin_weight_profile.import",
            binding_hash="sha256:3aa8558812f87d6f4a2983919573e46ef9714cbcfe665b3264d4c7a9461bb676",
            namespace="external",
            method="skin_weight_profile_import",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="profile_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="lod_index",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="external.sound_wave.import",
            binding_hash="sha256:46d9a157f8dc2786fc2a42cde0bf244fe9c00223e8a3eadbf1c211072e8b38a2",
            namespace="external",
            method="sound_wave_import",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destination_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="external.sparse_volume_texture.import",
            binding_hash="sha256:582f11dcfbcd5a62a6a83f1ac7c78d0d3a5a461f15348dc60db95c3f75bc9188",
            namespace="external",
            method="sparse_volume_texture_import",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destination_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="external.texture.import",
            binding_hash="sha256:a2001449fb68555bf624b5e0df8b58e075e823925094cacc3f035f371120d165",
            namespace="external",
            method="texture_import",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destination_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="options",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="graph.layout.apply",
            binding_hash="sha256:eca4556d635315340705374d719b637287eed76ac90450990c9122cd75fcd8b3",
            namespace="graph",
            method="layout_apply",
            parameters=(
                CommandParameterBinding(
                    name="targets",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="strategy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parameters",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="authorization_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="graph.view.read",
            binding_hash="sha256:9d01a95f745d87178be58b499395ae7f21f8a6e9da82ed075e4d34872025c3ee",
            namespace="graph",
            method="view_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="graph.view.update",
            binding_hash="sha256:f05fe5b66772c8ce8b457a24a43e88f4132868aa77750250ca1c915e61bbc82c",
            namespace="graph",
            method="view_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="job.compile_build",
            binding_hash="sha256:533a90cd1de4ee2c42c1468c4e52e759d8ecd224fa864ec274e4f3ea9588c5e4",
            namespace="job",
            method="compile_build",
            parameters=(
                CommandParameterBinding(
                    name="family_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="subject_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="policy_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parameters",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="landscape.create",
            binding_hash="sha256:c228d88eb150be4ee3dead15fd110ce7315186846694453f866c7c05c5622858",
            namespace="landscape",
            method="create",
            parameters=(
                CommandParameterBinding(
                    name="initial_height",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="sample_region",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="topology",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="landscape.height.read",
            binding_hash="sha256:5d95851a03fbf05c75ca699076faf35b28a0f1d391f0103d3501781afa365965",
            namespace="landscape",
            method="height_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="landscape.height_delta",
            binding_hash="sha256:5a9d4646e6e8ae31020b7a5c1900364e919476bc5097d9d6e35cb04b47bd71da",
            namespace="landscape",
            method="height_delta",
            parameters=(
                CommandParameterBinding(
                    name="delta",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="region",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="material.asset.create",
            binding_hash="sha256:f4125bda2db562a123c9a3314690c3a9623494edbe7a2333cddab8e10c9852df",
            namespace="material",
            method="asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="material_kind",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="material.expression.candidates",
            binding_hash="sha256:bbaf25c3a6beb982228fcbd68f803c47f3ddccbebaaadf8bd4a8e2f03c34e638",
            namespace="material",
            method="expression_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="graph_name",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="node_guid",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="pin_guid",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="pin_name",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="material.function.graph.apply",
            binding_hash="sha256:56ab63aa3ce88e35686bb631d6216769bf77c4663de9f8f28b2289e84386481a",
            namespace="material",
            method="function_graph_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="material.graph.apply",
            binding_hash="sha256:df2794d6e2a6addb6ee46462fbb7c8b94088ff917212f43ea7e26a930d0a8620",
            namespace="material",
            method="graph_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="material_instance.asset.create",
            binding_hash="sha256:ab684c3a7bb10156c425bbcc4247632a75dd0f245d87a5f1d8532218a54de957",
            namespace="material_instance",
            method="asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parent_material_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="material_instance.parameters.apply",
            binding_hash="sha256:6137f8760eecd46ac2b3976340fd519a7ab6dfc2c141a4024f4aff2d31283eca",
            namespace="material_instance",
            method="parameters_apply",
            parameters=(
                CommandParameterBinding(
                    name="parameters",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.attribute.material_slot.add",
            binding_hash="sha256:c66dce35373bf98d908d4116bbd24875023950f89d59c96d89e329d67a9dc1df",
            namespace="mesh",
            method="attribute_material_slot_add",
            parameters=(
                CommandParameterBinding(
                    name="material_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="slot_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.attribute.material_slot.assign",
            binding_hash="sha256:f3fe7fe0ec4ff0c72c721bdec391f6787066c69fa89e78debff24a0766e3fa05",
            namespace="mesh",
            method="attribute_material_slot_assign",
            parameters=(
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="slot_index",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.attribute.normals.recompute",
            binding_hash="sha256:f00740aeb586fad12a3b0f8760f0fb3d8961eaf6fc516980fcb71f8ffe37297d",
            namespace="mesh",
            method="attribute_normals_recompute",
            parameters=(
                CommandParameterBinding(
                    name="angle_degrees",
                    wire_type="number",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="preserve_existing_hard_edges",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.attribute.uv.auto",
            binding_hash="sha256:a5cb648f37784f34b0c140c42a6026096e3cbb992bdf3363d2a74bf462be1da9",
            namespace="mesh",
            method="attribute_uv_auto",
            parameters=(
                CommandParameterBinding(
                    name="island_source",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="method",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="pack",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="texture_resolution",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="uv_channel",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.attribute.uv.project",
            binding_hash="sha256:e3fc37a7863558831b3ed19058b716a9d5a33c8ce2abdbc36fd17a18b1a782e3",
            namespace="mesh",
            method="attribute_uv_project",
            parameters=(
                CommandParameterBinding(
                    name="dimensions_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection_frame",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection_type",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="uv_channel",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.collision.convex.generate",
            binding_hash="sha256:c7442516be405d735a163942e9e1ef9315d9bb3d6e4e82ba66abbe9f4f0c47ec",
            namespace="mesh",
            method="collision_convex_generate",
            parameters=(
                CommandParameterBinding(
                    name="max_hulls",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="max_vertices_per_hull",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="replace_existing",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.collision.simple.generate",
            binding_hash="sha256:be32993a765b5f5d3195315206996a621e60603cac491f1c88cacd16515b5dcd",
            namespace="mesh",
            method="collision_simple_generate",
            parameters=(
                CommandParameterBinding(
                    name="max_shapes",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="method",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="replace_existing",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.element.select_by_ray",
            binding_hash="sha256:0bd8c3eee0bf372800daf717091c9d5b3194adeef9a2c2743ceb4321645ac4f4",
            namespace="mesh",
            method="element_select_by_ray",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.modeling_session",
            binding_hash="sha256:fc5d10c9c4635ac6a39ed9d358e1dc65865054a0b63331f2352e75323a937f96",
            namespace="mesh",
            method="modeling_session",
            parameters=(
                CommandParameterBinding(
                    name="action",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.pivot.update",
            binding_hash="sha256:06fa77e4a63328fdec08ec43fcf9b776051726ac4496ea05f9c42c15fec81d21",
            namespace="mesh",
            method="pivot_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.box.create",
            binding_hash="sha256:7de7494626edcef4106f5a1219f104db9edb65879d1c935780a20691fab6a2c9",
            namespace="mesh",
            method="primitive_box_create",
            parameters=(
                CommandParameterBinding(
                    name="anchor",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="size_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="subdivisions",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.cylinder.create",
            binding_hash="sha256:58cc6e24b3c63bc7f04fcbcd71890dec95cc833dc05fa2934e542e89265301d2",
            namespace="mesh",
            method="primitive_cylinder_create",
            parameters=(
                CommandParameterBinding(
                    name="anchor",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cap_ends",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="height_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="height_segments",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="radial_segments",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="radius_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.plane.create",
            binding_hash="sha256:b4555386d01691d0edef104e6c9ad0084a9876f6049ffb1f9ad699ecdd55ccb6",
            namespace="mesh",
            method="primitive_plane_create",
            parameters=(
                CommandParameterBinding(
                    name="double_sided",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="size_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="subdivisions",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.ramp.create",
            binding_hash="sha256:85c6cd38465476550ffd7b5bb8d9d5c415dbfc7daaa533f81476c2109ab7d09a",
            namespace="mesh",
            method="primitive_ramp_create",
            parameters=(
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="rise_direction",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="size_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="slope_axis",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.ramp_corner.create",
            binding_hash="sha256:2ed2f6c284241f37079a58445d04e5c9dfde8de48a64760324fa91a2ef1a7d08",
            namespace="mesh",
            method="primitive_ramp_corner_create",
            parameters=(
                CommandParameterBinding(
                    name="high_corner",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="size_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.sphere.create",
            binding_hash="sha256:9fc71e5b67b78cb30429df371de5f657132594d24fdb532ef5afadb5de1b0d8e",
            namespace="mesh",
            method="primitive_sphere_create",
            parameters=(
                CommandParameterBinding(
                    name="latitude_segments",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="longitude_segments",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="radius_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.stairs.create",
            binding_hash="sha256:7afa30d1c8773779d42b82adb70aba2d338cc9d63f038aff476e2f544e53cb1e",
            namespace="mesh",
            method="primitive_stairs_create",
            parameters=(
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="rise_axis",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="rise_direction",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="step_count",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="step_depth_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="step_height_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="step_width_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.boolean",
            binding_hash="sha256:97fa664aaa58721b8e33b6800e86852e32e2d608d49652a2347615dbb1ce18fa",
            namespace="mesh",
            method="topology_boolean",
            parameters=(
                CommandParameterBinding(
                    name="operand_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_to_target",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operation",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="simplify_output",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.edges.bevel",
            binding_hash="sha256:a779f1cc7f35589b797dea2c194139cb350a6a1b0018b01fd4ad7c00f43dd0cf",
            namespace="mesh",
            method="topology_edges_bevel",
            parameters=(
                CommandParameterBinding(
                    name="distance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="roundness",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="segments",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.edges.weld",
            binding_hash="sha256:d0c5ce5cfaf8802e09d6b01e4d5c57d274dc3aa3f9af09fc5bbd6621b21e470d",
            namespace="mesh",
            method="topology_edges_weld",
            parameters=(
                CommandParameterBinding(
                    name="edge_pairs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="tolerance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.faces.duplicate",
            binding_hash="sha256:4d598ac6b84ffa45aa3445e3c60cfd1dd54c5310836fdd7ff3711cdb5ecd8110",
            namespace="mesh",
            method="topology_faces_duplicate",
            parameters=(
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="translation_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.faces.extrude",
            binding_hash="sha256:5723e018d1059ae0b8782b3926c3afdd032feadd9cd1d4dc6f40564f81e956b7",
            namespace="mesh",
            method="topology_faces_extrude",
            parameters=(
                CommandParameterBinding(
                    name="direction",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="direction_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="distance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.faces.inset",
            binding_hash="sha256:57fef9b3fe05bd16764baeb1a5ef3d44b7ee0831e686315c7934c6e49d8d0ece",
            namespace="mesh",
            method="topology_faces_inset",
            parameters=(
                CommandParameterBinding(
                    name="boundary_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="distance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.faces.offset",
            binding_hash="sha256:f53bf18266aafb1d02a1e34c1c68e6cd7ab407476d5fe7dddd9704115af5c031",
            namespace="mesh",
            method="topology_faces_offset",
            parameters=(
                CommandParameterBinding(
                    name="distance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="offset_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.faces.push_pull",
            binding_hash="sha256:6622398284b9a658b80dce36cd4ddb6d048e4493d6f6d1a7efaaa77123f5da56",
            namespace="mesh",
            method="topology_faces_push_pull",
            parameters=(
                CommandParameterBinding(
                    name="direction",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="direction_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="distance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.holes.fill",
            binding_hash="sha256:2d32eaa0b4b5d51932cb2f9dee3a20e3430299a776398282836d36d00a3a6a76",
            namespace="mesh",
            method="topology_holes_fill",
            parameters=(
                CommandParameterBinding(
                    name="fill_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.mesh_cut",
            binding_hash="sha256:533f40eb9938dadd81680d9fb569ab2e5c24b17b83f4d4a01e7259618a39535c",
            namespace="mesh",
            method="topology_mesh_cut",
            parameters=(
                CommandParameterBinding(
                    name="fill_cut",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="keep_sides",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_to_target",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.mirror",
            binding_hash="sha256:c72b4f2db7fb4c84e6263747ba88e14f793821956fa5186f20f92b40e1a9587b",
            namespace="mesh",
            method="topology_mirror",
            parameters=(
                CommandParameterBinding(
                    name="keep_original",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="plane",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="weld_seam",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.plane_cut",
            binding_hash="sha256:110fd4aa3bd35087db790225b38a796d66ff7c475f5d46cc27861a9442da37c9",
            namespace="mesh",
            method="topology_plane_cut",
            parameters=(
                CommandParameterBinding(
                    name="fill_hole",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="keep_side",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="plane",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.remesh",
            binding_hash="sha256:b86d46b0db84a1148b82ce9ff06be9f9337add0f76db0fcb17351d11282ec5f5",
            namespace="mesh",
            method="topology_remesh",
            parameters=(
                CommandParameterBinding(
                    name="iterations",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="preserve_boundaries",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="preserve_sharp_edges",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_edge_length_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.simplify",
            binding_hash="sha256:c73273ff97c2a0ad69bcb0f38d4957cb98dccd49e72bf8fead98540a8d791966",
            namespace="mesh",
            method="topology_simplify",
            parameters=(
                CommandParameterBinding(
                    name="preserve_boundaries",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_value",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.subdivide",
            binding_hash="sha256:3ef5d00be94378fa265083510970651925d6f67c401b9099dc04538a267da8e5",
            namespace="mesh",
            method="topology_subdivide",
            parameters=(
                CommandParameterBinding(
                    name="levels",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="scheme",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.trim",
            binding_hash="sha256:5c4d9ad8a62172236d87ea9ce06808b039deb9d8cbfd81736b8e55c314daae65",
            namespace="mesh",
            method="topology_trim",
            parameters=(
                CommandParameterBinding(
                    name="fill_hole",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="keep_region",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_to_target",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.voxel_boolean",
            binding_hash="sha256:6a92c991accfcac901b379fcb855a31badfd51509310c26ae8b513a143ed495f",
            namespace="mesh",
            method="topology_voxel_boolean",
            parameters=(
                CommandParameterBinding(
                    name="adaptivity",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operand_to_target",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="operation",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_revision",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="voxel_size_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.transform.bake",
            binding_hash="sha256:370a1d7e71d6111d715e022032607c15fe75f281ad6529b67974234ae5a28231",
            namespace="mesh",
            method="transform_bake",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.voxel_grid.apply",
            binding_hash="sha256:a87d85533b1b13e2f1d23c0330f226cc869bafc6bec28302ce80295f4165020f",
            namespace="mesh",
            method="voxel_grid_apply",
            parameters=(
                CommandParameterBinding(
                    name="session_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="mesh_build",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="collision",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="material_ref",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="keep_session",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.voxel_grid.session",
            binding_hash="sha256:f858a024a9ed53bfb9089f3c418fd3a2ce28580f95b6f5c2477a5594e714cf79",
            namespace="mesh",
            method="voxel_grid_session",
            parameters=(
                CommandParameterBinding(
                    name="action",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="session_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="mode",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="grid_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="actor_ref",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="label",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cell_size",
                    wire_type="number",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="origin",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="rotation",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="anchor",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="bounds",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="max_operation_cells",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="metasound.graph.compile_settle",
            binding_hash="sha256:5901f3a60f5edd5500b4358eb2bdfacc43cdaf51e0a87f66b7eb35a21bcbf4bc",
            namespace="metasound",
            method="graph_compile_settle",
            parameters=(
                CommandParameterBinding(
                    name="expected_document_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="registration_policy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="metasound.graph.default.mutate",
            binding_hash="sha256:9e81dd99043994d8b5697bfcb2f035fc0a756d907ae1c94ca98331461a37fcef",
            namespace="metasound",
            method="graph_default_mutate",
            parameters=(
                CommandParameterBinding(
                    name="data_type_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="intent",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="node_guid",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="value",
                    wire_type="any",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="vertex_guid",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="metasound.graph.interface.mutate",
            binding_hash="sha256:8529bede7ee1a91ddf93afede96c8ce9f78907eb234dc14ac9e036deb6f6e5db",
            namespace="metasound",
            method="graph_interface_mutate",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="metasound.graph.link.mutate",
            binding_hash="sha256:a3116add5d41703f35a2c0b63b4e868dd516f09228054d1ca1a05019b7729549",
            namespace="metasound",
            method="graph_link_mutate",
            parameters=(
                CommandParameterBinding(
                    name="links",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="metasound.graph.node.mutate",
            binding_hash="sha256:06cb42a890d3a0f9a3e6df9f28f7c94c8722b4d2f02ec4318b85ce7abdf5ee8d",
            namespace="metasound",
            method="graph_node_mutate",
            parameters=(
                CommandParameterBinding(
                    name="nodes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="modeling.actor.mesh.replace",
            binding_hash="sha256:200521c0ca16c0e1041bd145b057feee38236cd0287a1b364d276c859e30e53b",
            namespace="modeling",
            method="actor_mesh_replace",
            parameters=(
                CommandParameterBinding(
                    name="actor_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="mesh_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="modeling.asset.material_slot.remove",
            binding_hash="sha256:5367f44354fb41995265b8e9823e68ef6d589f4c4d685d739488fa258a21fa51",
            namespace="modeling",
            method="asset_material_slot_remove",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="index",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="modeling.voxel.bounds.remove",
            binding_hash="sha256:3c2051c802042d109eed5aa61b95906de52fc77f5c381762b6c2c47bae13f04a",
            namespace="modeling",
            method="voxel_bounds_remove",
            parameters=(
                CommandParameterBinding(
                    name="actor_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="component_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="space",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="min_x",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="min_y",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="min_z",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="max_x",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="max_y",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="max_z",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.asset.duplicate",
            binding_hash="sha256:e381ce6848397594dffbc9404844deeb175af94b5836a9e8c4beba265b0362e9",
            namespace="niagara",
            method="asset_duplicate",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.compile_refresh_settle",
            binding_hash="sha256:3a5a401ccd3becdd405c43d6ce71752c0737a8178afa09e811a1c39ac2c0774a",
            namespace="niagara",
            method="compile_refresh_settle",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.compound.apply",
            binding_hash="sha256:11057f534384503cff2194edb0ba3156cebd97865f82137ce7cfc1d7e6509ce9",
            namespace="niagara",
            method="compound_apply",
            parameters=(
                CommandParameterBinding(
                    name="emitter_handle_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="module_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="stage_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="value",
                    wire_type="any",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.emitter.asset.create",
            binding_hash="sha256:0497fbd4802909806c72092697478efebd07fa5e5efdde56327ebe650f766dac",
            namespace="niagara",
            method="emitter_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.module.candidates",
            binding_hash="sha256:7c55cfe07a8731237314ce0dde10fbe3834d1fce3c6bfaa5521326b027780204",
            namespace="niagara",
            method="module_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_usage",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_usage_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="emitter_handle_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.renderer_event_parameter.apply",
            binding_hash="sha256:eaa016791f347dd791c55c28e92e67b52e0c84277d2fb82e769a6ac01f8fb4e3",
            namespace="niagara",
            method="renderer_event_parameter_apply",
            parameters=(
                CommandParameterBinding(
                    name="emitter_handle_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parameter_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="renderer_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="type_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="value",
                    wire_type="any",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.stack.issue_fix",
            binding_hash="sha256:cebf3aaa4d8a282ea8237dbafc933a816599b2229db7a09b7bfa9370a876b97c",
            namespace="niagara",
            method="stack_issue_fix",
            parameters=(
                CommandParameterBinding(
                    name="emitter_handle_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="fix_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="issue_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.stack.reorder",
            binding_hash="sha256:92b0e99aacd81681f54fb9fa6808961fc2b4bdac77d4bdc0908cd7fff2300158",
            namespace="niagara",
            method="stack_reorder",
            parameters=(
                CommandParameterBinding(
                    name="emitter_handle_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="item_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="predecessor_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="stage_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.system.asset.create",
            binding_hash="sha256:0bac393995e9c4dffe2e6beeef5a1c358bde371174461114fd47594805d4f5e7",
            namespace="niagara",
            method="system_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="operation.cancel",
            binding_hash="sha256:c6f7515c44090c3f9f4e426aacdc0e7818a0b75a1d1a109e7c1daf94ee002fba",
            namespace="operation",
            method="cancel",
            parameters=(
                CommandParameterBinding(
                    name="operation_ref",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="reason",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="operation.plan.execute",
            binding_hash="sha256:095ff055d2dba236dbd9ecff3cb4c598824129035092166f7f03d90e35f6ea61",
            namespace="operation",
            method="plan_execute",
            parameters=(
                CommandParameterBinding(
                    name="steps",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="on_error",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="atomicity",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="operation.receipt",
            binding_hash="sha256:40aa5be4f1a344baaab9d9a52c2826fd7417f2f5f95139882c50714d5deed54f",
            namespace="operation",
            method="receipt",
            parameters=(
                CommandParameterBinding(
                    name="operation_ref",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="operation.reconcile",
            binding_hash="sha256:a98efc750a7bfb02f3da40c33ce91a45b9bd3081410e13c50d2ca20cfddb4ad4",
            namespace="operation",
            method="reconcile",
            parameters=(
                CommandParameterBinding(
                    name="operation_ref",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_generation",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="operation.release",
            binding_hash="sha256:6a04abe6d23974d2b93b9586183ff0e7f1e76c5c9f970330c6bb577b7416bc14",
            namespace="operation",
            method="release",
            parameters=(
                CommandParameterBinding(
                    name="operation_ref",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="operation.resume",
            binding_hash="sha256:574b18d8802b2a5d0ff144ba8393d19fa132c916530fbf1a4ad3e6194b97b722",
            namespace="operation",
            method="resume",
            parameters=(
                CommandParameterBinding(
                    name="operation_ref",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_generation",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="operation.status",
            binding_hash="sha256:f625e3740e10e3631438110180e46844c24542fc77a9bc970073ef4ce952ca70",
            namespace="operation",
            method="status",
            parameters=(
                CommandParameterBinding(
                    name="operation_ref",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.component.apply",
            binding_hash="sha256:45952af166e117d853fc196c06e386565eafc99779fdd4173c297a1db73d625d",
            namespace="pcg",
            method="component_apply",
            parameters=(
                CommandParameterBinding(
                    name="generation_policy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="graph_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.component.world_binding.apply",
            binding_hash="sha256:afbb1be83a55c4fd05a465ec441e3ba21b5ffaef20c1691aa6974cd8e732e533",
            namespace="pcg",
            method="component_world_binding_apply",
            parameters=(
                CommandParameterBinding(
                    name="actor_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="component_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="generation_policy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="graph_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.data_asset.apply",
            binding_hash="sha256:79aaaa133a9492261ccb76819da2c62f2aa2b2d9401ff9b818d8b1323a1f5624",
            namespace="pcg",
            method="data_asset_apply",
            parameters=(
                CommandParameterBinding(
                    name="content_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="data_type_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="value",
                    wire_type="any",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.data_asset.create_from_level",
            binding_hash="sha256:5be98851d0af84fca24bece523dc48c3b1c57bbaa09c1f56127786ebe5f8c354",
            namespace="pcg",
            method="data_asset_create_from_level",
            parameters=(
                CommandParameterBinding(
                    name="data_type_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="source_level_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.generated_spatial_data.read",
            binding_hash="sha256:90c729a0623e495c111451030feb67d0dba2d97d7de9efb5083499689471fa07",
            namespace="pcg",
            method="generated_spatial_data_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.graph.apply",
            binding_hash="sha256:f0ad99173861183150d4297dcd3409e9d7930518bb44733c52a936a3c1152b32",
            namespace="pcg",
            method="graph_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.graph.asset.create",
            binding_hash="sha256:ce817a6371a26314dab8072ebf6e79bc3e894076e475e2382b9d3091c70a8fe4",
            namespace="pcg",
            method="graph_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.graph_instance.apply",
            binding_hash="sha256:576ca7763749cae5bce1a20fb45219c89abe6da71feaef6c89bd015b84514827",
            namespace="pcg",
            method="graph_instance_apply",
            parameters=(
                CommandParameterBinding(
                    name="graph_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="overrides",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.graph_parameters.apply",
            binding_hash="sha256:88c79933e47917b5fa81f3395f285f9963c3a6271593ded5e0e8cc7076614612",
            namespace="pcg",
            method="graph_parameters_apply",
            parameters=(
                CommandParameterBinding(
                    name="parameters",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.node.candidates",
            binding_hash="sha256:3c19a512604ba79da8d0778d6d303669b8f8adc0d31836859a33b1a848f399d7",
            namespace="pcg",
            method="node_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.partition.spatial_state.read",
            binding_hash="sha256:7f061e03c57a0c065cbcdace08390c2bb05a6dd975edb65c9478916eb53da60c",
            namespace="pcg",
            method="partition_spatial_state_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="physics.asset.structure.replace",
            binding_hash="sha256:0233755e1e4edae35dfb7f36dffda68be72027854cbed0bafc47a1960d69b1ad",
            namespace="physics",
            method="asset_structure_replace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="physics.constraint.update",
            binding_hash="sha256:0796070647d18679781bcf3eae11a219f308898eaadb0eb8e12ef29547b485a6",
            namespace="physics",
            method="constraint_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="physics.material.update",
            binding_hash="sha256:c4077f6775422e5bffa4e138d22e24a120cee94708a59bfdfddba5d90e96ee7c",
            namespace="physics",
            method="material_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="physics.simulation.probe",
            binding_hash="sha256:783f27932fca79236ad11898f63d5c80980688a46f3608b570361fe7a2f0eae0",
            namespace="physics",
            method="simulation_probe",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="project.platform",
            binding_hash="sha256:f50916c2fce9ad2a38421cd614feee0c37f2f0244781d1be14ef415fa46eebaa",
            namespace="project",
            method="platform",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="project.settings",
            binding_hash="sha256:60268291aaf4bb3ca12afac08ef7422d386e365140b4bea6cf01adada4b2e059",
            namespace="project",
            method="settings",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="project.summary",
            binding_hash="sha256:cd9691d7a0d220f780906e7333b140ae37b9e3985463cbf81af25e9458b34da1",
            namespace="project",
            method="summary",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="project.validation",
            binding_hash="sha256:f084c970a9484a2cc88830d398f212c11664d4070bcca25b8d2387fe3faea7a9",
            namespace="project",
            method="validation",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="query.calibration.read",
            binding_hash="sha256:ef0dd8d86296719583c5c2e6fbf60468329d953856bca276e2c95ee928ed75ba",
            namespace="query",
            method="calibration_read",
            parameters=(
                CommandParameterBinding(
                    name="category",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="search_text",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="query.command.detail",
            binding_hash="sha256:779197969f28a3d3d386106c653a3bbfc2a35a5bb818471bc852fb6c0f531b09",
            namespace="query",
            method="command_detail",
            parameters=(
                CommandParameterBinding(
                    name="command_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="contract_hash",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="variant_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="query.command.search",
            binding_hash="sha256:b9ff4cb525b8c31a3859ebe7c5f7a4f9619a205d5690d1d0a0866772b387e772",
            namespace="query",
            method="command_search",
            parameters=(
                CommandParameterBinding(
                    name="intent",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="query.content.search",
            binding_hash="sha256:0e5fbdd3132f84c6386f602acc1c60750163c5319d928b60eb549e20e4a198e2",
            namespace="query",
            method="content_search",
            parameters=(
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="match_mode",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="content_kinds",
                    wire_type="array",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="class_path",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="path_prefix",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="owner_identity",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="required_operations",
                    wire_type="array",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit_per_provider",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="reference.asset_apply",
            binding_hash="sha256:c774792695bc79139dbcae322d732a7adc090632938b2e5452267425c9a8234d",
            namespace="reference",
            method="asset_apply",
            parameters=(
                CommandParameterBinding(
                    name="object_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="intent",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="proposed_text",
                    wire_type="string",
                    required=False,
                    nullable=True,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="reference.asset_read",
            binding_hash="sha256:1d285b2973bb3706a72e4a384cd7211ca9b484a9f22e90b591e5f29e12950ed8",
            namespace="reference",
            method="asset_read",
            parameters=(
                CommandParameterBinding(
                    name="object_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="reference.origin.resolve",
            binding_hash="sha256:fe618646a9e1a406e3a9a78ff8e72f32bccb1eaf905f96716614c44674b6414e",
            namespace="reference",
            method="origin_resolve",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.control.bake.animation",
            binding_hash="sha256:fb0d981de979beceec2d4ca6fee0dd9f6504b9f082744f7a8e9763b38a395c39",
            namespace="rig",
            method="control_bake_animation",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.control.bake.controls",
            binding_hash="sha256:6a204b459c82ab5b6bdc9ac812b443dcf4d4369059d04f2d77bebc691ffb569a",
            namespace="rig",
            method="control_bake_controls",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.ik.definition.update",
            binding_hash="sha256:a9948a2bc16e0178858b7d585e9bc807cbe91d60430803c35d335232c9e67695",
            namespace="rig",
            method="ik_definition_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.retarget.assets.generate",
            binding_hash="sha256:7e36f9625ede80869e68c149d412e027e3592043e5716455e63e2df9a3af9b3b",
            namespace="rig",
            method="retarget_assets_generate",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.retarget.definition.update",
            binding_hash="sha256:31132650ca99a1896ef51442b2d4bf8391fabc4d2b35c73109a85730bf019a29",
            namespace="rig",
            method="retarget_definition_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.retarget.pose.auto_align",
            binding_hash="sha256:6edb40e23c34732a19a88272a54b6f9dda64c090fe4eb6e76651bd83e3467eb2",
            namespace="rig",
            method="retarget_pose_auto_align",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.retarget.pose.update",
            binding_hash="sha256:cedc43cf3f296bca2bd2c587d9dbd88dc5ab88d1f5128dd28e38ecb2bbab547d",
            namespace="rig",
            method="retarget_pose_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.skeleton.preview_mesh.bind",
            binding_hash="sha256:c7c1b2485a75450ea3f2c560c230b47296badce360a913f64ce2dac78d95030c",
            namespace="rig",
            method="skeleton_preview_mesh_bind",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.skeleton.socket.update",
            binding_hash="sha256:7d47ba749b949f98e54ced5cfc2191b380e830681d49e64b90af9879d26ed24d",
            namespace="rig",
            method="skeleton_socket_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="skeletal_mesh.remove_morph_target",
            binding_hash="sha256:f0785facaf84447c86a896ddaa0e4bf304685253a0ac9a9ae068f240db8a8560",
            namespace="skeletal_mesh",
            method="remove_morph_target",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="skeletal_mesh.remove_skin_weight_profile",
            binding_hash="sha256:de046888fc9e70d7bc604ec5ee19634b7fe74a8ba7199c99e660968cb77cf712",
            namespace="skeletal_mesh",
            method="remove_skin_weight_profile",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="sound_cue.graph.compile_settle",
            binding_hash="sha256:5ac7e2f1e8cee31570b2158f9ef971fa60dab3b95a29b0974e0b66931220b5e1",
            namespace="sound_cue",
            method="graph_compile_settle",
            parameters=(
                CommandParameterBinding(
                    name="expected_graph_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="sync_policy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="sound_cue.graph.node.mutate",
            binding_hash="sha256:552b25f812a24e84d844eff0c2677a354db25047121e26433a41ef8964640f72",
            namespace="sound_cue",
            method="graph_node_mutate",
            parameters=(
                CommandParameterBinding(
                    name="nodes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="sound_cue.graph.relation.mutate",
            binding_hash="sha256:97c3e0d3e13591700a777e9eeda41d8b391243595c6c0cada1f3cf5e97c710c6",
            namespace="sound_cue",
            method="graph_relation_mutate",
            parameters=(
                CommandParameterBinding(
                    name="relations",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="sound_cue.graph.root.mutate",
            binding_hash="sha256:c00904c3b3c32ff2b2df06a724194eee22f82240e5fe6697e63da94ae9436a71",
            namespace="sound_cue",
            method="graph_root_mutate",
            parameters=(
                CommandParameterBinding(
                    name="intent",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="root_node_object_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="texture_graph.artifact.bake",
            binding_hash="sha256:271056d16049c8544ba3a273eb1003094cd6e2a45bfc90dbacf96ed616b454da",
            namespace="texture_graph",
            method="artifact_bake",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="outputs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="texture_graph.artifact.capture",
            binding_hash="sha256:34dba5fe4fd16632ec349aab47497d34a4d228c283bdc18eb7eb18725248a9ca",
            namespace="texture_graph",
            method="artifact_capture",
            parameters=(
                CommandParameterBinding(
                    name="expected_settled_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="outputs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="texture_graph.graph.link.mutate",
            binding_hash="sha256:beeb0e0db3fb11538050ca1a5adc6805f249535c0aee79158c45b40d8f47e1f3",
            namespace="texture_graph",
            method="graph_link_mutate",
            parameters=(
                CommandParameterBinding(
                    name="links",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="texture_graph.graph.node.mutate",
            binding_hash="sha256:18a23346c0e8c0a177a6df3cc212b405addccf69fdbfaf7332703da5ca972b05",
            namespace="texture_graph",
            method="graph_node_mutate",
            parameters=(
                CommandParameterBinding(
                    name="nodes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="texture_graph.graph.parameter.mutate",
            binding_hash="sha256:deb9eb2c819d9074f664f820cb1387bfffbe1d76a4cd6fa854068cc3f985aa80",
            namespace="texture_graph",
            method="graph_parameter_mutate",
            parameters=(
                CommandParameterBinding(
                    name="parameters",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="texture_graph.graph.validate_evaluate_settle",
            binding_hash="sha256:4c7d7820b6befebe476c71724193e6f77bdb420674ec2dd988ce3b953c8d2748",
            namespace="texture_graph",
            method="graph_validate_evaluate_settle",
            parameters=(
                CommandParameterBinding(
                    name="evaluation_policy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_graph_revision",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="texture_graph.runtime.probe",
            binding_hash="sha256:8f13af2855b4886869a3b9a151a05de12e48740133314e976659149ef28bf1c3",
            namespace="texture_graph",
            method="runtime_probe",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="render_output_index",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="expected_stats",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="timeline.sequence.create",
            binding_hash="sha256:00885226f4262fe6886c4cb95406784779c824eae7c249fdf79972bd01c70f84",
            namespace="timeline",
            method="sequence_create",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="timeline.sequence.read",
            binding_hash="sha256:e5f33d493bf9aa8e378fdf3764de78ac8ff19d54d1f2c2abcc6c594468d96391",
            namespace="timeline",
            method="sequence_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="timeline.sequence.settings.update",
            binding_hash="sha256:2e96cec3b2bd4327431608fd667d9fb5893901a529fed286c602251ce9c52692",
            namespace="timeline",
            method="sequence_settings_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="timeline.sequence.structure.replace",
            binding_hash="sha256:ffedd24b57bcabdc63b8d01791bd3e8013d83b549a7d3bb9692e09f700fa29fb",
            namespace="timeline",
            method="sequence_structure_replace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="timeline.widget_animation.read",
            binding_hash="sha256:4314e1ae50216f1c83ef933ecdab754ad16190eece9cfb1b839e0d308858b7d6",
            namespace="timeline",
            method="widget_animation_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="umg.asset.create",
            binding_hash="sha256:9735bb2baa46231f090b45a3d6f99154d5a4eb8ba7e282eda436d10a3cea616a",
            namespace="umg",
            method="asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="umg.widget.candidates",
            binding_hash="sha256:34ddd9f800b42cdd6a8f3e48ab24a75e0bbfe802590c54b66cabfbb110b4baf5",
            namespace="umg",
            method="widget_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="umg.widget.events.discover",
            binding_hash="sha256:0cc4c4479af40f28b82b5f66b06b63c127c4697b36774835f9b6cd1dc3481052",
            namespace="umg",
            method="widget_events_discover",
            parameters=(
                CommandParameterBinding(
                    name="owner_item_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.actor.pick",
            binding_hash="sha256:cf3ecc069ccf41469c55872b764929ca2ae999121e1dec63a190a26a610fb254",
            namespace="viewport",
            method="actor_pick",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.actor.select",
            binding_hash="sha256:c1a659ec3bc77f09bdeb90324e35ceea3b6af338946c74da821e6377d2687b6d",
            namespace="viewport",
            method="actor_select",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.camera.frame",
            binding_hash="sha256:0144039bad8be2683c7dfc1373990b85d654756b0ad352a261770ad8d165559f",
            namespace="viewport",
            method="camera_frame",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.instance.list",
            binding_hash="sha256:7e81d120ce6ff9172a46cce03c7b7244e7bd7561ceef77f15cb63feb4aaf728b",
            namespace="viewport",
            method="instance_list",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.pixel_scale.read",
            binding_hash="sha256:e0d890065c33461a495c750361c8804d9eb2ba5fb900d937e499ab4d6d1971b1",
            namespace="viewport",
            method="pixel_scale_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.ray.deproject",
            binding_hash="sha256:fc2621a1058cda5ca29e173a1bbda4c2403dc0797923a9863b6c1dd2cce43380",
            namespace="viewport",
            method="ray_deproject",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.ray.trace",
            binding_hash="sha256:3501df21b66fcc3ae13eff06ed9fc25c5001b30cfd95919ff289a41ffd6f8143",
            namespace="viewport",
            method="ray_trace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.state.read",
            binding_hash="sha256:3a538ac5bb65410636fbdd43a10c6eabb23e646ad613e3e614104b1d7012deb2",
            namespace="viewport",
            method="state_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.state.restore",
            binding_hash="sha256:1ca2dc99cfa0b28ee3595ff31d7036533b76eb5882d308dae0d26fc22d567289",
            namespace="viewport",
            method="state_restore",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.state.update",
            binding_hash="sha256:06a08541ae740d6ccff45ab2beaa6f4862e6f7401987d99084f17fa3c3102f83",
            namespace="viewport",
            method="state_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.view_mode.list",
            binding_hash="sha256:73d7367e4373267d6994da1b711bd50de1a7b24758e78615c8aaccf628c3e003",
            namespace="viewport",
            method="view_mode_list",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.warning.list",
            binding_hash="sha256:e05ea49c1abd922d26dbd45ef13bb05786aaf8472d733698200e9d1564a55a70",
            namespace="viewport",
            method="warning_list",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.actor.candidates",
            binding_hash="sha256:0ed3f6324ec95926b196edd348d39ab98818e1e5240668a9a9431429b92325b2",
            namespace="world",
            method="actor_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="category",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="limit",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="cursor",
                    wire_type="integer",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.actor.create",
            binding_hash="sha256:a962c8e7f6ef4526c04230e949750402729290f78ae0288bde708869ee221f37",
            namespace="world",
            method="actor_create",
            parameters=(
                CommandParameterBinding(
                    name="actor_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="folder_path",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="label",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="tags",
                    wire_type="array",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.actor_components",
            binding_hash="sha256:2c21a1afe1f4e3ab52c2364ddbc5a32fe62da8580563c00e5a2bfc8b5fd549bb",
            namespace="world",
            method="actor_components",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.actor_hlod_layer.update",
            binding_hash="sha256:45432945e67b2f49212a488ea86835a5cf37d160d0438a745801edc3b72fc95e",
            namespace="world",
            method="actor_hlod_layer_update",
            parameters=(
                CommandParameterBinding(
                    name="collection_ref",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="subject_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.actor_streaming_policy.update",
            binding_hash="sha256:db4f1ce9ab2786170d78cc32dcdf3db6dbc11ea103afedd71de547b018202231",
            namespace="world",
            method="actor_streaming_policy_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.actors",
            binding_hash="sha256:6e40949bf9310cf08f8934a44cd5623335bc66cfeea18ae6ce7a6614a25573bf",
            namespace="world",
            method="actors",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.capsule_path",
            binding_hash="sha256:6844dc21072fbedb32fa4e35ce9b0c50c77263c549f74b22460f1785e51e4420",
            namespace="world",
            method="capsule_path",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.capsule_sweep",
            binding_hash="sha256:2060a664d6c6cd8493b329fe90ba29664731f928f6cad7f2e7a22904da74a057",
            namespace="world",
            method="capsule_sweep",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.content",
            binding_hash="sha256:fd455e8417fe3e58c21d5e7442bf3cd7806de33ca0c45238e05e841c1ccd1bba",
            namespace="world",
            method="content",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.data_layer.delete",
            binding_hash="sha256:66a314e48b44f08920e346e6d63a3edb7d4f25cee07616829d83b99e1e8bbe57",
            namespace="world",
            method="data_layer_delete",
            parameters=(
                CommandParameterBinding(
                    name="layer",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.data_layer_instance.create",
            binding_hash="sha256:dda0a851d8d4b77d020737ac4a3101510bd1e0621c966b525bd2db97f53b7fb5",
            namespace="world",
            method="data_layer_instance_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_ref",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="initial_state",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="parent_ref",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="private",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="short_name",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.data_layer_relation.update",
            binding_hash="sha256:9b3b6682602337b6e65ecd6d91c01e8a278075ce9c456457c693dfff3570cee6",
            namespace="world",
            method="data_layer_relation_update",
            parameters=(
                CommandParameterBinding(
                    name="collection_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="relation_kind",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="subject_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.data_layer_state.update",
            binding_hash="sha256:c7665f5dfacdb5ab7864f080924d9e5e4c13e2112fb78397920d1cb0d40856b3",
            namespace="world",
            method="data_layer_state_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.data_layers",
            binding_hash="sha256:1f101499c8ed7644464e4e022582d606689109a2b5db9b69f89f10258362c5d7",
            namespace="world",
            method="data_layers",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.hlod_assignments",
            binding_hash="sha256:ee1ec9f7dbe87a8b837a3960d09d1b043bf30e9dbc384b2fafe0b9fb1449bdff",
            namespace="world",
            method="hlod_assignments",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.level_content.delete_scope",
            binding_hash="sha256:2d53b647cde176ed4c136e078f565070f1abe1fe08b6c69dfdb8176c537e1cad",
            namespace="world",
            method="level_content_delete_scope",
            parameters=(
                CommandParameterBinding(
                    name="folder_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="managed_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.level_game_mode.update",
            binding_hash="sha256:d786b55e788cf566de970a853f28879407bc57ae30d336d86aaacbc5ba90d0bc",
            namespace="world",
            method="level_game_mode_update",
            parameters=(
                CommandParameterBinding(
                    name="game_mode_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.level_streaming.move_actors",
            binding_hash="sha256:bb787215210479849bfad09fc2b684f0623f19eda525e1b07bf90e0fe7914fd5",
            namespace="world",
            method="level_streaming_move_actors",
            parameters=(
                CommandParameterBinding(
                    name="actor_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="level_package",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.level_streaming.remove",
            binding_hash="sha256:28ada3bb09ce69432ebc498c387eaeee3b97c28755a4238ea936714f3bc9df60",
            namespace="world",
            method="level_streaming_remove",
            parameters=(
                CommandParameterBinding(
                    name="level_package",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.mesh_closest_vertex",
            binding_hash="sha256:7c96da94c8df8d25dedc45be739749f481df0a8d3a16ae8e3e69a883dd8df9d4",
            namespace="world",
            method="mesh_closest_vertex",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.mesh_vertex_position",
            binding_hash="sha256:d7a2dd40fde4b356739ed6f1235040432d6f642bd9908e207b89b6d4c90d062b",
            namespace="world",
            method="mesh_vertex_position",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.nav_connectivity",
            binding_hash="sha256:457498347409f7f5d941c5ed0d436c4bdc3aca1c5af7f25474f3d6a5bacbb6a2",
            namespace="world",
            method="nav_connectivity",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.nav_find_path",
            binding_hash="sha256:dd93e3cafc7930098cf42998340e333514bcf06f324c55706dc15349a86d556b",
            namespace="world",
            method="nav_find_path",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.nav_project_point",
            binding_hash="sha256:0ff435a73f1239ac579565a121b700e643169fcf98fa9dbc61b5f3cbac1a707d",
            namespace="world",
            method="nav_project_point",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.nearby_shapes",
            binding_hash="sha256:1de6ede784d63f097882f5471101aa321cf4e9624d777c8398d3d94fdd30e8f5",
            namespace="world",
            method="nearby_shapes",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.object_align",
            binding_hash="sha256:8e26731cac6e674f5cfa0d1b880a5749778a4b984aaecefce11e999f5f8cb1de",
            namespace="world",
            method="object_align",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.object_snap_to_surface",
            binding_hash="sha256:8a362d7345c0d388dd665f092d3fd7c99030a1ef2b356d919fd77de0185160dc",
            namespace="world",
            method="object_snap_to_surface",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.object_transform.read",
            binding_hash="sha256:1bd45d3fc6ff1b99c94c8f1d78ade8e957f0c77c995aa61c0a127e4231494358",
            namespace="world",
            method="object_transform_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.object_transform.update",
            binding_hash="sha256:b21d52814180c133876d502d87cf94c512cd8d7dc29c5a631c0826fa5b365969",
            namespace="world",
            method="object_transform_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.overlap",
            binding_hash="sha256:31d60ba471b3f5f421e889c04b0569a96801ac6ef13f9ec37033f970849208b8",
            namespace="world",
            method="overlap",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.partition",
            binding_hash="sha256:e9533384f6f08e90bea5d3983dc35a96fd2721bb7d736c50031d4604c68965ee",
            namespace="world",
            method="partition",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.partition_health",
            binding_hash="sha256:dcb330b872e23a402a8e5a19e6eb8023d4edd8a8f383d61c024d57fa978f20b7",
            namespace="world",
            method="partition_health",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.pcg.cleanup",
            binding_hash="sha256:5a42b681531d0aa71367f6ce87d8ab81b6776ee3806d2441b1435ca462761009",
            namespace="world",
            method="pcg_cleanup",
            parameters=(
                CommandParameterBinding(
                    name="actor_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="component_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="destructive_authorization_id",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.physics_component",
            binding_hash="sha256:71ae9d5b85377172baae5aa2135fdd95c72f1730768af2ad71600a5b21cc4fb6",
            namespace="world",
            method="physics_component",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.physics_constraint",
            binding_hash="sha256:c8512f540e680c6e6bfc867ea148dceac2f2208009a8a1ec0f054120536ab882",
            namespace="world",
            method="physics_constraint",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.property",
            binding_hash="sha256:de868e3f7d1ac17577628746c56febb9a379e5df73d0d6c4fe645424cc5fbd9d",
            namespace="world",
            method="property",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.ray_trace",
            binding_hash="sha256:f2cfe2dd7dad8427e25c64a82a98c56711bb0ada4506841c3269f05bd5ac71a9",
            namespace="world",
            method="ray_trace",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.selection",
            binding_hash="sha256:2e54d576de8d914e37cbbb48cf0fa09db7476a6e9315991ea08af85dbce3a18a",
            namespace="world",
            method="selection",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.streaming_levels",
            binding_hash="sha256:f5069955d2bf2184f476bca23ce6f4788a4e06c18b8240f38f0bc9a3a1d3a759",
            namespace="world",
            method="streaming_levels",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.streaming_relation.create",
            binding_hash="sha256:f3df619ac84fc187dd42dc303a96dcf73fb952daef9f8826d59cac71b40f8b2c",
            namespace="world",
            method="streaming_relation_create",
            parameters=(
                CommandParameterBinding(
                    name="level_asset_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="streaming_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.streaming_relation.state.update",
            binding_hash="sha256:7dba9f6294926044bf8c51eb682992fe324bba924e2aa05194ec9cc5964addb2",
            namespace="world",
            method="streaming_relation_state_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.summary",
            binding_hash="sha256:df4d22766e65dd903830e5a67d3b31d9eb7ecd8bd6e9c0db6889895bce791cc6",
            namespace="world",
            method="summary",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.wall.create_with_opening",
            binding_hash="sha256:7efc3685f68b0729c935a60a166333c813f4f50eb40946643c7e81ca9c5fd2b5",
            namespace="world",
            method="wall_create_with_opening",
            parameters=(
                CommandParameterBinding(
                    name="opening",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="plane",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="segment_template",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="wall",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.world_partition_streaming.update",
            binding_hash="sha256:bbaf17e20753ed0c7036fc518539bf516ac69d37e8f86bfdc5cc8f9af0964a55",
            namespace="world",
            method="world_partition_streaming_update",
            parameters=(
                CommandParameterBinding(
                    name="enabled",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
    )
)

class GeneratedCommandNamespaces:
    __slots__ = ("ai", "animation", "animation_rig_graph", "asset", "asset_durable", "audio", "audio_media", "blueprint", "capture", "config", "content_graph", "deformer", "editor", "editor_project", "external", "graph", "job", "landscape", "material", "material_instance", "mesh", "metasound", "modeling", "niagara", "operation", "pcg", "physics", "project", "query", "reference", "rig", "skeletal_mesh", "sound_cue", "texture_graph", "timeline", "umg", "viewport", "world")

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self.ai = AiCommands(client)
        self.animation = AnimationCommands(client)
        self.animation_rig_graph = AnimationRigGraphCommands(client)
        self.asset = AssetCommands(client)
        self.asset_durable = AssetDurableCommands(client)
        self.audio = AudioCommands(client)
        self.audio_media = AudioMediaCommands(client)
        self.blueprint = BlueprintCommands(client)
        self.capture = CaptureCommands(client)
        self.config = ConfigCommands(client)
        self.content_graph = ContentGraphCommands(client)
        self.deformer = DeformerCommands(client)
        self.editor = EditorCommands(client)
        self.editor_project = EditorProjectCommands(client)
        self.external = ExternalCommands(client)
        self.graph = GraphCommands(client)
        self.job = JobCommands(client)
        self.landscape = LandscapeCommands(client)
        self.material = MaterialCommands(client)
        self.material_instance = MaterialInstanceCommands(client)
        self.mesh = MeshCommands(client)
        self.metasound = MetasoundCommands(client)
        self.modeling = ModelingCommands(client)
        self.niagara = NiagaraCommands(client)
        self.operation = OperationCommands(client)
        self.pcg = PcgCommands(client)
        self.physics = PhysicsCommands(client)
        self.project = ProjectCommands(client)
        self.query = QueryCommands(client)
        self.reference = ReferenceCommands(client)
        self.rig = RigCommands(client)
        self.skeletal_mesh = SkeletalMeshCommands(client)
        self.sound_cue = SoundCueCommands(client)
        self.texture_graph = TextureGraphCommands(client)
        self.timeline = TimelineCommands(client)
        self.umg = UmgCommands(client)
        self.viewport = ViewportCommands(client)
        self.world = WorldCommands(client)


class GeneratedClientBindingsMixin:
    __slots__ = ()

    @property
    def ai(self) -> AiCommands:
        return self._generated_commands.ai

    @property
    def animation(self) -> AnimationCommands:
        return self._generated_commands.animation

    @property
    def animation_rig_graph(self) -> AnimationRigGraphCommands:
        return self._generated_commands.animation_rig_graph

    @property
    def asset(self) -> AssetCommands:
        return self._generated_commands.asset

    @property
    def asset_durable(self) -> AssetDurableCommands:
        return self._generated_commands.asset_durable

    @property
    def audio(self) -> AudioCommands:
        return self._generated_commands.audio

    @property
    def audio_media(self) -> AudioMediaCommands:
        return self._generated_commands.audio_media

    @property
    def blueprint(self) -> BlueprintCommands:
        return self._generated_commands.blueprint

    @property
    def capture(self) -> CaptureCommands:
        return self._generated_commands.capture

    @property
    def config(self) -> ConfigCommands:
        return self._generated_commands.config

    @property
    def content_graph(self) -> ContentGraphCommands:
        return self._generated_commands.content_graph

    @property
    def deformer(self) -> DeformerCommands:
        return self._generated_commands.deformer

    @property
    def editor(self) -> EditorCommands:
        return self._generated_commands.editor

    @property
    def editor_project(self) -> EditorProjectCommands:
        return self._generated_commands.editor_project

    @property
    def external(self) -> ExternalCommands:
        return self._generated_commands.external

    @property
    def graph(self) -> GraphCommands:
        return self._generated_commands.graph

    @property
    def job(self) -> JobCommands:
        return self._generated_commands.job

    @property
    def landscape(self) -> LandscapeCommands:
        return self._generated_commands.landscape

    @property
    def material(self) -> MaterialCommands:
        return self._generated_commands.material

    @property
    def material_instance(self) -> MaterialInstanceCommands:
        return self._generated_commands.material_instance

    @property
    def mesh(self) -> MeshCommands:
        return self._generated_commands.mesh

    @property
    def metasound(self) -> MetasoundCommands:
        return self._generated_commands.metasound

    @property
    def modeling(self) -> ModelingCommands:
        return self._generated_commands.modeling

    @property
    def niagara(self) -> NiagaraCommands:
        return self._generated_commands.niagara

    @property
    def operation(self) -> OperationCommands:
        return self._generated_commands.operation

    @property
    def pcg(self) -> PcgCommands:
        return self._generated_commands.pcg

    @property
    def physics(self) -> PhysicsCommands:
        return self._generated_commands.physics

    @property
    def project(self) -> ProjectCommands:
        return self._generated_commands.project

    @property
    def query(self) -> QueryCommands:
        return self._generated_commands.query

    @property
    def reference(self) -> ReferenceCommands:
        return self._generated_commands.reference

    @property
    def rig(self) -> RigCommands:
        return self._generated_commands.rig

    @property
    def skeletal_mesh(self) -> SkeletalMeshCommands:
        return self._generated_commands.skeletal_mesh

    @property
    def sound_cue(self) -> SoundCueCommands:
        return self._generated_commands.sound_cue

    @property
    def texture_graph(self) -> TextureGraphCommands:
        return self._generated_commands.texture_graph

    @property
    def timeline(self) -> TimelineCommands:
        return self._generated_commands.timeline

    @property
    def umg(self) -> UmgCommands:
        return self._generated_commands.umg

    @property
    def viewport(self) -> ViewportCommands:
        return self._generated_commands.viewport

    @property
    def world(self) -> WorldCommands:
        return self._generated_commands.world


def bind_generated_commands(
    client: CommandExecutor,
) -> GeneratedCommandNamespaces:
    return GeneratedCommandNamespaces(client)
