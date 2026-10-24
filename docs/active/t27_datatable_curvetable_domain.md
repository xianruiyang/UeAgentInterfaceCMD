# T27 DataTable/CurveTable domain through the default SDK

For an existing DataTable, export a workspace and keep its handle:

```python
workspace = client.content_graph.export_workspace(target, name="table-edit")
# Edit the visible HJSON under workspace.path.
result = workspace.import_changes()
```

Check the export and import results before continuing. Edit the exported
property and row structure directly; do not assume a fixed `table.hjson`
filename or modify hidden workspace metadata. Use the current generated
query methods or a fresh export to read back the result.

The SDK transports the workspace; parsing, row types, change planning and
persistence belong to the server. Current DataTable/CurveTable behavior and
remaining creation boundaries are documented in the
[plugin domain contract](../../../Plugins/UeAgentInterface/docs/active/t27_datatable_curvetable_domain.md).
See [SDK workspace usage](../PYTHON_SDK_AND_CLI.md) for file and inline input.
