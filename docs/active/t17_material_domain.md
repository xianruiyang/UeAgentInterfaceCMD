# T17 Material domain SDK

## Missing-root initialization

Submit a complete document through `client.content_graph.import_inline(target, document)`.
For destination `/Game/Example/M_New.M_New`:

```hjson
schema: "uai.material.edit/1"
root: {
  type: "/Script/Engine.Material"
  create: {
    asset_name: "M_New"
    package_path: "/Game/Example"
  }
}
```

For MaterialFunction, use `/Script/Engine.MaterialFunction` and the matching
destination name. The domain derives `material_kind` from the root type.
MaterialInstanceConstant uses `/Script/Engine.MaterialInstanceConstant` and
also requires `parent_material_ref` in `root.create`, pointing to its existing
parent Material or Material Instance. The name and package fields must agree
with the independent destination argument.

Material authoring also accepts the mounted `/UeAgentInterface/Materials/`
namespace for maintaining the plugin's bundled materials. This is plugin source
content: normal user scene assets remain under `/Game`. It does not grant a
general writable `/Engine` or arbitrary-plugin namespace.

Layer and Blend use the public `asset.object.create` factory candidate; they
do not have this inline creation branch. Export a created asset before editing
its ordinary workspace.



Use the normal `uai.connect_project()` client and its default generated
bindings. Call `client.material.expression_candidates(...)` for the Material
candidate contract and `workspace.import_changes()` on the exported workspace
handle for the shared HJSON ingress. These bindings forward one exact request without
transport selection, HJSON generation, Material mechanics, retry, or cleanup.

When a method is not already known, use `client.query.command_search(...)` to
find the current command and `client.query.command_usage(...)` to inspect its
live contract and example. The same discovery flow is available in `ueagentinterfacecmd`;
this tutorial does not maintain a task-specific helper or second command
catalog.

Call `client.material.expression_candidates(...)` with the exact persisted
Material or Material Function and the native creation context: optional
`graph_name` and readable `pin_name`. Candidate search returns deduplicated
original names plus one response-level `scope`. The service re-enumerates the current graph on import;
a remaining same-name conflict returns `candidate_ambiguous` and readable
`choose` values. Retry that name with `select`; do not append a scope to it.
For this rejection, `result.error` directly contains `code`, `name`, and
`choose`. Copy the returned name and the selected field/value into the ordinary
HJSON candidate; no raw response or handler-detail parsing is required.

For an already selected candidate, request only needed creation properties with
`client.material.expression_candidates(target, describe={"name": "Scalar Parameter", "fields": ["DefaultValue", "ParameterName"]})`.
Optional `select` has the same meaning as creation. `description.properties`
is a writable `properties[]` descriptor array with native `property_path`, type
metadata and `value`; copy needed descriptors into a new node's inline
`properties` and edit the values. Defaults come from the native expression class and use
the same editable-field policy as export. They do not describe dynamic pins or
function-specific interfaces. Omit `describe` for the concise name-list search with shared `scope`;
existing nodes still use their actual exported properties.
Custom expression inputs belong to the graph interface: edit
`nodes.<alias>.custom_inputs`, or connect to `<CustomAlias>.<InputName>` to create
that input before connecting. The reflection `Inputs` member is managed and is
not a creation property descriptor.
The same [selected candidate property contract](candidate_properties.md) is used
by the other native-default consumers.

Put the returned `name` in the HJSON candidate. Add the short semantic fields needed to disambiguate
`select` fields only when the ambiguity response requires them. An invalidated
selection returns `candidate_selector_invalid` and the current choices when
ambiguity remains; if the name is now unique, retry it without `select`.
The service resolves it in the current native action. Add a node under the
ordinary graph's `nodes` with its readable `name` and `candidate: {name, select}`;
omit `select` when not needed. Preserve existing nodes and connections. Do not
copy internal `value` wrappers, class paths, or candidate binding context into
the ordinary document. Edit the exported semantic workspace as described below;
this is not a `root.edits` mutation. Do not copy a complete search row or
binding revision. The old
generic `reference.catalog_search` SDK binding is inactive and must not be used
as a Material fallback.

Export Material, Material Instance, Material Function, Material Layer, Material Layer
Blend, their three Function Instance types, or Material Parameter Collection with
`workspace = client.content_graph.export_workspace(target, name="material")` and
check `workspace.result.ok`. Edit only the readable graph aliases, properties and
connections under `workspace.path`, then call `workspace.import_changes()` and
check the returned result. Keep the hidden captured baseline unchanged. The common graph owner resolves the
visible document; the registered Material authoring owner adapts it to native
expressions, compiles, saves, reloads and reads back. Native object identity remains
machine-side.

Read the resulting node with
`client.content_graph.items(target, input={"items": [node_alias], "fields": ["name", "material_function", "pin_interface"]})`
for a function-call node, using its alias from the fresh ordinary export.
Check `result.ok` before reading the payload. `material_function` identifies the
actual assigned function asset; `pin_interface.pins[].alias` gives the current
Pin aliases used unchanged in HJSON connection endpoints. Do not derive aliases
from native names, empty labels or numeric suffixes.
Without explicit fields, the compact item result omits `pin_interface`.

Use the exported `categories` and property `value` fields for root and expression
edits. Keep their compact shape when appending container entries; omitted
members of new entries receive native defaults. A single workspace import can
combine these edits. Existing expression state and resolved connections are
preserved under the [Material domain contract](../../../Plugins/UeAgentInterface/docs/active/t17_material_domain.md).

The older single-document `root.graph`, sparse `root.edits`, and Instance `parameters`
array shapes are no longer write paths. Existing Material, Material Function and Material
Instance updates require the exported semantic directory and otherwise fail with
`material_domain_semantic_workspace_required`. Asset creation retains its initialization contract.
T13 remains the sole common source-carrier and recursive initialization authority.

For a Material Instance, edit the exported parameter item's `value`. An inherited
parameter becomes a local override when `authored_override` is also set to `true`.
Scalar, vector, double-vector, texture, texture-collection, font, runtime-virtual-texture,
sparse-volume-texture, static-switch and static-component-mask share this workflow;
parameter name, kind, association and index remain unchanged. Unedited parameters
keep their existing inheritance and overrides. Set `authored_override: false` to
clear a local override. A texture with `authored_override: true` and `value: null`
is an explicit null override, not inheritance. After import succeeds, inspect the refreshed workspace for
effective values and override state.
Values use the shared ordinary authoring forms: a scalar number, a four-component
vector array, a resource reference, or a boolean. Font and component-mask values
use their exported named fields. Keep the actual exported form and definitions.
Each parameter item's read-only `definition` points to its field types in
`definitions.hjson`; edit `values`, keeping this reference unchanged.

The shared `content_graph.export_workspace` identity publishes the registered
Material authoring workspace, and that semantic directory is the only graph update
surface for an existing Material or Material Function. Model-visible HJSON uses
readable aliases and names only; GUIDs, hashes, candidate ids, and class references
are not part of the public document.

An existing standalone Material Function uses this same workspace workflow.
Its FunctionOutput is an ordinary expression node; connections target the exported
pin names rather than a Material root output. The independent Function automation
case covers node addition, property edits, connections, rejection and persisted
readback. Public creation uses `client.asset.factory_candidates("asset.object.create", query=...)`
and `client.asset.object_create(...)` with the returned candidate name. Function,
Layer and Blend share the expression workflow. Their three Function Instance types
instead edit `Parent` and inherited parameter overrides through the workspace.

Material Parameter Collection exposes named `scalars` and `vectors` maps. New names
can start with `settings: {}`; edit the exported `DefaultValue` and `ParameterName`
descriptors, or remove an entry to delete it. Rename through `ParameterName` to retain
native parameter identity; the next export uses that name as the map key.

Material Attribute Layers nodes expose `layer_stack` in their graph entry. Material
Instances expose the same `layers` rows in their layer-stack property item, plus
`authored_override`. Both use the shared layer-stack adapter. Each exported row
contains a readable `instance` binding, `name`, `enabled`, `layer` and, where
applicable, `blend`. With the native layer tree enabled, `parent: null` identifies
a root row and `parent: "Entry1"` refers to a row from this export.

Keep each surviving row's `instance` when editing or moving it. Remove a row to
delete it; append a row without `instance` to create it. The native background
stays first. A newly created row receives its readable binding in the refreshed workspace;
use that fresh binding before assigning children to it. Layer and blend values
use the exported shared resource-reference form. For an Instance, set
`authored_override: true` to author its stack or `false` to restore inheritance.
Read the refreshed workspace after import for the resulting order and effective stack.
Renaming an inherited row or changing its layer/blend reference makes that row
local through UE's native unlink operation. Clearing the stack override restores
the parent stack, including its names and relationships.

Material Import consumes the shared domain HJSON authoring kit for resolved-source
validation, canonical capture, and result construction. The public import result is emitted
as the minimal `{"status":"succeeded"}` only after the authoring owner has completed native
mutation, compile/settle, save/reload, and internal independent content-graph capture. Those
lifecycle facts are not repeated in the shared result; use a separate query or export when
resulting state is needed.
