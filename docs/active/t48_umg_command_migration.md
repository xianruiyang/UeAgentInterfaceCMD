# UMG commands through the default SDK

Use client.query.command_search(...) and client.query.command_detail(...) before invoking:

```python
created = client.umg.asset_create(...)
events = client.umg.widget_events_discover(...)
```

The equivalent exact form uses uai-cli with the command ID, current contract
hash, and one JSON parameter object. The SDK does not carry a task-specific
projection or duplicate widget construction/event reflection.

asset_create is a durable common operation and succeeds only after terminal
native projection plus independent persisted readback after reload.
widget_events_discover is read-only and reports its actual state layer. Use
only the current parent class, package, widget identity, and event fields;
nothing is guessed. Invalid inputs fail before mutation, unknown post-write
state requires reconciliation, and cleanup removes only the owned Widget
Blueprint fixture with independent absence verification.

