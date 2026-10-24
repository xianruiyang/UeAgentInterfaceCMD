# T37 Asset Operations SDK and CLI

Import only `uai` and use `uai.connect_project()` for the local project. Search the
live constructor catalog and pass the returned readable factory name (and only
when needed, up to two short semantic `select` fields) to the generated create
method. The named methods are `asset.factory.candidates` and `asset.object.create`:

```python
import uai

with uai.connect_project() as client:
    candidates = client.asset.factory_candidates(
        "asset.object.create",
        query="Sound Class",
    )
    sound_class = client.asset.object_create(
        candidates.payload["names"][0],
        "/Game/StrictV2/T37/SC_Default.SC_Default",
    )
```

The string is a name shorthand; the same method also accepts
`{"name": name, "select": selection}`. When creation returns
`candidate_ambiguous`, use its public `error.choose` to select the required
creation semantics and retry with that name and returned selection. Invalid or
stale selections reject before writing and return current choices. Do not
invent a class path or infer a preferred constructor from the query order.

`target_ref` accepts `/Game/Folder/Asset` or `/Game/Folder/Asset.Asset`; both name
the same top-level asset. Create/update uses the resolved object path for identity
and readback. Invalid references identify `/target_ref` in
`error.diagnostic.json_pointer` with a readable correction. A mismatched object
suffix is rejected; an existing creation target is never overwritten.

The generic form uses the same generated binding:

```python
result = client.execute(
    "asset.object.create",
    {
        "factory": {"name": "Sound Class"},
        "target_ref": "/Game/StrictV2/T37/SC_Default.SC_Default",
    },
)
```

The CLI forwards one identical request:

```text
ueagentinterfacecmd exec asset.object.create --params-json '{"factory":{"name":"Sound Class"},"target_ref":"/Game/StrictV2/T37/SC_Default.SC_Default"}'
```

Use `client.query.command_search("asset object create")` and then
`client.query.command_usage(names)` to obtain the minimum named SDK call. Execute
the generated SDK method for that command; command identity and transport metadata remain internal.

The client contains no HTTP implementation, retry, alias, registry fallback,
parameter remapping, persistence, rollback, or Unreal Engine business behavior.
Inspect `Result.ok` and its verified business projection; machine operation and
verification identities stay in SDK custody. `state_unknown` is never safe for
automatic replay.

For File Media Source, discover the returned factory name and create through
`asset.object_create`. Export a normal workspace, edit the `value` of `FilePath`
(string) and `PrecacheFile` (boolean), call `workspace.import_changes()`, then
read the refreshed values. Use a native file path, not a `file://` URI from the dormant
typed update contract. HJSON preserves the authored absolute or relative path;
it does not promise setter normalization or media playback validation.

For Media Texture, export an ordinary workspace and edit the exported
`MediaPlayer` reference together with texture settings such as `AutoClear`,
`ClearColor`, and `AddressX`. Keep the exported enum and color shapes. Import
with the workspace handle, then inspect the refreshed values.
The server retains native texture notifications and media-clock resource
updates; no typed update or client-side player-binding helper is needed. This
edits asset configuration and does not open media, validate playback, or restore
a transient decoded frame after failure.
`ClearColor` is an RGBA array. New assets normally enable `NewStyleOutput`;
edit that exported boolean only when the external-texture output mode is
intended, rather than treating a missing external registry entry as a failure
of the default regular texture mode.

For Paper Flipbook, edit `FramesPerSecond` and `KeyFrames` in the same ordinary
workspace. Use the array's exported element template for new entries, supplying
a Sprite asset reference and its positive `FrameRun` duration in frames.
Existing entries can be reordered or edited; `[]` clears the keyframes.
Import through the workspace handle and read the refreshed HJSON.
The server handles native component refresh, persistence, and checkpoint
recovery. Sprite references remain external assets; Sprite and TileSet editing
use the separate workspace surfaces below. TileMap is deferred, and the dormant
typed `frames` shape is not a workspace input.

For a Paper Sprite, edit the exported
`SourceTexture`, `SourceUV`, `SourceDimension`, `PivotMode`, and
`CustomPivotPoint` rows in the ordinary workspace, then import and read the
refreshed values. Region and pivot coordinates use source-texture pixels;
`PixelsPerUnrealUnit` controls their physical scale. Keep the exported vector
and enum shapes. Native notifications rebuild geometry/collision, and the
server refreshes actual components after save/reload or checkpoint recovery.
Do not use the dormant typed `asset.paper_sprite.update` payload.

Set the exported `AtlasGroup` to an Atlas reference, or `null` to detach. Old and
new memberships are saved and reloaded together. Create an Atlas with the public
`Paper Sprite Atlas` candidate and edit its ordinary root settings; no dedicated
Atlas command or project menu-setting change is required. This requires the
server's UE5.6 Paper2D patch for native notifications, reload/cache restoration and
unattended optional-repack handling. Generated pages, packing slots and
`BodySetup` remain derived data. Sprite rendering/collision notifications still run.

For Paper TileSet, edit the exported `TileSheet`, `TileSize`, `BorderMargin`,
`PerTileSpacing`, `DrawingOffset`, `PerTileData`, and `Terrains` rows, then import
and read the refreshed values. The public factory candidate is `Paper Tile Set`.
Keep `TileSize` in its exported struct shape, such as
`value: { fields: { X: 16, Y: 16 } }`, rather than replacing it with an array.
Layout uses source-texture pixels from the top
left, X right and Y down; tile indices run across each row before the next row.
Use the public terrain element template for `TerrainName` and the zero-based
`CenterTileIndex`. Entries can be edited/reordered, and `[]` clears terrains.
Metadata has one entry per tile in the resulting grid; omitted metadata follows
the native overlap-copy by grid coordinate when layout changes. Keep the public
struct shapes, including their supplied defaults. Terrain corner memberships
and a terrain solver are not exposed. The server performs native cache/component
refresh and persistence/recovery. Do not use the dormant typed
`asset.paper_tileset.update`; this does not add TileMap authoring.

For an existing Input Action, export a normal workspace, edit its exported root
property rows, call the workspace handle's `import_changes()`, and read the
refreshed values. For example, `ValueType` uses the readable enum value supplied by
the export. Invalid enum values reject before writing.

To create direct Player Mappable Key Settings from null, query
`client.asset.owned_candidates(target, {"property_path": "PlayerMappableKeySettings",
"query": "Player Mappable Key Settings"})` and use the returned name in the
ordinary property row:

```hjson
value: {
  owned_object: {
    name: "Player Mappable Key Settings"
    properties: {
      Settings: { DisplayName: { type: "text", value: "Player Mapping" } }
    }
  }
}
```

Use a returned `select` only when selection requests it. Import with the workspace
handle and read the persistent owned value in the refreshed workspace.

The same query accepts `property_path: "Triggers"` or `"Modifiers"` for Input
Action arrays. Append `{owned_object: {name: <returned name>, properties: ...}}`
to the ordinary array value, retaining the exported existing items. For a Hold
trigger, `Trigger Settings.HoldTimeThreshold` is a float property; for a Dead
Zone modifier, `Settings.LowerThreshold` is a float property. Use the actual
returned names and exported property types. Editing an existing item's fields
preserves its exported identity and array position. Candidate selection and
successful persistence do not establish runtime input behavior or validity of
arbitrary trigger combinations.

Input Mapping Context also uses the normal workspace. Edit the exported `Mappings`
array: retain an existing entry's `instance` beside its `fields` when moving or
editing it, omit `instance` for a new entry, remove an entry to delete that mapping,
or use an empty array to clear mappings. Keys are local to that export and must not
be copied from another workspace. For a mapping that already exists in the asset,
query `client.asset.owned_candidates(target, {"property_path": "Mappings[0].Triggers",
"query": "Hold"})`, refining the query if needed, and use the returned name unchanged.
`Mappings[0].Modifiers` follows the same contextual query contract. The index is
zero-based; querying does not create a mapping. Preserve exported Action reference
and nested property shapes. Import with `workspace.import_changes()` and inspect
order, values and nested owned content in the refreshed workspace.

For Sound Attenuation or Sound Concurrency, use the same export/import workspace
flow and the exported nested settings fields (`Attenuation` or `Concurrency`).
For example, edit `bAttenuate` as a boolean or `MaxCount` as a number, retaining
the other fields; import and inspect the saved settings in the refreshed workspace.
Factory discovery may return both factory and constructor choices; only use a
`select` returned by an ambiguity response. A factory that requires an interactive
dialog cannot be used by this non-interactive creation flow. These settings edits
do not establish live playback behavior.

For Sound Class, edit the exported `child_classes` array together with ordinary
root property rows in the same workspace. Each entry is a child asset reference;
the full array specifies the desired children. Removing an entry detaches it and
an empty array clears the list. Import also updates the child and any former
parent through the common transaction. A cycle is rejected before writing.
After import, inspect the child list and edited settings in the refreshed workspace.
Use ordinary asset creation first for a new Sound Class; this workflow validates
editing existing assets, not creation with an initial child relationship bundle.

For Sound Submix, edit `child_submixes` together with ordinary settings such as
`AutoDisableTime` and the ordered `SubmixEffectChain` reference array. The child
array specifies the desired children; removal detaches a child and an empty array
clears the list. Use existing Submix Effect Preset asset references for the effect
chain. Import updates affected parent/child assets through the common transaction;
cycles and incompatible effect references are rejected. Read the refreshed workspace
for the settings, children and effect order. This does not edit preset settings
or establish playback behavior. Deletion uses the ordinary `asset.delete` lifecycle
and its native device-state limits described in T31.

Sound Mix uses ordinary `SoundClassEffects` struct-array entries and root settings
such as `InitialDelay` in the same workspace. Preserve each entry's exported
`fields` shape and Sound Class reference; reorder or remove entries to change the
list, or clear it with `[]`. Import and inspect the saved adjusters and settings
in the refreshed workspace. These edits do not prove live playback or passive-mix
behavior. To add the first entry, find the array type in ordinary `definitions`,
copy its `value_definition.element_template`, and edit the fields described by
`element_definition`. Choose a real Sound Class asset for the reference field.
The same native default template remains available when the array is nonempty;
it is independent of existing entries and their edited values.

For an existing Specular Profile, export a workspace and edit the ordinary
`Settings.ViewColor` or `LightColor` curve. Use `workspace.import_changes()` and
an independent export for readback. RichCurve enums, key defaults and the
embedded/asset-reference alternatives are in the referenced centralized
RuntimeColor definition. RGBA channels carry independent extrapolation and
defaults. A conflicting root/channel extrapolation setting is rejected.
The `time` key coordinate represents the profile's NoV/NoL or VoH/NoH sampling
input, according to LUT Format, rather than seconds. The generic factory flow
creates the asset; ordinary HJSON then edits it.

For a standalone Curve Float, Curve Vector or Curve Linear Color asset, query its native factory name and create it
through the same factory flow. Export a workspace and edit the whole
`curve_float_profile_state.value`, `curve_vector_profile_state.value` or
`curve_linear_color_profile_state.value` row on its curve surface, then use
`workspace.import_changes()` and an independent export. Its
Vector `x/y/z` and Color `r/g/b/a` channels have independent keys, defaults and pre/post infinity
extrapolation; centralized RichCurve definitions supply enum choices and key
defaults. `time` is an input coordinate with units determined by the consumer.
This asset surface has no external-reference switch and is not a timeline.
Float uses the `value` channel with root-level pre/post infinity extrapolation.
Color's editable `Adjust*` root properties and RGBA curve can share one import.
The native Float event flag is preserved without exposing a new editable field.

For an existing Physical Material, export a workspace and edit the ordinary
`Friction` and `Restitution` numeric property values, then import and independently
export for readback. This edits asset settings; it does not run a physics simulation.

Data Objects use the same workspace flow. Ordinary editable DataAsset fields,
including inherited fields, do not require `UAIAssetDataField` registration.
The metadata may additionally authorize supported non-editable fields.
Values use the shared recursive codec for native values, structures, containers
and references. Owned descendants use their normal native member editability;
their members do not need the root registration metadata, even when an owned
object is itself a DataAsset. Edit the native property names present in the export
(for example `Title`), not the metadata ID from the former `registered_fields`
input. Dedicated asset domains retain their own native owner. Preserve exported reference shapes;
ordinary asset references accept an object-path string and retain their native class
constraint. Import and inspect the saved values in the refreshed workspace.

Texture Render Target 2D uses ordinary `SizeX`, `SizeY`, `RenderTargetFormat`,
`ClearColor` and `bAutoGenerateMips` property values in the same workspace import.
Use the exported enum definition and color shape; inspect the refreshed workspace
after import for the saved settings. Resource clearing occurs in UE's deferred
render phase. This edits the resource settings, not scene capture contents.
UE derives `SRGB` from the render-target format during property notifications;
the first edit of a newly created floating-point target can change it from its
constructor value of true to false. Do not treat it as an independent override.
Both final dimensions must be positive. Workspace import supports dimensions
above 2048 without a UAI confirmation threshold. UE 5.6 normalizes the dimensions
to pixel-format block alignment and a maximum of 16384; the refreshed workspace
contains that native result. Actual rendering-device constraints still
apply. Import preserves the native resource update, gamma and scene-capture
notifications; inspect the refreshed workspace after import for the saved dimensions.

Runtime Virtual Texture settings use the same ordinary workspace. `TileCount`
stores a base-2 exponent, not a pixel width: for example, 2 selects 4 tiles.
`TileSize` is also an exponent, offset by 6 (2 selects 256 pixels per tile).
Preserve the exported native property shapes and use the `MaterialType` enum
definition and `bCompressTextures` boolean. Import and inspect the saved settings
in the refreshed workspace. Actual producer dimensions also depend on the placing
component's volume and device-profile biases; asset settings alone do not prove
that pages contain rendered scene content.
