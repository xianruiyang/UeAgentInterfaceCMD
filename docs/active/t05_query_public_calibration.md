# Query calibration SDK and CLI

The final manifest projects these three discovery/calibration commands into the
normal `query` namespace alongside the rest of the active catalog:

- `query.command.search` → `command_search`
- `query.command.detail` → `command_detail`
- `query.calibration.read` → `calibration_read`

Import only the public SDK and connect with the normal TOML configuration:

```python
import uai

with uai.connect("connection.toml") as client:
    candidates = client.query.command_search(
        "inspect the current editor runtime",
        limit=3,
    )
```

The helper sends exactly one `client.execute_exact` request. It performs no transport selection, command-name translation, UE business logic, retry or replay.

Use the candidate identity unchanged:

```python
detail = client.query.command_detail(
    "query.calibration.read",
    candidate["contract_hash"],
)
result = client.query.calibration_read(
    "runtime_probe",
    limit=2,
)
```

`query.command.detail` also returns `tutorial_references` and an `invocation`
object with named, generic, exact and CLI templates. The stable references are
`uai-docs:python-sdk-and-cli#command-discovery` and
`uai-skill:public-sdk-playbook#command-discovery`.

The default generic equivalent is `client.execute(command_id, params)`; use
`client.execute_exact(command_id, params, contract_hash=...)` to lock the exact
identity returned by discovery. The CLI exposes both forms:

```text
uai-cli --connection connection.toml exec query.command.search --params-json {"intent":"inspect the current editor runtime","limit":3}
uai-cli --connection connection.toml exec query.command.detail --params-json {"command_id":"query.calibration.read","contract_hash":"sha256:<exact>"}
uai-cli --connection connection.toml exec query.calibration.read --contract-hash sha256:<exact> --params-json {"category":"runtime_probe","limit":2}
```

Generated named methods, generic/default execution, exact execution and CLI
preserve the same command ID, parameter object, contract hash, result envelope
and typed failure. `query.command.search` is the only fuzzy step; callers must
not reinterpret the identity returned by it or import a task-specific helper.
