# Landscape commands through the default SDK

`landscape.create`, `landscape.height_read`, and `landscape.height_delta` are
ordinary entries in the default generated binding catalog. Do not import a
task-specific generated projection module. Discover them before authoring:

```python
matches = client.query.command_search("landscape terrain height", limit=8)
create_contract = client.query.command_detail(
    "landscape.create", create_hash_from_matches
)
read_contract = client.query.command_detail(
    "landscape.height.read", read_hash_from_matches
)
delta_contract = client.query.command_detail(
    "landscape.height_delta", delta_hash_from_matches
)
```

Copy only fields returned by the current `command_detail`. Named calls use the
same contract hash and send one exact request:

```python
result = client.landscape.create(
    initial_height=initial_height,
    placement=placement,
    sample_region=sample_region,
    target_ref=target_ref,
    topology=topology,
)

height_state = client.landscape.height_read(
    target_ref,
    input={
        "region": {
            "frame_id": "ue.landscape.local_sample_grid",
            "min_inclusive": [2, 1],
            "max_inclusive": [4, 2],
        },
        "space_contract": {
            "frame_id": "ue.landscape.local_sample_grid",
            "unit": "sample",
            "basis_evidence": "observed exact Landscape and bounded region",
        },
    },
)

delta_result = client.landscape.height_delta(
    delta=delta,
    region=region,
    space_contract=space_contract,
    target_ref=target_ref,
)
```

Mutation spatial objects must state their `semantic_frame_id`, unit, basis
evidence, and any conversion chain required by the current contract. The
read-only height input instead uses the exact `frame_id` fields shown above.
The SDK does not guess sample-grid coordinates, Landscape scale, topology,
revisions, or target identity.

`landscape.create.target_ref` is a stable managed identity. Creation binds it
to the actor's UAI marker and `UAI/Managed/landscape` folder, and the same exact
identity can be used for `height_read`, `height_delta`, and exact managed
cleanup after reload. Unreal still owns the resulting UObject name and path.
An exact observed UObject path is also accepted; never infer one from the
label, use a partial path, or rewrite either identity into an alias.

`height_read.input.region` uses inclusive local sample-grid coordinates.
`height_read.input.space_contract` must declare the same frame, `unit=sample`,
and non-empty basis evidence. A request is bounded to 16,384 samples. The
projected state reports extent, region, scale, managed evidence and local
heights in `row_major_x_fastest` order. The command is strictly read-only and
does not dirty the Landscape package.

### Replacing `landscape_raise_circle`

The retired single-purpose command has one current successor:
`landscape.height_delta`. First read the exact target transform, extent and
scale through the current public world/Landscape read flow advertised by
`command_detail`. Convert the world-space circle to a bounded delta grid; the
following is caller-side parameter preparation, not another UE command path:

```python
import math

def circle_delta(center_local_xy, extent, scale_xyz,
                 radius_cm, strength_cm, falloff):
    min_x, min_y, max_x, max_y = extent
    cx, cy = center_local_xy  # inverse(target_transform) * center_world
    rx = radius_cm / scale_xyz[0]
    ry = radius_cm / scale_xyz[1]
    x1 = max(min_x, math.floor(cx - rx))
    y1 = max(min_y, math.floor(cy - ry))
    x2 = min(max_x, math.ceil(cx + rx))
    y2 = min(max_y, math.ceil(cy + ry))
    blend = min(1.0, max(0.0, falloff))
    values = []
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            distance = math.hypot(
                (x - cx) * scale_xyz[0],
                (y - cy) * scale_xyz[1],
            )
            linear = max(0.0, 1.0 - distance / radius_cm)
            smooth = linear * linear * (3.0 - 2.0 * linear)
            weight = linear + (smooth - linear) * blend
            values.append(strength_cm / scale_xyz[2] * weight)
    return {
        "region": {
            "frame_id": "ue.landscape.local_sample_grid",
            "min_inclusive": [x1, y1],
            "max_inclusive": [x2, y2],
        },
        "delta": {
            "encoding": "landscape_local_height_delta",
            "row_stride": x2 - x1 + 1,
            "values": values,
        },
    }
```

Combine that `region` and `delta` with the exact managed ID or observed UObject
path and a complete `space_contract`, then call
`client.landscape.height_delta(...)` once. The
formula uses both XY scales, so a circle remains circular in world space under
non-uniform Landscape scale; `strength_cm / scale_z` preserves the requested
world-space height.

The equivalent exact CLI forms are shown by discovery:

```text
uai-cli --connection connection.toml exec landscape.height.read --contract-hash <hash-from-command_detail> --params-json <json-object>
uai-cli --connection connection.toml exec landscape.height_delta --contract-hash <hash-from-command_detail> --params-json <json-object>
```

Success is terminal only when the common operation lifecycle reports a
verified native outcome. Validate the exact region with
`client.landscape.height_read(...)` before and after mutation and after reload
when persistence is in scope. Prewrite validation failures leave no residue;
`operation_state_unknown` requires reconciliation and must not be blindly
replayed. Remove test fixtures through the public destructive-content workflow
using the same managed ID, then verify `landscape_height_target_not_found`.
