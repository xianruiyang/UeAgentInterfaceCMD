# Animation rig commands through the default SDK

Discover current contracts through client.command_search(...) and
client.command_detail(...), then use:

```python
client.animation.control_rig_asset_create(...)
client.animation.control_rig_hierarchy_graph_apply(...)
client.animation.control_rig_shape_library_apply(...)
client.animation.control_rig_shape_library_asset_create(...)
client.animation.ik_retargeter_asset_create(...)
client.animation.ik_retargeter_definition_apply(...)
client.animation.ik_retargeter_settings_apply(...)
client.animation.ik_rig_asset_create(...)
client.animation.ik_rig_definition_apply(...)
client.animation.ik_rig_definition_auto_generate(...)
client.animation.skeleton_compatibility_apply(...)
client.animation.skeleton_definition_apply(...)
client.animation.skeleton_slots_read(...)
client.animation.skeleton_virtual_bone_apply(...)
```

The exact CLI uses uai-cli with the current command ID, hash, and one JSON
parameter object. No task-specific generated projection remains active.

Creation and definition/graph/settings mutations use the common durable
operation lifecycle; skeleton slot read remains a query. Skeleton, bone,
hierarchy/control, shape, chain, retargeter/IK Rig identity, expected revision,
and auto-generation policy come only from command_detail. All transforms and
axis/chain data explicitly carry semantic_frame_id, write/read/verify frame,
unit, basis_evidence, and conversion_chain. The SDK does not infer rig or
spatial business.

Write success requires native compile/settle where declared, terminal
projection, and independent persisted readback after reload. Invalid skeleton,
bone, hierarchy, graph, shape, chain, axis/frame, compatibility, or stale
revision fails before mutation. Unknown state requires reconciliation. Cleanup
removes only owned rig/retarget/skeleton fixtures and verifies absence.

