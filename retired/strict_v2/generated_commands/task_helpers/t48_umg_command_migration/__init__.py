"""Exact projection-only bindings for the two T48 non-HJSON UMG commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class UmgCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "umg.asset.create": "sha256:bebb84dc5b59e08abd65d869c5214a96ea5362e2a2de3109a6b42db14c422610",
    "umg.widget.events.discover": "sha256:bd899756a530450581f16d43db70433c99cd316934150561a0cab1245ebfccd2",
}
BINDINGS = MappingProxyType(
    {
        command_id: UmgCommandBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact UMG command without local mechanics."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


__all__ = ["BINDINGS", "UmgCommandBinding", "execute"]
