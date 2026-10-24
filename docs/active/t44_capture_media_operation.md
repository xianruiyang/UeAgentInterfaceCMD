# Capture and media commands through the default SDK

When the command is unknown, discover it and request usage for its exact command ID:

```python
matches = client.query.command_search("capture image viewport niagara")
usage = client.query.command_usage(["capture.image.execute"])

started = client.capture.image_execute(
    subject_ref="capture-subject:viewport:active",
    policy_id="policy:image-capture:viewport/v1",
    parameters={"format": "png", "max_size": 1024},
)
```

The other exact default bindings are `client.capture.media_execute(...)` and
`client.capture.render_execute(...)`. Each named method forwards one exact
request; it does not poll, retry, render, clean up, or choose a policy. Use the SDK
handle for the capture lifecycle below. A CLI `exec` invocation of the same command
only starts it; it does not wait for the final image. Connection and machine
metadata remain SDK-owned.

Use `subject_ref` for the exact target, `policy_id` for the explicit behavior,
and `parameters` for only that policy's documented fields. Asset subjects use
`capture-subject:asset:<object-path>`, actors use
`capture-subject:actor:<actor-name-or-label>`, and the active Level viewport is
`capture-subject:viewport:active`. If a policy accepts `output_file`, it names
the final owned artifact; native work still uses operation-owned staging.

Actor references accept an exact object path, a unique native name or label,
or a name qualified by its discovery scope. If `parameters` repeats the target
as `actor`, `actor_name`, `actor_label`, `id`, or `asset_path`, every supplied
reference must identify the same subject. Ambiguous or conflicting targets
return a diagnostic before capture moves the camera or opens an asset editor.

Use `ueagentinterfacecmd describe capture.image.execute --parameter policy_id`
for available policy IDs. The base description also lists registered `variants`.
Select one with `--variant <variant_id>` for its exact request contract and guidance;
add `--parameter parameters` for the policy's parameter schema. These contracts are
generated from the plugin registry, including UMG canvas/crop fields. Policy behavior and documented
fields belong to the [plugin capture contract](../../../Plugins/UeAgentInterface/docs/active/t44_capture_media_operation.md),
not to a second catalog in this SDK guide.

Level viewport capture prepares its existing native window and layout when
needed, including restoring a minimized window. No separate SDK preparation
call is required; see the plugin capture contract for policy scope and
asset-editor window permissions.

Read policy-specific sampling facts from the terminal
`latest_signal.payload.capture_receipt`. Level Sequence image capture is an independent
scene-camera render, including when it falls back to viewport camera geometry; it does
not reproduce the viewport backbuffer or its exposure history at a larger resolution.
Its frame receipts associate individual outputs using `uses_primary_artifact` or
`raw_artifact_index` into `additional_artifact_refs`. The SDK exposes those declared roles as
`result.primary_artifact` and `result.additional_artifacts`, so a frame's
`raw_artifact_index` indexes `result.additional_artifacts` directly. The existing
`result.artifacts` tuple still lists all handles; its traversal order does not identify the
primary output. See the plugin contract for details.

## Transform-candidate visual preview

`policy:image-capture:transform-candidates/v1` is a current policy, not a
historical alias. Pass one exact Actor object path and one or more candidates:

```python
started = client.capture.image_execute(
    subject_ref="capture-subject:actor:/Game/Maps/MyMap.MyMap:PersistentLevel.MyActor",
    policy_id="policy:image-capture:transform-candidates/v1",
    parameters={
        "candidates": [
            {"label": "left", "relative_to_original": True,
             "transform": {"location": {"x": 0, "y": -100, "z": 0}}},
            {"label": "right", "relative_to_original": True,
             "transform": {"location": {"x": 0, "y": 100, "z": 0}}},
        ],
        "format": "png",
        "max_size": 720,
    },
)
```

The policy captures the original frame plus each temporary candidate from the
current Level viewport and publishes one operation-owned frame sheet. It does not
focus the Editor, score candidates, choose one, or persist a candidate. Every
terminal mechanics path restores the Actor transform, package dirty state,
Actor selection, and temporary viewport realtime override; success fails closed
unless those restorations are observed. After comparison, edit the Actor's declared
transform fields in its Level workspace and persist with `workspace.import_changes()`; the managed workspace
owns revision and identity. See [T26](t26_level_world_domain.md).

## Asset preview workspace capture

`policy:image-capture:asset-preview/v1` captures the selected asset's actual preview.
Use `capture-subject:asset:<object-path>` and `parameters={"mode":"single"}` or
`{"mode":"sequence"}`; `target` optionally selects a named target from the exported
`preview/index.hjson`. Camera, environment and capture settings are edited in the
asset workspace and applied with its ordinary import operation. Capture does not
implicitly import pending local edits or accept another copy of those settings.

Sampling, render extent, output dimensions, realtime state and receipt semantics
are defined in the plugin contract's
[Asset preview workspace capture](../../../Plugins/UeAgentInterface/docs/active/t44_capture_media_operation.md#asset-preview-workspace-capture)
section. Consume the exported preview fields and actual receipt; do not infer a
second configuration from an unrelated screenshot policy.

## Advance, inspect and release

A successful start returns a handle in `start_result.operation`, not the final image.
Use `handle.finish()` to collect and save the receipt and release the operation,
then inspect the result and materialize its published artifacts. Use `handle.close()`
to cancel and drain the same operation. The SDK saves recovery custody before submission;
follow [T32](t32_long_running.md) after a disconnect or process exit. `state_unknown` forbids automatic
replay. Timeout, unsupported policy, invalid subject, resource refusal, missing
artifact, failed independent readback, or incomplete cancellation must not be
reported as success. Reuse the current rendering-capable Editor. Use an owned
worker only when the requested operation needs process isolation.
