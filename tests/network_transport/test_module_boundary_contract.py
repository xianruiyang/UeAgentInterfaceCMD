from __future__ import annotations

import ast
import re
from pathlib import Path
import unittest

from network_transport_test_support import (
    PLUGIN_PRODUCTION_ROOT,
    PYTHON_PRODUCTION_ROOT,
    require_network_transport_module,
)


PROJECT_INCLUDE_ROOTS = frozenset(
    {
        "CommandEdge",
        "Composition",
        "Core",
        "DomainAdapters",
        "LifecycleHost",
        "NetworkTransport",
        "UaiProtocol",
    }
)


def _python_imports(path: Path) -> tuple[tuple[int, str], ...]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    imports: list[tuple[int, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend((0, alias.name) for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append((node.level, node.module or ""))
    return tuple(imports)


def _cpp_project_includes(path: Path) -> tuple[str, ...]:
    source = path.read_text(encoding="utf-8")
    includes = re.findall(r'^\s*#include\s+"([^"]+)"', source, re.MULTILINE)
    return tuple(
        include
        for include in includes
        if include.split("/", 1)[0] in PROJECT_INCLUDE_ROOTS
    )


class NetworkTransportModuleBoundaryTests(unittest.TestCase):
    def test_python_transport_depends_only_on_stdlib_and_its_own_package(
        self,
    ) -> None:
        require_network_transport_module(self)
        violations: list[str] = []
        for path in sorted(PYTHON_PRODUCTION_ROOT.rglob("*.py")):
            for level, module in _python_imports(path):
                if level > 0:
                    continue
                if module == "uai.network_transport" or module.startswith(
                    "uai.network_transport."
                ):
                    continue
                root = module.split(".", 1)[0]
                if root in sys_stdlib_modules():
                    continue
                violations.append(
                    f"{path.relative_to(PYTHON_PRODUCTION_ROOT).as_posix()}=>{module}"
                )
        self.assertEqual(
            violations,
            [],
            "network_transport_external_dependency:" + ",".join(violations),
        )

    def test_cpp_transport_has_no_dependency_on_uai_business_modules(
        self,
    ) -> None:
        violations: list[str] = []
        for path in sorted(PLUGIN_PRODUCTION_ROOT.glob("*")):
            if path.suffix.casefold() not in {".h", ".cpp"}:
                continue
            for include in _cpp_project_includes(path):
                if not include.startswith("NetworkTransport/"):
                    violations.append(f"{path.name}=>{include}")
        self.assertEqual(
            violations,
            [],
            "network_transport_business_include:" + ",".join(violations),
        )


def sys_stdlib_modules() -> frozenset[str]:
    import sys

    return frozenset(sys.stdlib_module_names) | {"__future__"}


if __name__ == "__main__":
    unittest.main()
