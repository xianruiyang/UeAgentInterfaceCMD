# T29 Skin Weight Profile SDK and CLI

Import only `uai` and use `uai.connect_project()` for the local project. The final
manifest generates the default `external` method:

```python
import uai

with uai.connect_project() as client:
    result = client.external.skin_weight_profile_import(
        "fixtures/Alternate.fbx",
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
        "source_ref": "fixtures/Alternate.fbx",
        "target_ref": "/Game/Characters/SK_Character.SK_Character",
        "profile_name": "Alternate",
        "lod_index": 0,
    },
)
```

The SDK resolves the short project-relative source privately. Raw CLI
absolute-path forms are machine integration surfaces and are not model guidance.

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery). Search matches only positive tokens from registered command names, registered
keywords and registered synonyms; execute the selected command name unchanged.

The client does not select or call the UE importer, inspect skeletal meshes,
retry a write, persist assets, reload packages, or synthesize readback. Inspect
`Result.ok`; successful unified import returns the short business result
`terminal_status`, `target_ref`, `asset_class`, `profile_name`,
`lod_index`, `profile_count`, and `reloaded`. Internal persisted profile/source
readback, receipts, hashes, revisions, lifecycle history, and package identity
remain server evidence. Use the domain query for detailed post-write state; it
is not part of the default import result.
