# Rig/spatial commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
client.animation.ik_probe_candidate_apply(...)
client.animation.subject_morph_weights_update(...)
client.animation.subject_pose_update(...)
client.rig.control_bake_context(...)
client.rig.control_bake_animation(...)
client.rig.control_bake_controls(...)
client.rig.ik_definition_update(...)
client.rig.retarget_assets_generate(...)
client.rig.retarget_definition_update(...)
client.rig.retarget_pose_auto_align(...)
client.rig.retarget_pose_update(...)
client.rig.skeleton_preview_mesh_bind(...)
client.rig.skeleton_socket_update(...)
```

The exact CLI uses ueagentinterfacecmd with the current command name and one JSON
parameter object. No task-specific generated projection remains active.

Every public request carries explicit target/input/context. The server
production binding seam resolves those request values once and freezes them as
real asset/native bindings or the declared current execution context before
operation execution. It reuses the unique TimelineAnimation and
RigSimulationSpatial native ports. An empty binding runtime, fixture-only
injection, Python-held binding state, or direct UE mutation in a command
handler is not a valid fallback.

For Control Rig baking, first export the LevelSequence workspace and use its
readable binding name. `rig.control.bake.context` is a read-only query with
`target=sequence_ref` and `input={sequence_ref, binding_name, rig_ref}`; `rig_ref`
is the generated ControlRig class path. Supply an existing `target_animation_ref`
when preparing animation export. The query resolves exactly one native binding,
its skeletal component, the sequence playback range/display rate, and the same
runtime revisions used by the bake operations. The SDK retains the complete
inputs in `result.rig_bake_context`; use that public handle's `bake_controls()`
or `bake_animation()` method. The latter requires `target_animation_ref` in the
context query. Both return the existing operation Result and accept the same
optional execution `context`. `sequence_ref`, `binding_name`, `authored_range`
and `sample_rate` are readable handle properties. The payload is a summary,
not a replayable bake input: binding/revision custody remains inside the SDK.
Refresh context after editing the sequence/animation or restarting Editor.
Do not infer binding GUIDs, calculate revision hashes, or extract hidden
workspace identity. The query does not create
tracks, evaluate animation, bake, or save assets; those effects remain owned by
the existing bake operations.

```python
prepared = client.rig.control_bake_context(sequence_ref, {
    "sequence_ref": sequence_ref, "binding_name": "Performer", "rig_ref": rig_class_ref,
})
prepared.raise_for_error()
with client.operation.named("bake-performer-controls"):
    started = prepared.rig_bake_context.bake_controls(context={"state_plane": "persisted"})
started.raise_for_error()
receipt = started.operation.finish(timeout=180) if started.operation else started
```

Rig/control/IK/retarget/pose/socket transforms explicitly state
semantic_frame_id, write_frame_id, read_frame_id, verify_frame_id, unit,
basis_evidence, and conversion_chain. Target, skeleton, mesh, chain, control,
pose, time/frame, revision custody, and generation/bake policy come only from
the generated SDK signature for that command.

Success requires native mechanics, applicable settle, terminal projection, and
independent readback in the declared state/frame after reload when persisted.
Invalid/unresolvable bindings or frames fail before mutation; unknown state
requires reconciliation. Cleanup restores transient subject state and removes
only owned durable fixtures, with independent verification.
