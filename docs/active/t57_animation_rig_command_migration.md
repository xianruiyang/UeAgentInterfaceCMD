# Animation rig commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
client.animation.control_rig_asset_create(...)
client.animation.control_rig_shape_library_asset_create(...)
client.animation.ik_retargeter_asset_create(...)
client.animation.ik_rig_asset_create(...)
client.animation.ik_rig_definition_auto_generate(...)
workspace = client.content_graph.export_workspace(...)
workspace.import_changes()
```

The exact CLI uses ueagentinterfacecmd with the current command name and one JSON
parameter object. No task-specific generated projection remains active.

Control Rig, IK Rig, and IK Retargeter creation remain explicit until the generic
asset candidate/create chain proves non-interactive equivalence. Definition,
graph, settings, compatibility, and virtual-bone mutations use the AnimationRig
HJSON root through content_graph.import_workspace and the common durable operation
lifecycle; their former typed IDs are internal operation kinds, not public SDK
methods. Shape-library editing and Skeleton slots use ordinary workspace
export/import; their former typed apply/read identities are dormant.
Shape-library asset creation and IK auto-generation remain explicit active
capabilities. Editable Skeleton, bone, hierarchy/control, shape, chain and
retargeter/IK Rig fields come from the exported document; creation and
auto-generation parameters come from the generated SDK signature. All transforms and
axis/chain data explicitly carry semantic_frame_id, write/read/verify frame,
unit, basis_evidence, and conversion_chain. The SDK does not infer rig or
spatial business.

Control Rig hierarchy local, control offset, and shape transforms can change
slightly on saved readback because UE persists their compact representation.
The native serializer can round components to float precision or elide
near-identity components; import verification follows that storage behavior.

Write success requires native compile/settle where declared, terminal
projection, and independent persisted readback after reload. Invalid skeleton,
bone, hierarchy, graph, shape, chain, axis/frame, compatibility, or stale
revision fails before mutation. Unknown state requires reconciliation. Cleanup
removes only owned rig/retarget/skeleton fixtures and verifies absence.
