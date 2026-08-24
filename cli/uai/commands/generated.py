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

GENERATED_MANIFEST_HASH = "sha256:5e6f960aca29c246ac2528dd6e62b35c6841dd00abb1105bdbb5662745656e5c"
GENERATED_REGISTRY_HASH = "sha256:36c11593999f6006b540e3433de6a546bf7f892035ba2e09d258dd61ae919261"

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
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
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
        space_ref: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if space_ref is not OMITTED:
            params["space_ref"] = space_ref
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
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
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
        component_class: str,
        requested_name: str,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["component_class"] = component_class
        params["requested_name"] = requested_name
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
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["graph_id"] = graph_id
        if query is not OMITTED:
            params["query"] = query
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
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
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
        query: str | object = OMITTED,
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["target_usage"] = target_usage
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
        limit: int | object = OMITTED,
        cursor: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
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
    ):
        params: dict[str, Any] = {}
        params["command_id"] = command_id
        params["contract_hash"] = contract_hash
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
            binding_hash="sha256:cc78fa3fcb31995d8c9155c86191c11827a6b247feca4e7800faba657c30da3e",
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
            binding_hash="sha256:b5405005d8022bcf9907194e84358a8520be82c8fb6a56cbc28e177c63500917",
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
            binding_hash="sha256:3bc346cdd93de9711a41fdcbd9b2e351d6d5e42d601290185d0c9d3e7557847c",
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
            binding_hash="sha256:9f5f6c83aefcac8958ae0e92b33c3f604694e296bee426d645e5cda726f0cc7c",
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
            binding_hash="sha256:736875e1dfd1f5a4618599750722a3f69952946bb9864ba4b5d62a0e4a47f8c7",
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
            binding_hash="sha256:c5b75ae7a061c6bb9cdfb865de9bc90a11ca9893bfd2583a228fcf607e53db94",
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
            binding_hash="sha256:2c971e2d58b77db85649397f41a27287f75b5ef7981a273c0a304c63faebb710",
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
            binding_hash="sha256:3e8b5180198447f81d475620e25a61af7c29a98c26dbc99be1ce98998ab02f18",
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
            binding_hash="sha256:f9bfabde311ca5927be00df650bbec735694172d90fce1042a8c84bdddb6513f",
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
            binding_hash="sha256:15b8b5f4698f56acbe2fe28c044529b8a005a7659282b359f6a24464d82b2a3f",
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
            binding_hash="sha256:beb0ff518aa7402b770ad152282b0759f5fc90adae6062b324afbe1363f98b91",
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
            binding_hash="sha256:cd42a1b9eb5afba707fb08e54ed6f18619af4dc01a02b24c1c12fed72d24e2cb",
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
            binding_hash="sha256:c502a058a07baa15209d625a80a7912eb1d53f902ede0aa48bf190ddb408529c",
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
            binding_hash="sha256:79448c0db11d449a1266f9755e21c1424cd0e34bee355c4a0f3d42fe5674cf44",
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
            binding_hash="sha256:35d04d9fc777087576ca4bf0b7ac9b324ca1e94760742e7d574a084b9016100e",
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
            binding_hash="sha256:f0d033149840c01bab2d4744a5940b3503a159f36ed5d2eb48e8ff108d13d600",
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
            binding_hash="sha256:b815b35a10f13999ef493f5c97dad5556cb2cf4c58809cd9d330b14dcab12343",
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
            binding_hash="sha256:58fbb3bd0a31b682785fe62fb01f8ff1ef3c752b81a9022888909c496c484878",
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
            binding_hash="sha256:6c3a3920a0647cd5c0f35c2fd9972262403330b71e2b8260160effd82be1e23e",
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
            binding_hash="sha256:83d3db0846535a3bcf8bb7275f1895214a53c8efa81fd80c1ec8e7e6623fd0be",
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
            binding_hash="sha256:0d9c66529eab430d512c1ae5c74ecc8857b2ba534dda4c14e17e6ab5dd71b22b",
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
            binding_hash="sha256:fa03338fb877cb4d816765642fb92e420e112aa311c00805138087d9882bb234",
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
            binding_hash="sha256:c891aeda6999469f5a65b80426f195ae00e1424362522864ae79d1184edc48e8",
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
            binding_hash="sha256:fb9124c6b7960ea698d9111285d9f0ebfb0317b4b520955fb797a1dd479fe8e6",
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
            binding_hash="sha256:c21daf9eefa66a87211e9803c144fae487dbaa8b4685d74ebcecb4cbeb9db46c",
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
            binding_hash="sha256:c64b19191047e7c953a9acd31d9a2032debb3bd60f44268eb0e9059701c21ebf",
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
            binding_hash="sha256:f526937609557e04efa4b20f876f7b9592a675a5d7c8ee620d6446664fa63dcb",
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
            binding_hash="sha256:36dcf6f1cd344d1186bd717442e66f05774267fcd5d50bec9bec065a3bf7271f",
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
            binding_hash="sha256:ee666c2c006452a7a39bd23eb57b62d95a50ca8f715f72129f4a19fe6c513872",
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
            binding_hash="sha256:25dca060e884fb80d35e0ac14ffc30fb0d293d966dcf1270bea930fb07441ac5",
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
            binding_hash="sha256:2da4cb93c93d327df14efc0cc4b608601194bb35ae76f4f24021a05ee5e4e447",
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
            binding_hash="sha256:23cd7471e19397c96bc7e0c23c2d4432f05d0002acb4cc7e42d35d454740e111",
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
            binding_hash="sha256:9e2526347f1eb0b0f09d0ce4d2191d77dd6e78b60861dbd27836bdc298af372d",
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
            binding_hash="sha256:8413309ffad5aa4a07f7daaa974713b6d4ae404050f52e90ed876100f27b7674",
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
            binding_hash="sha256:55771ca751739836e34aaf84b8c7d6ccad20137cfa2afe4fd293049271e610a1",
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
            binding_hash="sha256:2707dad643621e43df85b71d582679da7d94b157619c11979c00cfd85a7fe7e7",
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
            binding_hash="sha256:c7cbb41dd21871063ee0945e71840e0adddc0de902b3756f87e501a0a9f1e9a2",
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
            binding_hash="sha256:f502c13211448860fe140298281e372d9ceb274ac0a247bdd258e0bc5b3b8511",
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
            binding_hash="sha256:5ab228b8d5ad57f4c2bae6b4337460b6a03b2e49f225b2645de3e10a5873d661",
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
            binding_hash="sha256:d56a4e8cb1bf8a072541c95cc6296efd1add5214ac4ce34a9e8458266ab36289",
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
            binding_hash="sha256:68ea29ee300a113366e09d5f419c7b935c12a07d542ba2cff8de6014deb33543",
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
            binding_hash="sha256:e47d626e1b7f30fe3fb5e382ce7fa68784670eb6d427ccbb52981600bb49594f",
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
            binding_hash="sha256:ec2cbdcb09f11e1819851bb4e639dcb49ad27a9915131b4169cb8ce97e0af3d7",
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
            binding_hash="sha256:dc55730bc6254338d51da8f9d64628041eeb631dff3f21d6b9ef0de5be7ef873",
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
            binding_hash="sha256:194b0e8a62623a022a512b9a442befde35f3df9fc3c3b8415b741dee9ab1926e",
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
            binding_hash="sha256:198f09005d77d88513c643aee4f09da1a31efb6929b532af1b44dba3a57b300d",
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
            binding_hash="sha256:625180de7609c7d01d992d929f6346d35a9e79d7fd8838150a3e60331e883f83",
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
            binding_hash="sha256:3199a681440e6fb59c100e866375ca180ab74b0fe972f3f1cf116876ea288ef1",
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
            binding_hash="sha256:bc602da166e70181a3acba996e6b2b930941bb728fda94f9d8495d720551fe96",
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
            binding_hash="sha256:28aa6023a8cc42cb5cc8dc706f250781f2c2ffc9e88a67d59b715631fe2457b6",
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
            command_id="animation.subject.morph_weights.update",
            binding_hash="sha256:f5f41f8bb07442fced2214fde3b1dbe1ae02d52ca837b99abbf8a48b4ae06518",
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
            binding_hash="sha256:8200e39c83912d03dd91ffd13befc8706c171e3a99dbe941b2ec636c5ab4c257",
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
            binding_hash="sha256:74d66ae9e128d5ef04237fd55065843d2e52ad7b36e3e2da5ede064d149f23c3",
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
                    name="space_ref",
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
            binding_hash="sha256:4001e3aa6ad67926174312fd44e7a052fc8e84d613c9de1ce47c594fa15f9e06",
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
            binding_hash="sha256:35b6c3fe14831300abb1d2889d5e1c3b4eb1208be0bd83037353c314c8ee328c",
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
            binding_hash="sha256:6d104e788233668299d43d20d51ff2d3a6c36949d712d00388f115f901cd203c",
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
            binding_hash="sha256:c5e16f8771ed2a5159168b7235aa76fda01239ad070f2e8e19f84f4d79366b64",
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
            binding_hash="sha256:989e4272bf6c7208e20f996ee2262d70e18a42c8136ac4e38d052c1fcdd6fc53",
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
            binding_hash="sha256:01d30bbb776c118b719d1be6f1427c636de83d7c140e8a2952290183584761cc",
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
            binding_hash="sha256:a85f94f1b392a5509b666fc53b430fc18032240768feb98a553d55c7b13b271d",
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
            binding_hash="sha256:94aa0c0a2584889b4b3b4732dbdd7a4be1cdd809ec480433e2aa8c5308191c6d",
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
            binding_hash="sha256:bac326a3752ba2401c49483502960d6654423023c55e98d80c7e4cf81ce4bafc",
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
            binding_hash="sha256:a748b1108b63a7919c14a01afe44d3afa738626d160d31ee85eae50f0d1203f6",
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
            binding_hash="sha256:f1f0603ed1c9fea51bc5b7bd59262ffaeb6a58d1acffe673d27831111c69db41",
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
            binding_hash="sha256:b944d81e1e09c0090f08653106a97dc99c6be8e99bf63847d4228a74418b2966",
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
            binding_hash="sha256:b662896ee45ad97de6fa8be04084fad1616fdbd1bc1c08d155acabfd99bbbe0b",
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
            binding_hash="sha256:1f6a8769876808614b2942a49d13659448feead51ce5187ff87e3ffd219acf5c",
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
            binding_hash="sha256:ca71679177207c9fab17cfca16e06e47bc17a1a36653e8873e1da2cd60ff60f3",
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
            binding_hash="sha256:9612f93448565121cd3d35a0a8ee08bea7e7b1934139e874baf37311cf0c231b",
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
            binding_hash="sha256:400bd92654e69d60a2b1528acacb596a9aac43881d5d9931ef865130836fa8d4",
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
            binding_hash="sha256:0e28a51a63aea556bc85a811efd84ad32813192fc1d0ee72d57618588faf78be",
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
            binding_hash="sha256:4335ca0b302c11f2eab65d607adbafa7e8d2e7724da9c4715201bd213a12aa9b",
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
            binding_hash="sha256:3fc69834b9ae14ff78a901220f1e83be8c825fd9e465b9474b5114b971b1a4c6",
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
            binding_hash="sha256:24547e933adf363b5b5b740c5d948e27f5cb82656e9b4903d20743ab564c948d",
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
            binding_hash="sha256:a9fdcaae85fe55891cfe6df9efa2c26da550e0108fdcbcab71f23170cca879c8",
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
            binding_hash="sha256:7fd21f68b58967c33800d783f570d85b6e517293d07cab0416f740df069dd7a2",
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
            binding_hash="sha256:69762e88f0d788f1a2b894be3eabb96f9c8a622da9f22f0ddaf5567a288cf9e2",
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
            binding_hash="sha256:ed2fabf4118a7b65c3bab3ee01c0c75282719a8defd1fa233a454fbaa06fc10f",
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
            binding_hash="sha256:14c18578af5ee2c7286e8d577d2cb2b0fcc1c3c4b28b5c293d8cffbd6d662138",
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
            binding_hash="sha256:32d1881af1909484132c0c7e77cd11c51a2e85d18b790f819c55953ecaede50a",
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
            binding_hash="sha256:e89ea24c524e8c8c628395dca30cd6b1d8f5d5fde771710780262dbf1930d20a",
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
            binding_hash="sha256:17062d550a32c907de095b5f4dfc0660cac31a143a46ef4e45e392f9bb7ee371",
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
            binding_hash="sha256:df8755c244fb0fb6d82c9a812558007e051128e47985ca7153b0293caf2e7105",
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
            binding_hash="sha256:3773fe7145e2adca22de6e9665177f5d37f03c0bddc019dc5f1761a09ef9ce8d",
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
            binding_hash="sha256:e3a36043d31e6b4346bf268faa958f73692d10b328dc8bbaf3e8871737bc2d53",
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
            binding_hash="sha256:4b7d0053510499a4dfabcc26c4ae92f6fb7e1ba62e2ab60d68609636f5b22a0e",
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
            binding_hash="sha256:81d754593776cd3405fb98edd6b54326c32f6e351e27dc9062abcb9757601de2",
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
            binding_hash="sha256:65c954693d077114e7b5f963cd88c4f7e41b423c6de637d32b04151521cd30ed",
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
            binding_hash="sha256:551b94c9d42aede64dba50c528868d6aa217cef0e9b23bdd7cec9c60ff90cb49",
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
            binding_hash="sha256:51558add543f8daedd26eeb163d5e1abfb7584e912483ed8409669992112715f",
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
            binding_hash="sha256:3cc71a852ccdf40e5521d6ed3744dc480f994d7530e44eba572745536e60b2bb",
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
            binding_hash="sha256:b98bb689e8b558fe16ea2d52d980eddb033c2c951482efc433ca96b9ca5d3347",
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
            binding_hash="sha256:6563ff78ff1c730a60ee00f1f0f3657eb9eebf1efd8e0e6bc15a076177c38ddc",
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
            binding_hash="sha256:c4fe1c3531e28accd8917cdcaa9969d08f1903ccbb6117832030be0e8711e1fe",
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
            binding_hash="sha256:9e1808a74d9afbe7c8fbbde6477ad1340677827557563af127e0892ec62df6a2",
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
            binding_hash="sha256:798f298eac50a02731c90a81f26ea7df52497a4089a1c0bef43f9a40f6ee095d",
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
            binding_hash="sha256:7dbb316e82d7c4b1a0cd0b9576f32a3a5f6bad327c1e564769e3a64ae08a1d4c",
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
            binding_hash="sha256:5acc0af3252e9ecc955127b8d3e77b6d5d78501eedf2863a779993d4d96ae664",
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
            binding_hash="sha256:7c868b8c1de1c9ee70a67be3be4ba77d0c81f37be834d51023ebba581c03e286",
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
            binding_hash="sha256:a419b0ad507a9492f996e78e62d2eb5e4407aa2a7b1035006359816d4506c27b",
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
            binding_hash="sha256:3a30afa3b49ed2a33a50b1f8521a3a72a7b5d189db6df8be5b78d8edde799e9c",
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
            binding_hash="sha256:9f2e9d15bd1522e8bc425acf6d372eb831f88747aa077b0697b95394895be1b4",
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
            binding_hash="sha256:503316e0ca55ada350973e92d71b93f87930e459c8511c3f8e9205761b1c9178",
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
            binding_hash="sha256:cffd0a00e1dd740f24d24752f2de4e29a7932de01a7b93a9641f63f4ee0cae82",
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
            binding_hash="sha256:091f27ec3776dee3ae11b0b8ec7c1de7ff9490ea2ed8bb71e5b5c9b5f97aeef0",
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
            binding_hash="sha256:3b8c9ea5dbbbe05488a208bbaf6aeeaffd44222839b2605563b2d12e4a9a0241",
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
            binding_hash="sha256:65d817e2c132b62f6debc16cc1425c42c31966649f6942f0bad56b49b790635d",
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
            binding_hash="sha256:20df972a21626ddd2671316e1e3b4dd30737eed8609d8f904c2e3e05d56fe0d0",
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
            binding_hash="sha256:e4dcd5f9c889a6c250a31eb7aad08568cd42fa7a331b8c15fd5fd69b4afb53d9",
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
            binding_hash="sha256:7c1c81654a79423db60e29c4ccbb865b53fbb4ab4dfa6dec119c30de28f1099d",
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
            binding_hash="sha256:e62387a929d5684ace3842ecc6c7423532dbafc49ec73152b8872ed52b52daae",
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
            binding_hash="sha256:99fb6a71a35e1486d531f01ad18162bcfa7ccecfc7bb334e6851584030122367",
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
            binding_hash="sha256:34aed10ec26e2225102d59eaf1ac0ef9c2020ec991df3bd334896aded0899b36",
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
            binding_hash="sha256:3d241bad0a2d2f0feee4218954d24eedb75a481d6077ec6d2aa85ec94db5d342",
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
            binding_hash="sha256:9aef718a441a3c10f9a52f7d5d6f0b4aabf3b316ce5665b65aa087ca46e154bc",
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
            binding_hash="sha256:9838bd36a804f578f0f50a1aad824cac381010f5c7cda68c6c66e952eee23a0f",
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
            binding_hash="sha256:8c66896e2459d9a2e58c1a4ac78b34d8c4e9770e8726e60ce8e3310d78210363",
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
            binding_hash="sha256:b02b643f201fbdaac87908deb4e52a21fd6fc71799e6fcc990decc823abe57c3",
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
            binding_hash="sha256:0521396c3e18fa804e89c33a7fb8dd9f71fac011a04393c998fc8e7d522ff2ae",
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
            binding_hash="sha256:aaf8fc7643cd3dce8491df12790e0ff11347634d106e05b1af054535ad1f2f07",
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
            binding_hash="sha256:0348d3161708a5250f2839e776134e5bae3ba4f41a430f7cbc83b7567b04a291",
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
            binding_hash="sha256:26c52ff01d6c5cd230904a2edfd1cc1b1d979ec2822e4546fe3222c7319a337e",
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
            binding_hash="sha256:e252bb72ef40d6780901c824fcd37933b7afa07119f84c3e5f4e7234ba005125",
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
            binding_hash="sha256:3fee929abb997b9b5bf9b39cfbdb2d113e0e8dcc632f8bcbce6a74da47e6fa7a",
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
            binding_hash="sha256:63e00dad492a215f4ed9a32f0fcd0692fd0225b57385b251361b224c393e6597",
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
            binding_hash="sha256:93b77ba7bfd06d2ab022c758db3ae90af6f42974f5253a287528c1b18a80a796",
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
            binding_hash="sha256:8ae68e414d34ce97c616369ca12fe7b95d70f4a9132ddf1b51c8abccd3397cf3",
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
            binding_hash="sha256:cd3653ed504cd8cd478cb1d676cdf4b29155edfa7281a90f579928076f23f8ba",
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
                    name="component_class",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="requested_name",
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
            command_id="blueprint.component.events.discover",
            binding_hash="sha256:ff643b1c1311eef19b1c55755327b908e0a6184a31cfd4dab85fad3defe93691",
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
            binding_hash="sha256:98d4e0a7c21ccd46f42875166886c6f07bc8932c58ce7b381f41088027445558",
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
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="capture.image.execute",
            binding_hash="sha256:e8e32230712add95a27c1399c4146b6a13670a8b1b2c0a9487eb58c502fa36b3",
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
            binding_hash="sha256:7f0cccd504825fd49b00a28d84e466828549fa4ce77f71f403d11ce4ed6d026a",
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
            binding_hash="sha256:3cc3c1c86bb5efdda7551bd63e92b7f92f0110a139577138f8e3e8ea4f148663",
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
            binding_hash="sha256:ff96596da95140959275a5193282bb4879bb56fdbccf9c18a616097af4ee275a",
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
            binding_hash="sha256:11a8d0958bd623da7b9649a25e6d3e9a434f7e4c7fd78280a45d1ea3516bbe76",
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
            binding_hash="sha256:a9aa7c017b7edb1f19509019998c01633786168dc2ffc1a737a1e9b0f30bde80",
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
            binding_hash="sha256:0cf5a46a482db7d71f715002fe26c1c600c5a3bf4291328ea873f611a90b3eb9",
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
            binding_hash="sha256:8d42bbe76f7ae476328f0c873cd55b98cdbbbd10533ff6d83215f35e32f230ae",
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
            binding_hash="sha256:4117a13cc08abbc40cfe36c4bb062b604ba598e982a9893fcd092d12206be1b2",
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
            binding_hash="sha256:d9f2bb00c671fe54ad15b45f96a29a05e5291808d76f528dda39986282ea9b43",
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
            binding_hash="sha256:46149d5c4770cdc2a9acc23298564fd2ca997d0f3dd93168a4a069997ac7ec16",
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
            binding_hash="sha256:4b59f653fd063a5cb70f5892a7bd09f8bae833eb0058de6f013818c3c0d41964",
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
            binding_hash="sha256:df4087d36a0aeca2d49b66a86b9a1485c7b351a1ea92316a0c8dedea7cd33d94",
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
            binding_hash="sha256:c785378a2e94acde49ce8734534e04718b46eaabbda4058fa63c74117dc529e4",
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
            binding_hash="sha256:33c332bb2baf050083d46c984f7a334679c3c9ed69679cd2d46a4d74df0fda3a",
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
            binding_hash="sha256:14ede0954ecc6038bd934b8fae524e95655bfb8bd108e220a1af1305d3faa060",
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
            binding_hash="sha256:76fa4fc6be5825d00144429e310adfbc573ee5d9b49dda0fd2318ffedd9c9e23",
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
            binding_hash="sha256:2319dff88d60c5845b0f65a8bb3c3a7e1e00fa083da990c78f0de7e8bbca6d8b",
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
            binding_hash="sha256:18c25fc0e040a26220d20a681b1d6acf42434ff0a78203d568b7199fe77158a6",
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
            binding_hash="sha256:5debf213cb1e11de713a815e9a005e8a5d61ec0c21333197b9bbfcf6e10c4a6e",
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
            binding_hash="sha256:8a98b62ab9bf6b2faf1501ba93ef5b7214772a28ac3907e1b70ad358f64f517d",
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
            binding_hash="sha256:ea257355420f8fe5197030bf5ce9a141e699830772cd2446ce716c85335b4f37",
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
            binding_hash="sha256:62ecbc12372840264e1a01dee66e597587a213b3f32af929fa959ba0ea3f1e6d",
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
            binding_hash="sha256:e1235139f39c804254e5c8812b0e68b7a79f394afd43a3aefe6cd096dec0d0a6",
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
            binding_hash="sha256:6b9ddce1396a98d254e563247ebbca4cae7bfe87d2fba55a2b477f43746fa210",
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
            binding_hash="sha256:2617092f713bbccd99613016076111b8713aae002bd3cd3246c7a5aaac7e9cc4",
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
            binding_hash="sha256:3e0b0d21cfc96230bc7ba83f4e704722e24a435ed61a260addc060ce1a037aa3",
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
            binding_hash="sha256:8168f8f660c74f8b35ddf8b05b8ae4ad23c0cf9d054f8470a883ca2cba13f302",
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
            binding_hash="sha256:c8aa83ed2db8e991fcaf1ef53f3aeead4a282a69218a41c46583f2518a8a4c3a",
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
            binding_hash="sha256:e5f598c771849ebe1da07e53b1fa4c6608df1c507d6c628c571d3667ffc6e7b9",
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
            binding_hash="sha256:94475f51d3e9ae0e9288de2c9cc7c602978e9f72df025e2600a25f4cdbf43611",
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
            binding_hash="sha256:7e644ab70183e8e466efed3e3ef7174b64733c4eb30cbc9ef48f043490fa8f2c",
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
            binding_hash="sha256:8c16f3ad2aec134df541fba60688a551abfab42887e3b38462dab74cfccf525e",
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
            binding_hash="sha256:75d21efbfc6a9afe9089c61d6b584b448504d6e68ea9b393f9dd04dbdb746c23",
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
            binding_hash="sha256:0a17d19b47e9879a352b94baa029ca2d5086d44486cdc926af591cc952934443",
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
            binding_hash="sha256:ef388f98b96b9ee9357df9388cf51d9fa9e7e7a0f4d90ae1d6430510d3bcce98",
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
            binding_hash="sha256:4c4b6e523c22a46dc689a9981fa9724dac97611414cc67753cf38ff4716d7a27",
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
            binding_hash="sha256:f3fef6a3d346d49b966782ea9dd417acaba4547a06d80fd2610794bf797039d8",
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
            binding_hash="sha256:b991cff2d9b8a2bb436a8da7ac33de5091dbc3f074e277a41325343519169f78",
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
            binding_hash="sha256:ed36413dfbfd70779d28aa6783f04186110a20772247b73673483aa4c9a26e8b",
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
            binding_hash="sha256:d8e441ca867f93ca4a0d2ba201a47c516764141b347e7e2ee81f629b023213c0",
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
            binding_hash="sha256:b1519970de40ca3b656a3a66b49a5fb5785589cd2ba5056b949d828993d3c79c",
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
            binding_hash="sha256:a003b0a1a590bf2703fb64f130b54b201dc17b53bcb11f6cebd664d2bced4871",
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
            binding_hash="sha256:b88b72bd3132c728b920a2360ec61f3dcd92ff2f5a9a55d92930ae5fa2cb812e",
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
            binding_hash="sha256:61d4d61151d2f14e451e752efeb9443f6970c5edcb8adde2036355a6412c9b34",
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
            binding_hash="sha256:9c49740b66525888280afaf8f1d1f8284efbd7b435723e2010493a8a59507c7e",
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
            binding_hash="sha256:b65d94bf9979ec25e04f745d58b7c2013db217b21e3cd4a89b07c7885ae7a6af",
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
            binding_hash="sha256:0e7638612644663ed3a256eff4ee16c79539fbd6bd8bf8f6b0cd3eb50fa7d6e4",
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
            binding_hash="sha256:49d0bb907d4c18c281211969c1545be7205f9187d6efb889de4012ef675c4e3f",
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
            binding_hash="sha256:774ee2b3e47342fcea1b75e37242d1dff2832a9dff1e9a3fdbf0e3f49c9a4f29",
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
            binding_hash="sha256:357887f9beff111b67ed2f8133b50a92833e2cab7b24dad21caf0ddfef6b3223",
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
            binding_hash="sha256:7f7cf258fee34cb973dfeec8063c7c061b8f86c7cdbefdd5b298819b975c6d64",
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
            binding_hash="sha256:625f66f0fc7c06773dff2ce97def6052547d5c992b4903e9cfc488ca873221d7",
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
            binding_hash="sha256:a0ee563116eb8e728f8e5edc07f0fc77325a44b9598a68004d9ea5594ccf4ee8",
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
            binding_hash="sha256:fc4c8b7c60d608f8d651f9f922c0e6572b530d21092a70d6dbc50e725803ac8c",
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
            binding_hash="sha256:4cca9d65e067cf4fa12d27038500b1e98642120113ad07e1fee86240f443163e",
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
            binding_hash="sha256:75a1691a758dcebbcfd29441842b2de1ce25d1d4b2d54e7d74a6c09e098b5f93",
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
            binding_hash="sha256:ae5c1733601185084283d58d52538db28163cb2d03a4cd531417a5e4db81866e",
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
            binding_hash="sha256:b3d0a641bd2cbc5f3b908c88e44c5ea689ee11a84df87dd24705001619e16cbf",
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
            binding_hash="sha256:bb4a2c973914bb0a3fc4191f91e88f98451a70c1cd6da604c5d9334bb01c82bd",
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
            binding_hash="sha256:c2720be15240423ab2bda59a15cf5d5dccf1fc7d8a53d8074135e95509a8c248",
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
            binding_hash="sha256:a180dcf67845e424898cd9eb0de6de6bea43cdbdc6699216187307e5cdad02c5",
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
            binding_hash="sha256:103525d4676cc66ac0888ce3a069f083c43a985e13f7397cca6f1b592ad830b2",
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
            binding_hash="sha256:a9c17dabe26125cac9da32510e8379ad68ed27a88198673aae8298fa7d33e78d",
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
            binding_hash="sha256:b37b2513b7d8bb82dfdc567e4d6e9de01972af78d0806bdc4f43677771efd035",
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
            binding_hash="sha256:2f9cfe1e140651a97204f08d77aee76fa7a624aab1aba8a4d572b97d987843c3",
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
            binding_hash="sha256:73d941434eacd86a2d5c5fd58e67d6510c7e3421623cc0cbf889dfda4db5a761",
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
            binding_hash="sha256:04c63aff94768551de8a89d932ac618fd48b3f48d9e5b24ce47d3c319186d219",
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
            binding_hash="sha256:e0b3f7c50e7d44ecc206b3596b63b5da74b3f3c89a1e9257dd64b46a6fb3ec95",
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
            binding_hash="sha256:e57710ee7cc3286c18f1986594e97bc0676765eb55c5293704364ec07ed68874",
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
            binding_hash="sha256:624ebce4573bb1b34964f161947e29dd99f397a09b61000b71a1836b6c681ee9",
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
            binding_hash="sha256:aeb382bc86a5e1d5c33b8b978459086124a5671e14cfc0c53674f95da8af0c29",
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
            binding_hash="sha256:eda73907fde60be42cafbab4f63d6510369ee83aa3d6c3aa100de359c15c5b93",
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
            binding_hash="sha256:0013707989daed85280e4a93e5ac9151910449aa6d6d90f5e7dc9f6515ac4e70",
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
            binding_hash="sha256:11c64b4c9593c6ade1e1026fcd0db43eb85d88f135683ab7916fce04084e1206",
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
            binding_hash="sha256:0474d98b9dc3d15e48ebd0d76e237a03f99f8f61a565dfe4a0b03959385c4ccd",
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
            binding_hash="sha256:691ce5e7230d0761085dcc76615ab8e3d467a1643d7bd8072c4518653876da16",
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
            binding_hash="sha256:1aa0e44c972bb7eedac805bab58cb3cec2fa22e7d1c0a2f0147e24eb6923c1e9",
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
            binding_hash="sha256:e7754354fbf0d832c4b4929b6d2f25cc3f0f0f00d8266403ebc2a3a6947dd396",
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
            binding_hash="sha256:14dd09ff028cbc0f41b6013ce7840b51963db306a18960576e479a955ef7354d",
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
            binding_hash="sha256:09417e8b54e79f1b8de227af8ec546ed7519e7e8df12e6e3c7f481ddb2201f92",
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
            binding_hash="sha256:48cb07140c78f39b98c5729e6753580e81bed6b426fbf587f045dea0cf0379ec",
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
            binding_hash="sha256:1640d3e4a61df7a4281af1ae0c8966c25d3a4e2667f6ef53ff1d4dafb46159db",
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
            binding_hash="sha256:22ff6acfe9142f130962ab4e807845785f3f0c4f51f56f197955fa069f837312",
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
            binding_hash="sha256:72c7d20d4362b57e47f51fe84c3e0083c90b2fc985baab425c1acd86045595e7",
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
            binding_hash="sha256:00d848939886752ac0bd6a716f5bfa340e568bd9a0f43b3ef9e12a32a755bb1e",
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
            binding_hash="sha256:4db44a29632c296ead66d97c7222020da5d110b6c9beb2c4193a3ece57e08564",
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
            binding_hash="sha256:99edcf22eb94d749faef9d7973802d8f3313b8b43eb3e826cd954081d4b5fb89",
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
            binding_hash="sha256:55d9d3250bebaa893edfe9f890ebdb978e1c745c4f2a3a87712a7eb53e14a9ec",
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
            binding_hash="sha256:4626b5d4dfebd65fa9a1b387a0a191fe94dd027cf8e47fb78e234a0a42018a15",
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
            binding_hash="sha256:e910bdfeb26d2bbf94c1e4227ab617f2d9f39ad2ec8dc19c6293477014e85a7f",
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
            binding_hash="sha256:6d354114b9621827817d62430e2381a371087c0746c2dc7c4c31e876fd2cd4a8",
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
            binding_hash="sha256:df16d8362e83ee6b5c29e88c093e71414b01866e47ce41cc3393471144bd68b8",
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
            binding_hash="sha256:109691c674b438cf7a3697191d1d0fd78d74765862afd712a724d141b82ef540",
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
            binding_hash="sha256:eb91efab83586601733916cb2c8d5894124491bd698bd0e2ce4e1be4086ed8e4",
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
            binding_hash="sha256:a166a0123600c72494c708b4da85ad3c5e8b348d30403df44820ca0561c9bc26",
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
            binding_hash="sha256:79ed82bd8da201d5b7f46be462e2412df1acd73d2d52192f29dc291a8d548a72",
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
            binding_hash="sha256:2bee4970990b499edbe221203e876f46c0ede84bc2fe99151c27847ec696861b",
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
            binding_hash="sha256:ed15c256adf236faa01956ee420422b8144562aa40540bc925ba7cb197672260",
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
            binding_hash="sha256:44040363152c6e10007aaa09c6252ea54c1449c768a7569f99f8e501ef52227c",
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
            binding_hash="sha256:1181e867d319f3be7ad6a82a2e7f25d3b7829b731cea1fedf50cfc551c1e0466",
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
            binding_hash="sha256:941159e5a1d68584f7ef367a17a7b4dcb89591832da4a4bd69928d725cab7090",
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
            binding_hash="sha256:c56767887d0b9fb0f77ab1e2319e8deea49da721306306034cd0d1a737394a83",
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
            binding_hash="sha256:ce178c79a9c492e4d78599216d0cc4f8444933148748478f1bddd93a40e1692b",
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
            binding_hash="sha256:c07960961cfea4c21893b4300fa73fd6af81bc3faf858ef3bb52836b6b9b50d2",
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
            binding_hash="sha256:1ecd63b3075bed22fcc4ef4af35c5636d9bc77b9466e1ba19b105180d6f6ee2b",
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
            binding_hash="sha256:44c2cbc9a8e7935fc8261005153b072835d51f47ce8f3969434a4482445cb1c5",
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
            binding_hash="sha256:749b6a3c99830f45a5fc26650741039d1778091db825264a896f3baddf8b6cc5",
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
            binding_hash="sha256:09f66735183cd63160f6fb822f73bd72cc12115a1629e766180a259afec10fde",
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
            binding_hash="sha256:5a3c53095b0b7ad3357df0724faaaffed355d381a8950bd48a8a6066a40b17f2",
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
            binding_hash="sha256:62c99562f5a3cbfccb456b49d63e96e5d324a70e11b4ac4a4b7a0a169e43b794",
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
            binding_hash="sha256:01d6476f6aad8537079dd8421d3d8165db690ea897ce32c695c388835e670dba",
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
            binding_hash="sha256:5b9c39b530c9419a34ec2147acb16f2d0113c6f99840bbdee5d8a9e5bfddf8f2",
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
            binding_hash="sha256:1c0946b756245b6589a8fbae96ddd7938d6c253b715f81040e6fad3a0702a24f",
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
            binding_hash="sha256:3ff02049506fc10dd60b4d3608372c8b8d4c002d1065bfbf5f9f933362e53265",
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
            binding_hash="sha256:8d004e20770c32376b1d75cc6349f7f0c56687feabbc9e0533f77ee5f83522fb",
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
            binding_hash="sha256:d22c39cf57fe791bf97c89c4c21542df4372ed475d8bd6952b93f9c309e1054c",
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
            binding_hash="sha256:18656cde12f0a8043e1c608ca0a7df57e9165b119878719956e427e8eca89251",
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
            binding_hash="sha256:3e33a1676f758b46298cf911925a237fbbb0f692bff96fc4c6eb4d900012d035",
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
            binding_hash="sha256:865c11d49bf9a4ee9839441f8abee5b53b28882172bc62f91ff8de40b7d2e191",
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
            binding_hash="sha256:c7f5bdb2ce728e34a77c255042385efb2a4dffd12730651cf44d238239968d19",
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
            binding_hash="sha256:2a1115d4ed60a9b1139278a0bd17efa6696d5a70c7b554e8f05462777f7267d3",
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
            binding_hash="sha256:3f99330341f5a76d81adc40116a08e0478f228469fc9016bc946ba4ad3644028",
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
            binding_hash="sha256:508561028d8e68b64ef2490832f569d33170cdaf70b8dd21b1159629d8a1f454",
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
            binding_hash="sha256:5c5c67c13d23b0d3bc921a5a9c7992cb6ac980400964afcac863c89d14e70da0",
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
            binding_hash="sha256:3ebbec2c81a8f5dd9d89b4836130db1ecf564efbdb9f4b119179d7d02b1449c3",
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
            binding_hash="sha256:5ec87aa66abb4007be84840af717fe29c67e01fafd3f00dcbc865ae447052f6a",
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
            binding_hash="sha256:39310c674fdc95e7180906fc4d2296f2e2984d7ef243765e6d98da2927fbc28e",
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
            binding_hash="sha256:a962de3f7ab01439288a414576c87b27062d7f7f2d4680b4425206fef7f10791",
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
            binding_hash="sha256:abc22e1c26892758d80b64e25d0ff1d7a20fdcdd0e7d55c844918c581a6edcf3",
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
            binding_hash="sha256:0d0c867beaf6ec8180060843dae28fc1e5a65fe0c3b71b1e87c3525238f78d46",
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
            binding_hash="sha256:3bac8ef382dcd4d6a4c631d13de0ea918569f4cb70fefee3ef08de16c30d1349",
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
            binding_hash="sha256:e40bc15770b133639104ab89bb09de77c2a19f3a84985aafd02713c3289f2765",
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
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="query.command.search",
            binding_hash="sha256:5e625c558e8ada9eb4e18b1491d31c76c2f4335c52120345ed483e89563787d8",
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
            binding_hash="sha256:0e6693e7b5c5a9628675f13cacb61f6728a2d73f691858a6ec5d4b6459aba01b",
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
            binding_hash="sha256:0d4a782d8c0174a8ef81edb26bb62bff59e9fa83d098b05333793a4d0c83c088",
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
            binding_hash="sha256:75bddca4ce64d3c49d0d87b254bdb40457900336f9b1e79fdc4d829f1398dfdd",
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
            binding_hash="sha256:24d83481ae5d6f6bb0f3064d1aad31732ec25a7dc9f30c348c28d8e0f59d6090",
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
            binding_hash="sha256:028306f82acc6e306c3e02fce562ea50f64f12d5411eec9ec57d056a04c0e4e1",
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
            binding_hash="sha256:45f1042d61532cd0955f1bd3ce7a77dfff7dddad4e572a09ff0e999265e6ce07",
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
            binding_hash="sha256:c4f67ddaf04a0587c2e46f15667ff98598eac03141a56a3ede02f794c29c1433",
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
            binding_hash="sha256:74e2abf121755fe9f6bfa3ecacad766f706985698ced5fba073954b94b38b58c",
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
            binding_hash="sha256:b3419ea84c92e29072884db431f86dae9ced8d358c3a0e3a505e44c67fa555ce",
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
            binding_hash="sha256:5d282e8719a6c12bee9dcb2d1276f028b155f4d4443eba56eb873aef0001d5cf",
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
            binding_hash="sha256:103213eb02f23458ace453e7929afd0e95921b84489612f0bfc75c1740e63f1f",
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
            binding_hash="sha256:c3bf16eed5078e46d80cf3d8d1d397776b52563de8ef2d73308d742199309d82",
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
            binding_hash="sha256:f6326d2d8599a21bd17d7f7f6fb24fb5467f428eab477f8912888d9e500db579",
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
            binding_hash="sha256:42387c91e71eb0038f4d2400a42f19a27cc9141fbe0d1c8ce6786646638138ee",
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
            binding_hash="sha256:6bcd3d3ca2df2ebe5512778f4b13d174ec1f8b21047b14e0a53c3eedffa60d40",
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
            binding_hash="sha256:7b93d1c5be1818c9fa72cb9831dd4c67ed5e006c2265033a5acfeb69938d26c3",
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
            binding_hash="sha256:39c194b8e91624919a68b19343efac0cf5616b0a072dcc9556ad8b6e3810b4db",
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
            binding_hash="sha256:2eea2491a3e26a92f37c088e04bade6e7f2a070edf9bcbe065ea204d95e0dbe4",
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
            binding_hash="sha256:dd86eae918f4573483daeba2a018a26d320e742126026661548945875a523bc2",
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
            binding_hash="sha256:fd9ebb0adf667f930eb345febd3e315c420925d061080ad89edb6d55a02cb2f2",
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
            binding_hash="sha256:7208eab37f925347aa1e05990b0aa95210ad89335b7a65a1ba62b277f2734cb9",
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
            binding_hash="sha256:66a278e1d9338ba40f8db312187e390b9106af80a0a791fdd23e1afd9336e089",
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
            binding_hash="sha256:51965aec401fb7c374afd355029d5bc2e7df6cd4fc604cc352fbf7c5cf082c05",
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
            binding_hash="sha256:8fc062d0e03749922d91741fe3f0bfadfc4ca8eb98d975b239af9d9b16785b10",
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
            binding_hash="sha256:1c4e2bcadfe5a76e103dbb50124ad20c029b2fb71bdb198678d5b1e8625550d0",
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
            binding_hash="sha256:83b1e0bb6a31b110e2bf500e2469458e436f11a17a14477875344a32f1e07433",
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
            binding_hash="sha256:d759133c3d9049c9360b56d0b8fa5f06c139296cf51a59ca281fdb8c0453b896",
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
            binding_hash="sha256:f34bb4235c24ccb37f413dc48cad494a613c9bbc9858f14466dd2c59353df496",
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
            binding_hash="sha256:23fb13e38e48d55c84827028ee7c3b27c532c2b5878e8cda6f707a05e6ca9269",
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
            binding_hash="sha256:9d9ba71e5f2dd710badaef01c599898f179978110e48cd48d3a38e3c938c8e5b",
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
            binding_hash="sha256:b93a77ee478fca8cfbbbe7ca4521a16befdfd0eac666e63dbd2201c54a12723a",
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
            binding_hash="sha256:50057ea65d4f0b50d2c523eb55a1d976e3a4232917ade1d3ebdb464c67139a30",
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
            command_id="umg.widget.events.discover",
            binding_hash="sha256:47a5e6b6f4e24d856d9521e2a3a0d480f28652be6f3cad018d034e4d686b6119",
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
            binding_hash="sha256:cd1a55cafa731168c5025b8ba1a558729493b2241bdb5eadba75f1a20c7829bd",
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
            binding_hash="sha256:bf4c48300886648fde81d1d84fa9530d7585aa79a88a094b1623fed760d0e8ff",
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
            binding_hash="sha256:9006f06a10335ba5bec5ef023971480020915011922b2cac528763d9f7151ee3",
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
            binding_hash="sha256:d562eff0df17039f64b1281725b417aaa92f50592ae8bb499cb24a6b80d506fb",
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
            binding_hash="sha256:b9d3defaddf142ded971b241834b89558964e0b55d65184c80190fc383146674",
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
            binding_hash="sha256:0dc218b25c6b39f4d77af458b5c882f3192c51ce38fd52e2b711dcc7241582fb",
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
            binding_hash="sha256:e4e0d7b12efbc87a2ef6d2e6e31572521f7db100a6e116563aecdf08a9270082",
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
            binding_hash="sha256:b024c444bc69d92c6444e1eb47a0790abce3fd460cdda31e5cb5dd8889cbd646",
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
            binding_hash="sha256:db6e8b4b225bb64429ec2cc58ee92c81118d049eb58c74c610e53bcf2cc37657",
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
            binding_hash="sha256:83f651eac09eed1fe369ec86ee3f08b380e620b17672b73849279a857c596320",
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
            binding_hash="sha256:a29bbbd21fc4e59fdd818c48062846cb020c30c5bca3624b313984be5919a4f9",
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
            binding_hash="sha256:8a7270d19817fa39ec5068ec6bb88af213dd9309cc1017cb2005b564f035ccee",
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
            command_id="world.actor.create",
            binding_hash="sha256:5b8dd511f014b63793d8b6e41dad99158c2ee7d3f42bb6ff76a900378dc3578a",
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
            binding_hash="sha256:2def85c5ed7ae0f04219fa9d7f24aec58daa9c5a9d803fc236e8abd7af159bcf",
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
            binding_hash="sha256:e6116202b148689b84adb2623977fe5aa5a39c3b05bef4b676e20b801b64c064",
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
            binding_hash="sha256:8883349bb580b5573234b41e437ec47e6caa3acfd55d94bc9944a30bbcd936aa",
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
            binding_hash="sha256:177fc9deae0b2f9935cb8877d2197414945a413e40e1a30fa09d7ec5a8796947",
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
            binding_hash="sha256:6048373d2caa701640eb578029b19c0c963d891ec160f0c1d4ff7cba34756335",
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
            binding_hash="sha256:49c67baa586302933ecefc4aacdde50df59437e83a38b83c89125cef163292fd",
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
            binding_hash="sha256:7190446e9dab341369c38bc61567f86b67d537f53811e316335509eb8988ee6c",
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
            binding_hash="sha256:370ae6c2ed45b661e11954788c5a87384ad36afc24a1828b7500640bb6c555c4",
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
            binding_hash="sha256:0a4b003217733c692cf9405303313413d77893ed589f4d7cbe7d9a37b9114057",
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
            binding_hash="sha256:b8815e5fa0ae2ec1c3a7c65e35f6fc23e0c1587c16c6a04bb3ccfe4125de232f",
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
            binding_hash="sha256:53fe62afbd849ec8d8e129a96e8e2b4f6f3fad383798161b7f79285c31714860",
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
            binding_hash="sha256:d53585d3f52ee86de2f74e266825fcdbafcb38f99482085fe6c6765bf0d04952",
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
            binding_hash="sha256:0f1aaf9719903990fcb57c49b5d8a592dc263bfb79751e018eaf2c46060ca7db",
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
            binding_hash="sha256:f99c5914309922974a8b234c0f6dc43d8db79788554c41f0f560060ece282f67",
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
            binding_hash="sha256:4559c567d0b55bb8e6480823fbcb414f77ce3a51b7388b9f94f782d37d540e89",
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
            binding_hash="sha256:1d38a0fa3169876a7aadce0005d1241279601718dec76282c404c8a5e62aab97",
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
            binding_hash="sha256:427ac901063c1124806f989d76279139a9c535ab596837e43e6c16fc84e3f3cd",
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
            binding_hash="sha256:abe5a67452dca18c455e7c67bab1b82c3f437baf00104eca8c6350996d346eda",
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
            binding_hash="sha256:381930977295bbf8305bbeab41c01fa6a2ae090645c06973ec63f239a66340dc",
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
            binding_hash="sha256:0e9a6bfeb044df1b54fd4d88f010d5fe7ea880aa99d774f062e8108c9df360fa",
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
            binding_hash="sha256:16b78418b1762020fd1c8914bd5c4fe619662b3649702f27a6105bed14e0884b",
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
            binding_hash="sha256:bf1cb629bbc59856006d787cbe78e5275fc9025ec38a5dceea1544fd1b7806fd",
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
            binding_hash="sha256:ade51fbb48ede2dfa41f30db1e4e4fbd7c033a16014709afce28f9b4e9a7b981",
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
            binding_hash="sha256:e515c3a07e041cdaf7083b16670bf7bd767b6cd66518f5f05e6f37afc9c66ae9",
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
            binding_hash="sha256:0f61d5bc08afa1adf9f195d81242dcac059b7fd56c75de8de377a6ae2c3e4618",
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
            binding_hash="sha256:9013657da56b5a062235b5e7d5b51926c61b3773be58d0feabf26379ab9895c0",
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
            binding_hash="sha256:6027d967e1f58049e528fd3cd86fda59fe90c9503087be5fb3e3f0d4ad8f7d54",
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
            binding_hash="sha256:2ac5bc02cf8748636de58d9b4d51198d3008dec81f9ff03f8ba70fc421be404f",
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
            binding_hash="sha256:50b1f26bc7fc740b59f12fffdefde9b53cabe251cfc43bea58c94e78add0cd36",
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
            binding_hash="sha256:6be67e05afad203c9f992d17f62d4b64294e26f9fe7f7fa3cac0bf60f6c03a09",
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
            binding_hash="sha256:d94ae8f822678988fbd6583fcd676fd7f352c7e218941064d258569b2d41b0c4",
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
            binding_hash="sha256:718cee694a910a9ba2ac60f923c8447f03ae448e01ac39737a4b7d6473ff641e",
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
            binding_hash="sha256:7860ea575a11fbdd2e7a5fd39f3ed84815ec6e4db149e3fe21ab63208aabb750",
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
            binding_hash="sha256:8cb46cbeaaeca935e90af97c3c743ed0cd871a1a192742eb6c37e1e76afea7b2",
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
            binding_hash="sha256:7ecce9494105fde9306fab8e3f7d58d02b01be39d96e9d01f930101dbf38d340",
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
            binding_hash="sha256:3139297944980124dbfe76333f37c6f5b849cce10afc28959bf34e66f2f25e0a",
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
            binding_hash="sha256:d65553ba378758fff24babc70597b322d02c4d00437644c1ea2e778c625e33d0",
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
            binding_hash="sha256:d0ed471812895c1949cc802953f8c9bfa945589774ad33e679b5bf2ba871d3e3",
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
            binding_hash="sha256:108b1a5aaff20142b8595c649c3a88f79c9d98d955c08a880910a9a5e77ebac5",
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
            binding_hash="sha256:a8930b77906631aa6408fdc7709e9442c8decbb9e6c52abc124ddd22b7a538ce",
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
            binding_hash="sha256:e5e3f7d9de2cac4e5dd92c3810f6b36a5b93e912222536e0705366d8ecd9af15",
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
            binding_hash="sha256:9ab0ab862056cf4406ad15beef398d013e6fbea604c048c8cbda6b57c3dd6292",
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
