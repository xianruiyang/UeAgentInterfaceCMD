"""Exact projection-only bindings for T45 viewport and graph control."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class ViewportGraphBinding:
    command_id: str
    contract_hash: str


_HASHES = {
    "graph.layout.apply": "sha256:879e88b4205d1feebb832fc855108e9e60736b8368b0fcfd023311d9b3cc2ef3",
    "graph.view.read": "sha256:bbe2f553fce6a348b0e03ecfce2b556c09c20d934ee016273bac1bfacb3e2794",
    "graph.view.update": "sha256:dc9db1458a3eb8f3d04e6b64b64e73c6ac8e482aa07c8373c9a047e70e40b142",
    "viewport.actor.pick": "sha256:12a70c8ebef3b26163b745c7e882f022a3d236fba7c2f1757ecf2f364362c06b",
    "viewport.actor.select": "sha256:4f9cec0129ca1ac9f43782f20119c24e87cfd36f119d9874ee3933e38c577df2",
    "viewport.camera.frame": "sha256:958518e8dd76173d9fecb085871568fa81c2028c5d21ecc1864cbf4a2e417166",
    "viewport.instance.list": "sha256:fd0b1f516946674a1ba6431c8ffd9b616f8b3d192cf27ebc5f78a0dd2053c1c1",
    "viewport.pixel_scale.read": "sha256:dc28b100e006a0ee36a74a9b1e144e4f82bcb4f407f1d2e153f02fc1b1b399a3",
    "viewport.ray.deproject": "sha256:28b4d8b28eb00800054356ee2eff6a181fc57e0a13e4cee0f5d40ff538240141",
    "viewport.ray.trace": "sha256:6a9412270abbdac6e3f228221a268a5e0cb93f860e5150518e80ea1d0ec2991d",
    "viewport.state.read": "sha256:c3434d4e2d4f916c6266a4aa3bce97ba221188aefd76290ddb1b607eb9be2244",
    "viewport.state.restore": "sha256:1af721c987f13efce90dc6834809bfc2a7616630f88774c68bfebfc9760fc181",
    "viewport.state.update": "sha256:737112bd565c8b7cca93526420411843ab7dde72acb115f4a1cd4851b361aa4e",
    "viewport.view_mode.list": "sha256:cf61ab728866c16ec7f934daad183460df4143b459cfc246ffa7d731063a6332",
    "viewport.warning.list": "sha256:3c345e154810d15570600228b76454e214fe42222eaed75e362e5cc71ec4617c",
}
BINDINGS = MappingProxyType(
    {
        command_id: ViewportGraphBinding(command_id, contract_hash)
        for command_id, contract_hash in _HASHES.items()
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    """Forward one exact viewport/graph command without local mechanics."""
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        dict(params),
        contract_hash=binding.contract_hash,
    )


__all__ = ["BINDINGS", "ViewportGraphBinding", "execute"]
