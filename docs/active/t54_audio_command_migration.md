# Audio commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
client.audio_media.asset_create(...)
client.metasound.graph_compile_settle(...)
client.sound_cue.graph_compile_settle(...)
```

The exact CLI uses ueagentinterfacecmd with the current command name and one JSON
parameter object. No task-specific generated projection remains active.

Asset creation and explicit MetaSound/SoundCue compile/settle use the common
durable operation lifecycle and native audio mechanics. Graph mutations are
authored through the shared `content_graph` export/import workflow; their
default/interface/link/node/relation/root operation kinds remain internal to
the Audio HJSON owner and are not generated SDK methods. Parameters, source
class and compile/settle policy come only from
the generated SDK signature for that command. The SDK does not infer or duplicate graph or audio behavior.

Success requires native compile/settle where declared, terminal projection,
and independent persisted readback after reload. Invalid class, graph, node,
link, relation, root, interface, default, or stale revision fails before
mutation. Unknown state requires reconciliation. Cleanup removes only owned
audio fixtures and verifies absence independently.
