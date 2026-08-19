# T29 Skin Weight Profile SDK and CLI

Import only `uai` and connect from one complete Connection TOML. The final
manifest generates the default `external` method:

```python
import uai

with uai.connect("connection.toml") as client:
    result = client.external.skin_weight_profile_import(
        "D:/fixtures/Alternate.fbx",
        "/Game/Characters/SK_Character.SK_Character",
        "Alternate",
        0,
    )
```

The generic form uses the same generated binding:

```python
result = client.execute(
    "external.skin_weight_profile.import",
    {
        "source_ref": "D:/fixtures/Alternate.fbx",
        "target_ref": "/Game/Characters/SK_Character.SK_Character",
        "profile_name": "Alternate",
        "lod_index": 0,
    },
)
```

The CLI forwards one identical request:

```text
uai-cli --connection connection.toml exec external.skin_weight_profile.import --params-json {"source_ref":"D:/fixtures/Alternate.fbx","target_ref":"/Game/Characters/SK_Character.SK_Character","profile_name":"Alternate","lod_index":0}
```

Use `client.query.command_search("skin weight profile import", limit=5)` and
then `client.query.command_detail(command_id, contract_hash)` to obtain the
exact parameter schema, named SDK form, CLI form, owner, and tutorial
references. Search is the only fuzzy step; execute the selected command ID and
hash unchanged.

The client does not select or call the UE importer, inspect skeletal meshes,
retry a write, persist assets, reload packages, or synthesize readback. Inspect
`Result.ok`; success requires `terminal_status=succeeded`, a persistence
receipt, ordered lifecycle phases, and the independent persisted
profile/source readback.
