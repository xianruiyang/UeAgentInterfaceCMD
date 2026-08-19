# T27 DataTable/CurveTable domain through the default SDK

Discover the current contracts with `client.command_search(...)` and
`client.command_detail(...)`, then use
`client.content_graph.import_workspace(...)`,
`client.content_graph.structure(...)` for the supported write/read pair, and
`client.content_graph.export_workspace(...)` for verified directory export.
Export publishes a semantically rebuilt `table.hjson` through the common
artifact publisher. `uai-cli ... exec <command-id>` uses the same hash. No
task-specific generated binding remains active.

T13 is the sole HJSON initialization and recursive composition authority. T27
consumes T13's normalized `source.kind=resolved` document set, registers only
DataTable/CurveTable root and owned-entry creation contracts, and delegates
stable row/key identity, source update, save/reload, and independent readback
to T37. Unsupported creation fails before write.
