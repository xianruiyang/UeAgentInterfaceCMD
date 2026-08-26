from __future__ import annotations

from contextlib import AbstractContextManager
import json
from pathlib import Path
import re
from typing import Any

import pytest

import uai
from uai.commands import (
    BINDING_CATALOG,
    GENERATED_REGISTRY_HASH,
    bind_generated_commands,
)
from uai_cli.main import main as cli_main


class _RecordingClient:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, Any], str]] = []

    def execute_exact(
        self,
        command_id: str,
        params: dict[str, Any],
        *,
        contract_hash: str,
    ) -> _RecordedResult:
        snapshot = dict(params)
        self.calls.append((command_id, snapshot, contract_hash))
        return _RecordedResult(command_id, snapshot)

    def execute(
        self,
        command_id: str,
        params: dict[str, Any],
    ) -> _RecordedResult:
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        return self.execute_exact(
            binding.command_id,
            params,
            contract_hash=binding.binding_hash,
        )


class _RecordedResult:
    ok = True

    def __init__(self, command_id: str, params: dict[str, Any]) -> None:
        self.raw_response = {
            "ok": True,
            "command_id": command_id,
            "params": params,
        }


class _ClientContext(AbstractContextManager[_RecordingClient]):
    def __init__(self, client: _RecordingClient) -> None:
        self.client = client

    def __enter__(self) -> _RecordingClient:
        return self.client

    def __exit__(self, _exc_type, _exc, _traceback) -> None:
        return None


def _require_bindings():
    assert re.fullmatch(r"sha256:[0-9a-f]{64}", GENERATED_REGISTRY_HASH)
    command_ids = {
        "editor.session",
        "query.command.search",
        "query.command.detail",
        "query.calibration.read",
    }
    bindings = {
        command_id: BINDING_CATALOG.find(command_id)
        for command_id in command_ids
    }
    assert all(item is not None for item in bindings.values())
    assert all(
        re.fullmatch(r"sha256:[0-9a-f]{64}", item.binding_hash)
        for item in bindings.values()
        if item is not None
    )
    return bindings


def test_named_query_calibration_functions_send_one_exact_request() -> None:
    bindings = _require_bindings()
    client = _RecordingClient()
    commands = bind_generated_commands(client)

    commands.query.command_search(
        "inspect the current editor without changing assets",
        limit=3,
    )
    commands.query.command_detail(
        "query.calibration.read",
        bindings["query.calibration.read"].binding_hash,
    )
    commands.query.calibration_read(
        "runtime_probe",
        limit=2,
    )

    assert [call[0] for call in client.calls] == [
        "query.command.search",
        "query.command.detail",
        "query.calibration.read",
    ]
    assert [call[2] for call in client.calls] == [
        bindings[call[0]].binding_hash for call in client.calls
    ]
    assert len(client.calls) == 3


def test_generic_exact_and_named_query_requests_are_equivalent() -> None:
    bindings = _require_bindings()
    named = _RecordingClient()
    generic = _RecordingClient()
    params = {"category": "runtime_probe", "limit": 2}

    bind_generated_commands(named).query.calibration_read(
        "runtime_probe",
        limit=2,
    )
    generic.execute(
        "query.calibration.read",
        params,
    )
    assert named.calls == generic.calls


def test_named_command_detail_forwards_exact_variant_identity() -> None:
    bindings = _require_bindings()
    client = _RecordingClient()
    commands = bind_generated_commands(client)

    commands.query.command_detail(
        "editor.session",
        bindings["editor.session"].binding_hash,
        variant_id="policy:world-context:set-current/v1",
    )

    assert client.calls == [
        (
            "query.command.detail",
            {
                "command_id": "editor.session",
                "contract_hash": bindings["editor.session"].binding_hash,
                "variant_id": "policy:world-context:set-current/v1",
            },
            bindings["query.command.detail"].binding_hash,
        )
    ]


def test_cli_default_and_exact_forms_use_the_same_discovered_binding(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    bindings = _require_bindings()
    client = _RecordingClient()
    monkeypatch.setattr(
        uai,
        "connect",
        lambda _connection: _ClientContext(client),
    )

    default_status = cli_main(
        [
            "--connection",
            "fixture.toml",
            "exec",
            "query.calibration.read",
            "--params-json",
            json.dumps({"category": "runtime_probe", "limit": 2}),
        ]
    )
    exact_status = cli_main(
        [
            "--connection",
            "fixture.toml",
            "exec",
            "query.calibration.read",
            "--contract-hash",
            bindings["query.calibration.read"].binding_hash,
            "--params-json",
            json.dumps({"category": "runtime_probe", "limit": 2}),
        ]
    )
    captured = capsys.readouterr()
    assert default_status == 0, captured.err
    assert exact_status == 0, captured.err
    assert len(client.calls) == 2
    expected = (
        "query.calibration.read",
        {"category": "runtime_probe", "limit": 2},
        bindings["query.calibration.read"].binding_hash,
    )
    assert client.calls == [expected, expected]


def test_default_generated_query_surface_has_no_second_business_implementation() -> None:
    _require_bindings()
    generated = Path(__file__).resolve().parents[2] / "cli" / "uai" / "commands" / "generated.py"
    text = generated.read_text(encoding="utf-8")
    assert 'self._client.execute(' in text
    assert "alias" not in text.casefold()
    assert "http.client" not in text
    assert "requests." not in text
    assert "Unreal" not in text


def test_public_tutorials_route_discovery_to_the_default_sdk_and_cli() -> None:
    cmd_root = Path(__file__).resolve().parents[2]
    sdk_guide = cmd_root / "docs" / "PYTHON_SDK_AND_CLI.md"
    task_guide = cmd_root / "docs" / "active" / "t05_query_public_calibration.md"
    skill_guide = (
        cmd_root.parent
        / "UeAgentInterfacePak"
        / "skills"
        / "ue-agent-interface"
        / "references"
        / "public-sdk-playbook.md"
    )
    sdk_text = sdk_guide.read_text(encoding="utf-8")
    task_text = task_guide.read_text(encoding="utf-8")
    skill_text = skill_guide.read_text(encoding="utf-8")

    for text in (sdk_text, task_text, skill_text):
        assert "query.command.search" in text
        assert "query.command.detail" in text
        assert "client.query.command_search" in text
        assert "client.query.command_detail" in text
        assert "uai-cli" in text
        assert "reference.catalog_search" not in text
    assert "uai-docs:python-sdk-and-cli#command-discovery" in sdk_text
    assert "uai-skill:public-sdk-playbook#command-discovery" in skill_text
