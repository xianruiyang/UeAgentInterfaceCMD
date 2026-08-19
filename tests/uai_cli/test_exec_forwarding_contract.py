from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import ast
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import uai
from uai_cli import main as cli_main


CLI_MAIN = (
    Path(__file__).resolve().parents[2]
    / "cli"
    / "uai_cli"
    / "main.py"
)
BINDING_HASH = (
    "sha256:"
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
)


def _result(ok: bool) -> uai.Result:
    return uai.Result(
        {
            "schema": "uai.command.v1",
            "version": 1,
            "message_kind": "command_result",
            "correlation_id": "corr-cli",
            "request_id": "req-cli",
            "command_id": "fixture.echo_exact",
            "command_binding_hash": BINDING_HASH,
            "ok": ok,
            "payload": {
                "unicode": "协议/蓝图",
                "large_integer": 9007199254740993,
            },
            "error": (
                None
                if ok
                else {
                    "code": "fixture_failed",
                    "message": "fixture failed",
                }
            ),
        }
    )


class _Client:
    def __init__(self, result: uai.Result) -> None:
        self.result = result
        self.calls: list[tuple[str, dict[str, object]]] = []
        self.closed = False

    def execute(
        self,
        command_id: str,
        params: dict[str, object],
    ) -> uai.Result:
        self.calls.append((command_id, params))
        return self.result

    def __enter__(self):
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback):
        self.closed = True


class CliExecForwardingContractTests(unittest.TestCase):
    def _run_main(self, argv: list[str]) -> int:
        try:
            with redirect_stderr(io.StringIO()):
                return cli_main.main(argv)
        except SystemExit as exc:
            self.fail(
                "cli_exec_surface_missing:"
                f"unexpected_system_exit={exc.code}"
            )

    def test_exec_json_uses_public_connect_and_one_execute(self) -> None:
        client = _Client(_result(True))
        params = {
            "unicode": "协议/蓝图",
            "large_integer": 9007199254740993,
            "nullable": None,
            "empty": {},
        }
        output = io.StringIO()
        with mock.patch.object(
            cli_main.uai,
            "connect",
            return_value=client,
        ) as connect:
            with redirect_stdout(output):
                exit_code = self._run_main(
                    [
                        "--connection",
                        "fixture.toml",
                        "exec",
                        "fixture.echo_exact",
                        "--params-json",
                        json.dumps(params, ensure_ascii=False),
                    ]
                )
        self.assertEqual(exit_code, 0)
        connect.assert_called_once_with("fixture.toml")
        self.assertEqual(
            client.calls,
            [("fixture.echo_exact", params)],
        )
        self.assertTrue(client.closed)
        self.assertEqual(
            json.loads(output.getvalue()),
            dict(client.result.raw_response),
        )

    def test_server_failure_keeps_raw_stdout_and_stable_exit(
        self,
    ) -> None:
        client = _Client(_result(False))
        output = io.StringIO()
        with mock.patch.object(
            cli_main.uai,
            "connect",
            return_value=client,
        ):
            with redirect_stdout(output):
                exit_code = self._run_main(
                    [
                        "--connection",
                        "fixture.toml",
                        "exec",
                        "fixture.echo_exact",
                        "--params-json",
                        "{}",
                    ]
                )
        self.assertEqual(
            exit_code,
            5,
            "server_command_failure_exit_code_mismatch",
        )
        self.assertEqual(len(client.calls), 1)
        self.assertEqual(
            json.loads(output.getvalue()),
            dict(client.result.raw_response),
        )

    def test_params_file_and_report_preserve_the_result(self) -> None:
        client = _Client(_result(True))
        params = {
            "unicode": "协议/蓝图",
            "large_integer": 9007199254740993,
            "nullable": None,
        }
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            params_path = root / "params.json"
            report_path = root / "result.json"
            params_path.write_text(
                json.dumps(params, ensure_ascii=False),
                encoding="utf-8",
            )
            output = io.StringIO()
            with mock.patch.object(
                cli_main.uai,
                "connect",
                return_value=client,
            ):
                with redirect_stdout(output):
                    exit_code = self._run_main(
                        [
                            "--connection",
                            "fixture.toml",
                            "exec",
                            "fixture.echo_exact",
                            "--params-file",
                            str(params_path),
                            "--report",
                            str(report_path),
                        ]
                    )
            self.assertEqual(exit_code, 0)
            self.assertEqual(
                client.calls,
                [("fixture.echo_exact", params)],
            )
            self.assertEqual(
                json.loads(report_path.read_text(encoding="utf-8")),
                dict(client.result.raw_response),
            )
            self.assertEqual(
                json.loads(output.getvalue()),
                dict(client.result.raw_response),
            )

    def test_cli_has_no_direct_transport_or_orchestration_path(
        self,
    ) -> None:
        tree = ast.parse(
            CLI_MAIN.read_text(encoding="utf-8-sig"),
            filename=str(CLI_MAIN),
        )
        forbidden_imports: list[str] = []
        execute_calls = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if (
                        alias.name.startswith("uai.network_transport")
                        or alias.name.startswith("http")
                    ):
                        forbidden_imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom) and node.module:
                if (
                    node.module.startswith("uai.network_transport")
                    or node.module.startswith("uai.uai_protocol")
                    or node.module.startswith("http")
                ):
                    forbidden_imports.append(node.module)
            elif (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "execute"
            ):
                execute_calls += 1
        self.assertEqual(
            forbidden_imports,
            [],
            "cli_direct_transport_or_protocol_import:"
            + ",".join(forbidden_imports),
        )
        self.assertEqual(
            execute_calls,
            1,
            "cli_exec_must_contain_one_client_execute_call",
        )


if __name__ == "__main__":
    unittest.main()
