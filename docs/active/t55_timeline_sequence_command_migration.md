# Timeline and sequence commands through the default SDK

Discover current contracts through client.command_search(...) and
client.command_detail(...), then use:

```python
client.timeline.sequence_create(...)
client.timeline.sequence_read(...)
client.timeline.sequence_structure_replace(...)
client.timeline.widget_animation_read(...)
```

The exact CLI uses uai-cli with the current command ID, hash, and one JSON
parameter object. No task-specific generated projection remains active.

Sequence creation and structure replacement use the common durable operation
lifecycle and native timeline/sequence mechanics. Sequence and Widget
Animation reads remain queries. Asset/binding/track/section/channel identity,
display rate, tick resolution, time/frame convention, expected revision, and
target path come only from command_detail; the SDK does not infer or convert
them silently.

Write success requires terminal projection and independent persisted readback
after reload. Invalid asset, binding, track, section, channel, timebase, frame,
or stale revision fails before mutation. Unknown state requires reconciliation.
Cleanup removes only owned sequence fixtures and verifies absence independently.

