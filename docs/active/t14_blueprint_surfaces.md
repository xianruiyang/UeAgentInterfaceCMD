# T14 Blueprint Surfaces SDK Projection

Use `client.content_graph.import_workspace(...)` as the only public Blueprint
HJSON mutation ingress. Supply its `source` as `inline`, `single_file`, or
`directory`; there is no Blueprint-specific apply method. Use the shared
content-graph read methods and `client.content_graph.export_workspace(...)` for
persisted inspection and export. Use `client.command_search(...)` and
`client.command_detail(...)` when the current method or contract is not already
known; `uai-cli` exposes the same discovery path.

The generated SDK forwards exactly one public command with its manifest
contract hash. It contains no HTTP route, Unreal business rule, retry, HJSON
parser, recursive initializer, Blueprint mutation, compile, save, unload,
reload, or readback implementation. The server-side Blueprint Surfaces
provider remains the only Blueprint-root content-graph read authority and the
only owner of ordinary Blueprint settings, parent, interfaces, class defaults,
members, component tree, and managed graphs, nodes, pins, and edges.

Submit one `uai.blueprint.edit/1` entry document whose root type is
`/Script/Engine.Blueprint`. Create uses `expected_revision="missing"`; update
and upsert copy the latest revision from a public content-graph read unchanged.
Accept success only when `terminal_status` is `succeeded`, then independently
read back every intended surface. The directory carrier may contain recursive
workspace documents, but only the manifest-selected entry document owns the
target Blueprint mutation.

T13 remains the sole carrier-loading and common recursive initialization
authority. It resolves the public source into a target-bound workspace and T14
consumes that normalized source; T14 does not reopen files or implement a
parallel directory walker. Unsupported roots or creation roles, mismatched
identity, duplicate or missing entries, stale revisions, unresolved type
identities, compile or persistence failures are explicit terminal failures and
do not fall back to a retired owner.
