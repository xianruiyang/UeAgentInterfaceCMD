# Animation curve and sequence commands through the default SDK

Discover current contracts through client.command_search(...) and
client.command_detail(...), then use:

```python
client.animation.blend_space_asset_create(...)
client.animation.blend_space_definition_apply(...)
client.animation.blend_space_sample(...)
client.animation.montage_create(...)
client.animation.montage_read(...)
client.animation.montage_structure_replace(...)
client.animation.sequence_bone_tracks_replace(...)
client.animation.sequence_curves_update(...)
client.animation.sequence_events_update(...)
client.animation.sequence_metadata_update(...)
client.animation.sequence_pose_sample(...)
client.animation.sequence_read(...)
client.animation.sequence_root_motion_analyze(...)
```

The exact CLI uses uai-cli with the current command ID, hash, and one JSON
parameter object. No task-specific generated projection remains active.

Creation and update/replace calls use the common durable operation lifecycle;
read, sample, pose, and root-motion analysis calls retain their query state
layer. Skeleton/bone/curve/event/metadata/montage/blend-space identity,
display/tick rate, seconds/frame convention, expected revision, and sampling
policy come only from command_detail. Pose, bone-track, root-motion, and
blend-space spatial values explicitly carry semantic_frame_id, unit,
basis_evidence, and conversion_chain; the SDK does not infer them.

Write success requires terminal projection and independent persisted readback
after reload. Invalid skeleton, track, curve, key, event, montage section,
sample, timebase/frame, spatial frame, or stale revision fails before mutation.
Unknown state requires reconciliation. Cleanup removes only owned fixtures and
verifies absence independently.

