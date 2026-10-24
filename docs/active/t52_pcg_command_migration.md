# PCG commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
client.pcg.data_asset_create_from_level(...)
client.pcg.generated_spatial_data_read(...)
client.pcg.node_candidates(...)
client.pcg.partition_spatial_state_read(...)
```

The exact CLI uses ueagentinterfacecmd with the current command name and one
JSON parameter object. No task-specific generated projection remains.

`node_candidates` searches the target graph's native background context menu.
Its compact `name` or `id` selects what the native action creates; graph,
semantic identity, and placement remain in the owning HJSON edit submitted via
`content_graph.import_workspace`. Graph topology and graph-parameter apply are
internal HJSON operation kinds, not separate public SDK commands.

Selector properties use native text values such as `"$Position"`, `"@Last"`
and `"@Source"`, including within arrays and nested properties. Keep the exported
type and edit its value; see the [PCG property contract](../../../Plugins/UeAgentInterface/docs/active/t52_pcg_command_migration.md).

To edit PCGDataAsset content, export an ordinary workspace and edit its
`data` value (`source`, `sets`, and point `settings`), then import and independently
export the result:

```python
workspace = client.content_graph.export_workspace(target, name="pcg-data", profile_id="llm_authoring")
# Edit the ordinary properties.hjson under workspace.path.
result = workspace.import_changes()
```

Keep exported `instance` bindings for surviving sets and points; omit `instance`
for new items, remove rows to delete, and use `sets: []` to clear the collection.
Point settings retain the exported categories and `type/value` shape. Supported
point storage types are `point` and `point_array`; native metadata is preserved.
`pcg.data_asset.apply` is dormant and has no named SDK method.

For current spatial reads, `target` is an exact loaded world, level, actor or PCG
component. An explicit `input.actor` or `input.component` selects one object within
that scope by native name, actor label, scoped discovery name or exact object path.
Ambiguous names return the matching paths. Omit selectors to read the complete
collection; an unfiltered scope without PCG components is valid and empty.
`data_asset_create_from_level` remains the separate native conversion operation.
Its destination `target_ref` is a package path, such as `/Game/PCG/Points`, while
`source_level_ref` is a World object path, such as `/Game/Maps/Source.Source`:

```python
client.pcg.data_asset_create_from_level(
    "/Script/PCG.PCGPointData", "/Game/Maps/Source.Source", "/Game/PCG/Points")
```

After creation, ordinary asset operations and workspace export address the
result by its object path, `/Game/PCG/Points.Points`.

PCG components are edited in the Level workspace. Their `pcg` state exposes
`graph`, the shared `parameters` property bag, and an `overrides` array of
parameter names. Enable a name to use the local parameter value; remove it to
restore inheritance. Edit `GenerationTrigger` in the same component's ordinary
properties. The component/world-binding/graph-instance apply identities are
dormant and are not named SDK methods.
Changing the graph while leaving exported parameter values unchanged inherits
the new parent values. Clearing `graph` clears its dependent parameter schema
and overrides through native SetGraph.

Explicit generation uses `client.editor.session("pcg_generation",
"pcg-component:" + component_path, "policy:pcg-generation:generate/v1", {})`,
where `component_path` is the exact loaded current-world PCG component returned
by the spatial reads. Check the start result and call `started.operation.finish()`.
This finite native operation generates unchanged inputs too, reports this task's
`generation_started` and `generation_completed`, and preserves successful output
after release. Cancellation stops only its own task and does not roll back
partial effects. Save affected map/resources separately through the public Editor
save entry. Recovery uses the common Operation handle. See
[explicit Editor generation](../../../Plugins/UeAgentInterface/docs/active/t52_pcg_command_migration.md#explicit-editor-generation)
for scope and lifecycle.

Cleanup deliberately leaves the component ungenerated; ordinary Level imports
preserve UE's automatic-refresh eligibility. Use explicit generation to resume
after Cleanup; reopening the map with `GenerateOnLoad` is not equivalent.

Current generated-data and partition reads retain the same SDK
signatures and accept `input={}`, `context={}` for an exact loaded world, level,
actor or PCG component. They read the component's actual graph output and
native subsystem partition mapping; no generation identity, DataAsset fixture,
generation call or Python business implementation is needed.
Use `input={"max_points_per_data": 0}` for counts only, or explicit readable
`actor`/`component` selectors. An empty graph output does not prove that no mesh
was generated. The component statuses, point-local bounds, native coordinates,
partition scope and result shape are defined by the
[PCG command owner](../../../Plugins/UeAgentInterface/docs/active/t52_pcg_command_migration.md#current-native-generation-observations).

Persistent writes require native generate/settle where declared, terminal
projection, and independent persisted readback after reload. Explicit generation
above changes Editor memory and does not save. Invalid graph,
binding, source, bounds, frame, parameter, or stale revision fails before
mutation. Unknown state requires reconciliation. Cleanup removes only owned PCG
fixtures and generated state, then independently verifies absence.

Cleanup includes registered partition locals and nested managed resources.
It saves/deletes the affected native packages through the common durable runner;
failure recovery uses a memory package checkpoint and restores the original disk
versions and dirty flags. Check `terminal_state` and diagnostics: an unconfirmed
restore remains `state_unknown`. See the plugin contract's
[persistent cleanup](../../../Plugins/UeAgentInterface/docs/active/t52_pcg_command_migration.md#persistent-cleanup)
for the exact scope.
