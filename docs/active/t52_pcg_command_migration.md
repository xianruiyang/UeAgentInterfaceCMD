# PCG commands through the default SDK

Discover current contracts with client.query.command_search(...) and
client.query.command_detail(...), then use:

```python
client.pcg.component_apply(...)
client.pcg.component_world_binding_apply(...)
client.pcg.data_asset_apply(...)
client.pcg.data_asset_create_from_level(...)
client.pcg.generated_spatial_data_read(...)
client.pcg.graph_apply(...)
client.pcg.graph_instance_apply(...)
client.pcg.graph_parameters_apply(...)
client.pcg.node_candidates(...)
client.pcg.partition_spatial_state_read(...)
```

The exact CLI uses uai-cli with the current command ID, contract hash, and one
JSON parameter object. No task-specific generated projection remains.

`node_candidates` searches the target graph's native background context menu.
Its compact `name` or `id` selects what the native action creates; graph,
semantic identity, and placement remain in the owning HJSON edit.

Mutating calls use the common durable operation lifecycle and native PCG
mechanics. Generated-spatial-data and partition-state reads remain queries with
their declared state layer. Component/world binding and spatial reads keep
world/actor/component identity, semantic_frame_id, unit, bounds convention,
basis_evidence, and conversion_chain explicit; the SDK does not infer a world,
partition cell, component, graph, parameter schema, source level, or revision.

Success for writes requires native generate/settle where declared, terminal
projection, and independent persisted readback after reload. Invalid graph,
binding, source, bounds, frame, parameter, or stale revision fails before
mutation. Unknown state requires reconciliation. Cleanup removes only owned PCG
fixtures and generated state, then independently verifies absence.
