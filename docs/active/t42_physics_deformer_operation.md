# Physics and deformer commands through the default SDK

The 15 active commands are entries in the default binding catalog. Start with
client.query.command_search(...) and client.query.command_detail(...) so command IDs,
parameter names, contract hashes, lifecycle, and failure codes come from the
running service rather than a copied task helper.

Default named methods:

```python
client.animation.deformer_graph_asset_create(...)
client.animation.deformer_graph_topology_apply(...)
client.animation.deformer_source_library_asset_create(...)
client.animation.deformer_source_library_bindings_apply(...)
client.animation.mesh_deformer_collection_asset_create(...)
client.animation.mesh_deformer_collection_entries_apply(...)
client.animation.ml_deformer_asset_create(...)
client.animation.ml_deformer_configuration_apply(...)
client.deformer.evaluation_sample(...)
client.deformer.geometry_sample(...)
client.deformer.training_inputs_validate(...)
client.physics.asset_structure_replace(...)
client.physics.constraint_update(...)
client.physics.material_update(...)
client.physics.simulation_probe(...)
```

Each named method sends one exact request through the same catalog binding as
client.execute_exact(...). The equivalent exact CLI form is:

```text
uai-cli --connection connection.toml exec <command-id> --contract-hash <hash-from-command_detail> --params-json <json-object>
```

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

