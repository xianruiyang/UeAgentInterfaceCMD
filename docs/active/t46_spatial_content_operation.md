# Spatial-content commands through the default SDK

Use `client.query.command_search(...)` and
`client.query.command_detail(...)` to discover the current contract, then call
one of the six normal methods:

```python
client.mesh.element_select_by_ray(...)
client.mesh.pivot_update(...)
client.mesh.transform_bake(...)
client.reference.origin_resolve(...)
client.world.object_align(...)
client.world.object_snap_to_surface(...)
```

Each method forwards one exact manifest request. The equivalent CLI entry is
`uai-cli ... exec <command-id>`. There is no task-specific generated SDK module
or historical alias.

`world.object_transform.read` and `world.object_transform.update` are dormant.
Read persisted Actor/Component transforms through `content_graph.structure` or
`content_graph.items`; edit a `uai.world.edit/1` document and apply it through
`content_graph.import_workspace`. A StaticMesh content-graph read and a selected
World HJSON `ADynamicMeshActor` item expose the Modeling carrier revisions needed
by specialized mesh operations. This does not claim a PIE/runtime query surface.

Normal command search and generated named SDK methods hide both dormant IDs.
Development-only compatibility discovery uses
`client.query.command_search(intent, mode="compatibility")`; it returns the
active successors and `requires_user_confirmation=true`. Only when those active
HJSON successors cannot satisfy the authorized task, and after the user agrees,
may development code use `client.execute_dormant(..., user_confirmed=True)` or
the CLI `--allow-dormant` form. The original exact server handlers remain the
only compatibility implementation.

`world.object_align` supports anchor, bounds, face and vertex alignment;
`world.object_snap_to_surface` performs bounded Editor-world ray placement.
`expected_revisions` is optional for these two specialized operations: supplied
revisions are validated, while omission freezes current revisions at invocation.
Both still verify their result independently. Use World HJSON for an additional
persisted-state readback.

`mesh.element.select_by_ray` consumes an explicitly activated Modeling Tools
Editor Mode selection target. `mesh.transform.bake` and `mesh.pivot.update` are
durable geometry operations and obtain their carrier revision from a
content-graph read. `reference.origin.resolve` remains the read-only origin
resolver for catalog, JSON, UE object, graph-node and name references.

Invalid identities, frames, geometry, surfaces or stale supplied revisions fail
before mutation. Cleanup restores only owned transient state and preserves the
user's Editor. Spatial values retain `frame_id`, `basis_frame_id`, `dimension`,
`unit`, `basis_evidence_id`, and `observed_at`; the SDK does not infer or convert
these fields.
