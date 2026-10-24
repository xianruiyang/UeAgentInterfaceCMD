# T35 discovery and direct name reuse

Use the generated public SDK bindings for command, existing-content, and
domain-candidate discovery. Do not call HTTP directly, inspect source catalogs,
or translate a search result in client code.

Discovery is staged:

1. `query.command_search` returns the complete de-duplicated `commands`
   array of command names.
2. `query.command_usage` accepts those names and returns a compact mapping from
   each command name to its minimum named Python call.
3. When a selected parameter's nested shape is needed, use local
   `ueagentinterfacecmd describe <command> --parameter <name>` or
   `uai.describe_command(command, parameter=name)`. Both read the installed
   generated contract without contacting Editor. `--pointer` selects a JSON
   Pointer within that parameter's schema. Omit `--parameter` for the short
   name/type/required list; ordinary command search and usage remain compact.
   A parameter with no attached schema explicitly returns `schema_available: false`;
   use its focused domain contract rather than guessing a nested shape.

Candidate and existing-content searches return the complete matching `names`
array. Context-dependent candidate queries also return one `scope` containing
their public target and supplied graph, stack, parent, surface or create-command
context. `scope` is response metadata, not a creation selector. Optional `describe`
returns only the selected candidate's supported defaults; ordinary searches do not
return per-candidate details, provider metadata, paging envelopes or machine identities.
Creation names are grouped for display; an actual same-name ambiguity returns short
semantic `select` choices while preserving each native identity internally.
Existing-content searches retain their readable scoped aliases.

Native catalog coverage is a source fact, separate from the number of matches
and projected names. A known coverage/support gap returns a structured error.
The explicitly deferred SoundCue, MetaSound and UMG partial catalogs remain usable
and return a `diagnostics` warning describing their scope.

Reuse names in the same scope. When an asset, graph, pin, stage or factory context
changes, query the needed names there. Blueprint pin queries additionally return
`candidate_context` for the HJSON node; keep it beside `candidate` unchanged.
The shared implementation and scope fields are defined in Plugin T35's
`Candidate query scope` section.

Creation is fail-closed. The request uses the returned `name` and, only when
the live command contract proves it necessary, the short semantic `select`
fields needed to disambiguate. The service re-enumerates the current native context; zero or
multiple matches is an error, never an implicit first-match choice. After
creation, inspect the settled instance through its owning readback. Variable
pin interfaces are instance-owned and must be read from that created instance,
not inferred from a catalog candidate.

No model-facing search, usage, detail, request, result, log, or receipt may
contain hashes, digests, fingerprints, GUIDs, random identities, raw wire
metadata, or correlation identities. Internal transport and server bindings may
retain their own private metadata, but it is never an input or output of the
model workflow.

The public SDK entry remains:

```python
import uai

with uai.connect_project() as client:
    found = client.query.command_search("content graph read")
    usage = client.query.command_usage(found.payload["commands"])
```

This document specifies the discovery contract; it does not claim that any
particular domain create, persistence path, or independent readback is proven.
Those claims require the owning command's direct evidence.
