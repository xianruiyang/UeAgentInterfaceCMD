# T16 Animation Blueprint SDK Projection

Use `client.content_graph.import_workspace(...)` as the only Animation
Blueprint HJSON ingress and use the shared readback methods for independent
persisted inspection. Directory, `single_file`, and `inline` sources all use
this one method and the same manifest, path, hash, and exact entry-file
boundaries. Use
`client.command_search(...)` and `client.command_detail(...)` when the method
or current contract is not already known; `uai-cli` exposes the same discovery
path. This tutorial does not maintain a task-specific helper or command catalog.

The SDK contains no HTTP route, Unreal business rule, retry, parser, planner,
Animation Blueprint graph/state-machine mutation, compile, save, unload,
reload, or readback implementation. Each generated method forwards exactly one
public command with the manifest contract hash.

This revision supports one fully preflighted create of exact root type
`/Script/Engine.AnimBlueprint` with `expected_revision="missing"`. The document
declares class settings, optional shared Blueprint surfaces, animation graphs,
state machines, states, entry state, and transitions. Existing-target updates,
deletion, conduits, aliases, transition-rule graph authoring, layer interfaces,
and workspace export fail explicitly before persistent writes.

T16 reuses the verified T14 common Blueprint surfaces. T13 remains the sole
common recursive initialization authority; T16 registers only Animation
Blueprint-specific root, graph, state-machine, state, transition, and class
setting contracts and consumes the T13 seam. Accept success only after normal
Animation Blueprint compile, save, unload, reload, and independent content-graph
readback. No non-HJSON animation command or retired owner is a fallback.
