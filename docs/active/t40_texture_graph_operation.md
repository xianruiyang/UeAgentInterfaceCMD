# T40 TextureGraph SDK and CLI

Import only `uai` and connect from one complete Connection TOML. The final
manifest generates all seven methods in the default `texture_graph` namespace:

```python
import uai

with uai.connect("connection.toml") as client:
    capture = client.texture_graph.artifact_capture(
        expected_settled_revision=current_settled_revision,
        outputs=[{
            "element_id": "builtin_output",
            "output_name": "Output",
        }],
        target_ref="/Game/TextureGraphs/TG_Example",
    )
```

The mutation lane uses the same namespace, including
`client.texture_graph.graph_node_mutate(...)`,
`client.texture_graph.graph_link_mutate(...)`, and
`client.texture_graph.graph_parameter_mutate(...)`. The
`client.texture_graph.graph_validate_evaluate_settle(...)` call completes the
same public Operation lifecycle. Use
`client.texture_graph.artifact_bake(...)` for persistent Texture2D outputs and
`client.texture_graph.runtime_probe(...)` for a non-persistent real render with
pixel statistics. Feed the `package-md5:*` revision returned by the successful
settle operation directly into artifact capture or bake; do not replace it with
a content-graph revision, guess it, or reuse an older revision. Bake fails closed
when the source is unsaved/dirty. Runtime probe reads the current target and does
not accept a revision parameter.

The generic form uses the same generated binding:

```python
capture = client.execute(
    "texture_graph.artifact.capture",
    {
        "expected_settled_revision": current_settled_revision,
        "outputs": [{
            "element_id": "builtin_output",
            "output_name": "Output",
        }],
        "target_ref": "/Game/TextureGraphs/TG_Example",
    },
)
```

The CLI forwards one identical request:

```text
uai-cli --connection connection.toml exec texture_graph.artifact.capture --params-json {"expected_settled_revision":"package-md5:<current-settled-revision>","outputs":[{"element_id":"builtin_output","output_name":"Output"}],"target_ref":"/Game/TextureGraphs/TG_Example"}
```

Use `client.query.command_search("capture texture graph artifact", limit=5)` and
then `client.query.command_detail(command_id, contract_hash)` to obtain the exact
request schema, named SDK/CLI forms, owner, failures and tutorial references.
Search is the only fuzzy command-selection step; execute the selected ID and
hash unchanged.

The client contains no HTTP implementation, retry, alias, TextureGraph parsing,
evaluation, persistence, rollback or Unreal Engine business behavior. Inspect
`Result.ok` and the returned revision/output identities.
