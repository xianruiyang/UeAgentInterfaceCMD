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
client.world.object_transform_update(...)
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
frames fail before mutation. `world.object_transform.update` accepts exactly one
complete Actor transform plus the current revision returned by the read command.
It converts the declared transform to `unreal.world` centimeters, rejects stale
revisions, non-finite components, non-normalized rotation, and zero scale before
mutation, saves the Actor's map package, and verifies all ten transform
components through an independent readback. Successful durable Actor transform,
mesh bake, and pivot updates remain observable after reload.

Transform candidates are visual previews rather than a WorldSpatial scoring
query. Discover `capture.image.execute` and select
`policy:image-capture:transform-candidates/v1` to capture the original Actor and
up to 15 temporary candidates from the current Level viewport into one frame
sheet. The preview restores Editor state and never selects or persists a
candidate; submit the chosen value through
`client.world.object_transform_update(...)`.

For `client.reference.origin_resolve(...)`, pass one `input.target` whose
required `source` is `catalog_candidate`, `json_reference`, `ue_object`,
`graph_node`, or `name_reference`. Use the fields named by that source; the
result contains canonical target identity, asset/package/file/code origins,
`resolved`, `status`, and warnings. The command is read-only.

Invalid targets, frames, geometry, surfaces, source identities, or stale
revisions fail before mutation. Cleanup restores transient selection and removes
or restores only the owned fixture; it never closes or focuses the user's
Editor.
