# Spatial-content commands through the default SDK

When a command is unknown, use `client.query.command_search(...)`, then
`client.query.command_usage([...])` for selected exact IDs. Use
`ueagentinterfacecmd describe <command-id>` for public parameter shapes when needed.
The five normal methods are:

```python
client.mesh.element_select_by_ray(...)
client.mesh.transform_bake(...)
client.reference.origin_resolve(...)
client.world.object_align(...)
client.world.object_snap_to_surface(...)
```

Each method forwards one exact manifest request. The equivalent CLI entry is
`ueagentinterfacecmd ... exec <command-name>`. There is no task-specific generated SDK module
or historical alias.

`world.object_transform.read` and `world.object_transform.update` are dormant.
Read persisted Actor/Component transforms through `content_graph.structure` or
`content_graph.items`. Export the Level with `client.content_graph.export_workspace(...)`,
edit the selected transform's declared HJSON fields and apply with `workspace.import_changes()`.
Use a readable StaticMesh or `ADynamicMeshActor` target for specialized mesh operations;
revision custody stays inside the service. This does not claim a PIE/runtime query surface.

Normal command search and generated named SDK methods hide both dormant IDs.
Development-only compatibility discovery uses
`client.execute("query.command.search", {"intent": intent, "mode": "compatibility"})`.
If active HJSON cannot satisfy an authorized task, explain the gap and obtain
explicit user agreement before using a returned guarded dormant ID through
ordinary `client.execute` or `ueagentinterfacecmd exec`.
The original exact server handlers remain the only compatibility implementation
and use the ordinary exact dispatch path.

`world.object_align` supports anchor, bounds, face and vertex alignment;
`world.object_snap_to_surface` performs bounded Editor-world ray placement.
The server resolves every subject and freezes its current state at invocation;
reference-based alignment includes the reference object. It rechecks the whole
set before any write, and surface snap repeats its trace at the write boundary.
Callers never submit revisions. Both commands still verify their result
independently. Use World HJSON for an additional persisted-state readback.

`mesh.element.select_by_ray` consumes an explicitly activated Modeling Tools
Editor Mode selection target. `mesh.transform.bake` is a durable geometry
operation and obtains its carrier revision from a content-graph read. Persisted
pivot desired state uses HJSON and `mesh.pivot.update` is dormant.
`reference.origin.resolve` remains the read-only origin
resolver for catalog, JSON, UE object, graph-node and name references.

Invalid identities, frames, geometry or surfaces fail before mutation. Native
failures confirmed before any target write return `mutation_started=false` and
`retry_safe=true`, preserving the original diagnostic. Once a native write may
have occurred, later failures retain conservative mutation and recovery status;
an earlier successful item or patch field must not be forgotten. The
service captures and checks live revisions. Cleanup restores only owned
transient state and preserves the user's Editor. Spatial values use the compact
public shape: `quantity`, `frame_id`, `dimension`, `unit`, and `components`.
Frame-only inputs contain `frame_id`, `dimension`, and `unit`. Preserve the
coordinate frame and units; the server binds actual targets and performs the
supported native conversion. Observation timestamps and conversion evidence
are service-owned and are not invented by callers. Existing complete values
remain accepted for compatibility.
