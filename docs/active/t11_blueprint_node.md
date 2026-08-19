# Blueprint node through the default SDK

`blueprint.node.candidates` is an ordinary entry in the default generated
binding catalog. Do not import a task-specific generated projection. Discover
the current purpose and exact fields first:

```python
matches = client.command_search(query="Blueprint node candidate")
contract = client.command_detail(command_id="blueprint.node.candidates")
```

Copy the public content/graph query identities without reinterpretation, then
invoke the named binding. It uses the same current contract hash as exact
generic execution and sends one request:

```python
result = client.blueprint.node_candidates(
    target=target,
    graph_id=graph_id,
    query="branch",
)
```

Copy the returned `candidate.name`, `binding_revision`, and `graph_revision`
unchanged into `client.content_graph.import_workspace(...)`. T13 remains the
sole initialization and recursive HJSON authority; this query does not select
a candidate or mutate Unreal state.

The equivalent CLI call uses the hash returned by `command_detail`:

```text
uai-cli --connection connection.toml exec blueprint.node.candidates --contract-hash <hash> --params-json <json-object>
```

Unresolved target, graph, or candidate identity is a terminal read-only
failure. It does not fall back to a class alias or a task-local binding.
