from __future__ import annotations

import ast
import importlib
import inspect
from pathlib import Path
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
CLI_MAIN = REPO_ROOT / "cli" / "uai_cli" / "main.py"

EXPECTED_PUBLIC_NAMES = frozenset(
    {
        "__version__",
        "connect",
        "Client",
        "Result",
        "Error",
        "UsageError",
        "SerializationError",
        "TransportError",
        "ProtocolError",
        "ServerCommandError",
    }
)


class PublicFacadeContractTests(unittest.TestCase):
    def test_root_facade_is_small_and_complete(self) -> None:
        uai = importlib.import_module("uai")
        actual = frozenset(getattr(uai, "__all__", ()))
        self.assertEqual(
            actual,
            EXPECTED_PUBLIC_NAMES,
            "public_uai_surface_mismatch:"
            f"missing={sorted(EXPECTED_PUBLIC_NAMES - actual)},"
            f"unexpected={sorted(actual - EXPECTED_PUBLIC_NAMES)}",
        )

    def test_connect_requires_only_one_connection_source(self) -> None:
        uai = importlib.import_module("uai")
        connect = getattr(uai, "connect", None)
        self.assertTrue(
            callable(connect),
            "public_uai_connect_missing",
        )
        parameters = tuple(inspect.signature(connect).parameters.values())
        self.assertEqual(
            len(parameters),
            1,
            "public_connect_must_only_accept_connection_toml",
        )
        self.assertEqual(parameters[0].name, "connection")
        self.assertIn(
            parameters[0].kind,
            (
                inspect.Parameter.POSITIONAL_ONLY,
                inspect.Parameter.POSITIONAL_OR_KEYWORD,
            ),
        )
        self.assertIs(
            parameters[0].default,
            inspect.Parameter.empty,
            "public_connect_connection_must_be_required",
        )

    def test_client_exposes_only_explicit_connection_lifecycle(self) -> None:
        uai = importlib.import_module("uai")
        client_type = getattr(uai, "Client", None)
        self.assertIsNotNone(client_type, "public_uai_client_missing")
        for member in (
            "close",
            "probe",
            "connection_state",
            "__enter__",
            "__exit__",
        ):
            with self.subTest(member=member):
                self.assertIsNotNone(
                    inspect.getattr_static(client_type, member, None),
                    f"public_client_member_missing:{member}",
                )

    def test_cli_connection_option_uses_public_facade(self) -> None:
        tree = ast.parse(
            CLI_MAIN.read_text(encoding="utf-8-sig"),
            filename=str(CLI_MAIN),
        )
        option_strings: set[str] = set()
        imports_uai = False
        calls_public_connect = False
        forbidden_imports: list[str] = []

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports_uai = imports_uai or alias.name == "uai"
                    if alias.name in {"tomllib", "tomli"}:
                        forbidden_imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom) and node.module:
                if node.module.startswith("uai.connection"):
                    forbidden_imports.append(node.module)
            elif isinstance(node, ast.Call):
                if (
                    isinstance(node.func, ast.Attribute)
                    and isinstance(node.func.value, ast.Name)
                    and node.func.value.id == "uai"
                    and node.func.attr == "connect"
                ):
                    calls_public_connect = True
                if (
                    isinstance(node.func, ast.Attribute)
                    and node.func.attr == "add_argument"
                ):
                    option_strings.update(
                        arg.value
                        for arg in node.args
                        if isinstance(arg, ast.Constant)
                        and isinstance(arg.value, str)
                        and arg.value.startswith("--")
                    )

        self.assertTrue(imports_uai, "cli_must_import_public_uai")
        self.assertEqual(
            forbidden_imports,
            [],
            "cli_must_not_own_connection_loader:"
            + ",".join(forbidden_imports),
        )
        self.assertIn(
            "--connection",
            option_strings,
            "cli_connection_toml_option_missing",
        )
        forbidden_overrides = {
            "--endpoint",
            "--transport",
            "--host",
            "--port",
            "--connect-timeout",
            "--io-timeout",
            "--token",
        }
        self.assertEqual(
            sorted(option_strings & forbidden_overrides),
            [],
            "cli_connection_override_options_forbidden",
        )
        self.assertTrue(
            calls_public_connect,
            "cli_must_route_connection_through_uai_connect",
        )


if __name__ == "__main__":
    unittest.main()
