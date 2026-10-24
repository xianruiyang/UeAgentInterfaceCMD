# PIE flows

Use the project runner's `project_uai_client()` to obtain `client`. The SDK owns
operation progress, receipts, release, and cross-process recovery. UE executes
the timeline; Python does not implement gameplay or a resident command server.

```python
session = client.pie.start()          # initialization, pause, Current HJSON
print(session.snapshot)              # entry only; reading HJSON is optional
result = session.run([
    {"type": "capture_start", "name": "walk", "interval": 0.25,
     "source": "pie_output_surface", "format": "png"},
    {"type": "input_key", "key": "W", "event": "pressed"},
    {"type": "wait", "duration_ms": 2000},
    {"type": "input_key", "key": "W", "event": "released"},
    {"type": "wait", "duration_ms": 1000},
    {"type": "capture_stop", "name": "walk"},
])
print(result.payload)
# Each capture/frame's artifact_index selects result.artifacts[index].
# materialize to a caller-selected project-relative destination when needed.
session.close()                      # end PIE when the task is finished
```

To choose the actual game viewport size, use
`client.pie.start("ui-check", viewport_width=1920, viewport_height=1080)`.
Each dimension is a positive physical pixel count; omitted dimensions default to
1280 and 720. The active renderer's maximum texture dimension applies. These are
session settings, independent of desktop DPI and saved Editor Play window sizes.
`pie_output_surface` reports the real viewport/image size; it does not resize a
capture to satisfy a request. Closing the session restores the Play window
preferences that existed immediately before native PIE shutdown.

`run()` returns after the finite flow and pause/refresh attempt. Check `Result.ok`
and its `execution`, `results`, `snapshot`, and `diagnostics`. Failure retains
earlier values/images; it does not roll back game time or replay the flow.
Execution success is distinct from gameplay correctness and snapshot success.
Invalid static property paths/types are rejected before gameplay resumes; this
does not alter held input from the preceding successful flow. Dynamic array/map/set
membership is checked at its execution point, so earlier operations can create
the element. Cancellation is different: it clears the session's held input even
when received before resume. While paused, queued engine input is consumed when
gameplay next advances; clearing injection state does not invent a game tick.

Normal pause retains held keys/axes; explicitly release them in a subsequent
flow or close the session. Write waits in milliseconds (`duration_ms`). A wait
starts when it actually executes and completes after that much game time;
implicit following operations run after completion. Late dispatch never consumes
a later wait in advance. Optional `at_seconds` is an absolute game-time schedule
from this flow's start, so operations can run during a wait; equal eligible times
preserve declaration order. Legacy `duration` remains seconds for existing clients;
do not combine it with `duration_ms`. `execution.operation_times_ms` gives each
dispatched operation's `game_ms`, plus `wait_ms` and `completed_ms` for waits.
Screenshot
sets sample immediately, then at game-time intervals, and close automatically
at flow end. They do not extend the flow or capture during model think time.
Frame times are actual samples, not promises of exact engine-frame timing.
Active flows temporarily use UE's native CPU-throttling exemption so background
Editor execution is not reduced to its idle 3 FPS. The exemption ends with the
flow's terminal/cleanup path; it changes neither OS focus nor saved performance
settings. Native frame quantization and gameplay input processing still apply.
Startup keeps the world paused across a fresh unthrottled Editor frame, then
dispatches time-zero operations before the first resumed gameplay tick. A caller
does not need an extra delay merely to make a short initial key press observable.
Collections also expose an `overview` contact sheet through the same artifact
interface. Its thumbnails do not replace or reduce the original frames.
Artifact materialization reuses identical files and otherwise chooses a numbered
sibling by default; consume the returned file path. A local save failure does
not interrupt the completed flow: retry saving that artifact, not `resume()`
or another capture. See `PYTHON_SDK_AND_CLI.md` for exact-path conflict handling.

For another process, `session = client.pie.recover()` resumes custody of the
same session. After an interrupted `run()`, call `session.resume()` to collect
that flow before submitting new actions. Do not replay an uncertain write.
The optional session `name` distinguishes independently managed sessions;
per-flow checkpoint names are SDK-owned.

The SDK persists the terminal receipt before releasing an operation. If the
client stops between server release and local cleanup, `resume()` returns the
saved flow result without replaying it; `close()` can finish cleanup as well.
Recovery requires the same Editor session. A connection error, an Editor-session
mismatch, or a missing operation without a saved receipt remains unconfirmed.
Keep that custody for diagnosis rather than replaying an uncertain flow.

Terminal observation failure uses the same failure cleanup as execution failure,
before publishing the next Current snapshot. Cleanup errors remain separate from
the primary failure; a failed result alone does not prove cleanup succeeded.

Every image reports `source`. Camera images include their actual `view_transform`,
`fov_degrees`, `projection`, and the requested camera alias when present.
Elapsed wait time alone does not prove settled exposure. Compare brightness under
the same source, view, and scene state; different capture sources are not a
controlled color comparison.
Collections report `frame_count`, `missed_frames`, `failed_frames`, and `gaps`.
Frames carry `sample_index`, `scheduled_seconds`, and actual `game_seconds`.
Late sampling skips missed slots on the original interval timeline and reports
them; it never creates duplicate images to fill time. A collection with gaps is
`partial`, even when the flow's operations themselves succeeded. A stopped
collection does not promise coverage beyond its requested end.

Capture submission, GPU readback and image publication are separate phases.
The world pauses at flow end while already submitted frames finish publishing;
that drain adds wall time, not game time. Collections and successive single
captures reuse idle capture resources within the flow.
`capture_in_flight` gaps mean the preceding frame was still being processed;
`sampling_delayed` means game time passed scheduled slots. Neither is filled by
repeated images. `game_seconds` records the submitted world state; per-frame
`submit_seconds` measures synchronous submission, `readback_seconds` is elapsed
submission-to-pixel-consumption latency (including ticker/terminal snapshot work,
not isolated GPU time), and `processing_seconds` measures background publication.

Property operations are optional. Copy a `ref` from Current HJSON:

```python
result = session.run([
    {"type": "property_get", "ref": ref},
    {"type": "wait", "duration_ms": 200},
    {"type": "property_set", "ref": ref, "value": new_value},
    {"type": "property_get", "ref": ref},
])
```

`ref` is `{alias, property, path}`. Path segments are `{field: name}`, `{index: n}`,
`{map_key: encoded_key}`, or `{set_value: encoded_value}`; values use the shared
property codec. Array indices mean execution-time positions. The operation target
uses a direct session alias, never an implicit chain that can switch targets.
Inside a property value, live world objects use `{alias: "..."}`; asset/class
references use the shared `{path: "..."}` shape. Unloaded soft paths remain lazy.
`null` or `{path: null}` clears a reference. The same rules apply inside containers;
an `unavailable` observation is not a writable reference.
After the native update, `property_set` verifies the explicit input using the same
property codec. A readback failure does not imply rollback; inspect the current
state before deciding whether to retry. A set element is selected by its value:
after editing it, subsequent operations must use the updated `set_value` selector.
Writing a reflected property does not implicitly invoke native behavior such as
character movement or teleportation. When gameplay maintains that state, judge
the result after gameplay advances, not only from an immediate read after write.

Current HJSON refreshes globally; the small returned reference update list tracks
used references and their necessary structure, not numeric changes. Use
`watch_refs=[ref]` / `unwatch_refs=[ref]` with `run()` for explicit interests.
Ordinary visual tests need no property operations or full snapshot reads.

Computer input uses the same timeline:

- `input_key`: UE key name, `pressed`, `released`, `repeat`, or scalar `axis`;
  mouse buttons also accept `double_click`.
- `input_pointer`: either `position: [x,y]` in the target PIE viewport's pixels
  (top-left origin, right/down positive), or one-shot `delta: [dx,dy]`.
- `input_scroll`: one-shot vertical wheel `delta`, positive upwards.
- `input_text`: Unicode `text` for the currently focused PIE text widget.

Held buttons plus pointer movement form dragging. Physical key events and text
are distinct. These routes do not move the OS cursor, change OS window focus,
or read the system clipboard. Horizontal wheel, touch, XR and operating-system
IME composition are not currently implemented routes.
Current HJSON's `root.input` reports held input, focus/capture facts and pointer
coordinates. Its `key_catalog_path` points to the separately stored UE key
catalog for on-demand lookup; registered device keys do not imply that every
hardware-specific route has been implemented.

Native operation details and capture-source parameters, including the exact
`scene_camera.view_transform` vector encoding, remain in the
[Plugin public contract](../../../Plugins/UeAgentInterface/docs/contracts/long_running_session_public_commands.md).
