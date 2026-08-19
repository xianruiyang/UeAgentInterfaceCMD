# T60 HJSON External-Input SDK Projection

Use the default generated `client.content_graph.import_workspace(...)` and
`client.content_graph.export_workspace(...)` methods. Discover their live
contracts with `client.command_search(...)` and `client.command_detail(...)`;
`uai-cli` exposes the same `command_search` and `command_detail` operations.
No task-local generated helper or second command catalog remains active.

Callers author one versioned `uai.hjson.external_input/1` document containing
the exact external source identity, format, SHA-256 digest, optional source
information, import options, and target policy. The target policy names one
T28-T30 importer command and carries only that command's target parameters.
The server validates family, command, digest, and target equality before
delegating to the single importer owner; the SDK does not build, translate, or
reinterpret the document.

T13 remains the sole common HJSON source-carrier, initialization, and recursive
composition authority. T60 consumes T13's normalized `source.kind=resolved`
document set and contributes only its server-side domain projection and
validation; it does not add a client parser, carrier loader, recursive
traversal, importer, retry, rollback, or cleanup path. Full export/import
round-trip is supported only for registered T28 object-backed factory results.
Skin Weight Profile and Localization remain explicitly import-only until their
public provenance contract supports export.
