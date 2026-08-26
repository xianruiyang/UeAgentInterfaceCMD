# Blueprint Surfaces through the default SDK

Use `client.content_graph.import_workspace(...)` as the only public Blueprint
HJSON mutation ingress. Supply `source` as `inline`, `single_file`, or
`directory`; no Blueprint-specific apply method is public. Read or export the
current asset with the shared `content_graph.*` methods.

Use `client.query.command_search(...)` and `client.query.command_detail(...)` when the
generated method or current hash is not already known; `uai-cli` exposes the
same discovery path. T13 remains the sole carrier-loading and common recursive
initialization authority.

Submit one `uai.blueprint.edit/1` entry whose root type is
`/Script/Engine.Blueprint`. Create uses `expected_revision="missing"`; update
and upsert copy the latest public content-graph revision unchanged. The
directory carrier may contain multiple recursive workspace documents, but only
the manifest-selected entry owns the target Blueprint mutation.

For supported node and Component creation, call
`client.blueprint.node_candidates(...)` or
`client.blueprint.component_candidates(...)` and place either
`candidate: {name: ...}` or `candidate: {id: ...}` in the corresponding HJSON
entry. The Component stable-map key owns the instance name; graph/pin and SCS
parent remain outer context. Do not derive class aliases, spawners, factories,
or duplicate native mutation fields. The server re-enumerates the same native
menu immediately before write and invokes the resolved native action.

Accept success only when `terminal_status` is `succeeded`, then independently
read back every intended setting, member, Component, graph, node, pin, edge, or
Widget-owned Blueprint graph. The server owns compile/settle, save,
unload/reload, persistence receipt, and failure cleanup. Unsupported roots,
mismatched identity, missing entry documents, stale asset or candidate
revisions, unresolved types, compile failures, or persistence failures are
terminal and do not fall back to a retired Blueprint handler.
