# T13 UObject/DataAsset SDK and CLI

Import only `uai` and connect from one complete Connection TOML. The final
manifest generates the default `content_graph` namespace for all nine T13
contracts:

```python
import uai

with uai.connect("connection.toml") as client:
    graph = client.content_graph.compound(
        "/Game/StrictV2/T13/DA_Recursive.DA_Recursive",
        input={"sections": ["summary", "structure", "items"]},
        context={"state_plane": "persisted"},
        projection={"max_items": 50},
    )
```

A recursive inline import forwards one exact server contract without selecting
a provider or interpreting HJSON on the client:

```python
result = client.content_graph.import_workspace(
    "/Game/StrictV2/T13/DA_Recursive.DA_Recursive",
    {"kind": "inline", "document": document},
    expected_revision="absent",
    authorization_id="auth:t13:approved-impact",
    limits={"max_nodes": 64, "max_work_units": 4096},
)
```

The same generated method accepts the other carriers without selecting a
domain-specific command or adapter:

```python
single = client.content_graph.import_workspace(
    "/Game/StrictV2/T13/DA_FromFile.DA_FromFile",
    {"kind": "single_file", "path": "D:/uai/workspaces/dataasset.hjson"},
    expected_revision="absent",
    authorization_id="auth:t13:file-impact",
)
directory = client.content_graph.import_workspace(
    "/Game/StrictV2/T13/DA_FromDirectory.DA_FromDirectory",
    {"kind": "directory", "path": "D:/uai/workspaces/dataasset"},
    expected_revision="absent",
    authorization_id="auth:t13:directory-impact",
)
```

A directory workspace must provide `.uai/workspace.hjson` using
`uai.content_graph.workspace/1`. It binds the exact `target_identity` and
`base_revision`, names `entry_file`, lists every managed `.hjson` file with a
SHA-256 `content_hash`, and declares the `references` closure. Paths are
absolute only at the public `source.path`; paths inside the manifest are
relative to the workspace root and cannot escape it. The server loads and
verifies the complete source before any UE write. Do not send the retired
top-level `carrier` or `hjson_document` fields.

Export uses the same namespace and exact target:

```python
exported = client.content_graph.export_workspace(
    "/Game/StrictV2/T13/DA_Recursive.DA_Recursive",
    "D:/program/UE/GptProjectTest/Saved/StrictV2/T13/export",
    profile_id="llm_authoring",
)
```

The generic and exact forms use the same generated catalog:

```python
result = client.execute(
    "content_graph.summary",
    {"target": "/Game/StrictV2/T13/DA_Recursive.DA_Recursive"},
)
exact = client.execute_exact(
    "content_graph.summary",
    {"target": "/Game/StrictV2/T13/DA_Recursive.DA_Recursive"},
    contract_hash="sha256:<exact hash from discovery>",
)
```

The CLI forwards the same exact request:

```text
uai-cli --connection connection.toml exec content_graph.summary --params-json {"target":"/Game/StrictV2/T13/DA_Recursive.DA_Recursive"}
uai-cli --connection connection.toml exec content_graph.import_workspace --contract-hash sha256:<exact> --params-file recursive-import.json
```

`recursive-import.json` uses the same public shape:

```json
{
  "target": "/Game/StrictV2/T13/DA_Recursive.DA_Recursive",
  "source": {"kind": "directory", "path": "D:/uai/workspaces/dataasset"},
  "expected_revision": "absent",
  "authorization_id": "auth:t13:directory-impact"
}
```

Use `client.query.command_search(intent, limit=...)` to discover candidates and
`client.query.command_detail(command_id, contract_hash)` to obtain the exact
schema, named SDK form, CLI form, owner, and tutorial references. Search is the
only fuzzy step; do not rewrite the selected identity or hash.

The client contains no HJSON parser, type alias, provider selector, lifecycle
rule, retry loop, UE lookup, or mutation logic. Import success requires the
server terminal receipt plus an independent public query after persistence and
reload. Export success requires the server's semantic verification receipt.
