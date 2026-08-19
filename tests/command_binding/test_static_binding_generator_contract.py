from __future__ import annotations

import ast
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


REPO_ROOT = Path(__file__).resolve().parents[2]
FIXTURE = (
    Path(__file__).resolve().parent
    / "fixtures"
    / "cpp_registry_export_fixture.json"
)
GENERATOR = (
    REPO_ROOT
    / "tools"
    / "uai_binding"
    / "generate_bindings.py"
)
OLD_GENERATORS = (
    REPO_ROOT / "tools" / "generate_uai_core_commands.py",
    REPO_ROOT / "tools" / "generate_command_spec_surfaces.py",
)


class StaticBindingGeneratorContractTests(unittest.TestCase):
    def test_old_python_command_spec_generators_are_not_active(
        self,
    ) -> None:
        remaining = [
            str(path.relative_to(REPO_ROOT))
            for path in OLD_GENERATORS
            if path.exists()
        ]
        self.assertEqual(
            remaining,
            [],
            "old_python_command_spec_generators_active:"
            + ",".join(remaining),
        )

    def test_new_generator_only_consumes_cpp_manifest_file(
        self,
    ) -> None:
        self.assertTrue(
            GENERATOR.is_file(),
            f"cpp_manifest_binding_generator_missing:{GENERATOR}",
        )
        text = GENERATOR.read_text(encoding="utf-8-sig")
        for required in (
            "--manifest",
            "--output-root",
            "cpp_immutable_command_registry_export",
        ):
            with self.subTest(required=required):
                self.assertIn(
                    required,
                    text,
                    f"binding_generator_contract_missing:{required}",
                )
        for forbidden in (
            "command_specs",
            "uai_core",
            "rglob(",
            "docs/commands",
            "UeAgentCommandRegistry.cpp",
            "StartsWith",
            "prefix",
            "fallback",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(
                    forbidden,
                    text,
                    f"binding_generator_forbidden:{forbidden}",
                )

    def test_generator_rejects_non_cpp_manifest_source(self) -> None:
        self.assertTrue(
            GENERATOR.is_file(),
            "cpp_manifest_binding_generator_missing",
        )
        payload = json.loads(FIXTURE.read_text(encoding="utf-8"))
        payload["source"]["kind"] = "python_command_specs"
        with tempfile.TemporaryDirectory() as raw_root:
            root = Path(raw_root)
            invalid_manifest = root / "invalid_manifest.json"
            invalid_manifest.write_text(
                json.dumps(payload, ensure_ascii=False),
                encoding="utf-8",
            )
            completed = subprocess.run(
                [
                    sys.executable,
                    str(GENERATOR),
                    "--manifest",
                    str(invalid_manifest),
                    "--output-root",
                    str(root / "output"),
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(
                completed.returncode,
                0,
                "non_cpp_manifest_source_was_accepted",
            )

    def test_generator_emits_static_python_and_pyi(self) -> None:
        self.assertTrue(
            GENERATOR.is_file(),
            "cpp_manifest_binding_generator_missing",
        )
        with tempfile.TemporaryDirectory() as raw_root:
            output_root = Path(raw_root)
            completed = subprocess.run(
                [
                    sys.executable,
                    str(GENERATOR),
                    "--manifest",
                    str(FIXTURE),
                    "--output-root",
                    str(output_root),
                ],
                cwd=REPO_ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(
                completed.returncode,
                0,
                "binding_generator_failed:"
                + completed.stderr[-800:],
            )
            generated_py = output_root / "commands" / "generated.py"
            generated_pyi = output_root / "commands" / "generated.pyi"
            self.assertTrue(
                generated_py.is_file(),
                "generated_static_python_missing",
            )
            self.assertTrue(
                generated_pyi.is_file(),
                "generated_static_pyi_missing",
            )
            source = generated_py.read_text(encoding="utf-8-sig")
            tree = ast.parse(source, filename=str(generated_py))
            self.assertNotIn(
                "__getattr__",
                {
                    node.name
                    for node in ast.walk(tree)
                    if isinstance(
                        node,
                        (ast.FunctionDef, ast.AsyncFunctionDef),
                    )
                },
                "dynamic_generated_getattr_forbidden",
            )
            classes = {
                node.name: node
                for node in tree.body
                if isinstance(node, ast.ClassDef)
            }
            self.assertIn("FixtureCommands", classes)
            methods = {
                node.name: node
                for node in classes["FixtureCommands"].body
                if isinstance(node, ast.FunctionDef)
            }
            self.assertIn("echo_exact", methods)
            signature = methods["echo_exact"].args
            names = [
                argument.arg
                for argument in (
                    list(signature.args)
                    + list(signature.kwonlyargs)
                )
            ]
            self.assertEqual(
                names,
                [
                    "self",
                    "required_text",
                    "optional_note",
                    "nullable_value",
                    "large_integer",
                ],
            )
            defaults = dict(
                zip(
                    (
                        argument.arg
                        for argument in signature.kwonlyargs
                    ),
                    signature.kw_defaults,
                    strict=True,
                )
            )
            for optional_name in (
                "optional_note",
                "nullable_value",
            ):
                with self.subTest(optional=optional_name):
                    default = defaults.get(optional_name)
                    self.assertIsInstance(
                        default,
                        ast.Name,
                        f"omission_sentinel_missing:{optional_name}",
                    )
                    self.assertIn(
                        "OMITTED",
                        default.id.upper(),
                        f"omission_sentinel_misnamed:{optional_name}",
                    )
            execute_calls = [
                node
                for node in ast.walk(methods["echo_exact"])
                if isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "execute"
            ]
            self.assertEqual(
                len(execute_calls),
                1,
                "generated_method_must_call_execute_exactly_once",
            )
            self.assertEqual(
                ast.literal_eval(execute_calls[0].args[0]),
                "fixture.echo_exact",
            )
            self.assertIn(
                "def echo_exact",
                generated_pyi.read_text(encoding="utf-8-sig"),
                "generated_pyi_method_missing",
            )


if __name__ == "__main__":
    unittest.main()
