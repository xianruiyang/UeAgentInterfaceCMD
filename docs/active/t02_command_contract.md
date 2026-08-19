# Command contract projection generation

`tools.uai_repository.command_contract_generation` accepts one canonical
projection exported by the immutable C++ command registry. It validates the
registry provenance, complete contract fields, exact identities, hashes, and
uniqueness before rendering Python bindings or Markdown.

Generated Python functions call `client.execute_exact` with the registered
command identity and contract hash. Discovery synonyms are emitted only in
reference text and never become functions, aliases, prefix matching, or
fallback execution. This repository tool does not scan Markdown, tests, old
routes, or existing Python functions to infer command behavior.
