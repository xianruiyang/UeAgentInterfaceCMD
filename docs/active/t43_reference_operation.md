# Reference asset mutation through the default SDK

Discover the current contract before authoring:

```python
matches = client.query.command_search("reference asset mutation")
contract = client.query.command_detail(command_id="reference.asset_apply")
result = client.reference.asset_apply(
    object_path="/Game/UAI/Reference/BP_Reference.BP_Reference",
    intent="update",
    proposed_text="<current-contract-text>",
)
```

Only `object_path`, `intent`, and optional `proposed_text` from the current
`command_detail` are accepted. Do not guess an intent, normalize a different
target in the SDK, or replay a dynamic revision. The exact CLI equivalent is:

```text
uai-cli --connection connection.toml exec reference.asset_apply --contract-hash <hash-from-command_detail> --params-json <json-object>
```

Success requires the terminal revision from the common operation lifecycle and
an independent public `reference.asset_read` of the exact object's persisted
`BlueprintDisplayName`. Invalid intent
or target failures occur before mutation. `operation_state_unknown` requires
reconciliation and is not safe to replay. Cleanup is an explicit owned-target
operation followed by independent absence readback.
