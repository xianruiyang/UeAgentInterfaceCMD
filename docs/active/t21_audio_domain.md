# T21 Audio SDK Projection

Use the default generated `client.audio.graph_candidates(...)` method and the
shared `client.content_graph.import_workspace(...)` HJSON ingress. Use
`client.command_search(...)` and `client.command_detail(...)` when the method
or current contract is not already known; `uai-cli` exposes the same discovery
path. This tutorial does not maintain a task-specific helper or second command
catalog.

The SDK contains no HTTP route, Unreal business rule, retry, target classifier,
parser, planner, compile, save, or readback implementation. Each generated
method forwards exactly one public command with the manifest contract hash. The
server remains the only owner of `uai.audio_graph.edit/1`, candidate semantics,
MetaSound/Sound Cue mechanics, persistence, failure state, and cleanup.

Use `client.audio.graph_candidates(...)` with one persisted MetaSoundSource or
SoundCue identity. Copy the returned exact candidate name, kind, version, and
binding revision unchanged into the matching authoring entry. Then obtain the
authoritative target revision through `client.content_graph.summary(...)` and
submit one `uai.audio_graph.edit/1` document through
`client.content_graph.import_workspace(...)`.

T13 remains the sole common recursive initialization authority. T21 registers
only the audio root and owned/container initialization contracts and consumes
the T13 seam. Carrier loading and directory recursion remain in T13; T21
consumes only the normalized `source.kind=resolved` document set, selects
exactly the declared `entry_file`, and rejects legacy top-level `carrier` and
`hjson_document` fields. Successful import compiles or validates through the audio owner,
saves, reloads, and returns independent content-graph readback. Missing roots,
stale revisions, invalid candidates, unsupported root creation, or unregistered
operations fail before write or roll back without residue.
