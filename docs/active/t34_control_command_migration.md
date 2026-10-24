# T34 Control Command SDK and CLI

Import only `uai` and use `uai.connect_project()` for the local project. The generated
client exposes the same four exact bindings as the C++ registry:

```python
import uai

with uai.connect_project() as client:
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

`editor.session` and `job.compile_build` return a typed handle at
`start_result.operation`. Use that handle's `status()`, `receipt()`,
`cancel(reason)`, and `release()` methods for the shared T32 lifecycle; the SDK
keeps continuation identity private. Packaging policies are `query-environment`, `export-profile`,
`validate-profile`, `diff-profile`, `plan-build`, `run-build`, `parse-log`,
`report-artifacts`, and `clean-artifacts`, each under
`policy:packaging:<name>/v1` and subject `project:current`.

`asset_editor/open` is persistent: the SDK journals recovery before submission;
use `client.operation.named(...)` for a readable name, then wait until
`payload.latest_signal.payload.phase == "active"`.
Keep the handle for interaction; opening an asset or map does not make it terminal.
Use `handle.close()` to cancel, wait for actual cleanup, save the receipt and release.

The optional `parameters.ownership` is `"managed"` (default) or `"adopt"`.
Managed sessions own windows created by UAI, including implicit previews, and
follow the asset/editor replacements caused by imports. Existing user windows
are borrowed and remain open. Adopt explicitly assumes closing responsibility
for existing editors of that asset, including an older orphaned window.
Concurrent holders share one managed resource; the final holder closes it.

Preview actions and captures retain their existing persistent-window behavior.
To close a window they implicitly created, start the same `asset_editor/open`
session and close its returned handle. No private window identifier is required.
If an editor remains open, status reports `phase="cleanup_pending"` with the
asset and specific cause; the operation remains recoverable. Resolve unsaved
changes or close the editor, then `client.operation.recover(name).close()`.
Repeated cancel retries cleanup, not the original start. Closing does not
silently save or discard unsaved editor changes.

`pcg_generation` with `policy:pcg-generation:generate/v1` is a finite session:
use `pcg-component:<exact loaded component_path>` and empty parameters, then
`started.operation.finish()`. Its completion evidence belongs to this native
generation, including unchanged inputs. Successful content survives release;
save it separately through the public Editor save entry. See
[PCG generation](t52_pcg_command_migration.md).

PIE debug sessions expose `operation.runtime_session.scenario_execute(parameters=...)`.
The handle owns session identity and snapshot fencing. Use the current runtime
workspace's aliases and the property observation's typed value for `property_write`.
Within property values, live world objects use `{alias: "<current alias>"}`;
asset/class references use the shared `{path: "..."}` value, and soft paths need
not be loaded. `null` or `{path: null}` clears a reference. This also applies in
nested containers; an `unavailable` observation is not a writable reference.
Operation targets still require the current session's direct alias.
The runtime workspace is a paused-state snapshot, not a persistent asset import.
See the [PIE runtime scenario contract](../../../Plugins/UeAgentInterface/docs/contracts/long_running_session_public_commands.md#bounded-pie-runtime-scenario)
for lifecycle, step and recovery semantics.

`client.operation.plan_execute` preflights a bounded plan and routes exact
`public_command`, `editor_console`, or `transaction_history` steps. Public
command steps require an internal contract metadata. Undo/redo steps require
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
ueagentinterfacecmd exec job.compile_build --params-json '{"family_id":"packaging","subject_ref":"project:current","policy_id":"policy:packaging:query-environment/v1","parameters":{"include_sdks":true,"include_tools":true}}'
```

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery). The SDK contains no alternate
transport, command registry, polling implementation, Editor lifecycle, build
executor, or compatibility alias.
