# T18 Niagara domain SDK

Use the normal `uai.connect(connection.toml)` client and its default generated
bindings. Call `client.niagara.module_candidates(...)` for the Niagara module
candidate contract and `client.content_graph.import_workspace(...)` for the
shared HJSON ingress. Each binding forwards one exact request without
transport selection, HJSON generation, Niagara mechanics, retry, persistence,
or cleanup.

When a method is not already known, use `client.command_search(...)` and
`client.command_detail(...)` to find and inspect its live contract. The same
discovery flow is available in `uai-cli`; this tutorial does not maintain a
task-specific helper or second command catalog.

Call `client.niagara.module_candidates(...)` with the exact persisted Niagara target and
its usage context. Preserve `candidate.name`, `binding_revision`, placement
contract, required context, and `target_revision` unchanged. The executable
name is the module asset path; a display label is never a creation identity.
Continue paging while `has_more` is true.

Call `client.content_graph.summary(...)` to obtain the current persisted revision. Preserve
that revision and the HJSON document unchanged when calling
`client.content_graph.import_workspace(...)`. New roots use the explicit create contract;
existing roots use exactly one supported `root.operation`. The server owns
schema validation, T13 recursive initialization dispatch, T51 native operations,
compile/settle, persistence, independent readback, typed prewrite failures,
and cleanup. T13 remains the sole common recursive initialization authority;
it also owns source-carrier resolution. T18 consumes the normalized
`source.kind=resolved` document set, registers Niagara domain contracts, and
consumes that seam.

The default SDK also preserves the shared `content_graph.export_workspace`
identity, but the T18 provider deliberately returns
`niagara_domain_export_not_registered`. No Niagara serializer is registered,
so that result must not be treated as a successful query or verified export.
