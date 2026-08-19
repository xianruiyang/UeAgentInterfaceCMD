# AI commands through the default SDK

Discover current contracts through client.command_search(...) and
client.command_detail(...), then use:

```python
client.ai.behavior_tree_asset_create(...)
client.ai.behavior_tree_graph_apply(...)
client.ai.blackboard_asset_create(...)
client.ai.blackboard_schema_apply(...)
client.ai.eqs_asset_create(...)
client.ai.eqs_graph_apply(...)
client.ai.smart_object_definition_apply(...)
client.ai.smart_object_definition_asset_create(...)
client.ai.state_tree_asset_create(...)
client.ai.state_tree_hierarchy_apply(...)
```

The exact CLI uses uai-cli with the current command ID, contract hash, and one
JSON parameter object. No task-specific generated projection remains active.

All creation/schema/graph/hierarchy/definition calls use the common durable
operation lifecycle and native AI mechanics. Asset class, parent/schema
identity, nodes, links, keys, hierarchy, definition fields, expected revision,
compile/settle policy, and target path come only from command_detail. The SDK
does not infer or duplicate Behavior Tree, Blackboard, EQS, Smart Object, or
State Tree business.

Success requires native compile/settle where declared, terminal projection,
and independent persisted readback after reload. Invalid class, schema, graph,
key, hierarchy, definition, or stale revision fails before mutation. Unknown
state requires reconciliation. Cleanup removes only owned AI fixtures and
verifies absence independently.

