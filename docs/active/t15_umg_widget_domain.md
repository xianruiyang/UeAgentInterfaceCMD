# T15 UMG/Widget SDK Projection

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
rename; kind conversion is unsupported.
Native identities remain server-owned; no extra files or manifest edits are needed.


Use `workspace = client.content_graph.export_workspace(target, name="widgets")`
and `workspace.import_changes()` for public Widget Blueprint HJSON editing.
Edit only ordinary files under `workspace.path`; there is no UMG-specific apply method. Query the creation
surface for one target Widget Blueprint with
`client.umg.widget_candidates(target, query=...)`. Use the shared
content-graph read methods and export for persisted inspection. For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).

Each generated SDK method forwards exactly one public command with its
manifest internal contract metadata. It contains no HTTP route, Unreal business rule,
retry, candidate catalog, HJSON parser, recursive initializer, Widget/Slot
construction, layout, binding, animation, compile, save, unload, reload, or
readback implementation. The server-side UMG provider remains the only Widget
Blueprint content-graph owner.

For a missing-target `uai.umg.edit/1` create document, use
`client.content_graph.import_inline(target, document)`. Inline and single-file
sources initialize missing targets; existing targets require an exported directory
workspace and `workspace.import_changes()`, which retain the base revision and
hidden identity mapping. Existing-target inline input is rejected before apply.
The server compiles,
saves, unloads and reloads the Widget Blueprint, then performs final readback
inside the transaction before commit. A late rejection restores an absent
create target or the existing target's original dirty memory and disk artifacts.
Use the successful operation's persisted readback and workspace refresh result.
Export again only when new information or a new workspace baseline is needed.

The complete missing-root Widget Blueprint document is:

```hjson
schema: "uai.umg.edit/1"
root: {
  type: "/Script/UMGEditor.WidgetBlueprint"
  document: {
    operation: "create"
    target: { asset_path: "/Game/Example/WBP_New", asset_kind: "widget_blueprint" }
    provider_extension: { parent_class: "/Script/UMG.UserWidget" }
  }
}
```

Pass it to `client.content_graph.import_inline("/Game/Example/WBP_New.WBP_New", document)`.
The target package and object reference must match. `parent_class` is optional
and defaults to native UserWidget; then export for ordinary content editing.

The default candidate response contains target-bound names and one query `scope`, deduplicated
without synthetic scope suffixes. Copy just the readable
`name: ...` into a new entry of the ordinary `widgets` map. The shared server
projection creates the internal `candidate: {name: ...}` binding; keep widget key,
parent and index outside the candidate. `class` is optional assertion data,
not a required creation binding. Loaded ordinary native widgets such as Button
and TextBlock are the writable slice. Optional `describe={"name": "<returned name>"}`
reports `description.creation.supported/reason` even for unsupported actions,
without creating a widget. Supported native widgets also expose writable defaults.
The response carries a structured `diagnostics` warning describing the partial
loaded-widget catalog; it does not claim complete native Designer Palette coverage.

For `candidate_ambiguous`, use the returned `name` and minimal `choose` to retry
with `select`. `candidate_selector_invalid` preserves current recovery data in
`Result.error`; the SDK does not resolve candidates itself. UMG's `form` values
distinguish `native widget` and `widget blueprint`; unavailable semantic distinctions
and unsupported creation remain explicit failures.

The ordinary `widgets` map is complete desired state: existing keys retain captured
identity, new keys name new instances, and omitted keys request deletion. Edit the
exported document that contains this field; do not assume a fixed path for its readable
alias. Each widget's `properties.hjson` contains its own properties;
`slot/properties.hjson` contains its parent's layout-slot properties. These distinct
native objects may have identically named fields; edit them in their own documents.
Reparenting and wrapper insertion use the final tree in one import, including exchanges
between single-child panels. The same native slot class retains editable layout;
a different slot class uses its native layout. Border/BackgroundBlur mirror layout
changes to the parent through native synchronization.
`index` is an integer sibling position. Native bounds clamping is preserved;
conflicting final positions are diagnosed instead of silently accepting the last move.
The SDK owns workspace
identity and concurrency state.
Root Blueprint properties and generated-class defaults are also editable through
their exported ordinary property documents. Use the captured fields and keep
widget/slot properties in their own documents.
For existing Blueprint graph nodes, edit the exported pin property values and
the node's `pos`, import the workspace, and consume the returned readback/refresh.
The server reuses the Blueprint semantic projection for graph and class-default
changes. The ordinary `variables` map uses the same Blueprint member owner.
To create a variable, retain existing entries and add a readable key such as
`SdkCount: {type: {pin_category: "int"}, instance_editable: true,
default_property: {property_path: "SdkCount", value: 17}}`. No GUID is supplied.
After successful directory import, read the refreshed member fields and
generated-class default property in their captured documents. Other unverified
member forms remain outside this variable slice.
Edit the ordinary `bindings` map to create property-variable bindings, for example
`DisplayText_Text: {widget_name: "DisplayText", property_name: "Text",
binding_kind: "property_variable", source_variable_name: "SourceA"}` for an existing
TextBlock and compatible FText member. Binding records require no candidate.
Edit `source_variable_name` in the current workspace, import, and inspect its refreshed binding.
Keep the captured widget/property pair; remove the entry to delete its binding,
retaining other keys. Function bindings retain their native function contract
and are not established by this property-variable validation slice.
For an existing opacity animation, edit the ordinary `animations` map. Retain
animation and binding keys, navigate its returned track/section/channel maps,
and change a key's `value_lexeme` or exported `properties`, or the channel's
`default` object. Import with the same workspace handle and read its refreshed animation.
The server restores captured identities and uses the shared MovieScene value
owner; it preserves other sections and keys. Add an entry such as
`Added: {display_label: "Added animation"}` to create an empty animation with
native defaults. A new entry can also contain public scene settings and the common
`bindings`/`root_tracks` maps in the same import. For example,
`Added: {bindings: {Root: {binding_kind: "root_widget", object_ref: "", tracks: {}}}, root_tracks: {}}`
creates the animation with its root widget binding. Omitted settings use the new
native MovieScene defaults; no private clock identity is supplied. Read the refreshed
workspace before editing its returned track/section/channel/key defaults. Remove that entry to
delete the animation, retaining all other animation entries. No candidate, class
or GUID is required for this fixed native type. For a new property track, query
`client.timeline.track_candidates(target, animation_name="Timing", query="Float")`
using the exported animation name. Add the returned `name` to a new `root_tracks`
entry, import and read the refreshed track before adding sections and keys from native defaults.
For a bound property, also pass the exported `binding_kind`, `object_ref` and
native `property_path` to the candidate query. Use that same `property_path` in
the new track. The server resolves the leaf property and initializes its native
Vector dimensions, object class or enum context before creating section defaults.
For LevelSequence, omit `animation_name` and use the public object path as
`object_ref`; it shares the property-context candidate and track implementation.

Within an animation's `bindings` map, add a readable entry with
`binding_kind: "root_widget"` for the runtime UserWidget, or
`binding_kind: "widget", object_ref: "Button"` for the named Designer widget.
Use `binding_kind: "slot", object_ref: "Button"` for that widget's panel slot.
The Designer root panel is a `widget` binding, distinct from `root_widget`.
Create the binding with empty `tracks`, import, then read the refreshed binding before
adding its property tracks. Native possessable identities remain server-managed.
Deleting a Designer widget follows native UE deletion: its animation bindings and
tracks remain available even when their widget is missing. Remove the corresponding
entries from the animation's `bindings` map when those tracks should also be deleted.

Missing-target inline animation
initialization keeps its existing syntax and needs no caller-supplied GUID.
Existing animation entries also expose `display_rate` and `tick_resolution` (`numerator`/`denominator`)
and exact `playback_range` bounds. Change the exported `point.tick` using its
displayed rate, retaining the bound kind. Hidden context supplies clock identity.
Display-rate edits preserve key and section timing; playback edits change only
the native bounds. An inclusive playback upper bound persists as the equivalent
exclusive next tick; overflow, open, inverted or mismatched-clock playback ranges
fail before publication. New empty animations use the persistent empty range
`[0,0)` with native rate defaults. Tick-resolution edits use the shared native MovieScene
time migration after the other edits in the same request; input times use the exported rate.
For a new node in an existing graph, query
`client.blueprint.node_candidates(target, graph_name, query=...)` and
use its returned name in the new ordinary node entry. The server reuses the
Blueprint candidate normalizer and native action; no node type or GUID is supplied
by the caller. Read the refreshed workspace after creation for the settled pin interface and
native grid placement before editing existing values.
Successful import includes the server-owned persistence and independent readback of the intended
widget tree, slots, properties, bindings, animations, layout and managed graphs.
Inspect refreshed HJSON as needed; validate visual or runtime goals with the appropriate preview or PIE evidence.

T13 remains the sole carrier-loading and common recursive initialization
authority. It resolves the public source into a target-bound workspace and T15
consumes that normalized source; T15 does not reopen files or maintain a
parallel recursive path. Unsupported roots or creation roles, mismatched
identity, duplicate or missing entries, stale revisions, unresolved exact
identities, invalid hierarchy/bindings, and lifecycle failures are explicit
and leave no residue.
