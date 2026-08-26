# T26 Level/World SDK Projection

Use the default generated `client.content_graph.import_workspace(...)` method
for one `uai.world.edit/1` document. Pass one source union; for example:

```python
result = client.content_graph.import_workspace(
    "/Game/Maps/LV_Authoring.LV_Authoring",
    {"kind": "directory", "path": r"D:\\workspaces\\level_edit"},
    expected_revision,
    authorization_id="auth:level:edit",
)
```

The other supported carriers are `single_file` with `path` and `inline` with
`document`. A directory is one manifest-backed request: the shared loader
validates the complete declared file set, hashes, normalized paths, root and
symlink boundaries before the World provider runs. Do not loop over files and
do not use or invent `level_apply_folder` or another domain apply-file command.
Use `client.world.actor_candidates(...)` for the native Place Actors registry,
`client.blueprint.component_candidates(...)` for exact Blueprint Component
candidates, `client.content_graph.diagnostics(...)` for the current target
diagnostics, and the remaining `client.content_graph.*` methods for revision,
structure, export, and independent readback. Use
`client.query.command_search(...)` and `client.query.command_detail(...)` when the method or
live contract is not already known; `uai-cli` exposes the same discovery path.
There is no task helper, legacy `node_catalog_search`, or SDK-owned candidate
registry.

Search and create one native Actor as follows:

```python
page = client.world.actor_candidates(
    target="/Game/Maps/LV_Authoring.LV_Authoring",
    query="Cube",
    limit=10,
)
candidate = page.payload["candidates"][0]
```

Copy only `candidate["id"]` (or its unique `name`) into the Actor's
`candidate` object. Keep `managed_id`, transform, hierarchy and
placement context outside it:

```hjson
actors: [
  {
    managed_id: NativeCube
    operation: upsert
    candidate: { id: "candidate:..." }
    transform: {
      location: { x: 0, y: 0, z: 50 }
      rotation: { pitch: 0, yaw: 0, roll: 0 }
      scale: { x: 1, y: 1, z: 1 }
    }
  }
]
```

When the search used a category other than `AllClasses`, copy
`page.payload["context"]["placement_category"]` to the Actor's separate
`placement_context.category`. Optional returned class, asset and factory fields
may be supplied as assertions; they are not required selectors. The server
re-enumerates the same native context and submits the selected native item and
asset factory to UE's `UPlacementSubsystem`, the same owner used by current
editor placement.

The SDK contains no HTTP route, Unreal business rule, retry, parser, planner,
recursive initialization, Actor factory, component writer, Data Layer owner,
persistence, or cleanup implementation. Each generated method forwards exactly
one public command with the manifest contract hash.

Persistent graph layout is outside this provider; only the unified
`graph.layout.apply` owner defined by T62 may expose that operation.

Every document declares one three-dimensional space contract: semantic, write,
and read frames are `ue_world`, and unit is `centimeter`. Actor transforms are
World-space. SceneComponent transforms are parent-relative and carry an exact
parent component plus an optional socket. Actor hierarchy uses stable
`managed_id` references; component and Data Layer references remain exact.

T13 remains the sole common recursive initialization authority. T26 registers
only World root and owned/container Actor, Component, and Data Layer
initialization contracts and consumes the T13 seam. Obtain the current revision
from public readback, submit one document, and accept success only after World
and external Actor persistence plus independent readback. Unsupported frames,
units, types, roles, parents, or stale revisions fail before affected writes.
