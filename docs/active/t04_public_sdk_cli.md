# Public SDK and CLI client contract

The supported Python entry is `import uai`, followed by one
`uai.connect_project()` call for the local project. Explicit standalone connections
use `uai.connect(path)` as documented in `../PYTHON_SDK_AND_CLI.md`. Importing the package performs no
network or configuration I/O. The connection snapshot selects the production
transport adapter; command functions and the CLI do not know HTTP routes,
headers, sockets, or status codes.

Generated command functions forward one named public command through the same
`Client` and protocol used by `Client.execute()` and `ueagentinterfacecmd exec`. Transport
binding metadata remains internal. Callers and model-facing query results must
not provide or copy hashes, digests, fingerprints, GUIDs, or other machine
identities in Python, CLI parameters, prompts, logs, or receipts.

The sole binding input is
`Plugins/UeAgentInterface/Resources/UaiCommandManifest.json` with source kind
`cpp_immutable_command_registry_export`. The binding generator rebuilds generated
modules from that manifest when the command surface is explicitly refreshed.
Task-specific helper catalogs are not an input.
The manifest and generated bindings define available command names and Python
signatures. Complex nested schemas, variants, and typed failures come from the
generated SDK, formal schema, and owning domain documentation.

The current production adapter is HTTP. Each client invocation performs one
transport delivery attempt. A missing reply or disconnect raises
`TransportError`; an incompatible protocol envelope raises `ProtocolError`; a
valid command result with `ok=false` remains a `Result` and can be raised as
`ServerCommandError`. These outcomes are not rewritten into one another.

All SDK `Error` subclasses carry a public `diagnostic` mapping. Local producers
declare the failed field, expected/actual value or presence, and available file
location there. SDK wrappers, CLI failures and project lifecycle runners preserve
that mapping and only add their own recovery/status facts. A failed inspect,
start, status or recovery request retains the server diagnostic; its message is
never parsed to recover structured fields. Continuation, lease, authentication
and revision values remain private even when their field names identify an error.
HTTP exchange failures retain the concrete, redacted exception reason in the
message and expose `details.phase`, `details.exception_type`, and available
`errno`/`winerror` values. Connect, request send, response headers and body read
are distinguished at the source; custom exchanges may report `exchange`.
The delivery, SDK and CLI preserve this diagnostic without parsing its message.
Probe failures retain the same details under `transport_probe_failed`. No failed
request is automatically replayed, and connection credentials and request content
are excluded from the diagnostic.

For authoring failures, `Result.error.diagnostic` exposes the shared diagnostic's
code and stage, plus property path, target and retry safety when available.
Directory workspace failures include `source_file`, `json_pointer`, line and column
when parsed provenance or a native node mapped back to the workspace provides the
location. Locations without `source_file` refer to the underlying diagnostic input.
An existing container location can be refined to the declared field using parsed
workspace provenance, including referenced HJSON fragments. A missing field points
to its nearest existing parent with `source_kind: related_input`, not a fabricated
leaf location. `message` states the reason concisely; expected/actual fields carry
the concrete values without repeating them in the message or exposing private context.
Semantic comparison failures retain the source-selected difference path and
necessary `expected_value` and `actual_value`, including explicit null/false values.
Recursive comparison selects a field, element or semantic unit under the native
type's equivalence rules; the public result does not replace those values with
kind/count summaries. A supplied `*_value_present: false` denotes absence.
Workspace conflicts retain `proposed_value` at the same difference path, or a
structured proposed-edit diagnostic when the authored edit concerns another path.
`semantic_pointer` keeps the
comparison address when navigation is mapped back to editable HJSON.
`source_kind: authored_value` identifies a direct input; `related_input` identifies
related nodes/connections or a containing edit. `related_sources` retains additional
source context when supplied; a single parent location can use the main source fields.
Related inputs locate a derived failure; they do not identify an erroneous leaf.
Collected native issues retain their individual codes and available field paths
in `diagnostics`, with supplied expected/actual facts using the same public fields.
Native compile context in `related_sources` can retain its script path, node/pin
identity and call stack; that context does not by itself establish an HJSON file location.
The common command failure boundary preserves the machine error and adds an explicit
`diagnostic`. Ordinary command/native failure reasons are public; internal context
must be explicitly marked private by its owner. The SDK uses one recursive projection
for authoring, input, runtime, verification and operation diagnostic carriers. It
accepts the explicit `error.diagnostic` carrier; an inner cause
retains its own code, which need not equal its wrapper's code. Machine identities and
explicit private context remain hidden. Input-validation diagnostics contain `json_pointer`,
`keyword`, and a validation `message`; `schema_path` is present only when supplied
by schema validation. Missing fields, wrong types and invalid asset references can
be corrected without examining private handler logs. C3 failures after
execution use `uai.operation.failure/1` to retain the execution/verification
stage and receipt facts (`mutation_started` when known,
`mutation_may_have_started`, `retry_safe`). A verification failure after a write
must not be treated as an input rejection or automatically replayed. Unrecognized
legacy client-side detail retains its existing private projection; the SDK does not
guess facts from prose. Candidate disambiguation recovery remains available.
Shared runtime creation/resolution failures use `uai.runtime.diagnostic/1`:
`Result.error.diagnostic` retains the actual cause `code`, failed `stage` and public
`message`. Nested causes, source locations, collected errors, unchecked ranges,
expected/actual values and supplied suggestions survive wrappers without truncation.
The command boundary can supply a missing diagnostic target from the public request's
`target` selector; a more precise target already supplied by the cause is retained.
It never guesses a public target from `subject_id`, which also carries internal identity.
Only explicit private context stays in the machine envelope. This diagnostic does
not imply that content execution or a mutation started. Delegated command operations
carry the public diagnostic through the lifecycle error instead of reducing it to prose.
Shared apply failures also retain `transaction_status`, `rollback_attempted`,
`rollback_succeeded`, and conservative `retry_safe` in `Result.error.diagnostic`.
Absent outcome fields remain unknown, rather than being synthesized as false.
Post-apply workspace failures also retain `cause_code`, `asset_applied`,
`retry_import`, and `recovery_action` inside `Result.error["diagnostic"]`.
They report a committed asset with an unrefreshed workspace; never replay that
import. Typed import errors retain `mutation_started` when supplied by the owner.
These are coordinator facts, not client inferences; see the Plugin's
`docs/contracts/simple_authoring_typed_crud.md` for transaction ownership.

Closing a client closes only its owned transport. This module does not claim
that a particular UE query, operation, persistence path, or independent
readback has been proven; those claims require the owning command and direct
evidence.

CLI local usage, transport, serialization and protocol failures retain their reason
on stderr in the selected display format and in `--report`, with unchanged exit codes.
No command is retried to produce a report. A report-write failure preserves the command
result already written to stdout. PIE flow results retain a failed terminal operation's
actual error code and ordered flow details; `pie_flow_incomplete` is only a fallback
when no native failure code is available.
