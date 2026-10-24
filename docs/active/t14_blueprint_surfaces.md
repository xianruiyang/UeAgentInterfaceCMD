# Blueprint Surfaces through the default SDK

To create a generic function graph in an existing asset, edit the always-exported
`graph_declarations` map with a readable name and `{ graph_kind: "function_graph" }`.
Import and read the refreshed workspace before querying `client.blueprint.node_candidates(...)`
for that new graph and adding its returned node name in a second ordinary import.
Export again only if the workspace was not refreshed. Graph-body
name/kind are read-only references; nodes, pins, edges and layout stay in the
body. Omit a function or macro declaration to remove that graph; leave its old,
unedited body files in the workspace. Removing a declaration while editing its
body is rejected before writing. Event and animation-specific graph protections
remain native. Changing a map key means remove plus create, not identity-preserving
rename; kind conversion is unsupported. To rename an existing ordinary Function or Macro,
keep its declaration key and add the optional business name, for example
`ComputeStatus: { graph_kind: "function_graph", name: "EvaluateStatus" }`.
The existing key selects the captured graph identity. The server applies native
reference updates to callers and local scope in the same Blueprint, then compiles,
saves and reloads within the existing atomic lifecycle. Do not edit body headers
or hidden files to repeat the rename. A fresh export uses the new readable key
and omits its redundant name. Native name conflicts and actual effects on external
Blueprint callers, child overrides or child members are rejected before writing.
When the host already enables MVVM, its native binding-reference and migration
effects are checked through an optional adapter; rename does not enable MVVM.
An unrelated dependency alone does not reject the rename. Ordinary K2 functions,
macros and members in Widget/Animation Blueprints use this same native rename path.
Protected or animation-specific graphs and cross-asset rename transactions remain
outside it. Macro instances keep their graph identity and signature.
MacroLibrary rename preserves native old-name redirectors for saved external imports.
Its save and checkpoint readback use the existing resident-package replacement policy:
native redirectors moved to Transient can otherwise keep the old package alive.
The same macro can reclaim its old name, including late-failure restoration.
Loaded external instances retain their object identities, unsaved edits and disk bytes
during rename and late restoration. A redirector keeps its old name bound to its
original graph. Creating a new graph with that name is rejected. A rename may reclaim
it only when the redirector points to that exact graph; another or unresolved target
rejects before writing with `blueprint_graph_name_identity_conflict`.
Taking another graph's old name requires explicit reference migration, which is not
supported. This name-identity conflict does not claim an external consumer was found.
Native identities remain server-owned; no extra files or manifest edits are needed.

For an existing dispatcher in an ordinary Blueprint, keep its `delegates` key and
add an optional `name` to rename it. Export omits an unchanged, repeated name.
The key retains the captured member identity; changing the key remains removal
and creation. Edit the dispatcher signature in that same declaration. Its native
signature-graph name and same-Blueprint Bind/Call references follow the rename;
do not edit hidden identities, `new_name`, or a second graph-name declaration.
The retired delegate `new_name` field is explicitly rejected before writing.
The same member document keeps its `variables` and `interfaces` collections;
editing one preserves the others. An omitted collection keeps its captured state; an empty
collection explicitly requests removal of its items. The dispatcher's derived
item state is hidden, leaving one editable name/signature declaration.
Name conflicts and actual native writes to external Blueprints reject before
the source is modified. Unrelated dependencies remain allowed. A dispatcher with
a RepNotify callback is ineligible because the native rename requires interactive
confirmation. Ordinary dispatcher rename preserves member, graph, node and Pin
identities, signature and connections through save/reload and late-failure
recovery. Widget and AnimBlueprint members use the same eligibility checks.

Rename an ordinary Blueprint variable by setting the optional `name` on its
exported `variables` entry. Keep the map key: captured member identity selects
the existing variable, and omitting `name` keeps its captured name. Variables and
dispatchers share this name/identity path; the retired variable `new_name` is
explicitly rejected before writing. Native rename preserves the member GUID,
copies the current CDO default value, and updates same-Blueprint Get/Set references.
Save/reload and late-failure restoration preserve defaults, identities, Pins and
connections. Actual dependent and child-conflict writes reject before source
modification; RepNotify-associated variables reject because the native operation
requires interactive confirmation.

Change a variable's exported `type` while keeping its map key and captured GUID.
The adapter applies native member flags and K2 reconstruction without an
interactive warning. Native reconstruction decides which connections survive,
migrate, disconnect or remain on orphan Pins; unchanged exported connections
are context and are not replayed over that result. Submit explicit connection
edits only when a different connection is intended. Native compile errors
remain failures, and the resulting member type and GUID are checked.

Loaded child Blueprints affected by native reconstruction participate in the
same capture, compilation, save/readback and failure restoration. Native
Set/Map type changes clear unsupported replication settings. This does not
rewrite arbitrary unloaded cross-asset consumers. Export again to obtain the
settled native graph and updated references.

Rename an existing Custom Event in an ordinary Blueprint by editing its exported
`event_name`. Keep the node key; its captured NodeGuid selects the original node.
The definition node remains the sole signature owner, and an omitted signature
keeps its current value. Native `OnRenameNode` and the existing compile phase
resolve same-Blueprint Call and CreateDelegate references by native function identity.
Unchanged caller names in a whole-body edit follow the settled native reference;
explicit caller retargeting retains its requested value. No `new_name` or hidden
identity edits are needed. Native event-name validation applies, including its
parent-function restrictions. Loaded external Call references that compilation
would change reject before writing, including changes that do not emit Modify
or dirty notifications. Persistent rename also rejects exact external CreateDelegate
references: native package replacement refreshes their cached names, even though
compilation alone does not. Unrelated dependencies remain allowed. Ordinary
Blueprint saves use the shared resident-package replacement policy so retained
references cannot prevent genuine source reload or checkpoint restoration.
Custom Event rename does not invoke
the graph/member rename broadcast or its MVVM migration path. Graph/node/Pin
identities, signature and links are preserved through save/reload and late-failure
restoration. Cross-asset reference migration and Widget/AnimBlueprint sources
remain outside this operation.

Omitting a member or a deletable Function/Macro declaration invokes the native
Blueprint removal lifecycle. Native ownership determines which derived graphs,
member nodes and connections disappear and which unresolved callers remain for
compiler diagnostics. Unchanged exported context must not recreate removed
objects or require manual removal of every dependent node.

Explicit caller and connection removals can still accompany producer removal in
the same workspace. The plan applies the complete removal set before compiling,
saving and reloading. Editing the body of a graph that is also removed is a
conflicting request. Native non-deletable graphs retain their deletion rules.

Member type changes reconstruct native consumers, including loaded child
Blueprints, and persist the affected packages through the common transaction.
Do not manually load unrelated package referencers just to satisfy an obsolete
preflight error. This does not promise automatic rewriting of arbitrary soft or
dynamic references; unresolved native compiler errors are reported and failed
transactions restore their captured state.


Use `workspace.import_changes()` for an exported existing-asset directory, or
`client.content_graph.import_inline(...)` / `import_file(...)` to initialize a
missing target. These SDK entries share the public `content_graph.import_workspace`
command; no Blueprint-specific apply method is public. Read or export the current
asset with the shared `content_graph.*` methods.

Use `client.query.command_search(...)` and `client.query.command_usage(...)` when the
generated method is not already known; `ueagentinterfacecmd` exposes the
same discovery path. T13 remains the sole carrier-loading and common recursive
initialization authority.

Submit one `uai.blueprint.edit/1` entry whose root type is
`/Script/Engine.Blueprint`. Import receives the target and source. For existing
directory workspaces, the hidden `.uai/workspace.hjson` manifest owns identity
and concurrency state. Inline/single-file initialization uses the server-owned
missing expectation; callers do not supply `expected_revision`.
The directory carrier may contain multiple recursive workspace documents, but only
the manifest-selected entry owns the target Blueprint mutation.

For a missing Actor Blueprint, pass the following complete document to
`client.content_graph.import_inline("/Game/Example/BP_New.BP_New", document)`:

```hjson
schema: "uai.blueprint.edit/1"
root: {
  type: "/Script/Engine.Blueprint"
  document: {
    operation: "create"
    target: { asset_path: "/Game/Example/BP_New", asset_kind: "actor_blueprint" }
    provider_extension: { parent_class: "/Script/Engine.Actor" }
  }
}
```

The outer target is the full object reference; `document.target.asset_path` is
its matching package. Other Blueprint parents use their actual class reference;
ordinary non-Actor Blueprint creation uses `asset_kind: "blueprint"`.

Edit ordinary root settings in the exported `properties.hjson`, preserving the
existing category, property-name key, and displayed `type`, and changing its
`value`. A root-only change needs no graph or Component edit. The public
`bRunConstructionScriptOnDrag` true-to-false workflow is verified through
compilation, independent disk reload, and re-export with the existing parent
and graph structure preserved. An unchanged workspace is rejected with
`hjson_import_no_explicit_changes`.

Semantic workspace updates include final readback in the shared transaction.
Saved-update recovery is verified after staging and after persisted reload,
including prior dirty settings, captured graph/Pin state, and the separate
original disk contents. For missing Actor Blueprint initialization, failures after
staging or persisted readback restore object, asset-registry, and disk absence.

For supported node and Component creation, call
`client.blueprint.node_candidates(...)` or
`client.blueprint.component_candidates(...)`. For an ordinary component-tree,
put the readable `name` selector directly in the new stable-map row alongside
its `parent`; the row key owns the instance name. Known writable initial values
may accompany that row as the shared `properties` descriptor array. When fields
are unknown, import the minimal row and read the refreshed property file.
Subsequent edits use the ordinary properties. Graph nodes retain their exported
graph-file candidate shape. The server-side format and examples are defined in
the plugin's `docs/active/t14_blueprint_surfaces.md`.
Do not derive class aliases, spawners, factories,
or duplicate native mutation fields. The server re-enumerates the same native
menu immediately before write and invokes the resolved native action.
The Blueprint node query validates public names for actual query matches.
Unmatched actions used only as name context do not block the result, and matched
invalid names retain their diagnostic. Native navigation actions are not node
creation candidates; genuine catalog enumeration/identity failures still fail.

For a local dispatcher, the verified Add/Remove chain queries
`node_candidates` with the matching Custom Event's `node_name` and
`pin_name="OutputDelegate"`. Put the returned name and the exported
`candidate_context: { node: "EventAlias", pin: "OutputDelegate" }` in the ordinary
new-node row. The native action connects the delegate Pin. Keep existing
connections when adding Remove, and connect Bind's `then` to Remove's `execute`
to place it after Bind. Background queries also support Add/Remove: omit
node/Pin context, use the returned name without `candidate_context`, and add
the ordinary delegate/execution connections explicitly. Query the complete
returned Remove name or `StatusChanged Remove` to narrow the result without
changing the limit. The plugin T14 example covers both workflows; Assign is
not covered by this validation.

To add a RuntimeVectorCurve user variable, add its readable member name and
`type: {pin_category: "/Script/Engine.RuntimeVectorCurve"}` to the exported
member collection, then import. Read the refreshed workspace to edit the generated CDO's
ordinary curve property. Use its centralized definition for XYZ keys, defaults,
extrapolation and embedded/external alternatives, and import through the
workspace handle. Inspect the refreshed curve to review the change. The `time`
coordinate is generic and acquires units only from the Blueprint's consumer.
This workflow does not provide a standalone UCurveVector asset route.

Check `result.ok` and the public import status. Successful semantic directory
import also reports `workspace_refresh`. The server owns compile/settle, save,
unload/reload, independent readback and failure cleanup; these are not separate
caller steps. Inspect refreshed HJSON as needed; runtime behavior still requires
appropriate runtime evidence. Unsupported roots,
mismatched identity, missing entry documents, stale asset or candidate
revisions, unresolved types, compile failures, or persistence failures are
terminal and do not fall back to a retired Blueprint handler.
