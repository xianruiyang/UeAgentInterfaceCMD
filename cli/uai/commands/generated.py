"""Generated from the C++ command registry manifest. Do not edit."""

from __future__ import annotations

from typing import Any

from ._runtime import (
    CommandBinding,
    CommandBindingCatalog,
    CommandExecutor,
    CommandParameterBinding,
    CommandVariantBinding,
    ModelResultFieldBinding,
    OMITTED,
)

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
        parent: str | object = OMITTED,
        attachment_kind: str | object = OMITTED,
        graph_owner: str | object = OMITTED,
        describe: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if parent is not OMITTED:
            params["parent"] = parent
        if attachment_kind is not OMITTED:
            params["attachment_kind"] = attachment_kind
        if graph_owner is not OMITTED:
            params["graph_owner"] = graph_owner
        if describe is not OMITTED:
            params["describe"] = describe
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

class AnimationCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

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
        *,
        axes: list[Any] | object = OMITTED,
        dimension: int,
        package_path: str,
        samples: list[Any] | object = OMITTED,
        skeleton_ref: str,
    ):
        params: dict[str, Any] = {}
        params["asset_name"] = asset_name
        if axes is not OMITTED:
            params["axes"] = axes
        params["dimension"] = dimension
        params["package_path"] = package_path
        if samples is not OMITTED:
            params["samples"] = samples
        params["skeleton_ref"] = skeleton_ref
        return self._client.execute(
            "animation.blend_space.asset.create",
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

    def state_machine_candidates(
        self,
        target: str,
        surface: str,
        *,
        class_settings: dict[str, Any] | object = OMITTED,
        query: str | object = OMITTED,
        describe: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["surface"] = surface
        if class_settings is not OMITTED:
            params["class_settings"] = class_settings
        if query is not OMITTED:
            params["query"] = query
        if describe is not OMITTED:
            params["describe"] = describe
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
        describe: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if describe is not OMITTED:
            params["describe"] = describe
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

    def collection(
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
            "asset.collection",
            params,
        )

    def delete(
        self,
        targets: list[Any],
        *,
        recursive: bool | object = OMITTED,
        confirm: bool | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["targets"] = targets
        if recursive is not OMITTED:
            params["recursive"] = recursive
        if confirm is not OMITTED:
            params["confirm"] = confirm
        return self._client.execute(
            "asset.delete",
            params,
        )

    def factory_candidates(
        self,
        create_command: str,
        *,
        query: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["create_command"] = create_command
        if query is not OMITTED:
            params["query"] = query
        return self._client.execute(
            "asset.factory.candidates",
            params,
        )

    def fixup_redirectors(
        self,
        root_ref: str,
        *,
        confirm: bool | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["root_ref"] = root_ref
        if confirm is not OMITTED:
            params["confirm"] = confirm
        return self._client.execute(
            "asset.fixup_redirectors",
            params,
        )

    def move(
        self,
        target_ref: str,
        destination_ref: str,
        *,
        confirm: bool | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        params["destination_ref"] = destination_ref
        if confirm is not OMITTED:
            params["confirm"] = confirm
        return self._client.execute(
            "asset.move",
            params,
        )

    def object_clone(
        self,
        source_ref: str,
        target_ref: str,
        *,
        confirm: bool | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["source_ref"] = source_ref
        params["target_ref"] = target_ref
        if confirm is not OMITTED:
            params["confirm"] = confirm
        return self._client.execute(
            "asset.object.clone",
            params,
        )

    def object_create(
        self,
        factory: Any,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["factory"] = factory
        params["target_ref"] = target_ref
        return self._client.execute(
            "asset.object.create",
            params,
        )

    def owned_candidates(
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
            "asset.owned_candidates",
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
            "asset.relations",
            params,
        )

    def sample(
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
            "asset.sample",
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
        describe: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if describe is not OMITTED:
            params["describe"] = describe
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
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if parent is not OMITTED:
            params["parent"] = parent
        if query is not OMITTED:
            params["query"] = query
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
        graph_name: str,
        *,
        query: str | object = OMITTED,
        node_name: str | object = OMITTED,
        node_occurrence: int | object = OMITTED,
        pin_name: str | object = OMITTED,
        pin_occurrence: int | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["graph_name"] = graph_name
        if query is not OMITTED:
            params["query"] = query
        if node_name is not OMITTED:
            params["node_name"] = node_name
        if node_occurrence is not OMITTED:
            params["node_occurrence"] = node_occurrence
        if pin_name is not OMITTED:
            params["pin_name"] = pin_name
        if pin_occurrence is not OMITTED:
            params["pin_occurrence"] = pin_occurrence
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
            "config.resolved_value",
            params,
        )

    def section(
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
        source: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["workspace_path"] = workspace_path
        if profile_id is not OMITTED:
            params["profile_id"] = profile_id
        if source is not OMITTED:
            params["source"] = source
        return self._client.execute(
            "content_graph.export_workspace",
            params,
        )

    def import_workspace(
        self,
        target: str,
        source: dict[str, Any],
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["source"] = source
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

    def save_resources(
        self,
        resource_refs: list[Any],
    ):
        params: dict[str, Any] = {}
        params["resource_refs"] = resource_refs
        return self._client.execute(
            "editor.save_resources",
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
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.config_section.update",
            params,
        )

    def device_profile_update(
        self,
        changes: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.device_profile.update",
            params,
        )

    def platform_config_update(
        self,
        changes: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.platform_config.update",
            params,
        )

    def project_settings_update(
        self,
        changes: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.project_settings.update",
            params,
        )

    def scalability_group_update(
        self,
        changes: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["changes"] = changes
        params["target_ref"] = target_ref
        return self._client.execute(
            "editor_project.scalability_group.update",
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
        *,
        projection: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["targets"] = targets
        params["strategy"] = strategy
        params["parameters"] = parameters
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

    def expression_candidates(
        self,
        target: str,
        *,
        query: str | object = OMITTED,
        graph_name: str | object = OMITTED,
        pin_name: str | object = OMITTED,
        describe: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if graph_name is not OMITTED:
            params["graph_name"] = graph_name
        if pin_name is not OMITTED:
            params["pin_name"] = pin_name
        if describe is not OMITTED:
            params["describe"] = describe
        return self._client.execute(
            "material.expression.candidates",
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

class MeshCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

    def attribute_normals_recompute(
        self,
        *,
        angle_degrees: float | object = OMITTED,
        mode: str,
        preserve_existing_hard_edges: bool,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        if angle_degrees is not OMITTED:
            params["angle_degrees"] = angle_degrees
        params["mode"] = mode
        params["preserve_existing_hard_edges"] = preserve_existing_hard_edges
        params["target_ref"] = target_ref
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
        texture_resolution: int,
        uv_channel: int,
    ):
        params: dict[str, Any] = {}
        params["island_source"] = island_source
        params["method"] = method
        params["pack"] = pack
        params["target_ref"] = target_ref
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
        uv_channel: int,
    ):
        params: dict[str, Any] = {}
        params["dimensions_cm"] = dimensions_cm
        params["projection_frame"] = projection_frame
        params["projection_type"] = projection_type
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
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
    ):
        params: dict[str, Any] = {}
        params["max_hulls"] = max_hulls
        params["max_vertices_per_hull"] = max_vertices_per_hull
        params["mode"] = mode
        params["replace_existing"] = replace_existing
        params["target_ref"] = target_ref
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
    ):
        params: dict[str, Any] = {}
        params["max_shapes"] = max_shapes
        params["method"] = method
        params["replace_existing"] = replace_existing
        params["target_ref"] = target_ref
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
        operand_to_target: dict[str, Any],
        operation: str,
        simplify_output: bool,
        space_contract: dict[str, Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["operand_ref"] = operand_ref
        params["operand_to_target"] = operand_to_target
        params["operation"] = operation
        params["simplify_output"] = simplify_output
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
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
    ):
        params: dict[str, Any] = {}
        params["distance_cm"] = distance_cm
        params["roundness"] = roundness
        params["segments"] = segments
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.topology.edges.bevel",
            params,
        )

    def topology_edges_weld(
        self,
        edge_pairs: list[Any],
        target_ref: str,
        tolerance_cm: float,
    ):
        params: dict[str, Any] = {}
        params["edge_pairs"] = edge_pairs
        params["target_ref"] = target_ref
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
        translation_cm: list[Any],
    ):
        params: dict[str, Any] = {}
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
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
    ):
        params: dict[str, Any] = {}
        if direction is not OMITTED:
            params["direction"] = direction
        params["direction_mode"] = direction_mode
        params["distance_cm"] = distance_cm
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
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
    ):
        params: dict[str, Any] = {}
        params["boundary_mode"] = boundary_mode
        params["distance_cm"] = distance_cm
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
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
    ):
        params: dict[str, Any] = {}
        params["distance_cm"] = distance_cm
        params["offset_mode"] = offset_mode
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
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
    ):
        params: dict[str, Any] = {}
        if direction is not OMITTED:
            params["direction"] = direction
        params["direction_mode"] = direction_mode
        params["distance_cm"] = distance_cm
        params["selection"] = selection
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.topology.faces.push_pull",
            params,
        )

    def topology_holes_fill(
        self,
        fill_mode: str,
        selection: dict[str, Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["fill_mode"] = fill_mode
        params["selection"] = selection
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.topology.holes.fill",
            params,
        )

    def topology_mesh_cut(
        self,
        fill_cut: bool,
        keep_sides: str,
        operand_ref: str,
        operand_to_target: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["fill_cut"] = fill_cut
        params["keep_sides"] = keep_sides
        params["operand_ref"] = operand_ref
        params["operand_to_target"] = operand_to_target
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
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
        weld_seam: bool,
    ):
        params: dict[str, Any] = {}
        params["keep_original"] = keep_original
        params["plane"] = plane
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
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
    ):
        params: dict[str, Any] = {}
        params["fill_hole"] = fill_hole
        params["keep_side"] = keep_side
        params["plane"] = plane
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
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
    ):
        params: dict[str, Any] = {}
        params["iterations"] = iterations
        params["preserve_boundaries"] = preserve_boundaries
        params["preserve_sharp_edges"] = preserve_sharp_edges
        params["space_contract"] = space_contract
        params["target_edge_length_cm"] = target_edge_length_cm
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.topology.remesh",
            params,
        )

    def topology_simplify(
        self,
        preserve_boundaries: bool,
        target_mode: str,
        target_ref: str,
        target_value: float,
    ):
        params: dict[str, Any] = {}
        params["preserve_boundaries"] = preserve_boundaries
        params["target_mode"] = target_mode
        params["target_ref"] = target_ref
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
    ):
        params: dict[str, Any] = {}
        params["levels"] = levels
        params["scheme"] = scheme
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.topology.subdivide",
            params,
        )

    def topology_trim(
        self,
        fill_hole: bool,
        keep_region: str,
        operand_ref: str,
        operand_to_target: dict[str, Any],
        space_contract: dict[str, Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["fill_hole"] = fill_hole
        params["keep_region"] = keep_region
        params["operand_ref"] = operand_ref
        params["operand_to_target"] = operand_to_target
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
        return self._client.execute(
            "mesh.topology.trim",
            params,
        )

    def topology_voxel_boolean(
        self,
        adaptivity: float,
        operand_ref: str,
        operand_to_target: dict[str, Any],
        operation: str,
        space_contract: dict[str, Any],
        target_ref: str,
        voxel_size_cm: float,
    ):
        params: dict[str, Any] = {}
        params["adaptivity"] = adaptivity
        params["operand_ref"] = operand_ref
        params["operand_to_target"] = operand_to_target
        params["operation"] = operation
        params["space_contract"] = space_contract
        params["target_ref"] = target_ref
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

    def voxel_grid_begin(
        self,
        *,
        mode: str | object = OMITTED,
        actor_ref: str | object = OMITTED,
        label: str | object = OMITTED,
        cell_size: float | object = OMITTED,
        origin: dict[str, Any] | object = OMITTED,
        rotation: dict[str, Any] | object = OMITTED,
        anchor: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if mode is not OMITTED:
            params["mode"] = mode
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
        return self._client.execute(
            "mesh.voxel_grid.begin",
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
        registration_policy: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["registration_policy"] = registration_policy
        params["target_ref"] = target_ref
        return self._client.execute(
            "metasound.graph.compile_settle",
            params,
        )

class ModelingCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

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
        confirm: bool | object = OMITTED,
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
        if confirm is not OMITTED:
            params["confirm"] = confirm
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
        emitter_name: str | object = OMITTED,
        stage_name: str | object = OMITTED,
        query: str | object = OMITTED,
        describe: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["target_usage"] = target_usage
        if emitter_name is not OMITTED:
            params["emitter_name"] = emitter_name
        if stage_name is not OMITTED:
            params["stage_name"] = stage_name
        if query is not OMITTED:
            params["query"] = query
        if describe is not OMITTED:
            params["describe"] = describe
        return self._client.execute(
            "niagara.module.candidates",
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

class PcgCommands:
    __slots__ = ("_client",)

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self._client = client

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

    def node_candidates(
        self,
        target: str,
        *,
        query: str | object = OMITTED,
        describe: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if describe is not OMITTED:
            params["describe"] = describe
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

    def command_search(
        self,
        intent: str,
    ):
        params: dict[str, Any] = {}
        params["intent"] = intent
        return self._client.execute(
            "query.command.search",
            params,
        )

    def command_usage(
        self,
        commands: list[Any],
    ):
        params: dict[str, Any] = {}
        params["commands"] = commands
        return self._client.execute(
            "query.command.usage",
            params,
        )

    def content_search(
        self,
        *,
        query: str | object = OMITTED,
        match_mode: str | object = OMITTED,
        content_kinds: list[Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        if query is not OMITTED:
            params["query"] = query
        if match_mode is not OMITTED:
            params["match_mode"] = match_mode
        if content_kinds is not OMITTED:
            params["content_kinds"] = content_kinds
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

    def origin_resolve(
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
        confirm: bool | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        params["name"] = name
        if confirm is not OMITTED:
            params["confirm"] = confirm
        return self._client.execute(
            "skeletal_mesh.remove_morph_target",
            params,
        )

    def remove_skin_weight_profile(
        self,
        target_ref: str,
        name: str,
        *,
        confirm: bool | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target_ref"] = target_ref
        params["name"] = name
        if confirm is not OMITTED:
            params["confirm"] = confirm
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
        sync_policy: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["sync_policy"] = sync_policy
        params["target_ref"] = target_ref
        return self._client.execute(
            "sound_cue.graph.compile_settle",
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
        outputs: list[Any],
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        params["outputs"] = outputs
        return self._client.execute(
            "texture_graph.artifact.bake",
            params,
        )

    def artifact_capture(
        self,
        outputs: list[Any],
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["outputs"] = outputs
        params["target_ref"] = target_ref
        return self._client.execute(
            "texture_graph.artifact.capture",
            params,
        )

    def graph_validate_evaluate_settle(
        self,
        evaluation_policy: str,
        target_ref: str,
    ):
        params: dict[str, Any] = {}
        params["evaluation_policy"] = evaluation_policy
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

    def track_candidates(
        self,
        target: str,
        *,
        animation_name: str | object = OMITTED,
        binding_kind: str | object = OMITTED,
        object_ref: str | object = OMITTED,
        property_path: str | object = OMITTED,
        query: str | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if animation_name is not OMITTED:
            params["animation_name"] = animation_name
        if binding_kind is not OMITTED:
            params["binding_kind"] = binding_kind
        if object_ref is not OMITTED:
            params["object_ref"] = object_ref
        if property_path is not OMITTED:
            params["property_path"] = property_path
        if query is not OMITTED:
            params["query"] = query
        return self._client.execute(
            "timeline.track_candidates",
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
        describe: dict[str, Any] | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if query is not OMITTED:
            params["query"] = query
        if describe is not OMITTED:
            params["describe"] = describe
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
    ):
        params: dict[str, Any] = {}
        params["target"] = target
        if category is not OMITTED:
            params["category"] = category
        if query is not OMITTED:
            params["query"] = query
        return self._client.execute(
            "world.actor.candidates",
            params,
        )

    def capsule_path(
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
            "world.capsule_path",
            params,
        )

    def capsule_sweep(
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
            "world.capsule_sweep",
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
        confirm: bool | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["folder_path"] = folder_path
        if managed_id is not OMITTED:
            params["managed_id"] = managed_id
        if confirm is not OMITTED:
            params["confirm"] = confirm
        return self._client.execute(
            "world.level_content.delete_scope",
            params,
        )

    def mesh_closest_vertex(
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
            "world.mesh_closest_vertex",
            params,
        )

    def mesh_vertex_position(
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
            "world.mesh_vertex_position",
            params,
        )

    def nav_connectivity(
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
            "world.nav_connectivity",
            params,
        )

    def nav_find_path(
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
            "world.nav_find_path",
            params,
        )

    def nav_project_point(
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
            "world.nav_project_point",
            params,
        )

    def nearby_shapes(
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

    def overlap(
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
        confirm: bool | object = OMITTED,
    ):
        params: dict[str, Any] = {}
        params["actor_ref"] = actor_ref
        params["component_name"] = component_name
        if confirm is not OMITTED:
            params["confirm"] = confirm
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

    def ray_trace(
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

_BINDING_CATALOG = CommandBindingCatalog(
    (
        CommandBinding(
            command_id="ai.behavior.candidates",
            binding_hash="sha256:fd2ef5d289ef5fb3841e4b3bd16d78eced6d7e21779680e9a00e05c11c7f88e5",
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
                    name="parent",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="attachment_kind",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="graph_owner",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="describe",
                    wire_type="object",
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
            binding_hash="sha256:0af7feec64592b99640ead19b8a71bb69489312fb123ee7611c02f406dc3a596",
            namespace="ai",
            method="behavior_tree_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.blackboard.asset.create",
            binding_hash="sha256:246ed3c8a5c63ead062d7c5d5c8e0fcd58a6432a1b9f2fe32e7d2175460df307",
            namespace="ai",
            method="blackboard_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.eqs.asset.create",
            binding_hash="sha256:27b474813f5dc0203a97f2660f371e851ed343ccff1c723a93667328547b6040",
            namespace="ai",
            method="eqs_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.smart_object_definition.asset.create",
            binding_hash="sha256:a4532309492fd1f19e3b1a80c70dcdb98496015c352df783e0f56057d63dc2f6",
            namespace="ai",
            method="smart_object_definition_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="ai.state_tree.asset.create",
            binding_hash="sha256:d64ad0e9b6949005359e0da4f874b332a42bed873e6b455829dcbeebd470934c",
            namespace="ai",
            method="state_tree_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.anim_blueprint.asset.create",
            binding_hash="sha256:255546859a938c560dfe6ea782c2da13054c71c195c7c53e9a4aba5dca5bc173",
            namespace="animation",
            method="anim_blueprint_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="parent_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="skeleton_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.anim_blueprint.layer_interface.asset.create",
            binding_hash="sha256:320cc347eaed72782601581e959cd9a90b09de22a6e60ca8ce4f492f0f831e8e",
            namespace="animation",
            method="anim_blueprint_layer_interface_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.blend_space.asset.create",
            binding_hash="sha256:9f1b4921978f3d98f0c174de4ca3aeba905fc1a1dcbd2cf1fde2a02870190ec0",
            namespace="animation",
            method="blend_space_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="axes",
                    wire_type="array",
                    required=False,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"axis_index":{"minimum":0,"type":"integer"},"axis_name":{"minLength":1,"type":"string"},"grid_divisions":{"minimum":1,"type":"integer"},"maximum":{"type":"number"},"minimum":{"type":"number"}},"required":["axis_index","axis_name","grid_divisions","maximum","minimum"],"type":"object"},"minItems":1,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="dimension",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":2,"minimum":1,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="samples",
                    wire_type="array",
                    required=False,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"animation_ref":{"minLength":1,"type":"string"},"coordinates":{"items":{"type":"number"},"maxItems":3,"minItems":1,"type":"array"},"intent":{"enum":["create","update","replace","delete"],"type":"string"}},"required":["animation_ref","coordinates","intent"],"type":"object"},"type":"array"}',
                ),
                CommandParameterBinding(
                    name="skeleton_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.blend_space.definition.apply",
            binding_hash="sha256:7fbeb2eab65dfd1a1e12651d80f5150d06e61a99a0a1ab97b24866cf8f65e198",
            namespace="animation",
            method="blend_space_definition_apply",
            parameters=(
                CommandParameterBinding(
                    name="axes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"axis_index":{"minimum":0,"type":"integer"},"axis_name":{"minLength":1,"type":"string"},"grid_divisions":{"minimum":1,"type":"integer"},"maximum":{"type":"number"},"minimum":{"type":"number"}},"required":["axis_index","axis_name","grid_divisions","maximum","minimum"],"type":"object"},"minItems":1,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="samples",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"animation_ref":{"minLength":1,"type":"string"},"coordinates":{"items":{"type":"number"},"maxItems":3,"minItems":1,"type":"array"},"intent":{"enum":["create","update","replace","delete"],"type":"string"}},"required":["animation_ref","coordinates","intent"],"type":"object"},"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.blend_space.sample",
            binding_hash="sha256:d64689c9b535de358bf44eb41ec5f3431edc6ac43f7e9891744a6b52a77ed638",
            namespace="animation",
            method="blend_space_sample",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"blend_parameters":{"items":{"additionalProperties":false,"properties":{"axis_ref":{"minLength":1,"type":"string"},"value":{"type":"number"}},"required":["axis_ref","value"],"type":"object"},"minItems":1,"type":"array"},"bone_refs":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"output_frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"time_point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["blend_parameters"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.control_rig.asset.create",
            binding_hash="sha256:07af9010ca0abb74a2d04b8176032e5f503022146a8dbce423dc684a6b35a051",
            namespace="animation",
            method="control_rig_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="skeleton_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.control_rig.shape_library.apply",
            binding_hash="sha256:2091ca44a8f8ae4ac9208453d76e44ee90f8b3640218137f745dc6b703fcaa57",
            namespace="animation",
            method="control_rig_shape_library_apply",
            parameters=(
                CommandParameterBinding(
                    name="shapes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"intent":{"enum":["create","update","replace","delete"],"type":"string"},"material_ref":{"minLength":1,"type":"string"},"mesh_ref":{"minLength":1,"type":"string"},"name":{"minLength":1,"type":"string"},"order_index":{"minimum":0,"type":"integer"}},"required":["intent","material_ref","mesh_ref","name","order_index"],"type":"object"},"minItems":1,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.control_rig.shape_library.asset.create",
            binding_hash="sha256:c90f3ab9ab5d906a3f99af27dd70f5788da94c21c00606c3607b3f402587c3ab",
            namespace="animation",
            method="control_rig_shape_library_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.deformer_graph.asset.create",
            binding_hash="sha256:2efbedfb14fd6a8e10fa5266f570b2fe23aa0b4076c7801e001b6d808aca00bc",
            namespace="animation",
            method="deformer_graph_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="skeletal_mesh_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.deformer_graph.topology.apply",
            binding_hash="sha256:a0f79bb19ababcc78b75b8e13e2386f058fd395f48b086cadf7d4981c96b1b3e",
            namespace="animation",
            method="deformer_graph_topology_apply",
            parameters=(
                CommandParameterBinding(
                    name="edits",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"depends_on":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"element_kind":{"enum":["item","pin","relation","order","property"],"minLength":1,"type":"string"},"identity":{"minLength":1,"type":"string"},"intent":{"enum":["create","update","replace","delete"],"minLength":1,"type":"string"},"value":{}},"required":["identity","element_kind","intent"],"type":"object"},"minItems":1,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.deformer_source_library.asset.create",
            binding_hash="sha256:c7c258d1dde420605b421f96f85f078b17c9438cc91a9898b0c74dc1168a6c35",
            namespace="animation",
            method="deformer_source_library_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="concrete_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="disabled",
        ),
        CommandBinding(
            command_id="animation.deformer_source_library.bindings.apply",
            binding_hash="sha256:f0e7bd70ee37a385d643a74cb0b7890261efc6fe7b81dbd45737e15a14caa986",
            namespace="animation",
            method="deformer_source_library_bindings_apply",
            parameters=(
                CommandParameterBinding(
                    name="bindings",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"asset_ref":{"minLength":1,"type":"string"},"binding_key":{"minLength":1,"type":"string"},"intent":{"enum":["create","update","replace","delete"],"type":"string"},"property_type_ref":{"minLength":1,"type":"string"}},"required":["asset_ref","binding_key","intent","property_type_ref"],"type":"object"},"minItems":1,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="concrete_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.ik_probe_candidate.apply",
            binding_hash="sha256:adf5f52e6d49601813d8ebf2f5b9dd9b5d48509b047da455649938312b69ff06",
            namespace="animation",
            method="ik_probe_candidate_apply",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"authored_time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"candidate":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"goal_ref":{"minLength":1,"type":"string"},"rig_ref":{"minLength":1,"type":"string"}},"required":["rig_ref","goal_ref","candidate","authored_time","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ik_retargeter.asset.create",
            binding_hash="sha256:427107d2ee6cbdde544f4e649456a31c5ba604e6a0e42a572b5b454579810e8d",
            namespace="animation",
            method="ik_retargeter_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="source_ik_rig_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ik_rig_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ik_rig.asset.create",
            binding_hash="sha256:99d3aedcbf9408eb37466722c54cb2e79c1b14529fc2f576512e6ab8d283243d",
            namespace="animation",
            method="ik_rig_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="skeletal_mesh_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.ik_rig.definition.auto_generate",
            binding_hash="sha256:048aae1b5f89b60ae98f6d8cdcaf3b6c9e7855287a87cd9ff80cf789403a8d56",
            namespace="animation",
            method="ik_rig_definition_auto_generate",
            parameters=(
                CommandParameterBinding(
                    name="preset",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["humanoid","quadruped","custom"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="skeletal_mesh_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.mesh_deformer_collection.asset.create",
            binding_hash="sha256:dee328196237bef09d5f69148f083b0c10c43c4670b9cfa55d2898985e5e9751",
            namespace="animation",
            method="mesh_deformer_collection_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.mesh_deformer_collection.entries.apply",
            binding_hash="sha256:45d9acc80ad827692bc9ecc6067d94a2efc3ded2f8e6dcf3d51620a6382b78a7",
            namespace="animation",
            method="mesh_deformer_collection_entries_apply",
            parameters=(
                CommandParameterBinding(
                    name="entries",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"entry_kind":{"enum":["deformer","child_collection"],"type":"string"},"entry_ref":{"minLength":1,"type":"string"},"intent":{"enum":["create","update","replace","delete"],"type":"string"},"order_index":{"minimum":0,"type":"integer"}},"required":["entry_kind","entry_ref","intent","order_index"],"type":"object"},"minItems":1,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.ml_deformer.asset.create",
            binding_hash="sha256:8dbc011b0cd72eb690573ec6ce1009f91600668155c8684fab40f68c02634556",
            namespace="animation",
            method="ml_deformer_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="model_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="disabled",
        ),
        CommandBinding(
            command_id="animation.ml_deformer.configuration.apply",
            binding_hash="sha256:e9eee83fdb4ad503c4bcc2d4198bf6dc763aa192b2bd69420d6d5a34213d7f69",
            namespace="animation",
            method="ml_deformer_configuration_apply",
            parameters=(
                CommandParameterBinding(
                    name="animation_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="concrete_model_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="deformer_graph_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"string"}',
                ),
                CommandParameterBinding(
                    name="skeletal_mesh_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_geometry_cache_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.montage.create",
            binding_hash="sha256:97a9bf5fdb3d75eaef83b7db3b889b7a020642963acad9533e280df1b49c46ba",
            namespace="animation",
            method="montage_create",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"destination_ref":{"minLength":1,"type":"string"},"initial_structure":{"additionalProperties":false,"properties":{"bindings":{"items":{"additionalProperties":false,"properties":{"binding_kind":{"enum":["possessable","spawnable","widget","slot"],"type":"string"},"binding_ref":{"minLength":1,"type":"string"},"object_ref":{"minLength":1,"type":"string"},"tags":{"items":{"minLength":1,"type":"string"},"type":"array"},"tracks":{"items":{"additionalProperties":false,"properties":{"property_path":{"type":"string"},"sections":{"items":{"additionalProperties":false,"properties":{"keys":{"items":{"additionalProperties":false,"properties":{"key_ref":{"minLength":1,"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},"value_lexeme":{"type":"string"},"value_type":{"enum":["boolean","integer","decimal","transform","asset_ref","string"],"type":"string"}},"required":["key_ref","time","value_type"],"type":"object"},"type":"array"},"range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"section_kind":{"minLength":1,"type":"string"},"section_ref":{"minLength":1,"type":"string"},"source_ref":{"minLength":1,"type":"string"}},"required":["section_ref","section_kind","range","keys"],"type":"object"},"type":"array"},"track_kind":{"minLength":1,"type":"string"},"track_ref":{"minLength":1,"type":"string"}},"required":["track_ref","track_kind","sections"],"type":"object"},"type":"array"}},"required":["binding_ref","binding_kind","tracks"],"type":"object"},"type":"array"},"display_rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"folders":{"items":{"additionalProperties":false,"properties":{"bindings":{"items":{"type":"string"},"type":"array"},"folder_ref":{"type":"string"},"name":{"minLength":1,"type":"string"},"parent":{"type":"string"},"root_tracks":{"items":{"type":"string"},"type":"array"}},"required":["folder_ref","name"],"type":"object"},"type":"array"},"playback_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"root_tracks":{"items":{"additionalProperties":false,"properties":{"property_path":{"type":"string"},"sections":{"items":{"additionalProperties":false,"properties":{"keys":{"items":{"additionalProperties":false,"properties":{"key_ref":{"minLength":1,"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},"value_lexeme":{"type":"string"},"value_type":{"enum":["boolean","integer","decimal","transform","asset_ref","string"],"type":"string"}},"required":["key_ref","time","value_type"],"type":"object"},"type":"array"},"range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"section_kind":{"minLength":1,"type":"string"},"section_ref":{"minLength":1,"type":"string"},"source_ref":{"minLength":1,"type":"string"}},"required":["section_ref","section_kind","range","keys"],"type":"object"},"type":"array"},"track_kind":{"minLength":1,"type":"string"},"track_ref":{"minLength":1,"type":"string"}},"required":["track_ref","track_kind","sections"],"type":"object"},"type":"array"},"tick_resolution":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"}},"required":["display_rate","tick_resolution","playback_range","bindings","root_tracks"],"type":"object"},"skeleton_ref":{"minLength":1,"type":"string"},"source_animation_ref":{"minLength":1,"type":"string"}},"required":["destination_ref","skeleton_ref","initial_structure"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('projection', 'payload', 'result', 'target_ref'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.montage.read",
            binding_hash="sha256:6ff8fe1bd1f49f9d2a5fc859574260cfa5f024c189609042a3273e8220e44d5e",
            namespace="animation",
            method="montage_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_sections":{"type":"boolean"},"include_slots":{"type":"boolean"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.montage.structure.replace",
            binding_hash="sha256:e5685d46d18e9f772ae8035cc0d12ba09f64354c2f300773b1da705566295fd4",
            namespace="animation",
            method="montage_structure_replace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"structure":{"additionalProperties":false,"properties":{"bindings":{"items":{"additionalProperties":false,"properties":{"binding_kind":{"enum":["possessable","spawnable","widget","slot"],"type":"string"},"binding_ref":{"minLength":1,"type":"string"},"object_ref":{"minLength":1,"type":"string"},"tags":{"items":{"minLength":1,"type":"string"},"type":"array"},"tracks":{"items":{"additionalProperties":false,"properties":{"property_path":{"type":"string"},"sections":{"items":{"additionalProperties":false,"properties":{"keys":{"items":{"additionalProperties":false,"properties":{"key_ref":{"minLength":1,"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},"value_lexeme":{"type":"string"},"value_type":{"enum":["boolean","integer","decimal","transform","asset_ref","string"],"type":"string"}},"required":["key_ref","time","value_type"],"type":"object"},"type":"array"},"range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"section_kind":{"minLength":1,"type":"string"},"section_ref":{"minLength":1,"type":"string"},"source_ref":{"minLength":1,"type":"string"}},"required":["section_ref","section_kind","range","keys"],"type":"object"},"type":"array"},"track_kind":{"minLength":1,"type":"string"},"track_ref":{"minLength":1,"type":"string"}},"required":["track_ref","track_kind","sections"],"type":"object"},"type":"array"}},"required":["binding_ref","binding_kind","tracks"],"type":"object"},"type":"array"},"display_rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"folders":{"items":{"additionalProperties":false,"properties":{"bindings":{"items":{"type":"string"},"type":"array"},"folder_ref":{"type":"string"},"name":{"minLength":1,"type":"string"},"parent":{"type":"string"},"root_tracks":{"items":{"type":"string"},"type":"array"}},"required":["folder_ref","name"],"type":"object"},"type":"array"},"playback_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"root_tracks":{"items":{"additionalProperties":false,"properties":{"property_path":{"type":"string"},"sections":{"items":{"additionalProperties":false,"properties":{"keys":{"items":{"additionalProperties":false,"properties":{"key_ref":{"minLength":1,"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},"value_lexeme":{"type":"string"},"value_type":{"enum":["boolean","integer","decimal","transform","asset_ref","string"],"type":"string"}},"required":["key_ref","time","value_type"],"type":"object"},"type":"array"},"range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"section_kind":{"minLength":1,"type":"string"},"section_ref":{"minLength":1,"type":"string"},"source_ref":{"minLength":1,"type":"string"}},"required":["section_ref","section_kind","range","keys"],"type":"object"},"type":"array"},"track_kind":{"minLength":1,"type":"string"},"track_ref":{"minLength":1,"type":"string"}},"required":["track_ref","track_kind","sections"],"type":"object"},"type":"array"},"tick_resolution":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"}},"required":["display_rate","tick_resolution","playback_range","bindings","root_tracks"],"type":"object"}},"required":["structure","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.sequence.bone_tracks.replace",
            binding_hash="sha256:d5de9605e48c00a796f9ee6b63aa35ca46b0c2cf5589129681666c3d01c3e630",
            namespace="animation",
            method="sequence_bone_tracks_replace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"authored_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"bone_tracks":{"items":{"additionalProperties":false,"properties":{"bone_ref":{"minLength":1,"type":"string"},"keys":{"items":{"additionalProperties":false,"properties":{"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"}},"required":["time","transform"],"type":"object"},"minItems":1,"type":"array"}},"required":["bone_ref","keys"],"type":"object"},"minItems":1,"type":"array"},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"sample_rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"}},"required":["authored_range","sample_rate","bone_tracks","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.sequence.curves.update",
            binding_hash="sha256:ce73d37bfb724db71cde0e0bbc9f08270f65fcc33be3e88b9065d24fafbdabbb",
            namespace="animation",
            method="sequence_curves_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"curve_changes":{"items":{"additionalProperties":false,"properties":{"curve_ref":{"minLength":1,"type":"string"},"keys":{"items":{"additionalProperties":false,"properties":{"interpolation":{"enum":["constant","linear","cubic"],"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"value":{"type":"number"}},"required":["time","value","interpolation"],"type":"object"},"type":"array"},"operation":{"enum":["upsert","remove"],"type":"string"}},"required":["curve_ref","operation","keys"],"type":"object"},"minItems":1,"type":"array"},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"}},"required":["curve_changes","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.sequence.events.update",
            binding_hash="sha256:681461ea7d9aad0eda9bedbb841d0ee3dc1fd8593cf7f9402eb26cb660da7e0d",
            namespace="animation",
            method="sequence_events_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"event_changes":{"items":{"additionalProperties":false,"properties":{"event_kind":{"enum":["notify_track","notify","notify_state","sync_marker"],"type":"string"},"event_ref":{"minLength":1,"type":"string"},"operation":{"enum":["upsert","remove"],"type":"string"},"payload_class_ref":{"minLength":1,"type":"string"},"range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"track_ref":{"minLength":1,"type":"string"}},"required":["event_ref","event_kind","operation"],"type":"object"},"minItems":1,"type":"array"},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"}},"required":["event_changes","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.sequence.metadata.update",
            binding_hash="sha256:93aeb59c1e90a649bcd7247ca2b46032ba00dd4336623ac7467c1eab0399da32",
            namespace="animation",
            method="sequence_metadata_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"metadata_changes":{"items":{"additionalProperties":false,"properties":{"metadata_ref":{"minLength":1,"type":"string"},"operation":{"enum":["upsert","remove"],"type":"string"},"value_lexeme":{"type":"string"},"value_type":{"enum":["string","integer","decimal","boolean","asset_ref"],"type":"string"}},"required":["metadata_ref","operation","value_type","value_lexeme"],"type":"object"},"minItems":1,"type":"array"}},"required":["metadata_changes","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.sequence.pose.sample",
            binding_hash="sha256:a04ee02ef762cb7abb25748ae7ad1e82ccc28c237a304bf04e2a290cc6b0c574",
            namespace="animation",
            method="sequence_pose_sample",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"bone_refs":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"output_frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"time_point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["time_point"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.sequence.read",
            binding_hash="sha256:3f714f43d9d9c94c0c80008852c3907918045c22e3c3a9aae5323857abf445a7",
            namespace="animation",
            method="sequence_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_keys":{"type":"boolean"},"include_tracks":{"type":"boolean"},"temporal_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.sequence.root_motion.analyze",
            binding_hash="sha256:7e6c9f73a468728ffe4912dd59cab9cd0a5eaaedfc7508fc375fb0a0aa3a3a89",
            namespace="animation",
            method="sequence_root_motion_analyze",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"root_bone_ref":{"minLength":1,"type":"string"},"sample_rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"temporal_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"}},"required":["temporal_range","sample_rate"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.skeleton.slots.read",
            binding_hash="sha256:92b095263aa060cef2ca3bb694d1eb839e503c924a48c3e586261f120a1c691b",
            namespace="animation",
            method="skeleton_slots_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="animation.state_machine.candidates",
            binding_hash="sha256:e0b42d3fda528d84a300c3d7450359bacda2b436589dbefd81ca7552f8a39eef",
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
                    name="describe",
                    wire_type="object",
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
            binding_hash="sha256:66678cb77d13d54d67d54ae00cf9cabc4112e06e195ec794db58ab8abadc5c2d",
            namespace="animation",
            method="subject_morph_weights_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"evaluation_point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"morph_weights":{"items":{"additionalProperties":false,"properties":{"morph_ref":{"minLength":1,"type":"string"},"weight":{"type":"number"}},"required":["morph_ref","weight"],"type":"object"},"minItems":1,"type":"array"}},"required":["evaluation_point","morph_weights"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation.subject.pose.update",
            binding_hash="sha256:55e7f074eb603381f11bd4fbca7857ec6e32cbdab4e1e619c8c1169d15c838fa",
            namespace="animation",
            method="subject_pose_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"evaluation_point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"pose":{"items":{"additionalProperties":false,"properties":{"bone_ref":{"minLength":1,"type":"string"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"}},"required":["bone_ref","transform"],"type":"object"},"minItems":1,"type":"array"},"pose_frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"weight":{"maximum":1,"minimum":0,"type":"number"}},"required":["evaluation_point","pose","pose_frame"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="animation_rig_graph.candidates",
            binding_hash="sha256:a47723ccbee458841fca22360b8c6c4dd6184501661c3d6eaec6f83a68c9e719",
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
                    name="describe",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.audio_effect_preset.update",
            binding_hash="sha256:4b3016b76afb6dfe487f442a0e0d594ab81d4ffd7f892e8fd995f042af3ccbf9",
            namespace="asset",
            method="audio_effect_preset_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"settings"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.audio_effect_preset.settings.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"settings"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.collection",
            binding_hash="sha256:3a136a4c61234e689ed6c5c9bd7cfe335f87148fa4112e31634abd31e3841e43",
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
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"collection_kind":{"enum":["rows","items","entries"],"type":"string"},"field_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"key_prefix":{"type":"string"},"keys":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true}},"required":["collection_kind"],"type":"object"}',
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
            binding_hash="sha256:fe0a5ceffaa00330908623aced531a2e834b889ad4ff6559757fd52b275e4043",
            namespace="asset",
            method="curve_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"keys"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.curve.keys.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.data_object.update",
            binding_hash="sha256:5f354965536fa723fea195b229ea2000c8494739eb63b0cfbc72af64739b175a",
            namespace="asset",
            method="data_object_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"registered_fields"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.data_object.registered_fields.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"registered_fields"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.data_table.replace",
            binding_hash="sha256:d4af37a7c1c19f64a3491467edd82f423e3ba0ad1828ad312e176af2820a1af9",
            namespace="asset",
            method="data_table_replace",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"row_struct_ref"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.ref.struct.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"rows"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.data_table.rows.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.delete",
            binding_hash="sha256:5b872f96c3ca242b4f084364f75327cc88749e12ac4eeefe15f6988c549e7333",
            namespace="asset",
            method="delete",
            parameters=(
                CommandParameterBinding(
                    name="targets",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="recursive",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="confirm",
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
            command_id="asset.factory.candidates",
            binding_hash="sha256:aa96d09f71d99536ffc986e7fcd4fe6429be81aa3d8c138ef3ffa9267c6bda1e",
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
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.fixup_redirectors",
            binding_hash="sha256:d65fa05b33c28be4d244d305192102823dab4e49661f8eb5a3899c6d0e270593",
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
                    name="confirm",
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
            command_id="asset.input_action.update",
            binding_hash="sha256:57ee1102c105467ec8777c870cc87434eb6949b8ac250018ce7bd936acd6d313",
            namespace="asset",
            method="input_action_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"value_type"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.asset.input_action.value_type.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"consume_input"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"boolean"},"type_id":{"const":"uai.value.boolean.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"triggers"},"presence":{"enum":["set","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.input_action.triggers.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"triggers"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"modifiers"},"presence":{"enum":["set","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.input_action.modifiers.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"modifiers"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.input_mapping_context.update",
            binding_hash="sha256:c62deab1c556cb511b95adab37896954f230cfd7f38ab63fcff2e0aec9828aab",
            namespace="asset",
            method="input_mapping_context_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"mappings"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.input_mapping_context.mappings.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"mappings"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.media_player.update",
            binding_hash="sha256:55578f31fcade07de43bd1e273ec545f5a8dd50ae1b010e60710655bfa6fc795",
            namespace="asset",
            method="media_player_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"play_on_open"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"boolean"},"type_id":{"const":"uai.value.boolean.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"loop"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"boolean"},"type_id":{"const":"uai.value.boolean.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.media_source.update",
            binding_hash="sha256:fe273659086cf5902788d43592fcbb8288febdea2a3832c955135af2a9a95cc5",
            namespace="asset",
            method="media_source_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"source_uri"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.value.uri.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"source_uri"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"options"},"presence":{"enum":["set","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.media_source.options.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"options"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.media_texture.update",
            binding_hash="sha256:b626368c5a2efbd5eabe718f5f4562f90f656093d393623ac82506af98d463f3",
            namespace="asset",
            method="media_texture_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"media_player_ref"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.ref.asset.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"media_player_ref"},"presence":{"enum":["null","clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"auto_clear"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"boolean"},"type_id":{"const":"uai.value.boolean.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"auto_clear"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"clear_color"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.value.linear_color.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"clear_color"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.move",
            binding_hash="sha256:b5778a9ec1d9f9cb139753d7309b7c416b70e10bb549fec619ba47460df0d621",
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
                    name="confirm",
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
            command_id="asset.object.clone",
            binding_hash="sha256:07ff34327334042a17e58cd0e820b4d545e9dc026423f338adc54dbce44246e3",
            namespace="asset",
            method="object_clone",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="confirm",
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
            command_id="asset.object.create",
            binding_hash="sha256:c4c0edb838868e517e207c21bb7437fe40501da9dcca5c946c47d0eba03cead7",
            namespace="asset",
            method="object_create",
            parameters=(
                CommandParameterBinding(
                    name="factory",
                    wire_type="any",
                    required=True,
                    nullable=False,
                    schema_json='{"oneOf":[{"minLength":1,"type":"string"},{"additionalProperties":false,"properties":{"name":{"minLength":1,"type":"string"},"select":{"additionalProperties":true,"type":"object"}},"required":["name"],"type":"object"}]}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="asset.owned_candidates",
            binding_hash="sha256:079e563d7c5f5be66781cb4922711c667048c3228f19d12ecf290615ec84bbcb",
            namespace="asset",
            method="owned_candidates",
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
                    schema_json='{"additionalProperties":false,"properties":{"property_path":{"minLength":1,"type":"string"},"query":{"type":"string"}},"required":["property_path"],"type":"object"}',
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
            command_id="asset.paper_flipbook.update",
            binding_hash="sha256:3e225c217410e5beb766df9e81b4797bd2cfa967987666775c12ca26f0f298b6",
            namespace="asset",
            method="paper_flipbook_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"frames"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.paper_flipbook.frames.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"frames_per_second"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"number"},"type_id":{"const":"uai.value.decimal.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.paper_sprite.update",
            binding_hash="sha256:8fcd40cfa849a7f1546d53f0c420f33c837f4032b3c059dac5f2ba721a4708b8",
            namespace="asset",
            method="paper_sprite_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"source_texture_ref"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.ref.asset.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"source_texture_ref"},"presence":{"enum":["null","clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"source_region"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.value.rect2d.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"source_region"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"pivot"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.value.vector2d.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"pivot"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.paper_tilemap.update",
            binding_hash="sha256:2b05ff2ac26f84bc83abd39ae156e910161ddded0b6dd628e105f2ddca85b6e1",
            namespace="asset",
            method="paper_tilemap_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"map_size"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.value.extent2i.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"tile_size"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.value.extent2i.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"layers"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.paper_tilemap.layers.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.paper_tileset.update",
            binding_hash="sha256:865d55bd7201c5144e38eec70a64c4aa54c3a4d0bf236fd339168dfd16249938",
            namespace="asset",
            method="paper_tileset_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"source_texture_ref"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.ref.asset.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"tile_size"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.value.extent2i.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"margin"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"integer"},"type_id":{"const":"uai.value.integer.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"spacing"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"integer"},"type_id":{"const":"uai.value.integer.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"terrain"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.paper_tileset.terrain.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.properties",
            binding_hash="sha256:7024f63d21c84df6f54a746e63f956960ba265e4f606ac0c1b4f2bd37ffb6e29",
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
                    schema_json='{"additionalProperties":false,"properties":{"field_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"include_defaults":{"type":"boolean"},"include_presence":{"type":"boolean"}},"type":"object"}',
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
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.registry_record",
            binding_hash="sha256:2bdb53c5d6d550843b08a8a3ed6200ed434d362f68a24af5c79c687e3f27c659",
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
                    schema_json='{"additionalProperties":false,"properties":{"include_chunk_ids":{"type":"boolean"},"include_tags":{"type":"boolean"}},"type":"object"}',
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
            binding_hash="sha256:21684a31c50134e52c05951c1ca5f5a3e56cbb3a84bc2e20d1f9764775d2025e",
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
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"direction":{"enum":["dependencies","referencers","both"],"type":"string"},"relation_kinds":{"items":{"enum":["hard","soft","manage","searchable_name"],"type":"string"},"type":"array","uniqueItems":true}},"required":["direction"],"type":"object"}',
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
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.reimport_sound_wave",
            binding_hash="sha256:4d3ef538d857b21b876c41f8f519427d3a9a8f21b71694b63f6f47860b27a34c",
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
            binding_hash="sha256:b19c2244b9a4c8392567a998360f834ad3b3542162cbe06cce58fcdff947ba36",
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
            binding_hash="sha256:f01fdbf69565d44e913b70edbd9556efbdcf7ccfcdb166a8a36e8f80c5cc86bc",
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
            binding_hash="sha256:c4f2a8ab9fc3d3fc28776b2210a3066a8a4847a01cf58135af336c44cc663312",
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
            binding_hash="sha256:fa60f57ec84564569b8d28461c2a6a758cb2393c0e45bb6d52991e4d679b6bee",
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
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"direction":{"enum":["dependencies","referencers","both"],"type":"string"},"package_scope":{"enum":["all","game","editor_only","build"],"type":"string"},"relation_kinds":{"items":{"enum":["hard","soft","manage","searchable_name"],"type":"string"},"type":"array","uniqueItems":true}},"required":["direction"],"type":"object"}',
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
            command_id="asset.render_target.update",
            binding_hash="sha256:6d455be12c9476513f46e93b9148af29cd638e65b0d78007f6e39e213c795031",
            namespace="asset",
            method="render_target_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"size"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.value.extent2i.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"size"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"format"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.asset.render_target.format.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"format"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"clear_color"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.value.linear_color.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"clear_color"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"auto_generate_mips"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"boolean"},"type_id":{"const":"uai.value.boolean.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"auto_generate_mips"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.runtime_virtual_texture.update",
            binding_hash="sha256:b7543c96580da4446aa6569a189858bd3e463dc3baa1e78c96a0bc2cb9a424bc",
            namespace="asset",
            method="runtime_virtual_texture_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"size"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"integer"},"type_id":{"const":"uai.value.integer.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"material_type"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.asset.runtime_virtual_texture.material_type.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"compression"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"boolean"},"type_id":{"const":"uai.value.boolean.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.sample",
            binding_hash="sha256:3a33c43c0fdea12e3378d51dc93952a408f14890350d298f229019f095ff7172",
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
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"index":{"minimum":0,"type":"integer"},"sample_kind":{"enum":["bounds","vertex"],"type":"string"}},"required":["sample_kind"],"type":"object"}',
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
            binding_hash="sha256:c5fd49fd07a69fdc392c93384ad575c77cf8b5b82470f45168bb1e559755bf58",
            namespace="asset",
            method="skeletal_mesh_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"materials"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.mesh.material_slots.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"lod_settings"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.skeletal_mesh.lod_settings.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"bounds"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.value.box3d.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"skeleton_ref"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.ref.asset.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.sound_attenuation.update",
            binding_hash="sha256:36db5e8343b4494731e2b3868937a8094344b993154072be02d5c0334be03fb3",
            namespace="asset",
            method="sound_attenuation_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"attenuation"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.sound_attenuation.settings.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"attenuation"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.sound_class.update",
            binding_hash="sha256:8eed0b051e59151ceb7d759a94aa668eaec9c7cdb32eed65d4fff0bbe11829dc",
            namespace="asset",
            method="sound_class_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"properties"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.sound_class.properties.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"properties"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"child_classes"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.value.ordered_asset_refs.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"child_classes"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.sound_concurrency.update",
            binding_hash="sha256:5e67743789c1aaf344ea80a9ea2759eabf1a0f854074312d1325f24a3297c86b",
            namespace="asset",
            method="sound_concurrency_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"concurrency"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.sound_concurrency.settings.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"concurrency"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.sound_mix.update",
            binding_hash="sha256:52978648721ba90a88cabf4b016602b8197379ff788f7de16b5f7ab5069556ce",
            namespace="asset",
            method="sound_mix_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"modifiers"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.sound_mix.modifiers.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"modifiers"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"initial_delay"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"number"},"type_id":{"const":"uai.value.decimal.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"initial_delay"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.sound_submix.update",
            binding_hash="sha256:e7a8677add71f94368f161200286e18289f73e9d061a528f4224fef0b4876316",
            namespace="asset",
            method="sound_submix_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"parent"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.ref.asset.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"parent"},"presence":{"enum":["null","clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"effect_chain"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.value.ordered_asset_refs.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"effect_chain"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.sparse_volume_texture.update",
            binding_hash="sha256:a9b3cf326fb5ac00d965a49f22e38ba244a2825ef23e30a0c287476dfe141281",
            namespace="asset",
            method="sparse_volume_texture_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"addressing"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.sparse_volume_texture.addressing.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"addressing"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"streaming"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.sparse_volume_texture.streaming.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"streaming"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.static_mesh.update",
            binding_hash="sha256:777359adee03627725e07d4d0c5619bc8df2c8a6d0acd416dabebbe371d42950",
            namespace="asset",
            method="static_mesh_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"materials"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.mesh.material_slots.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"materials"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"collision"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.static_mesh.collision.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"collision"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"sockets"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.asset.static_mesh.sockets.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"sockets"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"build_settings"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.static_mesh.build_settings.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"build_settings"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.subuv_animation.update",
            binding_hash="sha256:71b960a903f5596a1041910476000ac2f887a24daaae9a28bca698adfe3f7f5a",
            namespace="asset",
            method="subuv_animation_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"source_texture_ref"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.ref.asset.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"source_texture_ref"},"presence":{"enum":["null","clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"grid"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.value.extent2i.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"grid"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"bounding_geometry"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.asset.subuv_animation.bounding_geometry.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"bounding_geometry"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.summary",
            binding_hash="sha256:41a3c4fa4fe852bb08dee42e24c6b0937390fb9e5f11003100ce3539fe592301",
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
                    schema_json='{"additionalProperties":false,"properties":{"include_class_lineage":{"type":"boolean"},"include_package_state":{"type":"boolean"}},"type":"object"}',
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
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.texture_array.replace",
            binding_hash="sha256:2d6e23fc99b204bfacdf72d512d8f21e8f66dfa705980d45ffce3842ff41ce4d",
            namespace="asset",
            method="texture_array_replace",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"source_texture_refs"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.value.ordered_asset_refs.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"format_settings"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.texture.format_settings.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.texture_collection.update",
            binding_hash="sha256:0b8b08d3f64c93b515ee3ed6c7ee5cb4c9536d02b6e246f118f907b997b6614a",
            namespace="asset",
            method="texture_collection_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"texture_refs"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.value.ordered_asset_refs.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"texture_refs"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.texture_cube.replace",
            binding_hash="sha256:3ced9bf27d3c7311408af864a7049612bc4211eb648eecff57155d067398053f",
            namespace="asset",
            method="texture_cube_replace",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"face_texture_refs"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.texture_cube.face_refs.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"format_settings"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.texture.format_settings.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.texture_cube_array.replace",
            binding_hash="sha256:45727073aa1a5832142889b065027823376a380313aafe699990e18602351336",
            namespace="asset",
            method="texture_cube_array_replace",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"source_cube_refs"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.value.ordered_asset_refs.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"format_settings"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.texture.format_settings.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset.validation",
            binding_hash="sha256:a8c6020c3b3746946aa07c41c8bb8ae8779f27b4f18897b60324ae218dd0520e",
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
                    schema_json='{"additionalProperties":false,"properties":{"include_passed":{"type":"boolean"},"rule_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true}},"type":"object"}',
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
            command_id="asset.volume_texture.replace",
            binding_hash="sha256:7e11adc4a195c72acf2a2df880bcb228c26f00cc2eeb7d08b72bc89930fa75e3",
            namespace="asset",
            method="volume_texture_replace",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"slice_texture_refs"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.value.ordered_asset_refs.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"format_settings"},"presence":{"enum":["replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.asset.texture.format_settings.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="asset_durable.journal.read",
            binding_hash="sha256:89501f16bb05e49c493352d31a4ac89bc3c9792379ff3cd9016dd95702854b73",
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
            status="dormant",
        ),
        CommandBinding(
            command_id="asset_durable.journal.reconcile",
            binding_hash="sha256:19b86b73456825a95aaa5986cfbd772fd307fa728853ab6847be17e76b115691",
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
            status="dormant",
        ),
        CommandBinding(
            command_id="audio.graph.candidates",
            binding_hash="sha256:759525db6518609efc5a44ecfc0b53ab5f056bd71de705099a11ffd4131d69bd",
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
                    name="describe",
                    wire_type="object",
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
            binding_hash="sha256:ffcba644c2ca9ad6a496da96a0eea8d0c9bccde029a05f2fc15172437c9d25ea",
            namespace="audio_media",
            method="asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_kind",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["metasound_source","sound_cue","texture_graph"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="blueprint.asset.create",
            binding_hash="sha256:c972c032f1360cde3866611e87a338a4ab9ebbe0791560c2c6301e8b09703666",
            namespace="blueprint",
            method="asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="parent_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="blueprint.component.candidates",
            binding_hash="sha256:51eb276c0641cc4c729ab52be34f826a86eebdd7441b42494185fa821225e00b",
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
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="blueprint.component.events.discover",
            binding_hash="sha256:d8576c1d5db8a8e7af092db4767aa05c22da69108c871f12ac3019c8675dd2a2",
            namespace="blueprint",
            method="component_events_discover",
            parameters=(
                CommandParameterBinding(
                    name="asset_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="compile_before_query",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="component_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="include_hidden",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="only_unbound",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="query",
                    wire_type="string",
                    required=False,
                    nullable=False,
                    schema_json='{"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="blueprint.node.candidates",
            binding_hash="sha256:32daa7accc4e0d9847b0fa2edc434ce2f5c8b51853d998da46f76fa369883310",
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
                    name="graph_name",
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
                    name="node_name",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="node_occurrence",
                    wire_type="integer",
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
                    name="pin_occurrence",
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
            binding_hash="sha256:1214fc766a657fd47497199b44a946fe678eccc34c27a4f3011f9d268ce97994",
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
                    schema_json='{"enum":["policy:image-capture:anim-blueprint/v1","policy:image-capture:asset-preview/v1","policy:image-capture:behavior-tree/v1","policy:image-capture:blueprint/v1","policy:image-capture:control-rig/v1","policy:image-capture:level-sequence/v1","policy:image-capture:metasound/v1","policy:image-capture:pcg-viewport/v1","policy:image-capture:sound-cue/v1","policy:image-capture:state-tree/v1","policy:image-capture:texture/v1","policy:image-capture:transform-candidates/v1","policy:image-capture:umg/v1","policy:image-capture:viewport-buffer/v1","policy:image-capture:viewport-sequence/v1","policy:image-capture:viewport/v1"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="parameters",
                    wire_type="object",
                    required=True,
                    nullable=False,
                ),
            ),
            variants=(
                CommandVariantBinding(
                    variant_id='policy:image-capture:anim-blueprint/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"allow_ui_mutation":{"default":false,"description":"Also permits window mutation.","type":"boolean"},"allow_window_mutation":{"default":false,"type":"boolean"},"asset_path":{"description":"Optional asset path; normally derived from subject_ref.","type":"string"},"capture_height":{"description":"Optional graph draw height; when graph size is requested the native default is 900 pixels.","minimum":1,"type":"integer"},"capture_width":{"description":"Optional graph draw width; when graph size is requested the native default is 1440 pixels.","minimum":1,"type":"integer"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"graph_name":{"default":"EventGraph","type":"string"},"max_size":{"minimum":1,"type":"integer"},"open_editor_if_needed":{"default":false,"type":"boolean"},"output_file":{"type":"string"},"quality":{"default":85,"maximum":100,"minimum":1,"type":"integer"},"restore_graph_view_after_capture":{"default":true,"type":"boolean"},"target":{"default":"viewport","description":"viewport, components, eventgraph/event_graph, graph, graph:<name>, or window.","type":"string"}},"type":"object"},"policy_id":{"const":"policy:image-capture:anim-blueprint/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Capture an Animation Blueprint editor viewport or graph. Opening defaults false; graph or window changes require explicit mutation flags. This captures editor UI, not a PIE animation test.',
                    parameter_guidance='Capture an Animation Blueprint editor viewport or graph. Opening defaults false; graph or window changes require explicit mutation flags. This captures editor UI, not a PIE animation test.',
                    result_guidance='Finish the returned operation, inspect its native result and materialize the image artifacts, then release. Read reported capture scope and any native editor changes.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/Anim/ABP_Example.ABP_Example', policy_id='policy:image-capture:anim-blueprint/v1', parameters={'open_editor_if_needed': True})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:asset-preview/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"mode":{"enum":["single","sequence"],"type":"string"},"target":{"minLength":1,"type":"string"}},"type":"object"},"policy_id":{"const":"policy:image-capture:asset-preview/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary="Capture the requested asset's real preview using its applied HJSON preview configuration. Select single or sequence and an optional target from preview/index.hjson; configure size and sampling in that target's capture.hjson.",
                    parameter_guidance="Capture the requested asset's real preview using its applied HJSON preview configuration. Select single or sequence and an optional target from preview/index.hjson; configure size and sampling in that target's capture.hjson.",
                    result_guidance='Advance to terminal, inspect actual frame times and artifacts, then release.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/Example/M_Material.M_Material', policy_id='policy:image-capture:asset-preview/v1', parameters={'mode': 'single'})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:behavior-tree/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"asset_path":{"description":"Optional asset path; normally derived from subject_ref.","type":"string"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"max_size":{"minimum":1,"type":"integer"},"open_editor_if_needed":{"default":true,"type":"boolean"},"output_file":{"type":"string"},"quality":{"default":90,"maximum":100,"minimum":1,"type":"integer"},"require_non_black":{"default":true,"type":"boolean"}},"type":"object"},"policy_id":{"const":"policy:image-capture:behavior-tree/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Capture the native Behavior Tree editor widget. The editor opens if needed by default; this does not execute the behavior tree.',
                    parameter_guidance='Capture the native Behavior Tree editor widget. The editor opens if needed by default; this does not execute the behavior tree.',
                    result_guidance='Finish the returned operation, inspect its native result and materialize the image artifacts, then release. Read reported capture scope and any native editor changes.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/AI/BT_Example.BT_Example', policy_id='policy:image-capture:behavior-tree/v1', parameters={})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:blueprint/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"allow_ui_mutation":{"default":false,"description":"Also permits window mutation.","type":"boolean"},"allow_window_mutation":{"default":false,"type":"boolean"},"asset_path":{"description":"Optional asset path; normally derived from subject_ref.","type":"string"},"capture_height":{"description":"Optional graph draw height; when graph size is requested the native default is 900 pixels.","minimum":1,"type":"integer"},"capture_width":{"description":"Optional graph draw width; when graph size is requested the native default is 1440 pixels.","minimum":1,"type":"integer"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"graph_name":{"default":"EventGraph","type":"string"},"max_size":{"minimum":1,"type":"integer"},"open_editor_if_needed":{"default":false,"type":"boolean"},"output_file":{"type":"string"},"quality":{"default":85,"maximum":100,"minimum":1,"type":"integer"},"restore_graph_view_after_capture":{"default":true,"type":"boolean"},"target":{"default":"viewport","description":"viewport, components, eventgraph/event_graph, graph, graph:<name>, or window.","type":"string"}},"type":"object"},"policy_id":{"const":"policy:image-capture:blueprint/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Capture a Blueprint editor viewport, component view, graph or window. Opening defaults false. Supply allow_ui_mutation for graph changes and use restore_graph_view_after_capture to restore the graph view.',
                    parameter_guidance='Capture a Blueprint editor viewport, component view, graph or window. Opening defaults false. Supply allow_ui_mutation for graph changes and use restore_graph_view_after_capture to restore the graph view.',
                    result_guidance='Finish the returned operation, inspect its native result and materialize the image artifacts, then release. Read reported capture scope and any native editor changes.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/Blueprints/BP_Example.BP_Example', policy_id='policy:image-capture:blueprint/v1', parameters={'open_editor_if_needed': True})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:control-rig/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"allow_ui_mutation":{"default":false,"description":"Also permits window mutation.","type":"boolean"},"allow_window_mutation":{"default":false,"type":"boolean"},"asset_path":{"description":"Optional asset path; normally derived from subject_ref.","type":"string"},"capture_height":{"description":"Optional graph draw height; when graph size is requested the native default is 900 pixels.","minimum":1,"type":"integer"},"capture_width":{"description":"Optional graph draw width; when graph size is requested the native default is 1440 pixels.","minimum":1,"type":"integer"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"graph_name":{"default":"EventGraph","type":"string"},"graph_name_or_path":{"description":"Alias used when graph_name is omitted.","type":"string"},"max_size":{"minimum":1,"type":"integer"},"open_editor_if_needed":{"default":false,"type":"boolean"},"output_file":{"type":"string"},"quality":{"default":85,"maximum":100,"minimum":1,"type":"integer"},"restore_graph_view_after_capture":{"default":true,"type":"boolean"},"target":{"default":"viewport","description":"viewport, components, eventgraph/event_graph, graph, graph:<name>, or window.","type":"string"}},"type":"object"},"policy_id":{"const":"policy:image-capture:control-rig/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Capture the Control Rig Blueprint editor. graph_name_or_path is an alias for graph_name; graph/window mutations require explicit flags. This does not run a rig evaluation.',
                    parameter_guidance='Capture the Control Rig Blueprint editor. graph_name_or_path is an alias for graph_name; graph/window mutations require explicit flags. This does not run a rig evaluation.',
                    result_guidance='Finish the returned operation, inspect its native result and materialize the image artifacts, then release. Read reported capture scope and any native editor changes.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/Rigs/CR_Example.CR_Example', policy_id='policy:image-capture:control-rig/v1', parameters={'open_editor_if_needed': True})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:level-sequence/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"asset_path":{"description":"Optional asset path; normally derived from subject_ref.","type":"string"},"count":{"default":1,"minimum":1,"type":"integer"},"create_frame_sheet":{"description":"Defaults true for multiple frames. At least sheet or individual output must remain enabled.","type":"boolean"},"display_frame":{"minimum":0,"type":"number"},"fallback_to_viewport_camera":{"default":true,"type":"boolean"},"first_frame_index":{"minimum":0,"type":"number"},"first_time_seconds":{"minimum":0,"type":"number"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"frame":{"minimum":0,"type":"number"},"frame_count":{"minimum":1,"type":"integer"},"frame_index":{"minimum":0,"type":"number"},"frame_interval":{"default":1,"type":"number"},"frame_sheet":{"type":"boolean"},"frame_stride":{"type":"number"},"frames":{"description":"Explicit display-frame numbers or time/frame objects; overrides count/start/interval. Time uses the sequence display rate.","items":{"anyOf":[{"minimum":0,"type":"number"},{"anyOf":[{"required":["time_seconds"]},{"required":["seconds"]},{"required":["frame_index"]},{"required":["frame"]},{"required":["display_frame"]}],"properties":{"display_frame":{"minimum":0,"type":"number"},"frame":{"minimum":0,"type":"number"},"frame_index":{"minimum":0,"type":"number"},"seconds":{"minimum":0,"type":"number"},"time_seconds":{"minimum":0,"type":"number"}},"type":"object"}]},"minItems":1,"type":"array"},"height":{"minimum":1,"type":"integer"},"interval_seconds":{"type":"number"},"keep_individual_frames":{"type":"boolean"},"max_size":{"minimum":1,"type":"integer"},"output_file":{"type":"string"},"output_individual_frames":{"type":"boolean"},"quality":{"default":95,"maximum":100,"minimum":1,"type":"integer"},"sample_count":{"minimum":1,"type":"integer"},"sequence_frame_image":{"type":"boolean"},"start_frame_index":{"minimum":0,"type":"number"},"start_time_seconds":{"minimum":0,"type":"number"},"target":{"default":"viewport","enum":["viewport","camera","sequence_camera"],"type":"string"},"time_interval_seconds":{"type":"number"},"time_seconds":{"minimum":0,"type":"number"},"width":{"minimum":1,"type":"integer"},"write_individual_frames":{"description":"Defaults true for one frame.","type":"boolean"}},"type":"object"},"policy_id":{"const":"policy:image-capture:level-sequence/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Evaluate a Level Sequence at explicit frames/time objects or count/start/interval samples; default is display frame zero. This is an independent final-color scene render with camera post-processing, not a viewport backbuffer screenshot. Viewport fallback borrows camera geometry, not editor rendering state or exposure history. Multiple frames require sheet or individual output.',
                    parameter_guidance='Evaluate a Level Sequence at explicit frames/time objects or count/start/interval samples; default is display frame zero. This is an independent final-color scene render with camera post-processing, not a viewport backbuffer screenshot. Viewport fallback borrows camera geometry, not editor rendering state or exposure history. Multiple frames require sheet or individual output.',
                    result_guidance='Finish the returned operation, inspect its native result and materialize the image artifacts, then release. Read reported capture scope and any native editor changes.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/Cinematics/LS_Example.LS_Example', policy_id='policy:image-capture:level-sequence/v1', parameters={'frames': [0]})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:metasound/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"asset_path":{"description":"Optional asset path; normally derived from subject_ref.","type":"string"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"max_size":{"minimum":1,"type":"integer"},"open_editor_if_needed":{"default":true,"type":"boolean"},"output_file":{"type":"string"},"quality":{"default":90,"maximum":100,"minimum":1,"type":"integer"},"require_non_black":{"default":true,"type":"boolean"}},"type":"object"},"policy_id":{"const":"policy:image-capture:metasound/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Capture the native graph editor for a MetaSound Source or Patch; this is a graph image, not rendered audio.',
                    parameter_guidance='Capture the native graph editor for a MetaSound Source or Patch; this is a graph image, not rendered audio.',
                    result_guidance='Finish the returned operation, inspect its native result and materialize the image artifacts, then release. Read reported capture scope and any native editor changes.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/Audio/MS_Example.MS_Example', policy_id='policy:image-capture:metasound/v1', parameters={})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:pcg-viewport/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"actor":{"description":"Optional framing selector; normally derived from the actor subject. Prefer the exact subject_ref.","type":"string"},"actor_label":{"description":"Framing alias used when actor and actor_name are empty or absent.","type":"string"},"actor_name":{"description":"Framing alias used when actor is empty or absent.","type":"string"},"auto_fallback":{"default":false,"type":"boolean"},"collision_aware":{"default":false,"type":"boolean"},"debug_mode":{"type":"string"},"debug_view_mode":{"type":"string"},"editor_view_mode":{"type":"string"},"fallback_offsets_cm":{"description":"Explicit world-space alternate-view offsets in centimeters. Each vector has three finite components; zero offsets are ignored.","items":{"anyOf":[{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},{"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"}},"required":["components"],"type":"object"}]},"type":"array"},"fallback_step_cm":{"default":200,"description":"Automatic alternate-view step in centimeters; negative values are clamped to zero.","type":"number"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"id":{"description":"Optional framing identity; it must identify the same actor as the subject and other framing selectors.","type":"string"},"look_at":{"default":false,"type":"boolean"},"max_size":{"minimum":1,"type":"integer"},"mode":{"type":"string"},"mode_key":{"type":"string"},"output_file":{"type":"string"},"padding":{"default":1.1,"description":"Multiplier applied to the actor bounds for framing.","type":"number"},"quality":{"default":85,"maximum":100,"minimum":1,"type":"integer"},"render_warmup_frames":{"maximum":2147483647,"minimum":0,"type":"integer"},"restore_view_mode":{"type":"boolean"},"restore_view_mode_after_capture":{"default":true,"type":"boolean"},"safety_offset_cm":{"default":15,"description":"Collision clearance in centimeters; negative values are clamped to zero.","type":"number"},"trace_channel":{"default":"visibility","description":"Case-insensitive visibility, camera, worldstatic/world_static, worlddynamic/world_dynamic, pawn or physicsbody/physics_body; the corresponding ecc_ names are accepted.","type":"string"},"trace_complex":{"default":false,"type":"boolean"},"view_mode":{"type":"string"},"view_mode_family":{"type":"string"},"visualization_family":{"type":"string"},"visualization_mode":{"type":"string"},"visualizer":{"type":"string"},"visualizer_mode":{"type":"string"},"warmup_frames":{"default":2,"maximum":2147483647,"minimum":0,"type":"integer"}},"type":"object"},"policy_id":{"const":"policy:image-capture:pcg-viewport/v1","type":"string"},"subject_ref":{"anyOf":[{"minLength":23,"pattern":"^capture-subject:actor:.+","type":"string"},{"const":"capture-subject:viewport:active","type":"string"}]}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Capture the active level viewport, optionally framing an exact actor first. Use an actor subject for framing or capture-subject:viewport:active to retain the current framing. Camera position/rotation changes remain applied; restore the previous viewport explicitly when needed. This captures visible PCG output and does not generate a PCG graph.',
                    parameter_guidance='Capture the active level viewport, optionally framing an exact actor first. Use an actor subject for framing or capture-subject:viewport:active to retain the current framing. Camera position/rotation changes remain applied; restore the previous viewport explicitly when needed. This captures visible PCG output and does not generate a PCG graph.',
                    result_guidance='Finish the operation, inspect frame_actor and screenshot details and materialize the image artifact, then release. Realtime and temporary view mode follow the viewport capture restoration settings; actor framing does not restore the camera transform.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:actor:<exact-object-path>', policy_id='policy:image-capture:pcg-viewport/v1', parameters={'padding': 1.1, 'look_at': True})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:sound-cue/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"asset_path":{"description":"Optional asset path; normally derived from subject_ref.","type":"string"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"max_size":{"minimum":1,"type":"integer"},"open_editor_if_needed":{"default":true,"type":"boolean"},"output_file":{"type":"string"},"quality":{"default":90,"maximum":100,"minimum":1,"type":"integer"},"require_non_black":{"default":true,"type":"boolean"}},"type":"object"},"policy_id":{"const":"policy:image-capture:sound-cue/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Capture a Sound Cue graph editor widget. The native result also reports node count; no audio playback is implied.',
                    parameter_guidance='Capture a Sound Cue graph editor widget. The native result also reports node count; no audio playback is implied.',
                    result_guidance='Finish the returned operation, inspect its native result and materialize the image artifacts, then release. Read reported capture scope and any native editor changes.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/Audio/SC_Example.SC_Example', policy_id='policy:image-capture:sound-cue/v1', parameters={})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:state-tree/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"asset_path":{"description":"Optional asset path; normally derived from subject_ref.","type":"string"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"max_size":{"minimum":1,"type":"integer"},"open_editor_if_needed":{"default":true,"type":"boolean"},"output_file":{"type":"string"},"quality":{"default":90,"maximum":100,"minimum":1,"type":"integer"},"require_non_black":{"default":true,"type":"boolean"}},"type":"object"},"policy_id":{"const":"policy:image-capture:state-tree/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Capture the native StateTree editor widget. The editor may open if needed; this does not execute the state machine.',
                    parameter_guidance='Capture the native StateTree editor widget. The editor may open if needed; this does not execute the state machine.',
                    result_guidance='Finish the returned operation, inspect its native result and materialize the image artifacts, then release. Read reported capture scope and any native editor changes.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/AI/ST_Example.ST_Example', policy_id='policy:image-capture:state-tree/v1', parameters={})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:texture/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"asset_path":{"description":"Optional texture path; normally derived from subject_ref.","type":"string"},"face":{"default":0,"minimum":0,"type":"integer"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"max_size":{"minimum":1,"type":"integer"},"mip_index":{"default":0,"minimum":0,"type":"integer"},"output_file":{"type":"string"},"require_non_black":{"default":false,"type":"boolean"},"slice":{"default":0,"minimum":0,"type":"integer"}},"type":"object"},"policy_id":{"const":"policy:image-capture:texture/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Read a texture source image at the requested mip, slice and face. Source pixels must be available; max_size optionally resizes the output. No asset editor window is required.',
                    parameter_guidance='Read a texture source image at the requested mip, slice and face. Source pixels must be available; max_size optionally resizes the output. No asset editor window is required.',
                    result_guidance='Finish the returned operation, inspect its native result and materialize the image artifacts, then release. Read reported capture scope and any native editor changes.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/Textures/T_Example.T_Example', policy_id='policy:image-capture:texture/v1', parameters={})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:transform-candidates/v1',
                    request_schema_json='{"$defs":{"rotator":{"additionalProperties":false,"properties":{"pitch":{"type":"number"},"roll":{"type":"number"},"yaw":{"type":"number"}},"required":["pitch","yaw","roll"],"type":"object"},"vector3":{"additionalProperties":false,"properties":{"x":{"type":"number"},"y":{"type":"number"},"z":{"type":"number"}},"required":["x","y","z"],"type":"object"}},"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"candidates":{"items":{"additionalProperties":false,"properties":{"label":{"minLength":1,"type":"string"},"relative_to_original":{"type":"boolean"},"transform":{"additionalProperties":false,"minProperties":1,"properties":{"location":{"$ref":"#/$defs/vector3"},"rotation":{"$ref":"#/$defs/rotator"},"scale":{"$ref":"#/$defs/vector3"}},"type":"object"}},"required":["transform"],"type":"object"},"minItems":1,"type":"array"},"format":{"enum":["png","jpg"],"type":"string"},"frame_sheet_padding":{"minimum":0,"type":"integer"},"max_size":{"minimum":1,"type":"integer"},"output_file":{"minLength":1,"type":"string"},"quality":{"maximum":100,"minimum":1,"type":"integer"},"warmup_frames":{"minimum":0,"type":"integer"}},"required":["candidates"],"type":"object"},"policy_id":{"const":"policy:image-capture:transform-candidates/v1","type":"string"},"subject_ref":{"minLength":23,"pattern":"^capture-subject:actor:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Use subject_ref capture-subject:actor:<exact Actor object path> and provide 1-15 labeled candidates. The policy captures the original plus each candidate from the current Level Viewport into one frame sheet, restores Actor transform, package dirty state, Actor selection, and viewport realtime state, and does not persist or choose a candidate.',
                    parameter_guidance='Use subject_ref capture-subject:actor:<exact Actor object path> and provide 1-15 labeled candidates. The policy captures the original plus each candidate from the current Level Viewport into one frame sheet, restores Actor transform, package dirty state, Actor selection, and viewport realtime state, and does not persist or choose a candidate.',
                    result_guidance='Poll operation.status until terminal. Success publishes one frame-sheet artifact and guarantees the preview state was restored; inspect the sheet, then submit the chosen transform separately and release the operation.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:actor:<exact-object-path>', policy_id='policy:image-capture:transform-candidates/v1', parameters={'candidates': [{'label': 'candidate-1', 'transform': {'location': {'x': 0, 'y': 0, 'z': 0}}}]})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:umg/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"alpha_threshold":{"maximum":255,"minimum":0,"type":"integer"},"asset_path":{"description":"Optional subject alias; must identify the same WidgetBlueprint as subject_ref.","type":"string"},"bounds_alpha_threshold":{"default":0,"maximum":255,"minimum":0,"type":"integer"},"bounds_padding":{"default":0,"minimum":0,"type":"integer"},"capture_height":{"default":1080,"description":"Offscreen canvas height in pixels, before cropping or output resizing.","minimum":1,"type":"integer"},"capture_width":{"default":1920,"description":"Offscreen canvas width in pixels, before cropping or output resizing.","minimum":1,"type":"integer"},"crop":{"additionalProperties":false,"description":"Pixel rectangle in the captured canvas: x/y default to zero; supply width and height. crop_* and left/top/w/h are accepted aliases.","properties":{"crop_height":{"minimum":1,"type":"integer"},"crop_width":{"minimum":1,"type":"integer"},"crop_x":{"type":"integer"},"crop_y":{"type":"integer"},"h":{"minimum":1,"type":"integer"},"height":{"minimum":1,"type":"integer"},"left":{"type":"integer"},"top":{"type":"integer"},"w":{"minimum":1,"type":"integer"},"width":{"minimum":1,"type":"integer"},"x":{"default":0,"type":"integer"},"y":{"default":0,"type":"integer"}},"type":"object"},"crop_height":{"minimum":1,"type":"integer"},"crop_mode":{"default":"auto_bounds","description":"full_canvas preserves the requested canvas. auto_bounds crops transparent margins; a supplied region selects manual_region unless another crop mode is explicit.","enum":["auto_bounds","manual_region","full_canvas","auto","manual","region","full"],"type":"string"},"crop_width":{"minimum":1,"type":"integer"},"crop_x":{"type":"integer"},"crop_y":{"type":"integer"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"h":{"minimum":1,"type":"integer"},"height":{"minimum":1,"type":"integer"},"left":{"type":"integer"},"max_size":{"description":"Optional post-crop output resizing; omit to preserve pixels.","minimum":1,"type":"integer"},"output_file":{"type":"string"},"padding":{"minimum":0,"type":"integer"},"quality":{"default":90,"maximum":100,"minimum":1,"type":"integer"},"region":{"additionalProperties":false,"description":"Pixel rectangle in the captured canvas: x/y default to zero; supply width and height. crop_* and left/top/w/h are accepted aliases.","properties":{"crop_height":{"minimum":1,"type":"integer"},"crop_width":{"minimum":1,"type":"integer"},"crop_x":{"type":"integer"},"crop_y":{"type":"integer"},"h":{"minimum":1,"type":"integer"},"height":{"minimum":1,"type":"integer"},"left":{"type":"integer"},"top":{"type":"integer"},"w":{"minimum":1,"type":"integer"},"width":{"minimum":1,"type":"integer"},"x":{"default":0,"type":"integer"},"y":{"default":0,"type":"integer"}},"type":"object"},"top":{"type":"integer"},"use_project_dpi_scale":{"default":false,"type":"boolean"},"w":{"minimum":1,"type":"integer"},"width":{"minimum":1,"type":"integer"},"x":{"type":"integer"},"y":{"type":"integer"}},"type":"object"},"policy_id":{"const":"policy:image-capture:umg/v1","type":"string"},"subject_ref":{"pattern":"^capture-subject:asset:.+","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Capture a WidgetBlueprint in design-time mode. capture_width/capture_height specify canvas pixels; crop_mode=full_canvas preserves that canvas, while region={x,y,width,height} selects a pixel crop. Omit max_size to avoid output resizing. Set use_project_dpi_scale=true for the project viewport DPI rule. This does not run Construct or validate runtime interaction.',
                    parameter_guidance='Capture a WidgetBlueprint in design-time mode. capture_width/capture_height specify canvas pixels; crop_mode=full_canvas preserves that canvas, while region={x,y,width,height} selects a pixel crop. Omit max_size to avoid output resizing. Set use_project_dpi_scale=true for the project viewport DPI rule. This does not run Construct or validate runtime interaction.',
                    result_guidance='Resume the operation to terminal, read its receipt and materialize the image artifact. The receipt distinguishes design-time rendering, applied DPI scale, canvas and crop. Release the operation after reading artifacts.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:asset:/Game/UI/WBP_Menu.WBP_Menu', policy_id='policy:image-capture:umg/v1', parameters={'capture_width': 1920, 'capture_height': 1080, 'crop_mode': 'full_canvas', 'use_project_dpi_scale': True})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:viewport-buffer/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"buffer":{"default":"SceneDepth","description":"SceneDepth, DeviceDepth, BaseColor or WorldNormal; native aliases are also accepted.","type":"string"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"max_size":{"minimum":1,"type":"integer"},"output_file":{"type":"string"},"quality":{"default":85,"maximum":100,"minimum":1,"type":"integer"}},"type":"object"},"policy_id":{"const":"policy:image-capture:viewport-buffer/v1","type":"string"},"subject_ref":{"const":"capture-subject:viewport:active","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Capture the active level viewport buffer: SceneDepth, DeviceDepth, BaseColor or WorldNormal. The buffer is sampled from the current scene and viewpoint.',
                    parameter_guidance='Capture the active level viewport buffer: SceneDepth, DeviceDepth, BaseColor or WorldNormal. The buffer is sampled from the current scene and viewpoint.',
                    result_guidance='Finish the operation and inspect the buffer image artifact before release.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:viewport:active', policy_id='policy:image-capture:viewport-buffer/v1', parameters={'buffer': 'SceneDepth'})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:viewport-sequence/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"format":{"enum":["png","jpg"],"type":"string"},"frame_count":{"minimum":1,"type":"integer"},"frame_sheet_padding":{"minimum":0,"type":"integer"},"interval_frames":{"minimum":1,"type":"integer"},"max_size":{"minimum":1,"type":"integer"},"output_file":{"minLength":1,"type":"string"},"quality":{"maximum":100,"minimum":1,"type":"integer"},"view_mode":{"minLength":1,"type":"string"},"warmup_frames":{"minimum":0,"type":"integer"}},"type":"object"},"policy_id":{"const":"policy:image-capture:viewport-sequence/v1","type":"string"},"subject_ref":{"const":"capture-subject:viewport:active","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Use exact subject_ref capture-subject:viewport:active. Captures the requested ordered frames across real Editor engine frames from one active Level Viewport and publishes a frame sheet plus raw frame files.',
                    parameter_guidance='Use exact subject_ref capture-subject:viewport:active. Captures the requested ordered frames across real Editor engine frames from one active Level Viewport and publishes a frame sheet plus raw frame files.',
                    result_guidance='Poll operation.status until terminal, then inspect frame_sheet_file_path, raw_frames and capture metadata before releasing the operation.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:viewport:active', policy_id='policy:image-capture:viewport-sequence/v1', parameters={'frame_count': 4, 'interval_frames': 1, 'format': 'png'})",
                ),
                CommandVariantBinding(
                    variant_id='policy:image-capture:viewport/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"debug_mode":{"type":"string"},"debug_view_mode":{"type":"string"},"editor_view_mode":{"type":"string"},"format":{"default":"png","enum":["png","jpg","jpeg"],"type":"string"},"max_size":{"minimum":1,"type":"integer"},"mode":{"type":"string"},"mode_key":{"type":"string"},"output_file":{"type":"string"},"quality":{"default":85,"maximum":100,"minimum":1,"type":"integer"},"render_warmup_frames":{"maximum":2147483647,"minimum":0,"type":"integer"},"restore_view_mode":{"type":"boolean"},"restore_view_mode_after_capture":{"default":true,"type":"boolean"},"view_mode":{"type":"string"},"view_mode_family":{"type":"string"},"visualization_family":{"type":"string"},"visualization_mode":{"type":"string"},"visualizer":{"type":"string"},"visualizer_mode":{"type":"string"},"warmup_frames":{"default":2,"maximum":2147483647,"minimum":0,"type":"integer"}},"type":"object"},"policy_id":{"const":"policy:image-capture:viewport/v1","type":"string"},"subject_ref":{"const":"capture-subject:viewport:active","type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Use exact subject_ref capture-subject:viewport:active. Optional parameters select png/jpg/jpeg output, quality, maximum size, output path, warmup frames and a temporary view mode that is restored after capture.',
                    parameter_guidance='Use exact subject_ref capture-subject:viewport:active. Optional parameters select png/jpg/jpeg output, quality, maximum size, output path, warmup frames and a temporary view mode that is restored after capture.',
                    result_guidance='Poll operation.status until terminal, read latest_signal.payload.artifact_ref, then verify the published image artifact before releasing the operation.',
                    minimum_example="client.capture.image_execute(subject_ref='capture-subject:viewport:active', policy_id='policy:image-capture:viewport/v1', parameters={'format': 'png', 'max_size': 1024, 'restore_view_mode_after_capture': True})",
                ),
            ),
            supports_operation_recovery=True,
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
            supports_operation_recovery=True,
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
            supports_operation_recovery=True,
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="config.resolved_value",
            binding_hash="sha256:f69c8fe557b20c8c99de7479cde228b9fad1dd1a7f5c24a499d9b2ad25d540fd",
            namespace="config",
            method="resolved_value",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"oneOf":[{"additionalProperties":false,"properties":{"config_scope":{"enum":["engine","game","editor","input","device_profiles","scalability","platform"],"type":"string"},"device_profile_id":{"minLength":1,"type":"string"},"key":{"minLength":1,"type":"string"},"platform_id":{"minLength":1,"type":"string"},"section_id":{"minLength":1,"type":"string"}},"required":["config_scope","section_id","key"],"type":"object"},{"additionalProperties":false,"properties":{"editor_project_capability":{"enum":["device_profile.resolve_cvars","target.read"],"type":"string"},"parameters":{"type":"object"}},"required":["editor_project_capability"],"type":"object"}]}',
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
            binding_hash="sha256:83d8e4474f6f2d640ac884567e01c617a2fa4e74759a3b09a49f32f952948852",
            namespace="config",
            method="section",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"oneOf":[{"additionalProperties":false,"properties":{"config_scope":{"enum":["engine","game","editor","input","device_profiles","scalability","platform"],"type":"string"},"keys":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"section_id":{"minLength":1,"type":"string"}},"required":["config_scope","section_id"],"type":"object"},{"additionalProperties":false,"properties":{"editor_project_capability":{"enum":["device_profile.export","device_profile.query","scalability.export","target.read"],"type":"string"},"parameters":{"type":"object"}},"required":["editor_project_capability"],"type":"object"}]}',
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
            command_id="content_graph.compound",
            binding_hash="sha256:8c66ab05b329c0210e70a9c9a07fe4b77da4191aa5bb04b0767b5c428a9e6616",
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
                    schema_json='{"additionalProperties":false,"properties":{"include_closure":{"type":"boolean"},"localization_capability":{"enum":["localization.diff","localization.target.read","localization.culture.read","localization.query_targets","localization.report","localization.validate","string_table.diff","string_table.validate"],"type":"string"},"parameters":{"type":"object"},"roots":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"sections":{"items":{"enum":["summary","structure","items","relations","properties","parameters","diagnostics"],"type":"string"},"type":"array","uniqueItems":true}},"type":"object"}',
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
            binding_hash="sha256:3a7b8b8b5bac941c876f332ab2d48232105d66a1fb4834059729592d519f919b",
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
                    schema_json='{"additionalProperties":false,"properties":{"include_resolved":{"type":"boolean"},"severity":{"items":{"enum":["info","warning","error"],"type":"string"},"type":"array","uniqueItems":true}},"type":"object"}',
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
            binding_hash="sha256:9f3cda6a3027aa429d4daaa7e4e0c40312fc5a09e8db9dfaf4dfb371095a6a60",
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
                CommandParameterBinding(
                    name="source",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"oneOf":[{"additionalProperties":false,"properties":{"document":{"minLength":1,"type":"string"},"kind":{"const":"inline"}},"required":["kind","document"],"type":"object"},{"additionalProperties":false,"properties":{"kind":{"const":"single_file"},"path":{"minLength":1,"type":"string"}},"required":["kind","path"],"type":"object"},{"additionalProperties":false,"properties":{"kind":{"const":"directory"},"path":{"minLength":1,"type":"string"}},"required":["kind","path"],"type":"object"}]}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.import_workspace",
            binding_hash="sha256:18cbd6733dc287d25222670d8069f8861e8e79aded6cd4e31172cac3fed6f928",
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
                    schema_json='{"oneOf":[{"additionalProperties":false,"properties":{"document":{"minLength":1,"type":"string"},"kind":{"const":"inline"}},"required":["kind","document"],"type":"object"},{"additionalProperties":false,"properties":{"kind":{"const":"single_file"},"path":{"minLength":1,"type":"string"}},"required":["kind","path"],"type":"object"},{"additionalProperties":false,"properties":{"kind":{"const":"directory"},"path":{"minLength":1,"type":"string"}},"required":["kind","path"],"type":"object"}]}',
                ),
            ),
            supports_operation_recovery=True,
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="content_graph.items",
            binding_hash="sha256:89c8b79f580e7d8f3c798f1f58aadb666a3f15ac75600e53860fee1b47d7e503",
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
                    schema_json='{"additionalProperties":false,"properties":{"containers":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"fields":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"item_kinds":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"items":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true}},"type":"object"}',
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
            binding_hash="sha256:0d76fae074b1fa49c8304bfbd32db396991b91a4364f9e301bee4ba6958f8367",
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
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"containers":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"fields":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"include_defaults":{"type":"boolean"},"include_presence":{"type":"boolean"},"owners":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true}},"required":["owners"],"type":"object"}',
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
            binding_hash="sha256:7647ebf85faad578b5f9dcc5b880c143a6982e7b500618c5583f858a488e6c64",
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
                    schema_json='{"additionalProperties":false,"properties":{"containers":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"endpoints":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"relation_kinds":{"items":{"enum":["connection","parent","membership","order","reference","transition"],"type":"string"},"type":"array","uniqueItems":true}},"type":"object"}',
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
            binding_hash="sha256:2f148ae3c79ac504984564f5916ca378ad21f82a0df8e0824fa3b23e741671e8",
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
                    schema_json='{"additionalProperties":false,"properties":{"containers":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"include_hierarchy":{"type":"boolean"},"include_order":{"type":"boolean"}},"type":"object"}',
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
            binding_hash="sha256:037c72aca910778784d9aca66e87d8b84aa24f5d52c4f17b1120b72278e713ca",
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
                    schema_json='{"additionalProperties":false,"properties":{"include_counts":{"type":"boolean"},"include_revision":{"type":"boolean"}},"type":"object"}',
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
            binding_hash="sha256:c3cf2bef778606d004457f0d48c974fe352c2f8c3d9049a43c851725da507f31",
            namespace="deformer",
            method="evaluation_sample",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"deformer_ref":{"minLength":1,"type":"string"},"output_frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"sample_time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"enum":["authored","evaluation","simulation"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"subject_ref":{"minLength":1,"type":"string"},"vertex_selector":{"additionalProperties":false,"properties":{"count":{"minimum":1,"type":"integer"},"mode":{"enum":["all","indices","range","refs","tags"],"type":"string"},"refs":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"start":{"minimum":0,"type":"integer"}},"required":["mode"],"type":"object"}},"required":["deformer_ref","subject_ref","sample_time","output_frame"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["runtime_instance"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="deformer.geometry.sample",
            binding_hash="sha256:4d7bcecc3cba9a1d4fd95e89a701b3af7c14e1c71acb1b01015cf89ae037afaf",
            namespace="deformer",
            method="geometry_sample",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"geometry_cache_ref":{"minLength":1,"type":"string"},"output_frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"sample_time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"enum":["authored","evaluation","simulation"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"vertex_selector":{"additionalProperties":false,"properties":{"count":{"minimum":1,"type":"integer"},"mode":{"enum":["all","indices","range","refs","tags"],"type":"string"},"refs":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"start":{"minimum":0,"type":"integer"}},"required":["mode"],"type":"object"}},"required":["geometry_cache_ref","sample_time","output_frame"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["runtime_instance"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="deformer.training_inputs.validate",
            binding_hash="sha256:1e9e13bdf84c411d7072cc57ba1f62c15ebc37665486f2c6b7a41485a9c5aad3",
            namespace="deformer",
            method="training_inputs_validate",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"frame_mappings":{"items":{"additionalProperties":false,"properties":{"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"source_frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"target_frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"}},"required":["source_frame","target_frame","conversion_evidence_ids"],"type":"object"},"minItems":1,"type":"array"},"temporal_ranges":{"items":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower_tick":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"enum":["authored","evaluation","simulation"],"type":"string"},"upper_tick":{"minLength":1,"type":"string"}},"required":["clock_id","lower_tick","upper_tick","rate","state"],"type":"object"},"minItems":1,"type":"array"},"training_input_refs":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true}},"required":["training_input_refs","temporal_ranges","frame_mappings"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor.dirty_resources",
            binding_hash="sha256:b3c6f4d1e93ab24c7479b10ba4e3befcebb3e4f94694892e24807145be83945d",
            namespace="editor",
            method="dirty_resources",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"resource_kinds":{"items":{"enum":["asset","map","config"],"type":"string"},"type":"array","uniqueItems":true}},"type":"object"}',
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
            binding_hash="sha256:9142d2568573ae90eac173508b1412f1c0629cc37dd0dfa508df7df6cdc3f6c3",
            namespace="editor",
            method="open_assets",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_editor_identity":{"type":"boolean"}},"type":"object"}',
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
            supports_operation_recovery=True,
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor.save_resources",
            binding_hash="sha256:9b2b513a63f4b78bf816c79f1a77539fc90d4bba041a50e03f406cc339693d3c",
            namespace="editor",
            method="save_resources",
            parameters=(
                CommandParameterBinding(
                    name="resource_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"minLength":1,"type":"string"},"type":"array"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor.session",
            binding_hash="sha256:7628a6cffa51b3b2b3aa48ad46f234e4d99d28dc9b96a9bc246c1de11760a4e5",
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
            variants=(
                CommandVariantBinding(
                    variant_id='policy:asset-editor:open/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"asset_editor","type":"string"},"parameters":{"additionalProperties":false,"properties":{"ownership":{"default":"managed","enum":["managed","adopt"],"type":"string"}},"type":"object"},"policy_id":{"const":"policy:asset-editor:open/v1","type":"string"},"subject_ref":{"pattern":"^asset:/.*","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Managed ownership closes windows created by UAI, including implicit previews and native reload replacements; existing user windows are borrowed. Use ownership=adopt only to explicitly take responsibility for existing windows of this asset.',
                    parameter_guidance='Managed ownership closes windows created by UAI, including implicit previews and native reload replacements; existing user windows are borrowed. Use ownership=adopt only to explicitly take responsibility for existing windows of this asset.',
                    result_guidance='Wait for active, then cancel and observe actual cleanup. cleanup_pending retains the operation and reports the remaining window; resolve unsaved changes and recover/close again. Shared holders close the window when the final holder releases it.',
                    minimum_example="client.editor.session(family_id='asset_editor', subject_ref='asset:/Game/Example.Example', policy_id='policy:asset-editor:open/v1', parameters={})",
                ),
                CommandVariantBinding(
                    variant_id='policy:asset-editor:preview-action/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"asset_editor","type":"string"},"parameters":{"additionalProperties":false,"properties":{"action":{"enum":["status","focus","reset_view","play","pause","stop","reset","seek"],"type":"string"},"target":{"minLength":1,"type":"string"},"time_seconds":{"type":"number"}},"required":["action"],"type":"object"},"policy_id":{"const":"policy:asset-editor:preview-action/v1","type":"string"},"subject_ref":{"pattern":"^asset:/.*","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Use the exact asset and a preview action advertised by its preview/index.hjson. Stable configuration is edited in the workspace; seek requires time_seconds. Opens the native asset preview if needed and leaves it open.',
                    parameter_guidance='Use the exact asset and a preview action advertised by its preview/index.hjson. Stable configuration is edited in the workspace; seek requires time_seconds. Opens the native asset preview if needed and leaves it open.',
                    result_guidance='Resume to terminal, inspect the native details and release. Release does not close or reset the asset preview. Playback support follows the actual preview owner.',
                    minimum_example="client.editor.session(family_id='asset_editor', subject_ref='asset:/Game/Example.Example', policy_id='policy:asset-editor:preview-action/v1', parameters={'action': 'status'})",
                ),
                CommandVariantBinding(
                    variant_id='policy:modeling-tool:invoke-action/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"modeling_tool","type":"string"},"parameters":{"additionalProperties":false,"properties":{"action_id":{"const":"spawn_transient_box","type":"string"},"size_x":{"default":100,"description":"X dimension in centimeters.","exclusiveMinimum":0,"maximum":100000,"type":"number"},"size_y":{"default":100,"description":"Y dimension in centimeters.","exclusiveMinimum":0,"maximum":100000,"type":"number"},"size_z":{"default":100,"description":"Z dimension in centimeters.","exclusiveMinimum":0,"maximum":100000,"type":"number"}},"required":["action_id"],"type":"object"},"policy_id":{"const":"policy:modeling-tool:invoke-action/v1","type":"string"},"subject_ref":{"const":"modeling-session:operation-local","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='spawn_transient_box creates an operation-owned dynamic mesh at the world origin. Sizes are centimeters, each in (0, 100000]. This is a transient modeling session, not a saved asset.',
                    parameter_guidance='spawn_transient_box creates an operation-owned dynamic mesh at the world origin. Sizes are centimeters, each in (0, 100000]. This is a transient modeling session, not a saved asset.',
                    result_guidance='Observe the active session and close it to destroy the owned transient actor; release only after cleanup completes.',
                    minimum_example="client.editor.session(family_id='modeling_tool', subject_ref='modeling-session:operation-local', policy_id='policy:modeling-tool:invoke-action/v1', parameters={'action_id': 'spawn_transient_box'})",
                ),
                CommandVariantBinding(
                    variant_id='policy:pcg-generation:generate/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"pcg_generation","type":"string"},"parameters":{"additionalProperties":false,"properties":{},"type":"object"},"policy_id":{"const":"policy:pcg-generation:generate/v1","type":"string"},"subject_ref":{"pattern":"^pcg-component:/.+","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Use pcg-component:<exact loaded component_path> from a current-world PCG read and empty parameters. Explicitly generates or regenerates unchanged inputs through native PCG, preserving its cache and editor settings. Requires an active, assigned graph outside preview/runtime generation and no current generation, cleanup or refresh.',
                    parameter_guidance='Use pcg-component:<exact loaded component_path> from a current-world PCG read and empty parameters. Explicitly generates or regenerates unchanged inputs through native PCG, preserving its cache and editor settings. Requires an active, assigned graph outside preview/runtime generation and no current generation, cleanup or refresh.',
                    result_guidance='Finish this finite operation. generation_started and generation_completed refer to this native task, not persisted output. Cancel stops only its owned task and does not roll back partial effects. Successful output remains after release; save the affected map/resources through the existing editor save entry. PCG spatial reads provide independent output inspection.',
                    minimum_example="client.editor.session(family_id='pcg_generation', subject_ref='pcg-component:/Game/Maps/L_Main.L_Main:PersistentLevel.PCGActor.PCGComponent', policy_id='policy:pcg-generation:generate/v1', parameters={})",
                ),
                CommandVariantBinding(
                    variant_id='policy:runtime-session:culture-preview/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"runtime_preview","type":"string"},"parameters":{"additionalProperties":false,"properties":{"culture":{"description":"Registered culture name matching the culture: subject.","minLength":1,"type":"string"},"restore_after":{"default":true,"type":"boolean"},"scope":{"const":"session","default":"session","type":"string"}},"required":["culture"],"type":"object"},"policy_id":{"const":"policy:runtime-session:culture-preview/v1","type":"string"},"subject_ref":{"pattern":"^culture:.+","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Use a registered culture and matching culture:<name> subject. restore_after=true applies and restores immediately; false keeps the preview active until closed.',
                    parameter_guidance='Use a registered culture and matching culture:<name> subject. restore_after=true applies and restores immediately; false keeps the preview active until closed.',
                    result_guidance='Inspect the terminal result for immediate preview, or wait for active and close the retained preview to restore the previous culture.',
                    minimum_example="client.editor.session(family_id='runtime_preview', subject_ref='culture:en', policy_id='policy:runtime-session:culture-preview/v1', parameters={'culture': 'en'})",
                ),
                CommandVariantBinding(
                    variant_id='policy:runtime-session:pie-debug/v2',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"runtime_preview","type":"string"},"parameters":{"additionalProperties":false,"properties":{"local_player_index":{"const":0,"type":"integer"},"viewport_height":{"default":720,"description":"PIE viewport height in physical pixels; session-local, independent of desktop DPI and saved Play window preferences.","maximum":2147483647,"minimum":1,"type":"integer"},"viewport_width":{"default":1280,"description":"PIE viewport width in physical pixels; session-local, independent of desktop DPI and saved Play window preferences.","maximum":2147483647,"minimum":1,"type":"integer"}},"type":"object"},"policy_id":{"const":"policy:runtime-session:pie-debug/v2","type":"string"},"subject_ref":{"pattern":"^runtime-subject:pie:(0|[1-9][0-9]*)$","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Use family_id runtime_preview, one exact runtime-subject:pie:<instance>, this policy_id and optional local_player_index 0. Optional viewport_width/viewport_height are positive physical pixel dimensions, defaulting to 1280/720. They affect only this session, not saved Play window preferences. The operation becomes active only after exact single-PIE/single-player resolution, a verified pause and initial current-workspace publication.',
                    parameter_guidance='Use family_id runtime_preview, one exact runtime-subject:pie:<instance>, this policy_id and optional local_player_index 0. Optional viewport_width/viewport_height are positive physical pixel dimensions, defaulting to 1280/720. They affect only this session, not saved Play window preferences. The operation becomes active only after exact single-PIE/single-player resolution, a verified pause and initial current-workspace publication.',
                    result_guidance='Resume until phase active, then use the SDK-owned RuntimeSessionHandle to execute bounded scenarios. Session identity and pause/workspace fences remain machine-side; cancel this editor session only after scenarios are terminal and released.',
                    minimum_example="client.editor.session(family_id='runtime_preview', subject_ref='runtime-subject:pie:0', policy_id='policy:runtime-session:pie-debug/v2', parameters={'local_player_index': 0})",
                ),
                CommandVariantBinding(
                    variant_id='policy:runtime-session:pie/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"runtime_preview","type":"string"},"parameters":{"additionalProperties":false,"properties":{},"type":"object"},"policy_id":{"const":"policy:runtime-session:pie/v1","type":"string"},"subject_ref":{"pattern":"^runtime-subject:pie:(0|[1-9][0-9]*)$","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Use family_id runtime_preview, subject_ref runtime-subject:pie:<non-negative instance>, this policy_id and an empty parameters object.',
                    parameter_guidance='Use family_id runtime_preview, subject_ref runtime-subject:pie:<non-negative instance>, this policy_id and an empty parameters object.',
                    result_guidance='Resume the returned operation until the PIE session is running; use runtime_instance queries for readback, then cancel, resume to terminal, read the receipt and release.',
                    minimum_example="client.editor.session(family_id='runtime_preview', subject_ref='runtime-subject:pie:0', policy_id='policy:runtime-session:pie/v1', parameters={})",
                ),
                CommandVariantBinding(
                    variant_id='policy:world-context:create-blank/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"world_context","type":"string"},"parameters":{"additionalProperties":false,"properties":{"create_world_partition":{"default":false,"type":"boolean"},"overwrite_policy":{"default":"fail","enum":["fail","reuse","replace"],"type":"string"},"save_existing_map":{"default":true,"type":"boolean"}},"type":"object"},"policy_id":{"const":"policy:world-context:create-blank/v1","type":"string"},"subject_ref":{"minLength":12,"pattern":"^world:/Game/.+","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Use an exact world:/Game/... destination package. fail rejects an existing map, reuse activates it, and replace creates and saves a new blank map at that path. save_existing_map defaults true; create_world_partition affects newly created maps.',
                    parameter_guidance='Use an exact world:/Game/... destination package. fail rejects an existing map, reuse activates it, and replace creates and saves a new blank map at that path. save_existing_map defaults true; create_world_partition affects newly created maps.',
                    result_guidance='Finish the operation and inspect its receipt, then read the current world and dirty resources. The saved map remains after release; reuse does not recreate it.',
                    minimum_example="client.editor.session(family_id='world_context', subject_ref='world:/Game/Maps/L_New', policy_id='policy:world-context:create-blank/v1', parameters={'overwrite_policy': 'fail', 'save_existing_map': True})",
                ),
                CommandVariantBinding(
                    variant_id='policy:world-context:partition-actor-loader/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"world_context","type":"string"},"parameters":{"additionalProperties":false,"anyOf":[{"properties":{"actor_guids":{"minItems":1}},"required":["actor_guids"]},{"properties":{"actor_ids":{"minItems":1}},"required":["actor_ids"]}],"properties":{"actor_guids":{"description":"Actor GUIDs returned by World Partition discovery.","items":{"minLength":1,"type":"string"},"type":"array"},"actor_ids":{"description":"Exact path, name or label of actors in the current world; prefer an unambiguous path.","items":{"minLength":1,"type":"string"},"type":"array"},"dry_run":{"default":false,"type":"boolean"}},"type":"object"},"policy_id":{"const":"policy:world-context:partition-actor-loader/v1","type":"string"},"subject_ref":{"minLength":12,"pattern":"^world:/Game/.+","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='The subject must be the current Editor World with World Partition. Supply at least one discovered actor GUID or current-world actor identity; both arrays may be combined. dry_run validates without loading.',
                    parameter_guidance='The subject must be the current Editor World with World Partition. Supply at least one discovered actor GUID or current-world actor identity; both arrays may be combined. dry_run validates without loading.',
                    result_guidance='Observe the operation-owned loader until active, then close to unload/drain it. Dry-run success does not mean actors were loaded.',
                    minimum_example="client.editor.session(family_id='world_context', subject_ref='world:/Game/Maps/L_Partition', policy_id='policy:world-context:partition-actor-loader/v1', parameters={'actor_ids': ['TargetActor'], 'dry_run': True})",
                ),
                CommandVariantBinding(
                    variant_id='policy:world-context:partition-region-loader/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"world_context","type":"string"},"parameters":{"additionalProperties":false,"properties":{"bounds":{"properties":{"center":{"description":"World-space XYZ center in centimeters.","items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"extent":{"description":"Nonnegative XYZ half-extents in centimeters.","items":{"minimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"}},"required":["center","extent"],"type":"object"},"dry_run":{"default":false,"type":"boolean"},"label":{"default":"UAI_WP_Region","minLength":1,"type":"string"}},"required":["bounds"],"type":"object"},"policy_id":{"const":"policy:world-context:partition-region-loader/v1","type":"string"},"subject_ref":{"minLength":12,"pattern":"^world:/Game/.+","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='The subject must be the current Editor World with World Partition. Supply world-space center and nonnegative half-extents in centimeters. dry_run validates without retaining a loader.',
                    parameter_guidance='The subject must be the current Editor World with World Partition. Supply world-space center and nonnegative half-extents in centimeters. dry_run validates without retaining a loader.',
                    result_guidance='A real loader remains active and owned by the operation. Close it to unload/drain; a dry run terminates with a planned result.',
                    minimum_example="client.editor.session(family_id='world_context', subject_ref='world:/Game/Maps/L_Partition', policy_id='policy:world-context:partition-region-loader/v1', parameters={'bounds': {'center': [0, 0, 0], 'extent': [1000, 1000, 1000]}})",
                ),
                CommandVariantBinding(
                    variant_id='policy:world-context:set-current/v1',
                    request_schema_json='{"additionalProperties":false,"properties":{"family_id":{"const":"world_context","type":"string"},"parameters":{"additionalProperties":false,"properties":{"save_existing_map":{"type":"boolean"}},"type":"object"},"policy_id":{"const":"policy:world-context:set-current/v1","type":"string"},"subject_ref":{"minLength":12,"pattern":"^world:/Game/.+","type":"string"}},"required":["family_id","subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Open or switch the Editor to one existing target map; this variant does not create a map asset.',
                    parameter_guidance='Pass the existing target as subject_ref and optionally save_existing_map; no create or factory parameters are accepted.',
                    result_guidance='accepted means operation registration only. Preserve the original operation_ref and call operation.resume with the latest generation until typed latest_signal reports phase entered/ready; only then is the session usable. After the task, call operation.cancel, operation.resume to a safe boundary until terminal, read operation.receipt, then operation.release.',
                    minimum_example="client.editor.session(family_id='world_context', subject_ref='world:/Game/UAI/Experiments/Foundation/R001/Work/Maps/L_Main', policy_id='policy:world-context:set-current/v1', parameters={'save_existing_map': True})",
                ),
            ),
            supports_operation_recovery=True,
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.config_section.update",
            binding_hash="sha256:28f787aa2de73e68ac74efacc56606f9b82b554668f52d90399935022e38ff14",
            namespace="editor_project",
            method="config_section_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"entries"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.editor_project.config_entry_map.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"entries"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.device_profile.update",
            binding_hash="sha256:aa6fa0be27637fcc5c2de6a63f6a30b5172cf0fa418ee8dabeb24790f8f8b87b",
            namespace="editor_project",
            method="device_profile_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"device_type"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.value.string.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"device_type"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"base_profile_ref"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.value.canonical_ref.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"base_profile_ref"},"presence":{"enum":["null","clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"cvars"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.editor_project.config_entry_map.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"cvars"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.localization_target.update",
            binding_hash="sha256:a8f584c099222e38dda4650eb10a3ecb2b0b6e5fed24203aee214423331eb60c",
            namespace="editor_project",
            method="localization_target_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"native_culture"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.value.culture_name.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"cultures"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.value.culture_name_set.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"cultures"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="editor_project.platform_config.update",
            binding_hash="sha256:411538ca48a4a92ee32231f510d8cbe57c31f04754c1744749e38141c3b3b119",
            namespace="editor_project",
            method="platform_config_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"entries"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.editor_project.config_entry_map.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"entries"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.project_settings.update",
            binding_hash="sha256:ab2c77e44d848682a2a584c9dd8bbc7c9331b7d1c3c761fc5c93c90ee6f3c2f8",
            namespace="editor_project",
            method="project_settings_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"properties"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.editor_project.settings_property_changes.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.scalability_group.update",
            binding_hash="sha256:7f28d4fb4f9c95ffa8165879a687d45023e8f027037df86790cd887e5b09b0bb",
            namespace="editor_project",
            method="scalability_group_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"entries"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"object"},"type_id":{"const":"uai.editor_project.config_entry_map.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"entries"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="editor_project.string_table.update",
            binding_hash="sha256:6897eb7b3d92155a8c5706da2db1680f9863b6286dcea23690fe768d8419bc57",
            namespace="editor_project",
            method="string_table_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"oneOf":[{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"namespace"},"presence":{"enum":["set"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"minLength":1,"type":"string"},"type_id":{"const":"uai.value.string.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"namespace"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]},{"oneOf":[{"additionalProperties":false,"properties":{"field_id":{"const":"entries"},"presence":{"enum":["set","remove","replace"],"minLength":1,"type":"string"},"value":{"additionalProperties":false,"properties":{"canonical_value":{"type":"array"},"type_id":{"const":"uai.editor_project.string_table_entries.v1"}},"required":["type_id","canonical_value"],"type":"object"}},"required":["field_id","presence","value"],"type":"object"},{"additionalProperties":false,"properties":{"field_id":{"const":"entries"},"presence":{"enum":["clear"],"minLength":1,"type":"string"}},"required":["field_id","presence"],"type":"object"}]}]},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="external.fbx.animation.import",
            binding_hash="sha256:958b4b07be89af4885f0bdfce1ece3456c87bc08c90e6638adf32696dca41265",
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
            binding_hash="sha256:1c2f15809ba58efe9f02a477bee7e6f51b5feabcc42fcfd24f09bd41f18f0b6a",
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
            binding_hash="sha256:b0d8ffe4e033b72a4770da1eab27e7e692ae60b9bc1c74713b7b076d7fe8c212",
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
            binding_hash="sha256:e6140373d12bab488578f984f630208deb0ceb4bd967c7f71ba2dea4d0505299",
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
            binding_hash="sha256:a8f3950006b7320298aabf2684070cf1f377e6bdb244d73d5b1f94e9bad7da45",
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
            binding_hash="sha256:b5233cfbb128ce4762ebd6c07100c5ab1e2f27183a01929ae34d536b1f786b52",
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
            binding_hash="sha256:8ddc7c7c3d19cfc8412130d74a0d80993ab9d133b6b321659f5178ce7db7dabe",
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
            binding_hash="sha256:9afe5df6c4bb146b5fa35413c754783c1625ffe58f4dfe76682b4c929db1f102",
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
            binding_hash="sha256:ec83e1cb635cc3b5e864a400915490d3c0b2782a6057b5129cb519c9a018736f",
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
            binding_hash="sha256:34605aecc94f7d97dd22e3fcdcf59a8f63d5cb2b595560470d6e51a9b423f78f",
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
                    name="projection",
                    wire_type="object",
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
            binding_hash="sha256:5abf24f5ba7585626ed153bc9e0a85194fe0edbed73fa643e489edef115adb75",
            namespace="graph",
            method="view_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_document_state":{"type":"boolean"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["asset_editor"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="graph.view.update",
            binding_hash="sha256:b6f88ed5e3a67142615bddc22033e2dd838e1e093694355f0aaf33967166484d",
            namespace="graph",
            method="view_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"save_after_update":{"type":"boolean"},"update_document_state":{"type":"boolean"},"view_state":{"additionalProperties":false,"properties":{"location":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":2,"minItems":2,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":2,"minItems":2,"type":"array"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"zoom":{"exclusiveMinimum":0,"type":"number"}},"required":["location","zoom"],"type":"object"}},"required":["view_state"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["asset_editor"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
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
            supports_operation_recovery=True,
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="landscape.create",
            binding_hash="sha256:2ac04cc2278ddaafaade7592682c3a06be579868a31d648950ccc12fa4fa0b45",
            namespace="landscape",
            method="create",
            parameters=(
                CommandParameterBinding(
                    name="initial_height",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"encoding":{"const":"landscape_local_height"},"value":{"type":"number"}},"required":["encoding","value"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"minLength":1,"type":"string"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"subject_point":{"const":"sample_origin"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["subject_point","frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="sample_region",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"const":"ue.landscape.local_sample_grid"},"max_inclusive":{"items":{"type":"number"},"maxItems":2,"minItems":2,"type":"array"},"min_inclusive":{"items":{"type":"number"},"maxItems":2,"minItems":2,"type":"array"}},"required":["frame_id","min_inclusive","max_inclusive","basis_evidence"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="topology",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"component_count":{"items":{"minimum":1,"type":"number"},"maxItems":2,"minItems":2,"type":"array"},"quads_per_section":{"enum":[7,15,31,63,127,255],"type":"number"},"sections_per_component":{"enum":[1,2],"type":"number"}},"required":["quads_per_section","sections_per_component","component_count"],"type":"object"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="landscape.height.read",
            binding_hash="sha256:ae479315766642fa7b160c0e68e135cda4cca263a5e7067d5ff93dd7cd261dd7",
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
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"region":{"additionalProperties":false,"properties":{"frame_id":{"const":"ue.landscape.local_sample_grid"},"max_inclusive":{"items":{"type":"integer"},"maxItems":2,"minItems":2,"type":"array"},"min_inclusive":{"items":{"type":"integer"},"maxItems":2,"minItems":2,"type":"array"}},"required":["frame_id","min_inclusive","max_inclusive"],"type":"object"},"space_contract":{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"const":"ue.landscape.local_sample_grid"},"unit":{"const":"sample"}},"required":["frame_id","unit","basis_evidence"],"type":"object"}},"required":["region","space_contract"],"type":"object"}',
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
            binding_hash="sha256:e2d7923715d2ae427728f2c56321a4e44f35ea766bcbfda02be57354e4ff6fa2",
            namespace="landscape",
            method="height_delta",
            parameters=(
                CommandParameterBinding(
                    name="delta",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"encoding":{"const":"landscape_local_height_delta"},"row_stride":{"minimum":1,"type":"number"},"values":{"items":{"type":"number"},"minItems":1,"type":"array"}},"required":["encoding","row_stride","values"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="region",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"frame_id":{"const":"ue.landscape.local_sample_grid"},"max_inclusive":{"items":{"type":"number"},"maxItems":2,"minItems":2,"type":"array"},"min_inclusive":{"items":{"type":"number"},"maxItems":2,"minItems":2,"type":"array"}},"required":["frame_id","min_inclusive","max_inclusive"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"expected_scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"read_frame_id":{"const":"ue.landscape.local_sample_grid"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.landscape.local_sample_grid"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","expected_scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="material.expression.candidates",
            binding_hash="sha256:d192a25f21f77771f8b0a70438fcb379bdb0493cd110763b01d3b7278792eefc",
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
                    name="pin_name",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="describe",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="material_instance.asset.create",
            binding_hash="sha256:9de257410d698156c927c315a125d9fa3a12a92a07d22e2fa588b8a376518d21",
            namespace="material_instance",
            method="asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="parent_material_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.attribute.material_slot.add",
            binding_hash="sha256:8c83652b50db518a178797398032cdadc52b59cf678b944bcbe76b6eb84406a4",
            namespace="mesh",
            method="attribute_material_slot_add",
            parameters=(
                CommandParameterBinding(
                    name="material_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="slot_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="mesh.attribute.material_slot.assign",
            binding_hash="sha256:27f357022ec5396b901d354070c871b819cb94bf913ed6a179dd57004121cae9",
            namespace="mesh",
            method="attribute_material_slot_assign",
            parameters=(
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"element_ids":{"items":{"minimum":0,"type":"integer"},"minItems":1,"type":"array","uniqueItems":true},"element_kind":{"const":"triangle"}},"required":["element_kind","element_ids"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="slot_index",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"minimum":0,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="mesh.attribute.normals.recompute",
            binding_hash="sha256:90fa46757903270a391009478e5d61b96d227d348e8dea7e8daea57cf6c1cd6f",
            namespace="mesh",
            method="attribute_normals_recompute",
            parameters=(
                CommandParameterBinding(
                    name="angle_degrees",
                    wire_type="number",
                    required=False,
                    nullable=False,
                    schema_json='{"maximum":180,"minimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["area_angle_weighted","face","angle_threshold"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="preserve_existing_hard_edges",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.attribute.uv.auto",
            binding_hash="sha256:70ae9721878681fbe9d2af151cf1767cd8dabdd2427a7865c37b30d0b255c0c0",
            namespace="mesh",
            method="attribute_uv_auto",
            parameters=(
                CommandParameterBinding(
                    name="island_source",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["polygroups","existing_seams"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="method",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["patch_builder","xatlas"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="pack",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="texture_resolution",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":16384,"minimum":16,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="uv_channel",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":7,"minimum":0,"type":"integer"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.attribute.uv.project",
            binding_hash="sha256:fcfde5c589b5c5d85317bc6d95583441921ff4531d40d8c07256ca48a14b0e91",
            namespace="mesh",
            method="attribute_uv_project",
            parameters=(
                CommandParameterBinding(
                    name="dimensions_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="projection_frame",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"axis_u":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"axis_v":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"axis_w":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"const":"ue.mesh.target_local"},"origin":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["frame_id","unit","origin","axis_u","axis_v","axis_w","basis_evidence"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection_type",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["planar","box","cylindrical"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="uv_channel",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":7,"minimum":0,"type":"integer"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.collision.convex.generate",
            binding_hash="sha256:56e4b958425186a900718955c50a9890424916304ac7b92387548aaa417a455a",
            namespace="mesh",
            method="collision_convex_generate",
            parameters=(
                CommandParameterBinding(
                    name="max_hulls",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":64,"minimum":1,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="max_vertices_per_hull",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":1024,"minimum":4,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["single_hull","decomposition"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="replace_existing",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.collision.simple.generate",
            binding_hash="sha256:06bd01acb879956ba1f6219ecf5b48182ddad0c19e6e5866b327297366687023",
            namespace="mesh",
            method="collision_simple_generate",
            parameters=(
                CommandParameterBinding(
                    name="max_shapes",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":256,"minimum":1,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="method",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["aligned_boxes","min_volume_shapes","capsules","spheres"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="replace_existing",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.element.select_by_ray",
            binding_hash="sha256:6b50e00fe5b448ef9f5f1025e9bdc0c5cc729f259ed9856d0226a766d44ec527",
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
                    schema_json='{"additionalProperties":false,"properties":{"element_kind":{"enum":["vertex","edge","triangle","polygon"],"type":"string"},"screen_point":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":2,"minItems":2,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":2,"minItems":2,"type":"array"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"selection_mode":{"enum":["replace","add","remove"],"type":"string"},"trace_query":{"additionalProperties":false,"properties":{"ignore_target_refs":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"max_distance_cm":{"exclusiveMinimum":0,"type":"number"},"trace_channel":{"minLength":1,"type":"string"},"trace_complex":{"type":"boolean"}},"required":["max_distance_cm","trace_channel","trace_complex","ignore_target_refs"],"type":"object"}},"required":["screen_point","element_kind","selection_mode"],"type":"object"}',
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
            binding_hash="sha256:398cfce494981da4e289d7fbbc23631f14becfb06678a7bb8ebc22ef259119f4",
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
                    schema_json='{"additionalProperties":false,"properties":{"pivot":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"preserve_world_geometry":{"type":"boolean"}},"required":["pivot"],"type":"object"}',
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
            status="dormant",
        ),
        CommandBinding(
            command_id="mesh.primitive.box.create",
            binding_hash="sha256:5fcd7bb6e15df83a6d272b583f35ac257516fee48624742bb8cf539980e10669",
            namespace="mesh",
            method="primitive_box_create",
            parameters=(
                CommandParameterBinding(
                    name="anchor",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["center","base_center"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.world"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"semantic_frame_id":{"minLength":1,"type":"string"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.world"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="size_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="subdivisions",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"maximum":256,"minimum":1,"type":"integer"},"maxItems":3,"minItems":3,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.cylinder.create",
            binding_hash="sha256:4055070022043abccc7911c405b8cda2de9cc2a0ea3ab3f8596c032ad06ebeb5",
            namespace="mesh",
            method="primitive_cylinder_create",
            parameters=(
                CommandParameterBinding(
                    name="anchor",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["center","base_center"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="cap_ends",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="height_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="height_segments",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":256,"minimum":1,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.world"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"semantic_frame_id":{"minLength":1,"type":"string"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.world"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="radial_segments",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":512,"minimum":3,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="radius_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.plane.create",
            binding_hash="sha256:d8443bd759e5fc7df86055484bbee19c7d85a761066fc3ec5428ea55c86cfff0",
            namespace="mesh",
            method="primitive_plane_create",
            parameters=(
                CommandParameterBinding(
                    name="double_sided",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.world"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"semantic_frame_id":{"minLength":1,"type":"string"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.world"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="size_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":2,"minItems":2,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="subdivisions",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"maximum":256,"minimum":1,"type":"integer"},"maxItems":2,"minItems":2,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.ramp.create",
            binding_hash="sha256:a6e92560e378ccf69b8b5dd1ba2412bb88261c74d0609b7e22c024eb323a903d",
            namespace="mesh",
            method="primitive_ramp_create",
            parameters=(
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.world"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"semantic_frame_id":{"minLength":1,"type":"string"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.world"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="rise_direction",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["positive","negative"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="size_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="slope_axis",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["x","y"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.ramp_corner.create",
            binding_hash="sha256:b5192e930a58b61acd145e4dcd3634266e7eb692e30fc7b69f5bcfd89e904fd9",
            namespace="mesh",
            method="primitive_ramp_corner_create",
            parameters=(
                CommandParameterBinding(
                    name="high_corner",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["positive_x_positive_y","positive_x_negative_y","negative_x_positive_y","negative_x_negative_y"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.world"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"semantic_frame_id":{"minLength":1,"type":"string"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.world"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="size_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.sphere.create",
            binding_hash="sha256:09e5d88905f4e8a2cb8c2c849705e09f8d18a2bff8f733ea378edd9be413c00c",
            namespace="mesh",
            method="primitive_sphere_create",
            parameters=(
                CommandParameterBinding(
                    name="latitude_segments",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":256,"minimum":2,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="longitude_segments",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":512,"minimum":3,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.world"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"semantic_frame_id":{"minLength":1,"type":"string"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.world"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="radius_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.primitive.stairs.create",
            binding_hash="sha256:05b1bd9c9cfc104615c3efaacee361f6a90ec2d511a1861a1d4f393fc0afa478",
            namespace="mesh",
            method="primitive_stairs_create",
            parameters=(
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.world"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"semantic_frame_id":{"minLength":1,"type":"string"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.world"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="rise_axis",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["x","y"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="rise_direction",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["positive","negative"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="step_count",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":1024,"minimum":1,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="step_depth_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="step_height_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="step_width_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.boolean",
            binding_hash="sha256:a68bb1467a2adf6040e1b85525c8009c85a02839027c4c1d39e285b6197212af",
            namespace="mesh",
            method="topology_boolean",
            parameters=(
                CommandParameterBinding(
                    name="operand_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="operand_to_target",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"from_frame_id":{"const":"ue.mesh.operand_local"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"to_frame_id":{"const":"ue.mesh.target_local"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["from_frame_id","to_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="operation",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["union","intersection","difference"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="simplify_output",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.edges.bevel",
            binding_hash="sha256:1befe569a87647b6056868380111609d738398bd3c94f342f7c3b62a969d72ef",
            namespace="mesh",
            method="topology_edges_bevel",
            parameters=(
                CommandParameterBinding(
                    name="distance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="roundness",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":1,"minimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="segments",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":64,"minimum":0,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"element_ids":{"items":{"minimum":0,"type":"integer"},"minItems":1,"type":"array","uniqueItems":true},"element_kind":{"const":"edge"}},"required":["element_kind","element_ids"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.edges.weld",
            binding_hash="sha256:2cfd2da98acc89b8f349dac4854824fdebf4b2d6ef65b9fb70f03df9c0f44cef",
            namespace="mesh",
            method="topology_edges_weld",
            parameters=(
                CommandParameterBinding(
                    name="edge_pairs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"items":{"minimum":0,"type":"integer"},"maxItems":2,"minItems":2,"type":"array","uniqueItems":true},"minItems":1,"type":"array","uniqueItems":true}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="tolerance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"minimum":0,"type":"number"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.faces.duplicate",
            binding_hash="sha256:3615145e9d5a90aa0c6f2e6dc80eb2687ed3cf183018f9444fe171bf95177c46",
            namespace="mesh",
            method="topology_faces_duplicate",
            parameters=(
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"element_ids":{"items":{"minimum":0,"type":"integer"},"minItems":1,"type":"array","uniqueItems":true},"element_kind":{"const":"triangle"}},"required":["element_kind","element_ids"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="translation_cm",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.faces.extrude",
            binding_hash="sha256:d56a64917cbb74c9a29e3674ea02fc24f9c11b99919eb15de2d90d01bc2be597",
            namespace="mesh",
            method="topology_faces_extrude",
            parameters=(
                CommandParameterBinding(
                    name="direction",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"const":"ue.mesh.target_local"},"vector":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"}},"required":["frame_id","vector","basis_evidence"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="direction_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["vertex_normals","fixed"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="distance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"number"}',
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"element_ids":{"items":{"minimum":0,"type":"integer"},"minItems":1,"type":"array","uniqueItems":true},"element_kind":{"const":"triangle"}},"required":["element_kind","element_ids"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.faces.inset",
            binding_hash="sha256:04de8ebeec2275f6798ba8ca3e04b2b779bf2ef1292d55cce90f7a5395fbe28b",
            namespace="mesh",
            method="topology_faces_inset",
            parameters=(
                CommandParameterBinding(
                    name="boundary_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["uniform","reprojected"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="distance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"element_ids":{"items":{"minimum":0,"type":"integer"},"minItems":1,"type":"array","uniqueItems":true},"element_kind":{"const":"triangle"}},"required":["element_kind","element_ids"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.faces.offset",
            binding_hash="sha256:0a94723809c94d01a389d2325e5d2db5617176b87944d7065b823cf0d61d3ea3",
            namespace="mesh",
            method="topology_faces_offset",
            parameters=(
                CommandParameterBinding(
                    name="distance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"number"}',
                ),
                CommandParameterBinding(
                    name="offset_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["vertex_normals","face_normals"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"element_ids":{"items":{"minimum":0,"type":"integer"},"minItems":1,"type":"array","uniqueItems":true},"element_kind":{"const":"triangle"}},"required":["element_kind","element_ids"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.faces.push_pull",
            binding_hash="sha256:b5fb2b780effd810d7be8d1957c855dca961b781b919301facb4bf72726ad5ba",
            namespace="mesh",
            method="topology_faces_push_pull",
            parameters=(
                CommandParameterBinding(
                    name="direction",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"const":"ue.mesh.target_local"},"vector":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"}},"required":["frame_id","vector","basis_evidence"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="direction_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["face_normals","fixed"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="distance_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"number"}',
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"element_ids":{"items":{"minimum":0,"type":"integer"},"minItems":1,"type":"array","uniqueItems":true},"element_kind":{"const":"triangle"}},"required":["element_kind","element_ids"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.holes.fill",
            binding_hash="sha256:22ccb362aa2bbc60b0e4dbc346e529f3c9e4b23046e9b38c7162bbbf545b0165",
            namespace="mesh",
            method="topology_holes_fill",
            parameters=(
                CommandParameterBinding(
                    name="fill_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["minimal","triangle_fan","planar"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="selection",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"element_ids":{"items":{"minimum":0,"type":"integer"},"minItems":1,"type":"array","uniqueItems":true},"element_kind":{"const":"boundary_edge"}},"required":["element_kind","element_ids"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.mesh_cut",
            binding_hash="sha256:43674692f4872cf3b4cbbbdc5de78233ce7f711031f58925e15c845cff0f51b5",
            namespace="mesh",
            method="topology_mesh_cut",
            parameters=(
                CommandParameterBinding(
                    name="fill_cut",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="keep_sides",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["both","target_outside","target_inside"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="operand_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="operand_to_target",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"from_frame_id":{"const":"ue.mesh.operand_local"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"to_frame_id":{"const":"ue.mesh.target_local"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["from_frame_id","to_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.mirror",
            binding_hash="sha256:0a1ec2f1fc193518fcb5f97fbc31ae172b3fd66c7edc424aa54027cdb397fb70",
            namespace="mesh",
            method="topology_mirror",
            parameters=(
                CommandParameterBinding(
                    name="keep_original",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="plane",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"const":"ue.mesh.target_local"},"normal":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"origin":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["frame_id","unit","origin","normal","basis_evidence"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="weld_seam",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.plane_cut",
            binding_hash="sha256:96d52f1d0162311a051f6df55d0121af5ed52f4b1bde475cac7ae9f67d6b35e0",
            namespace="mesh",
            method="topology_plane_cut",
            parameters=(
                CommandParameterBinding(
                    name="fill_hole",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="keep_side",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["positive","negative","both"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="plane",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"const":"ue.mesh.target_local"},"normal":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"origin":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["frame_id","unit","origin","normal","basis_evidence"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.remesh",
            binding_hash="sha256:7f49158b02db7a701d259beb80c8437880f950880fe4f45c23242be55463655f",
            namespace="mesh",
            method="topology_remesh",
            parameters=(
                CommandParameterBinding(
                    name="iterations",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":100,"minimum":1,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="preserve_boundaries",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="preserve_sharp_edges",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_edge_length_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.simplify",
            binding_hash="sha256:d53b4d26a645dc8e888c971ba8f01a6d0f3db98b2aed1bc78c998087a3d08b62",
            namespace="mesh",
            method="topology_simplify",
            parameters=(
                CommandParameterBinding(
                    name="preserve_boundaries",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="target_mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["triangle_count","triangle_ratio","tolerance_cm"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_value",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.subdivide",
            binding_hash="sha256:beaaafb4494fc544c9afc13c5d9994a1e1960c2fb91c5d81615577e9b4004722",
            namespace="mesh",
            method="topology_subdivide",
            parameters=(
                CommandParameterBinding(
                    name="levels",
                    wire_type="integer",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":6,"minimum":1,"type":"integer"}',
                ),
                CommandParameterBinding(
                    name="scheme",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["uniform","pn_triangles"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.trim",
            binding_hash="sha256:e5c32bc3e2b66b69e1768599b64b15b015339c2a963508abb2537b73ce1f3ff6",
            namespace="mesh",
            method="topology_trim",
            parameters=(
                CommandParameterBinding(
                    name="fill_hole",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
                CommandParameterBinding(
                    name="keep_region",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["outside","inside"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="operand_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="operand_to_target",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"from_frame_id":{"const":"ue.mesh.operand_local"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"to_frame_id":{"const":"ue.mesh.target_local"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["from_frame_id","to_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.topology.voxel_boolean",
            binding_hash="sha256:09e35cb4d52853c85489db9bb480a1f33b4e99e63372761c1bbbb7f54d7f3c9e",
            namespace="mesh",
            method="topology_voxel_boolean",
            parameters=(
                CommandParameterBinding(
                    name="adaptivity",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"maximum":1,"minimum":0,"type":"number"}',
                ),
                CommandParameterBinding(
                    name="operand_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="operand_to_target",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"from_frame_id":{"const":"ue.mesh.operand_local"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"to_frame_id":{"const":"ue.mesh.target_local"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["from_frame_id","to_frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="operation",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["union","intersection","difference"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="space_contract",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"conversion_chain":{"minLength":1,"type":"string"},"read_frame_id":{"const":"ue.mesh.target_local"},"semantic_frame_id":{"minLength":1,"type":"string"},"unit":{"enum":["centimeter","meter"],"type":"string"},"verify_frame_id":{"minLength":1,"type":"string"},"write_frame_id":{"const":"ue.mesh.target_local"}},"required":["semantic_frame_id","write_frame_id","read_frame_id","verify_frame_id","unit","basis_evidence","conversion_chain"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="voxel_size_cm",
                    wire_type="number",
                    required=True,
                    nullable=False,
                    schema_json='{"exclusiveMinimum":0,"type":"number"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.transform.bake",
            binding_hash="sha256:cc246231ec4b1cae7dffff4b5c6971b014907820fea69ae5c16c2434242c1f97",
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
                    schema_json='{"additionalProperties":false,"properties":{"preserve_placement":{"type":"boolean"},"transform":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":10,"minItems":10,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"transform","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]}},"required":["transform"],"type":"object"}',
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
            binding_hash="sha256:f535576cbac7be45ac5d2debf0d7f01078a3f191ac938838076c873fa69c2bc9",
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
            status="dormant",
        ),
        CommandBinding(
            command_id="mesh.voxel_grid.begin",
            binding_hash="sha256:70f64d17cedfea17d6da4da6fcd8753bf9319a36aee44fed378de52595ed033f",
            namespace="mesh",
            method="voxel_grid_begin",
            parameters=(
                CommandParameterBinding(
                    name="mode",
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
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="mesh.voxel_grid.session",
            binding_hash="sha256:24f68598e3577e6ced9e108f1549b30c4be9cfd577e66858e50eb1792d646cf7",
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
                    name="shape",
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
            status="dormant",
        ),
        CommandBinding(
            command_id="metasound.graph.compile_settle",
            binding_hash="sha256:1a3e78480b5a3594894137dfb014b50c0c409e1c0a54ee9338e31c22fa7f498d",
            namespace="metasound",
            method="graph_compile_settle",
            parameters=(
                CommandParameterBinding(
                    name="registration_policy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["register_and_compile"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="modeling.actor.mesh.replace",
            binding_hash="sha256:f8e5d7029540e202038a33b279a2ccdfff8d4c814abd6f2422dd3550ea39c1cf",
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
                    name="confirm",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="modeling.asset.material_slot.remove",
            binding_hash="sha256:b9a1595e735caddaa49a1a1e344585659f3962ccfa77b09f5f91b0ddbc1a8efa",
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
                    name="confirm",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="modeling.voxel.bounds.remove",
            binding_hash="sha256:f3f4bfe71f0d3f80640f53dff86635ae16b214f8b25f86bb700a99223218d8a9",
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
                    name="confirm",
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
            command_id="niagara.asset.duplicate",
            binding_hash="sha256:837e888a45317e1df345778c80f7d8a519cf14da9e82541c756bc04fe9d9ea06",
            namespace="niagara",
            method="asset_duplicate",
            parameters=(
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.compile_refresh_settle",
            binding_hash="sha256:e47a7ee6bbb9e101133854fe8b50295028634ec0b93a8ac821a218f1ab4cef8b",
            namespace="niagara",
            method="compile_refresh_settle",
            parameters=(
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.compound.apply",
            binding_hash="sha256:68c0ef6121a1874249bd47defe74eac988c3c5ac0c3fc430ea841c2c2608fae4",
            namespace="niagara",
            method="compound_apply",
            parameters=(
                CommandParameterBinding(
                    name="emitter_handle_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="module_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="stage_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="value",
                    wire_type="any",
                    required=True,
                    nullable=False,
                    schema_json='{}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="niagara.emitter.asset.create",
            binding_hash="sha256:d88dbd742981b402643d88c98ade706f4deb83e74aa88ad3194ca725bf713d3a",
            namespace="niagara",
            method="emitter_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.module.candidates",
            binding_hash="sha256:8699e59bc0120ce2170acdc7451ad9acfad937d04a23b93e7abc42568c1b3b42",
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
                    name="emitter_name",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="stage_name",
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
                    name="describe",
                    wire_type="object",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.stack.issue_fix",
            binding_hash="sha256:a93a281e4dc41b49b93116bcd6098fbff2783b3385f20d7618d1c66c93aa274a",
            namespace="niagara",
            method="stack_issue_fix",
            parameters=(
                CommandParameterBinding(
                    name="emitter_handle_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="fix_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="issue_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="niagara.system.asset.create",
            binding_hash="sha256:201352d726b0ffb02fa6c5db9a366996159890d17f54d485b9df46e7c0f74ceb",
            namespace="niagara",
            method="system_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="operation.cancel",
            binding_hash="sha256:108bcbd807bb05c32b808bc82cc908ab58666bc2db4b4ec26f169be1ad63612b",
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
            status="dormant",
        ),
        CommandBinding(
            command_id="operation.discover",
            binding_hash="sha256:fa812be79dd3ba46c44c813830eb1f3133780adb12e6fe4b1c46f0733a886c57",
            namespace="operation",
            method="discover",
            parameters=(
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
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
            binding_hash="sha256:107a041c10c360af0ce395c1a4601c0aae780e89d591c3736099ba5dccb611b1",
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
            status="dormant",
        ),
        CommandBinding(
            command_id="operation.reconcile",
            binding_hash="sha256:e31e23f06e27a77fc10051b2289dde5f2e24a718f8a1639a3df1d5199ff6918c",
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
            status="dormant",
        ),
        CommandBinding(
            command_id="operation.recover",
            binding_hash="sha256:bbfcdfc26715b3d840c98b4217aa08cec2422b429a4dd4bf128096f27efe40f5",
            namespace="operation",
            method="recover",
            parameters=(
                CommandParameterBinding(
                    name="request_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="command_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="operation.release",
            binding_hash="sha256:76d767d9cc74e2d46616baf630720e083864e4990c5e62885845cf24fc9ae2ab",
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
            status="dormant",
        ),
        CommandBinding(
            command_id="operation.resume",
            binding_hash="sha256:392e4a1c979c754f65392f371d4d94a438fb9eab997b0eb0f7c7c638242cea48",
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
            status="dormant",
        ),
        CommandBinding(
            command_id="operation.status",
            binding_hash="sha256:72f297845202a76be465218ea2d9723e65a67632a0db826f5d360640184ea4e9",
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
            status="dormant",
        ),
        CommandBinding(
            command_id="operation.takeover",
            binding_hash="sha256:90ac8972732d85b06dca3b7fdb25dd07b7a167e1d17bac2f47da4acd038c81c3",
            namespace="operation",
            method="takeover",
            parameters=(
                CommandParameterBinding(
                    name="operation_id",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            supports_operation_recovery=True,
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="pcg.component.apply",
            binding_hash="sha256:0fdd99f05cbf2a3e8948faee90b0d712c7315521a0dc282328e21571f7662279",
            namespace="pcg",
            method="component_apply",
            parameters=(
                CommandParameterBinding(
                    name="generation_policy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["on_demand","on_load","runtime"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="graph_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="pcg.component.world_binding.apply",
            binding_hash="sha256:638e36e8e33af85131f58e2bab0acef95ee7b337eca2c217fbc6667d6d1bea1d",
            namespace="pcg",
            method="component_world_binding_apply",
            parameters=(
                CommandParameterBinding(
                    name="actor_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="component_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="generation_policy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["on_demand","on_load","runtime"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="graph_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="pcg.data_asset.apply",
            binding_hash="sha256:99155d74b4792bdf47f7262cb01f8163dac8adfc12e8f6871ac14d3e9ad4e747",
            namespace="pcg",
            method="data_asset_apply",
            parameters=(
                CommandParameterBinding(
                    name="data_type_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="source_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="value",
                    wire_type="any",
                    required=True,
                    nullable=False,
                    schema_json='{}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="pcg.data_asset.create_from_level",
            binding_hash="sha256:a0ffdd6ba5560ed98e7d8479f60f1990cf811f98c9b3e844b825cb48cd9fe57a",
            namespace="pcg",
            method="data_asset_create_from_level",
            parameters=(
                CommandParameterBinding(
                    name="data_type_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="source_level_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.generated_spatial_data.read",
            binding_hash="sha256:0bc8f4b266cce2b4d03dbaa07d2900443865de4a1e718ade006c54e720ecc7db",
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
            command_id="pcg.graph.asset.create",
            binding_hash="sha256:77621aca5aa09a3a6729039f73324cbdac674caa3da7375631705d50ecd0a8a7",
            namespace="pcg",
            method="graph_asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="pcg.graph_instance.apply",
            binding_hash="sha256:331559a4784b0a095963fb311fa2aaf275b3c9c7a4085f4646c22aa65ecbca08",
            namespace="pcg",
            method="graph_instance_apply",
            parameters=(
                CommandParameterBinding(
                    name="graph_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="overrides",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"property_guid":{"minLength":1,"type":"string"},"property_name":{"minLength":1,"type":"string"},"property_type_ref":{"minLength":1,"type":"string"},"value":{}},"required":["property_guid","property_name","property_type_ref","value"],"type":"object"},"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="pcg.node.candidates",
            binding_hash="sha256:25f931b0abb7373291d61ba3f5c8a9b3be4c322a8e4bd5ceeae8a75c0a3b39b3",
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
                    name="describe",
                    wire_type="object",
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
            binding_hash="sha256:afe49373192b4279f840fd000484c3d17f57d2472e1b498e84f31b189959d8a1",
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
            binding_hash="sha256:1e9f259f1bfa204e40f5b76d1d9f6e9ab8372bc4dbf3e9767361fbb39e49a424",
            namespace="physics",
            method="asset_structure_replace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"bodies":{"items":{"additionalProperties":false,"properties":{"body_ref":{"minLength":1,"type":"string"},"bone_ref":{"minLength":1,"type":"string"},"shape_refs":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"state":{"additionalProperties":false,"minProperties":1,"properties":{"collision_enabled":{"enum":["no_collision","query_only","physics_only","query_and_physics"],"type":"string"},"consider_for_bounds":{"type":"boolean"},"mass_kg":{"minLength":1,"type":"string"},"physics_type":{"enum":["default","kinematic","simulated"],"type":"string"}},"type":"object"}},"required":["body_ref","bone_ref","shape_refs","state"],"type":"object"},"minItems":1,"type":"array"},"constraints":{"items":{"additionalProperties":false,"properties":{"constraint_ref":{"minLength":1,"type":"string"},"endpoint_a":{"additionalProperties":false,"properties":{"body_ref":{"minLength":1,"type":"string"},"frame":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":16,"minItems":16,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"}},"required":["body_ref","frame"],"type":"object"},"endpoint_b":{"additionalProperties":false,"properties":{"body_ref":{"minLength":1,"type":"string"},"frame":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":16,"minItems":16,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"}},"required":["body_ref","frame"],"type":"object"},"state":{"additionalProperties":false,"minProperties":1,"properties":{"disable_collision":{"type":"boolean"},"linear_limit_cm":{"minLength":1,"type":"string"},"linear_x_motion":{"enum":["locked","limited","free"],"type":"string"},"linear_y_motion":{"enum":["locked","limited","free"],"type":"string"},"linear_z_motion":{"enum":["locked","limited","free"],"type":"string"},"swing1_limit_degrees":{"minLength":1,"type":"string"},"swing1_motion":{"enum":["locked","limited","free"],"type":"string"},"swing2_limit_degrees":{"minLength":1,"type":"string"},"swing2_motion":{"enum":["locked","limited","free"],"type":"string"},"twist_limit_degrees":{"minLength":1,"type":"string"},"twist_motion":{"enum":["locked","limited","free"],"type":"string"}},"type":"object"}},"required":["constraint_ref","endpoint_a","endpoint_b","state"],"type":"object"},"minItems":1,"type":"array"},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"physics_asset_ref":{"minLength":1,"type":"string"},"profiles":{"items":{"additionalProperties":false,"properties":{"body_refs":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"constraint_refs":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"profile_name":{"minLength":1,"type":"string"}},"required":["profile_name"],"type":"object"},"minItems":1,"type":"array"}},"required":["physics_asset_ref","bodies","constraints","profiles","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="physics.constraint.update",
            binding_hash="sha256:8a51b706ce8c1836073349fc89febaf4942ad9107571be3fb525ed9d9c07b113",
            namespace="physics",
            method="constraint_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"constraint_ref":{"minLength":1,"type":"string"},"constraint_state":{"additionalProperties":false,"minProperties":1,"properties":{"disable_collision":{"type":"boolean"},"linear_limit_cm":{"minLength":1,"type":"string"},"linear_x_motion":{"enum":["locked","limited","free"],"type":"string"},"linear_y_motion":{"enum":["locked","limited","free"],"type":"string"},"linear_z_motion":{"enum":["locked","limited","free"],"type":"string"},"swing1_limit_degrees":{"minLength":1,"type":"string"},"swing1_motion":{"enum":["locked","limited","free"],"type":"string"},"swing2_limit_degrees":{"minLength":1,"type":"string"},"swing2_motion":{"enum":["locked","limited","free"],"type":"string"},"twist_limit_degrees":{"minLength":1,"type":"string"},"twist_motion":{"enum":["locked","limited","free"],"type":"string"}},"type":"object"},"endpoint_a":{"additionalProperties":false,"properties":{"body_ref":{"minLength":1,"type":"string"},"frame":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":16,"minItems":16,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"}},"required":["body_ref","frame"],"type":"object"},"endpoint_b":{"additionalProperties":false,"properties":{"body_ref":{"minLength":1,"type":"string"},"frame":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":16,"minItems":16,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"}},"required":["body_ref","frame"],"type":"object"},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"physics_asset_ref":{"minLength":1,"type":"string"}},"required":["physics_asset_ref","constraint_ref","endpoint_a","endpoint_b","constraint_state","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="physics.material.update",
            binding_hash="sha256:14379448a23dd6af4eea23e3d7bedb079b74572e8a9a97c2c9b6088947f3d91d",
            namespace="physics",
            method="material_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"material_state":{"additionalProperties":false,"minProperties":1,"properties":{"density":{"minLength":1,"type":"string"},"friction":{"minLength":1,"type":"string"},"friction_combine_mode":{"enum":["average","min","multiply","max"],"type":"string"},"raise_mass_to_power":{"minLength":1,"type":"string"},"restitution":{"minLength":1,"type":"string"},"restitution_combine_mode":{"enum":["average","min","multiply","max"],"type":"string"},"static_friction":{"minLength":1,"type":"string"}},"type":"object"},"physical_material_ref":{"minLength":1,"type":"string"}},"required":["physical_material_ref","material_state","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="physics.simulation.probe",
            binding_hash="sha256:d868f00cfa3d8ba914ecd62465b9ac0164ef7ebeb0b363e7ae2bfffac15f4a0a",
            namespace="physics",
            method="simulation_probe",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"impulses":{"items":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"subject_ref":{"minLength":1,"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"enum":["authored","evaluation","simulation"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["subject_ref","time","frame","components","evidence_ids"],"type":"object"},"minItems":1,"type":"array"},"simulation_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower_tick":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"enum":["authored","evaluation","simulation"],"type":"string"},"upper_tick":{"minLength":1,"type":"string"}},"required":["clock_id","lower_tick","upper_tick","rate","state"],"type":"object"},"simulation_session":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"owner_ref":{"minLength":1,"type":"string"},"session_id":{"minLength":1,"type":"string"}},"required":["session_id","owner_ref","generation"],"type":"object"},"subject_refs":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"velocities":{"items":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"subject_ref":{"minLength":1,"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"enum":["authored","evaluation","simulation"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["subject_ref","time","frame","components","evidence_ids"],"type":"object"},"minItems":1,"type":"array"}},"required":["subject_refs","simulation_session","simulation_range"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["runtime_instance"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="project.platform",
            binding_hash="sha256:e6e590388a49ac0e4dda9346433762bf80775b67547889f72a98b40d82ce1cd7",
            namespace="project",
            method="platform",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"oneOf":[{"additionalProperties":false,"properties":{"field_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"platform_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"resolve_inheritance":{"type":"boolean"}},"type":"object"},{"additionalProperties":false,"properties":{"editor_project_capability":{"enum":["platform_config.export","target_platform.query","target.read"],"type":"string"},"parameters":{"type":"object"}},"required":["editor_project_capability"],"type":"object"}]}',
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
            binding_hash="sha256:0cfc146c88a361dff864679a0482f5ac91d218aa00d38b05d385fc47d5cfae59",
            namespace="project",
            method="settings",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"oneOf":[{"additionalProperties":false,"properties":{"field_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"include_defaults":{"type":"boolean"},"section_id":{"minLength":1,"type":"string"}},"required":["section_id"],"type":"object"},{"additionalProperties":false,"properties":{"editor_project_capability":{"enum":["project_settings.index","project_settings.page","target.read"],"type":"string"},"parameters":{"type":"object"}},"required":["editor_project_capability"],"type":"object"}]}',
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
            binding_hash="sha256:e08f30b089c063cc163776a9f0da5e9e9d3043f24497c67e7d2660b337e3c6f6",
            namespace="project",
            method="summary",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{},"type":"object"}',
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
            binding_hash="sha256:725f04a1086921a399c52329c857148448a0464d35f5c3b1db163500df53f9b6",
            namespace="project",
            method="validation",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"oneOf":[{"additionalProperties":false,"properties":{"include_passed":{"type":"boolean"},"rule_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"section_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true}},"type":"object"},{"additionalProperties":false,"properties":{"editor_project_capability":{"enum":["device_profile.diff","device_profile.validate","platform_config.validate","platform_profile.validate_packaging","project_settings.diff","project_settings.validate","scalability.validate","target.read"],"type":"string"},"parameters":{"type":"object"}},"required":["editor_project_capability"],"type":"object"}]}',
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
            command_id="query.command.search",
            binding_hash="sha256:16c66c396f88cd2f747e179e314ff4f2f7d1a4dd233e92184fc612194fd188b3",
            namespace="query",
            method="command_search",
            parameters=(
                CommandParameterBinding(
                    name="intent",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="query.command.usage",
            binding_hash="sha256:73646b68a467f61ae2d45dd6440be76049432e5bdaff7b5d5f17bf6b8255eb53",
            namespace="query",
            method="command_usage",
            parameters=(
                CommandParameterBinding(
                    name="commands",
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
            command_id="query.content.search",
            binding_hash="sha256:1ff277d2be905e08939816f367507fd683db0eb1a116f1cbf6ef7f7bc151efa1",
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
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="reference.origin.resolve",
            binding_hash="sha256:b805c3b79be3ecffa579863b4c93d4ca98b2053078a308805fdad43d74eb30f4",
            namespace="reference",
            method="origin_resolve",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"target":{"additionalProperties":false,"properties":{"asset_path":{"minLength":1,"type":"string"},"candidate_id":{"minLength":1,"type":"string"},"full_name":{"minLength":1,"type":"string"},"graph_name":{"minLength":1,"type":"string"},"json_file":{"minLength":1,"type":"string"},"json_pointer":{"minLength":1,"type":"string"},"kind":{"minLength":1,"type":"string"},"name":{"minLength":1,"type":"string"},"node_guid":{"minLength":1,"type":"string"},"source":{"enum":["catalog_candidate","json_reference","ue_object","graph_node","name_reference"],"type":"string"}},"required":["source"],"type":"object"}},"required":["target"],"type":"object"}',
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
            binding_hash="sha256:4fddae9f46689978b0a5fe9289016e46b88dd56688e240cd7172fb68788e36f0",
            namespace="rig",
            method="control_bake_animation",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"authored_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower_tick":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"enum":["authored","evaluation","simulation"],"type":"string"},"upper_tick":{"minLength":1,"type":"string"}},"required":["clock_id","lower_tick","upper_tick","rate","state"],"type":"object"},"binding_ref":{"minLength":1,"type":"string"},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"rig_ref":{"minLength":1,"type":"string"},"sample_rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"source_sequence_ref":{"minLength":1,"type":"string"},"target_animation_ref":{"minLength":1,"type":"string"}},"required":["source_sequence_ref","target_animation_ref","binding_ref","rig_ref","authored_range","sample_rate","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.control.bake.controls",
            binding_hash="sha256:44f2f60492d5a0f7e0068cdef895e60db36250b6a793d6f6f13590a92b56ee14",
            namespace="rig",
            method="control_bake_controls",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"authored_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower_tick":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"enum":["authored","evaluation","simulation"],"type":"string"},"upper_tick":{"minLength":1,"type":"string"}},"required":["clock_id","lower_tick","upper_tick","rate","state"],"type":"object"},"binding_ref":{"minLength":1,"type":"string"},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"rig_ref":{"minLength":1,"type":"string"},"sample_rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"target_sequence_ref":{"minLength":1,"type":"string"}},"required":["target_sequence_ref","binding_ref","rig_ref","authored_range","sample_rate","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.ik.definition.update",
            binding_hash="sha256:74b2e9386bac9dfa94580cb226b5872e088db07d27b89e750ce8f0f8c6a198c5",
            namespace="rig",
            method="ik_definition_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"definition_changes":{"items":{"additionalProperties":false,"properties":{"kind":{"enum":["retarget_root","goal","retarget_chain","solver","preview_mesh"],"type":"string"},"operation":{"enum":["set","remove"],"type":"string"},"primary_ref":{"minLength":1,"type":"string"},"secondary_ref":{"minLength":1,"type":"string"},"solver_kind":{"enum":["full_body_ik","pole","set_transform","body_mover"],"type":"string"},"tertiary_ref":{"minLength":1,"type":"string"}},"required":["kind","operation","primary_ref"],"type":"object"},"minItems":1,"type":"array"},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"ik_rig_ref":{"minLength":1,"type":"string"},"preview_context":{"additionalProperties":false,"properties":{"preview_mesh_ref":{"minLength":1,"type":"string"}},"required":["preview_mesh_ref"],"type":"object"}},"required":["ik_rig_ref","definition_changes","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="rig.retarget.assets.generate",
            binding_hash="sha256:1721c088aa3463999fd5d078046c32348b4d920d47481b0121044c7f01c88b6c",
            namespace="rig",
            method="retarget_assets_generate",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"asset_requests":{"items":{"additionalProperties":false,"properties":{"asset_kind":{"minLength":1,"type":"string"},"name":{"minLength":1,"type":"string"},"overwrite_policy":{"enum":["fail","replace"],"type":"string"}},"required":["asset_kind","name","overwrite_policy"],"type":"object"},"minItems":1,"type":"array"},"destination_root":{"minLength":1,"type":"string"},"retargeter_ref":{"minLength":1,"type":"string"},"source_subject_ref":{"minLength":1,"type":"string"},"target_subject_ref":{"minLength":1,"type":"string"}},"required":["source_subject_ref","target_subject_ref","retargeter_ref","destination_root","asset_requests"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="generated_asset_refs",
                    source_path=('projection', 'payload', 'result', 'generated_asset_refs'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.retarget.definition.update",
            binding_hash="sha256:1de68810dcf3ac812632c7752cb560dfb339d8e7e2bf92508df268c002d7a0cd",
            namespace="rig",
            method="retarget_definition_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"chain_mappings":{"items":{"additionalProperties":false,"properties":{"goal_ref":{"minLength":1,"type":"string"},"source_chain_ref":{"minLength":1,"type":"string"},"target_chain_ref":{"minLength":1,"type":"string"}},"required":["source_chain_ref","target_chain_ref"],"type":"object"},"minItems":1,"type":"array"},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"retargeter_ref":{"minLength":1,"type":"string"},"source_rig_ref":{"minLength":1,"type":"string"},"target_rig_ref":{"minLength":1,"type":"string"}},"required":["retargeter_ref","source_rig_ref","target_rig_ref","chain_mappings","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="rig.retarget.pose.auto_align",
            binding_hash="sha256:2da3784c91135906120c1019a1e6cb6d07ad6bce3ffc40ea32e2b85c59a6a786",
            namespace="rig",
            method="retarget_pose_auto_align",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"alignment_policy":{"enum":["root","chain","full_pose"],"type":"string"},"bone_refs":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"retargeter_ref":{"minLength":1,"type":"string"},"subject_side":{"enum":["source","target"],"type":"string"}},"required":["retargeter_ref","subject_side","alignment_policy","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="rig.retarget.pose.update",
            binding_hash="sha256:933e10190bee674af1f626380124609a75a10617618632a37b0ab46ad382765b",
            namespace="rig",
            method="retarget_pose_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"pose":{"items":{"additionalProperties":false,"properties":{"bone_ref":{"minLength":1,"type":"string"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":16,"minItems":16,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"}},"required":["bone_ref","transform"],"type":"object"},"minItems":1,"type":"array"},"pose_frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"retargeter_ref":{"minLength":1,"type":"string"},"subject_side":{"enum":["source","target"],"type":"string"}},"required":["retargeter_ref","subject_side","pose","pose_frame","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="rig.skeleton.preview_mesh.bind",
            binding_hash="sha256:9355f0843e2335de53f59f45c29cb9961d5a5a2d51de740a53d01ca4fc87d5e0",
            namespace="rig",
            method="skeleton_preview_mesh_bind",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"preview_mesh_ref":{"minLength":1,"type":"string"},"skeleton_ref":{"minLength":1,"type":"string"}},"required":["skeleton_ref","preview_mesh_ref","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="rig.skeleton.socket.update",
            binding_hash="sha256:939a9ab5d5ab499247586c0974af566b2b7a695a44b26651994db34e8ef55894",
            namespace="rig",
            method="skeleton_socket_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"operation":{"enum":["create","update","remove"],"type":"string"},"parent_bone_ref":{"minLength":1,"type":"string"},"skeleton_ref":{"minLength":1,"type":"string"},"socket_ref":{"minLength":1,"type":"string"},"socket_transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":16,"minItems":16,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"}},"required":["skeleton_ref","operation","socket_ref","parent_bone_ref","socket_transform","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="runtime.scenario.execute",
            binding_hash="sha256:da34aaec598b724510a3f85307cc97e3fb750b7440a78c6e708ee0c54b5c3aeb",
            namespace="runtime",
            method="scenario_execute",
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
            variants=(
                CommandVariantBinding(
                    variant_id='policy:runtime-scenario:bounded/v2',
                    request_schema_json='{"additionalProperties":false,"properties":{"parameters":{"additionalProperties":false,"properties":{"expected_pause_epoch":{"minimum":1,"type":"integer"},"expected_workspace_revision":{"minimum":1,"type":"integer"},"limits":{"additionalProperties":false,"properties":{"frame_count":{"minimum":0,"type":"integer"},"game_seconds":{"minimum":0,"type":"number"},"wall_seconds":{"minimum":0,"type":"number"}},"type":"object"},"observation_fields":{"items":{"type":"object"},"type":"array"},"steps":{"items":{"additionalProperties":false,"properties":{"action_ref":{"type":"string"},"alias":{"type":"string"},"amount":{"type":"number"},"at_seconds":{"minimum":0,"type":"number"},"camera":{"type":"string"},"delta":{},"duration":{"minimum":0,"type":"number"},"duration_ms":{"minimum":0,"type":"number"},"event":{"type":"string"},"format":{"type":"string"},"fov_degrees":{"type":"number"},"interval":{"minimum":0,"type":"number"},"key":{"type":"string"},"name":{"type":"string"},"position":{"items":{"type":"number"},"maxItems":2,"minItems":2,"type":"array"},"property":{"type":"string"},"ref":{"type":"object"},"source":{"type":"string"},"text":{"type":"string"},"transform":{"type":"object"},"type":{"enum":["wait","input_key","input_pointer","input_scroll","input_text","input_action","actor_transform","property_write","property_get","property_set","capture","capture_start","capture_stop"],"type":"string"},"value":{},"view_transform":{"type":"object"}},"required":["type"],"type":"object"},"type":"array"},"unwatch_refs":{"items":{"type":"object"},"type":"array"},"watch_refs":{"items":{"type":"object"},"type":"array"}},"required":["expected_pause_epoch","expected_workspace_revision","steps"],"type":"object"},"policy_id":{"const":"policy:runtime-scenario:bounded/v2"},"subject_ref":{"minLength":1,"type":"string"}},"required":["subject_ref","policy_id","parameters"],"type":"object"}',
                    summary='Run one bounded PIE scenario from one verified pause barrier to the next.',
                    parameter_guidance='Use only the activation descriptor request schema and aliases from the latest Current HJSON. property reads and writes use the common typed value wrapper; actor transforms and existing scene cameras use the same session alias resolver. input_action accepts exact UInputAction asset refs with bool, Axis1D, Axis2D or Axis3D samples. capture selects pie_output_surface, the evaluated pie_player_camera, or an aliased/operation-owned transient scene_camera; only scene_camera accepts a transient pose or FOV.',
                    result_guidance='Observe the typed operation until terminal; SDK custody refreshes the runtime-session handle.',
                    minimum_example='result.operation.runtime_session.scenario_execute(parameters=parameters)',
                ),
            ),
            supports_operation_recovery=True,
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="skeletal_mesh.remove_morph_target",
            binding_hash="sha256:fba89686e51da48cc3a33cda7c43c0036d9b73824c400c63800926ae1f6c261b",
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
                    name="confirm",
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
            command_id="skeletal_mesh.remove_skin_weight_profile",
            binding_hash="sha256:55414aa77e3af3b3ddf8e5a99786a35915edbc8781e51387f772dced32e5e35c",
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
                    name="confirm",
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
            command_id="sound_cue.graph.compile_settle",
            binding_hash="sha256:ef23ceee1b3b1b18a9cc748d0196a203ca5255106d0b764545a11ba7f87383bd",
            namespace="sound_cue",
            method="graph_compile_settle",
            parameters=(
                CommandParameterBinding(
                    name="sync_policy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["sync_and_compile"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="texture_graph.artifact.bake",
            binding_hash="sha256:8ef361aef696df9b5d7a18c7d4de9537b10eec935c44c1c8d24aa1800d00d497",
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
                    name="outputs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="asset_refs",
                    source_path=('asset_refs',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="texture_graph.artifact.capture",
            binding_hash="sha256:f1f0ac66443798ea7d189f3e2aec1805a4bae4cf99a8a10de7dd4c1032d12c12",
            namespace="texture_graph",
            method="artifact_capture",
            parameters=(
                CommandParameterBinding(
                    name="outputs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"element_id":{"minLength":1,"type":"string"},"output_name":{"minLength":1,"type":"string"}},"required":["element_id","output_name"],"type":"object"},"minItems":1,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="texture_graph.graph.link.mutate",
            binding_hash="sha256:8f2411da08ebc779540c76e973127ceb4d253f53606779555422ceec804d91b7",
            namespace="texture_graph",
            method="graph_link_mutate",
            parameters=(
                CommandParameterBinding(
                    name="links",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"from":{"additionalProperties":false,"properties":{"direction":{"enum":["output"],"type":"string"},"element_id":{"minLength":1,"type":"string"},"pin_name":{"minLength":1,"type":"string"}},"required":["direction","element_id","pin_name"],"type":"object"},"intent":{"enum":["create","delete"],"type":"string"},"to":{"additionalProperties":false,"properties":{"direction":{"enum":["input"],"type":"string"},"element_id":{"minLength":1,"type":"string"},"pin_name":{"minLength":1,"type":"string"}},"required":["direction","element_id","pin_name"],"type":"object"}},"required":["from","intent","to"],"type":"object"},"minItems":1,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="texture_graph.graph.node.mutate",
            binding_hash="sha256:cecbd93558b5ba2e3f87df4ed1e06b122742666e2c261bb5e99ad005382a49df",
            namespace="texture_graph",
            method="graph_node_mutate",
            parameters=(
                CommandParameterBinding(
                    name="nodes",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"element_id":{"minLength":1,"type":"string"},"expression_class_ref":{"minLength":1,"type":"string"},"intent":{"enum":["create","update","replace","delete"],"type":"string"}},"required":["element_id","expression_class_ref","intent"],"type":"object"},"minItems":1,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="texture_graph.graph.parameter.mutate",
            binding_hash="sha256:a58edb4607fb8d6aa89276a8d8497d9c2f3a303d6d34fc4e17cce8ceb16f4285",
            namespace="texture_graph",
            method="graph_parameter_mutate",
            parameters=(
                CommandParameterBinding(
                    name="parameters",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"additionalProperties":false,"properties":{"alias":{"minLength":1,"type":"string"},"element_id":{"minLength":1,"type":"string"},"intent":{"enum":["update","replace"],"type":"string"},"pin_name":{"minLength":1,"type":"string"},"value":{}},"required":["alias","element_id","intent","pin_name","value"],"type":"object"},"minItems":1,"type":"array"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="texture_graph.graph.validate_evaluate_settle",
            binding_hash="sha256:a2d183d7a6be2be41b0a8d3141c7182bcf772197fba1ef9198fbc08b66835809",
            namespace="texture_graph",
            method="graph_validate_evaluate_settle",
            parameters=(
                CommandParameterBinding(
                    name="evaluation_policy",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"enum":["validate_and_evaluate"],"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
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
            binding_hash="sha256:b83ea34c36c7dfe8a7e0bd98789a4ca7968e80b8b245169f1b721677960b183d",
            namespace="timeline",
            method="sequence_create",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"destination_ref":{"minLength":1,"type":"string"},"display_rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"initial_structure":{"additionalProperties":false,"properties":{"bindings":{"items":{"additionalProperties":false,"properties":{"binding_kind":{"enum":["possessable","spawnable","widget","slot"],"type":"string"},"binding_ref":{"minLength":1,"type":"string"},"object_ref":{"minLength":1,"type":"string"},"tags":{"items":{"minLength":1,"type":"string"},"type":"array"},"tracks":{"items":{"additionalProperties":false,"properties":{"property_path":{"type":"string"},"sections":{"items":{"additionalProperties":false,"properties":{"keys":{"items":{"additionalProperties":false,"properties":{"key_ref":{"minLength":1,"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},"value_lexeme":{"type":"string"},"value_type":{"enum":["boolean","integer","decimal","transform","asset_ref","string"],"type":"string"}},"required":["key_ref","time","value_type"],"type":"object"},"type":"array"},"range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"section_kind":{"minLength":1,"type":"string"},"section_ref":{"minLength":1,"type":"string"},"source_ref":{"minLength":1,"type":"string"}},"required":["section_ref","section_kind","range","keys"],"type":"object"},"type":"array"},"track_kind":{"minLength":1,"type":"string"},"track_ref":{"minLength":1,"type":"string"}},"required":["track_ref","track_kind","sections"],"type":"object"},"type":"array"}},"required":["binding_ref","binding_kind","tracks"],"type":"object"},"type":"array"},"display_rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"folders":{"items":{"additionalProperties":false,"properties":{"bindings":{"items":{"type":"string"},"type":"array"},"folder_ref":{"type":"string"},"name":{"minLength":1,"type":"string"},"parent":{"type":"string"},"root_tracks":{"items":{"type":"string"},"type":"array"}},"required":["folder_ref","name"],"type":"object"},"type":"array"},"playback_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"root_tracks":{"items":{"additionalProperties":false,"properties":{"property_path":{"type":"string"},"sections":{"items":{"additionalProperties":false,"properties":{"keys":{"items":{"additionalProperties":false,"properties":{"key_ref":{"minLength":1,"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},"value_lexeme":{"type":"string"},"value_type":{"enum":["boolean","integer","decimal","transform","asset_ref","string"],"type":"string"}},"required":["key_ref","time","value_type"],"type":"object"},"type":"array"},"range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"section_kind":{"minLength":1,"type":"string"},"section_ref":{"minLength":1,"type":"string"},"source_ref":{"minLength":1,"type":"string"}},"required":["section_ref","section_kind","range","keys"],"type":"object"},"type":"array"},"track_kind":{"minLength":1,"type":"string"},"track_ref":{"minLength":1,"type":"string"}},"required":["track_ref","track_kind","sections"],"type":"object"},"type":"array"},"tick_resolution":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"}},"required":["display_rate","tick_resolution","playback_range","bindings","root_tracks"],"type":"object"},"tick_resolution":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"}},"required":["destination_ref","initial_structure"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('projection', 'payload', 'result', 'target_ref'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="timeline.sequence.read",
            binding_hash="sha256:e4003d208ece3c4743edc23e7cb2aa9788ec2ea8c551b545beda560cc4716753",
            namespace="timeline",
            method="sequence_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_bindings":{"type":"boolean"},"include_keys":{"type":"boolean"},"include_tracks":{"type":"boolean"},"temporal_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="timeline.sequence.structure.replace",
            binding_hash="sha256:77bdf330a669485e171f6d07d8220f3e270d5f55252208f890bb987d1144fc33",
            namespace="timeline",
            method="sequence_structure_replace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"expected_revision":{"additionalProperties":false,"properties":{"generation":{"minLength":1,"type":"string"},"sequence":{"minLength":1,"type":"string"},"source_id":{"minLength":1,"type":"string"}},"required":["source_id","generation","sequence"],"type":"object"},"structure":{"additionalProperties":false,"properties":{"bindings":{"items":{"additionalProperties":false,"properties":{"binding_kind":{"enum":["possessable","spawnable","widget","slot"],"type":"string"},"binding_ref":{"minLength":1,"type":"string"},"object_ref":{"minLength":1,"type":"string"},"tags":{"items":{"minLength":1,"type":"string"},"type":"array"},"tracks":{"items":{"additionalProperties":false,"properties":{"property_path":{"type":"string"},"sections":{"items":{"additionalProperties":false,"properties":{"keys":{"items":{"additionalProperties":false,"properties":{"key_ref":{"minLength":1,"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},"value_lexeme":{"type":"string"},"value_type":{"enum":["boolean","integer","decimal","transform","asset_ref","string"],"type":"string"}},"required":["key_ref","time","value_type"],"type":"object"},"type":"array"},"range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"section_kind":{"minLength":1,"type":"string"},"section_ref":{"minLength":1,"type":"string"},"source_ref":{"minLength":1,"type":"string"}},"required":["section_ref","section_kind","range","keys"],"type":"object"},"type":"array"},"track_kind":{"minLength":1,"type":"string"},"track_ref":{"minLength":1,"type":"string"}},"required":["track_ref","track_kind","sections"],"type":"object"},"type":"array"}},"required":["binding_ref","binding_kind","tracks"],"type":"object"},"type":"array"},"display_rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"folders":{"items":{"additionalProperties":false,"properties":{"bindings":{"items":{"type":"string"},"type":"array"},"folder_ref":{"type":"string"},"name":{"minLength":1,"type":"string"},"parent":{"type":"string"},"root_tracks":{"items":{"type":"string"},"type":"array"}},"required":["folder_ref","name"],"type":"object"},"type":"array"},"playback_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"root_tracks":{"items":{"additionalProperties":false,"properties":{"property_path":{"type":"string"},"sections":{"items":{"additionalProperties":false,"properties":{"keys":{"items":{"additionalProperties":false,"properties":{"key_ref":{"minLength":1,"type":"string"},"time":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"},"transform":{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","basis_frame_id","dimension","unit","basis_evidence_id"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},"value_lexeme":{"type":"string"},"value_type":{"enum":["boolean","integer","decimal","transform","asset_ref","string"],"type":"string"}},"required":["key_ref","time","value_type"],"type":"object"},"type":"array"},"range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"},"section_kind":{"minLength":1,"type":"string"},"section_ref":{"minLength":1,"type":"string"},"source_ref":{"minLength":1,"type":"string"}},"required":["section_ref","section_kind","range","keys"],"type":"object"},"type":"array"},"track_kind":{"minLength":1,"type":"string"},"track_ref":{"minLength":1,"type":"string"}},"required":["track_ref","track_kind","sections"],"type":"object"},"type":"array"},"tick_resolution":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"}},"required":["display_rate","tick_resolution","playback_range","bindings","root_tracks"],"type":"object"}},"required":["structure","expected_revision"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory","persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="timeline.track_candidates",
            binding_hash="sha256:ca3c0b23d5c3fc6fdf4c6e8e77f694c0cec64d204ef3d58071f7ce70bd902b3a",
            namespace="timeline",
            method="track_candidates",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="animation_name",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="binding_kind",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="object_ref",
                    wire_type="string",
                    required=False,
                    nullable=False,
                ),
                CommandParameterBinding(
                    name="property_path",
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
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="timeline.widget_animation.read",
            binding_hash="sha256:21f69d2196c2051898746959ab0b335060b13b559e90382f3f95d266390400d0",
            namespace="timeline",
            method="widget_animation_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_bindings":{"type":"boolean"},"include_tracks":{"type":"boolean"},"temporal_range":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"lower":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"},"state":{"const":"authored","type":"string"},"upper":{"additionalProperties":false,"properties":{"kind":{"enum":["open","inclusive","exclusive"],"type":"string"},"point":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate":{"additionalProperties":false,"properties":{"denominator":{"minLength":1,"type":"string"},"numerator":{"minLength":1,"type":"string"}},"required":["numerator","denominator"],"type":"object"},"state":{"const":"authored","type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate","state"],"type":"object"}},"required":["kind"],"type":"object"}},"required":["clock_id","state","lower","upper"],"type":"object"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["persisted"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="umg.asset.create",
            binding_hash="sha256:ff82dee226f2d6c516d7e7ee566ac4395c94d72a50bbebc9cc5ccafe1b40bf7a",
            namespace="umg",
            method="asset_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_name",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="package_path",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="target_ref",
                    source_path=('target_ref',),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="umg.widget.candidates",
            binding_hash="sha256:c93f94b6e50f97bb1d2fa88c3797e79dbd832df962aa01f22b8437441421dfb4",
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
                    name="describe",
                    wire_type="object",
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
            binding_hash="sha256:2cb5c9c41d79b93c1dc9cb679d641afdfa79c74a22bb17c91871fa546facf8f3",
            namespace="umg",
            method="widget_events_discover",
            parameters=(
                CommandParameterBinding(
                    name="owner_item_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.actor.pick",
            binding_hash="sha256:e2776d0285b07168872d73d4b89d6f8ef91be266e43df9256d2458e2d86b70ed",
            namespace="viewport",
            method="actor_pick",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"allow_no_hit":{"type":"boolean"},"screen_point":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":2,"minItems":2,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":2,"minItems":2,"type":"array"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"trace_query":{"additionalProperties":false,"properties":{"ignore_target_refs":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"max_distance_cm":{"exclusiveMinimum":0,"type":"number"},"trace_channel":{"minLength":1,"type":"string"},"trace_complex":{"type":"boolean"}},"required":["max_distance_cm","trace_channel","trace_complex","ignore_target_refs"],"type":"object"}},"required":["screen_point","trace_query"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.actor.select",
            binding_hash="sha256:221b2bb2479cc72aaafa4a4e9a537385839478b800a49e60a0e085dcf7c4ef8a",
            namespace="viewport",
            method="actor_select",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"actor_refs":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"screen_point":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":2,"minItems":2,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":2,"minItems":2,"type":"array"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"selection_mode":{"enum":["replace","add","remove","toggle"],"type":"string"},"trace_query":{"additionalProperties":false,"properties":{"ignore_target_refs":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"max_distance_cm":{"exclusiveMinimum":0,"type":"number"},"trace_channel":{"minLength":1,"type":"string"},"trace_complex":{"type":"boolean"}},"required":["max_distance_cm","trace_channel","trace_complex","ignore_target_refs"],"type":"object"}},"required":["selection_mode"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.camera.frame",
            binding_hash="sha256:ccffaf43b999c8ec7c8921b8b572210de3600c747c1249a6a8295868c40e86ef",
            namespace="viewport",
            method="camera_frame",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"folder_path":{"minLength":1,"type":"string"},"frame_policy":{"additionalProperties":false,"properties":{"auto_fallback":{"type":"boolean"},"collision_aware":{"type":"boolean"},"look_at":{"type":"boolean"},"maximum_distance_cm":{"exclusiveMinimum":0,"type":"number"},"minimum_distance_cm":{"minimum":0,"type":"number"},"padding_ratio":{"minimum":0,"type":"number"},"preserve_rotation":{"type":"boolean"}},"required":["padding_ratio","minimum_distance_cm","maximum_distance_cm","preserve_rotation"],"type":"object"},"include_child_folders":{"type":"boolean"},"subject_refs":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"use_current_selection":{"type":"boolean"},"world_bounds":{"additionalProperties":false,"properties":{"max":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"min":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]}},"required":["min","max"],"type":"object"},"world_point":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]}},"required":["frame_policy"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.instance.list",
            binding_hash="sha256:f4ab2473dff5bfe968b7a0d38472f08c5ebd36499e8daaf62a7d833c238a3b35",
            namespace="viewport",
            method="instance_list",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.pixel_scale.read",
            binding_hash="sha256:12fb0af820b6abb490c0ad982d133b114ecad1e664cfd6c56e294d3a80988e8b",
            namespace="viewport",
            method="pixel_scale_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"sample_point":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]}},"required":["sample_point"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.ray.deproject",
            binding_hash="sha256:9f86c01b6ca619e57a39d075da676b2315e5681ebe928c6340b81a8822ffa681",
            namespace="viewport",
            method="ray_deproject",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"screen_point":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":2,"minItems":2,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":2,"minItems":2,"type":"array"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]}},"required":["screen_point"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.ray.trace",
            binding_hash="sha256:767574a89f752112d2f610fdcaeb8645daf88d20608ff24c48fc1628daaf1f75",
            namespace="viewport",
            method="ray_trace",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"screen_point":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":2,"minItems":2,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":2,"minItems":2,"type":"array"},"dimension":{"const":2,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"trace_query":{"additionalProperties":false,"properties":{"ignore_target_refs":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"max_distance_cm":{"exclusiveMinimum":0,"type":"number"},"trace_channel":{"minLength":1,"type":"string"},"trace_complex":{"type":"boolean"}},"required":["max_distance_cm","trace_channel","trace_complex","ignore_target_refs"],"type":"object"}},"required":["screen_point","trace_query"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.state.read",
            binding_hash="sha256:e50a1524c71eea910250d112759c66d48461acf99b87af1d8c4fb3eaa71ad690",
            namespace="viewport",
            method="state_read",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.state.restore",
            binding_hash="sha256:0d5ef9fd27b370c338875ab8471ff26fdb0806491c816456b44f2a5832249d31",
            namespace="viewport",
            method="state_restore",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"snapshot":{"additionalProperties":false,"properties":{"camera":{"additionalProperties":false,"properties":{"camera_transform":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":10,"minItems":10,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"transform","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"fov_degrees":{"exclusiveMinimum":0,"maximum":179,"type":"number"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"view_mode":{"minLength":1,"type":"string"}},"required":["camera_transform","fov_degrees","view_mode"],"type":"object"},"game_view":{"type":"boolean"},"interaction":{"additionalProperties":false,"properties":{"editor_primitives":{"type":"boolean"},"game_primitives":{"type":"boolean"},"mode_widgets":{"type":"boolean"},"pivot":{"type":"boolean"},"selection":{"type":"boolean"},"widget_mode":{"minLength":1,"type":"string"}},"required":["mode_widgets","selection","pivot","editor_primitives","game_primitives","widget_mode"],"type":"object"},"realtime":{"type":"boolean"},"realtime_configured":{"type":"boolean"},"realtime_override_reason":{"type":"string"},"show_flags":{"items":{"enum":["Lighting","StaticMeshes"],"type":"string"},"type":"array","uniqueItems":true},"viewport_ref":{"minLength":1,"type":"string"}},"required":["viewport_ref","camera","realtime","game_view","show_flags","interaction"],"type":"object"}},"required":["snapshot"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.state.update",
            binding_hash="sha256:61d9c90bb5a839e9b295204b2d8c878e117d0ef6e6546fae328a3d850436a226",
            namespace="viewport",
            method="state_update",
            parameters=(
                CommandParameterBinding(
                    name="target",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"description":"Exact readable viewport_ref/target or graph_ref. Viewport targets must equal the viewport_ref returned by viewport.instance.list.","minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"state_patch":{"additionalProperties":false,"properties":{"camera_transform":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":10,"minItems":10,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"transform","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"camera_transform_mode":{"enum":["absolute","delta"],"type":"string"},"fov_degrees":{"exclusiveMinimum":0,"maximum":179,"type":"number"},"game_view":{"type":"boolean"},"interaction":{"additionalProperties":false,"properties":{"editor_primitives":{"type":"boolean"},"game_primitives":{"type":"boolean"},"mode_widgets":{"type":"boolean"},"pivot":{"type":"boolean"},"selection":{"type":"boolean"},"widget_mode":{"minLength":1,"type":"string"}},"required":["mode_widgets","selection","pivot","editor_primitives","game_primitives","widget_mode"],"type":"object"},"realtime":{"type":"boolean"},"show_flags":{"items":{"enum":["Lighting","StaticMeshes"],"type":"string"},"type":"array","uniqueItems":true},"view_mode":{"minLength":1,"type":"string"}},"type":"object"}},"required":["state_patch"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.view_mode.list",
            binding_hash="sha256:b0d37292a753a35cb59b4854ad9641005b03801798800118c0aaf9c891e5c0c7",
            namespace="viewport",
            method="view_mode_list",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"query":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["registry_index"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="viewport.warning.list",
            binding_hash="sha256:72fb581ea72f799299b40735cc40d19cbcf98bdb876cc792cbb562350b5bf9b1",
            namespace="viewport",
            method="warning_list",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_suppressed":{"type":"boolean"},"viewport_ref":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="context",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"description":"Model-writable execution context. project_instance_id, editor_instance_id, context_revision, and resolved_from_current are server-owned and excluded.","properties":{"asset_editor":{"minLength":1,"type":"string"},"data_layers":{"items":{"minLength":1,"type":"string"},"type":"array"},"level":{"type":"string"},"net_mode":{"type":"string"},"net_role":{"type":"string"},"pie_instance":{"type":"integer"},"selection":{"items":{"minLength":1,"type":"string"},"type":"array"},"state_plane":{"enum":["authoring_memory"],"type":"string"},"viewport":{"description":"Readable viewport_ref returned by viewport.instance.list; for viewport commands it must equal target.","minLength":1,"type":"string"},"viewport_role":{"type":"string"},"viewport_scope":{"type":"string"},"world":{"type":"string"},"world_partition":{"type":"string"},"world_type":{"enum":["editor","pie","simulate_in_editor","game","preview"],"type":"string"}},"required":["viewport"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="projection",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_defaults":{"type":"boolean"},"include_details":{"type":"boolean"},"include_provenance":{"type":"boolean"},"profile_id":{"minLength":1,"type":"string"}},"type":"object"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.actor.candidates",
            binding_hash="sha256:eb3c5db010ace1dbb8f2de130d6c392849677dc21481c048976e268c76a18338",
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
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.actor.create",
            binding_hash="sha256:eb4234c82d2b28c6dcef6d627dfab1c771c7b74e6055019bb6f18fcb322b1911",
            namespace="world",
            method="actor_create",
            parameters=(
                CommandParameterBinding(
                    name="actor_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="folder_path",
                    wire_type="string",
                    required=False,
                    nullable=False,
                    schema_json='{"type":"string"}',
                ),
                CommandParameterBinding(
                    name="label",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"minLength":1,"type":"string"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="tags",
                    wire_type="array",
                    required=False,
                    nullable=False,
                    schema_json='{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.actor_components",
            binding_hash="sha256:539674c106e8f31f5d7384f7a421853e0357cd675a2f108b7cd6b0d45e97e01a",
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
                    schema_json='{"additionalProperties":false,"properties":{},"type":"object"}',
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
            status="dormant",
        ),
        CommandBinding(
            command_id="world.actor_hlod_layer.update",
            binding_hash="sha256:0948b47405d6acc4ba9e987e62b56bd1867ed924e4ec5919d86194c21b83b9c4",
            namespace="world",
            method="actor_hlod_layer_update",
            parameters=(
                CommandParameterBinding(
                    name="collection_ref",
                    wire_type="string",
                    required=False,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"anyOf":[{"const":"replace"},{"const":"clear"}]}',
                ),
                CommandParameterBinding(
                    name="subject_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.actor_streaming_policy.update",
            binding_hash="sha256:9d04ff9a1872676636e5f945f70372c73068ce8ce88efed712c53b41a3904266",
            namespace="world",
            method="actor_streaming_policy_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"minProperties":1,"properties":{"is_spatially_loaded":{"type":"boolean"},"runtime_grid":{"oneOf":[{"additionalProperties":false,"properties":{"intent":{"const":"set"},"value":{"minLength":1,"type":"string"}},"required":["intent","value"],"type":"object"},{"additionalProperties":false,"properties":{"intent":{"const":"clear"}},"required":["intent"],"type":"object"}]}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.actors",
            binding_hash="sha256:af8aa52fe46d337c26f6072bc744f08b85ca20dc6a67327f98504d88c73f96b0",
            namespace="world",
            method="actors",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"class_paths":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"folder_path_prefix":{"type":"string"},"tags":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true}},"type":"object"}',
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
            status="dormant",
        ),
        CommandBinding(
            command_id="world.capsule_path",
            binding_hash="sha256:dc0117b6c8a461edbfbc552fe24f14bb85e27c73254f1806b115c430e78ad0c5",
            namespace="world",
            method="capsule_path",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"half_height_cm":{"exclusiveMinimum":0,"type":"number"},"points":{"items":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"},"minItems":2,"type":"array"},"radius_cm":{"exclusiveMinimum":0,"type":"number"},"step_cm":{"exclusiveMinimum":0,"type":"number"},"trace_channel":{"minLength":1,"type":"string"}},"required":["points","radius_cm","half_height_cm","step_cm"],"type":"object"}',
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
            binding_hash="sha256:53eb2c3517dd07f86613435fff7371ec9d0fb69b5f6c4d3babc2b202ecf04ded",
            namespace="world",
            method="capsule_sweep",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"end":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"},"find_initial_overlaps":{"type":"boolean"},"half_height_cm":{"exclusiveMinimum":0,"type":"number"},"include_hits":{"type":"boolean"},"radius_cm":{"exclusiveMinimum":0,"type":"number"},"start":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"},"trace_channel":{"minLength":1,"type":"string"},"trace_complex":{"type":"boolean"}},"required":["start","end","radius_cm","half_height_cm"],"type":"object"}',
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
            binding_hash="sha256:94b6b528141971823985c7dfc22378517830c28316bf27a5241a6e5f2e2dc9a3",
            namespace="world",
            method="content",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_bounds":{"type":"boolean"},"include_components":{"type":"boolean"},"scope":{"enum":["world","selection","target"],"type":"string"},"sections":{"items":{"enum":["actors","attachments","components","folders","world_settings"],"type":"string"},"type":"array","uniqueItems":true}},"type":"object"}',
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
            status="dormant",
        ),
        CommandBinding(
            command_id="world.data_layer.delete",
            binding_hash="sha256:d9a5d50005a000f671dcb8d49f44c7cc85eb11bb56590b0460d82fe8434629b3",
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
                    name="confirm",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.data_layer_instance.create",
            binding_hash="sha256:89e9b8a5c03d84f1dcda0c7af25ccc83c0f3aaf52bf8db5662dd267cbfa6d56e",
            namespace="world",
            method="data_layer_instance_create",
            parameters=(
                CommandParameterBinding(
                    name="asset_ref",
                    wire_type="string",
                    required=False,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="initial_state",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"minProperties":1,"properties":{"initial_runtime_state":{"enum":["unloaded","loaded","activated"],"type":"string"},"initially_visible":{"type":"boolean"},"loaded_in_editor":{"type":"boolean"},"visible":{"type":"boolean"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="parent_ref",
                    wire_type="string",
                    required=False,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="private",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                    schema_json='{"anyOf":[{"const":false},{"const":true}]}',
                ),
                CommandParameterBinding(
                    name="short_name",
                    wire_type="string",
                    required=False,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.data_layer_relation.update",
            binding_hash="sha256:3a9951449af05fb62c314468fa2a3abc331cef07a27fca75c7606ab8e099f501",
            namespace="world",
            method="data_layer_relation_update",
            parameters=(
                CommandParameterBinding(
                    name="collection_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"anyOf":[{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},{"items":{"minLength":1,"type":"string"},"maxItems":1,"type":"array","uniqueItems":true}]}',
                ),
                CommandParameterBinding(
                    name="mode",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"anyOf":[{"enum":["add","remove","replace","clear"],"type":"string"},{"enum":["replace","clear"],"type":"string"}]}',
                ),
                CommandParameterBinding(
                    name="relation_kind",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"anyOf":[{"const":"actor_membership"},{"const":"parent"}]}',
                ),
                CommandParameterBinding(
                    name="subject_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.data_layer_state.update",
            binding_hash="sha256:419eed6b91f6e1b6c4b692f42558a79087511969b3ee1796f6f80fd39edc08d1",
            namespace="world",
            method="data_layer_state_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"minProperties":1,"properties":{"initial_runtime_state":{"enum":["unloaded","loaded","activated"],"type":"string"},"initially_visible":{"type":"boolean"},"loaded_in_editor":{"type":"boolean"},"short_name":{"minLength":1,"type":"string"},"visible":{"type":"boolean"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_refs",
                    wire_type="array",
                    required=True,
                    nullable=False,
                    schema_json='{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.data_layers",
            binding_hash="sha256:0161f1d45e428c0d129446274bef1aa8b480bf2fa8c2941d63072299ebff234e",
            namespace="world",
            method="data_layers",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_actor_membership":{"type":"boolean"},"scope":{"enum":["world","selection"],"type":"string"}},"type":"object"}',
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
            binding_hash="sha256:5d0ab07b2db5ac0b9f9357e9eb93fbb7438e7ddaa2d6b79115f77b010d1159a0",
            namespace="world",
            method="hlod_assignments",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"folder_path_prefix":{"type":"string"},"managed_tag":{"type":"string"}},"type":"object"}',
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
            binding_hash="sha256:7c43e5bcdd35d2ee2e5e3c2f8880711ab1d3f0b353fdedb6927469c0c7fed7be",
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
                    name="confirm",
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
            command_id="world.level_game_mode.update",
            binding_hash="sha256:17c10c0d8f3c85c538ad22338fe4364749a50c26aaa35a45bf4698bde8952551",
            namespace="world",
            method="level_game_mode_update",
            parameters=(
                CommandParameterBinding(
                    name="game_mode_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.level_streaming.move_actors",
            binding_hash="sha256:e81d6df94723bf393df73b0a0dd135d265e37bb7e1860e5b21451ed316c7f37c",
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
                    name="confirm",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.level_streaming.remove",
            binding_hash="sha256:acca7702c8543d3c448c998b2f4bbd97fea849adccf9d8986a323f094728ce5c",
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
                    name="confirm",
                    wire_type="boolean",
                    required=False,
                    nullable=False,
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.mesh_closest_vertex",
            binding_hash="sha256:0521c43c2c4ecf0f0935e4626b2f87f16bafcf5c4f46f005543471ca7560d707",
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
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"world_point":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"}},"required":["world_point"],"type":"object"}',
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
            binding_hash="sha256:de98a4ca4308efff4d5f89d12dafff5bc176745dece4d7c392720bde04dc9df4",
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
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"vertex_index":{"minimum":0,"type":"integer"}},"required":["vertex_index"],"type":"object"}',
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
            binding_hash="sha256:fa5673b8f032576e9eadc3b305886cee1e66fa02a02e4ea51664d32453a0e8ad",
            namespace="world",
            method="nav_connectivity",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"allow_partial":{"type":"boolean"},"allow_projection_failure":{"type":"boolean"},"include_path_points":{"type":"boolean"},"pairs":{"items":{"items":{"minimum":0,"type":"integer"},"maxItems":2,"minItems":2,"type":"array"},"type":"array"},"points":{"items":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"},"minItems":2,"type":"array"},"project_to_nav":{"type":"boolean"},"query_extent_cm":{"items":{"minimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"}},"required":["points"],"type":"object"}',
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
            binding_hash="sha256:e138b8e5615ce32c25902b23b3316e5d691b6bfb1f373ccd48b2b31bb390617d",
            namespace="world",
            method="nav_find_path",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"allow_partial":{"type":"boolean"},"allow_projection_failure":{"type":"boolean"},"end":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"},"include_path_points":{"type":"boolean"},"project_to_nav":{"type":"boolean"},"query_extent_cm":{"items":{"minimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"start":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"}},"required":["start","end"],"type":"object"}',
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
            binding_hash="sha256:33bb4f7147533a0c10eaf473cef367406200880b548dfe5426c2b35989852e19",
            namespace="world",
            method="nav_project_point",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"point":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"},"query_extent_cm":{"items":{"minimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"}},"required":["point"],"type":"object"}',
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
            binding_hash="sha256:dfadd3d3e8770c002d0ea75f8c6c51eb2944ba888a475f35fc25661acc224ce6",
            namespace="world",
            method="nearby_shapes",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"center":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"},"folder_path_prefix":{"type":"string"},"half_extents_cm":{"items":{"minimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"ignore_folder_path_prefix":{"type":"string"},"include_shapes":{"type":"boolean"},"radius_cm":{"minimum":0,"type":"number"}},"required":["center"],"type":"object"}',
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
            binding_hash="sha256:6c15412948a28eaf7531d2943d0621a35175eb126ca397b1245a310114027ae6",
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
                    schema_json='{"additionalProperties":false,"properties":{"alignment":{"additionalProperties":false,"properties":{"axis":{"enum":["x","y","z"],"type":"string"},"kind":{"enum":["anchors","bounds","face","vertex"],"type":"string"},"offset_cm":{"type":"number"},"reference_anchor":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"reference_normal":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"normal","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"normal","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"rotation_policy":{"enum":["preserve","align_normals","align_frames"],"type":"string"},"source_anchor":{"enum":["min","center","max"],"type":"string"},"source_face":{"minLength":1,"type":"string"},"source_vertex_index":{"minimum":0,"type":"integer"},"subject_anchor":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"subject_normal":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"normal","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"normal","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"target_anchor":{"enum":["min","center","max"],"type":"string"},"target_face":{"minLength":1,"type":"string"},"target_vertex_index":{"minimum":0,"type":"integer"},"verify_frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"}},"required":["kind","verify_frame"],"type":"object"},"anchor_ref":{"minLength":1,"type":"string"},"subject_refs":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true}},"required":["subject_refs","alignment"],"type":"object"}',
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
            binding_hash="sha256:cd9971fc012638f1b73c8ededc83127ba9b82a2f4192d3e87f4df1c50dc7d2cb",
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
                    schema_json='{"additionalProperties":false,"properties":{"placement_policy":{"additionalProperties":false,"properties":{"align_to_surface_normal":{"type":"boolean"},"clearance_cm":{"minimum":0,"type":"number"},"preserve_yaw":{"type":"boolean"}},"required":["clearance_cm","align_to_surface_normal","preserve_yaw"],"type":"object"},"subject_refs":{"items":{"minLength":1,"type":"string"},"minItems":1,"type":"array","uniqueItems":true},"surface_query":{"additionalProperties":false,"properties":{"direction":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"direction","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"direction","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"ignore_target_refs":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"max_distance_cm":{"exclusiveMinimum":0,"type":"number"},"origin":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":3,"minItems":3,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"point","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":3,"minItems":3,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"point","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]},"trace_channel":{"enum":["visibility","camera"],"type":"string"},"trace_complex":{"type":"boolean"}},"required":["origin","direction","max_distance_cm","trace_channel","trace_complex","ignore_target_refs"],"type":"object"}},"required":["subject_refs","surface_query","placement_policy"],"type":"object"}',
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
            binding_hash="sha256:86c29957a36664e9174d7b12906373bca37ee3672861c8f18222b7b836e0bf64",
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
                    schema_json='{"additionalProperties":false,"properties":{"verify_frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"}},"required":["verify_frame"],"type":"object"}',
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
            status="dormant",
        ),
        CommandBinding(
            command_id="world.object_transform.update",
            binding_hash="sha256:2ea317496e0bfa0b814fecfda42f788d144ccf4532d94c634dfe0d9a0830c062",
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
                    schema_json='{"additionalProperties":false,"properties":{"transform":{"anyOf":[{"additionalProperties":false,"properties":{"components":{"items":{"minLength":1,"type":"string"},"maxItems":10,"minItems":10,"type":"array"},"conversion_evidence_ids":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true},"frame":{"additionalProperties":false,"properties":{"basis_evidence_id":{"minLength":1,"type":"string"},"basis_frame_id":{"minLength":1,"type":"string"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"observed_at":{"additionalProperties":false,"properties":{"clock_id":{"minLength":1,"type":"string"},"rate_denominator":{"minLength":1,"type":"string"},"rate_numerator":{"minLength":1,"type":"string"},"state":{"enum":["captured","frozen"],"type":"string"},"tick":{"minLength":1,"type":"string"}},"required":["clock_id","tick","rate_numerator","rate_denominator","state"],"type":"object"},"unit":{"minLength":1,"type":"string"}},"required":["frame_id","dimension","unit"],"type":"object"},"quantity":{"const":"transform","type":"string"},"subject":{"minLength":1,"type":"string"}},"required":["subject","quantity","frame","components","conversion_evidence_ids"],"type":"object"},{"additionalProperties":false,"properties":{"components":{"items":{"anyOf":[{"type":"number"},{"minLength":1,"type":"string"}]},"maxItems":10,"minItems":10,"type":"array"},"dimension":{"const":3,"type":"integer"},"frame_id":{"minLength":1,"type":"string"},"quantity":{"const":"transform","type":"string"},"unit":{"minLength":1,"type":"string"}},"required":["quantity","frame_id","dimension","unit","components"],"type":"object"}]}},"required":["transform"],"type":"object"}',
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
            status="dormant",
        ),
        CommandBinding(
            command_id="world.overlap",
            binding_hash="sha256:6aa319b2de6c63b001374c5b4aa5701b2a920ca5561ef41af129cea90941c37a",
            namespace="world",
            method="overlap",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"center":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"},"half_extents_cm":{"items":{"minimum":0,"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"half_height_cm":{"minimum":0,"type":"number"},"include_targets":{"type":"boolean"},"radius_cm":{"minimum":0,"type":"number"},"shape":{"enum":["box","sphere","capsule"],"type":"string"},"trace_channel":{"minLength":1,"type":"string"}},"required":["shape","center"],"type":"object"}',
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
            binding_hash="sha256:b033714526221704f202c5b192bd0fdd39208f52a9bad527fe2a376dabae2d5b",
            namespace="world",
            method="partition",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"include_loaded_regions":{"type":"boolean"}},"type":"object"}',
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
            binding_hash="sha256:bd53602bdb21ed918eb59bc146df663626e149b33712374fd6fd5ee9b95c20ac",
            namespace="world",
            method="partition_health",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"enable_streaming":{"type":"boolean"}},"type":"object"}',
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
            binding_hash="sha256:4e5cd7b70f77fc3aa7d91fe2b806dbfe7c84c5124a963dac38ff2656e6576f22",
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
                    name="confirm",
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
            command_id="world.physics_component",
            binding_hash="sha256:865f27c68d147115926c5720df13cc9a0532f3539bab4b14f43b477d4c6b4673",
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
                    schema_json='{"additionalProperties":false,"properties":{"include_collision_responses":{"type":"boolean"},"include_material":{"type":"boolean"},"include_runtime_state":{"type":"boolean"}},"type":"object"}',
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
            binding_hash="sha256:9503a06f26256a17a9747ab4184f99da8f097cc9213cfa33811498dd5e836655",
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
                    schema_json='{"additionalProperties":false,"properties":{"include_endpoints":{"type":"boolean"},"include_limits":{"type":"boolean"},"include_runtime_state":{"type":"boolean"}},"type":"object"}',
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
            binding_hash="sha256:b4f56cb960775efe3f3d3994ed43d7d03a626eca7218b7f5747f3911d2bc0506",
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
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"property_path":{"minLength":1,"type":"string"}},"required":["property_path"],"type":"object"}',
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
            status="dormant",
        ),
        CommandBinding(
            command_id="world.ray_trace",
            binding_hash="sha256:857b86fa00ae744b800d354657853d66e57d858863e14446af53d5cf9088ea1a",
            namespace="world",
            method="ray_trace",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"direction":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"}},"required":["frame_id","components"],"type":"object"},"distance_cm":{"exclusiveMinimum":0,"type":"number"},"start":{"additionalProperties":false,"properties":{"components":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"const":"ue.world","type":"string"},"unit":{"const":"centimeter","type":"string"}},"required":["frame_id","unit","components"],"type":"object"},"trace_channel":{"minLength":1,"type":"string"},"trace_complex":{"type":"boolean"}},"required":["start","direction","distance_cm"],"type":"object"}',
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
            binding_hash="sha256:59f7be38b3ca5ecf45a4c0c52d9a4a902f3005f2fd0dc42b27c90b8545824e34",
            namespace="world",
            method="selection",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{},"type":"object"}',
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
            binding_hash="sha256:94b0f98c6795629c8271ccdc8bd399cd596e8446d116cd0bd05b24f82eac77f3",
            namespace="world",
            method="streaming_levels",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"level_packages":{"items":{"minLength":1,"type":"string"},"type":"array","uniqueItems":true}},"type":"object"}',
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
            binding_hash="sha256:47ef71158d01dbb123c51320f10bf025b71555d698ab37c4a3d40ce8ad1b03eb",
            namespace="world",
            method="streaming_relation_create",
            parameters=(
                CommandParameterBinding(
                    name="level_asset_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
                CommandParameterBinding(
                    name="placement",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"minLength":1,"type":"string"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="streaming_class_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.streaming_relation.state.update",
            binding_hash="sha256:fc6ad56e974a638b37ebada6d856f3819721290f1ca21989bbc856381c31b662",
            namespace="world",
            method="streaming_relation_state_update",
            parameters=(
                CommandParameterBinding(
                    name="changes",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"minProperties":1,"properties":{"loaded":{"type":"boolean"},"placement":{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"frame_id":{"minLength":1,"type":"string"},"rotation_quaternion_xyzw":{"items":{"type":"number"},"maxItems":4,"minItems":4,"type":"array"},"scale":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"translation":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"}},"required":["frame_id","unit","translation","rotation_quaternion_xyzw","scale","basis_evidence"],"type":"object"},"visible":{"type":"boolean"}},"type":"object"}',
                ),
                CommandParameterBinding(
                    name="target_ref",
                    wire_type="string",
                    required=True,
                    nullable=False,
                    schema_json='{"minLength":1,"type":"string"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
        CommandBinding(
            command_id="world.summary",
            binding_hash="sha256:59cc0fcb7a9f2fc4a82aa78911b945ef8e24239607889bf55873ee972bffbb72",
            namespace="world",
            method="summary",
            parameters=(
                CommandParameterBinding(
                    name="input",
                    wire_type="object",
                    required=False,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{},"type":"object"}',
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
            binding_hash="sha256:f84f6d868ac4e6d2de3476151e3cab40fcef606f6c95c429a0ba0b052a843c52",
            namespace="world",
            method="wall_create_with_opening",
            parameters=(
                CommandParameterBinding(
                    name="opening",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"center":{"items":{"type":"number"},"maxItems":2,"minItems":2,"type":"array"},"minimum_segment_size":{"minimum":0,"type":"number"},"out_of_bounds":{"enum":["reject","clamp"],"type":"string"},"padding":{"minimum":0,"type":"number"},"size":{"items":{"exclusiveMinimum":0,"type":"number"},"maxItems":2,"minItems":2,"type":"array"}},"required":["center","size"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="plane",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"basis_evidence":{"minLength":1,"type":"string"},"center":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"frame_id":{"minLength":1,"type":"string"},"normal":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"},"unit":{"enum":["centimeter","meter"],"type":"string"},"up":{"items":{"type":"number"},"maxItems":3,"minItems":3,"type":"array"}},"required":["frame_id","unit","center","normal","up","basis_evidence"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="segment_template",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"actor_class_ref":{"minLength":1,"type":"string"},"folder_path":{"type":"string"},"label_prefix":{"minLength":1,"type":"string"},"mesh_ref":{"minLength":1,"type":"string"}},"required":["actor_class_ref","mesh_ref"],"type":"object"}',
                ),
                CommandParameterBinding(
                    name="wall",
                    wire_type="object",
                    required=True,
                    nullable=False,
                    schema_json='{"additionalProperties":false,"properties":{"height":{"exclusiveMinimum":0,"type":"number"},"thickness":{"exclusiveMinimum":0,"type":"number"},"width":{"exclusiveMinimum":0,"type":"number"}},"required":["thickness","width","height"],"type":"object"}',
                ),
            ),
            model_result_fields=(
                ModelResultFieldBinding(
                    name="status",
                    source_path=('projection', 'payload', 'status'),
                ),
                ModelResultFieldBinding(
                    name="effect_outcome",
                    source_path=('projection', 'payload', 'effect_outcome'),
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="active",
        ),
        CommandBinding(
            command_id="world.world_partition_streaming.update",
            binding_hash="sha256:07fb86047bbba545997cfc9faefbc46278859a9afb7458d2f1b9907654156bf0",
            namespace="world",
            method="world_partition_streaming_update",
            parameters=(
                CommandParameterBinding(
                    name="enabled",
                    wire_type="boolean",
                    required=True,
                    nullable=False,
                    schema_json='{"type":"boolean"}',
                ),
            ),
            min_wire_version=1,
            max_wire_version=1,
            status="dormant",
        ),
    )
)

class GeneratedCommandNamespaces:
    __slots__ = ("ai", "animation", "animation_rig_graph", "asset", "audio", "audio_media", "blueprint", "capture", "config", "content_graph", "deformer", "editor", "editor_project", "external", "graph", "job", "landscape", "material", "material_instance", "mesh", "metasound", "modeling", "niagara", "operation", "pcg", "physics", "project", "query", "reference", "rig", "skeletal_mesh", "sound_cue", "texture_graph", "timeline", "umg", "viewport", "world")

    def __init__(
        self,
        client: CommandExecutor,
    ) -> None:
        self.ai = AiCommands(client)
        self.animation = AnimationCommands(client)
        self.animation_rig_graph = AnimationRigGraphCommands(client)
        self.asset = AssetCommands(client)
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
