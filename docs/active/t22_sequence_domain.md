# T22 Sequence domain through the default SDK

Sequence HJSON has no task-specific SDK projection. Discover the current
contracts with `client.command_search(...)` and `client.command_detail(...)`,
then use the default bindings:

```python
result = client.content_graph.import_workspace(
    target,
    {"kind": "inline", "document": hjson_document},
    expected_revision,
    authorization_id,
)
state = client.content_graph.structure(target)
```

The shared SDK also exposes
`client.content_graph.export_workspace(target, workspace_path)`, and its exact
contract remains discoverable through `command_search`, `command_detail`, and
`uai-cli`. T22 does not claim a lossless Sequence export projection: that call
returns `sequence_domain_export_not_registered` instead of a false-success read
payload. The SDK forwards one request and owns no Sequence, time, HJSON, retry,
transport, persistence, or cleanup mechanics.

T13 is the sole HJSON initialization and recursive composition authority.
Sequence contributes only its frozen domain contract and delegates native
Binding/Track/Section/Channel/Key work to T55. Unsupported creation fails
before write; successful mutation is independently read back after reload.
