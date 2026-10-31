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
leave `.uai/` unchanged: its manifest, captured baseline files, identities, baseline
content/edit hashes and fingerprints are machine-owned. Import recomputes the
edited unit hashes and semantic fingerprint. Directory Import recovers target and concurrency
context from the hidden manifest; `single_file` and `inline` are create-only with a server-side
missing expectation. Do not extract one structure fragment and submit it as `single_file` or `inline`.
Python contains no Level parser, planner, factory, transaction, persistence or
readback implementation.

For basic placement, mesh/material replacement, native light intensity/radius and
PostProcessVolume settings, opt into the Level profile:

```python
workspace = client.content_graph.export_workspace(
    target, name="level_scene", profile_id="scene_editing",
)
workspace.result.raise_for_error()
# Edit the exported scene values or membership; retain unedited Settings fields/override flags.
result = workspace.import_changes()
result.raise_for_error()
```

The default remains `llm_authoring`. `scene_editing` keeps Actor/component structure
and basic placement/render/lighting properties; the exact native class/field scope is maintained in
[Plugin T26](../../../Plugins/UeAgentInterface/docs/active/t26_level_world_domain.md#optional-scene-editing-profile).
Unexported properties are preserved, not reset. Import recovers this profile from
the workspace and refreshes in the same profile; do not add an import parameter or
change machine files. Use a separately named full workspace when other fields are
needed. Neither workspace tracks edits made through the other: consume current
refreshes or re-export if a baseline is stale. Recovery/persistence can still capture
full state internally; this is not a promise that every import stage becomes narrow.

### Read a proposed scene and analyze geometry before applying

The optional read-only analysis path uses the same native preparation as directory
Import. It does not apply the HJSON or execute Blueprint construction in a temporary
World. A context query is useful for design decisions; geometry analysis can also be
called directly:

```python
context = workspace.scene_context(limit=40)
overlap = context.geometry_overlap(limit=40)  # shares the preparation and snapshot
print(overlap.result.payload["analysis"])
# Read another page or one object's facts without exporting the level again.
page = overlap.geometry_overlap(offset=40, limit=40)
# After deciding whether the geometry facts are intended:
result = workspace.import_changes(analysis=overlap)
```

After editing HJSON again, call `workspace.scene_context()` or
`workspace.geometry_overlap()` again. An existing handle identifies its analyzed
version; it is not a request to reinterpret newly edited files. `analysis=` binds
the actual normalized operation, relevant live objects, assets and neighborhood
membership. A stale or superseded reference must be analyzed again. Ordinary
`workspace.import_changes()` remains available with its existing semantics.

For the current loaded scene, the two exact command IDs are `world.scene_context`
and `world.geometry_overlap`. Supply `input.targets` with exact Actor/component
references, or `input.regions` with `min_cm`/`max_cm` triples. `margin_cm` adds
context around each region; `near_distance_cm` controls the reported near-surface
distance, not a universal safe spacing. The default is 0.01 cm. For example:

```python
result = client.execute("world.geometry_overlap", {"input": {
    "regions": [{"min_cm": [0, 0, 0], "max_cm": [400, 400, 300]}],
    "limit": 40,
}})
if result.operation is not None:
    result = result.operation.finish_result()
result.raise_for_error()
analysis = result.payload["analysis"]
```

`payload.analysis` contains counts, timings, paged `objects` or `facts`, and
explicit coverage/limitations. Reuse the returned `analysis_ref` in either command
for another projection/page; `object_ref` filters one exact object. Each of objects,
facts, surface totals and coverage has its own count and `has_more` indication.
Names are navigation data, not a statement of narrative purpose. Geometry facts
are not pass/fail design judgments or proof of visible Z-fighting. See
[the native contract](../../../Plugins/UeAgentInterface/docs/active/t26_level_world_domain.md#scene-context-and-geometry-analysis)
for representations, ratios, unsupported cases and resource bounds.

A successful bound import also returns `payload.scene_analysis`. It distinguishes
the saved mutation from the post-apply comparison. `geometry_recheck_required`
means that native results differed or could not be predicted; use the handle's
context projection to page `recheck_objects`, then analyze those actual objects and
their neighborhood. The old handle becomes a historical analyzed snapshot, not a
fresh scene read. Recover a transport-interrupted import through the existing
operation/recovery path; do not replay the mutation to obtain diagnostics.

Editable native `AWorldSettings` properties are exported into the same Level
workspace's World target `properties.hjson`, grouped by native categories. Edit its current typed property values and
call the same `workspace.import_changes()`. GameMode Override uses the exported
native `DefaultGameMode` property; use its declared class-reference shape. The
common reflection and durable-readback owners apply these settings without
changing omitted properties or using dormant typed World commands.

The same World properties contain `General.level_world.value`. For legacy
streaming, edit `streaming_levels`, keyed by existing map package paths. Rows
declare `streaming_class`, `editor_visible`, `transform`, and (for Dynamic
subclasses) `initially_loaded`/`initially_visible`. Set a row to `null` to unlink
the map without deleting its asset; omissions preserve baseline state. Actor
hierarchy items expose `level`: changing it moves the Actor to the persistent map
or a loaded associated sub-map, preserving world placement. Consume refreshed
identities after a native move. Hidden loaded sub-map Actors/Components are editable.
The shared transaction saves source and target maps and verifies reloaded state.

In the Editor, associated legacy sub-maps remain loaded; `editor_visible` is not
a runtime streaming request. `world.streaming_levels` separately reports actual
`loaded`/`visible`, `editor_visible`, requested `should_be_loaded`/`should_be_visible`,
and Dynamic `initially_loaded`/`initially_visible`. Runtime behavior requires its
own validation. The Level transform uses centimeters and pitch/yaw/roll degrees.

For an ordinary saved map, use the native `partition-convert` WorldBuild policy
described in [T59](t59_world_command_migration.md). It creates a separate `_WP` map;
`create_world_partition` on blank-map creation is a different workflow.
On an existing World Partition map, use
`General.level_world.value.world_partition.streaming_enabled`. Default HLOD Layer
and other reflected WP settings use the existing `WorldPartitionSetup.WorldPartition`
owned-object properties; Actor spatial loading, RuntimeGrid and HLOD Layer use
their exported native property units. Export includes unloaded WP Actors through
scoped native descriptor loading. HLOD Layer asset editing and native generation
are separate operations; see [T59](t59_world_command_migration.md). Enable Streaming
only toggles streaming on an existing partition; it does not convert map formats.
Generated HLOD component `bVisible` is controlled by UE's Editor HLOD subsystem
and is not exported as a persistent edit; normal component visibility is unchanged.
Use `world.partition(input={"include_actor_descriptors": True})` for descriptor-only
inspection of unloaded Actors, external packages, membership and loading status.

Create a DataLayerAsset through `uai.world_data_layer.edit/1` (root type
`/Script/Engine.DataLayerAsset`, asset kind `data_layer`), or edit its exported
Reflection workspace. In the map's `General.level_world.value.data_layers`, add
an entry keyed by the exact existing asset object path, for example:

```hjson
"/Game/Maps/DL_Stage.DL_Stage": {
  initially_visible: true
  initial_runtime_state: "Activated"
}
```

`initial_runtime_state` accepts `Unloaded`, `Loaded`, or `Activated` on Runtime
layers only. The native instance is created when missing. Omitted rows/fields
preserve existing state; null deletion, hierarchy and private/external Data Layers
are not supported. Actor membership uses the exported `DataLayers.DataLayerAssets`
array of asset references, with the normal Level save/reload transaction. Initial
runtime state is configuration; temporary Editor loading/visibility uses the
`data-layer-editor-state` session in T59 and is restored on close.

For staged read-only inspection, `content_graph.structure` returns the `actors`
container and each Actor's `actors/<actor-key>/components` container.
`content_graph.items` uses the same Actor keys as the exported HJSON and the
native Component names within their Actor container. Pass the returned
container and item names directly to subsequent queries; duplicate Component
names across Actors require the container scope. Actor items also provide
`object_ref` for commands that accept a native object reference.
`content_graph.properties` selects these names through `owners` and `containers`.
Results are in `payload.entries`; do not use the internal adapter's
`owner_ids`/`field_ids` names or expect `payload.items`. Query values locate current
state; the workspace's typed property documents are the editing contract.
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

## Actor creation and component scope

To add a Level Actor, call `client.world.actor_candidates(target=target, query=...)`
with the saved World target and use a supported result. `category` is optional
placement context. `client.blueprint.component_candidates(...)` instead requires
a Blueprint/SCS target and cannot discover components for a placed Level Actor.
For a placed Level Actor use `client.world.component_candidates(target=actor_object_ref, ...)`,
where the exact `object_ref` comes from `content_graph.items`. Its Actor-owned
`components` collection supports instance additions/removals through the same
workspace import. For independent scene parts, place separate Actors; component
support does not require or justify a whole-scene Blueprint/container.

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

The `world.actor.candidates` and `blueprint.component.candidates` commands currently
have no candidate `describe` parameter. A names-only result is not an initial
property descriptor. Add known placement fields (`label`, `folder_path`, `level`,
`transform`) using their current exported shape, in the same first import when
already known; an extra empty-Actor import is not required just to set placement.
For a mesh candidate, native placement supplies its mesh component. Reflected
component fields come from the refreshed workspace after creation; do not put
`StaticMesh`, `OverrideMaterials`, or arbitrary initial `properties` on an Actor
creation row. Use the generated `examples/index.hjson` for the current collection,
not a legacy actor-array schema or an entire search result.

## Creating and removing Level instance components

Query a small candidate/property scope before constructing a new component:

```python
result = client.world.component_candidates(
    target=actor_object_ref,
    describe={"name": "Point Light", "fields": ["Intensity", "AttenuationRadius"]},
)
result.raise_for_error()
description = result.payload["description"]
```

Use a returned candidate name; do not guess localized names or `select` values.
The result gives native defaults, creation support, and `unavailable_fields` when
requested properties are not editable. Copy only the needed returned property
descriptors and change their values. In the exported Actor-owned `level_components`
structure, retain existing rows and add:

```hjson
components: {
  // Keep the captured rows here.
  GuideLight: {
    name: Point Light
    // properties: [selected description.properties with edited values]
  }
}
```

The new map key is a valid UE object name. `name` selects the component type;
`select` resolves actual name ambiguity. `properties` is the common descriptor
array returned by `describe`, not an arbitrary map of property names. Omission
uses native defaults. An optional `attachment` follows the current Level-exported
shape; do not substitute Blueprint `parent` syntax. Import creates, initializes,
saves and refreshes through the existing public workspace path.

Remove an instance-added component by deleting its exact captured map key and
importing the same workspace. Keep unrelated keys. Native/class/SCS components
cannot be removed this way because their owner reconstructs them; edit that source
instead. Removing component files/directories is not deletion. Do not simultaneously
remove a component and edit its state/properties, or remove an Actor while editing
its components. Existing components' `class` is captured type context; their
ordinary `properties.hjson` remains the property-editing owner.

The collection belongs to an already captured Actor. When creating an Actor,
consume the import refresh before adding components. This does not change Actor
candidate defaults or add `describe` support to `world.actor.candidates`.

## Component properties and same-Actor replacement

Resolve the Actor key, component container, and native component name from
`content_graph.structure/items`. For example, after those names are known:

```python
result = client.content_graph.properties(
    target=target,
    input={
        "containers": ["actors/<actor-key>/components"],
        "owners": ["<component-name>"],
        "fields": ["StaticMesh", "OverrideMaterials", "BodyInstance"],
    },
)
result.raise_for_error()
entries = result.payload["entries"]
```

Replace the placeholders with returned names. Many Actors have a component named
`StaticMeshComponent0`; its Actor container is required to disambiguate it. Use
only fields applicable to that component type.

Export once using the SDK-managed workspace, not a raw `workspace_path` argument
to CLI dispatch:

```python
workspace = client.content_graph.export_workspace(
    target, name="scene-edit", profile_id="llm_authoring"
)
workspace.result.raise_for_error()
print(workspace.path)
```

Locate the component's ordinary `properties.hjson` under the returned workspace.
The query Actor key may be its label while the directory uses its native object
name; do not construct a file path from the label. In that file, change the
existing `categories.StaticMesh.StaticMesh.value` and/or
`categories.Rendering.OverrideMaterials.value` when those categories are exported.
An `object_ref` value is the replacement asset's exact object-path string;
`object_ref[]` is an array of such values. Preserve the file's actual category,
`type`, and `definition` rather than copying a definition number from an example.
Leave the Actor's hierarchy row, class and component identity intact. Incoming
Actor and component references then continue to target the same objects in the
ordinary StaticMeshActor case. Renaming a newly created Actor to the old label is
not an identity-preserving replacement.

This changes the placed component's references, not the shared assets. Reconcile
material slot indices, mesh-local pivot/bounds and any required collision changes
with the selected mesh; changing `StaticMesh` alone does not establish placement
or collision correctness. Material overrides are indexed by the new mesh's slots;
map the intended materials to those slots and clear obsolete overrides using the
exported array shape (`null` for a slot that should use the mesh material, or an
empty array when no instance overrides are wanted). Do not retain surplus old
overrides merely because the import accepts them. For a construction-script-owned
component value, edit the actual Blueprint owner when an instance override would
be overwritten; reconstruction can also change component identity.

For a mesh/material-only edit, `scene_editing` can reduce export cost. Use a full
workspace if this replacement also edits collision or referring properties. Reuse
successful refresh rather than capturing the map again after each small change.

## Stage management with existing HJSON

Use the existing Level workspace for all three stages. At creation, assign Actor
`folder_path` such as `SceneContent/LevelBlockout/Region/Part`,
`SceneContent/ArtBlockout/Region/Part` and `SceneContent/FinalScene/Region/Part`.
Use one scene-content root with stage folders immediately beneath it; nesting
inside a stage is flexible. Every scene-content Actor, including lights and
gameplay, must be below a stage folder. Retain the project's established names
when they express this structure; do not put a separate `Shared`/`Environment`
group beside the stages. Shared gameplay can be grouped inside its owning stage.
For an existing Actor carried into the next stage, retain its identity/references
and update `folder_path` to that receiving stage before retiring the old content;
record the old folder if the transfer must be reversible. This concerns placed
instances, not duplicating source assets in the Content Browser. A folder is
organization, not an enable/disable switch. Stage state is not a new HJSON schema
or command.

For a reversible transition, keep the old Actor/component rows. Select the actual
replaced instances, including their old dedicated collision and auxiliary
presentation, while preserving other regions and shared gameplay. Capture their
public identities and original values in the existing layout/replacement record.
Do not reduce the full `actors` map to a selected subset: omission requests removal.

Export with `profile_id="llm_authoring"` using the workspace call above. The
optional `scene_editing` profile supports display edits, but excludes the collision
fields required for static retirement. Locate the applicable native properties
in the captured Actor/component documents; edit their `value` while preserving
the actual `type`, `definition` and unrelated fields:

| Property | Retained static blockout's off-stage value |
| --- | --- |
| Actor `bHidden` | `true` (game-hidden) |
| Component `bVisible` / `bHiddenInGame` | `false` / `true` |
| Primitive `CastShadow` / `bGenerateOverlapEvents` | `false` / `false` |
| StaticMeshComponent `bUseDefaultCollision` | `false` |
| `BodyInstance.value.fields.CollisionProfileName` | Native `NoCollision` profile where supported by the project |
| `BodyInstance.value.fields.CollisionEnabled` | `NoCollision` |

These are field edits inside the existing exported wrappers, not a replacement
component document. `bHidden` alone does not hide an Actor in the Editor;
component visibility is needed for persistent display isolation. Apply the
relevant settings to each component that contributes to the old presentation.
If only comparing visuals temporarily, do not describe remaining collision or
behavior as inactive.

For StaticMeshComponent, **do not omit `bUseDefaultCollision=false`** when the
instance must stop colliding. UE otherwise takes collision from the mesh asset:
an import can return success with a readback warning and the object still blocks.
Set that flag and the `BodyInstance` settings in the same import. Do not modify the
shared mesh asset or rely on HJSON field order. Preserve the original complete
collision configuration for restoration; switching profile can also normalize
`ObjectType` and `CollisionResponses`.

Import once for the known batch. Consume warnings and `workspace_refresh`, not
only top-level `ok`. A relevant `readback_mismatch` means the intended state was
not established; inspect the actual refreshed values before a dependent action.
For collision retirement, a bounded `world.capsule_path` or other applicable
static query through the old collider distinguishes a real state change from
visibility-only success. It does not verify runtime gameplay. A valid refreshed
workspace is reusable; do not repeatedly export the entire map after each edit.

To restore, use that current workspace (or export again if stale), resolve the
same instances, and restore the recorded original values including collision
inheritance and normalized collision fields. Merge only the affected fields;
keep later unrelated Actor additions, transform/material changes and other stage
content. If another edit changed one of those fields, reconcile that change rather
than blindly overwriting it. Keep current type definitions; they can be regenerated
after normalization. Do not copy an old whole workspace or assume every original
flag was true. Retire the corresponding replacement presentation when returning
to the old one; keep stage ownership so it remains recoverable.

For behavior-bearing content, use its existing Blueprint/component lifecycle and
report what was actually stopped. Hiding, NoCollision and disabled Tick do not
prove timers, AI, interactions, audio or effects stopped; `bAutoActivate=false`
only configures initialization. Old light contributions, navigation and baked
data are separate from this mesh recipe. Retaining instances also does not unload
their assets or exclude them from cooking. Existing sublevel/Data Layer workflows
remain available for suitable maps; temporary Editor state and runtime state
must not be conflated. No PIE is required to edit these configurations.

Bounded verification (UE 5.6, 2026-10-29): three independent static-mesh Actors
were placed in distinct stage folders on a temporary ordinary Level. Retiring
only the level-blockout Actor produced no readback warnings with the complete
recipe; a Pawn-channel capsule path changed from blocked to clear and remained
clear after saving and reopening the map. Restoring original values returned
the blocker with the same component identity; all 25 public workspace documents
returned to their baseline, with the other two Actors unchanged. The fixture was
deleted and GreyCanal restored without edits. This covers static instance
configuration, persistence, scoped preservation and that collision query; it does
not certify rendered pixels, Blueprint/runtime deactivation, baked lighting,
navigation rebuilds, loading performance or cook exclusion. No PIE was started.

## Composing new parts and retiring old Actors

For permanent removal, in the original workspace's `actors` map, add the new candidate rows and delete
only the exact keys of Actors being retired. Keep every unrelated captured row;
replacing the map with a short selection would request deletion of the omitted
Actors. Do not hand-write `operation`, internal GUIDs, or hidden manifest entries.
Removing a Component file/directory is not a public Component deletion method.
For retained, recoverable old-stage instances, keep those rows and use the stage
retirement procedure above instead of deletion.

Before editing, identify what is replaced and which relationships need to survive:
old Actor/component -> replacement part(s), retained gameplay owner, known referring
field -> responsible new target, and old-content disposition. Keep this in the
existing layout/replacement record when recovery or multiple steps require it;
do not add a parallel replacement registry. One old visual object can become
several independently placed parts, while a scalar reference still needs one
semantically appropriate target. A reference to an interaction owner may belong
on the retained gameplay Actor rather than on any new decorative mesh.

If the new Actors need only known placement fields and no unresolved target
references, additions and removals can share one import. Otherwise:

1. Add the new Actor rows with known placement and stage ownership, preserving
   old and unrelated rows. Import and consume the same workspace refresh.
2. Obtain actual new Actor/component identities and exported property documents.
   Configure those parts and explicitly update the needed supported references.
3. Retire old presentation: remove the precise old keys for permanent replacement,
   or apply the preceding stage-retirement recipe for reversible retention.
   Configuration, reflected reference changes and removal can share this import
   once the new targets exist. Do not also edit the deleted Actor's properties.

Keep the intermediate overlap out of completion screenshots. Independent old
collision, lights and other presentation follow their actual ownership, not only
the old mesh's name. Keep genuinely shared gameplay active. An unsuccessful or
uncertain import is not an instruction to replay the whole replacement.

New Actors do not inherit old identities or incoming references. A folder-scope purge is useful
only when that complete folder scope is intended; it is not required for an exact
keyed Actor replacement. Same-workspace transaction behavior and remaining
boundaries are defined in [Plugin T26](../../../Plugins/UeAgentInterface/docs/active/t26_level_world_domain.md#replacement-through-the-existing-workspace).

Use `workspace.import_changes()` for that same directory. Target identity, revision,
apply evidence and independent readback remain service-owned; the caller consumes
the public result and refreshed HJSON. If import reports
`content_graph_import_applied_workspace_refresh_failed`, the asset was applied:
recover the workspace by exporting, rather than replaying the import. Common HJSON source resolution, hidden revision
custody, transaction, persistence and readback remain shared; Level mechanics
own only World/Actor/Component behavior.

### Finding and rebinding the relevant references

For the selected map, use a current full `llm_authoring` workspace. Search its
ordinary `targets/` content for the exact old Actor/component paths and inspect
the referring property or relationship, including nested values. Keep dependency
summaries and generated definitions out of the edits. This is scoped discovery,
not proof that all consumers across the project have been found. The scene profile
omits most reference-bearing properties. Other maps, Level Script/Blueprint nodes,
Sequence bindings, soft references and name-based lookup logic may need their own
existing domain entry according to the known consumer; do not blindly replace
the old string across files.

Do not substitute `asset.relations` (on-disk Asset Registry dependencies), Level
`content_graph.relations` (membership/component ownership), or
`reference.origin.resolve` for an Actor incoming-reference query. None currently
enumerates all reflected Actor-field referencers in a Level.

For an ordinary reflected Actor reference, obtain the new value through the
existing query. For example, after creating a part named `NewPrimary`:

```python
items = client.content_graph.items(
    target=target,
    input={"containers": ["actors"], "items": ["NewPrimary"],
           "fields": ["name", "object_ref"]},
)
items.raise_for_error()
new_actor_ref = items.payload["entries"][0]["object_ref"]

reference = client.content_graph.properties(
    target=target,
    input={"containers": ["actors/RefOwner/components"],
           "owners": ["MyConstraintComp"], "fields": ["ConstraintActor1"]},
)
reference.raise_for_error()
```

`RefOwner`/`MyConstraintComp` are example names from a Physics Constraint fixture,
not a required scene pattern. In that existing component's exported document,
replace only `ConstraintActor1.value` with the returned `new_actor_ref` string,
keeping its `object_ref` type/definition. Query values can display `{path: ...}`;
the HJSON authored value uses the exported string form. For a component reference,
obtain the actual component's `object_ref` and respect the property's required
class; an Actor path cannot substitute for a component path. New generated alias
numbers can change after membership edits without changing native object identity.

Explicitly rebind known relationships before or in the supported same-world
removal import; otherwise native deletion may leave null/unresolved consumers.
Separate asset imports are not one transaction. If a consumer has no supported
rebind path, retain its still-needed logical owner and retire only the old
presentation where valid, or report that specific migration unfinished. Do not
clear the reference or duplicate behavior merely to make removal succeed.
Actor attachment is a separate relation: its current `parent_managed_id` field
does not accept an Actor key or `object_ref`; preserve existing valid exported
values and do not invent identifiers for a new parent. See Plugin T26 for this
boundary. Reversible visual restoration also needs the original reference values
if this transition transferred them; restoring visibility alone does not undo a
reference change.

Consume the refreshed component values, surviving native identities and old-content
disposition. Verify only the relationships and spatial/runtime behavior relevant
to this replacement; configuration success does not certify appearance, traversal,
animation or gameplay. Bounded ordinary-Level verification (UE 5.6, 2026-10-29)
covered Cube -> Sphere plus a material override on the same Actor/component,
preserving a Physics Constraint's Actor reference and other exported object state.
It also covered creating two parts, then in one import configuring the primary
part, transferring `ConstraintActor1` to it and deleting the old Actor. Saving and
reopening preserved both new Actors, the transferred reference and material; the
unrelated Actor's native identity and properties were unchanged. Imports had no
readback warnings. The fixture was deleted and GreyCanal restored unchanged.
This did not exercise new Actor attachments, component-reference transfers,
Blueprint reconstruction, cross-map/Sequence bindings, runtime behavior or visual
quality. No PIE was started. Reversible static retirement retains the preceding
stage-management section's separately verified scope.

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
