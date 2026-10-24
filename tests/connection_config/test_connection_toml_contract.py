from __future__ import annotations

import importlib
import os
from pathlib import Path
import tempfile
import unittest


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
FORMAL_HTTP_TEMPLATE = (
    REPOSITORY_ROOT / "templates" / "connection.http.toml"
)


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


def _write(root: Path, text: str, name: str = "connection.toml") -> Path:
    path = root / name
    path.write_text(text, encoding="utf-8")
    return path


class ConnectionTomlContractTests(unittest.TestCase):
    def _api(self):
        try:
            uai = importlib.import_module("uai")
            config = importlib.import_module("uai.connection_config")
        except ModuleNotFoundError as exc:
            self.fail(f"connection_config_module_missing:{exc.name}")
        loader = getattr(config, "load_connection_toml", None)
        self.assertTrue(
            callable(loader),
            "load_connection_toml_missing",
        )
        return uai, config, loader

    def _assert_usage_error(
        self,
        path: Path,
        expected_code: str,
        *,
        environ: dict[str, str] | None = None,
    ) -> None:
        uai, _, loader = self._api()
        error_type = getattr(uai, "UsageError", None)
        self.assertIsNotNone(error_type, "public_usage_error_missing")
        with self.assertRaises(error_type) as caught:
            loader(path, environ={} if environ is None else environ)
        self.assertEqual(
            getattr(caught.exception, "code", None),
            expected_code,
            f"connection_error_code_mismatch:{caught.exception}",
        )
        self.assertEqual(caught.exception.diagnostic["code"], expected_code)
        self.assertEqual(caught.exception.diagnostic["message"], caught.exception.message)
        self.assertEqual(caught.exception.diagnostic["stage"], "connection_config")

    def test_valid_file_produces_an_immutable_snapshot(self) -> None:
        _, config, loader = self._api()
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            path = _write(root, VALID_TOML)
            snapshot = loader(path, environ={})

            self.assertIsInstance(
                snapshot,
                getattr(config, "ConnectionSnapshot"),
            )
            self.assertEqual(snapshot.source_path, path.resolve())
            self.assertEqual(snapshot.format_version, 1)
            self.assertEqual(snapshot.transport, "http")
            self.assertEqual(
                snapshot.endpoint,
                "http://127.0.0.1:8090",
            )
            self.assertEqual(snapshot.protocol_version, "current")
            self.assertEqual(snapshot.connect_timeout_seconds, 5.0)
            self.assertEqual(snapshot.io_timeout_seconds, 120.0)
            self.assertEqual(snapshot.authentication.mode, "none")
            self.assertIsNone(
                snapshot.authentication.get_secret_value(),
            )
            self.assertIs(
                snapshot.transport_options["http"]["tls_verify"],
                True,
            )
            self.assertEqual(
                snapshot.transport_options["http"]["route_path"],
                "/api/uai/command",
            )
            self.assertEqual(
                snapshot.transport_options["http"]["probe_path"],
                "/api/ping",
            )
            self.assertEqual(
                snapshot.transport_options["http"]["auth_header"],
                "X-UeAgentInterface-Token",
            )

            with self.assertRaises((AttributeError, TypeError)):
                snapshot.endpoint = "http://invalid"
            with self.assertRaises(TypeError):
                snapshot.transport_options["http"]["tls_verify"] = False

    def test_snapshot_does_not_reload_changed_toml(self) -> None:
        _, _, loader = self._api()
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            path = _write(root, VALID_TOML)
            snapshot = loader(path, environ={})
            path.write_text(
                VALID_TOML.replace(
                    "http://127.0.0.1:8090",
                    "http://127.0.0.1:9999",
                ),
                encoding="utf-8",
            )
            self.assertEqual(
                snapshot.endpoint,
                "http://127.0.0.1:8090",
            )

    def test_missing_and_invalid_toml_fail_before_connect(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            self._assert_usage_error(
                root / "missing.toml",
                "connection_file_missing",
            )
            malformed = _write(
                root,
                "format_version = [\n",
                "malformed.toml",
            )
            self._assert_usage_error(
                malformed,
                "connection_toml_invalid",
            )

    def test_format_version_is_required_and_supported(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            missing = _write(
                root,
                VALID_TOML.replace("format_version = 1\n", ""),
                "missing-version.toml",
            )
            self._assert_usage_error(
                missing,
                "connection_config_invalid",
            )
            unsupported = _write(
                root,
                VALID_TOML.replace(
                    "format_version = 1",
                    "format_version = 2",
                ),
                "unsupported-version.toml",
            )
            self._assert_usage_error(
                unsupported,
                "connection_format_unsupported",
            )

    def test_unknown_common_and_business_fields_are_rejected(self) -> None:
        cases = {
            "unknown-top-level.toml": VALID_TOML.replace(
                "format_version = 1",
                'format_version = 1\nunexpected = "value"',
            ),
            "unknown-connection.toml": VALID_TOML.replace(
                'endpoint = "http://127.0.0.1:8090"',
                'endpoint = "http://127.0.0.1:8090"\nasset_path = "/Game/X"',
            ),
            "business-table.toml": (
                VALID_TOML
                + '\n[business]\nhjson = "forbidden"\n'
            ),
            "unknown-http-option.toml": VALID_TOML.replace(
                "tls_verify = true",
                'tls_verify = true\nbusiness_retry = "forbidden"',
            ),
        }
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            for name, content in cases.items():
                with self.subTest(name=name):
                    path = _write(root, content, name)
                    self._assert_usage_error(
                        path,
                        "connection_config_invalid",
                    )

    def test_required_fields_and_types_are_strict(self) -> None:
        cases = {
            "missing-endpoint.toml": VALID_TOML.replace(
                'endpoint = "http://127.0.0.1:8090"\n',
                "",
            ),
            "transport-type.toml": VALID_TOML.replace(
                'transport = "http"',
                "transport = true",
            ),
            "timeout-type.toml": VALID_TOML.replace(
                "connect_seconds = 5.0",
                'connect_seconds = "5"',
            ),
            "timeout-positive.toml": VALID_TOML.replace(
                "io_seconds = 120.0",
                "io_seconds = 0.0",
            ),
            "tls-type.toml": VALID_TOML.replace(
                "tls_verify = true",
                'tls_verify = "true"',
            ),
            "endpoint-scheme.toml": VALID_TOML.replace(
                "http://127.0.0.1:8090",
                "ftp://127.0.0.1:8090",
            ),
            "endpoint-host.toml": VALID_TOML.replace(
                "http://127.0.0.1:8090",
                "http:///missing-host",
            ),
            "endpoint-credentials.toml": VALID_TOML.replace(
                "http://127.0.0.1:8090",
                "http://user:secret@127.0.0.1:8090",
            ),
        }
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            for name, content in cases.items():
                with self.subTest(name=name):
                    path = _write(root, content, name)
                    self._assert_usage_error(
                        path,
                        "connection_config_invalid",
                    )

    def test_only_http_transport_is_currently_supported(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            path = _write(
                Path(raw_root),
                VALID_TOML.replace(
                    'transport = "http"',
                    'transport = "tcp"',
                ),
            )
            self._assert_usage_error(
                path,
                "connection_transport_unsupported",
            )

    def test_bearer_env_is_explicit_snapshotted_and_redacted(self) -> None:
        _, _, loader = self._api()
        content = VALID_TOML.replace(
            'mode = "none"',
            'mode = "bearer_env"\nbearer_env = "UAI_TEST_TOKEN"',
        )
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            path = _write(root, content)
            environ = {"UAI_TEST_TOKEN": "first-secret"}
            snapshot = loader(path, environ=environ)
            environ["UAI_TEST_TOKEN"] = "changed-secret"
            self.assertEqual(
                snapshot.authentication.get_secret_value(),
                "first-secret",
            )
            self.assertNotIn("first-secret", repr(snapshot))

            missing = _write(root, content, "missing-env.toml")
            self._assert_usage_error(
                missing,
                "connection_secret_missing",
                environ={},
            )

    def test_formal_http_template_requires_an_explicit_secret_reference(
        self,
    ) -> None:
        self.assertTrue(
            FORMAL_HTTP_TEMPLATE.is_file(),
            "formal_http_connection_template_missing",
        )
        text = FORMAL_HTTP_TEMPLATE.read_text(encoding="utf-8")
        self.assertIn('mode = "bearer_env"', text)
        self.assertIn('bearer_env = "UAI_AUTH_TOKEN"', text)
        self.assertIn('route_path = "/api/uai/command"', text)
        self.assertNotIn('mode = "none"', text)
        self.assertNotIn("AuthToken=", text)

        _, _, loader = self._api()
        snapshot = loader(
            FORMAL_HTTP_TEMPLATE,
            environ={"UAI_AUTH_TOKEN": "fixture-secret"},
        )
        self.assertEqual(snapshot.authentication.mode, "bearer_env")
        self.assertEqual(
            snapshot.authentication.secret_source,
            "env:UAI_AUTH_TOKEN",
        )
        self.assertEqual(
            snapshot.authentication.get_secret_value(),
            "fixture-secret",
        )
        self.assertNotIn("fixture-secret", repr(snapshot))

    def test_bearer_file_is_resolved_relative_to_toml(self) -> None:
        _, _, loader = self._api()
        content = VALID_TOML.replace(
            'mode = "none"',
            'mode = "bearer_file"\nbearer_file = "secrets/uai.token"',
        )
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            secrets = root / "secrets"
            secrets.mkdir()
            secret_path = secrets / "uai.token"
            secret_path.write_text("file-secret", encoding="utf-8")
            config_path = _write(root, content)

            original_cwd = Path.cwd()
            try:
                other_cwd = root / "other"
                other_cwd.mkdir()
                os.chdir(other_cwd)
                snapshot = loader(config_path, environ={})
            finally:
                os.chdir(original_cwd)

            self.assertEqual(
                snapshot.authentication.get_secret_value(),
                "file-secret",
            )
            self.assertEqual(
                snapshot.authentication.secret_source,
                secret_path.resolve(),
            )
            self.assertNotIn("file-secret", repr(snapshot))

    def test_missing_or_empty_secret_file_is_a_usage_error(self) -> None:
        content = VALID_TOML.replace(
            'mode = "none"',
            'mode = "bearer_file"\nbearer_file = "secrets/uai.token"',
        )
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            config_path = _write(root, content)
            self._assert_usage_error(
                config_path,
                "connection_secret_missing",
            )

            secrets = root / "secrets"
            secrets.mkdir()
            secret_path = secrets / "uai.token"
            secret_path.write_text("", encoding="utf-8")
            self._assert_usage_error(
                config_path,
                "connection_secret_invalid",
            )

            secret_path.unlink()
            self.assertFalse(
                secret_path.exists(),
                "secret_file_handle_leaked_after_failed_load",
            )


if __name__ == "__main__":
    unittest.main()
