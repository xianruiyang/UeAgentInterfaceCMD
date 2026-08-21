# Spatial-content commands through the default SDK

Use `client.command_search(...)` and `client.command_detail(...)` to discover
the current exact contract and hash, then call one of the eight normal methods:

```python
client.mesh.element_select_by_ray(...)
client.mesh.pivot_update(...)
client.mesh.transform_bake(...)
client.reference.origin_resolve(...)
client.world.object_align(...)
client.world.object_snap_to_surface(...)
client.world.object_transform_read(...)
client.world.transform_candidates_evaluate(...)
```

Each method forwards one manifest command. The equivalent CLI entry is
`uai-cli --connection connection.toml exec <command-id> --contract-hash
<hash-from-command_detail> --params-json <json-object>`. There is no
task-specific generated SDK projection and no historical alias.

For `client.world.object_align(...)`, put the exact actor or mesh identity in
`target`, the typed request in `input`, and the frozen world/frame identities in
`context`. `input.alignment.kind` is required:

- `anchors` uses explicit subject/reference 3D points;
- `bounds` uses `axis` plus `source_anchor`/`target_anchor`;
- `face` uses signed `source_face`/`target_face` and optional offset;
- `vertex` uses a complete index pair or a unique nearest world-vertex pair.

All spatial inputs preserve `semantic_frame_id`, dimension, unit, basis
evidence, observation time, conversion evidence, and the declared
write/read/verify frames. Supply current expected revisions for writes and use
`client.world.object_transform_read(...)` for independent readback.

`world.object_transform.read` accepts exactly an Actor or StaticMesh target. An
Actor returns its transform in the requested convertible frame. A StaticMesh
requires an identity `mesh.geometry.local`, three-dimensional, centimeter
verify frame and returns real mesh-description vertices plus any live component
placement observations. In both cases its returned revision comes from the same
WorldSpatial runtime/session as the mutation validator, so pass it unchanged as
that target's `expected_revision`. Other UObject types or non-local StaticMesh
frames fail before mutation. Successful durable mesh bake or pivot updates save
the asset package and remain observable after reload.

For `client.reference.origin_resolve(...)`, pass one `input.target` whose
required `source` is `catalog_candidate`, `json_reference`, `ue_object`,
`graph_node`, or `name_reference`. Use the fields named by that source; the
result contains canonical target identity, asset/package/file/code origins,
`resolved`, `status`, and warnings. The command is read-only.

Invalid targets, frames, geometry, surfaces, source identities, or stale
revisions fail before mutation. Cleanup restores transient selection and removes
or restores only the owned fixture; it never closes or focuses the user's
Editor.
