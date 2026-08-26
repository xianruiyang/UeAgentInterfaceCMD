# Blueprint node candidates through the default SDK

Discover the current method and contract hash when they are not already known,
then query the exact owning Blueprint graph or pin-drag context:

```python
result = client.blueprint.node_candidates(
    target="/Game/Blueprints/BP_Example.BP_Example",
    graph_id="graph:...",
    query="Branch",
    limit=10,
)
candidate = result.payload["candidates"][0]
```

Obtain `graph_id` from the current Blueprint instead of guessing it. Call
`content_graph.structure`, select the unique container with
`kind="blueprint_graph"`, `value.name="EventGraph"`, and
`value.graph_kind="event_graph"`, then pass that container's opaque `id`
unchanged to `blueprint.node.candidates`. Do not infer the graph from its node
types, cache an earlier GUID, or reconstruct the identifier.

Use that same structure for compact semantic readback of existing nodes. The
node `value` reuses the Blueprint authoring state owner: events expose
`event_name`/`event_class`, component-bound events expose component and
delegate identity, function calls expose `function_name` and
`function_owner_class`, and variable nodes expose `variable_name`/`access`.
Select and verify by these fields plus the stable node `id`; do not infer an
identity from position, count, edges, or the raw K2 class, and do not export a
full workspace only to recover these semantics.

Copy only the exact `id`, or the `name` when it is unique in that same native
context, into the node entry of the Blueprint-root `uai.blueprint.edit/1`
document:

```hjson
"event_graph:EventGraph": {
  operation: update
  graph: { graph_kind: event_graph }
  nodes: {
    "node:BranchGate": {
      operation: create
      candidate: { id: "candidate:..." }
      pos: { x: 800, y: 600 }
    }
  }
}
```

The retired `uai.blueprint.node.edit/1` schema has no runtime provider. Do not
construct or submit a node-specific HJSON root.

The graph map key and optional pin context remain outside `candidate`; the node
map key remains the stable instance identity. Do not copy the complete search
row or synthesize `node_type`, `node_class`, function owner, spawner or action
metadata. The server re-enumerates the same native Blueprint Action Menu and
invokes the resolved `FEdGraphSchemaAction::PerformAction` before applying
explicit pins, edges or properties.

The response-level `graph_revision` is read-only candidate evidence. Use the
owning asset's latest public content-graph revision as `expected_revision` for
`client.content_graph.import_workspace(...)`. Unknown, ambiguous, stale or
wrong-context selectors fail before persistent mutation.

Use `client.query.command_search(...)` and `client.query.command_detail(...)` for the live
tutorial and nested contract; the equivalent CLI call is:

```text
uai-cli --connection connection.toml exec blueprint.node.candidates --contract-hash <hash> --params-json <json-object>
```
