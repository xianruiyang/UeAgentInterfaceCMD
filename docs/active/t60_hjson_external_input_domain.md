# T60 HJSON External-Input SDK Projection

Use `client.content_graph.export_workspace(...)` to obtain a workspace handle,
then `workspace.import_changes()` to import edits to its ordinary HJSON files.
For an existing standalone HJSON document, use `client.content_graph.import_file`
or `import_inline`. The SDK deliberately does not expose a callable
`client.content_graph.import_workspace`; the exact server command remains the
shared import binding. Discover commands with `client.query.command_search(...)`
and consult the current SDK signatures for the appropriate source carrier.
No task-local generated helper or second command catalog remains active.

The current server consumes a versioned `uai.hjson.external_input/1` document
with source, format, options, and target policy. Prepare a new source without
importing it:

This is an explicit source/schema workflow. Exporting an existing asset without
`source` exports its ordinary asset workspace and applicable preview settings;
historical import provenance does not select the reimport workflow.

```python
workspace = client.content_graph.export_workspace(
    target, name="external-input",
    source={"kind": "inline", "document": document_text},
)
if not workspace.result.ok:
    raise RuntimeError(workspace.result.error)
# Edit only ordinary files below workspace.path, then:
result = workspace.import_changes()
```

The complete document uses `schema: uai.hjson.external_input/1` and a registered
root type, for example `uai.external_input.factory`. Its `root.external_input`
contains `source: {identity: "tmp/input.png", format: "png"}`, `options`, and
`target_policy: {command_id: "external.texture.import", parameters: {destination_ref: ...}}`.
The target parameter must match `target`. The server captures source integrity
in hidden workspace metadata; callers never provide or edit a digest. Changing
options declared by the selected importer is an ordinary edit. Changing source identity requires new preparation;
changed source bytes after preparation are rejected. Independent re-export or
query supplies the result readback, rather than the edited input document.

Factory options follow the selected command's native option record. Skin Weight
Profile and Localization currently use `options: {}`; Skin Weight profile name
and LOD are target parameters. Undeclared option fields are diagnosed before
mutation instead of silently ignored.

T13 remains the sole common HJSON source-carrier, initialization, and recursive
composition authority. T60 consumes T13's normalized sources and semantic
workspace resolver and contributes only its server-side domain projection and
validation; it does not add a client parser, carrier loader, recursive
traversal, importer, retry, rollback, or cleanup path. Full export/import
round-trip is supported only for registered T28 object-backed factory results.
Skin Weight Profile and Localization remain explicitly import-only until their
public provenance contract supports export.
