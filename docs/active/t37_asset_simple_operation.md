# T37 Asset Operations SDK and CLI

Import only `uai` and connect from one complete Connection TOML. The final
manifest generates all 52 methods in the default `asset` namespace:

```python
import uai

with uai.connect("connection.toml") as client:
    sound_class = client.asset.sound_class_create(
        "/Game/StrictV2/T37/SC_Default.SC_Default"
    )
    render_target = client.asset.render_target_create(
        "/Game/StrictV2/T37/RT_Default.RT_Default"
    )
```

The generic form uses the same generated binding:

```python
result = client.execute(
    "asset.sound_class.create",
    {"target_ref": "/Game/StrictV2/T37/SC_Default.SC_Default"},
)
```

The CLI forwards one identical request:

```text
uai-cli --connection connection.toml exec asset.sound_class.create --params-json {"target_ref":"/Game/StrictV2/T37/SC_Default.SC_Default"}
```

Use `client.query.command_search("create sound class", limit=5)` and then
`client.query.command_detail(command_id, contract_hash)` to obtain the exact
schema, named SDK/CLI forms, owner, failure catalog, and tutorial references.
Search is the only fuzzy step; execute the selected ID and hash unchanged.

The client contains no HTTP implementation, retry, alias, registry fallback,
parameter remapping, persistence, rollback, or Unreal Engine business behavior.
Inspect `Result.ok` and the returned stable `operation_id` plus canonical
verified `projection`; `state_unknown` is never safe for automatic replay.
