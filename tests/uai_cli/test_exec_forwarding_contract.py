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
    def test_local_failures_keep_message_format_report_and_exit_without_retry(self) -> None:
        for error_type, code in ((uai.UsageError, 2), (uai.TransportError, 3),
                                 (uai.SerializationError, 4), (uai.ProtocolError, 4)):
            for output_format in ("compact", "json"):
                with self.subTest(error=error_type.__name__, format=output_format), tempfile.TemporaryDirectory() as directory:
                    report = Path(directory) / "failure.json"
                    diagnostic = {"code": "fixture_failed", "message": "Specific reason at 字段 /commands/2",
                                  "stage": "command_protocol", "json_pointer": "/commands/2",
                                  "cause": {"message": "nested cause", "actual_value": {"identity": "business", "hash": "value"}},
                                  "unchecked": [{"reason": "request rejected"}]}
                    failure = error_type(code="fixture_failed", message=diagnostic["message"], diagnostic=diagnostic)
                    output, errors = io.StringIO(), io.StringIO()
                    with mock.patch.object(cli_main.uai, "connect_project", side_effect=failure) as connect:
                        with redirect_stdout(output), redirect_stderr(errors):
                            actual = cli_main.main(["exec", "fixture.echo_exact", "--format", output_format,
                                                    "--report", str(report)])
                    self.assertEqual(actual, code)
                    connect.assert_called_once()
                    self.assertEqual(output.getvalue(), "")
                    self.assertIn(failure.message, errors.getvalue())
                    saved = json.loads(report.read_text(encoding="utf-8"))
                    self.assertEqual(saved["error"]["diagnostic"]["message"], failure.message)
                    self.assertEqual(saved["error"]["diagnostic"], diagnostic)
                    self.assertFalse(saved["ok"])
                    self.assertNotIn("mutation_started", saved["error"])
                    if output_format == "json":
                        self.assertEqual(json.loads(errors.getvalue()), saved)

    def test_report_failure_keeps_completed_command_stdout_and_never_replays(self) -> None:
        client = _Client(_result(True))
        output, errors = io.StringIO(), io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            with mock.patch.object(cli_main.uai, "connect_project", return_value=client):
                with redirect_stdout(output), redirect_stderr(errors):
                    code = cli_main.main(["exec", "fixture.echo_exact", "--format", "json", "--report", directory])
        self.assertEqual(code, 2)
        self.assertTrue(json.loads(output.getvalue())["ok"])
        self.assertEqual(json.loads(errors.getvalue())["error"]["code"], "cli_report_write_failed")
        self.assertEqual(len(client.calls), 1)

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
                        "--format", "json",
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
            {
                "ok": True,
                "payload": dict(client.result.payload),
                "error": None,
            },
        )

    def test_server_failure_keeps_model_stdout_and_stable_exit(
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
                        "--format", "json",
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
            {
                "ok": False,
                "payload": dict(client.result.payload),
                "error": dict(client.result.error),
            },
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
                            "--format", "json",
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
                {
                    "ok": True,
                    "payload": dict(client.result.payload),
                    "error": None,
                },
            )
            self.assertEqual(
                json.loads(output.getvalue()),
                {
                    "ok": True,
                    "payload": dict(client.result.payload),
                    "error": None,
                },
            )

    def test_default_display_keeps_json_report_and_failure_exit(self) -> None:
        client = _Client(_result(False))
        output = io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "result.json"
            with mock.patch.object(cli_main.uai, "connect_project", return_value=client):
                with redirect_stdout(output):
                    code = self._run_main(["exec", "fixture.echo_exact", "--report", str(report)])
            self.assertEqual(code, 5)
            self.assertIn("ok: false", output.getvalue())
            self.assertIn("large_integer: 9007199254740993", output.getvalue())
            self.assertIn("code: fixture_failed", output.getvalue())
            saved = json.loads(report.read_text(encoding="utf-8"))
            self.assertEqual(saved, {"ok": False, "payload": dict(client.result.payload), "error": dict(client.result.error)})
        self.assertEqual(client.calls, [("fixture.echo_exact", {})])

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
