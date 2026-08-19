# Material commands through the default SDK

Discover current fields, graph/parameter schema, and hashes through
client.command_search(...) and client.command_detail(...), then use:

```python
client.material.asset_create(...)
client.material.function_graph_apply(...)
client.material.graph_apply(...)
client.material_instance.asset_create(...)
client.material_instance.parameters_apply(...)
```

The exact CLI uses uai-cli with the current command ID, contract hash, and one
JSON parameter object. No task-specific generated projection remains active.

Creation, graph application, and instance parameter application use the common
durable operation lifecycle and native material mechanics. The SDK does not
infer asset class, parent, nodes, links, expressions, parameter types, static
switches, expected revision, compile/settle policy, or save target. Success is
terminal only after native compile/settle where required and independent
persisted readback after reload.

Invalid class, graph, link, parameter, parent, or stale-revision input fails
before mutation. Unknown post-write state requires reconciliation. Cleanup
removes only owned material/function/instance fixtures and verifies absence
independently.

