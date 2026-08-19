from __future__ import annotations

from contextlib import AbstractContextManager
import http.server
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import threading
from typing import Any

import pytest

import uai
from uai.commands import BINDING_CATALOG, GENERATED_REGISTRY_HASH
from uai_cli.main import main as cli_main


COMMAND_ID = "reference.asset_read"
PARAMS = {"object_path": "/Game/StrictV2/DA_Client.DA_Client"}
BINDING = BINDING_CATALOG.find(COMMAND_ID)
assert BINDING is not None


def _project_root() -> Path:
    return Path(__file__).resolve().parents[3]


def _packaged_cli_paths() -> tuple[Path, Path]:
    return (
        _project_root()
        / "UeAgentInterfacePak/skills/ue-agent-interface/tools/uai-cli.exe",
        Path.home()
        / ".codex/skills/ue-agent-interface/tools/uai-cli.exe",
    )


def _trace(name: str, payload: dict[str, Any]) -> None:
    root = os.environ.get("UAI_T04_TRACE_DIR")
    if not root:
        return
    path = Path(root)
    path.mkdir(parents=True, exist_ok=True)
    (path / f"{name}.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
        newline="\n",
    )


class _ProtocolHttpServer(AbstractContextManager["_ProtocolHttpServer"]):
    def __init__(self) -> None:
        self.mode = "success"
        self.requests: list[dict[str, Any]] = []
        self._server: http.server.ThreadingHTTPServer | None = None
        self._thread: threading.Thread | None = None

    @property
    def endpoint(self) -> str:
        assert self._server is not None
        host, port = self._server.server_address[:2]
        return f"http://{host}:{port}"

    @property
    def stopped(self) -> bool:
        return self._thread is not None and not self._thread.is_alive()

    def __enter__(self) -> _ProtocolHttpServer:
        owner = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def do_POST(self) -> None:  # noqa: N802 - stdlib callback
                length = int(self.headers.get("Content-Length", "0"))
                body = self.rfile.read(length)
                request = json.loads(body.decode("utf-8"))
                owner.requests.append(request)
                if owner.mode == "disconnect":
                    try:
                        self.connection.shutdown(socket.SHUT_RDWR)
                    except OSError:
                        pass
                    self.connection.close()
                    return

                common = {
                    "schema": request["schema"],
                    "version": request["version"],
                    "correlation_id": request["correlation_id"],
                    "request_id": request["request_id"],
                    "command_id": request["command_id"],
                    "command_binding_hash": request[
                        "command_binding_hash"
                    ],
                }
                status = 200
                if owner.mode == "success":
                    response = {
                        **common,
                        "message_kind": "command_result",
                        "ok": True,
                        "payload": {"echo": request["params"]},
                        "error": None,
                    }
                elif owner.mode == "business_failure":
                    response = {
                        **common,
                        "message_kind": "command_result",
                        "ok": False,
                        "payload": {},
                        "error": {
                            "code": "strict_v2_business_rejected",
                            "message": "The exact target was rejected.",
                        },
                    }
                elif owner.mode == "protocol_failure":
                    status = 409
                    response = {
                        **common,
                        "message_kind": "protocol_error",
                        "error": {
                            "code": "command_contract_mismatch",
                            "message": "The projected contract is stale.",
                        },
                    }
                else:
                    raise AssertionError(f"unsupported fixture mode: {owner.mode}")

                encoded = json.dumps(
                    response,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
                self.send_response(status)
                if status >= 300:
                    self.send_header(
                        "X-Transport-Diagnostic", "remote_rejected"
                    )
                self.send_header("Content-Type", "application/octet-stream")
                self.send_header("Content-Length", str(len(encoded)))
                self.end_headers()
                self.wfile.write(encoded)

            def log_message(self, _format: str, *_args: object) -> None:
                return

        self._server = http.server.ThreadingHTTPServer(
            ("127.0.0.1", 0), Handler
        )
        self._thread = threading.Thread(
            target=self._server.serve_forever,
            name="uai-t04-http-fixture",
            daemon=True,
        )
        self._thread.start()
        return self

    def __exit__(self, _exc_type, _exc, _traceback) -> None:
        assert self._server is not None
        assert self._thread is not None
        self._server.shutdown()
        self._server.server_close()
        self._thread.join(timeout=5)
        assert not self._thread.is_alive()


def _write_connection(path: Path, endpoint: str) -> Path:
    path.write_text(
        "\n".join(
            (
                "format_version = 1",
                "[connection]",
                'transport = "http"',
                f'endpoint = "{endpoint}"',
                "[protocol]",
                'version = "uai.command.v1"',
                "[timeouts]",
                "connect_seconds = 2",
                "io_seconds = 2",
                "[authentication]",
                'mode = "none"',
                "[transport_options.http]",
                'auth_header = "X-UeAgentInterface-Token"',
                'probe_path = "/health"',
                'route_path = "/uai/command"',
                "tls_verify = false",
                "",
            )
        ),
        encoding="utf-8",
        newline="\n",
    )
    return path


def _stable_request(request: dict[str, Any]) -> dict[str, Any]:
    return {
        key: request[key]
        for key in (
            "schema",
            "version",
            "message_kind",
            "command_id",
            "command_binding_hash",
            "params",
        )
    }


def test_import_uai_is_inert_and_one_toml_call_connects(
    tmp_path: Path,
) -> None:
    repository = Path(__file__).resolve().parents[2]
    code = "\n".join(
        (
            "import pathlib, socket",
            "def forbidden(*args, **kwargs):",
            "    raise AssertionError('import performed external I/O')",
            "socket.socket.connect = forbidden",
            "pathlib.Path.read_text = forbidden",
            "import uai",
            "print(uai.__version__)",
        )
    )
    environment = dict(os.environ)
    environment["PYTHONPATH"] = str(repository / "cli")
    completed = subprocess.run(
        [sys.executable, "-c", code],
        cwd=tmp_path,
        env=environment,
        capture_output=True,
        text=True,
        timeout=30,
        check=False,
    )
    assert completed.returncode == 0, completed.stderr
    assert completed.stdout.strip() == uai.__version__
    _trace(
        "import",
        {
            "import_inert": True,
            "connection_api": "with uai.connect(connection_toml)",
        },
    )


def test_formal_manifest_is_the_exact_default_binding_catalog() -> None:
    manifest_path = (
        _project_root()
        / "Plugins/UeAgentInterface/Resources/UaiCommandManifest.json"
    )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    commands = manifest["commands"]
    by_id = {item["command_id"]: item for item in commands}

    assert manifest["source"]["kind"] == (
        "cpp_immutable_command_registry_export"
    )
    assert len(by_id) == len(commands)
    assert GENERATED_REGISTRY_HASH == manifest["registry_hash"]
    assert BINDING_CATALOG.command_ids == tuple(sorted(by_id))
    assert "query.command.search" in by_id
    assert "query.command.detail" in by_id
    assert "query.calibration.read" in by_id
    assert "reference.catalog_search" not in by_id

    for command_id, projected in by_id.items():
        binding = BINDING_CATALOG.find(command_id)
        assert binding is not None
        assert binding.binding_hash == projected["binding_hash"]
        assert binding.namespace == projected["namespace"]
        assert binding.method == projected["method"]
        assert [
            {
                "name": parameter.name,
                "wire_type": parameter.wire_type,
                "required": parameter.required,
                "nullable": parameter.nullable,
            }
            for parameter in binding.parameters
        ] == projected["parameters"]


def test_source_pak_and_installed_cli_share_exact_exec_surface() -> None:
    for executable in _packaged_cli_paths():
        assert executable.is_file(), executable
        completed = subprocess.run(
            [str(executable), "exec", "--help"],
            cwd=_project_root(),
            capture_output=True,
            text=True,
            timeout=30,
            check=False,
        )
        assert completed.returncode == 0, completed.stderr
        assert "--contract-hash" in completed.stdout


def test_named_generic_and_cli_emit_equivalent_single_http_requests(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
) -> None:
    with _ProtocolHttpServer() as server:
        config = _write_connection(
            tmp_path / "uai-local.toml", server.endpoint
        )

        with uai.connect(str(config)) as client:
            named_result = client.reference.asset_read(PARAMS["object_path"])
            named_state = client.connection_state
        assert named_result.ok is True
        assert named_state == "open"
        assert client.connection_state == "closed"

        with uai.connect(str(config)) as client:
            generic_result = client.execute(COMMAND_ID, PARAMS)
        assert generic_result.ok is True

        cli_status = cli_main(
            [
                "--connection",
                str(config),
                "exec",
                COMMAND_ID,
                "--params-json",
                json.dumps(PARAMS),
            ]
        )
        captured = capsys.readouterr()
        assert cli_status == 0, captured.err
        cli_result = json.loads(captured.out)
        assert cli_result["ok"] is True

        exact_cli_status = cli_main(
            [
                "--connection",
                str(config),
                "exec",
                COMMAND_ID,
                "--contract-hash",
                BINDING.binding_hash,
                "--params-json",
                json.dumps(PARAMS),
            ]
        )
        exact_captured = capsys.readouterr()
        assert exact_cli_status == 0, exact_captured.err
        assert json.loads(exact_captured.out)["ok"] is True

        for executable in _packaged_cli_paths():
            completed = subprocess.run(
                [
                    str(executable),
                    "--connection",
                    str(config),
                    "exec",
                    COMMAND_ID,
                    "--contract-hash",
                    BINDING.binding_hash,
                    "--params-json",
                    json.dumps(PARAMS),
                ],
                cwd=_project_root(),
                capture_output=True,
                text=True,
                timeout=30,
                check=False,
            )
            assert completed.returncode == 0, completed.stderr
            assert json.loads(completed.stdout)["ok"] is True

        assert len(server.requests) == 6
        stable = [_stable_request(item) for item in server.requests]
        assert all(item == stable[0] for item in stable[1:])
        assert stable[0] == {
            "schema": "uai.command.v1",
            "version": 1,
            "message_kind": "command_request",
            "command_id": COMMAND_ID,
            "command_binding_hash": BINDING.binding_hash,
            "params": PARAMS,
        }
        assert len({item["request_id"] for item in server.requests}) == 6
        request_id = server.requests[0]["request_id"]

    assert server.stopped
    _trace(
        "equivalence",
        {
            "registry_hash": GENERATED_REGISTRY_HASH,
            "command_id": COMMAND_ID,
            "request_id": request_id,
            "transport_adapter": "http",
            "connection_source": "toml",
            "request_count": 6,
            "surfaces": [
                "named_function",
                "generic_execute",
                "source_cli_default",
                "source_cli_exact",
                "pak_cli_exact",
                "installed_cli_exact",
            ],
            "stable_request": stable[0],
            "server_stopped": server.stopped,
        },
    )


def test_projected_exact_binding_and_disconnect_never_replay(
    tmp_path: Path,
) -> None:
    with _ProtocolHttpServer() as server:
        config = _write_connection(
            tmp_path / "uai-local.toml", server.endpoint
        )
        with uai.connect(str(config)) as client:
            exact_result = client.execute_exact(
                COMMAND_ID,
                PARAMS,
                contract_hash=BINDING.binding_hash,
            )
        assert exact_result.ok is True
        assert len(server.requests) == 1

        server.mode = "disconnect"
        before = len(server.requests)
        with uai.connect(str(config)) as client:
            with pytest.raises(uai.TransportError) as caught:
                client.execute_exact(
                    COMMAND_ID,
                    PARAMS,
                    contract_hash=BINDING.binding_hash,
                )
        assert caught.value.code in {
            "transport_disconnected",
            "transport_failed",
        }
        assert len(server.requests) - before == 1

    assert server.stopped
    _trace(
        "no_replay",
        {
            "exact_binding_supported": True,
            "disconnect_attempts": 1,
            "transport_error_code": caught.value.code,
            "server_stopped": server.stopped,
        },
    )


def test_transport_protocol_and_business_failures_remain_distinct(
    tmp_path: Path,
) -> None:
    with _ProtocolHttpServer() as server:
        config = _write_connection(
            tmp_path / "uai-local.toml", server.endpoint
        )

        server.mode = "business_failure"
        with uai.connect(str(config)) as client:
            business = client.execute(COMMAND_ID, PARAMS)
        assert business.ok is False
        with pytest.raises(uai.ServerCommandError) as business_error:
            business.raise_for_error()
        assert business_error.value.code == "strict_v2_business_rejected"

        server.mode = "protocol_failure"
        with uai.connect(str(config)) as client:
            with pytest.raises(uai.ProtocolError) as protocol_error:
                client.execute(COMMAND_ID, PARAMS)
        assert protocol_error.value.code == "command_contract_mismatch"

        server.mode = "disconnect"
        before = len(server.requests)
        with uai.connect(str(config)) as client:
            with pytest.raises(uai.TransportError) as transport_error:
                client.execute(COMMAND_ID, PARAMS)
        assert len(server.requests) - before == 1
        assert not isinstance(transport_error.value, uai.ProtocolError)
        assert not isinstance(transport_error.value, uai.ServerCommandError)

    assert server.stopped
    _trace(
        "failures",
        {
            "business": business_error.value.code,
            "protocol": protocol_error.value.code,
            "transport": transport_error.value.code,
            "negative_case_verified": True,
            "server_stopped": server.stopped,
        },
    )


def test_cli_and_client_have_no_second_http_or_business_implementation() -> None:
    repository = Path(__file__).resolve().parents[2]
    client_source = (
        repository / "cli/uai/uai_client/__init__.py"
    ).read_text(encoding="utf-8-sig")
    cli_source = (repository / "cli/uai_cli/main.py").read_text(
        encoding="utf-8-sig"
    )
    for forbidden in ("http.client", "urllib", "requests."):
        assert forbidden not in client_source
        assert forbidden not in cli_source
    assert "uai.connect" in cli_source
    assert "client.execute" in cli_source
    assert "retry" not in client_source.casefold()
    _trace(
        "legacy_exit",
        {
            "verified": True,
            "client_transport_owner": "uai.network_transport",
            "cli_business_owner": "uai.Client",
        },
    )
