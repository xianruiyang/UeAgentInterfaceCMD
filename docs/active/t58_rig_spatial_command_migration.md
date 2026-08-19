# Rig/spatial commands through the default SDK

Discover current contracts through client.command_search(...) and
client.command_detail(...), then use:

```python
client.animation.ik_probe_candidate_apply(...)
client.animation.subject_morph_weights_update(...)
client.animation.subject_pose_update(...)
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

The exact CLI uses uai-cli with the current command ID, hash, and one JSON
parameter object. No task-specific generated projection remains active.

Every public request carries explicit target/input/context. The server
production binding seam resolves those request values once and freezes them as
real asset/native bindings or the declared current execution context before
operation execution. It reuses the unique TimelineAnimation and
RigSimulationSpatial native ports. An empty binding runtime, fixture-only
injection, Python-held binding state, or direct UE mutation in a command
handler is not a valid fallback.

Rig/control/IK/retarget/pose/socket transforms explicitly state
semantic_frame_id, write_frame_id, read_frame_id, verify_frame_id, unit,
basis_evidence, and conversion_chain. Target, skeleton, mesh, chain, control,
pose, time/frame, expected revision, and generation/bake policy come only from
command_detail.

Success requires native mechanics, applicable settle, terminal projection, and
independent readback in the declared state/frame after reload when persisted.
Invalid/unresolvable bindings or frames fail before mutation; unknown state
requires reconciliation. Cleanup restores transient subject state and removes
only owned durable fixtures, with independent verification.

