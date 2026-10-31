# T59 World command authority

T59 keeps one typed World mutation active for procedural whitebox authoring:

```python
client.world.wall_create_with_opening(...)
```

The nine typed persistent World mutations for Actor HLOD/streaming policy, Data
Layer structure/state, level GameMode, streaming relations and World Partition
streaming are dormant compatibility identities. Their desired state belongs to
World HJSON; incomplete profile/adapter coverage remains an explicit capability
gap and does not justify exposing the old typed commands in ordinary discovery.
Level HJSON covers legacy streaming associations, explicit unlink, cross-Level
Actor migration, Editor visibility, transforms and initial-state save/reload.
Use the exported `level_world` and Actor `level` fields described in [T26](t26_level_world_domain.md).
World Partition streaming enablement uses the native setter in that same World
state; HLOD defaults and Actor policy use exported reflected properties. DataLayerAsset
create/update uses the Reflection route; existing WP maps expose keyed
`level_world.data_layers` instance configuration and Actor `DataLayerAssets`
membership. The `data-layer-editor-state` session covers temporary Editor
unload/visibility and close restores the prior flags. These are not runtime
activation/unload tests, nor support for private/external layers or hierarchy editing.
Dormant exact handlers remain executable
for compatibility; they do not establish current HJSON coverage.

Level GameMode is covered by the native `AWorldSettings` properties in the Level
workspace's World target properties (`GameMode.DefaultGameMode`). Other editable world
settings use the same property path; export the current map and edit its declared
typed values. This does not reactivate the dormant typed mutation identities.

`world.actor.create` is also dormant and has no generated named SDK method. New persistent Actor creation uses
`world.actor.candidates` followed by a Level Actor HJSON create through
`content_graph.import_workspace`. Its provider extension carries the selected
candidate plus optional label, folder, transform, attachment and non-reserved
Actor tags; properties and components remain ordinary HJSON units.

Discover an unknown operation with `client.query.command_search(intent)`, then call
`client.query.command_usage(names)` for the minimum named SDK call. Use the generated SDK method for that command;
discovery never executes a command.

## HLOD Layer HJSON

HLOD Layer assets use the common Reflection semantic workspace. Export the real asset, edit only
the ordinary HJSON returned by that workspace, and import it through the workspace handle:

```python
workspace = client.content_graph.export_workspace(
    "/Game/World/HLOD/HLOD_Instancing.HLOD_Instancing",
    name="hlod_edit",
    profile_id="llm_authoring",
)
result = workspace.import_changes()
```

The workspace exposes editable `UHLODLayer` root properties and editable descendants of the existing
`HLODBuilderSettings` object. Its pointer is read-only: an import cannot clear it, replace its class,
or bind an external object. Native `LayerType`/`HLODBuilderClass` notifications derive the settings
object before its descendant edits are applied. Read the refreshed workspace after a type change for its editable
fields; a combined edit must use fields valid on the resulting native settings class. An explicit
`class_path` is an assertion, not permission to replace the read-only pointer. Empty
`owner_relative_path` cannot request a new settings object.

To create an absent HLOD Layer, import an ordinary initialization document through the same
`content_graph.import_workspace` command. The SDK/service owns revision and authorization; do not
provide machine-token fields. The source union accepts
`inline`, `single_file`, or a domain document directory. The document uses the shared Reflection
operation/target/properties contract:

Use `client.content_graph.import_inline(target_object_path, document_text)` for inline creation.

```hjson
schema: uai.world_hlod_layer.edit/1
root: {
  type: /Script/Engine.HLODLayer
  document: {
    operation: create
    target: {
      asset_path: /Game/World/HLOD/HLOD_Instancing
      asset_kind: hlod_layer
    }
    properties: [
      { property_path: "LayerType", value: "Instancing" }
      { property_path: "CellSize", value: 512 }
    ]
  }
}
```

This replaces the former HLOD-only `layer_type`/`cell_size` value parser. The native factory creates
the root and its defaults; common Reflection owns preview, recursive properties, transaction,
save/reload, final readback and absent-target recovery. Existing assets use exported semantic
workspaces. HLOD build and execution remain independent World commands.

## Read-only World Partition and streaming state

```python
partition = client.world.partition(
    input={"include_loaded_regions": True, "include_actor_descriptors": True}, context={}, projection={}
)
health = client.world.partition_health(
    input={"enable_streaming": True}, context={}, projection={}
)
streaming = client.world.streaming_levels(input={}, context={}, projection={})
hlod = client.world.hlod_assignments(input={}, context={}, projection={})
```

`world.partition_health` calls the real World Partition error checker and returns
`health_status`, `error_count` and issue entries. These four commands are Query operations: they do
not create jobs, save packages or claim a lifecycle terminal state. The optional
`include_actor_descriptors` flag returns Actor object paths, external package paths,
labels, classes, actual loaded state, spatial policy, grid, HLOD Layer and Data Layer
references without loading those Actors. Defaults are unchanged. `world.data_layers`
Actor membership lists concern loaded Actor objects; use descriptors when inspecting
membership of unloaded Actors.

## Level sessions and World Partition loaders

Create a blank persistent map with a recoverable session:

```python
start = client.editor.session(
    "world_context",
    "world:/Game/Maps/LV_Test",
    "policy:world-context:create-blank/v1",
    {
        "overwrite_policy": "fail",
        "save_existing_map": False,
        "create_world_partition": True,
    },
)
handle = start.operation
status = handle.resume()
```

Open an existing map with `policy:world-context:set-current/v1`. If it is already
the current Editor World, the policy reuses that World; success does not prove a
reload. A different target switches and loads the map. Region and actor loaders use
`policy:world-context:partition-region-loader/v1` and
`policy:world-context:partition-actor-loader/v1`. A loader remains owned by its typed SDK handle;
observe it with `handle.status()` and unload/drain it with `handle.close()`.
There is no domain loader registry or second loader
ID source.

For a real region loader, wait for the native typed signal's `active` phase:

```python
ready = handle.wait(
    timeout=30,
    until=lambda observation: observation.payload.get("latest_signal", {})
        .get("payload", {}).get("phase") == "active",
)
ready.raise_for_error()
# Inspect the loaded content while retaining the handle.
closed = handle.close()
closed.raise_for_error()
```

The outer `running` phase only means work is in progress. The `world.partition`
`loaded_region_count` and `loaded_regions` fields describe user-loaded Editor
regions, not all operation-owned loaders. Check the loader's typed readiness and
content, then its terminal `cleanup_complete` receipt. Workspace export can also
load Actor descriptors temporarily for capture; that is separate from a retained
region loader and from runtime streaming.

For an existing ordinary DataLayerAsset instance in the current WP map, use
`policy:world-context:data-layer-editor-state/v1` with `asset_path` (exact asset
object path) and at least one of `loaded_in_editor` or `visible` (booleans).
Wait for `active`, retain the handle while inspecting, then `close()` to restore
the previous flags and refresh native loaders/visibility. This session does not
save user loading preferences or change `initial_runtime_state`/`initially_visible`.
Close it before switching maps or independently changing the same layer. Region
loading and Data Layer eligibility jointly determine whether an Actor is loaded;
restoring a layer alone does not promise to load every Actor in that layer.

## Convert a saved ordinary Level to World Partition

```python
start = client.job.compile_build(
    "world_build", "world:/Game/Maps/LV_Source",
    "policy:world-build:partition-convert/v1",
    {"enable_streaming": True, "report_only": False},
)
receipt = start.operation.finish(timeout=600)
receipt.raise_for_error()
# Inspect the native report, then open /Game/Maps/LV_Source_WP with set-current.
```

The owned commandlet subclasses UE's `WorldPartitionConvertCommandlet` and invokes
its native conversion with `ConversionSuffix`; it never enables source deletion.
The existing source remains available and the destination is `<source>_WP`.
`enable_streaming` defaults to true and `report_only` defaults to false. Conversion
does not switch the current Editor World. Save source content before starting;
the commandlet reads packages from disk. A nonzero exit or cancelled job is not
atomic rollback: inspect its native log and any task-owned partial output before retrying.

This route supports the native default conversion configuration. It rejects
already-partitioned sources, existing destination maps/external-package directories,
its scoped output asset folder, collisions with the source-prefixed native default
HLOD Layer outputs, and custom conversion `.ini`/class-to-HLOD mappings. It does not
provide in-place conversion, arbitrary custom INI, `OnlyMergeSubLevels` (OFPA alone),
or `GenerateIni`. Retained sublevel outputs also receive the native suffix. Data Layer
and foliage conversion assets are restricted to the destination's `_Assets` folder.
`report_only` is native planning and does not prove an output map exists.

Verify an actual destination by opening it, querying `world.partition`, inspecting
external Actor descriptors, and saving/reopening needed edits. A separate blank-WP
creation success or Enable Streaming toggle does not establish this conversion chain.
See [Epic UE 5.6 World Partition](https://dev.epicgames.com/documentation/en-us/unreal-engine/world-partition-in-unreal-engine?application_version=5.6).

## HLOD, navigation and partition jobs

```python
start = client.job.compile_build(
    "world_build",
    "world:/Game/Maps/LV_Test",
    "policy:world-build:hlod-plan/v1",
    {"step": "build"},
)
receipt = start.operation.finish()
```

HLOD execute uses `policy:world-build:hlod-run/v1`; accepted steps are `setup`, `build`,
`finalize`, `delete` and `stats`. The run policy starts the owned commandlet;
`delete` additionally requires `allow_delete=true`. Build and finalize enable the
renderer; the other steps use NullRHI. Navigation uses
`policy:world-build:navigation/v1`. World Partition streaming generation uses
`policy:world-build:partition-streaming-plan/v1` and its run peer. Exact Actor-GUID resave uses
`policy:world-partition-resave:actors-plan/v1` and
`policy:world-partition-resave:actors-run/v1`. Plan returns a durable report without executing; run uses one owned,
unattended `UnrealEditor-Cmd` process and exposes its report and process return code through the
common operation lifecycle.

Materialize the terminal receipt's `primary_artifact` to inspect the native
commandlet report/log. A successful process and Layer assignments alone do not
describe generated content: reload the target map and inspect its generated HLOD
Actors/components through the same Content Graph readback. `world.hlod_assignments`
only reports Actor-to-Layer references. Instancing HLOD uses instanced components;
it does not require a newly merged mesh asset.

UE 5.6 RuntimeHashSet validates a spatial Actor's HLOD Layer against the selected
runtime partition's `HLODSetups[].HLODLayers`. A new Layer asset plus an Actor or
default-Layer reference does not register that Layer in a runtime partition. Use
a Layer already configured by the map's native setup, or configure the runtime
partition separately before generation. The current Level authoring additions
do not create/rebuild RuntimeHashSet partition descriptors. An `invalid HLOD layer`
native diagnostic and zero generated Actors are not successful HLOD content,
even when the setup process exits successfully. Inspect the native setup report
before spending time on a rendered build.

## Completion semantics

A successful start is not success. Use `handle.finish()` for finite work and
`handle.wait(until=...)` for persistent readiness. Mutation success is emitted only after required validation,
real UE mechanics, persistence and independent readback. Wall geometry keeps
`semantic_frame_id`, write/read/verify frames, units, basis evidence and conversion chain explicit.
Prewrite failure leaves no residue, unknown post-write state is reconciled, and cleanup is bounded.
