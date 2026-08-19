# T19 PCG domain SDK projection

Use the default generated `client.pcg.node_candidates(...)` method to obtain
exact PCG settings-class candidates. Use
`client.content_graph.import_workspace(...)` and the other default
`client.content_graph.*` methods to read or import an existing PCG Graph with
schema `uai.pcg.edit/1`. These bindings only forward the exact command ID,
params, and frozen binding hash; they contain no HTTP transport or Unreal/PCG
business mechanics.

Use `client.command_search(...)` and `client.command_detail(...)` when the
method or current contract is not already known. The same discovery path is
available in `uai-cli`; this tutorial does not own a task helper or second
command catalog.

T13 remains the sole common recursive initialization authority. T19 registers
only the PCG root, node, endpoint, and parameter initialization contracts and
consumes the T13 seam. T13 also owns every inline, single-file, and directory
carrier plus directory recursion; T19 consumes only the normalized
`source.kind=resolved` document set, selecting exactly its declared
`entry_file`, and rejects legacy top-level `carrier` or `hjson_document`
fields. Root creation and workspace export are explicitly
unsupported by the current native authority.
