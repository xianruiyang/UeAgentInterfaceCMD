"""Exact, projection-only bindings for T39 Editor project operations."""

from __future__ import annotations

from dataclasses import dataclass
from types import MappingProxyType


@dataclass(frozen=True, slots=True)
class EditorProjectBinding:
    command_id: str
    contract_hash: str


COMMAND_IDS = (
    "editor_project.config_section.update",
    "editor_project.device_profile.update",
    "editor_project.localization_target.update",
    "editor_project.platform_config.update",
    "editor_project.project_settings.update",
    "editor_project.scalability_group.update",
    "editor_project.string_table.update",
)


_CONTRACT_HASHES = {
    "editor_project.config_section.update": "sha256:5036aec4baf6b36b8132cac9e0547afda9bb4056976b1cf77a289793feb2af5d",
    "editor_project.device_profile.update": "sha256:383b4a61569d1ec291e1d65ac8dbb22583a8720ea6faf83426e1dd86e0f84e74",
    "editor_project.localization_target.update": "sha256:5452d391693a79918f543bd3c65f91b1588022ab7fee12ac00eaf54a99327155",
    "editor_project.platform_config.update": "sha256:48f384cc04b46c5384e7b7acd921a421bd57f5cfb485ecad59d8558387c8a272",
    "editor_project.project_settings.update": "sha256:64632c22261367afb613e96a661303605b79ceefbd6cd968ee972324035dfd29",
    "editor_project.scalability_group.update": "sha256:d515a3838a0d890ff3fe330dd9775bdc26f94b7a62ce167d2c5ae73154df3ecd",
    "editor_project.string_table.update": "sha256:ccc80a3ce611d7dd81dc9ccf09b8d895bd66e98d96926f33e27cb897dcc7cc86",
}

BINDINGS = MappingProxyType(
    {
        command_id: EditorProjectBinding(command_id, _CONTRACT_HASHES[command_id])
        for command_id in COMMAND_IDS
    }
)


def execute(client, command_id: str, params: dict[str, object]):
    binding = BINDINGS[command_id]
    return client.execute_exact(
        binding.command_id,
        params,
        contract_hash=binding.contract_hash,
    )
