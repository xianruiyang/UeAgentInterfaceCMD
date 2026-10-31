# Viewport and graph control through the default SDK

The default SDK exposes these named methods:

```python
client.graph.view_read(...)
client.graph.view_update(...)
client.viewport.actor_pick(...)
client.viewport.actor_select(...)
client.viewport.camera_frame(...)
client.viewport.instance_list(...)
client.viewport.pixel_scale_read(...)
client.viewport.ray_deproject(...)
client.viewport.ray_trace(...)
client.viewport.state_read(...)
client.viewport.state_restore(...)
client.viewport.state_update(...)
client.viewport.view_mode_list(...)
client.viewport.warning_list(...)
```

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
Each named method forwards one catalog-bound request and contains no UE
business logic, retry loop, alias mapping, or transport fallback.

For a minimized zero-size Editor viewport, `ray_deproject` and `ray_trace` accept
`input.cold_start_render_size={"width":1280,"height":720}`. Use the actual capture
receipt's dimensions for image coordinates. The explicit dimensions apply only
when native extent is zero; the temporary fixed-size policy is restored before
return and the window remains untouched. Omit the option to retain normal
zero-size failure semantics. Each dimension is an integer from 1 to 4096.

Discover a viewport, retain its exact identity, and read its transient state:

```python
catalog = client.viewport.instance_list(
    input={},
    context={"world_type": "editor"},
    projection={"include_provenance": True},
)
viewport = "level:0"  # choose the readable viewport_ref returned by the catalog
context = {"world_type": "editor", "viewport": viewport}
before = client.viewport.state_read(
    viewport,
    input={},
    context=context,
    projection={"include_provenance": True},
)
```

`before.payload` is the complete restoration snapshot: readable `viewport_ref`,
nested `camera` and `interaction`, realtime preference/effective state, Game
View and show flags. Keep this payload, perform the transient operation, then
restore it directly; no canonical-entry reconstruction is needed:

```python
before.raise_for_error()
snapshot = before.payload
restored = client.viewport.state_restore(
    viewport, input={"snapshot": snapshot}, context=context,
)
after = client.viewport.state_read(viewport, input={}, context=context)
```

Inspect the restore result and compare the new readback. The server freezes and
rechecks the live viewport revision inside the restore operation; callers do
not copy or submit it. Do not infer a viewport or reuse a snapshot from another
viewport.

`camera.view_mode` and `view_mode_list`'s `active_mode_id` use the same canonical
ID. Accepted aliases may read back with a different spelling; the server verifies
their native meaning. Preserve a returned family mode ID during restoration,
including an unset `family_none` selector (`buffer_overview` for Buffer).

`viewport.actor_select` accepts either explicit `actor_refs[]` or a
`screen_point` plus bounded `trace_query`, never both. `selection_mode` is
`replace`, `add`, or `remove`. `viewport.camera_frame` likewise accepts exactly
one of `subject_refs[]`, `folder_path`, `use_current_selection=true`,
`world_point`, or `world_bounds={min,max}`. A subject may be an Actor or bounded
primitive component; point and bounds values use `unreal.world`. Its
`frame_policy` declares padding, distance bounds, rotation, collision-aware,
look-at, and fallback behavior. `viewport.actor_pick` uses `allow_no_hit=true`
when an empty hit is a valid observation. Spatial inputs use the same compact
value returned by public reads: `quantity`, `frame_id`, `dimension`, `unit`, and
numeric `components`. Preserve the frame and unit when changing components.
The service binds the actual target/context and owns conversion evidence;
callers do not manufacture subject identities, basis evidence, or timestamps.

Put viewport changes inside `input.state_patch`. When it carries
`camera_transform`, set `camera_transform_mode` inside that same patch explicitly:

```python
client.viewport.state_update(
    viewport,
    input={"state_patch": {
        "camera_transform": camera_transform,
        "camera_transform_mode": "absolute",
    }},
    context=context,
)
```

Realtime readback distinguishes `realtime_configured` (preference), `realtime`
(sustained effective state) and `realtime_override_reason`. Update/restore keeps
native Editor overrides. A conflicting override returns partial/mismatch with
`world_spatial_viewport_realtime_overridden`. The warning includes the active
override reason and the field's `property_path`, `expected_value`, and
`actual_value`; use these facts instead of retrying the write. Other viewport
differences remain independent diagnostics, nested under `diagnostics` when
more than one field differs. Full diagnostics are in `warnings`; the compact
verification projection retains its summary and existing partial/mismatch and
retry-safe semantics. Background throttling is removed when Editor regains focus; UAI does
not change global performance settings or force a temporary success override.

Use `absolute` with `unreal.world` to set
the complete camera pose. Use `delta` with either `unreal.world` or
`viewport.camera.local`; a local translation follows the current camera axes.
Viewport cameras do not expose scale, so the transform scale must remain
`[1,1,1]`. Preserve the prior snapshot and use `viewport.state_restore` for the
restore rather than constructing a reverse delta.

A transform's ten components are translation XYZ, quaternion XYZW, and scale
XYZ. A restoration snapshot contains `viewport_ref`, `camera` (compact
`camera_transform`, `fov_degrees`, `view_mode`), `realtime`, `game_view`,
`show_flags`, and `interaction`. Camera observation metadata is not required.
Retain `realtime_configured` in the complete readback payload. Restore prefers
it over effective `realtime`; legacy snapshots without
it still use `realtime`.

`show_flags` accepts only the enum exposed by describe (currently `Lighting`
and `StaticMeshes`). The array replaces enabled flags within that subset;
omitted members are disabled, while other engine flags are unchanged. Both
update and restore validate all supplied state before changing the viewport.
Pass the complete `state_read.payload` as the restoration snapshot so that
configured preferences are preserved alongside effective state.

For a graph, first open or otherwise own a real graph editor, then use the
readable `UEdGraph` path as target and `asset_editor`:

```python
graph_context = {
    "world_type": "editor",
    "asset_editor": graph_path,
}
before = client.graph.view_read(
    graph_path,
    input={},
    context=graph_context,
    projection={"include_provenance": True},
)
```

Read `graph_view.location` and `graph_view.zoom` from the snapshot. Pass those
business values to `graph.view_update`; use a `graph.editor.view.local` point
with `graph_unit` components. The server freezes the live graph revision during
preflight and rejects a change before the editor view mutates. Reapply the
captured location and zoom to restore the original view, then read again. This
command changes only the current editor view; persisted node layout belongs
exclusively to `graph.layout.apply`.

The CLI forwards the same request through the same client and protocol:

```text
ueagentinterfacecmd exec graph.view.read  --params-json <json-object>
ueagentinterfacecmd exec viewport.state.update  --params-json <json-object>
```

Invalid or stale inputs fail before mutation. Cleanup restores only owned
transient changes, releases any UAI realtime override, destroys test fixtures,
and preserves the user's Editor.
