from __future__ import annotations

from contextlib import redirect_stdout
import io
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import uai
from uai_cli import main as cli_main


VALID_TOML = """\
format_version = 1

[connection]
transport = "http"
endpoint = "http://127.0.0.1:8090"

[protocol]
version = "current"

[timeouts]
connect_seconds = 5.0
io_seconds = 120.0

[authentication]
mode = "none"

[transport_options.http]
tls_verify = true
route_path = "/api/uai/command"
probe_path = "/api/ping"
auth_header = "X-UeAgentInterface-Token"
"""


class _CliClient:
    def __init__(self) -> None:
        self.connection_state = "open"
        self.closed = False

    def __enter__(self):
        return self

    def __exit__(self, _exc_type, _exc_value, _traceback) -> None:
        self.closed = True


class PublicConnectionLifecycleTests(unittest.TestCase):
    def _connection_file(self, root: Path) -> Path:
        path = root / "connection.toml"
        path.write_text(VALID_TOML, encoding="utf-8")
        return path

    def test_one_line_connect_returns_client_without_eager_network(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            path = self._connection_file(Path(raw_root))
            with mock.patch(
                "uai.network_transport.http.StdlibHttpExchange.exchange"
            ) as exchange:
                client = uai.connect(path)
                self.assertIsInstance(client, uai.Client)
                self.assertEqual(client.connection_state, "open")
                self.assertEqual(
                    client._transport._config.connect_timeout_seconds,
                    5.0,
                )
                self.assertEqual(
                    client._transport._config.io_timeout_seconds,
                    120.0,
                )
                exchange.assert_not_called()
                client.close()
                client.close()
                self.assertEqual(client.connection_state, "closed")

    def test_context_manager_closes_the_owned_transport(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            path = self._connection_file(Path(raw_root))
            with uai.connect(path) as client:
                self.assertEqual(client.connection_state, "open")
            self.assertEqual(client.connection_state, "closed")

    def test_cli_show_delegates_the_same_path_to_public_connect(self) -> None:
        client = _CliClient()
        with tempfile.TemporaryDirectory() as raw_root:
            path = self._connection_file(Path(raw_root))
            output = io.StringIO()
            with mock.patch.object(
                cli_main.uai,
                "connect",
                return_value=client,
            ) as connect:
                with redirect_stdout(output):
                    exit_code = cli_main.main(
                        [
                            "--connection",
                            str(path),
                            "connection",
                            "show",
                            "--format",
                            "json",
                        ]
                    )
            self.assertEqual(exit_code, 0)
            connect.assert_called_once_with(str(path))
            self.assertTrue(client.closed)
            self.assertEqual(output.getvalue().strip(), '{"connection_state":"open"}')


if __name__ == "__main__":
    unittest.main()
