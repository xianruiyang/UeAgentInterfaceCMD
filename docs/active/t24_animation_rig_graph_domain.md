# T24 Animation Rig Graph SDK Projection

Use the generated `client.animation_rig_graph.candidates(...)` method and the
shared `client.content_graph.import_workspace(...)` HJSON ingress. Use
`client.query.command_search(...)` and `client.query.command_detail(...)` when the
current command or tutorial contract is not already known; `uai-cli` exposes
the same discovery path. The SDK forwards one manifest-bound command and owns no
HTTP route, Unreal business rule, candidate registry, writer, compiler,
persistence, or readback implementation.

## Search

Pass one persisted ControlRigBlueprint identity to
`client.animation_rig_graph.candidates(target=..., query=...)`. The command
enumerates the native default RigVM graph menu in blank context. Use the compact
`candidate.id` for an exact selection, or `candidate.name` only when it is
unique in that context. The query result also reports `target_revision`,
`graph_name`, native/executable action counts, paging, and distinct search and
creation coverage.

Search coverage is currently complete only for the default-graph blank context.
Creation is intentionally partial: verified RigVM Unit spawners are writable;
other native action kinds remain visible with
`write_support/support_reason` and are rejected before write. Pin-drag and
selection-dependent menus are outside this claim. IKRigDefinition,
IKRetargeter, and Skeleton are T24 domain roots but are not accepted by this
candidate command.

## HJSON creation

Copy only the selected `name` or `id` into the RigVM create edit:

```hjson
edits: [{
  intent: create
  semantic_id: "rigvm_node:AddSpaces"
  value: {
    candidate: { id: "candidate:..." }
    position: { x: 240, y: 144 }
  }
}]
```

If `name` and `id` are both supplied they are conjunctive. Do not copy the
complete search result, `target_revision`, labels, categories, support text,
or legacy `binding_revision` into HJSON. `semantic_id` is the new instance
identity; `position` is graph placement. Known `script_struct_ref` and
`method` may be added beside `candidate` as assertions, not as replacement
selectors.

The server re-enumerates the same current menu during preflight and again at
commit, then invokes the selected native `PerformAction`. Successful import
compiles, saves, unloads/reloads, and returns independent content-graph
readback. Ambiguous/stale selectors, search-only actions, assertion mismatch,
invalid target/revision, compile failure, or persistence failure do not become
silent fallback writes.

## Shared lifecycle

T13 remains the sole workspace loader and recursive initialization authority.
T24 consumes only `source.kind=resolved`, selects the declared `entry_file`,
and rejects legacy top-level `carrier` and `hjson_document` fields. Control
Rig hierarchy, IK Rig, IK Retargeter, and Skeleton operations keep their own
explicit parent, transform, chain, and space contracts; the compact RigVM
candidate does not absorb those contexts.
