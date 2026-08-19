"""Exact projection-only bindings for the ten T51 Niagara commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class NiagaraCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "niagara.asset.duplicate": "sha256:258ce30b1ce444b17772aa70f28dacce9832676108f7ed1dc7dcf65f88ecc407",
    "niagara.compile_refresh_settle": "sha256:05a334533805ccfe4b952b3abb23f080a536ef99bd13bd406a0da8d649a50fc0",
    "niagara.compound.apply": "sha256:842cbb241d054896980a0f428f0e0589b2a4be3f0af7af57b98b07cd98b3e30b",
    "niagara.emitter.asset.create": "sha256:8afe0a72d11a1b86bbf0e72f20300158334809892b2c96d4769ae4221dbcd66e",
    "niagara.renderer_event_parameter.apply": "sha256:fff82a8ad32e08d9487d75d7aeafe4bbe01d9292430a9160b985a29b98376b48",
    "niagara.script.graph.apply": "sha256:c0ad1c8c155f4036b7419ca468992a6136817ecf7441c20a86df4aa68ec252f7",
    "niagara.stack.apply": "sha256:2a1968d1faaa3c4dc4587aaf764f2ecac02da9d4abd36857461be13fa699a5ea",
    "niagara.stack.issue_fix": "sha256:79fc41bc8b0ccd7e69d773d775b9c71af1fe617e68989f0b383734c3f14922f0",
    "niagara.stack.reorder": "sha256:ed2da1ede9931f1883ebbf62c5ef237a3b7bfc31771ce4e8bd881948de182aeb",
    "niagara.system.asset.create": "sha256:30bf69c745b1522ab8084e8037527f3df77031e7a56f6ca64417b46026ff606d",
}
BINDINGS = MappingProxyType(
    {
        command_id: NiagaraCommandBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact Niagara command without local mechanics."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


__all__ = ["BINDINGS", "NiagaraCommandBinding", "execute"]
