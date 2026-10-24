# Command contract projection generation

`tools.uai_repository.command_contract_generation` accepts one canonical
projection exported by the immutable C++ command registry. It validates the
registry internally before rendering Python bindings or Markdown.

Generated Python functions call the internal executor with machine metadata
hidden from the model. Public guidance is command_search names → command_usage
minimal named calls → generated SDK; synonyms never become aliases or fallback
execution. This repository tool does not scan Markdown, tests, old routes, or
existing Python functions to infer command behavior.
