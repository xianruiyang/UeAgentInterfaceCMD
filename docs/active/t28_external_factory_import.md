# T28 Factory Import SDK and CLI

Import only `uai` and use `uai.connect_project()` for the local project. The final
manifest generates the default `external` methods for create imports and
`asset` methods for reimports:

For a fresh import, the destination supplies the asset name independently of the
source filename (for example, `Mask.png` and `/Game/Textures/WallMask`). The
destination must not already exist. Use
`replace_existing=False` or omit it for a create import; `True` belongs to a
reimport route. The same rules apply when preparing a Factory HJSON workspace.
Generic texture, sound and light-profile formats follow the class-compatible
native UE import factories; specialized routes retain their native formats.
Reimports use the native automated mode and an unattended script scope, including
the Factory workspace path. They do not wait for import-option or painted-texture
confirmation dialogs. Supply the intended source and options in the request;
native failures are returned through the existing result and rollback paths.

```python
import uai

with uai.connect_project() as client:
    walk = client.external_source.from_project("fixtures/Walk.fbx")
    animation = client.external.fbx_animation_import(
        walk,
        "/Game/StrictV2/T28/Walk",
        "/Game/Characters/SK_Mannequin_Skeleton.SK_Mannequin_Skeleton",
        options={
            "import_materials": False,
            "import_textures": False,
            "create_physics_asset": False,
        },
    )
    sound = client.external.sound_wave_import(
        "fixtures/OwnedSound.wav",
        "/Game/StrictV2/T28/OwnedSound",
        options={"replace_existing": False},
    )
    texture = client.asset.reimport_texture(
        "fixtures/OwnedTexture.png",
        "/Game/StrictV2/T28/OwnedTexture.OwnedTexture",
        options={"replace_existing": True},
    )
    configured_texture = client.external.texture_import(
        "fixtures/Mask.png",
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
        "source_ref": "fixtures/OwnedSound.wav",
        "destination_ref": "/Game/StrictV2/T28/OwnedSound",
        "options": {"replace_existing": False},
    },
)
```

The normal SDK resolves short project-relative sources to absolute wire paths
privately. Raw CLI absolute-path forms are machine integration surfaces and are
not model guidance.

For unknown command names or parameter shapes, follow [public command discovery](../PYTHON_SDK_AND_CLI.md#command-discovery).
Search matches only positive tokens from registered command names, registered keywords and
registered synonyms; execute the selected generated SDK method unchanged.

The client does not select a UE factory, rewrite identities or options, call
transport directly, retry a write, persist generated assets, or synthesize
readback. Inspect `Result.ok`; a successful response contains a short
`command_id`/`terminal_status` pair and readable business `readback` (target,
asset class, state summary, relevant options, dependencies, and bounded counts).
Source paths and hashes, option fingerprints, plan/receipt identifiers, lifecycle phase
history, reload evidence, and full independent readback are internal machine
evidence and are not returned. Texture configuration and skeletal FBX
Morph/LOD/material validation stay inside the same `options` object and the same
generated command binding; there are no legacy `asset_import_*` methods or
client-side compatibility mappings.
