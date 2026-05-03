from __future__ import annotations

import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PLUGIN_ROOT = (
    REPO_ROOT / "Plugins" / "UeAgentInterface"
    if (REPO_ROOT / "Plugins" / "UeAgentInterface").exists()
    else REPO_ROOT / "UeAgentInterface"
)
COMMAND_SOURCE_ROOT = PLUGIN_ROOT / "Source" / "UeAgentInterface" / "Private" / "Commands"
PRIVATE_SOURCE_ROOT = PLUGIN_ROOT / "Source" / "UeAgentInterface" / "Private"


def _source_files(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in {".cpp", ".h", ".inl"}
    )


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="ignore")


def _extract_function_bodies(text: str) -> list[tuple[str, int, str]]:
    results: list[tuple[str, int, str]] = []
    pattern = re.compile(
        r"bool\s+FUeAgentHttpServer::(Cmd[A-Za-z0-9_]+)\s*\([^)]*\)\s*(?:const\s*)?\{"
    )
    for match in pattern.finditer(text):
        start = match.end() - 1
        depth = 0
        end = None
        for index in range(start, len(text)):
            char = text[index]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    end = index + 1
                    break
        if end is None:
            continue
        line = text[: match.start()].count("\n") + 1
        results.append((match.group(1), line, text[start:end]))
    return results


class CommandSourceAuditTests(unittest.TestCase):
    def test_dispatch_targets_have_definitions(self) -> None:
        source_text_by_path = {path: _read(path) for path in _source_files(PRIVATE_SOURCE_ROOT)}
        function_defs: set[str] = set()
        for text in source_text_by_path.values():
            function_defs.update(
                re.findall(r"bool\s+FUeAgentHttpServer::(Cmd[A-Za-z0-9_]+)\s*\(", text)
            )

        dispatch_targets: dict[str, set[str]] = {}
        for text in source_text_by_path.values():
            for command, target in re.findall(
                r'CommandLower\s*==\s*TEXT\("([a-z][a-z0-9_]+)"\)\)\s*return\s+(Cmd[A-Za-z0-9_]+)\s*\(',
                text,
            ):
                dispatch_targets.setdefault(command, set()).add(target)
            for command, target in re.findall(
                r'\{\s*TEXT\("([a-z][a-z0-9_]+)"\)\s*,\s*&(?:FUeAgentHttpServer::)?(Cmd[A-Za-z0-9_]+)\s*\}',
                text,
            ):
                dispatch_targets.setdefault(command, set()).add(target)

        missing = sorted(
            f"{command}->{target}"
            for command, targets in dispatch_targets.items()
            for target in targets
            if target not in function_defs
        )
        duplicate_targets = sorted(
            f"{command}:{','.join(sorted(targets))}"
            for command, targets in dispatch_targets.items()
            if len(targets) > 1
        )

        self.assertEqual(missing, [])
        self.assertEqual(duplicate_targets, [])

    def test_command_param_reads_are_consumed(self) -> None:
        param_read_patterns = [
            re.compile(
                r'JsonTryGet\w*\s*\([^;\n]*?TEXT\("([^"]+)"\)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)'
            ),
            re.compile(
                r'\b(?:[A-Za-z_][A-Za-z0-9_]*->)?TryGet(?:Array|Object|String|Number|Bool)Field\s*'
                r'\(\s*TEXT\("([^"]+)"\)\s*,\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)'
            ),
        ]

        issues: list[str] = []
        for path in _source_files(COMMAND_SOURCE_ROOT):
            text = _read(path)
            for function_name, function_line, body in _extract_function_bodies(text):
                for pattern in param_read_patterns:
                    for match in pattern.finditer(body):
                        field_name, variable_name = match.groups()
                        rest = body[match.end() :]
                        if re.search(rf"\b{re.escape(variable_name)}\b", rest):
                            continue
                        absolute_line = function_line + body[: match.start()].count("\n")
                        rel_path = path.relative_to(REPO_ROOT).as_posix()
                        issues.append(
                            f"{rel_path}:{absolute_line} {function_name} reads '{field_name}' into {variable_name} but never consumes it"
                        )

        self.assertEqual(issues, [])


if __name__ == "__main__":
    unittest.main()
