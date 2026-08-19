# T32 Long-Running SDK and CLI

Import only `uai` and create the normal Client from one Connection TOML. The
final manifest generates the default `operation` namespace:

```python
import uai

with uai.connect("connection.toml") as client:
    status = client.operation.status(operation_ref)
    resumed = client.operation.resume(operation_ref, expected_generation)
    cancelled = client.operation.cancel(operation_ref, "user_cancelled")
```

The same catalog also exposes `client.operation.receipt(operation_ref)`,
`client.operation.reconcile(operation_ref, expected_generation)`, and
`client.operation.release(operation_ref)`. Pass the complete `operation_ref`
returned by the initiating server command without modification. Resume and
reconcile require the exact last observed generation; cancel requires a
non-empty reason. Each generated method sends one request through
`Client.execute`; it owns no transport, retry loop, operation registry, lease
generation, polling workflow, UE work, or cleanup logic.

The ordinary and exact CLI forms reuse that same Client:

```text
uai-cli --connection connection.toml exec operation.status --params-json {"operation_ref":{"operation_id":"...","owner_lease_id":"...","server_session_id":"..."}}
uai-cli --connection connection.toml exec operation.resume --contract-hash sha256:<exact> --params-json {"operation_ref":{"operation_id":"...","owner_lease_id":"...","server_session_id":"..."},"expected_generation":7}
```

A connection failure is not a business result. Reconnect and query the same reference. Inspect `Result.ok`, `Result.payload`, and `Result.error`; accepted, running, stop-requested, and joining states are nonterminal. Never replay the initiating side effect after `state_unknown`, an unknown operation, a lease or session mismatch, or a stale generation unless a later server receipt explicitly proves retry safety.
