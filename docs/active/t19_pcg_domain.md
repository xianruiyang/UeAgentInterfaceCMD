# T19 PCG domain SDK projection

Use the default generated `client.pcg.node_candidates(...)` method to search
the target PCG Graph's native background context menu. The method accepts the
target, a bounded query, an optional exact candidate `id`, and pagination. Its
rows expose compact `id`/native menu `name` selectors plus presentation and
support metadata; they are not settings-class bindings. Search coverage and
creation coverage are reported separately because the complete background menu
is searchable while only the verified native-element action kind is currently
enabled for creation.

Use `candidate: {id: ...}` or a context-unique `candidate: {name: ...}` in the
owning `pcg.graph.apply` edit. Keep semantic node identity and `position`
outside the candidate. The server re-enumerates the same graph context during
preflight and commit and calls the selected native schema action; the SDK does
not construct or infer a settings class.

Use
`client.content_graph.import_workspace(...)` and the other default
`client.content_graph.*` methods to read or import an existing PCG Graph with
schema `uai.pcg.edit/1`. These bindings only forward the exact command ID,
params, and frozen binding hash; they contain no HTTP transport or Unreal/PCG
business mechanics.

Use `client.query.command_search(...)` and `client.query.command_detail(...)` when the
method or current contract is not already known. The same discovery path is
available in `uai-cli`; this tutorial does not own a task helper or second
command catalog.

T13 remains the sole common recursive initialization authority. T19 registers
only the PCG root, node, endpoint, and parameter initialization contracts and
consumes the T13 seam. T13 also owns every inline, single-file, and directory
carrier plus directory recursion; T19 consumes only the normalized
`source.kind=resolved` document set, selecting exactly its declared
`entry_file`, and rejects legacy top-level `carrier` or `hjson_document`
fields. Root creation is supported as a separate `expected_revision: "missing"`
import before any edit. Workspace export remains explicitly unavailable until
a complete round-trip export contract is registered.
