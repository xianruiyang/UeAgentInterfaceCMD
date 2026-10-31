# Fab SDK usage

The [plugin Fab contract](../../../Plugins/UeAgentInterface/docs/contracts/fab_command_contract.md) owns command behavior, selection, import boundaries and recovery semantics. Parameters come from the generated `client.fab` signatures or CLI `describe`.

Fab commands return a shared Operation. Consume the completed business result, rather than treating initial submission as completion:

```python
with uai.connect_project(project_path) as client:
    with client.operation.named("find-fab-assets"):
        started = client.fab.search(query="pickaxe")
    started.raise_for_error()
    result = started.operation.finish_result(timeout=120)
    result.raise_for_error()
    print(result.payload)
```

Pass the returned `name`, optional `select`, and `scope` directly to `asset` or `download`; pass the completed download's readable `download` name to `files` or `import_asset`. Category filters come from `categories`. Use `has_more` and `next_page` for pagination. For archive ambiguity, `files(download=..., query=...)` exposes every entry; copy the chosen entry unchanged into a generic import. Native UE packs import together and reject `entry`.

For download/import, choose a timeout appropriate to asset size. On a timeout or disconnect, recover the original operation by its name; do not blindly repeat a mutation. [Operation handling](t32_long_running.md) covers custody, cancellation and completed results. Output only the public fields needed by the caller, never the underlying connection or operation identity.

Reuse one connected client for related calls. After submitting and resuming a download Operation, `downloads` and `files` can inspect already completed local content while that download runs; they do not wait behind its network transfer. These queries read the currently published local records, not in-progress files. Wait for the original download's `finish_result()` before inspecting or importing its new content. Each local query still has its own Operation; a synchronous native import can occupy the Editor game thread and delay dispatch.

If the completed import returns `state="recovery_required"`, preserve that failed `Result`. Its `durable_journals` handles support `inspect()` and `reconcile()` for the same transaction. Reconcile verifies the current state; it does not delete or overwrite files to restore it. Resolve any remaining `state_unknown` using its concrete diagnostic before retrying import. A recorded recovery receipt alone does not prove that the original state was restored.
