# T17 Material domain SDK

Use the normal `uai.connect(connection.toml)` client and its default generated
bindings. Call `client.material.expression_candidates(...)` for the Material
candidate contract and `client.content_graph.import_workspace(...)` for the
shared HJSON ingress. These bindings forward one exact request without
transport selection, HJSON generation, Material mechanics, retry, or cleanup.

When a method is not already known, use `client.command_search(...)` to find
the current command and `client.command_detail(...)` to inspect its live
contract and example. The same discovery flow is available in `uai-cli`; this
tutorial does not maintain a task-specific helper or second command catalog.

Call `client.material.expression_candidates(...)` with the exact persisted Material or
Material Function object identity. Preserve the returned `candidate.name`,
`binding_revision`, and `target_revision` unchanged. Put the first two fields
in the expression edit's `value.candidate`, use the same `name` as
`value.class_ref`, and use `target_revision` as the import's expected revision.
Continue paging while `has_more` is true; display `label` is not a creation
identity. The old generic `reference.catalog_search` SDK binding is inactive
and must not be used as a Material fallback.

Call `client.content_graph.summary(...)` to obtain the current persisted revision. Preserve
that revision and the HJSON fields unchanged when calling
`client.content_graph.import_workspace(...)`. The server owns schema validation, Material
or Material Instance native operations, compile/settle, persistence, independent
readback, and typed prewrite failure semantics. T13 remains the sole common
source-carrier and recursive initialization authority; T17 consumes the
normalized `source.kind=resolved` document set, registers Material root and
owned expression contracts, and consumes the T13 initialization seam.

The default SDK also preserves the shared `content_graph.export_workspace`
identity, but the T17 server provider deliberately returns
`material_domain_export_not_registered`: no Material serializer is registered,
so the command must not be treated as a successful query or a verified export.

Material Import now consumes the shared domain HJSON authoring kit for resolved-source
validation, canonical capture, and result construction. Material remains the sole owner of
candidate validation and native graph mutation. A successful result is emitted only when the
native mutation returns its exact `reload:` persistence evidence and the independent content
graph capture reports `compile_status=valid`; the shared result includes
`mutation_applied`, `compile_settled`, `saved`, `reloaded`,
`persistence_receipt_id`, and `independent_readback`. Do not infer these lifecycle facts from
HTTP success or manufacture them in caller code.
