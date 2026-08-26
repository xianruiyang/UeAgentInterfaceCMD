# T16 Animation Blueprint SDK Projection

Use `client.content_graph.import_workspace(...)` as the only Animation
Blueprint HJSON ingress and use the shared readback methods for independent
persisted inspection. Before creating a State Machine or State, call
`client.animation.state_machine_candidates(...)`; the method is read-only and
forwards the public `animation.state_machine.candidates` command. Directory,
`single_file`, and `inline` sources all use the same import method and manifest,
path, hash, and exact entry-file boundaries. Use `client.query.command_search(...)`
and `client.query.command_detail(...)` when the method or current contract is not
already known; `uai-cli` exposes the same discovery path. This tutorial does
not maintain a task-specific helper or command catalog.

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

Candidate search takes the exact future target, one `surface`, and the same
optional `class_settings` used by import. Use `surface="animation_graph"` for
the parent StateMachine node and `surface="state_machine_graph"` for a child
State. Both surfaces are enumerated from a transient AnimBlueprint created by
the same `UAnimBlueprintFactory`; no persistent asset or editor window is
created. Prefer exact candidate `id`, paginate while `has_more` is true, and
inspect `supported`, `write_support`, `coverage_complete`, and
`creation_coverage_complete`. Plain State is currently writable; sibling State
Machine actions such as Alias, Conduit and Comment remain search-only.

In HJSON put only `candidate: {id: ...}` or a unique
`candidate: {name: ...}` inside each StateMachine/State item. Keep the item
`name`, `animation_graph`, `pos_x/pos_y`, `entry_state`, and `transitions`
outside candidate. If both name and id are present they must select the same
native action. A known `class` is only an assertion. Transitions are relations
created through the native State Machine schema connection path and are not
candidate entries. Preflight and commit both re-enumerate the same native owner
before mutation.

T16 reuses the verified T14 common Blueprint surfaces. T13 remains the sole
common recursive initialization authority; T16 registers only Animation
Blueprint-specific root, graph, state-machine, state, transition, and class
setting contracts and consumes the T13 seam. Accept success only after normal
Animation Blueprint compile, save, unload, reload, and independent content-graph
readback. No non-HJSON animation command or retired owner is a fallback.
