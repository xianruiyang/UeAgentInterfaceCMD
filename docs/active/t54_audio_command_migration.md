# Audio commands through the default SDK

Discover current contracts with client.command_search(...) and
client.command_detail(...), then use:

```python
client.audio_media.asset_create(...)
client.metasound.graph_compile_settle(...)
client.metasound.graph_default_mutate(...)
client.metasound.graph_interface_mutate(...)
client.metasound.graph_link_mutate(...)
client.metasound.graph_node_mutate(...)
client.sound_cue.graph_compile_settle(...)
client.sound_cue.graph_node_mutate(...)
client.sound_cue.graph_relation_mutate(...)
client.sound_cue.graph_root_mutate(...)
```

The exact CLI uses uai-cli with the current command ID, hash, and one JSON
parameter object. No task-specific generated projection remains active.

Asset creation and MetaSound/SoundCue graph mutations use the common durable
operation lifecycle and native audio mechanics. Node, link, relation, root,
interface, default, parameter, source class, expected revision, and
compile/settle policy come only from command_detail. The SDK does not infer or
duplicate graph or audio behavior.

Success requires native compile/settle where declared, terminal projection,
and independent persisted readback after reload. Invalid class, graph, node,
link, relation, root, interface, default, or stale revision fails before
mutation. Unknown state requires reconciliation. Cleanup removes only owned
audio fixtures and verifies absence independently.

