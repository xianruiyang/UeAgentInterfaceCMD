# T15 UMG/Widget SDK Projection

Use `client.content_graph.import_workspace(...)` as the only public Widget
Blueprint HJSON mutation ingress. Supply `source` as `inline`, `single_file`,
or `directory`; there is no UMG-specific apply method. Use the shared
content-graph read methods and export for persisted inspection. Use
`client.command_search(...)` and `client.command_detail(...)` when the current
method or contract is not already known; `uai-cli` exposes the same discovery
path.

The generated SDK forwards exactly one public command with its manifest
contract hash. It contains no HTTP route, Unreal business rule, retry, HJSON
parser, recursive initializer, Widget/Slot construction, layout, binding,
animation, compile, save, unload, reload, or readback implementation. The
server-side UMG provider remains the only Widget Blueprint content-graph owner.

Submit one `uai.umg.edit/1` entry document whose exact root type is
`/Script/UMGEditor.WidgetBlueprint`. Create uses
`expected_revision="missing"`; update and upsert copy the latest public
content-graph revision unchanged. Accept success only after terminal success
and independent readback of the intended widget tree, slots, properties,
bindings, animations, layout, and managed graphs.

T13 remains the sole carrier-loading and common recursive initialization
authority. It resolves the public source into a target-bound workspace and T15
consumes that normalized source; T15 does not reopen files or maintain a
parallel recursive path. Unsupported roots or creation roles, mismatched
identity, duplicate or missing entries, stale revisions, unresolved exact
identities, invalid hierarchy/bindings, and lifecycle failures are explicit
and leave no residue.
