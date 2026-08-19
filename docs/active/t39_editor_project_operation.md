# T39 Editor Project SDK and CLI

Import only `uai` and connect from one complete Connection TOML. The final
manifest generates all seven methods in the default `editor_project` namespace:

```python
import uai

with uai.connect("connection.toml") as client:
    result = client.editor_project.config_section_update(
        changes=[
            {
                "field_id": "entries",
                "presence": "set",
                "value": {
                    "type_id": "uai.editor_project.config_entry_map.v1",
                    "canonical_value": {
                        "UAI_StrictV2_T39": "public-write",
                    },
                },
            }
        ],
        expected_revision=current_target_revision,
        target_ref=(
            "uai://editor-project/v1/config-section/game/"
            "%2FScript%2FEngineSettings.GeneralProjectSettings"
        ),
    )
```

The same namespace exposes the other typed profiles, including
`client.editor_project.string_table_update(...)`. `expected_revision` must come
from `target.read` on the matching active Query command immediately before the
write; it is not a literal from this tutorial and must not be guessed or
replayed after a stale-revision failure. The retired
`reference.catalog_search` identity is not a fallback.

```python
import json

read = client.config.section(
    input={
        "config_scope": "game",
        "section_id": "/Script/EngineSettings.GeneralProjectSettings",
        "editor_project_capability": "target.read",
        "parameters": {"target_ref": target_ref},
    },
    projection={"max_items": 2},
)
entry = read.payload["query_result"]["projection"]["payload"]["snapshot"][
    "entries"
][0]
target = json.loads(entry["value"]["text"])
current_target_revision = target["target_revision"]
```

`target.read` is accepted only by the five Editor Project Query providers:
`config.section`, `config.resolved_value`, `project.settings`,
`project.platform`, and `project.validation`. Config-backed observations expose
independently loaded `entries`; project-settings observations expose exact
`fields[]` metadata and current values. Repeat the same read after the write to
verify durable product state independently.

The generic form uses the same generated binding:

```python
result = client.execute(
    "editor_project.config_section.update",
    {
        "changes": changes,
        "expected_revision": current_target_revision,
        "target_ref": target_ref,
    },
)
```

The CLI forwards one identical request:

```text
uai-cli --connection connection.toml exec editor_project.config_section.update --params-json {"changes":[{"field_id":"entries","presence":"set","value":{"type_id":"uai.editor_project.config_entry_map.v1","canonical_value":{"UAI_StrictV2_T39":"public-write"}}}],"expected_revision":"<current-target-revision>","target_ref":"uai://editor-project/v1/config-section/game/%2FScript%2FEngineSettings.GeneralProjectSettings"}
```

Use `client.query.command_search("update project config section", limit=5)` and
then `client.query.command_detail(command_id, contract_hash)` to obtain the exact
request schema, named SDK/CLI forms, owner, failures and tutorial references.
Search is the only fuzzy command-selection step; execute the selected ID and
hash unchanged.

The fifteen historical read/diff/validate behaviors are supporting actions,
not public command aliases. Pass one of the closed action names in
`input.editor_project_capability` and its parameters in `input.parameters`:

- `config.section`: `device_profile.export`, `device_profile.query`,
  `scalability.export`;
- `config.resolved_value`: `device_profile.resolve_cvars`;
- `project.settings`: `project_settings.index`, `project_settings.page`;
- `project.platform`: `platform_config.export`, `target_platform.query`;
- `project.validation`: `device_profile.diff`, `device_profile.validate`,
  `platform_config.validate`, `platform_profile.validate_packaging`,
  `project_settings.diff`, `project_settings.validate`,
  `scalability.validate`.

These Query calls never write server-side export files; requested output paths
are returned only as provenance.

The client contains no HTTP implementation, retry, alias, config parser,
persistence, rollback or Unreal Engine business behavior. Inspect `Result.ok`
and the verified terminal projection; `state_unknown` is never safe for
automatic replay.
