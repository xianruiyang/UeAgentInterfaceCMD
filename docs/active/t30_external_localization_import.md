# T30 Localization / StringTable SDK and CLI

Import only uai and use `uai.connect_project()` for the local project. T30 has no Python-side parser,
route selector, retry loop, commandlet launcher, persistence workflow, or second state source.

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
Discovery does not execute the selected business command.

## HJSON

~~~python
import uai

target = "/Game/Localization/ST_UI.ST_UI"

with uai.connect_project() as client:
    workspace = client.content_graph.export_workspace(
        target,
        name="localization_ui",
    )
    # Edit only files below workspace.path.
    result = workspace.import_changes()
~~~

The SDK privately owns the absolute exported workspace path. There is no domain
apply-file/apply-folder command. The hidden `.uai/workspace.hjson` manifest owns
target identity, revision and authorization state.
For project LocalizationSettings, use `target="/Script/Localization.Default__LocalizationSettings"`
in the export call above. This identifies the native settings object, not a Content asset.
For an existing project LocalizationSettings target, edit its keyed `targets` entry in the exported
ordinary document. Change `native_culture`, `cultures`, or the exported typed values under `settings`
(native gather/export/compile configuration); omitted fields retain their captured values.
Unedited targets retain their native state, including an unconfigured native culture. For an edited
target, the native culture must belong to the effective culture set. Do not add an `operation` field or edit
configuration files directly. Add a new target key with `native_culture` and `cultures` to create a
project target; UE supplies its identity and publishes its native configuration and formal scripts.
For new targets, omitted culture fields use the current Editor culture. Removing a key from the
present `targets` object deletes that target, its native scripts and its complete localization data
directory; omitting `targets` preserves the collection. Trees or path ancestors containing symbolic
links or Windows reparse points are rejected before writing. A failed removal restores the original
target object and its in-memory settings, configuration, scripts and data tree.
For an existing StringTable,
edit the exported ordinary document's `namespace` and keyed `entries`: add or remove keys to change
the entry set. Entry keys are case-sensitive. Omitted fields on an existing entry preserve their
exported values; explicit `metadata` replaces the metadata object and `{}` clears it. Omitting
`entries` preserves the entry set, allowing a namespace-only edit. Do not edit hidden workspace files.
Check `result.ok` and inspect the refreshed workspace as needed. Revision and
persistence evidence stay inside the server-owned lifecycle and are not returned.

To initialize a missing StringTable, call `client.content_graph.import_inline(target, document)`
with HJSON text, or `client.content_graph.import_file(target, "relative/path.hjson")` with a
project-local file. Use schema `uai.string_table.edit/1` and a `root` containing
`type: "/Script/Engine.StringTable"`; `namespace` and keyed `entries` are optional. Omitted
namespace uses the native asset name, and omitted entries creates an empty table. Every supplied
entry needs a string source and may include string metadata. Initialization and subsequent directory
editing share the same entry semantics. Do not provide revision or authorization fields. After a
successful initialization, freshly export the target for further edits.

Export uses `client.content_graph.export_workspace(target, name=...,
profile_id="llm_authoring")`. Read-only diff/validate/query/report uses
client.content_graph.compound(target, input={"localization_capability":"...",
"parameters":{...}}).

## Managed Localization tools

~~~python
start = client.job.compile_build(
    "external_process",
    "localization:Game",
    "policy:owned-tool:localization-compile-text/v1",
    {
        "execute": True,
        "cultures": ["en", "fr"],
        "timeout_seconds": 300,
    },
)
handle = start.operation
generation = start.payload["generation"]
snapshot = handle.resume()
receipt = handle.receipt()
released = handle.release()
~~~

The other policies are localization-gather-text and localization-export-po under the same
policy:owned-tool:<name>/v1 form and `external_process` family. PO export requires a project-relative
`output_dir` and writes one native target PO file beneath each culture directory. `timeout_seconds`
is nonnegative; zero or omission allows the process to run to completion. execute=False returns a managed
plan. Advance until terminal, consume the structured report through `receipt.artifacts`, then release.
Status never advances work; the SDK handle carries the returned generation for resume.

## Culture preview

~~~python
start = client.editor.session(
    "runtime_preview",
    "culture:fr",
    "policy:runtime-session:culture-preview/v1",
    {"culture": "fr", "restore_after": True, "scope": "session"},
)
~~~

Use `start.operation.finish()` to collect the receipt and release custody. Its terminal
signal records previous/requested/restored culture; independently read localization.culture.read.

## PO import

~~~python
source = client.external_source.from_project("Localization/fr/Game.po")
result = client.external.localization_po_import(source, "Game")
~~~

The source handle owns the absolute filesystem path; model-facing calls use a
short project-relative source name. Raw CLI path forms are machine integration
surfaces and are not copied into model guidance.

Use query.command_search only for discovery, then query.command_usage for the minimal generated
SDK call. Execute the selected command name unchanged. A successful result contains terminal status
and the short target/culture, format, and importer/compiler/refresh business fields.
Receipts, hashes, paths, revisions, phase history, and full independent readback are internal
server evidence and are not model-facing result fields.
