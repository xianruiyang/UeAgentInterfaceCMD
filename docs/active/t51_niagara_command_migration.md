# Niagara commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
client.niagara.asset_duplicate(...)
client.niagara.compile_refresh_settle(...)
client.niagara.emitter_asset_create(...)
client.niagara.stack_issue_fix(...)
client.niagara.system_asset_create(...)
```

`asset_duplicate(source_ref, target_ref)` accepts a package path or its matching
top-level object path for the destination, for example `/Game/VFX/NS_Copy` or
`/Game/VFX/NS_Copy.NS_Copy`. Both identify the same new asset package. A subobject
or a different object name is not an asset creation target. The source accepts
the existing asset's package or object path. Existing destinations are preserved
and reported as already present.

`compile_refresh_settle(target_ref)` accepts the existing asset's package or
object path. Persistence uses the resolved asset package for either spelling.

A standalone Emitter compiles through UE's transient System instance using the
exposed version. Success covers that compile/settle and source persistence;
instance VM bytecode is not copied back to the definition. Independent stored
VM freshness on the definition is `not_applicable`, not `observed` or a compile
error. System instances and compilable standalone scripts retain their native
stored-state diagnostics; actual messages and Stack issues remain visible.

The exact CLI uses ueagentinterfacecmd with one command name and
one JSON parameter object. No task-specific generated projection remains.

These commands use one Niagara command owner and the common operation
lifecycle. `niagara.script.graph.apply`, `niagara.stack.apply`,
`niagara.renderer_event_parameter.apply`, and `niagara.stack.reorder` are
replaced public identities: they are absent from discovery, the formal
manifest, and the default SDK. Renderer event parameter editing and stack
ordering use Niagara HJSON authoring through the T18 domain provider and the
single `content_graph.import_workspace` public ingress. Their internal
operation kinds and native mechanics remain available to that provider;
`niagara.compound.apply` is now a dormant compatibility identity. Linked parameter
and stack desired state must be completed in the common Niagara HJSON profile;
the old typed command is not exposed by ordinary discovery or the named SDK. Its
handler remains available only through the central dormant compatibility path.
The SDK and command handler do not retain an alias, parse HJSON, or own a second
runtime; the provider consumes T13's common initialization and cleanup contracts.

Captured emitter struct properties now use the shared compact property path
described in T18. Standalone and unversioned System embedded `FixedBounds` cases
are verified; linked parameter, multi-version emitter, renderer, and data-interface
coverage remain separate obligations.

Use only the generated SDK signature for that command fields and declared
compile/settle policy. Success requires native compile/refresh/settle where
applicable, terminal projection, and independent persisted readback after
reload. Invalid class, graph, stack, renderer/event, parameter, source, or
stale internal state fails before mutation. Unknown state requires reconciliation.
Cleanup is bounded to owned Niagara fixtures and independently verified.
