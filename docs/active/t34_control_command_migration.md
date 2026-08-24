# T34 Control Command SDK and CLI

Import only `uai` and connect from one complete Connection TOML. The generated
client exposes the same four exact bindings as the C++ registry:

```python
import uai

with uai.connect("connection.toml") as client:
    session = client.editor.session(
        "asset_editor",
        "asset:/Game/MyAsset.MyAsset",
        "policy:asset-editor:open/v1",
        {},
    )
    environment = client.job.compile_build(
        "packaging",
        "project:current",
        "policy:packaging:query-environment/v1",
        {"include_sdks": True, "include_tools": True},
    )
    plan = client.operation.plan_execute(
        [{
            "step_id": "status",
            "kind": "transaction_history",
            "action": "status",
            "subject_ref": "editor:transaction-history",
            "policy_id": "policy:transaction-history:standard/v1",
            "parameters": {},
        }],
        "stop",
        "reject_non_atomic",
    )
    # editor.safe_exit remains a generated exact binding, but ordinary callers
    # must use scripts/ue/SafeExitLifecycle.py to create its external witness.
```

The generated catalog exposes the exact
`client.editor.safe_exit(dirty_resolution, external_witness)` binding, but it
is not a direct lifecycle entry point. After exact dirty resource readback and
an explicit `reject|save|discard` decision, use the project
`scripts/ue/SafeExitLifecycle.py` runner. The runner owns the external process
witness and durable terminal; callers must not construct `external_witness`
themselves.

`editor.session` and `job.compile_build` return `operation_ref`. Use
`client.operation.status`, `client.operation.receipt`,
`client.operation.cancel`, and `client.operation.release` for the shared T32
lifecycle. Packaging policies are `query-environment`, `export-profile`,
`validate-profile`, `diff-profile`, `plan-build`, `run-build`, `parse-log`,
`report-artifacts`, and `clean-artifacts`, each under
`policy:packaging:<name>/v1` and subject `project:current`.

`client.operation.plan_execute` preflights a bounded plan and routes exact
`public_command`, `editor_console`, or `transaction_history` steps. Public
command steps require an exact current binding hash. Undo/redo steps require
the observed transaction revision. Mixed plans declare `best_effort`; the
atomic mode is restricted to a single transaction-history mutation.

The generic and CLI forms use the identical generated binding:

```python
result = client.execute(
    "operation.plan.execute",
    {"steps": steps, "on_error": "stop", "atomicity": "best_effort"},
)
```

```text
uai-cli --connection connection.toml exec job.compile_build --params-json {"family_id":"packaging","subject_ref":"project:current","policy_id":"policy:packaging:query-environment/v1","parameters":{"include_sdks":true,"include_tools":true}}
```

Use `client.query.command_search("editor session packaging operation plan",
limit=10)` and `client.query.command_detail(command_id, contract_hash)` for
the current schema, failures, and tutorial. The SDK contains no alternate
transport, command registry, polling implementation, Editor lifecycle, build
executor, or compatibility alias.
