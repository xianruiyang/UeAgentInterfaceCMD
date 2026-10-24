# T38 Modeling Geometry SDK and CLI

Import only `uai` and use `uai.connect_project()` for the local project. The final
manifest generates the active Modeling methods in their default namespaces:

```python
import uai

with uai.connect_project() as client:
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
        target_ref="UAI/StrictV2/T38/Box_Default",
    )
```

The same namespace also exposes topology methods such as
`client.mesh.topology_mirror(...)`. The generic form uses the same generated
binding:

```python
result = client.mesh.modeling_session(
    action="observe_tool",
)
```

`mesh.modeling_session` owns only Modeling Mode lifecycle, active-tool
observation, tool properties/actions, session-native actor selection, mesh
selection mode and screen selection, and mesh save. The supported actions are
`activate`, `observe_tool`, `start_tool`, `set_tool_property`,
`invoke_tool_action`, `accept_tool`, `cancel_tool`, `set_actor_selection`,
`set_selection_mode`, `clear_mesh_selection`, `select_via_screen`, and
`save_mesh_asset`. Read selection through `world.selection`; call
`mesh.element.select_by_ray` and `world.object_snap_to_surface` directly for ray
selection and surface snapping. Actor-mesh replacement is HJSON desired state;
its old typed command is dormant. Historical `modeling_*` registered command
names are not callable aliases.

For `set_tool_property`, `input.tool_properties` contains one direct descriptor:
`{property_set, property_path, kind, value}`. Copy its selector, type and value
shape from the current `observe_tool` response; do not send a property-set
object containing a nested `properties` array. `start_tool` may include a batch
of these descriptors; `set_tool_property` edits one descriptor in the current tool.
`target`, when needed, is an exact identity string. Property failures preserve
the common authoring diagnostic, including the property path and available
expected/actual values or source location. Other session failures expose the
native cause and action as `error.diagnostic.code` and `error.diagnostic.stage`,
with the actionable native/input reason in `error.diagnostic.message`. Explicit
internal context remains in the machine receipt.

`mesh.primitive.*.create` produces a world `DynamicMeshActor`;
`target_ref` identifies that Modeling result, not a `/Game/...` Static Mesh
asset to query through the asset registry. If a native Modeling tool is used
to produce an asset, read its actual output type and asset-generation settings
before accepting it. The generic `accept_tool` receipt does not promise a
`created_asset_path`; read the resulting selection and `save_mesh_asset` receipt
for the actual native output. Creation wrappers that return `created_asset_path`
provide that same asset identity directly.
`save_mesh_asset` only saves Static Mesh packages already referenced by the
selected actors (or `input.actor_ids`). It does not convert Dynamic Mesh actors
or choose an output asset path; its receipt lists `saved_package_paths`.

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
        "target_ref": "UAI/StrictV2/T38/Box_Default",
    },
)
```

The CLI forwards one identical request:

```text
ueagentinterfacecmd exec mesh.primitive.box.create --params-json '{"anchor":"base_center","placement":{"semantic_frame_id":"uai.world","write_frame_id":"ue.world","read_frame_id":"ue.world","verify_frame_id":"ue.world","unit":"centimeter","translation":[125,-50,30],"rotation_quaternion_xyzw":[0,0,0,1],"scale":[1,1,1],"basis_evidence":"UE left-handed Z-up centimeters","conversion_chain":"identity"},"size_cm":[120,80,60],"subdivisions":[2,2,1],"target_ref":"UAI/StrictV2/T38/Box_Default"}'
```

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
Search matches only positive tokens from registered command names, registered keywords and
registered synonyms; execute the selected generated SDK method unchanged.

Existing-carrier methods take `target_ref`; binary operations additionally take
`operand_ref` and its transform. Carrier revisions are resolved and frozen by
the server owner, so the generated SDK neither accepts nor returns them.

The client contains no HTTP implementation, retry, alias, registry fallback,
parameter remapping, geometry processing, persistence, rollback or Unreal
Engine business behavior. Inspect `Result.ok` and the operation's terminal
projection; `state_unknown` is never safe for automatic replay.
