# Public SDK and CLI client contract

The supported Python entry is `import uai`, followed by one `uai.connect("path/to/connection.toml")` call. Importing the package performs no network or configuration I/O. The immutable connection snapshot selects the production transport adapter; command functions and the CLI do not know HTTP routes, headers, sockets, or status codes.

Generated command functions call `Client.execute_exact(command_id, params, contract_hash=...)`. The command identity, contract hash, and parameters are forwarded without aliases, defaults, fallback, retry, or replay. `Client.execute(command_id, params)` and `uai-cli exec` resolve their exact binding from the same generated catalog and then use `execute_exact`, so named, generic, and CLI calls create the same protocol request apart from their unique request and correlation identities.

The sole binding input is `Plugins/UeAgentInterface/Resources/UaiCommandManifest.json` with source kind `cpp_immutable_command_registry_export`. `tools/uai_binding/generate_bindings.py` rejects the legacy registry exporter, and check mode fails when either generated module differs from that manifest. The manifest registry hash, all command ids, Python namespaces/methods, parameter schemas, and frozen binding hashes must exactly equal the default catalog; task-specific helper catalogs are not an input.

The source CLI, Pak CLI, and installed CLI expose the same `exec COMMAND_ID --contract-hash HASH` surface. Omitting the hash resolves the current default catalog entry; supplying it calls `Client.execute_exact` with the discovery-provided identity. Both paths share the same Client, protocol codec, transport adapter, TOML connection source, and one-delivery failure behavior.

The current production adapter is HTTP. Each client invocation performs one transport delivery attempt. A missing reply or disconnect raises `TransportError`; an incompatible protocol envelope raises `ProtocolError`; a valid command result with `ok=false` remains a `Result` and can be raised as `ServerCommandError`. These outcomes are not rewritten into one another.

Closing a client closes only its owned transport. This client-contract module does not claim that a particular UE Query, operation, persistence path, or independent readback has been proven; the first real Query vertical is owned by the dependent strict-v2 calibration task.
