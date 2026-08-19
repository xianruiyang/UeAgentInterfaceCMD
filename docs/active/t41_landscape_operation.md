# Landscape commands through the default SDK

`landscape.create` and `landscape.height_delta` are ordinary entries in the
default generated binding catalog. Do not import a task-specific generated
projection module. Discover them before authoring:

```python
matches = client.command_search(query="landscape terrain height")
create_contract = client.command_detail(command_id="landscape.create")
delta_contract = client.command_detail(command_id="landscape.height_delta")
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

delta_result = client.landscape.height_delta(
    delta=delta,
    region=region,
    space_contract=space_contract,
    target_ref=target_ref,
)
```

The spatial objects must state their `semantic_frame_id`, unit, basis evidence,
and any conversion chain required by the current contract. The SDK does not
guess sample-grid coordinates, Landscape scale, topology, revisions, or target
identity.

`landscape.create.target_ref` is a requested creation identity and supplies
the actor label; Unreal still owns the resulting UObject name and path. Read
the persisted Landscape after creation and use the exact returned UObject path
as `landscape.height_delta.target_ref`. Do not reuse a logical URI or infer a
path from the label.

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

Combine that `region` and `delta` with the observed `target_ref` and a complete
`space_contract`, then call `client.landscape.height_delta(...)` once. The
formula uses both XY scales, so a circle remains circular in world space under
non-uniform Landscape scale; `strength_cm / scale_z` preserves the requested
world-space height.

The equivalent exact CLI form is shown by discovery:

```text
uai-cli --connection connection.toml exec landscape.height_delta --contract-hash <hash-from-command_detail> --params-json <json-object>
```

Success is terminal only when the common operation lifecycle reports a
verified native outcome. Validate persistence with an independent public
world/Landscape read after reload. Prewrite validation failures leave no
residue; `operation_state_unknown` requires reconciliation and must not be
blindly replayed. Remove test fixtures through the public destructive-content
workflow and verify absence after reload.
