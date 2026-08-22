# Non-HJSON Query SDK and CLI

Import only `uai` and connect from one complete Connection TOML. The final
manifest generates the normal domain namespaces for all forty-two current
Query routes:

```python
import uai

with uai.connect("connection.toml") as client:
    summary = client.project.summary(
        projection={"include_provenance": True, "max_items": 25},
    )
    components = client.world.actor_components(
        "/Game/Maps/WB_WhiteBox01.WB_WhiteBox01:PersistentLevel.Actor_1",
        input={"include_inherited": True},
        context={"state_plane": "authoring_memory"},
        projection={"max_items": 25},
    )
    asset = client.reference.asset_read(
        "/Game/UAI/Reference/BP_Reference.BP_Reference",
    )
    heights = client.landscape.height_read(
        "uai://landscape/example",
        input={
            "region": {
                "frame_id": "ue.landscape.local_sample_grid",
                "min_inclusive": [0, 0],
                "max_inclusive": [3, 3],
            },
            "space_contract": {
                "frame_id": "ue.landscape.local_sample_grid",
                "unit": "sample",
                "basis_evidence": "exact managed target and observed extent",
            },
        },
    )
```

`client.reference.asset_read` sends the exact public
`reference.asset_read` identity. It is not a client alias for
`asset.properties`; the server-owned Query route selects the shared asset
property mechanics and freezes `BlueprintDisplayName`, while retaining the
public command identity and contract hash.

The generic forms use the same generated catalog:

```python
result = client.execute(
    "project.summary",
    {"projection": {"max_items": 25}},
)
exact = client.execute_exact(
    "project.summary",
    {"projection": {"max_items": 25}},
    contract_hash="sha256:<exact hash from discovery>",
)
```

The CLI forwards the same request through the same Client, Protocol, and
Transport:

```text
uai-cli --connection connection.toml exec project.summary --params-json {"projection":{"max_items":25}}
uai-cli --connection connection.toml exec project.summary --contract-hash sha256:<exact> --params-json {"projection":{"max_items":25}}
```

Use `client.query.command_search(intent, limit=...)` to find candidates, then
`client.query.command_detail(command_id, contract_hash)` to obtain the exact
schema, named SDK form, CLI form, owner, and tutorial references. Search is
the only fuzzy step; execute the selected ID and hash unchanged.

Asset commands and selected World commands require an exact `target`;
`reference.asset_read` requires `object_path`. Missing required identities
return typed failures such as `query_target_required`. Successful results
expose `command_id`, `mechanics_command_id`, `read_only`, and `query_result`.
Inspect completeness and state semantics before extending a conclusion beyond
the returned scope. The generated methods add no UE business logic, alias
mapping, retry loop, transport fallback, or result reinterpretation.

The former 21 public query identities assigned to T06 are not aliases. Their
frozen contracts and exact current successors are recorded in
`Plugins/UeAgentInterface/docs/active/successors/t06_non_hjson_query_migration.json`.
Use only the current generated methods named there; the old IDs are absent from
the manifest, SDK catalog, CLI, and compatibility routing.
