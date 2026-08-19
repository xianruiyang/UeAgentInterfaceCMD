# T38 Modeling Geometry SDK and CLI

Import only `uai` and connect from one complete Connection TOML. The final
manifest generates all 32 methods in the default `mesh` namespace:

```python
import uai

with uai.connect("connection.toml") as client:
    result = client.mesh.primitive_box_create(
        anchor="base_center",
        placement={
            "semantic_frame_id": "uai.world",
            "write_frame_id": "ue.world",
            "read_frame_id": "ue.world",
            "verify_frame_id": "ue.world",
            "unit": "centimeter",
            "translation": [125.0, -50.0, 30.0],
            "rotation_quaternion_xyzw": [0.0, 0.0, 0.0, 1.0],
            "scale": [1.0, 1.0, 1.0],
            "basis_evidence": "UE left-handed Z-up centimeters",
            "conversion_chain": "identity",
        },
        size_cm=[120.0, 80.0, 60.0],
        subdivisions=[2, 2, 1],
        target_ref="UAI/StrictV2/T38/Box_Default_r58",
    )
```

The same namespace also exposes topology methods such as
`client.mesh.topology_mirror(...)`. The generic form uses the same generated
binding:

```python
result = client.mesh.modeling_session(
    action="observe_tool",
    target={},
    input={},
    context={},
    projection={},
)
```

`mesh.modeling_session` is the only public successor for Modeling Mode
lifecycle, active-tool observation, tool properties/actions, mesh selection,
save, actor-mesh replacement and surface snapping when no narrower exact
current mesh command owns the capability. The supported actions are
`activate`, `observe_tool`, `start_tool`, `set_tool_property`,
`invoke_tool_action`, `accept_tool`, `cancel_tool`, `observe_selection`,
`set_actor_selection`, `set_selection_mode`, `clear_mesh_selection`,
`select_via_screen`, `select_via_world_ray`, `replace_actor_mesh`,
`save_mesh_asset`, and `snap_to_surface`. Historical `modeling_*` command IDs
are not callable aliases.

```python
result = client.execute(
    "mesh.primitive.box.create",
    {
        "anchor": "base_center",
        "placement": {
            "semantic_frame_id": "uai.world",
            "write_frame_id": "ue.world",
            "read_frame_id": "ue.world",
            "verify_frame_id": "ue.world",
            "unit": "centimeter",
            "translation": [125.0, -50.0, 30.0],
            "rotation_quaternion_xyzw": [0.0, 0.0, 0.0, 1.0],
            "scale": [1.0, 1.0, 1.0],
            "basis_evidence": "UE left-handed Z-up centimeters",
            "conversion_chain": "identity",
        },
        "size_cm": [120.0, 80.0, 60.0],
        "subdivisions": [2, 2, 1],
        "target_ref": "UAI/StrictV2/T38/Box_Default_r58",
    },
)
```

The CLI forwards one identical request:

```text
uai-cli --connection connection.toml exec mesh.primitive.box.create --params-json {"anchor":"base_center","placement":{"semantic_frame_id":"uai.world","write_frame_id":"ue.world","read_frame_id":"ue.world","verify_frame_id":"ue.world","unit":"centimeter","translation":[125,-50,30],"rotation_quaternion_xyzw":[0,0,0,1],"scale":[1,1,1],"basis_evidence":"UE left-handed Z-up centimeters","conversion_chain":"identity"},"size_cm":[120,80,60],"subdivisions":[2,2,1],"target_ref":"UAI/StrictV2/T38/Box_Default_r58"}
```

Use `client.query.command_search("create mesh box", limit=5)` and then
`client.query.command_detail(command_id, contract_hash)` to obtain the exact
schema, named SDK/CLI forms, owner, failure catalog and tutorial references.
Search is the only fuzzy step; execute the selected ID and hash unchanged.

The client contains no HTTP implementation, retry, alias, registry fallback,
parameter remapping, geometry processing, persistence, rollback or Unreal
Engine business behavior. Inspect `Result.ok` and the operation's terminal
projection; `state_unknown` is never safe for automatic replay.
