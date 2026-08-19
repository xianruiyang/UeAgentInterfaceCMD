"""Exact, projection-only bindings for T42 Physics/Deformer commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class PhysicsDeformerOperationBinding:
    command_id: str
    contract_hash: str


_CONTRACT_HASHES = {
    "animation.deformer_graph.asset.create": "sha256:f6dc4268f799949192d11627aadfc8c382358f1d32e7dc1a04366eee429d0ac7",
    "animation.deformer_graph.topology.apply": "sha256:ea919cecbd7356d35730e4779f863997e2d336f9277c224d03f12d4c2d5d6bfc",
    "animation.deformer_source_library.asset.create": "sha256:d2ef98bcfb98111739d52dfb64b5cc02280dcb1001434ce6aa6fdbf4add82f62",
    "animation.deformer_source_library.bindings.apply": "sha256:a5a2cae32c3cb7ade8c337bbdaec9c7bbd9d488485b7dd7c2e0649baa0fededa",
    "animation.mesh_deformer_collection.asset.create": "sha256:b0f674ef762f9eb95f4f6680b3d389dbc14e4776ca61e8d04c492d9e12ff484f",
    "animation.mesh_deformer_collection.entries.apply": "sha256:f2a38fb4ebd9a855d979213f5c4178475eed06cf105f8aadd930878a1d3875fa",
    "animation.ml_deformer.asset.create": "sha256:9a03cda3b8db441a27fff7528e99b7e3e799f2fb3660c90d992ff3723048f72d",
    "animation.ml_deformer.configuration.apply": "sha256:0e06e288ff3509cee25c9e74d5cc208ab482c46713a5a37ceb7771a90389ecbe",
    "deformer.evaluation.sample": "sha256:3d71e15d735d02e9c7b98ef61d4bfb2fc446b7f12b22b6d501925fdafbc191ec",
    "deformer.geometry.sample": "sha256:2ccc860838128393867ebb30216e4d56712285556f5134d138a36a85498ee386",
    "deformer.training_inputs.validate": "sha256:3811b17e30470fc88b2d5e67edea972fb485592544d351788c6dc3dbaf44fde8",
    "physics.asset.structure.replace": "sha256:79341610dcdcf07eba08c49efb5d0aebac2b3e52e17f9c42af479f4563ae04a6",
    "physics.constraint.update": "sha256:b20791528d243a8d260a7b58ac3734d0532205c741fae6cf40042c2c4d2ebc6f",
    "physics.material.update": "sha256:5f662751e7bd0634fbc244755f7357dd4c832c2bfe47b7fd7d94bc9c9be9a334",
    "physics.simulation.probe": "sha256:488b6b178fd078f7427af5d723497b9b8fd35d1fc261d91f6e153bea719a6458",
}

COMMAND_IDS = tuple(_CONTRACT_HASHES)
BINDINGS = MappingProxyType(
    {
        command_id: PhysicsDeformerOperationBinding(command_id, contract_hash)
        for command_id, contract_hash in _CONTRACT_HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS.get(command_id)
    if binding is None:
        raise ValueError(f"physics_deformer_command_unknown: {command_id}")
    return client.execute_exact(
        binding.command_id,
        params,
        contract_hash=binding.contract_hash,
    )


__all__ = [
    "BINDINGS",
    "COMMAND_IDS",
    "PhysicsDeformerOperationBinding",
    "execute",
]
