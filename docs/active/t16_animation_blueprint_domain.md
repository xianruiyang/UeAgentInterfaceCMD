# T16 Animation Blueprint SDK Projection

Ordinary Blueprint-family workspaces always include a `graph_declarations` map.
Add a readable graph name with `{ graph_kind: "function_graph" }` in that existing
collection document, then call the workspace handle's `import_changes()` and
export a fresh workspace. Query `blueprint.node_candidates` for the now-existing
graph before adding a returned node name to its ordinary `nodes` map in a second
import. Do not create extra graph files or edit the hidden manifest. The server
captures native graph/node/pin identity and owns creation replay.

The declaration owns graph name and kind; graph-body headers are read-only
references, while the body owns nodes, pins, edges and layout. Existing names and
kinds identify the captured graph. Omit a function or macro declaration to remove
it, leaving its unedited body files in place. Deletion combined with body edits
is rejected before writing. A changed map key means remove plus create; preserving
identity through rename or kind conversion is unsupported. Animation-specific
schemas retain their domain owner. This does not add animation-graph or
state-machine creation through the generic declaration map.


Use `client.content_graph.import_inline(target, document)` to initialize a missing
Animation Blueprint. For an existing asset, use `export_workspace(...)`, edit
the ordinary files, and call the returned handle's `import_changes()`. Export
again to an independent workspace for persisted inspection. Before creating a State Machine or State, call
`client.animation.state_machine_candidates(...)`; the method is read-only and
forwards the public `animation.state_machine.candidates` command. Existing assets
require their exported directory and server-owned mapping; inline and single-file
sources are for missing-target initialization. For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery). This tutorial does
not maintain a task-specific helper or command catalog.

The missing-target input is HJSON text containing `schema`, `root.type`, and
`root.document` with `operation: create`, `target.asset_path`, and
`provider_extension`. The SDK does not insert this wrapper. The complete example
is maintained in `Plugins/UeAgentInterface/docs/active/t16_animation_blueprint_domain.md`.

The SDK contains no HTTP route, Unreal business rule, retry, parser, planner,
Animation Blueprint graph/state-machine mutation, compile, save, unload,
reload, or readback implementation. Each generated method forwards exactly one
public command with the manifest internal contract metadata.

This revision supports one fully preflighted create of exact root type
`/Script/Engine.AnimBlueprint`. The document
declares class settings, optional shared Blueprint surfaces, animation graphs,
state machines, states, entry state, and transitions. Existing inline updates,
conduits, aliases, layer interfaces, and animation graph/state-machine topology
changes through this dedicated extension fail before persistent writes.
Existing Animation Blueprints consume common root properties, Blueprint members
and class defaults through ordinary workspaces. Ordinary node creation/deletion,
properties, pin defaults, pose connections, layout, and transition-rule graph
nodes use the shared Blueprint projector and prepared mutation with the native
K2-derived schema. Query `blueprint.node_candidates` for the captured graph,
including nested State and transition-rule graphs. State-machine topology
remains with the Animation owner; no second animation node format is required.
Locate nested graphs using the exported read-only `display_name`/`parent_graph`.
Pass `query_name` to node discovery when present, otherwise `name`; import
continues using the server's captured graph identity.
Generic structural updates require compile/save; unsupported non-persistent
structural requests reject before mutation. Early post-mutation failure and final
readback rejection use the common checkpoint to restore dirty memory and disk
independently.

Candidate search takes the exact future target, one `surface`, and the same
optional `class_settings` used by import. Use `surface="animation_graph"` for
the parent StateMachine node and `surface="state_machine_graph"` for a child
State. Both surfaces are enumerated from a transient AnimBlueprint created by
the same `UAnimBlueprintFactory`; no persistent asset or editor window is
created. Use the returned candidate `name` unchanged; the service re-enumerates
the current graph context and fails closed when it is missing or ambiguous.
For a character, `class_settings` binds `target_skeleton` to an existing Skeleton
object path, or supplies `preview_skeletal_mesh` so the native factory derives
its Skeleton. `parent_class` must be a creatable AnimInstance subclass.
Use `template=false` for this bound asset. `template=true` creates a
Skeleton-independent template and cannot include Skeleton or preview mesh.
The complete HJSON creation envelope and field contract are maintained in
`Plugins/UeAgentInterface/docs/active/t16_animation_blueprint_domain.md`.
Ordinary workspace class settings are separate from AnimInstance CDO properties;
existing Skeleton/template identity is read-only, while mutable settings retain
the Animation owner's native application and compatibility checks.
Use `describe={name, select?}` to inspect `description.creation.supported/reason`.
Plain State is currently writable; sibling State Machine actions such as Alias,
Conduit and Comment remain search-only and are included in matching name results.
Creation support does not determine catalog completeness; actual source-enumeration
gaps still return `candidate_catalog_incomplete`.

In HJSON put the returned readable `name` and, after an ambiguity, its short semantic
`select` fields inside each StateMachine/State candidate. Keep the item
`name`, `animation_graph`, `pos_x/pos_y`, `entry_state`, and `transitions`
outside candidate. A known `class` is only an assertion. Transitions are relations
created through the native State Machine schema connection path and are not
candidate entries. Preflight and commit both re-enumerate the same native owner
before mutation.

State-machine names are scoped to `animation_graph`, and state names to their
state machine. Do not repeat a named declaration within one scope; conflicting
identities are diagnosed before the target is created. Each transition item is
an independent native transition, so several items may share endpoints.

T16 reuses the verified T14 common Blueprint surfaces. T13 remains the sole
common recursive initialization authority; T16 registers only Animation
Blueprint-specific root, graph, state-machine, state, transition, and class
setting contracts and consumes the T13 seam. Accept success only after normal
Animation Blueprint compile, save, unload, reload, and independent content-graph
readback. Existing-workspace edits keep final readback inside the shared
transaction, restoring pre-import memory and package bytes on late rejection.
Missing-target creation verifies original structure after compile and reload;
a late failure removes the newly created target. No non-HJSON animation command
or retired owner is a fallback.

For an existing PoseDriver node, edit its ordinary exported
`Node.PoseTargets[*].CustomCurve`, then call the workspace handle's
`import_changes()` and inspect the refreshed workspace. Use the RichCurve contract
in the centralized definitions for enum values and key fields. Preserve the
other keys, tangents and extrapolation when making a local edit. The key `time`
coordinate is an activation-weight input, not elapsed seconds; the curve output
is the mapped weight. New nodes and connections use the same ordinary graph
contract and context-sensitive candidates, rather than a reflected-property edit.
