# T23 Animation/Curve domain through the default SDK

Discover current contracts with `client.query.command_search(...)` and the
generated SDK. Use `client.content_graph.import_inline(target, document)` for
inline documents or `workspace.import_changes()` for an exported workspace;
independent readback uses `client.content_graph.structure(...)` or a fresh export.
The shared `client.content_graph.export_workspace(...)` command publishes the
registered AnimSequence, BlendSpace, AnimMontage or PoseAsset authoring workspace for existing assets.
Semantic-directory import includes declared root UObject properties and the
AnimSequence `animation` document. The SDK owns command bindings; callers do not pass hashes or task-specific
bindings.

T13 is the sole HJSON initialization and recursive composition authority. T23
contributes its Animation/Curve domain contract and delegates curve, channel,
key, notify, compression, refresh, persistence, and readback to T56. The SDK
does not implement those mechanics; unsupported creation fails before write.

## Missing-root animation documents

The registered Animation family uses `schema: "uai.animation_curve.edit/1"`.
Creation settings are directly under the literal `root.create`. Pass the target
separately to `client.content_graph.import_inline(target, document)`; the public
entry supplies the missing-target expectation and source carrier. The complete
Montage document is:

```hjson
schema: "uai.animation_curve.edit/1"
root: {
  type: "/Script/Engine.AnimMontage"
  create: { source_animation_ref: "/Game/Example/AS_Source.AS_Source" }
}
```

Use an actual source reference and a new target such as
`/Game/Example/AM_New.AM_New`. The same outer shape applies to the following
registered types; substitute only `root.type` and `root.create`:

| Asset | `root.type` | Required `root.create` fields |
| --- | --- | --- |
| AnimSequence | `/Script/Engine.AnimSequence` | `skeleton_ref` supplies the skeletal context; an empty sequence may omit it |
| Montage | `/Script/Engine.AnimMontage` | `source_animation_ref` or `skeleton_ref` |
| PoseAsset | `/Script/Engine.PoseAsset` | `source_animation_ref` |
| BlendSpace 1D | `/Script/Engine.BlendSpace1D` | `skeleton_ref`, `dimension: 1` |
| BlendSpace 2D | `/Script/Engine.BlendSpace` | `skeleton_ref`, `dimension: 2` |

BlendSpace creation may include `root.axes` and `root.samples` in the same import;
omitted definitions retain UE factory defaults. AnimSequence creation uses the
native factory and shared Animation transaction. Export the result for ordinary
workspace editing.

For a new AnimSequence curve, use the generated guide for its `float_curves` or
`transform_curves` index file. A scalar curve contains
`channels: { value: { value_type: "float", keys: [...] } }`; retain the `value`
channel wrapper. Animation curves cannot author `default_value`, and transform
subcurves cannot author extrapolation. Their examples omit these fields.
CurveFloat/Vector/LinearColor have different writable subsets and publish their
own templates; do not infer animation creation fields from another asset type.
Invalid curve fields report the original HJSON file and leaf location when that
input exists; missing fields locate the nearest authored container.

Missing-root inline creation supports BlendSpace with a skeleton and dimension
1 or 2. Native axis/sample editing may accompany creation. AnimSequence supports
missing-root creation; ordinary root-property workspace edits preserve its native
document without resending curves or keys.

Root-property and AnimSequence structure imports use the shared Animation
provider transaction for mutation, saving, package reload, and final readback.
Existing non-directory AnimSequence change documents may combine
`metadata_changes`, `curve_changes`, and `event_changes`. They are prepared on
one proposed asset and applied in one shared transaction, including the retained
Timeline compatibility bindings. A later invalid change cannot leave an earlier
category committed. Verification compares the complete sequence document.
For compatibility `event_changes`, `event_ref` selects the exported row's
`instance` within its event collection. A unique event name is also accepted;
ambiguous names fail instead of changing the first match. New events use a new
name. Re-export after applying changes before selecting rows for another import.
New notifications inherit their class's default trigger weight threshold;
the compatibility adapter does not turn captured struct defaults into explicit
property overrides. Existing notification settings remain preserved.
Late readback rejection restores the prior dirty in-memory state and original
package bytes independently. AnimSequence exposes `animation` through shared
whole-value projection: frame rate/count, named bone tracks, float curves and nine
transform subcurves. Bone values use the shared struct codec; curve values use the
shared rich-curve codec and native Animation Data Controller. The current `skeleton`
is read context; skeleton reassignment is not exposed. BlendSpace's reflected
`BlendParameters` and `SampleData` use shared property editing and native sample
validation/resampling in the Animation lifecycle.
Notifications use `notify_tracks`, `notifies` and `sync_markers`; retained records
keep their exported `instance`, while new records omit it. Notification time and
duration are seconds, and `track_index` addresses the authored track array.
Use `client.asset.owned_candidates(target, {"property_path": "Notifies[0].Notify"})`
for native Notify candidates (or `NotifyStateClass` for states), then use the returned
name in the shared `owned_object` value. `animation.metadata` edits the package's
object metadata string map, independently of instanced UAnimMetaData objects.

Empty and populated event collections both export current minimum examples under
workspace `examples/`. Follow `examples/index.hjson` to the actual event file;
its guide includes named Notify, owned Notify/NotifyState, track and sync-marker
shapes as applicable. Merge the selected example into business `value`, preserving
existing records. `settings` uses native Details categories for Notify events and
the common struct `fields` shape for tracks/markers. Examples are read-only;
replace placeholders using current candidates. Candidate queries support prospective
array positions, so no dummy Notify is needed before querying its owned property.

Transform keys/tangents are editable; transform extrapolation is omitted because
UE5.6's native Sequencer controller cannot write it. Scalar extrapolation remains editable.
Montage inline creation uses `root.type: "/Script/Engine.AnimMontage"` with
`root.create.source_animation_ref` or `root.create.skeleton_ref`. Its workspace
`animation` document contains ordered slots/segments and sections. Segment positions
are derived from ordered lengths; section `time` and `next_section` are explicit
structure fields. Retained records keep their exported `instance`; new records omit it.
Section `properties.Section.MetaData` uses shared owned-object values; query candidates
with `CompositeSections[0].MetaData`. The active plan maintains the remaining verification
status; this contract does not declare Animation-family completion.
Existing AnimSequence fixtures can be prepared with the public
`client.asset.object_clone(...)` command; this is a copy of an existing animation,
not missing-root AnimSequence creation.

PoseAsset missing-root creation uses `client.content_graph.import_inline` with
`schema: "uai.animation_curve.edit/1"`, `root.type: "/Script/Engine.PoseAsset"`, and
`root.create.source_animation_ref` naming an existing AnimSequence. The native
PoseAsset factory establishes its skeleton and source poses; export the result
before editing. In the ordinary workspace, `pose_asset_document.value` contains
`pose_data`, `pose_data_definitions`, and `settings`. The categorized reflected
pose rows expose names, tracks, source local-space transforms and source curve
values. Reuse their definitions and maintain matching pose/track/curve dimensions.
`settings.additive` and `settings.base_pose` select the native representation and
base pose by name (`None` means no named base). Native `ConvertSpace` rebuilds
derived pose data and caches; those caches are not separate authored content.
Create/export, pose rename, source transform/curve edits, pose insertion/removal,
and additive/base-pose changes have independent persisted readback evidence.
