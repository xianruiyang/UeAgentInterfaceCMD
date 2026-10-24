# T20 AI Behavior HJSON domain

`ai-behavior-domain-owner` is the sole public owner for
`ai.behavior.candidates` and the `uai.ai_behavior.edit/1` domain. Discover candidates
with `client.ai.behavior_candidates(...)`. Obtain
`workspace = client.content_graph.export_workspace(...)`, edit its ordinary
HJSON files and call `workspace.import_changes()`. For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).

The shared source loader owns inline, single-file, and directory carriers. T20
consumes only the normalized `source.kind=resolved` document set and does not
accept legacy top-level `carrier` or `hjson_document` fields.

T13 remains the sole common recursive initialization authority. T20 registers
only AI Behavior root and owned-entry initialization contracts and consumes
that shared seam; it does not create another recursive dispatcher.

## Supported roots and native owners

| Root type | Create command | Mutation command |
| --- | --- | --- |
| `/Script/AIModule.BehaviorTree` | `ai.behavior_tree.asset.create` | `ai.behavior_tree.graph.apply` |
| `/Script/AIModule.BlackboardData` | `ai.blackboard.asset.create` | `ai.blackboard.schema.apply` |
| `/Script/AIModule.EnvQuery` | `ai.eqs.asset.create` | `ai.eqs.graph.apply` |
| `/Script/StateTreeModule.StateTree` | `ai.state_tree.asset.create` | `ai.state_tree.hierarchy.apply` |
| `/Script/SmartObjectsModule.SmartObjectDefinition` | `ai.smart_object_definition.asset.create` | `ai.smart_object_definition.apply` |

T20 owns root classification, target validation, candidate binding,
and lifecycle completion. It forwards one normalized request to the existing AI
command owner and does not duplicate graph planning, UE construction,
compilation/validation, persistence, reload, readback, or cleanup mechanics.

## Root lifecycle and edit shape

For a missing BehaviorTree destination, submit the complete domain document
with `client.content_graph.import_inline(target, document)`:

```hjson
schema: "uai.ai_behavior.edit/1"
root: {
  type: "/Script/AIModule.BehaviorTree"
  create: {}
}
```

The same envelope applies to the five root types in the table above. The public
target supplies the asset name and package path; conflicting declarations fail
before write. Creation contains `root.create` without a root `operation`.
Export the created root, then edit its ordinary workspace and import changes.
The hidden workspace manifest owns identity and concurrency state; the revision
used by the lifecycle is server-owned and is not part of the public success result.

Existing-root import uses the current exported workspace. The operation params
use each native command's stable item/relation/key/slot shape:
BehaviorTree nodes and hierarchy, Blackboard entries, EQS options and
generators, StateTree states and node placement, or SmartObject slots and
behavior definitions.

## SmartObject workspace

For existing SmartObject properties, export through the public workspace handle:

```python
workspace = client.content_graph.export_workspace(
    target, name="smart-object-edit", profile_id="llm_authoring")
# Edit the ordinary categorized HJSON files under workspace.path.
result = workspace.import_changes()
```

Check `result.ok` and read the refreshed workspace for the result. The ordinary `smart_object_items` collection uses readable
names and references; keep native IDs and the hidden workspace metadata out of
model editing. Existing slot, owned behavior and parameter properties share the
public value and property contracts. Parameter edits include native binding
propagation, and the shared Reflection transaction provides persistence and
failure recovery. Slot, owned behavior and definition-data rows also support
creation, deletion, ordering and readable parents. Use the query's original name
as the new row's top-level `name`, with optional `select`, `parent`, `index` and
initial `categories`; do not construct machine candidate IDs. Deleting a parent
also removes its unchanged owned children. Explicit child edits must retain a
surviving parent; they are not silently discarded.

For a SlotLinkAnnotation row, set `linked_slot` to an exported slot name or the
key of a new slot in the same import. Use `""` or `null` to clear it. Do not write
native slot IDs or indices. The link belongs in the structure row; the old empty
`data.LinkedSlot` property is no longer exported. Unchanged links follow native
handling when their target is deleted; a retained unresolved link has a readable
handle in the refreshed workspace. New or changed links need a surviving target.

See the Plugin's [SmartObject workspace contract](../../../Plugins/UeAgentInterface/docs/active/t20_ai_behavior_domain.md#smartobject-workspace)
for native parent restrictions, fixed owners, binding validation and unsupported type changes
and the loaded-native-types candidate coverage boundary. Names from an independent
export can also select the shared read APIs directly:

```python
client.content_graph.items(target, input={"items": [slot_name]})
client.content_graph.properties(
    target, {"owners": [slot_name], "fields": ["slot.bEnabled"]})
```

To add a property binding, query `Binding` and use the returned
name in an ordinary `smart_object_items` row:

```hjson
"Size Binding": {
  name: Binding
  source: Parameters
  source_path: Size
  target: "SDK Slot"
  target_path: Offset.X
}
```

Use the actual exported slot name and an existing compatible parameter. The
parameter bag's shared `schema` and `fields` can also add that parameter in the
same import. Edit an exported binding's paths to change it, or remove its row to
delete it. Read `slot.Offset` in the refreshed workspace to inspect propagation;
the public vector value is in `components`, while scalar values use `literal`.
Whole-struct/context sources with empty paths remain unsupported.

For a slot's WorldCondition, use its ordinary editable path as `target_path`,
such as `SelectionPreconditions.EditableConditions[0].Condition.TagQuery`.
The condition and compatible parameter can be added in the same import. Read
back the condition property and the exported binding; the runtime retargeted
path is server-owned and must not be authored as a second binding.

## Candidate-to-authoring chain

`ai.behavior.candidates` is read-only and target-sensitive. Its public filters
are `target` and optional text `query`. BehaviorTree also accepts
`parent` (an exported node alias) with `attachment_kind` (`service` or `decorator`).
For an existing CompositeDecorator's internal graph, pass `graph_owner` copied
directly from that graph's exported `owner` value. This context is exclusive with
`parent` and `attachment_kind`. Omitting all context fields selects the
blank-background menu. The BehaviorTree branch enumerates the selected native schema
menu without opening an asset editor and returns readable
names without adding scope prefixes. BehaviorTree candidate resolution uses the
shared exact-name selector; ambiguity returns readable `name/select` choices.
Selection fields describe the native kind, class name or readable source folders/module, and only the
shortest distinguishing fields are returned for correction.

For BehaviorTree, composite, task, service, decorator and CompositeDecorator menu
actions use the native creation action. CompositeDecorator creation also creates
its native default owned graph and Result node. Within that graph, native
AND/OR/NOT and decorator candidates use the same internal schema actions as the
editor menu. Auto Arrange and Add Comment remain search-only; other pin contexts
are not yet covered. Put only the selected readable `candidate.name` and,
when necessary, the short readable semantic `select` fields needed to disambiguate inside the candidate
object. Node identity, position, ownership, and relations remain in the
surrounding edit:

```hjson
nodes: {
  Focus1: {
    candidate: { name: "Default Focus" }
    parent: Wait1
    attachment_kind: service
    order: 0
  }
}
```

`Wait1` must be a parent alias in the same graph; it can be created in the same import.
For example, `client.ai.behavior_candidates(target, query="Default Focus", parent="Wait1", attachment_kind="service")`
returns the name consumed by this row. Query and import use the shared captured alias projection.
The domain resolves the readable selector during normalization, derives or
checks the carrier and payload types, then re-enumerates the same native context
immediately before commit and invokes the same schema action. An unresolved
same-name ambiguity fails closed. BehaviorTree relations use the native schema
connection path; the root must connect to a composite, not directly to a task.

BehaviorTree, Blackboard, EQS, StateTree, and SmartObject discovery share the
same name-list and query-`scope` public result. Their class, struct, signature, support and
revision metadata remain inside the owning context and are resolved again from
the readable selector before authoring. This does not claim that every catalog
is equivalent to its native editor menu; each owner still needs independent
coverage verification.

## Lifecycle and readback

BehaviorTree readback uses the domain native graph capture for nodes, recursive
subnodes, connections, placement and instance pins. The ordinary workspace export
now consumes graph/node/edge state and shared editable-property requests through
the common composition. It emits readable node/connection aliases, an interface
companion and categorized payload properties without exposing native node GUIDs.
Export does not create a graph for a newly created empty tree or save dirty state.
BehaviorTree semantic-directory import applies graph structure and payload
property changes through the shared Reflection authoring transaction, including
checkpoint, save/reload and final readback. The verified creation path uses an
intrinsic root row with `role: root`, native Selector/Wait candidate names and
readable connections; subsequent property and placement edits retain node identity
and compiled execution relationships. If final readback rejects after the Wait node has been
deleted and persisted, the lifecycle restores the complete dirty graph and the different
original disk bytes. A stale `select` rejects before mutation, while a valid native-class selection
reaches creation and persisted readback. `candidate_selector_invalid` leaves the graph unchanged,
and the queried readable name supplies the correction. Same-name BTTask Blueprints return readable
source choices; ambiguous ordinary import leaves the target unchanged, and both ordinary and
incremental imports consume the selected choice. Reloaded task classes match the selected Blueprint.
Existing decorator attachments appear in the same graph `nodes` collection, with
a readable `parent` node alias, `attachment_kind`, and zero-based typed `order`.
Removing a row deletes that attachment; changing `order` reorders the native
Decorator execution list. Generic SubNodes storage retains its independent order.
The attachment workspace test verifies deletion and reorder through ordinary
import, original-object release, clean reload, and compiled decorator order. It
also rejects a persisted attachment deletion at final readback and verifies the
complete dirty memory checkpoint and the different original disk bytes. Native
ownership capture uses persisted collections, not transient ParentNode links.
BehaviorTree attachments and EQS tests share persisted AIGraph ownership capture.
Single-node readback and full graph export carry the same parent reference;
top-level nodes omit `parent` rather than emitting an empty reference.
The ServiceContext test verifies a discovered Default Focus service created with a
new parent, original-object release and clean reload of native/compiled ownership.
Public SDK verification also covers adding it to an existing parent, rejecting an
invalid creation context and editing its Interval through the common property workspace.
For an existing attachment, attachment_kind describes its captured type and cannot
be changed in place; the public SDK rejection test verifies the graph remains unchanged.
Public SDK creation also covers a native Cooldown decorator on the same parent while
preserving its existing service.
Existing CompositeDecorator BoundGraphs export as separate graph files. Their
`owner` uses the common readable item reference, while node and pin aliases remain
local to each graph. Internal test properties use the common property files.
OwnedGraphWorkspace verifies ordinary And-to-Or and position edits, a Cooldown
property edit, original-object release, independent clean reload, and unchanged
main-graph state. It also rejects an internal test-node deletion after persistence
and verifies the complete dirty graph checkpoint and separate original disk bytes.
The same test also creates the outer CompositeDecorator with its new parent,
creates internal NOT and Cooldown nodes from queried names, and expands an OR
node from two inputs to three while connecting a newly created test to the new
input in the same import. AND/OR expose `pin_groups: { inputs: N }` with a minimum
of two inputs; the interface companion describes the current native group.
Result and NOT have fixed inputs. Keep the exported `interface_ref` when editing
the graph, and use the actual exported pin aliases for existing nodes.
The public SDK chain verifies outer creation, readable owner discovery, AND with
three Cooldown tests and connections, input shrink to two, and invalid input-count
rejection with the entire main and owned graphs unchanged. Removing the outer
CompositeDecorator row removes its owned graph while preserving the remaining
main graph. A separate public SDK check reparents an existing CompositeDecorator
from Wait to Selector. After import and independent export, its And with three
Cooldown nodes, connections, and all six graph property files remain unchanged,
including nondefault cooldown values 7.25, 9.5 and 12.75.
RunBehavior's native injected decorator previews retain their source Guid. The
capture scopes each preview to its parent task while keeping the original Guid
inside the checkpoint. Public rows have distinct readable aliases and
`read_only: true`; injected payloads do not expose writable property files.
Ordinary import rejects independent edits to these derived rows. InjectedWorkspace
verifies two tasks referencing one saved subtree, read-only edit rejection with
the full native graph unchanged, and a normal Wait position edit followed by
unload/reload with both previews preserved. It also creates a RunBehavior from
its native candidate, clears one existing source binding through the property
workspace, and verifies that only the corresponding preview disappears after
reload. Native graph initialization hydrates subtree caches inside the transaction;
the native refresh runs on both the isolated proposed tree and the live tree
before execution data is rebuilt. Candidate carrier types come from the native
action template, including RunBehavior's SubtreeTask.
A late-failure case deletes a bound parent and its preview, observes the clean
persisted deletion, then rejects final readback. The complete dirty graph and
the different original disk bytes are restored independently. Native Root
deletion restrictions remain intact.
InjectedCompositeWorkspace covers the same lifecycle with two native copies of
a CompositeDecorator containing an And and two Cooldown nodes. Each BoundGraph
exports separately with a readable owner; the graph and its inner nodes are
read-only. Derived payloads have no writable property files, variable input
interfaces disable adding/removing pins, and candidate creation in a read-only
graph is rejected. Independent inner-graph edits are rejected before mutation.
Capture preserves the native ownership distinction: ordinary BoundGraphs have
one SubGraphs registration, while injected copies have none and must be read-only
with the correct owning node. Normal parent edits, clearing one source reference,
and late-failure recovery of the remaining parent and inner graph are verified;
the editable OwnedGraphWorkspace regression remains passing.
The native-domain incremental graph entry now adapts its prepared
edits to the same domain graph document and Reflection transaction. Its result
oracle runs in the shared final-readback callback; its former independent
BehaviorTree save/rollback path is no longer used. The incremental lifecycle test
checks that the original asset is released before the persisted graph is read.

Success requires the native owner to finish mutation, native editor settle,
compile or domain validation, save, unload/reload, and independent `ContentGraphRead`
capture. Completion follows the native operation's result, not runtime readiness:
Behavior Tree and EQS `UpdateAsset` may produce empty runtime roots/options while
preserving a valid editable graph, and StateTree uses the native compiler's success
result. Actual compiler and structural errors still fail. Disconnected editor nodes
can be imported and saved first; query their instance `pin_interface` aliases before
adding connections in a later import. Successful editing does not establish that
the asset is ready to execute. The
public success result is a compact terminal-status projection; target identity,
revision, persistence receipt, and readback evidence
remain server-owned lifecycle facts. Unsupported roots or operations, stale
revisions, mismatched targets, invalid candidates, and lifecycle failures fail
without a legacy fallback. `content_graph.export_workspace` publishes the
registered Behavior Tree, State Tree, EQS, Blackboard or SmartObject reflection-authoring workspace.
EQS export includes editor option generators and enabled/disabled test children,
their parent/order/layout/connection data, and categorized properties. The latter
include EditDefaultsOnly fields exposed by the native EQS Details view.
EQS semantic-directory import projects the editor graph and property changes into
the complete EQS GraphDocument and the common Reflection apply/save/reload path.
Existing-test enable and property edits have persisted through independent reload.
Candidate discovery resolves exported option references with `attachment_kind: test`.
Returned generator/test names can be used unchanged for HJSON creation, including
a new generator and its test in one import. ActorsOfClass/Distance creation and a
new root connection have persisted through independent reload. The specialized
GraphCompound option/layout consumer also projects into the same complete graph
state and Reflection lifecycle; its former manual creation and separate apply
branch have been removed. A nonempty-graph creation test preserves existing tests
and properties through reload. Late rejection after deleting an option and its
tests restores the complete dirty graph and the original disk bytes independently.
For an empty asset, the first generator import includes the native schema's default
root in the planned graph state; export remains read-only. The public SDK chain
has created a generator/test, connected the root and retained edited properties
and a disabled test in re-export. Independent queries now consume the same shared
readable graph projection: `items` returns graph nodes without generic UObject
fragments, `relations` returns readable pin connections and test attachments, and
node names select items and properties. Pin interfaces are available on demand.

Behavior Tree and EQS queries share the canonical authoring graph projection and
the same item/relation assembly. Behavior Tree queries include both the main graph
and CompositeDecorator owned graphs, retain their declared owners and Blackboard
binding, and do not mix in generic internal UObject rows. Node aliases, connection
endpoints and `pin_interface` come from the same projection as workspace export.
Owned graph containers expose the workspace's readable `owner` reference; when the
native graph name is empty, that same reference is their selectable `name`.
Select the intended nodes before requesting their pin interfaces; binding items
and other item kinds do not acquire graph-node fields.
The SDK roundtrip and first query after Editor restart preserve the disabled test
and edited properties. These observations cover the ActorsOfClass/Distance slice.
StateTree uses `workspace = client.content_graph.export_workspace(...)`
and `workspace.import_changes()` for structure and property editing.
The server owns capture, identity resolution and the Reflection
save/reload transaction. See the Plugin's authoritative
[StateTree workspace contract](../../../Plugins/UeAgentInterface/docs/active/t20_ai_behavior_domain.md#statetree-workspace)
for supported edits, candidate inputs, lifecycle guarantees and evidence boundaries.
The SDK does not maintain a separate StateTree document or root-property-only path.
