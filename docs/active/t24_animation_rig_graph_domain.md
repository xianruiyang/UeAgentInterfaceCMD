# T24 Animation Rig Graph SDK Projection

Use the default generated `client.animation_rig_graph.candidates(...)` method
and the shared `client.content_graph.import_workspace(...)` HJSON ingress. Use
`client.command_search(...)` and `client.command_detail(...)` when the method
or current contract is not already known; `uai-cli` exposes the same discovery
path. This tutorial does not maintain a task-specific helper or second command
catalog.

The SDK contains no HTTP route, Unreal business rule, retry, target classifier,
parser, planner, RigVM writer, compile, save, or readback implementation. Each
generated method forwards exactly one public command with the manifest contract
hash. The server remains the only owner of
`uai.animation_rig_graph.edit/1`, candidate semantics, explicit space
contracts, persistence, failure state, and cleanup.

Use `client.animation_rig_graph.candidates(...)` with one persisted
ControlRigBlueprint, IKRigDefinition, IKRetargeter, or Skeleton identity. Copy
the returned exact candidate name, kind, binding revision, and placement-space
requirements unchanged. Obtain the target revision with
`client.content_graph.summary(...)`, then submit one document through
`client.content_graph.import_workspace(...)`.

T13 remains the sole common recursive initialization authority. T24 registers
only the Rig/IK/Skeleton root and owned/container initialization contracts and
consumes the T13 seam. Carrier loading and directory recursion remain in T13;
T24 consumes only the normalized `source.kind=resolved` document set, selects
exactly the declared `entry_file`, and rejects legacy top-level `carrier` and
`hjson_document` fields. Placement-bearing entries carry the exact `space_ref`,
parent, and transform context required by the selected native command.
Successful import compiles or validates through the domain owner, saves,
reloads, and returns independent content-graph readback. Invalid spaces,
candidates, revisions, targets, or unsupported creation fail before write or
roll back without residue.
