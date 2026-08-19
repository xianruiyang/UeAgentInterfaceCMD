"""Exact projection-only binding for the T43 Reference operation."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class ReferenceOperationBinding:
    command_id: str
    contract_hash: str


_COMMAND_ID = "reference.asset_apply"
BINDINGS = MappingProxyType(
    {
        _COMMAND_ID: ReferenceOperationBinding(
            _COMMAND_ID,
            "sha256:cb700d1c92701ab8caf5c6f3b89e681eba6d158b3f77796a947d3bdc6bd2340f",
        ),
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact Reference operation without aliases or workflow logic."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


__all__ = ["BINDINGS", "ReferenceOperationBinding", "execute"]
