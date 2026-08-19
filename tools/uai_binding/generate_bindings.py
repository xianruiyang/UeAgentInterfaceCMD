from __future__ import annotations

import argparse
import hashlib
import json
import keyword
from pathlib import Path
import re
from typing import Any, Mapping, Sequence


_SCHEMA = "uai.command_manifest.v1"
_WIRE_SCHEMA = "uai.command.v1"
_SOURCE_KIND = "cpp_immutable_command_registry_export"
_WIRE_TYPES = frozenset(
    {
        "any",
        "array",
        "boolean",
        "integer",
        "number",
        "object",
        "string",
    }
)
_HASH_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")


class BindingGenerationError(ValueError):
    pass


def _required_text(
    value: Any,
    *,
    field_name: str,
) -> str:
    if not isinstance(value, str) or not value.strip():
        raise BindingGenerationError(
            f"{field_name} must be a non-empty string"
        )
    return value.strip()


def _identifier(
    value: Any,
    *,
    field_name: str,
) -> str:
    text = _required_text(value, field_name=field_name)
    if not text.isidentifier() or keyword.iskeyword(text):
        raise BindingGenerationError(
            f"{field_name} must be a Python identifier"
        )
    return text


def _sha256_file(path: Path) -> str:
    return f"sha256:{hashlib.sha256(path.read_bytes()).hexdigest()}"


def _load_manifest(path: Path) -> dict[str, Any]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise BindingGenerationError(
            f"manifest cannot be loaded: {path}"
        ) from exc
    if not isinstance(payload, dict):
        raise BindingGenerationError("manifest root must be an object")
    if payload.get("schema") != _SCHEMA:
        raise BindingGenerationError("manifest schema is unsupported")
    if payload.get("wire_schema") != _WIRE_SCHEMA:
        raise BindingGenerationError("manifest wire schema is unsupported")
    if payload.get("wire_version") != 1:
        raise BindingGenerationError("manifest wire version is unsupported")
    source = payload.get("source")
    if (
        not isinstance(source, Mapping)
        or source.get("kind") != _SOURCE_KIND
    ):
        raise BindingGenerationError(
            "manifest source.kind must be "
            "cpp_immutable_command_registry_export"
        )
    registry_hash = payload.get("registry_hash")
    if (
        not isinstance(registry_hash, str)
        or not _HASH_PATTERN.fullmatch(registry_hash)
    ):
        raise BindingGenerationError("manifest registry_hash is invalid")
    commands = payload.get("commands")
    if not isinstance(commands, list):
        raise BindingGenerationError("manifest commands must be a list")

    seen_ids: set[str] = set()
    seen_methods: set[tuple[str, str]] = set()
    for command_index, command in enumerate(commands):
        if not isinstance(command, dict):
            raise BindingGenerationError(
                f"commands[{command_index}] must be an object"
            )
        command_label = f"commands[{command_index}]"
        command_id = _required_text(
            command.get("command_id"),
            field_name=f"{command_label}.command_id",
        )
        namespace = _identifier(
            command.get("namespace"),
            field_name=f"{command_label}.namespace",
        )
        method = _identifier(
            command.get("method"),
            field_name=f"{command_label}.method",
        )
        if command_id in seen_ids:
            raise BindingGenerationError(
                f"duplicate command_id: {command_id}"
            )
        if (namespace, method) in seen_methods:
            raise BindingGenerationError(
                f"duplicate generated method: {namespace}.{method}"
            )
        seen_ids.add(command_id)
        seen_methods.add((namespace, method))
        binding_hash = command.get("binding_hash")
        if (
            not isinstance(binding_hash, str)
            or not _HASH_PATTERN.fullmatch(binding_hash)
        ):
                raise BindingGenerationError(
                f"{command_label}.binding_hash is invalid"
            )
        status = command.get("status")
        if status not in {"active", "deprecated"}:
                raise BindingGenerationError(
                f"{command_label}.status is unsupported"
            )
        for version_name in (
            "min_wire_version",
            "max_wire_version",
        ):
            version = command.get(version_name)
            if (
                isinstance(version, bool)
                or not isinstance(version, int)
                or version <= 0
            ):
                    raise BindingGenerationError(
                    f"{command_label}.{version_name} is invalid"
                    )
        if command["max_wire_version"] < command["min_wire_version"]:
            raise BindingGenerationError(
                f"{command_label} wire version range is invalid"
            )
        parameters = command.get("parameters")
        if not isinstance(parameters, list):
            raise BindingGenerationError(
                f"{command_label}.parameters must be a list"
            )
        parameter_names: set[str] = set()
        for parameter_index, parameter in enumerate(parameters):
            if not isinstance(parameter, dict):
                raise BindingGenerationError(
                    f"{command_label}.parameters[{parameter_index}] "
                    "must be an object"
                )
            parameter_label = (
                f"{command_label}.parameters[{parameter_index}]"
            )
            name = _identifier(
                parameter.get("name"),
                field_name=f"{parameter_label}.name",
            )
            if name in parameter_names:
                raise BindingGenerationError(
                    f"duplicate parameter: {command_id}.{name}"
                )
            parameter_names.add(name)
            if parameter.get("wire_type") not in _WIRE_TYPES:
                raise BindingGenerationError(
                    f"{parameter_label}.wire_type is unsupported"
                )
            if type(parameter.get("required")) is not bool:
                raise BindingGenerationError(
                    f"{parameter_label}.required is invalid"
                )
            if type(parameter.get("nullable")) is not bool:
                raise BindingGenerationError(
                    f"{parameter_label}.nullable is invalid"
                )
    return payload


def _class_name(namespace: str) -> str:
    return "".join(part.capitalize() for part in namespace.split("_")) + (
        "Commands"
    )


def _type_hint(parameter: Mapping[str, Any]) -> str:
    base = {
        "any": "Any",
        "array": "list[Any]",
        "boolean": "bool",
        "integer": "int",
        "number": "float",
        "object": "dict[str, Any]",
        "string": "str",
    }[str(parameter["wire_type"])]
    if parameter["nullable"]:
        return f"{base} | None"
    return base


def _signature_parts(
    parameters: Sequence[Mapping[str, Any]],
) -> tuple[list[str], list[str]]:
    positional: list[str] = []
    keyword_only: list[str] = []
    seen_optional = False
    for parameter in parameters:
        name = str(parameter["name"])
        annotation = _type_hint(parameter)
        if parameter["required"] and not seen_optional:
            positional.append(f"{name}: {annotation}")
            continue
        seen_optional = seen_optional or not parameter["required"]
        if parameter["required"]:
            keyword_only.append(f"{name}: {annotation}")
        else:
            keyword_only.append(
                f"{name}: {annotation} | object = OMITTED"
            )
    return positional, keyword_only


def _method_lines(command: Mapping[str, Any]) -> list[str]:
    parameters = list(command["parameters"])
    positional, keyword_only = _signature_parts(parameters)
    signature = ["self", *positional]
    if keyword_only:
        signature.extend(["*", *keyword_only])
    lines = [
        f"    def {command['method']}(",
        *[f"        {item}," for item in signature],
        "    ):",
        "        params: dict[str, Any] = {}",
    ]
    for parameter in parameters:
        name = parameter["name"]
        if parameter["required"]:
            lines.append(f'        params["{name}"] = {name}')
        else:
            lines.extend(
                [
                    f"        if {name} is not OMITTED:",
                    f'            params["{name}"] = {name}',
                ]
            )
    lines.extend(
        [
            "        return self._client.execute(",
            f'            "{command["command_id"]}",',
            "            params,",
            "        )",
            "",
        ]
    )
    return lines


def _stub_method_lines(command: Mapping[str, Any]) -> list[str]:
    positional, keyword_only = _signature_parts(command["parameters"])
    keyword_only = [
        item.replace(" | object = OMITTED", " = ...")
        for item in keyword_only
    ]
    signature = ["self", *positional]
    if keyword_only:
        signature.extend(["*", *keyword_only])
    return [
        f"    def {command['method']}(",
        *[f"        {item}," for item in signature],
        "    ) -> Any: ...",
        "",
    ]


def _render_python(
    manifest: Mapping[str, Any],
    *,
    manifest_hash: str,
) -> str:
    commands = sorted(
        manifest["commands"],
        key=lambda item: item["command_id"],
    )
    namespaces: dict[str, list[Mapping[str, Any]]] = {}
    for command in commands:
        if command["status"] == "active":
            namespaces.setdefault(command["namespace"], []).append(
                command
            )
    lines = [
        '"""Generated from the C++ command registry manifest. Do not edit."""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from ._runtime import (",
        "    CommandBinding,",
        "    CommandBindingCatalog,",
        "    CommandExecutor,",
        "    CommandParameterBinding,",
        "    OMITTED,",
        ")",
        "",
        f'GENERATED_MANIFEST_HASH = "{manifest_hash}"',
        f'GENERATED_REGISTRY_HASH = "{manifest["registry_hash"]}"',
        "",
    ]
    for namespace, namespace_commands in sorted(namespaces.items()):
        class_name = _class_name(namespace)
        lines.extend(
            [
                f"class {class_name}:",
                '    __slots__ = ("_client",)',
                "",
                "    def __init__(",
                "        self,",
                "        client: CommandExecutor,",
                "    ) -> None:",
                "        self._client = client",
                "",
            ]
        )
        for command in namespace_commands:
            lines.extend(_method_lines(command))

    lines.extend(
        [
            "BINDING_CATALOG = CommandBindingCatalog(",
            "    (",
        ]
    )
    for command in commands:
        parameter_lines = []
        for parameter in command["parameters"]:
            parameter_lines.extend(
                [
                    "                CommandParameterBinding(",
                    f'                    name="{parameter["name"]}",',
                    (
                        "                    wire_type="
                        f'"{parameter["wire_type"]}",'
                    ),
                    (
                        "                    required="
                        f'{parameter["required"]!r},'
                    ),
                    (
                        "                    nullable="
                        f'{parameter["nullable"]!r},'
                    ),
                    "                ),",
                ]
            )
        lines.extend(
            [
                "        CommandBinding(",
                f'            command_id="{command["command_id"]}",',
                f'            binding_hash="{command["binding_hash"]}",',
                f'            namespace="{command["namespace"]}",',
                f'            method="{command["method"]}",',
                "            parameters=(",
                *parameter_lines,
                "            ),",
                (
                    "            min_wire_version="
                    f'{command["min_wire_version"]},'
                ),
                (
                    "            max_wire_version="
                    f'{command["max_wire_version"]},'
                ),
                f'            status="{command["status"]}",',
                "        ),",
            ]
        )
    lines.extend(["    )", ")", ""])

    slots = ", ".join(f'"{item}"' for item in sorted(namespaces))
    if len(namespaces) == 1:
        slots += ","
    lines.extend(
        [
            "class GeneratedCommandNamespaces:",
            f"    __slots__ = ({slots})",
            "",
            "    def __init__(",
            "        self,",
            "        client: CommandExecutor,",
            "    ) -> None:",
        ]
    )
    if namespaces:
        for namespace in sorted(namespaces):
            lines.append(
                f"        self.{namespace} = "
                f"{_class_name(namespace)}(client)"
            )
    else:
        lines.append("        pass")
    lines.extend(["", ""])

    lines.extend(
        [
            "class GeneratedClientBindingsMixin:",
            "    __slots__ = ()",
            "",
        ]
    )
    for namespace in sorted(namespaces):
        lines.extend(
            [
                "    @property",
                f"    def {namespace}(self) -> "
                f"{_class_name(namespace)}:",
                (
                    "        return "
                    f"self._generated_commands.{namespace}"
                ),
                "",
            ]
        )
    if not namespaces:
        lines.append("    pass")
        lines.append("")
    lines.extend(
        [
            "",
            "def bind_generated_commands(",
            "    client: CommandExecutor,",
            ") -> GeneratedCommandNamespaces:",
            "    return GeneratedCommandNamespaces(client)",
            "",
        ]
    )
    return "\n".join(lines)


def _render_stub(
    manifest: Mapping[str, Any],
) -> str:
    commands = sorted(
        (
            command
            for command in manifest["commands"]
            if command["status"] == "active"
        ),
        key=lambda item: item["command_id"],
    )
    namespaces: dict[str, list[Mapping[str, Any]]] = {}
    for command in commands:
        namespaces.setdefault(command["namespace"], []).append(command)
    lines = [
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from ._runtime import (",
        "    CommandBindingCatalog,",
        "    CommandExecutor,",
        ")",
        "",
        "GENERATED_MANIFEST_HASH: str",
        "GENERATED_REGISTRY_HASH: str",
        "BINDING_CATALOG: CommandBindingCatalog",
        "",
    ]
    for namespace, namespace_commands in sorted(namespaces.items()):
        lines.extend([f"class {_class_name(namespace)}:", ""])
        for command in namespace_commands:
            lines.extend(_stub_method_lines(command))
    lines.extend(["class GeneratedCommandNamespaces:", ""])
    for namespace in sorted(namespaces):
        lines.append(
            f"    {namespace}: {_class_name(namespace)}"
        )
    lines.extend(
        [
            "    def __init__(",
            "        self,",
            "        client: CommandExecutor,",
            "    ) -> None: ...",
            "",
            "class GeneratedClientBindingsMixin:",
            "",
        ]
    )
    for namespace in sorted(namespaces):
        lines.extend(
            [
                "    @property",
                f"    def {namespace}(self) -> "
                f"{_class_name(namespace)}: ...",
                "",
            ]
        )
    lines.extend(
        [
            "def bind_generated_commands(",
            "    client: CommandExecutor,",
            ") -> GeneratedCommandNamespaces: ...",
            "",
        ]
    )
    return "\n".join(lines)


def _write_or_check(
    path: Path,
    content: str,
    *,
    check: bool,
) -> None:
    normalized = content.rstrip() + "\n"
    if check:
        try:
            actual = path.read_text(encoding="utf-8-sig")
        except OSError as exc:
            raise BindingGenerationError(
                f"generated file is missing: {path}"
            ) from exc
        if actual != normalized:
            raise BindingGenerationError(
                f"generated file is stale: {path}"
            )
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalized, encoding="utf-8", newline="\n")


def generate(
    *,
    manifest_path: Path,
    output_root: Path,
    check: bool,
) -> None:
    manifest_path = manifest_path.resolve()
    manifest = _load_manifest(manifest_path)
    manifest_hash = _sha256_file(manifest_path)
    commands_root = output_root.resolve() / "commands"
    _write_or_check(
        commands_root / "generated.py",
        _render_python(manifest, manifest_hash=manifest_hash),
        check=check,
    )
    _write_or_check(
        commands_root / "generated.pyi",
        _render_stub(manifest),
        check=check,
    )


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Generate static Python bindings from one formal "
            "C++ command registry manifest."
        )
    )
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--check", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        generate(
            manifest_path=args.manifest,
            output_root=args.output_root,
            check=args.check,
        )
    except BindingGenerationError as exc:
        print(str(exc))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
