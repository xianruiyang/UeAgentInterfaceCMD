"""Exact projection-only bindings for the fourteen T57 Animation Rig commands."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class AnimationRigCommandBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "animation.control_rig.asset.create": "sha256:f4f920e9609eb2759de35a5638ae37a90bfa4e246075dd166737e392692f661a",
    "animation.control_rig.hierarchy_graph.apply": "sha256:e67ed93f7a3d3e608f221f67bbde34b7cb6d12df5dcfbefe4554759755ddb113",
    "animation.control_rig.shape_library.apply": "sha256:27fc410413cfeee0810f5d3174a8ac2dc289a075a67101322855e2249aeb2a33",
    "animation.control_rig.shape_library.asset.create": "sha256:21ae58bb5f2d90862ec410dc285d85c29227bb4f2322abc54e3fcaf5d6f5248e",
    "animation.ik_retargeter.asset.create": "sha256:70590f710562e0a8723597128251267b8f5f4c39386ae16b1a5599a30a65a72a",
    "animation.ik_retargeter.definition.apply": "sha256:2a2f2ec86da840086662b8ed2719b81b06732881fac6b9471072204fefd47073",
    "animation.ik_retargeter.settings.apply": "sha256:49334c4ad87c6539e953c7f4fabd3344a2d460066e851fc90482a2b2ca3b909d",
    "animation.ik_rig.asset.create": "sha256:5bc2b6cb690d76613ba52fb990441556fc3172d6b2349417560b043034a6f112",
    "animation.ik_rig.definition.apply": "sha256:697260b249f6b16b799a63b8a4895bf940bf1524bdc3b62abb6bd7a781b6ef77",
    "animation.ik_rig.definition.auto_generate": "sha256:4bfb39455563e84daf75a3702364c874fb3b4b456332eaaec5c7d8641b2011e2",
    "animation.skeleton.compatibility.apply": "sha256:b216946279ab5241a5cd204d99cd1f479bf7ca05029ac2ea0370222e60842db7",
    "animation.skeleton.definition.apply": "sha256:d676863c385fc54ad3d855209e8a48d553e895449ff4cea96bbecc160d3d6359",
    "animation.skeleton.slots.read": "sha256:101cbce97ec67cd8f0fa6dc5618074bb711f8278051d131fbc74ac6f33d2813e",
    "animation.skeleton.virtual_bone.apply": "sha256:40d3a97c85e06883fcda75a73168a8751db49ab521404ec514018c05949a6318",
}
BINDINGS = MappingProxyType(
    {
        command_id: AnimationRigCommandBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id, dict(params), contract_hash=binding.contract_hash
    )


__all__ = ["AnimationRigCommandBinding", "BINDINGS", "execute"]
