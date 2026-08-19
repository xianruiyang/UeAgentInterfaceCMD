# T28 Factory Import SDK and CLI

Import only `uai` and connect from one complete Connection TOML. The final
manifest generates the default `external` methods for create imports and
`asset` methods for reimports:

```python
import uai

with uai.connect("connection.toml") as client:
    animation = client.external.fbx_animation_import(
        "D:/fixtures/Walk.fbx",
        "/Game/StrictV2/T28/Walk",
        "/Game/Characters/SK_Mannequin_Skeleton.SK_Mannequin_Skeleton",
        options={
            "import_materials": False,
            "import_textures": False,
            "create_physics_asset": False,
        },
    )
    sound = client.external.sound_wave_import(
        "D:/fixtures/OwnedSound.wav",
        "/Game/StrictV2/T28/OwnedSound",
        options={"replace_existing": False},
    )
    texture = client.asset.reimport_texture(
        "D:/fixtures/OwnedTexture.png",
        "/Game/StrictV2/T28/OwnedTexture.OwnedTexture",
        options={"replace_existing": True},
    )
    configured_texture = client.external.texture_import(
        "D:/fixtures/Mask.png",
        "/Game/StrictV2/T28/Mask",
        options={
            "srgb": False,
            "compression_settings": "TC_Masks",
            "mip_gen_settings": "TMGS_NoMipmaps",
            "lod_group": "TEXTUREGROUP_UI",
        },
    )
```

The generic and exact forms use the same generated catalog:

```python
result = client.execute(
    "external.sound_wave.import",
    {
        "source_ref": "D:/fixtures/OwnedSound.wav",
        "destination_ref": "/Game/StrictV2/T28/OwnedSound",
        "options": {"replace_existing": False},
    },
)
```

The CLI forwards one identical request:

```text
uai-cli --connection connection.toml exec external.texture.import --params-json {"source_ref":"D:/fixtures/T_Grid.png","destination_ref":"/Game/StrictV2/T28/T_Grid","options":{"replace_existing":false}}
uai-cli --connection connection.toml exec asset.reimport_texture --contract-hash sha256:<exact> --params-json {"source_ref":"D:/fixtures/T_Grid.png","target_ref":"/Game/StrictV2/T28/T_Grid.T_Grid","options":{"replace_existing":true}}
```

Use `client.query.command_search(intent, limit=...)` and then
`client.query.command_detail(command_id, contract_hash)` to obtain the exact
parameter schema, named SDK form, CLI form, owner, and tutorial references.
Search is the only fuzzy step; execute the selected identity and hash unchanged.

The client does not select a UE factory, rewrite identities or options, call
transport directly, retry a write, persist generated assets, or synthesize
readback. Inspect `Result.ok`; success requires the returned terminal receipt,
persistence receipt, and independent class/import-data/business-state readback.
Texture configuration and skeletal FBX Morph/LOD/material validation stay inside
the same `options` object and the same generated command binding; there are no
legacy `asset_import_*` methods or client-side compatibility mappings.
