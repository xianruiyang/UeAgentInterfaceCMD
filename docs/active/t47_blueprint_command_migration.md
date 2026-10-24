# Blueprint commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
client.blueprint.asset_create(
    asset_name="BP_Example",
    package_path="/Game/Examples",
    parent_class_ref="/Script/Engine.Actor",
)
client.blueprint.component_events_discover(...)
```

`parent_class_ref` accepts a known native class reference or a verified Blueprint
generated-class reference. A known standard reference does not require a preceding
candidate lookup. Factory, placeable-actor, component and node candidates describe
their own creation surfaces; they are not Blueprint parent-class lookup commands.

The equivalent CLI entry is
`ueagentinterfacecmd exec <command-name> --params-json <json-object>`. There is no
task-specific generated module, historical alias, or Python Blueprint business
implementation.

Component-event discovery accepts the exact Actor Blueprint asset and component,
then returns real `BlueprintAssignable`
delegate identities and binding state.

Successful Blueprint-root HJSON import already compiles, saves, reloads, and
checks persisted content. Do not add a separate compile job just to repeat those
steps. For an independent compile report use `client.job.compile_build(...)` with
`family_id="asset_compile"` and
`policy_id="policy:asset-compile:blueprint/v1"`. Set
`subject_ref="asset:" + asset_path`, where `asset_path` is the exact Blueprint
object path, and include that same `asset_path` in `parameters`. A bare object
path is not the job subject envelope. Keep the returned handle alive,
advance with `resume()` to terminal, then consume the report through
`receipt.artifacts` and `materialize()` before release. `status()` only observes;
check the report's `has_error/error_count`, not just operation completion.
For the complete lifecycle example see [T32](t32_long_running.md).
The generic `policy:asset-compile:standard/v1` takes empty parameters and now
returns the same Blueprint report with native messages and no save. Use the
dedicated policy when selecting its filter, messages, or save options.
Policy parameters and report semantics are maintained by the
[Plugin Blueprint contract](../../../Plugins/UeAgentInterface/docs/active/t47_blueprint_command_migration.md#consolidated-blueprint-workflows).

For graph view use `client.graph.view_read(...)` or
`client.graph.view_update(...)` with the exact `UEdGraph` identity in target and
context. A persisted update uses `update_document_state`; optional
`save_after_update` saves and independently reloads the Blueprint.

For the Components preview camera use `client.viewport.state_read(...)` or
`client.viewport.state_update(...)`. Set target and readable `viewport` to
`asset:<BlueprintObjectPath>#blueprint_components`, set
`asset_editor` to the Blueprint object path, and set
`viewport_scope="asset_editor"`, `viewport_role="components"`, and
`world_type="editor"`. Camera location/rotation are a typed transform and FOV
is `fov_degrees`. The command resolves only an existing live preview session;
it never opens, activates, or focuses an Editor window.
