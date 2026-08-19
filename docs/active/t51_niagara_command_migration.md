# Niagara commands through the default SDK

Discover the current contracts through client.command_search(...) and
client.command_detail(...), then use:

```python
client.niagara.asset_duplicate(...)
client.niagara.compile_refresh_settle(...)
client.niagara.compound_apply(...)
client.niagara.emitter_asset_create(...)
client.niagara.renderer_event_parameter_apply(...)
client.niagara.stack_issue_fix(...)
client.niagara.stack_reorder(...)
client.niagara.system_asset_create(...)
```

The exact CLI uses uai-cli with one command ID, the current contract hash, and
one JSON parameter object. No task-specific generated projection remains.

All eight commands use one Niagara command owner and the common operation
lifecycle. `niagara.script.graph.apply` and `niagara.stack.apply` are replaced
public identities: they are absent from discovery, the formal manifest, and
the default SDK. Niagara HJSON authoring uses the T18 domain provider behind
the single `content_graph.import_workspace` public ingress. The SDK and command
handler do not retain a compatibility alias, parse HJSON, or own a second
runtime; the provider consumes T13's common initialization and cleanup
contracts.

Use only command_detail fields, current expected revisions, and declared
compile/settle policy. Success requires native compile/refresh/settle where
applicable, terminal projection, and independent persisted readback after
reload. Invalid class, graph, stack, renderer/event, parameter, source, or
revision input fails before mutation. Unknown state requires reconciliation.
Cleanup is bounded to owned Niagara fixtures and independently verified.
