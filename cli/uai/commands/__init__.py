"""Static Client-bound commands generated from the C++ registry manifest."""

from ._runtime import (
    CommandBinding,
    CommandBindingCatalog,
    CommandExecutor,
    CommandParameterBinding,
    OMITTED,
)
from .generated import (
    BINDING_CATALOG,
    GENERATED_REGISTRY_HASH,
    GeneratedClientBindingsMixin,
    GeneratedCommandNamespaces,
    bind_generated_commands,
)


__all__ = [
    "BINDING_CATALOG",
    "CommandBinding",
    "CommandBindingCatalog",
    "CommandExecutor",
    "CommandParameterBinding",
    "GENERATED_REGISTRY_HASH",
    "GeneratedClientBindingsMixin",
    "GeneratedCommandNamespaces",
    "OMITTED",
    "bind_generated_commands",
]

