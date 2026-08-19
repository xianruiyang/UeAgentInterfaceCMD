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
Use
`client.blueprint.component_candidates(...)` for exact component candidates,
`client.content_graph.diagnostics(...)` for the current target diagnostics, and
the remaining `client.content_graph.*` methods for revision, structure, export,
and independent readback. Use `client.command_search(...)` and
`client.command_detail(...)` when the method or live contract is not already
known; `uai-cli` exposes the same discovery path. This tutorial does not retain
the old task helper or its misleading `world_actor_candidates` alias.

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
