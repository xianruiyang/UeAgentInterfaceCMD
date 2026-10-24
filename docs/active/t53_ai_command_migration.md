# AI commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
client.ai.behavior_tree_asset_create(...)
client.ai.blackboard_asset_create(...)
client.ai.eqs_asset_create(...)
client.ai.smart_object_definition_asset_create(...)
client.ai.state_tree_asset_create(...)
```

The exact CLI uses ueagentinterfacecmd with the current command name and one
JSON parameter object. No task-specific generated projection remains active.

Asset creation uses the public command contract above. Structure mutation uses
`workspace = client.content_graph.export_workspace(...)` followed by sparse HJSON editing
and `workspace.import_changes()`; the former typed apply IDs
are internal HJSON operation kinds, not duplicate public SDK methods. Asset
class, parent/schema identity, nodes, links, keys, hierarchy, definition fields,
compile/settle policy and target path come from the current
export, generated SDK and focused domain documentation; revision and identity
are hidden service state. The SDK does not infer or duplicate Behavior Tree,
Blackboard, EQS, Smart Object, or State Tree business.

Success requires native compile/settle where declared, terminal projection,
and independent persisted readback after reload. Invalid class, schema, graph,
key, hierarchy, definition, or stale revision fails before mutation. Unknown
state requires reconciliation. Cleanup removes only owned AI fixtures and
verifies absence independently.
