# T23 Animation/Curve domain through the default SDK

Discover current contracts with `client.command_search(...)` and
`client.command_detail(...)`; then use
`client.content_graph.import_workspace(...)`,
`client.content_graph.structure(...)` for authoring and independent readback.
The shared `client.content_graph.export_workspace(...)` binding remains
discoverable, but T23 returns
`animation_curve_domain_export_not_registered` because this task does not
claim a lossless export projection. The exact CLI form is `uai-cli ... exec
<command-id>` with the returned hash. No task-specific binding is an active SDK
entry.

T13 is the sole HJSON initialization and recursive composition authority. T23
contributes its Animation/Curve domain contract and delegates curve, channel,
key, notify, compression, refresh, persistence, and readback to T56. The SDK
does not implement those mechanics; unsupported creation fails before write.
