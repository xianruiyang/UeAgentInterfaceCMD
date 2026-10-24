# Animation curve and sequence commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
client.animation.blend_space_asset_create(...)
client.animation.blend_space_sample(...)
client.animation.sequence_pose_sample(...)
client.animation.sequence_root_motion_analyze(...)
workspace = client.content_graph.export_workspace(...)
workspace.import_changes()
client.content_graph.import_inline(...)
```

The exact CLI uses ueagentinterfacecmd with the current command name and one JSON
parameter object. Inspect a nested query parameter from the generated contract:

```powershell
ueagentinterfacecmd describe animation.sequence.pose.sample --parameter input --pointer /properties/time_point
ueagentinterfacecmd describe animation.sequence.root_motion.analyze --parameter input
```

These local descriptions expose the actual required fields, types, constants,
enums and interval bounds. No task-specific generated projection remains active.

BlendSpace definitions, AnimSequence bone tracks/curves/events/metadata, Montage
structure and PoseAsset source pose data use ordinary HJSON workspace export/import.
Missing Montage targets and PoseAssets sourced from an existing AnimSequence can
be created with `import_inline`; the root fields are documented in T23.
Their former typed mutations and
asset `read` commands are dormant compatibility identities, not default named
SDK methods. Pose sampling, root-motion and BlendSpace sampling remain separate active
queries; workspace export does not replace evaluation.

Content targets accept current names returned by `query.content.search` through
the shared content resolver, as well as exact object paths. Explicit runtime
subject and rig bindings retain priority; they are not reinterpreted as assets.

For BlendSpace sampling, each `blend_parameters` item binds by `axis_ref`, not
array order. Use `x`/`y`/`z`, the native `axis_index` as a string (`0`/`1`/`2`),
or a unique native axis display name from the exported definition. Coordinate
and index identifiers take precedence over display names. Omitted coordinates
are zero; unknown, ambiguous or duplicate axes return an explicit diagnostic.

AnimSequence pose/root-motion query points use the exact native clock
`animation_sequence:<full UObject path>` and the asset's native frame rate.
Root-motion analysis requires explicit lower and upper points; open bounds are
not an implicit full-animation range. Obtain duration/frame rate from the current
asset document and specify the intended interval. Semantic time errors identify
the required clock/rate/bounds rather than reporting a missing readback.

HJSON writes use the common durable operation lifecycle. Skeleton, bone, curve,
event, metadata, Montage and BlendSpace fields come from the exported domain
document; query parameters come from the generated signature and on-demand parameter schema. Pose, bone-track, root-motion, and
blend-space spatial values explicitly carry semantic_frame_id, unit,
basis_evidence, and conversion_chain; the SDK does not infer them.

Write success requires terminal projection and independent persisted readback
after reload. Invalid skeleton, track, curve, key, event, montage section,
sample, timebase/frame, spatial frame, or stale revision fails before mutation.
Unknown state requires reconciliation. Cleanup removes only owned fixtures and
verifies absence independently.
