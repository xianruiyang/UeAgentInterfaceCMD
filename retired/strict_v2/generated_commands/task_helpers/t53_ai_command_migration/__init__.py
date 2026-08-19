"""Exact projection-only bindings for the ten T53 AI commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class AiCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "ai.behavior_tree.asset.create": "sha256:5785ca06e924335be30380053c9ed7fcc3c2803be3d3c1f76194cedd9af05943",
    "ai.behavior_tree.graph.apply": "sha256:44da2a8ef748cba16019f3f906000c09a5117a16e7f6876da905a12dfccfbf04",
    "ai.blackboard.asset.create": "sha256:dc089b060b5fa8b7ebacd59d9a89054dd356f696b2b974a5b48b2f34cf904ffe",
    "ai.blackboard.schema.apply": "sha256:854dec4910942aabf7212987fbaad809cf4847e80389585dfd7f1b67ca545416",
    "ai.eqs.asset.create": "sha256:bcb9bf927a865491729a4875e82258ccea96b909e422d52ff8b3d133ca0c2e31",
    "ai.eqs.graph.apply": "sha256:1a21d9ad02e569b6778fcc5ca4aadd598557f8513cac5663d72890cf924102a4",
    "ai.smart_object_definition.apply": "sha256:30c388acca131439fafd4601fbfbe453c0de8528058a981fd40fe0dbf3a692ce",
    "ai.smart_object_definition.asset.create": "sha256:c4c94876510f4220fbbcda95eec216f6381c6a3e15e67fa5ebeccd72c28c60f6",
    "ai.state_tree.asset.create": "sha256:27422875027bf460a51157808c994bd7ca2c996eac526d328b6019f072154d19",
    "ai.state_tree.hierarchy.apply": "sha256:d90a1dc829cbf24c54cc0c7114a8f8a1882eaaf539774b69fa71a4c9abc3d156",
}
BINDINGS = MappingProxyType(
    {command_id: AiCommandBinding(command_id, contract_hash)
     for command_id, contract_hash in _HASHES.items()}
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id, dict(params), contract_hash=binding.contract_hash
    )


__all__ = ["AiCommandBinding", "BINDINGS", "execute"]
