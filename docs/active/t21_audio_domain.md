# T21 Audio SDK Projection

Use the default generated `client.audio.graph_candidates(...)` method and the
shared `client.content_graph.import_workspace(...)` HJSON ingress. Use
`client.query.command_search(...)` and `client.query.command_detail(...)` when the method
or current contract is not already known; `uai-cli` exposes the same discovery
path. This tutorial does not maintain a task-specific helper or second command
catalog.

The SDK contains no HTTP route, Unreal business rule, retry, target classifier,
parser, planner, compile, save, or readback implementation. Each generated
method forwards exactly one public command with the manifest contract hash. The
server remains the only owner of `uai.audio_graph.edit/1`, candidate semantics,
MetaSound/Sound Cue mechanics, persistence, failure state, and cleanup.

Use `client.audio.graph_candidates(...)` with one persisted MetaSoundSource or
SoundCue identity. For MetaSound, select the compact `id` (preferred) or a name
that is unique in that same target context; when both are supplied they must
identify the same candidate. The optional `id` query parameter re-resolves one
exact result through the server and requires no Python-side class map.

Put only that selector inside the MetaSound HJSON candidate:

```hjson
nodes: [{
  intent: create
  candidate: { id: "candidate:..." }
  position: { x: 384, y: 192 }
}]
```

Placement and optional known assertions remain outside `candidate`; the server
generates `node_guid` when it is omitted and resolves class/version immediately
before mutation. Then obtain the authoritative target revision through
`client.content_graph.summary(...)` and submit one `uai.audio_graph.edit/1`
document through `client.content_graph.import_workspace(...)`.

Inspect `coverage_scope`, `coverage_complete`, and
`creation_coverage_complete` before claiming editor-menu coverage. MetaSound
currently reports the partial `metasound_frontend_registry_loaded_classes`
surface and writes through the existing Builder owner; it is not native blank
menu equivalence. SoundCue remains the legacy loaded-class/full-binding
compatibility surface and must not be given the compact MetaSound HJSON shape.

T13 remains the sole common recursive initialization authority. T21 registers
only the audio root and owned/container initialization contracts and consumes
the T13 seam. Carrier loading and directory recursion remain in T13; T21
consumes only the normalized `source.kind=resolved` document set, selects
exactly the declared `entry_file`, and rejects legacy top-level `carrier` and
`hjson_document` fields. Successful import compiles or validates through the audio owner,
saves, reloads, and returns independent content-graph readback. Missing roots,
stale revisions, invalid candidates, unsupported root creation, or unregistered
operations fail before write or roll back without residue.
