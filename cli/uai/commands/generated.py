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

GENERATED_MANIFEST_HASH = "sha256:01eea87da11b3ff1c4c8293d209891fd270ad39f02fe7c97b8c170a062a0804f"
GENERATED_REGISTRY_HASH = "sha256:05dbf08cee411326cd6a910e0ed816a122c08657a7f0e8fac26a7d1609281d39"

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
            binding_hash="sha256:63ea2957031fb066fd0d216cbbc7e998ff17a9a3ba7a0b26f87e388635160dc6",
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
            binding_hash="sha256:883e625e85133cb16582d74ca70547808010906b7cb8ca316df6a4920f6504dc",
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
            binding_hash="sha256:79dade558033f627b106174f038be223852c98016cb5cf2330517aaba236c18a",
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
            binding_hash="sha256:619250cf53426e61a0eced9b8512d96f045ab8f52e8c462ba4e2bd01877cac6b",
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
            binding_hash="sha256:025dbb8ad1f0851ba33c84df10cc7d96aee3d6b47165a4a0df85e803c0cfa95a",
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
            binding_hash="sha256:001bb3a2c8a6b83309564820bb0f299f0fd0cbd46bf5bdce02d5b93323fc73e5",
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
            binding_hash="sha256:2c8c86cdae13f2bbe01edcdc0538f959343f72b539f3cf2bcfa6a9de3d1ab1f1",
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
            binding_hash="sha256:4a78d6a83ed29e94ace88474ac8ca64fbe12694f7227d1d10ce9466f004ce4cd",
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
            binding_hash="sha256:4a70c181f2b80a02e5fee385b2f0d562a6ec3ee13612036330fef2a097118474",
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
            binding_hash="sha256:2ce4454f223d9826f20a8b248eee6059f8d04a722454a8989b687e05d8a01da6",
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
            binding_hash="sha256:fc0287d737272032cd52c5920345436a993edd7bd5f5cb4b16661014775ee3a9",
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
            binding_hash="sha256:e57faefca86efe9ab7c59ebacca0053b2867e597128c1a1de00a36ad87939c2a",
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
            binding_hash="sha256:4babbb771d417dc7db9743526285aa799adb5b133f26c376785935a73168a2c9",
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
            binding_hash="sha256:a66c0bdf01570f6370ec16b992b547ca0a76c537bdbc4db098f1a688f5a6ed4b",
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
            binding_hash="sha256:66078b89337d755d7a4cd4b6ed0d4053defc4726bd5f41bc03f7a06b14afd257",
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
            binding_hash="sha256:8e82671f7a86feee19a015f9c07221616113795850c052fd1bca8f90c3e86064",
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
            binding_hash="sha256:52b957c587710ca57b1d847bf2a599ee88c4b25f46eb99ad145b726fc61fc4ed",
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
            binding_hash="sha256:d5464cfc78d91d161692e2d2fe5de795b16ce9e36220cfa8775c6ed328da788d",
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
            binding_hash="sha256:66da5dbb1f2ce696105bf4a295223251ad299476ca490545ce5f37cefd85ba40",
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
            binding_hash="sha256:093c9309876ae2145c89afd576a192d728cc3fc4ceebdddb7166eea92fcfda35",
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
            binding_hash="sha256:0a6e00f2150ff930b819b58b42eef1f255a7b487d220b28d6bcb9289421f93af",
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
            binding_hash="sha256:eaa2ba3c932933ec7db8e914d3d4cbd7164c1d9e8a931cbb508fcd91e39c6e05",
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
            binding_hash="sha256:efa30212b201bd7e8c62e9ec2008d4a4339612857027ea13374b9fc2d002cbfe",
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
            binding_hash="sha256:4709d72d775a6ba3e08c941ed6026ee2bc8f26ec1f5f76969281f51da1fba74f",
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
            binding_hash="sha256:830fc335552c1a3bc03b8d3ba7a1c12bca858d3fa8399a51683581e6db5df599",
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
            binding_hash="sha256:2b9c94cabd1d63a0eddae995b469e94c5638c2bbbc8b9d2d340b3f9e96d740d7",
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
            binding_hash="sha256:c8f0ce79b2796aa133b615ce210e606a019fc57805e3e7784438448ec869dbd5",
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
            binding_hash="sha256:4c44639c13f11c1a387c1c9e05fee65d29c4b4ffffcdc92da113d32c2718f7c2",
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
            binding_hash="sha256:d1c691fd09ab6fa5290ffa83aa93a639c60f0230364b07ba97e2dd33a1330ce6",
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
            binding_hash="sha256:c7ad2e7be6e2fdd581faa4d9292c97cacd4e2986bca2f39449740959c1de8df3",
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
            binding_hash="sha256:f6754c7135b64f45d57322c0bc29dee69884ea9423ea2af0312305d45fd3ad87",
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
            binding_hash="sha256:961701aebfde7edbcf886371316b96a74570f0ada81462807dff00e79abb46df",
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
            binding_hash="sha256:70a3d96f8dac0e53d48517070715643e0ef9f65eb441f8f23dacf5e23ed85192",
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
            binding_hash="sha256:3986b08672c8ee9da0a92f7a9aaf20c808ae87817a75a017f5f0cdab6f44f6e3",
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
            binding_hash="sha256:12b6b14cb74c09da16b795f93cea2391c60ea4504eb4b1b3834059b8e6c6520d",
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
            binding_hash="sha256:abce50f6fca17ec22d0756c1bd19449797b67f4eacaa1a4676cee9124c45e200",
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
            binding_hash="sha256:109056f72ba64188de04be43f99c0c40301bd41a020d3b2e9c3d7519ef0f489c",
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
            binding_hash="sha256:0b914bfacf362a8dd01267f5d5f3e0abc23516f8f0af8e086aad8a2f881e7202",
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
            binding_hash="sha256:400ee9e41fa70e5b79eedc36d4d4fee98efaf69a980888a5a2640c38279ce1af",
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
            binding_hash="sha256:f1443927a50fa27d97e441a74f4f87fa908a18e5eaf35644b50ed5c34bb6c696",
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
            binding_hash="sha256:3e9fdfcbfcb9e23d517737c96aa883c4a79ef24e014a36625144a19a99424964",
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
            binding_hash="sha256:c9805652ea979f05cae0cbe1622179fb726d58d78d8ce3ee7796c63c2c256dbe",
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
            binding_hash="sha256:9d1da189bc954bc03d8521d763a9efee542115bfb6c854e59c7ad972ed028b4d",
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
            binding_hash="sha256:f485fbab2b1f7ec2de81895d8b00be755f146d1404dbfec526562cfa6a4bf3e7",
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
            binding_hash="sha256:e3b0790776345806448bd815c090b17f613fb73f5f346549af64d06e3f4b6cae",
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
            binding_hash="sha256:97510e5ef0c1021cf2ead0304bd1c0bd4ebf482463f75d61f811fa1cddc189ad",
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
            binding_hash="sha256:43e1640555d85cd95727f90426f0dc6eb6f371822ca2a99d40a026249b2ebddd",
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
            binding_hash="sha256:34560203153f77421fbd7be05633559f3c2dd590705efaafa5395852e1e420de",
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
            binding_hash="sha256:939c2b8870f7470e84986e1e1b1606012ff3299d8d1dffe30d39868537e7b52d",
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
            binding_hash="sha256:202034a97fb90c22b562e948aea85b5bfee599053a2b67cef545fcbcd153b6f9",
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
            binding_hash="sha256:2d98d8632cee07a35a389d1677c0002181a577c3004a7747eb3365afcac9c1b1",
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
            binding_hash="sha256:8a2a26e7b58dbe3b772dfbfdad251c0b2e8280a5e24b6ad275750a5a965a465d",
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
            binding_hash="sha256:69616a4c6937ebb706243a4aa6a6a40f3b5196e4bd5f65ae94fc4a12bec5c1b1",
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
            binding_hash="sha256:5562e45efe73d87184ef68bbd308c2f1e491a6110d13acba637d24519fc6dce2",
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
            binding_hash="sha256:ba6a0ba8d00e2a0a5cb9a637d5e355bd2cdce34e2f92bd4f4255c7d02fb7e220",
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
            binding_hash="sha256:3545222de9449fefe7d5dfa7c1d819d157b4a5d92e70d69498bbbd4a7e8c6bb3",
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
            binding_hash="sha256:533cc9547ef18579e66541eedc39ca5e7e1a954a4176ab661db775db19d49a1d",
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
            binding_hash="sha256:5efa8a0dd21b209c10037cc13266385fc1967ebff654937584e90b3471f7d21b",
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
            binding_hash="sha256:5b715eeb7d5aa4870c142e170c627322606720ab8f7817dd98be728d4513bb7a",
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
            binding_hash="sha256:29e02596af27a7de42d89af12014c5551a5a8807a482df4f3490d4235cff743e",
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
            binding_hash="sha256:59d7b9d9b53132620c6cb37ebda334daa8693e498ba2824d59ff0edd027d4a1b",
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
            binding_hash="sha256:4555d9f7e1221b79ab3f5de1d3b441607593c557f7f308b52391152d1c1b6c06",
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
            binding_hash="sha256:5b70a245344851ea0e44d6a610ddfd60de53dda91a52f2d6e92bf4b2bec50a61",
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
            binding_hash="sha256:b96329ebc295e0f400143209c3614b6cdf4123d8ec0489e43b2294abe4a10848",
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
            binding_hash="sha256:8be92965fab792aace4c5d7175c82af71c7b5bf0fc6b443e4eb214c7d0db1640",
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
            binding_hash="sha256:9715ce582909453f405c9bf7b0ccd49be29ce3d575183641e5274f3f8dde0c48",
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
            binding_hash="sha256:9ffa7df22efed12e23e47454f864e004fd88aa629cc53af7e94ec088097205c4",
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
            binding_hash="sha256:e066afcd81f78d28f3b6df734aec4ae7f3343b0903abc8692b3b1ca27f9e822d",
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
            binding_hash="sha256:44cae8b776d9cf590bf75a6e6a9c9e834456bb3199dae5e019f123bb6dbb3c43",
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
            binding_hash="sha256:f2a4baf6b4013831e5753f7d3f3f4509b9434c6baa8fe998fc6c05105dfc7d5e",
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
            binding_hash="sha256:d225a08de6542e989865ddc1cab828e3faa43be22ecca1b65d89b3034f388449",
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
            binding_hash="sha256:4f58b6f131d890c225af1f9b5433f2f2f0e3055fe197edeaf55856217d766858",
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
            binding_hash="sha256:16ee2be1ae906dc019bb94bf91e969ed288c642800004bdcbac399581bab1129",
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
            binding_hash="sha256:4872213dea25a4674bce7841e94d9497ba85a80f9c671d2cc774068c4adb0aa7",
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
            binding_hash="sha256:7399bc70a17efd842925b406b637c4501f277e3d307d4b78d01f1fe81e46f1b1",
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
            binding_hash="sha256:48cb5dd766b188d6f655775d479072a9496e9b5688e0dfdd71a0e7231b400b44",
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
            binding_hash="sha256:b10549a0732229cb7923bcca3213e0ce8c2cd3f452ad04b764fdcb573a73d35e",
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
            binding_hash="sha256:7c4852ad77da85a07bab3e998f4e42f026c5107d1a339fe6c99604d8c4f4a64c",
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
            binding_hash="sha256:be389e4421c098e0f66fa49a54626e24373b05ec1a11b5348978483b4c9b71df",
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
            binding_hash="sha256:7245e5dc944188e0fee5523898fbd9559ab6ab6a527c8f50f1bb0486b715f7e0",
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
            binding_hash="sha256:6e25bf10cc2e7db91459ef04cf61588a71025337d952b64f73e70b21eb70a0ec",
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
            binding_hash="sha256:308733ebb67b617b01405a548cc9351ba0b5810ea5de5a19f1d4ba40e8484346",
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
            binding_hash="sha256:94ecb41f5237724c3c53cd190d0b9f6ad3255618dc4740324cee15cefbd1b3ed",
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
            binding_hash="sha256:2c207b9b53794ffc02ddf2d776ee74058c62f1b60aadc50ff86f2d2a382871c7",
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
            binding_hash="sha256:758bd5454b7f1c3cae3a8016cc22045e710fa4ffb4c085184d9829b1a84cf69b",
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
            binding_hash="sha256:117fb1e7d795eba1d7a755b3587d0d9a9674a3cfa766e176e4f550eb07d47111",
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
            binding_hash="sha256:311b41cad86e70ec3e12081f4bec2952d47fe6aacfab4fefd0cacc511414afaf",
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
            binding_hash="sha256:4c1f50a33978bbc420656b5eb20879b2cb1888e60ff70ba474a69885dd938e47",
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
            binding_hash="sha256:eb586fb5b29159400042ff734f18bf5d9e1a6e160dc309c3c994a4f2ccb6a8e7",
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
            binding_hash="sha256:b6454c0f7deac38624abf493a776061e7a2a026ac1b146df7ff4f273454ed43e",
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
            binding_hash="sha256:efd79bb67bfec6ce81fdd052ff99b374886cb112761bde21bf74093fb54ca480",
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
            binding_hash="sha256:da8f1a3e52d3904500928b2c33a9065cd2f0ad2800132ecde313af2376f772e6",
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
            binding_hash="sha256:4466fa98b7d6963878d05aeb55284cd25c558a411591752888e5c92f381189ad",
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
            binding_hash="sha256:755229c64d8af6fe58741fac06d32bc69ceda4c0a3823e0730322d9b1820f701",
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
            binding_hash="sha256:dc184b6906b4ba671c433e7f1d704f5513591af440e054ee8e26dd0aba8c09e7",
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
            binding_hash="sha256:80433c862a660bb548c82125311fba38e371265dfe8c81da62e1b378f25884c7",
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
            binding_hash="sha256:1fff0f157bb4394c673e2c5baa4f31ddbe64f415b0089f5758a04f2b7a2ec6ac",
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
            binding_hash="sha256:0d2ad729d87dd3c67de347adda57555ce7ff000761ea25467c8324d00a2664ef",
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
            binding_hash="sha256:2e5be43ec4eaaf0f34db68582f730efdf209f3c7424c60488fb7be529c3b5306",
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
            binding_hash="sha256:be7d80dde6b2b22ebce5134d61bb558493ca8aafe5877927469b8534207abf4b",
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
            binding_hash="sha256:78648290052c3c1571a1839c8829e731afd5de9125510f24a4167cd9a1bd8f50",
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
            binding_hash="sha256:d57a90349137d1dcb2c22bd4942b9c777332dcd89027354be4d424374b7945c0",
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
            binding_hash="sha256:29f11f4826b1bea9bbe727b28b8a92258f041bda8a7cfdf96830a2cbf39afbf4",
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
            binding_hash="sha256:169dc5204d0927c659cb7ead4725c78be091f13e1096c99561885f7fe71d3418",
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
            binding_hash="sha256:e9fc796995913547e5a3a3aac98eb98394e9167ebc47be4c2796dbe54c0c1a81",
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
            binding_hash="sha256:90c4339722870f167cc47301425a2f8a7c9cdca1eff119fc424a17912bdcbba4",
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
            binding_hash="sha256:f40c65faf48c80a58d11f259c21db9e37e5b41c6cef958836db90534d20976ce",
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
            binding_hash="sha256:8218cd67785566830d2317098c38e350bdd2ad1003c2e0386df1b729d8af158b",
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
            binding_hash="sha256:d512b2df6cddcf7e355e4d528ea32817e535596118ff9c94cc0372d474ae2ceb",
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
            binding_hash="sha256:9e4984f298ab89facb623206d50d50068b4e42c9f2685b89c1659d0e508fa517",
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
            binding_hash="sha256:128d58ca9d634915491ac79b01bba20f082d5c8a50c4d9d2b4d503e7ef51d286",
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
            binding_hash="sha256:56c8ac3da2e0dd2c3fdff19795fa9880322ea27782a88cf40545c17af45fd836",
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
            binding_hash="sha256:233b388701b61ce63efc20dd6f3b901f178eb1e1247b000b3031c4e40b261539",
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
            binding_hash="sha256:5e0160e8b1b6c02899808a9c78560cf4ee2eed48c028fea0c2e7704b783b2217",
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
            binding_hash="sha256:bad7e4063d9c9fc40027b40279c45f32649b78b7ba0c0ca90acb456e99425953",
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
            binding_hash="sha256:36255051343cb02f6b72e4d0d9dc26101321277dbcd3c1cd6578e5e7c4d80d60",
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
            binding_hash="sha256:303a8ea98dea3b5930e96bc6c18d77cb8c8807d2e0fd38012067fd90b4c910cd",
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
            binding_hash="sha256:8b9bcd7aa4d84bb90d34ff8515bcb910b8def01616358ab50ab092e0f03c6a49",
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
            binding_hash="sha256:2f6c34d4f7d112b754edf792d1dea1681331dfc87219c3d5505db7843989e7cc",
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
            binding_hash="sha256:fdc2743011483a78f4ad55c71042685670ef14e7ca5b7e2db9d0ba40f9bb6820",
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
            binding_hash="sha256:f954e70cde74c8cc2d3cb650f99f763e112e880a1cc33a535e25b1ebe650b5ca",
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
            binding_hash="sha256:7b7238a8411f15ceac0c79b69b9edf9ec1a9b4dc85860ffa3370b1e8ce6e6171",
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
            binding_hash="sha256:8cf01b220d2020afc9a484c034a90e6c09d5db2a15ab8c3c9591a84495d98fb7",
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
            binding_hash="sha256:eb293e498d696dfa2db5f1fcce8ed1c4a701554cf21d591124ead7555d058001",
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
            binding_hash="sha256:664e365d7948827e139e2d2a949ae092bbc87c2b225d8595e2d50b4bf2f09fb7",
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
            binding_hash="sha256:eab35ecaa8581ec83682bf3e4e095fffda4089863a8a2684f4a332ffe3c6ebf9",
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
            binding_hash="sha256:005868e76c170f2202d7528729008b6ebc3262772494b5485e5a0f318d0b6777",
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
            binding_hash="sha256:5d154134ea5ee921d60713bdc4b4ffe25141f78d90ed077397c4b68a3d9b5a69",
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
            binding_hash="sha256:3851a8fb24e2aee18ae47bc1ff14718bd42043d865166edf94a6046f151a6233",
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
            binding_hash="sha256:b10f63f3fb9c78994ef809d5600e1f458145ef8625d9f0aeb9e29236105c8ed3",
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
            binding_hash="sha256:ec963823b446742d725082f0cc8a64623c6a806c2dd4fd7aadd304f085bbaefe",
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
            binding_hash="sha256:0c51c5dcfec66a6855f8c66641d31e7fa707f8a0e3828f92d821827cb051d12d",
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
            binding_hash="sha256:b4ea6b7ac6c495f1fcfed297c389ffeb7bca8e3bcfc8e89713252c125e72a1b0",
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
            binding_hash="sha256:f922a4e31a58a3c95b74bfe5790e6c8eacc0aa44ce3c910b14b5e338fb6d8d01",
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
            binding_hash="sha256:d0dea4c3af987554dc70c444b7b1190acd6499b8908c08f8c8d9383ae79a44fe",
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
            binding_hash="sha256:3558f6dc27193d01e97c710fedd4411d64a3b3bad258e7dda9e551b804e1a51c",
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
            binding_hash="sha256:21491e0557add9b41cab5aff0b39761dc24303738184f2d9c4cee66d75692d9d",
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
            binding_hash="sha256:6c1d66355210b4dd63461ec561678773c42f2dd975556412be799ea88edc4462",
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
            binding_hash="sha256:1578e3c5367b1928cdc0bb5984d8df6a00b8ad3b19ea8e4792e5db617b287660",
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
            binding_hash="sha256:769cd8f5456bec8d3d296cf5aa335ad0c4c8513234d0ac616462058b486804be",
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
            binding_hash="sha256:6e9ee32df4d7d7d64430ebeb51cff3579e0513e490d0022cf56840d7704b5b1e",
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
            binding_hash="sha256:d2ef4febbc773ce4b81d345cc92aed6d0fca57d125e2e3af1d85ce55af91c486",
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
            binding_hash="sha256:111bdb1f7b2af9663b38004b0b5eacac0cd80324d99b15da2b8e32a9edab818a",
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
            binding_hash="sha256:d0504af869d09e68cc40f79f4dcfa340cf4470526d253379c6e761bc13f31822",
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
            binding_hash="sha256:931a44a45e9d04d40f1069975b350209a87da325b66f35257db88ac83050c3fb",
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
            binding_hash="sha256:5bbba2c9f172bea2130965ea06fd5dde50955c749254e4247981b410f939d6e1",
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
            binding_hash="sha256:1223cf2633f0e0a78432fe4f8ee05144dbe02278d63fc6b3fd2b3814a7dd46b5",
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
            binding_hash="sha256:7ee5f744a7cc291d34de4cad4603d48ca70358758c603f35e4ee5e3165e4270f",
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
            binding_hash="sha256:e5dc1bfc7ea46df05593f3db370f746ae9de7df952b958ed358f25a98312a3a3",
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
            binding_hash="sha256:65b9b94e7ea0619533056e6efeb001cd18afc8849bf98897774269b5e24d71a1",
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
            binding_hash="sha256:5594467113635655ef6a4a5dc7c028149a0efd2ed22b6b802afb5a51d4839a02",
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
            binding_hash="sha256:cad3a46246a2c405f6ebfeb370e732be9211e58626aa05691b4c74dcda3798d6",
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
            binding_hash="sha256:5529357f9719bdc7a9dafcf3c2dfb444d6b8d25058294b87d7a04775b3fdb017",
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
            binding_hash="sha256:ea9e077b98ea2aa7731c0d3b1562ab36528141c753a9fddd8350c1defadb35b3",
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
            binding_hash="sha256:9a5522d3c17437c87d86e135677b468c099f7104e47825868f413cc23d29936c",
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
            binding_hash="sha256:208e1b6a1bafc9912e54efcf24475cf061333cc43e657618a5250c09344983cd",
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
            binding_hash="sha256:7758f948570beee5de929f1afcaa9f50556812745d93b86dbf3bb7faff2b9ff0",
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
            binding_hash="sha256:11d9a227961313e9e92a49d4df02b49b47d1135873e546e9ea23f1e05ccdaf1b",
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
            binding_hash="sha256:10a87e0d90b7698d7f9fc0259ffa01c6185d59742a3e5897987e3650437ec248",
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
            binding_hash="sha256:c1f1a462f664286b3a47d2cdbdf20a8447946d5bff9dc5f6bc55705af0decd34",
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
            binding_hash="sha256:4dbabf692ca342862a7a3cc534a680732a7b1025f67262aa49c2ed60ad3fa0bf",
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
            binding_hash="sha256:912fdb74df2f8eb964375aeda496d0d0fcbb2e00b66e4c96a0ccb3b5fdf01697",
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
            binding_hash="sha256:86def36f8920552f7b3870eb994074fd9dd712f36e6facbcff8229daadfa9cfc",
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
            binding_hash="sha256:bded3ec8a6e92d5c79f78fe8d28c58f67968b6b53288faa2834d9ceef4be56ae",
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
            binding_hash="sha256:ae29ac22e84be10ca4267aadf6132c0281840643b3b5ffb796eabaaf7fa5e928",
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
            binding_hash="sha256:4e351149af0c1a47c82753bd6bc134872a4c80d62878039334cfe27d063a1fa6",
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
            binding_hash="sha256:1d6a2ec5b52fc38a3104c50892a3c2823e59df9eedbdcfba0078ee38f5bd2f59",
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
            binding_hash="sha256:6df678fc777376922c94e2d81b747077934fc02cf0d2b3c9bb2a48b6b9d1ec82",
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
            binding_hash="sha256:f2d44a9b9e580fd914395f994f72b2f6f2d552590ac8eba15fd49b436afcc252",
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
            binding_hash="sha256:88fa4b491f9f69c2e7435838405096286de19298b028a2af2b1092c085ccdec9",
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
            binding_hash="sha256:3bf663a9628c2f6e8f3833a2ecc53f82087b70a50ace729c752ae3c01f088114",
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
            binding_hash="sha256:40eb529bf9b1a1b909beb40ddd3a9131e2a1e9447e25323da76cbc19b112ccec",
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
            binding_hash="sha256:6e08b024b0b6758745042aaa81b9692c66e4dbd028fde2e72276496db4a56d9f",
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
            binding_hash="sha256:c6560da317251ec178130e66defbb40451b0cba6fca22b41e4f83f02c5b0effb",
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
            binding_hash="sha256:5b245a09fdf22e05a47aaf30162dd90889ab2aa7966f06e429cd2df4e8186617",
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
            binding_hash="sha256:e102500d9eb690472a49bb2e69d930b986b8bee8ddfb2c026313368a3153da7c",
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
            binding_hash="sha256:59043df221c4f718b838f1c29770127d7e0f3257094b1e524d2183c7d4c51b65",
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
            binding_hash="sha256:6821837a3b19da592880306135fa6c0f8fdeb75fe1a242afd89e3f78a32f6b69",
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
            binding_hash="sha256:d677ded727ccf1528739c7cdd8dc27194ec49888048e231b8529c8471cb06db1",
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
            binding_hash="sha256:87a6c149a27a4736f51cc8cd47085e66dcd5e8308ec122a3c548d07391835491",
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
            binding_hash="sha256:b436429395faeca2edaa840c28ae21640fe36f76a067d111e0cfdc3aa3c060f4",
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
            binding_hash="sha256:64d3ed9e7c4b5c5ddc8003b4b544f4c536809a96d52d73689e4ea4ba602402f6",
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
            binding_hash="sha256:81d1fb212f0162549a45548c7ddce45f1055ef32b0b8824940f0991ecf488609",
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
            binding_hash="sha256:df37875e4782a091e549d271017453cf71a8cd195d4e204e4d6423c86363e65c",
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
            binding_hash="sha256:979ae710286ccb7ff101959396db822891a7a51e399fbe1197acb812f598a943",
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
            binding_hash="sha256:424c8b9ad93f63b4cdafc7a8c4fd2d2425cf42adf2978a7ea35e5600f60db372",
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
            binding_hash="sha256:023caa2487482ac7233214d9e4adcff676f0e61bbc43391d0704b6712faf5eb0",
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
            binding_hash="sha256:cde126ff4f55ce5734efa76413f8cb6879f305cb014a3e8e0a9ee0dc05d1e07a",
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
            binding_hash="sha256:2165474dfa586ddf2d7df47d10f16fb47e6c6683214992e0fd0c22ae551ecd33",
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
            binding_hash="sha256:6230946462c0e46d7237e63b4559ce41919fa395353a137e28bc670886569311",
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
            binding_hash="sha256:f5dcbda1bb519c446101494361c4dc240a7c570a64c7051ddfec48422c07c765",
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
            binding_hash="sha256:65ef0e663becbb50b65511c529a6739c869e5a4094cc86f43bb61edee4ba76bb",
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
            binding_hash="sha256:8b68e53b3b3786b0d5a026ddfdbbec66b0c0f2eea551c7b7a77a7c712a5d149e",
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
            binding_hash="sha256:1837c8e869813663060b6a6cbdc47bd72e2251817bb446ad319bb73d4cd8ddde",
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
            binding_hash="sha256:a625784d6dc3373314652f7edb0fbd3546a63cc00fd3e3482d9a1678b009de0d",
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
            binding_hash="sha256:17947ab94e72a6bf5127de165cd00aa083ff5fb7aa474cf348e96bbcc778b589",
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
            binding_hash="sha256:ea5df8ab0dd7fba666a05a021a83e7d4fbdd232ab40bd5598d4ddfd1a6175743",
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
            binding_hash="sha256:74eb9b52de922ab062cb864ad3155d35914700fde9262f84c0c9c8efa750634f",
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
            binding_hash="sha256:2e05557c03a389ea0e60f664712097e1f076e94f8e506cd57d042025b913581e",
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
            binding_hash="sha256:85c0bfc8b80902cee69dd9e0d5f354940d12bfab9243ad5905487a4d3e921d3a",
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
            binding_hash="sha256:d173c9be0d4e0bf1de678a280ba4d77df9c1ebb242002041ff1d6a07abe6c44f",
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
            binding_hash="sha256:563104715649aafc0a13ef763c1d4fc9eae2583cc500e55895100c722dfb737b",
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
            binding_hash="sha256:8a8630e5631d9674a8684657a9a459043e888dc5ee2038d1278f9bfac92cc629",
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
            binding_hash="sha256:a075e2f2080b015062818bba742509e920c8c25df7f1cd08a0e158f84a73ebf3",
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
            binding_hash="sha256:84aaf35f04a51d79a06f0a8d907c9b2ba1d2dc818f468b970241c0838b136c8e",
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
            binding_hash="sha256:77eb79c592e7660a53fb649b9cfac92d435ddc94cc347cf54ba7260d73fdffbb",
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
            binding_hash="sha256:2881a0b7522e4326dc20fe80f0c4cc1a7b4cef3103cfd240d1928206dc92fdc7",
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
            binding_hash="sha256:60265b7de2185ba689dfc6c69343151f562a38c18e6061c67007c106f6f4df7b",
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
            binding_hash="sha256:78877338647a604e9d81b1fff527846c82df4a7dde0ab5acfe3aa314dc6757f6",
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
            binding_hash="sha256:822f2208c1d70e87f312dbf389b1f02312d04eadf17d0aae05e5b0804e2add96",
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
            binding_hash="sha256:081c56c7fc590818879d9db6d91cda131a1ea7e343f31a926658c6beec626706",
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
            binding_hash="sha256:b911f6fbbaf652ae571d044f2d988ae3ee839a023e0aecc3d6c24803bc4f1729",
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
            binding_hash="sha256:8de5300367854b56607e7f93efc58360b06ef944243e542ea4596c311937a53d",
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
            binding_hash="sha256:6aef2333d718d834e0de95328d529161965a350619b381cad36333af66aece57",
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
            binding_hash="sha256:11d048e6c1561923e3f30c5eb6d4a3e8f7291a4b77537b74f2404e3acacf8794",
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
            binding_hash="sha256:6fc3936c86f94ca82b2c928754f3c6c05b491e606ca25b43de489083d810ce6b",
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
            binding_hash="sha256:e76df729a009b2dd2eb9fe9e63772644a76938e6cb62687076e9ce89164d52e9",
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
            binding_hash="sha256:dd726a08de1498177080cb778ac5541c398b62931c85894be1a4e62876bd21dc",
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
            binding_hash="sha256:4bf01305e0fa9e8c50cc296bc14340c4d11e658fde2637310e90ec6965511593",
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
            binding_hash="sha256:7fe36568429f5cc7702c91455fa5e4c47d45f5b1c875d69a4d7bb6f8235e6ab9",
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
            binding_hash="sha256:10c6a17a00dd14edf2e574b50ec23727f1d2c5a866b181f016a68fe09b4dc5ec",
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
            binding_hash="sha256:7dbc72e5ec176c22ebbfa956f0f123369155dac0918256ed82754d5265325894",
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
            binding_hash="sha256:3c2d7e4e8f368e3c565060c2b7147d5746f07bdff8aeac226d5e92b0a21c4125",
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
            binding_hash="sha256:0e90076e2c0e3d3a7d3b3e7ab8e51a4e6643f459be3b03476b940c22e86157d0",
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
            binding_hash="sha256:c637285768168750f1f8c9b43f85e6dc1a7962867ee6f22a33efcb500fb3b1fb",
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
            binding_hash="sha256:7f734663f00bd46e47b6fd030a4afd4b3e5c24956bad92016c9077390a1750f5",
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
            binding_hash="sha256:793424e520536a1ce46632257561db557c30fb6728b7d4fbc491c95e32cfe9a1",
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
            binding_hash="sha256:be66e08602b42e2419cd2b4b80b10ff9dbfcff1aca6fe280f15ed4abfdee9b68",
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
            binding_hash="sha256:eaadd5f125e7b94b7b7fd5daab987ebe922ac7609ad83367b897eb61e764e315",
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
            binding_hash="sha256:fa5e2ff9b1593ff27df6fda42cbadff31941468c65c479513adf1862923d113f",
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
            binding_hash="sha256:f28046aad479ec3dce5cbc6ec45a6758e11796725426f10b8c459d4b43344219",
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
            binding_hash="sha256:71707734fbcf3fa15967143f2bf95fc0bbd9d2d2cb0466c56b7d3917b1158210",
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
            binding_hash="sha256:ac4011feb960862734b4bbc0b78ee005d44e063f3b586d0f9af588aef65bcd17",
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
            binding_hash="sha256:711fe22e9a0b881668add6bbba912517a8394c3375f4f5980619367355fddad7",
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
            binding_hash="sha256:209fe5c904fa4552ac4f03dda56db2fd61f1caa152af3dbbebc43b9c98670b40",
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
            binding_hash="sha256:81cea69505c20496d0970f707b88ec94fe3fdbc0ccd81d21bccd0f78e9fd6d3b",
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
            binding_hash="sha256:b23ca8c4479ae1e3e6004fbdb589bbb76c5294e331b3edd57d94ef2a5bbbb77a",
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
            binding_hash="sha256:755be6ae2d9afe2ae4bd64111a4cdc39915de1340b32cc905a77e65cfacc8369",
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
            binding_hash="sha256:4d7aa549e0c14db34849fe1956a076080cdb84eb5c05019ac0f1b0b099e6842e",
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
            binding_hash="sha256:f03eefc336366c65be663870777f504b5e62c2f0f8a5de6bc3d7c9f6c4048d40",
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
            binding_hash="sha256:36e377a58fda4063d9505222aa73f2e9cda72c4b1a2cd7718dbe1162ea872df5",
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
            binding_hash="sha256:c78b6fa0276eb846044af9ec8c14dac40011490aa542c8ba8f909bc9dfc62ca6",
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
            binding_hash="sha256:e63679d14a63f648d034747c9f82b35dffe9d137446fe3f1d19686f10458026a",
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
            binding_hash="sha256:90b38ba15176bc0f297ce342c36ee026c7a514107b80ba3a7646f43bca4fc59e",
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
            binding_hash="sha256:2b87d1079945d597c59e030be0261dc1bb8d04317bc983c81df4084bb5486105",
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
            binding_hash="sha256:97f9adba988bb9de017e553fae8e9ee4916acdaeb6d7062256e4b309dbed19dd",
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
            binding_hash="sha256:a90cdd2764117936938604cd92712c47b34cf53109fd9f4b173311d47b70700b",
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
            binding_hash="sha256:30a2c20e6b8fe3625dc597b7e5dd60ef1f1d2a158569e0d5aa58fa453b7d9bd3",
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
            binding_hash="sha256:5c427b90feda6b6ea8d2d1ef73957fd81c7d8f7540c58f06193a9cffbefb295a",
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
            binding_hash="sha256:970a97470117493fd6112dea539e0b403a9ae330dba9f08443fe92bce5fc72aa",
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
            binding_hash="sha256:14a033a2ccc200de62d99f6c5c098943ee92c4a64f0d01a696ea646907e3877b",
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
            binding_hash="sha256:84b0b05d9e0f9b9f6bdf1a206eed1d591b64ff493ff8ea91fb8d7e7fde0bce02",
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
            binding_hash="sha256:92520b44d48859b457e8fff3f104aa6057443193f75324b8933cfe77d9a44214",
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
            binding_hash="sha256:f9827b1aa4fe8445ca4b5bf912c6870e00066626cc8e5ae697169cd2c8ce2b13",
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
            binding_hash="sha256:bb0d75993b1a118ff8218330df1eb8bfab966781542207190e308709167588df",
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
            binding_hash="sha256:1af9598f9570bc75b6285fccc4967fa99faa51187a286627248e9ffea6366594",
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
            binding_hash="sha256:ad0c57ac9a095de1945e2042244963a2cfd28d8309ac4caa30cd4177dec67bb9",
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
            binding_hash="sha256:8bf96196e43bf8b84d11e25175491eca77fef3e1311088ecfb14a8bad2c4f155",
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
            binding_hash="sha256:e1ac3ba82a1487163a6cad2fdb28b2ec586ccae8c20f8a92913ef3eb7c591d3f",
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
            binding_hash="sha256:8ec7c9f7077431d498bbd1adc68b41162f70f591f5941304beeee10812acb004",
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
            binding_hash="sha256:10ebb53f6d7beb11d1ec060f1228051be3ebe5aaaed53ff3ea28994536101d80",
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
            binding_hash="sha256:349f6af74650ce90f1e291515fd877a06a30f81150ebed291519a82f17643ad9",
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
            binding_hash="sha256:1f6da25af9341be4d0530f3174f529a0e99046dadb3b6b3fa652777bc374845d",
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
            binding_hash="sha256:8cbf17cb04da2eb3dc8c426a302b00b9a37985317ac7baa6fb99fc6ed7adeaac",
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
            binding_hash="sha256:0c659dc3a73242f61f516bc1483c73b9c424d863d9dc158acc127ffcd2757b64",
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
            binding_hash="sha256:6f67f9ee61421d28c1008881d5123e4afbaaef516ff56e7c8ec1e5498bbf69d0",
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
            binding_hash="sha256:d7cc5e7ee764e946322a893f7596f4724866e2cfdb4133a64b2c4f16d722befe",
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
            binding_hash="sha256:507bc174a585020b803e6fbec519f05f6f794e7cc9599eb2511e306414a06412",
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
            binding_hash="sha256:4c4b72fa373a8b51a5b93ff44d72367eab62727356101693de62928653117134",
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
            binding_hash="sha256:7551e853a4676d242e0712d75078190543ef5a011ecda4885939c2226d224d48",
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
            binding_hash="sha256:1e6d0f713cd0be9f3f951cf639254cb24212d5201211f38d63ad3f85980ca181",
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
            binding_hash="sha256:80e06480ab979ac904d100c9a5fb2417ffae9242eb8bed9a47e1dc7f05b24e6d",
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
            binding_hash="sha256:c85b6a316400910bafa03906f6b4bfece6a267a40abd4bec43920d0a03aae200",
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
            binding_hash="sha256:ac035ad1bbb81afab171b6b3439722cf47382509f26ffd3c082e0068eec0d03e",
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
            binding_hash="sha256:8cf341db767e5e4bffd8ac47daeca7e50ed6f3a15d4214a184f0af291060e780",
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
            binding_hash="sha256:5134bbcdc45c630199f4aab44643fbd9e62aa4a8a445f07dd726c616ac9ee8d8",
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
            binding_hash="sha256:9dfba4588cdc3b4c94042dbd9419ec86fdcbc0b3bd8ead2032938c972db21ed1",
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
            binding_hash="sha256:2246aeb239a9a0f8f01f39daa2da1d000323443c2bbec429a1d4d74c280c5837",
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
            binding_hash="sha256:43e4f4ac21c820d538a19362f95aac612a115f2657373a0770093f86be16f124",
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
            binding_hash="sha256:9a14b1b2c12a646c8bd5905af3bb852c14e0b4e58daef3a3660a99307382afb9",
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
            binding_hash="sha256:43bd7b32e0c65f0b5cb643088a0c81235346da15a0b0e9912f0021cc2db6fad1",
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
            binding_hash="sha256:3ed271033d8fd906e694a18afe0ed22f31c9660ed5ac5306b8c826af335c2949",
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
            binding_hash="sha256:0624fec837223117100fb1f805e619cabf2a6edf63c691aac4f87a069e06d65b",
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
            binding_hash="sha256:d2a2a31f786e7d5c6ea5b0527b63a73e58b6b7e66e5b7683c903eb0a9571f14d",
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
            binding_hash="sha256:4f1e4f3c3cf50df98e1cdc4b68432168dd3e89432e0e9bea7c33b4855223e132",
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
            binding_hash="sha256:f206bea7712bb6431ab9b2f3745ba1aa47c9289a1604279d420eb267b9cb3979",
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
            binding_hash="sha256:8378346234d466ee8c31237df6e4c7f2fa3778883ec5f91611f3a0c539d23980",
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
            binding_hash="sha256:4023a585b76ea86d19b90a8f2bd9af1d02ef4072fad28a5a72da9d17b1cd092c",
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
            binding_hash="sha256:67bae5ec5ad50889fcb8177bbe92b1f2dbf1394c33ddd54020fab084014f59d8",
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
            binding_hash="sha256:9be0ac49ac19a0cf1394f61fa04be6a74f1a64fa25fc8e637388cdf46dab475a",
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
            binding_hash="sha256:87f66b6baff704549a13690d3060590a89d37c2261007b2940ad2335aa916856",
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
            binding_hash="sha256:bf97a1af6903fcb840984d9483330ad72e21db424d8ad7a06f2b5b5cd4e083e5",
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
            binding_hash="sha256:bc882c54ce7e75a729a082b60556bf04db0d7fc43768a42fb4a0a9a47cdc3fe2",
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
            binding_hash="sha256:387f5ee146bf9ddf5f160ec20536465ba143418fdb863fc616d97645ab846378",
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
            binding_hash="sha256:db2d8425bdf07e942d02ccf138a7870df813d5ee42bdce55163bf9c12fe5a57f",
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
            binding_hash="sha256:cb8a0c6163334624fc36745c1bcfa99d7eaaabf5a3fa6f78b5a5871fd57297c1",
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
            binding_hash="sha256:9104582047f13134c6300e363da15e290ec6790d7c0920cee95d6aaa6590faca",
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
            binding_hash="sha256:9cf442545efd4ae6f6494f7863f69292d25b15e454329383f917aeabf8d6e40c",
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
            binding_hash="sha256:07d6cb418bcfd3a837a03e13716c7a8a7ac024686bdf4d979ddf289c2252e213",
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
            binding_hash="sha256:a84004ac93bb937ebca38b02c59d234b6280979caa8194c788211e8dfa24dab0",
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
            binding_hash="sha256:55d281f66f397906525cc9cf3dd206dbeb600a5addfa6528e2837f839725f63d",
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
            binding_hash="sha256:014f0dd90f01e7df9366ba4ae6729d6c074bd181b2936303e85b30b3add9ff1d",
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
            binding_hash="sha256:b1d8f0445c6c4fd81f699de1708fbe0cc48144dded5d7bc48f71aa168778913a",
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
            binding_hash="sha256:25b23c58b8091ce51a1bcfa221fd7229da2d99daa49d284d3fa3f3835e175696",
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
            binding_hash="sha256:70929b299b18085401d802666efc4a3c6ba9cfa2102547822ea51e698310d5e8",
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
            binding_hash="sha256:e969b1ee5f111a74542c0835dd18784b252ffd78eacd51db66453f8b081c9bc4",
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
            binding_hash="sha256:91d9234beca2a585bc95547252d5af4b5fba23e10502cdc0d042b82ac145d90f",
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
            binding_hash="sha256:3987a0a15a64df3c35887b9b10540ac3719b00e01d8f3a07927d5f352c24befe",
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
            binding_hash="sha256:ebcbace7239c6366d8b97d112299fe488e50248ffac51a0c352a1fc99d170843",
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
            binding_hash="sha256:595b30688feecc7710d5f774df3182f7b00eb3758632aec041a65038f7b2bc92",
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
            binding_hash="sha256:03b61d1a509cdc81d33fe3960617a3ef43b7541884a0197a01f4f55331d3a322",
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
            binding_hash="sha256:87ebfad43ffe5aebc2b0d6d7e98a02a71e88bf5e1461b4229cb2d1e757c54afe",
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
            binding_hash="sha256:eb955df1a63eb48bdb993ab347dad171f00a53b384e173042e147612309dbf80",
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
            binding_hash="sha256:5e4cff01ac4d6b0717cb05a0426a63b892ed0d648429342f08c5f15f8b3b31d4",
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
            binding_hash="sha256:c9e94f837ec7e27359fc3218ee607f936ac4944a7e014d03d5386102866fccb8",
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
            binding_hash="sha256:4312d1ce37ea6a910705ad4686a14ca2dace055c043f1df540b92a8689640829",
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
            binding_hash="sha256:3a8d1a59729882625381be10d76214a642a565e57eff0fa05b889d22220b923f",
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
            binding_hash="sha256:ef002a14a763838f678b4ccd3515ca3ae2fa34131b6ebde02a117d357bde1037",
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
            binding_hash="sha256:76b3b66904283828169444add9c2e56a0122d97be8f291852815396922b9349a",
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
            binding_hash="sha256:5c19ab8b1e5e946af17a2642d322611d2d9817202147749e0d940195ccdb3bf2",
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
            binding_hash="sha256:c2d52aa8dfd72cbe68b5ada3474908a1b03d6ea0d4a30bdcdf69bd6f9a365f9a",
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
            binding_hash="sha256:ce712ff5e2df3dd62934bc24b89909c0f6fa0b6d3269c452a57c7b3e30efc84f",
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
            binding_hash="sha256:94b216f5e740ca1c4452d7962785309d2098442106c175dde56d17a01c991f0d",
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
            binding_hash="sha256:a996a48733cb273ee54c037f24b551a57c6b41515dd01571e261700e3f56edf7",
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
            binding_hash="sha256:5e3e741e194d44ab6357aa26fa2760815fcc2cad50f9fc31d7bc3cd20d727dc8",
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
            binding_hash="sha256:c1d6308ef89f6086383af0c98f497239cb2b97f05e6942e91fabd124c7583d8c",
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
            binding_hash="sha256:2a875634fb6cb2db46edf23df1aab2ad3a9e4ad603e0b3c9324fd8ffb09ad870",
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
            binding_hash="sha256:79b4043d97ead00ee40bc1de4da8123b38fd3d56fc58434d4241329003e4b66d",
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
            binding_hash="sha256:dc3039c3761245c3f8349a4df164a44242d5ba49b2efc211b07de25dc567432c",
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
            binding_hash="sha256:fc025e7b882abf3853110ef75f2db174d7d24702ba9ac3393f935f154138d615",
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
            binding_hash="sha256:8863303bae9512041b36b89b1d5dcdcaee8ec8f60b3abebc90e5481df3b277d6",
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
            binding_hash="sha256:048718c4a9e187e13d92247fdec8768f261b74a4772ed2599ac7dc3f5df36ebd",
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
            binding_hash="sha256:1abdc8ee5da6c7206326187e46c278f9b3f6876ee1a8dd16dbc72bb838e714bf",
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
            binding_hash="sha256:f64cc0def1967f5bfd0a136bb2d01f4dceed69b4f9f4345fa535454a7516677e",
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
            binding_hash="sha256:7059a720517e49bb8419ae2f68ab8b59108606520b5d8cb2e3f04cc19e1be8ab",
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
            binding_hash="sha256:6a5dae2652b7aa90bcdeaa941fa97cd1ec6af6b824dc0a84f5e9a3b75d04f1c4",
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
            binding_hash="sha256:9bb173205c12b79372515d8d2c95247582de1550cd2fef6077993def9069555f",
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
            binding_hash="sha256:1ccafe676e530a3b9cf9ef1527c9e20a5f26e3355acd4141705290f9f1f07a1c",
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
            binding_hash="sha256:8f736479b33f69ddef3044b48686d1b4045e7f73458c8192c5ece089c423550a",
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
            binding_hash="sha256:0c2c726a3a04c88645f24ce1bf988517fd5b5f6abfc778765e21840d2806ae43",
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
            binding_hash="sha256:c8ab42e2eee8b6c037c5eb9b7b7854425eae1c9c16987e4f9f41cd3952907b89",
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
            binding_hash="sha256:220f39a784ee79b7e09b732c5b6140dc317008048308f05eb82b59e68c6f1a36",
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
            binding_hash="sha256:0a0d00d2e83d58c2e37e3e7bdbde53d8e5241a412cd201cb876efd8ca643b2d1",
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
            binding_hash="sha256:cabea4e3759c1f0abcfd30022394b5bee7857750cb856971a0d96d19de264d27",
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
            binding_hash="sha256:0f6d45fc8416e00051ebbe86cd0f3fb98269c55ee2c9554ba977d0b26439f71b",
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
            binding_hash="sha256:0d61006fd63e3ba4758d45b2314ecf4e0105912ff49e52d6517cb090ab3f78dd",
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
            binding_hash="sha256:2f014af565ed5c9d30a2b578e3213ae4999f28616311578a0eb2646d5873ee70",
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
            binding_hash="sha256:95c37e276540e4afe2c25f5525268d17af863680f9ada015d5756716be8c7534",
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
            binding_hash="sha256:6030ab8a0dc12264cb77cefe741f239e31a73cf5a3be0e4e239caf8ad064d5e7",
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
            binding_hash="sha256:304b491d61b09745dd874b2c0ada1e95460f0993022175eee5a5e05265c17976",
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
            binding_hash="sha256:b1b7cfdd95329a393c071ba61b11c8cf3fc91f091f894255a49d15354f9d0d77",
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
            binding_hash="sha256:d0d3eda897f9d1d704ac328104d51a3189acce58b9f04d52c58a0e1568187254",
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
            binding_hash="sha256:944e098a65ecfd8fed22ce33ca3d04a5cb4bb0fda78800b9f15192ff8ad5f3cc",
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
            binding_hash="sha256:f6fcf741523938447646744b040521aa927a9f7f1092f3020f68abc955cde0c7",
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
            binding_hash="sha256:0d64d6194b4ee900a3cfd7be9e3dde2dbc9cbbcf642a90695eb14605ab7ddbc0",
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
