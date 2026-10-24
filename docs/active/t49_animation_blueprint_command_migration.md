# Animation Blueprint commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
client.animation.anim_blueprint_layer_interface_asset_create(...)
client.content_graph.import_inline(...)
workspace = client.content_graph.export_workspace(...)
workspace.import_changes()
```

The exact CLI is ueagentinterfacecmd exec <command-name>
 --params-json <json-object>. No
task-specific generated projection is supported.

Animation Blueprint graph mutation uses HJSON authoring. Its typed apply
identity remains an internal operation kind for the content graph import
mechanics; it is not a public command or named SDK method.

Create an Animation Blueprint at a missing target through HJSON `import_inline`;
edit an existing asset through workspace export/import. The former
`animation.anim_blueprint.asset.create` identity is dormant and is not a
generated named SDK method. Layer-interface creation remains active.

Animation Blueprint authoring and layer-interface creation use the
common durable operation lifecycle and native mechanics. Asset identity,
package path, revision, and compile/settle policy are service-owned contract
state; the SDK does not ask the model to infer, supply, or replay them.

Schema, target, graph, compile, or stale-revision rejection occurs before
mutation where declared. Unknown post-write state requires reconciliation.
Cleanup removes only the owned animation Blueprint/interface fixtures and
verifies absence independently.
