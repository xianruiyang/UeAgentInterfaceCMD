# Blueprint node candidate through the default SDK

Discover the current method and hash when they are not already known, then
query the exact owning Blueprint graph:

```python
matches = client.command_search(query="Blueprint node candidate")
contract = client.command_detail(command_id="blueprint.node.candidates")
result = client.blueprint.node_candidates(
    target="/Game/Blueprints/BP_Example.BP_Example",
    graph_id="graph:...",
    query="branch",
)
candidate = result.payload["candidates"][0]
```

Copy `candidate` unchanged to the node entry in the Blueprint-root
`uai.blueprint.edit/1` document:

```hjson
"event_graph:EventGraph": {
  operation: update
  graph: { graph_kind: event_graph }
  nodes: {
    "11111111-1111-1111-1111-111111111111": {
      operation: create
      candidate: {
        name: "/Script/BlueprintGraph.K2Node_IfThenElse"
        binding_revision: "sha256:..."
        display_name: Branch
        graph_id: "graph:..."
      }
      pos: { x: 800, y: 600 }
    }
  }
}
```

Do not turn `candidate.graph_id` into the graph map key and do not synthesize
`node_type` or `node_class`; the server validates the exact binding and expands
those native fields. The response-level `graph_revision` is read-only candidate
evidence. Use the owning asset's latest public content-graph revision as the
`expected_revision` of `client.content_graph.import_workspace(...)`.

A changed binding fails before write, including the exact stale code
`blueprint_surface_node_candidate_binding_stale`. The equivalent CLI call is:

```text
uai-cli --connection connection.toml exec blueprint.node.candidates --contract-hash <hash> --params-json <json-object>
```
