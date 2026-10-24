# T32 Long-Running SDK and CLI

Import only `uai` and create the normal Client with `uai.connect_project()`. The
final manifest generates the default `operation` namespace. Start results expose
their opaque lifecycle handle as `start_result.operation`:

For `client.job.compile_build`, `subject_ref` is a typed subject reference,
separate from the policy's `parameters`:

| `family_id` | `subject_ref` |
| --- | --- |
| `asset_compile` | `asset:<exact asset object path>` |
| `world_build`, `world_partition_resave` | A `world:` reference for the target world |
| `external_process` | The owned tool policy's `project:` or `asset:` reference; localization policies also accept `localization:` |
| `packaging` | `project:current` |

For example, a Blueprint compile uses
`subject_ref="asset:/Game/Example/BP_Item.BP_Item"` and
`parameters={"asset_path": "/Game/Example/BP_Item.BP_Item", ...}`. Use the
selected policy's documented parameters. Successful Blueprint HJSON imports
already compile and persist; a separate job is useful when its compile report
is needed, not as a mandatory second step after every import.

`policy:asset-compile:standard/v1` takes empty parameters. For Blueprint it
returns the existing Blueprint report; inspect `has_error/error_count`.
For StaticMesh it waits for native build completion and returns `build_completed`,
`diagnostic_count`, and native `messages`. UE supplies these
mesh diagnostics without severity and may include warnings; a nonzero count is
not automatically a failed build. This compile report does not replace asset validation.

For a finite job, use the common completion method:

```python
start_result.raise_for_error()
receipt = start_result.operation.finish(timeout=120)
receipt.raise_for_error()
# Inspect lifecycle_status/error_code and the policy's business report.
# Published receipt.artifacts remain available after operation release.
```

`wait()` starts accepted work and returns a terminal receipt without removing
the server record. `finish()` additionally saves that receipt and releases the
record. `close(reason)` requests cancellation, drains native cleanup, and saves
and releases the receipt. `wait(until=predicate)` supports persistent-session
readiness. A local timeout or disconnect retains custody; it does not cancel or
replay work. `native_stop_pending_deadline_exceeded` remains pending.
`receipt.ok` means the receipt was read, not that the business operation succeeded.
`cleanup_complete` separately confirms native Join/Release. An unknown result
without cleanup proof cannot be released as if cleanup had succeeded.

When Start is rejected before native work, a port may explicitly confirm that
no native resource needs cleanup. Such rejection returns a failed, releasable
operation. A failed native start attempt without that proof remains unknown;
the SDK does not infer cleanup from an input error or a no-mutation diagnostic.

An asset-editor session remains recoverable in `cleanup_pending` until its owned
windows are confirmed closed. After resolving a native close refusal, recover
the operation and call `close()` again. An explicit repeated cancel retries the
close request; background observation only checks completion and does not repeat
native close dialogs.

PCG generation is finite: `finish()` observes the native task's completion and
uses the same Join/Release path. Cancellation targets only this operation's task;
it does not delete successful output or promise rollback. The final signal
separates this generation's completion from pre-existing output.

The manifest identifies operation-producing commands. Before sending one, the
SDK atomically saves its original request identity in project-local custody.
Successful observations update it automatically. Use
`with client.operation.named("compile-job"):` around the initiating call to
choose a readable name in advance; otherwise use `handle.recovery_name` or
`client.operation.pending()`. `checkpoint(name)` only adds an optional alias.
It is no longer required to close the initial-response gap.

In another process, `client.operation.recover(name)` confirms the retained
original request or saved handle without resubmitting business work. If local
custody is missing, `client.operation.discover()` lists operations retained for
the authenticated local principal. `client.operation.takeover(name)` explicitly
rotates custody for a selected discovery entry; old handles lose access.
The principal is shared by authenticated local clients, not an agent identity.
Discovery alone does not take ownership. A lost takeover reply is itself
recoverable from the automatically saved request.

The server independently observes started operations and joins/releases their
native resources after completion, including after a client exits. Accepted work
still requires its first advance; discovery and status do not start it.
Persistent sessions remain active until explicitly closed. The server retains
their terminal records for receipt collection. `finish` persists the receipt
before removing that record, so a lost release response can be recovered.
Cached released receipts can be read locally; they cannot reopen work.
Missing server state without a matching saved receipt remains unconfirmed.
Editor restart never authorizes replay.

`forget_checkpoint(name)` deletes only local custody. Closing the Client closes
transport only. Editor shutdown uses the public SafeExit runner and its paired
external process witness; that receipt confirms process exit and is saved before
the runner removes its SDK custody. It is not an ordinary operation receipt.
If the exit start reply is lost, the runner keeps its witness alive while
recovering the original request. It does not submit another exit attempt.
Unconfirmed recovery retains the readable recovery name and pending custody.

The low-level `status/resume/cancel/receipt/reconcile/release` methods remain
available for deliberate incremental control. SDK workflows use the common
`wait/finish/close` implementation instead of domain-specific polling loops.

The ordinary and exact CLI forms reuse that same Client; lifecycle handles are
preferred over manually assembled `exec` payloads:

A connection failure is not a business result. Reconnect and query the same handle. Inspect `Result.ok`, `Result.payload`, and `Result.error`; accepted, running, stop-requested, and joining states are nonterminal. Never replay the initiating side effect after unknown state unless a later server receipt explicitly proves retry safety.

For persistent `asset_editor/open` sessions, readiness is
`Result.payload.latest_signal.payload.phase == "active"`; the outer operation
remains running after the asset opens. Use `handle.wait(until=...)`, retain the
handle during interaction, then `handle.close()`.

For PIE debug sessions, readiness is `latest_signal.payload.phase == "active"`
while the outer operation remains running. Use `handle.runtime_session` for
scenarios. Scenario termination refreshes that shared session handle; it does
not end the PIE session. `client.pie.start/run/resume/close` delegates lifecycle
work to the common Operation methods and persists both parent and flow custody
before submission. Its exited/failed signal ends the runtime handle without
requiring a paused snapshot in the exit response.
The SDK persists its shared runtime-session custody together with the operation
custody. Recovery still confirms the operation with the server; an older cached
parent signal cannot replace a newer session snapshot. A different session is
never merged, and an ended session remains ended. Legacy checkpoints without
runtime custody can still recover their operation, but cannot reconstruct a
newer scenario snapshot that was never saved. External concurrent changes still
require the server's exact snapshot check; recovery does not bypass it.
