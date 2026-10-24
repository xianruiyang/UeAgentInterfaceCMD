# Physics and deformer commands through the default SDK

Start with command search and usage for current named SDK methods, parameters
and failure behavior. Compatibility registrations do not imply a named method.

Default named methods:

```python
client.animation.deformer_graph_asset_create(...)
client.animation.mesh_deformer_collection_asset_create(...)
client.deformer.evaluation_sample(...)
client.deformer.geometry_sample(...)
client.deformer.training_inputs_validate(...)
client.physics.simulation_probe(...)
```

Each named method uses the generated catalog binding. The corresponding CLI form is:

```text
ueagentinterfacecmd exec <command-name>  --params-json <json-object>
```

The typed Deformer topology operation is dormant and is not exposed as
`client.animation.deformer_graph_topology_apply`. Its comment-node behavior is
not a general node-creation contract. Use the public HJSON workspace path for
normal asset editing; support for a specific edit still requires its domain
implementation and readback, not merely a registered workspace provider.

Deformer Source Library is the native `UOptimusSource` asset. Query its readable
constructor with `asset.factory_candidates` using query `Optimus Source`, create through `asset.object_create`,
then edit `SourceText` and `AdditionalSources` in the exported HJSON workspace.
This uses the shared Reflection property/reference/persistence path. It does not
edit a component-binding table or compile a consuming Deformer graph.

ML Deformer configuration uses the native `MLDeformer Asset` factory candidate
and the ordinary HJSON workspace. Edit the exported `model_settings.value`
categories, including the skeletal mesh reference and model training settings.
The adapter preserves the existing Model type and ownership and uses shared
Details/ObjectApply and Reflection persistence. Changing training settings does
not run training, inference, or switch model types.

For an existing Deformer UpdateGraph, export with `content_graph.export_workspace`,
add a node to the ordinary `nodes` object using `candidate: {name: "Custom Compute Kernel"}`
for that native basic-node type, and import with `content_graph.import_workspace`. Position is optional
and defaults to the origin. Existing node positions appear as `pos: {x: ..., y: ...}`
and can be edited in the ordinary graph. The server resolves the native class and performs shared
persistence and final readback before commit; no class path or manually updated
machine manifest is required.

Custom Compute Kernel creation has passed independent disk reload/re-export while
preserving existing nodes and bindings. This does not establish full native menu
coverage or a Deformer candidate-query endpoint; `animation_rig_graph.candidates`
targets Control Rig. New nodes may include
`properties: [{property_path: "GroupSize", value: {fields: {X: 32, Y: 1, Z: 1}}}]`
in the same entry. Descriptors bind to the created native node and use shared
recursive apply and persisted-intent checks. After refresh, edit the exported
property file; no creation-only property fragment remains.
Editable root and existing-node properties use the common property path.
Custom Compute Kernel `GroupSize` has passed ordinary editing, independent disk
reload and re-export with other persistent state preserved. Edit its recursive
value as `value: {fields: {X: 32, Y: 1, Z: 1}}` in the exported property entry.
Adding a binding by copying an ordinary exported `InputBindingArray` entry and
editing its name has passed native input-Pin and shader-declaration updates,
independent reload and re-export. Recursive value wrappers are restored internally.
Use graph-local Pin aliases from the ordinary `*.interfaces.hjson` files in the
graph's `connections` array. Connection creation has passed public import, native
endpoint checks, independent reload and re-export, including nested input Pins.
Adding an input binding while retaining an existing connection has also passed
Pin reconstruction and independent persisted readback. A single import can also
add a binding and connect its new Pin: retain the exported input alias's group
prefix and use the new binding name. Both connections have passed independent
reload and re-export. To clear the root `Mesh` preview reference, set its ordinary
property entry to `value: null`. This has passed compile, independent reload and
re-export together with a `GroupSize` edit. Other creation categories remain incomplete.
Deletion followed by either pre-release
staging failure or post-reload final-readback rejection has verified recovery of
the dirty in-memory graph and the original disk package separately.

Asset creation and structure/configuration mutations use the common operation
lifecycle. Success is accepted only after the returned terminal projection and
an independent persisted readback agree. Evaluation, geometry, training-input,
and simulation probes keep their declared read-only state layer and do not
inherit persistence claims from mutations.

Geometry and physics payloads keep target identity, semantic_frame_id, unit,
basis evidence, and conversion chain explicit when the current contract
requires them. The SDK does not infer skeletal meshes, sample frames, physics
constraints, deformer topology, revisions, or cleanup targets. Prewrite
validation failures leave no residue; an unknown post-write state must be
reconciled rather than replayed. Remove owned fixtures through the public
destructive workflow and verify their absence independently.
