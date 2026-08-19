# T20 AI Behavior SDK Projection

Use the default generated `client.ai.behavior_candidates(...)` method and the
shared `client.content_graph.import_workspace(...)` HJSON ingress. Use
`client.command_search(...)` and `client.command_detail(...)` when the method
or current contract is not already known; `uai-cli` exposes the same discovery
path. This tutorial does not maintain a task-specific helper or second command
catalog.

The module contains no HTTP route, Unreal business rule, retry, target classifier, parser, planner, compile, save, or readback implementation. Every helper forwards exactly one public command with the frozen contract hash. The server remains the only owner of `uai.ai_behavior.edit/1`, candidate semantics, Behavior/State Tree mechanics, persistence, failure state, and cleanup.

Use `client.ai.behavior_candidates(...)` with a persisted BehaviorTree,
BlackboardData, or StateTree identity. Copy `candidate.name`, `candidate.kind`,
and `candidate.binding_revision` unchanged into the matching authoring entry;
StateTree candidates may be Blueprint classes or native task, condition, and
evaluator structs. Use `client.content_graph.summary(...)` for the authoritative
revision, then `client.content_graph.import_workspace(...)` with one
`uai.ai_behavior.edit/1` document and that exact revision.

T13 remains the sole common recursive initialization authority. T20 registers
only the AI Behavior root and owned-entry initialization contracts and consumes
the T13 seam. Carrier loading and directory recursion remain in T13; T20
consumes only the normalized `source.kind=resolved` document set, selects
exactly the declared `entry_file`, and rejects legacy top-level `carrier` and
`hjson_document` fields.

BehaviorTree documents may combine node, service, decorator, relation, and `binding:blackboard_asset` edits in one operation. Blackboard documents use the key candidate contract, and StateTree documents use an exact node identity, owner-state identity, node class or struct, and placement. Treat the returned `saved`, `reloaded`, `terminal_status`, and `independent_readback` fields as the write receipt, then verify persistence with a separate content-graph read after an Editor restart. Do not retry a stale revision; read the current revision and rebuild the intended document.
