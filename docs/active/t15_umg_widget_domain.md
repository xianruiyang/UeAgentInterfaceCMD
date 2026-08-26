# T15 UMG/Widget SDK Projection

Use `client.content_graph.import_workspace(...)` as the only public Widget
Blueprint HJSON mutation ingress. Supply `source` as `inline`, `single_file`,
or `directory`; there is no UMG-specific apply method. Query the creation
surface for one target Widget Blueprint with
`client.umg.widget_candidates(target, query=..., limit=...)`. Use the shared
content-graph read methods and export for persisted inspection. Use
`client.query.command_search(...)` and `client.query.command_detail(...)` when the current
method or contract is not already known; `uai-cli` exposes the same discovery
path.

Each generated SDK method forwards exactly one public command with its
manifest contract hash. It contains no HTTP route, Unreal business rule,
retry, candidate catalog, HJSON parser, recursive initializer, Widget/Slot
construction, layout, binding, animation, compile, save, unload, reload, or
readback implementation. The server-side UMG provider remains the only Widget
Blueprint content-graph owner.

The candidate response is target/revision-bound. Use only an entry with
`supported: true`, copy just `candidate: {id: ...}` or the context-unique
`candidate: {name: ...}` into the widget create entry, and keep widget key,
parent and index outside the candidate. `class` is optional assertion data,
not a required creation binding. Both response coverage flags are currently
false: loaded ordinary native widgets such as Button and TextBlock are the
writable slice; the response is not the complete native Designer Palette.

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
