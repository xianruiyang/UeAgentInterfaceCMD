# T13 UObject/DataAsset SDK and CLI

Import only `uai` and use `uai.connect_project()` for the local project. The final
manifest generates the default `content_graph` namespace for the two T13
contracts:

The recursive schema creates an absent root. Pass its complete document through
the public inline helper, then export independently to inspect the result:

```python
import uai

with uai.connect_project() as client:
    result = client.content_graph.import_inline(
        "/Game/StrictV2/T13/DA_Recursive.DA_Recursive", document,
    )
    workspace = client.content_graph.export_workspace(
        "/Game/StrictV2/T13/DA_Recursive.DA_Recursive",
        name="dataasset",
    )
    # Edit the visible Category/type/value rows below workspace.path.
    result = workspace.import_changes()
```

`inline` and `single_file` are create-only carriers for a complete domain-authored
document with explicit schema and root type identity; the server supplies the missing
expectation. They are not shortcuts for workspace fragments; ordinary editing uses the
exported directory and its hidden manifest.

For the registered native recursive DataAsset, default export and directory
editing use the shared Reflection workspace. Root and owned descendant values
are editable through ordinary Category/type/value rows. Owned collection changes
use native candidate eligibility and the common property apply path; preserve
exported reference identities when retaining the existing shared or cyclic graph.
The Reflection profile does not enable generic asset creation.

For a dynamic Struct array, ordinary `definitions.hjson` exposes an independent
`value_definition.element_definition` reference and `element_template`, including
when the array is empty. Resolve the reference within that ordinary catalog and
copy the template into the array, selecting asset references according to the
field definitions. The template contains native defaults, not an existing item's
captured values or `instance` identity; nonempty arrays keep the same insertion
template. Existing owned items retain their exported instance keys.

A directory workspace must provide `.uai/workspace.hjson` using
`uai.content_graph.workspace/1`. It binds the exact `target_identity` and
`base_revision`, names `entry_file`, lists every managed `.hjson` file with its
server/exporter-owned integrity metadata, and declares the `references` closure. Paths are
absolute only inside SDK/server custody; the public handle exposes a short
project-relative path. Paths inside the manifest are relative to the workspace
root and cannot escape it. The server loads and
verifies the complete source before any UE write. Do not send the retired
top-level `carrier` or `hjson_document` fields.

Export uses the same namespace and exact target and returns a managed workspace handle:

```python
workspace = client.content_graph.export_workspace(
    "/Game/StrictV2/T13/DA_Recursive.DA_Recursive",
    name="dataasset",
    profile_id="llm_authoring",
)
```

Successful Import returns `status: succeeded`; semantic directory Import also
returns `workspace_refresh` and refreshes the standard HJSON and current baseline
in that workspace. Read the refreshed files for newly created items and changed
values. If `content_graph_import_applied_workspace_refresh_failed` is returned,
the asset was applied: export a fresh workspace instead of replaying the import.
The shared behavior belongs to [Plugin T13](../../../Plugins/UeAgentInterface/docs/active/t13_uobject_recursive_init.md).

The raw command/CLI wire still carries an absolute path internally, but it is a
machine integration surface rather than model guidance. Model-facing Python
must use the typed workspace handle and must not copy a path from a manifest,
receipt, error, or command detail.

Use `client.query.command_search(intent)` to discover command names and
`client.query.command_usage([...])` for the selected exact IDs' SDK examples.
Use `ueagentinterfacecmd describe <command-id>` for public parameter names and
available schemas; consult the owning domain contract for semantics. Search matches
only positive tokens from registered command names, registered keywords and registered
synonyms; call the selected generated SDK method unchanged. Machine identities
remain internal to the SDK and server.

The client contains no HJSON parser, type alias, provider selector, lifecycle
rule, retry loop, UE lookup, or mutation logic. Receipts, revisions, hashes and
independent verification remain hidden machine evidence. Read the refreshed workspace
for post-write state; use a separate query or export for observations not already present.

The recursive provider keeps the native root factory, requested object names,
real `Outer` hierarchy, owned-object construction, and post-creation reference
binding for its registered `UeAgentRecursiveDataAsset` and
`UeAgentRecursiveOwnedObject` types, without promising arbitrary DataAsset support.
Ordinary scalar and container values use the shared UObject property
codec/apply path; all root and descendant values are checked against the
registered native properties before root creation, and omitted fields retain
native constructor defaults. Before the
minimal success result is returned, the server compares the complete planned
node, `Outer`, reference, value, container, and default-subobject state against the
request, accepted plan and native class defaults after a real unload/reload.
Final result projection is part of that recoverable stage,
so a late rejection rolls the new asset back to object, registry, and disk
absence.

For directory edits, final readback remains inside the shared Reflection
operation. A late rejection restores the original in-memory values, persisted
package bytes and dirty state. Inspect the refreshed workspace after successful edits;
an independent export is needed only for a separate observation or refresh recovery.
