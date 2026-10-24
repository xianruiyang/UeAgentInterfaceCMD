# T21 Audio SDK Projection

Use the default generated `client.audio.graph_candidates(...)` method and the
shared `workspace = client.content_graph.export_workspace(...)` handle,
then edit its ordinary HJSON files and call `workspace.import_changes()`. For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery). This tutorial does not maintain a task-specific helper or second command
catalog.

The SDK contains no HTTP route, Unreal business rule, retry, target classifier,
parser, planner, compile, save, or readback implementation. Each generated
method forwards exactly one public command with the manifest internal contract metadata. The
server remains the only owner of audio candidate semantics, MetaSound, SoundCue,
and SoundSubmix mechanics, validation/apply, persistence, failure state, and
cleanup. Existing SoundWave assets use the shared reflection workspace for
editable properties and native audio preview configuration. Creating or replacing
their binary audio source remains the external-input workflow; it is not an audio graph.

## Missing-root audio graph documents

Pass a complete document to `client.content_graph.import_inline(target, document)`
with a new full object target:

```hjson
schema: "uai.audio_graph.edit/1"
root: { type: "/Script/MetasoundEngine.MetaSoundSource", create: {} }
```

For SoundCue, use `root.type: "/Script/Engine.SoundCue"` in the same shape.
The server derives asset name/package and invokes the native factory/defaults;
no `root.operation` is needed for creation. Export before graph editing.
This domain's root types do not include SoundSubmix or MetaSound Patch.

Use `client.audio.graph_candidates(...)` with one persisted MetaSoundSource or
SoundCue identity when the current contract requires a server-resolved
candidate. For MetaSound, use the returned base name, with the short
`select` fields returned for an actual ambiguity. The server
re-enumerates the target context and fails closed on ambiguity.

Put that selector inside the exported graph's `candidate` object, retaining the
ordinary graph-local node keys and structure described in the
[Audio HJSON contract](../../../Plugins/UeAgentInterface/docs/active/t21_audio_domain.md).

Placement and optional known assertions remain outside `candidate`; the server
generates any native identity and resolves class/version immediately before
mutation. Submit edits through the `HjsonWorkspaceHandle.import_changes()`
returned by export; revision, absolute path, and identity stay in SDK/hidden
workspace custody.

Root property edits use the exported `categories` and compact `value` fields.
For a MetaSoundSource `SoundSubmixSends` entry, keep existing values and supply
only changed or added members; omitted members of a new entry receive native
defaults. Preserve the exported nested curve channel structure. The same
workspace import applies these properties and supports independent re-export.

For the declared Submix EQ preset, export its ordinary `Settings` property and
use the `EQBands` element template in `definitions` for the first or another
band. Import through the same workspace handle; an empty array clears bands.
This profile covers `USubmixEffectSubmixEQPreset`, not every audio preset.
Saving independently reloads settings and their native copy. Registered current
submix-chain target slots are rebound with their enabled state, preserving
non-target instances. Replacement and failure recovery reset target transient
DSP history; dynamic overrides, fading old chains, and non-enumerable external
instances are outside that restoration contract. See the
[server audio contract](../../../Plugins/UeAgentInterface/docs/active/t21_audio_domain.md)
for the exact lifecycle boundary.

SoundCue and MetaSound names results include a structured `diagnostics` warning
that states the partial catalog scope. MetaSound uses the frontend registry and
existing Builder owner; it does not claim native blank-menu equivalence. SoundCue and
SoundSubmix use their declared profiles; do not apply the compact MetaSound
HJSON shape to unrelated audio profiles.

T13 remains the sole common recursive initialization authority. T21 registers
only the audio root and owned/container initialization contracts and consumes
the T13 seam. Carrier loading and directory recursion remain in T13; T21
consumes only the normalized `source.kind=resolved` document set, selects
exactly the declared `entry_file`, and rejects legacy top-level `carrier` and
`hjson_document` fields. Export creates the compact authoring projection through
the shared workspace publisher. Import compiles or validates through the audio
domain owner, saves, reloads, and returns independent content-graph readback.
Missing roots, stale revisions, invalid candidates, unsupported profile fields,
or native contract failures fail before write or roll back without residue.
