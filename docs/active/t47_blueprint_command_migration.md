# Blueprint commands through the default SDK

Discover exact contracts with `client.query.command_search(...)` and
`client.query.command_detail(...)`, then use the normal generated methods:

```python
client.blueprint.asset_create(...)
client.blueprint.component_events_discover(...)
```

The equivalent CLI entry is
`uai-cli --connection connection.toml exec <command-id> --contract-hash
<hash-from-command_detail> --params-json <json-object>`. There is no
task-specific generated module, historical alias, or Python Blueprint business
implementation.

Component-event discovery accepts the exact Actor Blueprint asset and component
plus compile/filter/limit options, then returns real `BlueprintAssignable`
delegate identities and binding state.

For Blueprint compilation use `client.job.compile_build(...)` with
`family_id="asset_compile"` and
`policy_id="policy:asset-compile:blueprint/v1"`, then consume the normal
operation status, receipt, and release lifecycle. The policy accepts
`asset_path`, `include_messages`, `max_messages`, `save_after_compile`, and
`severity_filter`.

For graph view use `client.graph.view_read(...)` or
`client.graph.view_update(...)` with the exact `UEdGraph` identity in target and
context. A persisted update uses `update_document_state`; optional
`save_after_update` saves and independently reloads the Blueprint.

For the Components preview camera use `client.viewport.state_read(...)` or
`client.viewport.state_update(...)`. Set target and `viewport_identity` to
`asset:<BlueprintObjectPath>#blueprint_components`, set
`asset_editor_identity` to the exact Blueprint object path, and set
`viewport_scope="asset_editor"`, `viewport_role="components"`, and
`world_type="editor"`. Camera location/rotation are a typed transform and FOV
is `fov_degrees`. The command resolves only an existing live preview session;
it never opens, activates, or focuses an Editor window.
