# Viewport and graph control through the default SDK

There are fourteen default named methods:

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

Find the command with `client.query.command_search(...)`, then call
`client.query.command_detail(command_id, contract_hash)` for the exact input,
context, projection schema, named SDK form, CLI form, and tutorial reference.
Each named method forwards one catalog-bound request and contains no UE
business logic, retry loop, alias mapping, or transport fallback.

Discover a viewport, retain its exact identity, and read its transient state:

```python
catalog = client.viewport.instance_list(
    input={},
    context={"world_type": "editor"},
    projection={"include_provenance": True, "max_items": 100},
)
viewport_id = "level:0"  # choose an identity returned by the catalog
context = {"world_type": "editor", "viewport_identity": viewport_id}
before = client.viewport.state_read(
    viewport_id,
    input={},
    context=context,
    projection={"include_provenance": True, "max_items": 100},
)
```

The compact Query result is a canonical snapshot under
`projection.payload.snapshot`. Index its `entries[]` by
`identity.object_role`. A viewport restoration snapshot is built only from the
returned `viewport_state.camera_transform`, FOV, view mode, realtime, Game
View, show flags, six interaction fields, and the three
`viewport_state.revision.*` fields. Keep that complete snapshot, perform the
transient operation, call `viewport.state_restore(snapshot=...)`, then perform
a new `viewport.state_read` and compare. Do not infer a viewport or reuse a
snapshot from another viewport.

`viewport.actor_select` accepts either explicit `actor_refs[]` or a
`screen_point` plus bounded `trace_query`, never both. `selection_mode` is
`replace`, `add`, or `remove`. `viewport.camera_frame` likewise accepts exactly
one of `subject_refs[]`, `folder_path`, or `use_current_selection=true`; its
`frame_policy` declares padding, distance bounds, rotation, collision-aware,
look-at, and fallback behavior. `viewport.actor_pick` uses `allow_no_hit=true`
when an empty hit is a valid observation. Pixel, ray, camera, and screen values
must retain the returned frame, unit, basis evidence, observation time, and
conversion evidence.

For a graph, first open or otherwise own a real graph editor, then use the exact
`UEdGraph` path as target and `asset_editor_identity`:

```python
graph_context = {
    "world_type": "editor",
    "asset_editor_identity": graph_path,
}
before = client.graph.view_read(
    graph_path,
    input={},
    context=graph_context,
    projection={"include_provenance": True, "max_items": 20},
)
```

Read `graph_view.location`, `graph_view.zoom`, and
`graph_view.revision.source_id/generation/sequence` from the snapshot. Pass the
exact revision in `view_state.graph_revision` to `graph.view_update`; use a
`graph.editor.view.local` point with `graph_unit` components. A stale revision
is rejected before the editor view changes. Reapply the captured location,
zoom, and revision to restore the original view, then read again. This command
changes only the current editor view; persisted node layout belongs exclusively
to `graph.layout.apply`.

The CLI forwards the same request through the same client and protocol:

```text
uai-cli --connection connection.toml exec graph.view.read --contract-hash sha256:<hash-from-command_detail> --params-json <json-object>
uai-cli --connection connection.toml exec viewport.state.update --contract-hash sha256:<hash-from-command_detail> --params-json <json-object>
```

Invalid or stale inputs fail before mutation. Cleanup restores only owned
transient changes, releases any UAI realtime override, destroys test fixtures,
and preserves the user's Editor. The nineteen old public IDs and their exact
successors are frozen in
`Plugins/UeAgentInterface/docs/active/successors/t45_viewport_graph_control.json`;
they are not callable aliases.
