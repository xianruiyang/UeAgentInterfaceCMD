# T26 Level/World SDK Projection

When the command is unknown, use positive-keyword `client.query.command_search(...)`,
then `client.query.command_usage([...])` for the selected exact command IDs.
The ordinary workspace authoring path uses the public SDK:

```python
workspace = client.content_graph.export_workspace(
    target,
    name="level_edit",
    profile_id="llm_authoring",
)

# Edit only model-visible HJSON under workspace.path.
result = workspace.import_changes()
```

Export returns the managed workspace handle. Successful semantic directory Import
returns `status: succeeded` with `workspace_refresh`; the refreshed directory contains
the standard exported shape and current baseline. Read that directory for newly created
items instead of routinely exporting again. Edit only model-visible HJSON and
leave `.uai/workspace.hjson` unchanged: its inventory, identities, baseline
content/edit hashes and fingerprints are machine-owned. Import recomputes the
edited unit hashes and semantic fingerprint. Directory Import recovers target and concurrency
context from the hidden manifest; `single_file` and `inline` are create-only with a server-side
missing expectation. Do not extract one structure fragment and submit it as `single_file` or `inline`.
Python contains no Level parser, planner, factory, transaction, persistence or
readback implementation.

Editable native `AWorldSettings` properties are exported into the same Level
workspace's World target `properties.hjson`, grouped by native categories. Edit its current typed property values and
call the same `workspace.import_changes()`. GameMode Override uses the exported
native `DefaultGameMode` property; use its declared class-reference shape. The
common reflection and durable-readback owners apply these settings without
changing omitted properties or using dormant typed World commands.

For staged read-only inspection, `content_graph.structure` returns the `actors`
container and each Actor's `actors/<actor-key>/components` container.
`content_graph.items` uses the same Actor keys as the exported HJSON and the
native Component names within their Actor container. Pass the returned
container and item names directly to subsequent queries; duplicate Component
names across Actors require the container scope. Actor items also provide
`object_ref` for commands that accept a native object reference.
`content_graph.properties` selects these names through `owners` and `containers`.
These queries consume the same Level authoring capture as workspace export,
including its authorability rules and reflected property descriptors.
The `parent` relation identifies a Component's owning Actor; scene attachment
and relative transform remain in the Component item's `attachment` state.

Level Actor items also expose read-only `geometry_components` for attached
InstancedStaticMesh and SplineMesh components, including generated transient
components that are intentionally absent from editable workspace items. ISM
`instances` contain world translation, rotation (pitch/yaw/roll in degrees),
scale and instance index. SplineMesh `start/end` and tangents use world space
and centimeters; `world_transform` records the component transform.
`offsets` are separately tagged `spline_cross_section` and are not included
in the reported centerline endpoints. These observations are not authoring
properties and must not be copied into Level workspace structures.

For edited actors owning active editor PCG components, persistent Level import
settles the native input refresh before saving. PCG-managed meshes and its
non-user-managed World service Actor are excluded from editable source; inspect
the generated result through `geometry_components`. REQ30 verifies this lifecycle
with synchronous Static Mesh Spawner loading, not arbitrary asynchronous PCG graphs.

After all Actor/Component input updates, Level imports publish the final bounds of
new or resized NavMeshBoundsVolume actors, process the world's pending native
navigation updates, and finish submitted generation work on registered navigation
data before capturing the save inventory. Automatically created navigation actors
and their completed updates are saved together, so reload does not recreate their
identity or require regeneration of an intermediate navigation state. Unchanged
bounds are not resubmitted for unrelated edits. The import retains the configured
navigation update policy and does not force a full navigation rebuild. This boundary
applies to directory and inline imports, including caller-controlled map saves.

Use `client.content_graph.diagnostics(...)` for explicit read-only diagnostics;
`ueagentinterfacecmd` exposes the same command-search, command-usage and execution surface.
T13 remains the shared recursive initialization owner: do not use or invent `level_apply_folder`
or another Level-specific HJSON ingress.

To add an Actor, call `client.world.actor_candidates(...)` in the exact World
context and use a supported result. To add a Component, call
`client.blueprint.component_candidates(...)` in the exact Blueprint/SCS context.
In the exported
`actor_component_hierarchy` structure, the model-visible minimum edit is a
keyed Actor item with a direct `name` or `id` field:

```hjson
actors: {
  NativeCube: {
    name: Cube
  }
}
```

The map key is the Actor instance identity. Do not write a nested
`candidate: {name, select?}` object in this semantic workspace. The common keyed-item
projection constructs that internal candidate only after parsing the visible
HJSON. When a non-default placement category is required, copy the category to
the item's declared `placement_context.category` field.

Discovery returns base names. If an import reports a real same-name ambiguity, copy
the returned `select` beside `name` and retry. Actor alternatives may use an asset
`folder`, `class_module` or `factory_module`; these are short semantic namespace values,
not machine paths. `select.folder` identifies the candidate asset's directory, separately
from the placed Actor's folder. Do not invent selector values.

For transform or other fields, first import the minimum item, then read the refreshed
workspace and edit its declared shape. A known extra field may
be supplied on initial creation only when the current export or live detail
declares it; do not infer a legacy actor-array schema or copy an entire search
row.

Use `workspace.import_changes()` for that same directory. Target identity, revision,
apply evidence and independent readback remain service-owned; the caller consumes
the public result and refreshed HJSON. If import reports
`content_graph_import_applied_workspace_refresh_failed`, the asset was applied:
recover the workspace by exporting, rather than replaying the import. Common HJSON source resolution, hidden revision
custody, transaction, persistence and readback remain shared; Level mechanics
own only World/Actor/Component behavior.

Spline Component `SplineCurves` uses the shared property codec, in Blueprint
component templates and Level component instances alike:

```hjson
SplineCurves: {
  type: spline
  value: {
    schema: "uai.spline.points/1"
    points: [
      { input_key: 0, type: "Linear", position: [0,0,0], rotation: [0,0,0,1], scale: [1,1,1] }
      { input_key: 1, type: "Linear", position: [1200,0,0], rotation: [0,0,0,1], scale: [1,1,1] }
    ]
  }
}
```

Positions and tangents are in the Spline Component's local space, in centimeters;
rotation is a quaternion in x/y/z/w order. Point keys must increase. Point types
are `Linear`, `Constant`, `Curve`, `CurveClamped`, and
`CurveCustomTangent`; custom tangent points also provide `arrive_tangent`
and `leave_tangent` three-number arrays. Edit the exported category/property,
not a new Level-specific structure. The shared apply owner synchronizes native
spline state, preserves edited points against construction-script defaults and
rebuilds derived curves. Reparameterization tables and automatic tangents are
not authoring fields. Closed-loop settings remain their separate native properties.
