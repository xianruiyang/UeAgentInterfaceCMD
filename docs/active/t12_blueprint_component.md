# Blueprint Add Component candidates through the default SDK

Search the native Add Component registry through the generated binding:

```python
page = client.blueprint.component_candidates(
    target="/Game/Blueprints/BP_Example.BP_Example",
    parent="DefaultSceneRoot",
    query="Point Light",
    limit=10,
)
candidate = page.payload["candidates"][0]
```

Continue with `cursor=page.payload["next_cursor"]` while `has_more` is true.
Pass `id=candidate["id"]` to resolve one exact row again. `name` may be used
instead only when it is unique in the same registry.

The minimum Blueprint-root HJSON is:

```hjson
"component:PointLight": {
  operation: create
  candidate: { id: "candidate:..." }
  parent: DefaultSceneRoot
}
```

The retired `uai.blueprint.component.edit/1` schema has no runtime provider.
Do not construct or submit a Component-specific HJSON root.

The map key is the Component instance name. The candidate selects the native
Component action; it does not own the instance name, parent, operation, or
properties. Optional `class_path` and `asset_path` are diagnostics and may be
supplied as assertions, but they are not required creation fields.

The server re-enumerates the native registry, invokes the same Component
creation mechanics, and independently reads back the persisted SCS. Use the
owning asset's latest public content-graph revision as `expected_revision` for
`client.content_graph.import_workspace(...)`.

Use `client.query.command_search(...)` and `client.query.command_detail(...)` for the
current command tutorial; `uai-cli` exposes the same exact command and JSON
parameter object. T13 remains the sole source-carrier and common recursive
initialization authority; the SDK forwards only the selected public command.
