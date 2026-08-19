# Blueprint Component candidate SDK

Use the default generated binding
`client.blueprint.component_candidates(target=..., component_class=...,
requested_name=...)` for the exact `blueprint.component.candidates` contract.
The binding preserves all three arguments without translation. Copy the
returned candidate identity and `scs_revision` unchanged into the T12 HJSON
document, then call the default
`client.content_graph.import_workspace(...)` ingress.

When the method is not already known, use `client.command_search(...)` to find
the command and `client.command_detail(...)` to read its current contract and
example. The same discovery path is available from `uai-cli`; tutorials do not
maintain a second command catalog or a task-specific generated helper.

The default binding contains no transport selection, retry, HJSON generation,
SCS mechanics, or Unreal Engine business logic. The server owns candidate
validation, T13 recursive initialization-contract resolution, mutation,
persistence, reload, and typed failure semantics. T13 remains the sole common
source-carrier, initialization, and recursive traversal authority; T12 consumes
the normalized `source.kind=resolved` document set and only contributes the
Blueprint Component domain contract and SCS mechanics.

The retired ids `blueprint_add_component`, `blueprint_remove_component`, and
`blueprint_set_component_property` have no SDK binding and are not public
discovery results. `blueprint.component.events.discover` is a separate active
T47 contract and is not replaced by this T12 candidate surface.
