# Animation Blueprint commands through the default SDK

Discover current fields and hashes through client.command_search(...) and
client.command_detail(...), then use:

```python
client.animation.anim_blueprint_asset_create(...)
client.animation.anim_blueprint_graph_apply(...)
client.animation.anim_blueprint_layer_interface_asset_create(...)
```

The exact CLI is uai-cli --connection connection.toml exec <command-id>
--contract-hash <hash-from-command_detail> --params-json <json-object>. No
task-specific generated projection is supported.

All three calls use the common durable operation lifecycle and native Animation
Blueprint mechanics. Asset class, skeleton/interface identity, package path,
graph nodes/links, expected revision, and compile/settle policy come only from
the current contract; the SDK does not infer or replay them. A graph apply is
not successful until native compile/settle and terminal projection complete,
followed by independent persisted readback after reload.

Schema, target, graph, compile, or stale-revision rejection occurs before
mutation where declared. Unknown post-write state requires reconciliation.
Cleanup removes only the owned animation Blueprint/interface fixtures and
verifies absence independently.

