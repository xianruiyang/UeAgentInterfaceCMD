from __future__ import annotations

import argparse
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
_TUTORIAL_REFERENCE_PATTERN = re.compile(
    r"^(?:uai-docs|uai-skill):[^#\s]+#[^#\s]+$"
)

# These routes remain in the machine binding catalog because typed SDK owners
# call them internally.  They must not appear in the model-readable signature
# stub, where their opaque continuation/path parameters would look public.
_PUBLIC_SDK_PRIVATE_COMMAND_IDS = frozenset(
    {
        "asset_durable.journal.read",
        "asset_durable.journal.reconcile",
        "content_graph.export_workspace",
        "content_graph.import_workspace",
        "runtime.scenario.execute",
    }
)


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
        if status not in {"active", "dormant", "disabled", "deprecated"}:
                raise BindingGenerationError(
                f"{command_label}.status is unsupported"
            )
        tutorial_references = command.get("tutorial_references")
        if (
            not isinstance(tutorial_references, list)
            or not tutorial_references
        ):
            raise BindingGenerationError(
                f"{command_label}.tutorial_references must be "
                "a non-empty list"
            )
        seen_tutorial_references: set[str] = set()
        for reference_index, reference in enumerate(
            tutorial_references
        ):
            reference_label = (
                f"{command_label}.tutorial_references["
                f"{reference_index}]"
            )
            if (
                not isinstance(reference, str)
                or not _TUTORIAL_REFERENCE_PATTERN.fullmatch(reference)
            ):
                raise BindingGenerationError(
                    f"{reference_label} is invalid"
                )
            if reference in seen_tutorial_references:
                raise BindingGenerationError(
                    f"duplicate tutorial reference: {reference}"
                )
            seen_tutorial_references.add(reference)
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
            if "schema" in parameter and not isinstance(parameter["schema"], dict):
                raise BindingGenerationError(f"{parameter_label}.schema must be an object")
        if type(command.get("supports_operation_recovery", False)) is not bool:
            raise BindingGenerationError(f"{command_label}.supports_operation_recovery must be a boolean")
        variants = command.get("variants", [])
        if not isinstance(variants, list):
            raise BindingGenerationError(f"{command_label}.variants must be a list")
        variant_ids: set[str] = set()
        for variant_index, variant in enumerate(variants):
            variant_label = f"{command_label}.variants[{variant_index}]"
            if not isinstance(variant, dict):
                raise BindingGenerationError(f"{variant_label} must be an object")
            variant_id = _required_text(variant.get("variant_id"), field_name=f"{variant_label}.variant_id")
            if variant_id in variant_ids:
                raise BindingGenerationError(f"duplicate variant: {command_id}.{variant_id}")
            variant_ids.add(variant_id)
            if not isinstance(variant.get("request_schema"), dict):
                raise BindingGenerationError(f"{variant_label}.request_schema must be an object")
            for name in ("summary", "parameter_guidance", "result_guidance", "minimum_example"):
                if not isinstance(variant.get(name, ""), str):
                    raise BindingGenerationError(f"{variant_label}.{name} must be a string")
        model_result_fields = command.get("model_result_fields", [])
        if not isinstance(model_result_fields, list):
            raise BindingGenerationError(
                f"{command_label}.model_result_fields must be a list"
            )
        model_result_names: set[str] = set()
        for field_index, field in enumerate(model_result_fields):
            field_label = (
                f"{command_label}.model_result_fields[{field_index}]"
            )
            if not isinstance(field, dict):
                raise BindingGenerationError(
                    f"{field_label} must be an object"
                )
            name = _identifier(
                field.get("name"),
                field_name=f"{field_label}.name",
            )
            if name in model_result_names:
                raise BindingGenerationError(
                    f"duplicate model result field: {command_id}.{name}"
                )
            source_path = field.get("source_path")
            if not isinstance(source_path, list) or not source_path:
                raise BindingGenerationError(
                    f"{field_label}.source_path must be a non-empty list"
                )
            for segment_index, segment in enumerate(source_path):
                _required_text(
                    segment,
                    field_name=(
                        f"{field_label}.source_path[{segment_index}]"
                    ),
                )
            model_result_names.add(name)
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
    *,
    preserve_positional_order: bool = False,
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
        if preserve_positional_order:
            positional.append(f"{name}: {annotation} | object = OMITTED")
            continue
        if parameter["required"]:
            keyword_only.append(f"{name}: {annotation}")
        else:
            keyword_only.append(
                f"{name}: {annotation} | object = OMITTED"
            )
    return positional, keyword_only


def _method_lines(command: Mapping[str, Any]) -> list[str]:
    parameters = list(command["parameters"])
    # This method historically accepted (subject_ref, policy_id, parameters).
    # Making the middle argument optional must not reinterpret those calls.
    preserve_order = command["command_id"] == "capture.image.execute"
    positional, keyword_only = _signature_parts(
        parameters, preserve_positional_order=preserve_order
    )
    signature = ["self", *positional]
    if keyword_only:
        signature.extend(["*", *keyword_only])
    lines = [
        f"    def {command['method']}(",
        *[f"        {item}," for item in signature],
        "    ):",
        "        params: dict[str, Any] = {}",
    ]
    seen_optional = False
    for parameter in parameters:
        name = parameter["name"]
        if parameter["required"]:
            if preserve_order and seen_optional:
                lines.extend([
                    f"        if {name} is OMITTED:",
                    f"            raise TypeError(\"{command['method']}() missing required argument: '{name}'\")",
                ])
            lines.append(f'        params["{name}"] = {name}')
        else:
            seen_optional = True
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
    if command["command_id"] == "capture.image.execute" and any(
        parameter["name"] == "policy_id" and not parameter["required"]
        for parameter in command["parameters"]
    ):
        # The original positional call and the new omitted-policy keyword call
        # both keep parameters required to static consumers.
        explicit = dict(command)
        explicit["command_id"] = ""
        explicit["parameters"] = [
            {**parameter, "required": True}
            if parameter["name"] == "policy_id" else parameter
            for parameter in command["parameters"]
        ]
        omitted = {**command, "command_id": ""}
        return ["    @overload", *_stub_method_lines(explicit),
                "    @overload", *_stub_method_lines(omitted)]
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


def _render_python(manifest: Mapping[str, Any]) -> str:
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
        "    CommandVariantBinding,",
        "    ModelResultFieldBinding,",
        "    OMITTED,",
        ")",
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
            "_BINDING_CATALOG = CommandBindingCatalog(",
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
            if "schema" in parameter:
                schema_json = json.dumps(parameter["schema"], ensure_ascii=False, separators=(",", ":"))
                parameter_lines.insert(len(parameter_lines) - 1, f"                    schema_json={schema_json!r},")
        variant_lines = []
        for variant in command.get("variants", []):
            schema_json = json.dumps(variant["request_schema"], ensure_ascii=False, separators=(",", ":"))
            variant_lines.extend([
                "                CommandVariantBinding(",
                f"                    variant_id={variant['variant_id']!r},",
                f"                    request_schema_json={schema_json!r},",
                *[f"                    {name}={variant[name]!r},"
                  for name in ("summary", "parameter_guidance", "result_guidance", "minimum_example")
                  if variant.get(name)],
                "                ),",
            ])
        model_result_field_lines = []
        for field in command.get("model_result_fields", []):
            source_path = ", ".join(
                repr(segment) for segment in field["source_path"]
            )
            if len(field["source_path"]) == 1:
                source_path += ","
            model_result_field_lines.extend(
                [
                    "                ModelResultFieldBinding(",
                    f'                    name="{field["name"]}",',
                    f"                    source_path=({source_path}),",
                    "                ),",
                ]
            )
        model_result_argument_lines = []
        if model_result_field_lines:
            model_result_argument_lines = [
                "            model_result_fields=(",
                *model_result_field_lines,
                "            ),",
            ]
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
                *model_result_argument_lines,
                *(["            variants=(", *variant_lines, "            ),"] if variant_lines else []),
                *(['            supports_operation_recovery=True,']
                  if command.get("supports_operation_recovery", False) else []),
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
            and command["command_id"] not in _PUBLIC_SDK_PRIVATE_COMMAND_IDS
        ),
        key=lambda item: item["command_id"],
    )
    namespaces: dict[str, list[Mapping[str, Any]]] = {}
    for command in commands:
        namespaces.setdefault(command["namespace"], []).append(command)
    lines = [
        "from __future__ import annotations",
        "",
        "from typing import Any, overload",
        "",
        "from ._runtime import (",
        "    CommandExecutor,",
        ")",
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


def _write(path: Path, content: str) -> None:
    normalized = content.rstrip() + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(normalized, encoding="utf-8", newline="\n")


def generate(
    *,
    manifest_path: Path,
    output_root: Path,
) -> None:
    manifest_path = manifest_path.resolve()
    manifest = _load_manifest(manifest_path)
    commands_root = output_root.resolve() / "commands"
    _write(
        commands_root / "generated.py",
        _render_python(manifest),
    )
    _write(
        commands_root / "generated.pyi",
        _render_stub(manifest),
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
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        generate(
            manifest_path=args.manifest,
            output_root=args.output_root,
        )
    except BindingGenerationError as exc:
        print(str(exc))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
