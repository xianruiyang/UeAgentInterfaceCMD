# Capture and media commands through the default SDK

Discover the current contract and a policy before calling it:

```python
matches = client.command_search("capture image viewport niagara")
contract = client.command_detail(command_id="capture.image.execute")

started = client.capture.image_execute(
    subject_ref="capture-subject:viewport:active",
    policy_id="policy:image-capture:viewport/v1",
    parameters={"format": "png", "max_size": 1024},
)
```

The other exact default bindings are `client.capture.media_execute(...)` and
`client.capture.render_execute(...)`. Each named method forwards one exact
request; it does not poll, retry, render, clean up, or choose a policy. The CLI
form uses the same contract hash:

```text
uai-cli --connection connection.toml exec capture.image.execute --contract-hash <hash-from-command_detail> --params-json <json-object>
```

Use `subject_ref` for the exact target, `policy_id` for the explicit behavior,
and `parameters` for only that policy's documented fields. Asset subjects use
`capture-subject:asset:<object-path>`, actors use
`capture-subject:actor:<actor-name-or-label>`, and the active Level viewport is
`capture-subject:viewport:active`. If a policy accepts `output_file`, it names
the final owned artifact; native work still uses operation-owned staging.

`command_detail(command_id="capture.image.execute")` dynamically projects the
current image-policy catalog into the `policy_id` input schema and places any
policy-specific parameter schemas under `parameters.schema` at
`x-uai-policy-contracts`. This projection comes from the same policy registry
that executes the request, so the SDK tutorial does not maintain a second list.

## Transform-candidate visual preview

`policy:image-capture:transform-candidates/v1` is a current policy, not a
historical alias. Pass one exact Actor object path and 1-15 candidates:

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
current Level viewport and publishes one operation-owned frame sheet. The 15
candidate limit keeps the complete sheet at no more than 16 frames. It does not
focus the Editor, score candidates, choose one, or persist a candidate. Every
terminal mechanics path restores the Actor transform, package dirty state,
Actor selection, and temporary viewport realtime override; success fails closed
unless those restorations are observed. After comparison, persist the chosen
value separately with `world.object_transform.update` and verify it with
`world.object_transform.read`.

## Image policy migration table

| Retired historical identity | Current `capture.image.execute` policy | `parameters` responsibility |
| --- | --- | --- |
| `anim_blueprint_screenshot` | `policy:image-capture:anim-blueprint/v1` | graph/window/viewport fields |
| `anim_sequence_screenshot` | `policy:image-capture:anim-sequence/v1` | time, frame and sequence-sheet fields |
| `behavior_tree_screenshot` | `policy:image-capture:behavior-tree/v1` | offscreen widget fields |
| `blueprint_screenshot` | `policy:image-capture:blueprint/v1` | graph/window/viewport and restore fields |
| `control_rig_screenshot` | `policy:image-capture:control-rig/v1` | capture target fields |
| `metasound_screenshot` | `policy:image-capture:metasound/v1` | graph image fields |
| `niagara_screenshot` | `policy:image-capture:niagara/v1` | preview camera, tick, frames and sheet fields |
| `pcg_screenshot` | `policy:image-capture:pcg-viewport/v1` | actor framing and viewport image fields |
| `screenshot_viewport` | `policy:image-capture:viewport/v1` | view mode, visualization, warmup, tick, restore, format and output fields |
| `screenshot_viewport_buffer` | `policy:image-capture:viewport-buffer/v1` | buffer, depth, invert, format and output fields |
| `sequence_screenshot` | `policy:image-capture:level-sequence/v1` | time, frame and sequence-sheet fields |
| `sound_cue_screenshot` | `policy:image-capture:sound-cue/v1` | graph image fields |
| `state_tree_screenshot` | `policy:image-capture:state-tree/v1` | offscreen widget fields |
| `texture_screenshot` | `policy:image-capture:texture/v1` | mip, slice, format and statistics fields |
| `umg_screenshot` | `policy:image-capture:umg/v1` | offscreen size, crop and region fields |

The historical names in the first column are documentation identities only.
Do not call them and do not construct an alias from them.

Every image policy requires a rendering-capable Editor process. In a process
where `FApp::CanEverRender()` is false, including `-NullRHI`, the returned
operation reaches terminal failure with
`capture_image_rhi_unavailable:<policy_id>` before screenshot mechanics or an
asset editor is opened, and it publishes no image artifact. The SDK and CLI do
not provide a fallback; run image capture in a rendering-capable Editor or
owned RHI worker.

## Observe, cancel and release

A successful start returns an `operation_ref`, not the final image. Use the
public `operation.status` contract to observe or reattach until terminal. Use
`operation.cancel` for the same operation, read the terminal receipt and
artifact, then call `operation.release`. `state_unknown` forbids automatic
replay. Timeout, unsupported policy, invalid subject, resource refusal, missing
artifact, failed independent readback, or incomplete cancellation must not be
reported as success. The user's main Editor is preserved; tests use an owned
background Editor process.
