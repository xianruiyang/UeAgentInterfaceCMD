# T30 Localization / StringTable SDK and CLI

Import only uai and connect through one complete Connection TOML. T30 has no Python-side parser,
route selector, retry loop, commandlet launcher, persistence workflow, or second state source.

When the route is not already known, discover it through
`client.query.command_search("localization or StringTable intent", limit=5)`, then inspect the
selected live contract with `client.query.command_detail(command_id, contract_hash)`. These query
calls are discovery only; invoke the returned public command through its generated SDK method.

## HJSON

~~~python
import json
import uai

target = "/Game/Localization/ST_UI.ST_UI"
document = json.dumps({
    "schema": "uai.string_table.edit/1",
    "root": {
        "type": "/Script/Engine.StringTable",
        "namespace": "UI",
        "entries": [{"key": "Start", "source": "Start"}],
    },
}, separators=(",", ":"))

with uai.connect("connection.toml") as client:
    result = client.content_graph.import_workspace(
        target,
        {"kind": "inline", "document": document},
        "absent",
        "authorization:string-table-create",
    )
~~~

The same command accepts single_file and directory sources. There is no domain
apply-file/apply-folder command. Existing targets require the exact current revision.
Localization items require operation=create|update|upsert|remove; StringTable input is a complete
replacement. Check Result.ok, then independently read the returned target/revision.

Export uses client.content_graph.export_workspace(target, workspace_path,
profile_id="llm_authoring"). Read-only diff/validate/query/report uses
client.content_graph.compound(target, input={"localization_capability":"...",
"parameters":{...}}).

## Managed Localization tools

~~~python
start = client.job.compile_build(
    "localization_owned_tool",
    "localization:Game",
    "policy:owned-tool:localization-compile-text/v1",
    {
        "execute": True,
        "allow_commandlet": True,
        "cultures": ["en", "fr"],
        "timeout_seconds": 300,
    },
)
operation_ref = start.payload["operation_ref"]
generation = start.payload["generation"]
snapshot = client.operation.resume(operation_ref, generation)
receipt = client.operation.receipt(operation_ref)
released = client.operation.release(operation_ref)
~~~

The other policies are localization-gather-text and localization-export-po under the same
policy:owned-tool:<name>/v1 form. PO export requires output_dir. execute=False returns a managed
plan. Status never advances work; resume must use the exact returned generation.

## Culture preview

~~~python
start = client.editor.session(
    "runtime_preview",
    "culture:fr",
    "policy:runtime-session:culture-preview/v1",
    {"culture": "fr", "restore_after": True, "scope": "session"},
)
~~~

Advance via operation.resume. The terminal signal records previous/requested/restored culture;
independently read localization.culture.read after terminal, then receipt and release the operation.

## PO import

~~~python
result = client.external.localization_po_import(
    "D:/Localization/fr/Game.po",
    "Game",
)
~~~

~~~text
uai-cli --connection connection.toml exec external.localization.po.import --params-json {"source_ref":"D:/Localization/fr/Game.po","target_ref":"Game"}
~~~

Use query.command.search only for discovery and query.command.detail(command_id, contract_hash) for
current fields and examples. Execute the selected ID/hash unchanged. A successful start is not a
terminal success; inspect typed Result/Error, managed reports, independent readback, and cleanup.
