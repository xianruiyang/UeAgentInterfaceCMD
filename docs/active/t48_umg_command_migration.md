# UMG commands through the default SDK

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
The normal SDK methods are:

```python
created = client.umg.asset_create(...)
events = client.umg.widget_events_discover(...)
```

The equivalent exact form uses ueagentinterfacecmd with the command name and one JSON
parameter object. The public client owns contract metadata; the SDK does not carry a task-specific
projection or duplicate widget construction/event reflection.

asset_create is a durable common operation and succeeds only after terminal
native projection plus independent persisted readback after reload.
widget_events_discover is read-only and reports its actual state layer. Use
`owner_item_ref="widget:<WidgetName>"` with the actual Widget name and the target
Widget Blueprint object path. A `stable_item_order` entry such as `item:<alias>`
is an ordering reference, not this command's event-owner selector. Use
only the current parent class, package, widget identity, and event fields;
nothing is guessed. Invalid inputs fail before mutation; reconcile an unknown
post-write state against the affected asset before continuing.

