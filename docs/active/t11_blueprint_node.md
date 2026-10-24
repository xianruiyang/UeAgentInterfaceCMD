# Blueprint node candidates through the default SDK

Discover the current method and parameter contract when they are not already known,
then query the exact owning Blueprint graph or pin-drag context:

```python
result = client.blueprint.node_candidates(
    target="/Game/Blueprints/BP_Example.BP_Example",
    graph_name="EventGraph",
    query="Branch",
)
names = result.payload["names"]
candidate_name = next(name for name in names if name == "If Then Else")
```

`Branch` is a native search label; the returned creation name in this example is `If Then Else`.
Candidate discovery returns the complete matching `names` array and one `scope`
containing `target` and `graph_name`. The service resolves the
returned name again in the current graph context and fails closed if it is not
unique; callers use the readable name and never copy internal identities. Select
the intended exact name from the returned list. Only refine when the service returns a
typed refine error.
Reuse names only in that scope and optional returned `candidate_context`.
When target, graph or pin context changes, query the needed names there; do not
reuse an Actor Blueprint menu as an Animation/Widget Blueprint menu.
Creation runs without menu-only opening, selection or Goto behavior; native
bindings and autowiring remain active. View/navigation actions do not create nodes.
Adding or removing members, components or widgets can change the current action catalog.
Refresh only the affected candidate names; an import ambiguity returns the current readable
`name` and minimal `choose`. Keep the name unchanged and use the chosen short
fields as `candidate.select` in a candidate envelope, or alongside `name` as
top-level `select` in an ordinary graph row. Class choices use short native class
names; component events distinguish their component binding this way.
The same interface function can expose both a direct call and a message node.
When `choose.node_class` distinguishes them, copy the returned short choice into
`select.node_class`; include a returned class source only when it is needed.
This applies to Actor, Widget and Animation Blueprint creation contexts alike.
When same-name alternatives use different semantic fields, `choose` is an array of
objects; copy the complete chosen object to `select`. For example, a generic `Add`
operator uses `operation_name`, while a collection function can use `function_name`.
Pin promotion determines the operator's concrete function; its registered
representative function is not a selection value.

Input-node ambiguities use native binding names: `input_key` for a key or hardware
axis, `input_action` for a legacy Action mapping, and `input_axis` for an Axis
mapping. For example, querying `W` can return `Input Key`; copy the returned
`choose.input_key` value `W` into `candidate.select` when creation asks for it.
The query text is not retained as a selector. Debug-key and scalar/vector axis
nodes use the same key-binding mechanism. Enhanced Input assets continue to use
their existing asset selection fields.
Read the created node's actual key or mapping through
`content_graph.items(..., input={"containers": [graph_name], "items": [node_name],
"fields": ["input_binding"]}, projection={"profile_id": "compact"})`.
Reuse the current graph and node aliases; if the service returns `choose`, copy
its compatible item selection while keeping the requested fields. The read-only
`input_binding` object contains the same semantic key/mapping fields, including
bindings omitted from editable property exports. Do not copy it into the writable
graph; creation still uses `candidate.name/select`.

`node_name`, `node_occurrence`, and `pin_name` describe an existing node/pin
drag context. They are not semantic filters for narrowing a creation query and
must not be supplied merely to reduce a successful name-list result.

Use `content_graph.structure(...).payload["entries"]`, select the intended
`graph_kind`, and pass its `name` unchanged as `graph_name`. Named graphs preserve
their authored HJSON name, including in Widget and Animation Blueprints. The server
resolves the graph and re-enumerates it for the candidate query; do not expose
or cache opaque graph identities.

Use that same structure for compact semantic readback of existing nodes. The
node entry reuses the Blueprint authoring state owner: events expose
`event_name`/`event_class`, component-bound events expose component and
delegate identity, function calls expose `function_name` and
`function_owner_class`, variable nodes expose `variable_name`/`access`, and macro instances
expose `macro_graph` with the actual local or external graph reference.
Select and verify by these fields and its public `name`; do not infer an
identity from position, count, edges, or the raw K2 class, and do not export a
full workspace only to recover these semantics.
For pin-drag context, exported node and pin aliases can be supplied directly as
`node_name` and `pin_name`. Existing semantic-name plus occurrence inputs remain
accepted; omit occurrences when selecting exact aliases. The service resolves the
full alias mapping rather than guessing a native name from an ordinal suffix.
If discovery uses this pin context, copy the returned `candidate_context` object
unchanged into the new node. It already contains the resolved public aliases:

```hjson
SprintSpeed: {
  candidate: { name: "Set Max Walk Speed" }
  candidate_context: { node: "CharacterMovement", pin: "CharacterMovement" }
}
```

Here `CharacterMovement` is an existing getter node and its exported output Pin
alias. The returned context is a sibling of `candidate`; do not reconstruct it
from native names or occurrence numbers. A name does not retain query context between calls.
The same rule applies to ordinary Blueprint, Widget and Animation graphs.

Within `candidate`, copy only the returned readable `name` and, when needed, the short semantic `select`
fields into `candidate` in the current workspace graph's `nodes` map.
Ordinary discovery does not return class paths, function owners,
event owners, provider metadata, or a complete candidate row:

```hjson
nodes: {
  BranchGate: {
    candidate: { name: "If Then Else" }
    pos: { x: 800, y: 600 }
  }
}
```

The retired `uai.blueprint.node.edit/1` schema has no runtime provider. Do not
construct or submit a node-specific HJSON root.
UMG ordinary workspaces reuse this candidate query and the same server-side
normalizer for new nodes in existing graphs; see T15 for the UMG workflow.

This is an addition to the exported graph file, not a replacement for its other
nodes. Use the name returned by the current candidate query; search text or menu
display labels need not be the returned name. The node map key is a local alias;
the workspace diff derives creation, update and removal without an `operation`
field. Optional pin context remains outside `candidate`. Do not copy the complete search
row or synthesize semantic, spawner or action metadata. `native_action_signature`
is deliberately not public. A copied semantic field is only an exact assertion
and cannot replace readable `name`/`select`; mismatch fails before write with
`blueprint_surface_node_candidate_metadata_mismatch`. The server re-enumerates
the same native Blueprint Action Menu and invokes the resolved
`FEdGraphSchemaAction::PerformAction` before applying explicit pins, edges or
properties.

The response-level `scope` is not a candidate selector; do not copy it into HJSON.
Use `workspace.import_changes()` on the same managed workspace; target identity
and concurrency state remain SDK/server-owned. Unknown, ambiguous,
stale or wrong-context selectors fail before persistent mutation.
Missing/ambiguous action diagnostics identify the requested name, target and current
graph/menu context, with the HJSON file/pointer/line location and corrective guidance.

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The equivalent CLI command ID is `blueprint.node.candidates`:

```text
ueagentinterfacecmd exec blueprint.node.candidates --params-json <json-object>
```
