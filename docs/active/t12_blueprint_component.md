# Blueprint Component candidate through the default SDK

Query the requested Component class and name through the default generated
binding:

```python
result = client.blueprint.component_candidates(
    target="/Game/Blueprints/BP_Example.BP_Example",
    component_class="/Script/Engine.PointLightComponent",
    requested_name="PointLight",
)
candidate = result.payload["candidates"][0]
```

Copy `candidate` unchanged to the Component entry in the Blueprint-root
`uai.blueprint.edit/1` document:

```hjson
"component:PointLight": {
  operation: create
  candidate: {
    name: PointLight
    component_class: "/Script/Engine.PointLightComponent"
    binding_revision: "sha256:..."
  }
  parent: DefaultSceneRoot
}
```

Do not synthesize duplicate `name` or `class` fields; the server validates the
candidate against current SCS state and expands the native mutation fields.
The response-level `scs_revision` and `existing_components` are read-only
evidence. Use the owning asset's latest public content-graph revision as the
`expected_revision` of `client.content_graph.import_workspace(...)`.

A changed class, name availability, SCS state, or binding fails before write,
including the exact stale code
`blueprint_surface_component_candidate_binding_stale`. Use
`client.command_search(...)` and `client.command_detail(...)` for the current
contract; `uai-cli` exposes the same exact command and JSON parameter object.
T13 remains the sole source-carrier and common recursive initialization
authority; the SDK forwards only the selected public command.
