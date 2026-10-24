# Material commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
client.material_instance.asset_create(...)
```

The exact CLI uses ueagentinterfacecmd with the current command name and one
JSON parameter object. No task-specific generated projection remains active.

Material creation uses `asset.factory.candidates` followed by
`asset.object.create`. Material and material-instance authoring then use
`content_graph.export_workspace` / `content_graph.import_workspace`; the old
typed material-create and instance-parameter apply identities are internal
operation kinds rather than public SDK commands. Material-instance creation
remains public until the common factory path can reproduce its required native
initialization.

Invalid class, parameter, parent, or stale internal state fails
before mutation. Unknown post-write state requires reconciliation. Cleanup
removes only owned material/function/instance fixtures and verifies absence
independently.
