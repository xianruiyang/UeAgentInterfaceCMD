# T25 Rig Simulation/Spatial SDK Projection

Use the default generated `client.content_graph.structure(...)` method first to
read the exact existing runtime subject, its `runtime_non_persistent` revision,
component-local frame, evaluation clock, skeletal binding, and available bones.
Submit one `uai.rig_simulation_spatial.edit/1` document through
`client.content_graph.import_workspace(...)` with that exact revision. Use
`client.query.command_search(...)` and `client.query.command_detail(...)` when a method or
live contract is not already known; `uai-cli` exposes the same discovery path.
This tutorial does not maintain a task-specific helper or second command
catalog.

The SDK contains no HTTP route, Unreal business rule, retry, UE object access,
Actor or Component creation, pose writer, simulation loop, recursive
initialization, persistence, or cleanup implementation. Each generated method
forwards exactly one shared public command with the manifest contract hash.
`client.content_graph.export_workspace(...)` remains discoverable but is
explicitly rejected because runtime pose state has no persistent workspace.

The root is an existing `/Script/Engine.PoseableMeshComponent` created and
persisted through T26. The only supported operation is `update_runtime_pose`.
Copy the exact evaluation clock, component-local spatial frame, real bone
identities, transforms, and conversion evidence from the live contract and
readback. The complete request is preflighted before the first runtime write.

T13 remains the sole common recursive initialization authority. T25 registers
only the runtime pose-subject root contract and consumes that seam; it creates
no Actor, Component, skeletal asset, or package. Success reports `saved=false`,
`reloaded=false`, and `package_dirty=false`, then an independent structure
read confirms the runtime pose. Failure restores affected bones and the
original clean package state.
