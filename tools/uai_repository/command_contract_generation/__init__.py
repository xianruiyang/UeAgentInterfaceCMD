"""Generate SDK and documentation projections from the frozen C++ registry."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any, Mapping


_IDENTITY = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
_COMMAND_ID = re.compile(
    r"^[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+$"
)
_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
_WIRE_TYPES = {
    "boolean",
    "integer",
    "number",
    "string",
    "object",
    "array",
    "any",
}
_AVAILABILITY = {"enabled", "disabled"}
_SIDE_EFFECTS = {
    "none",
    "editor_state",
    "asset_state",
    "world_state",
    "external_state",
}


class CommandProjectionError(ValueError):
    """A stable projection failure returned to repository tooling."""

    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code


@dataclass(frozen=True)
class FieldProjection:
    name: str
    wire_type: str
    required: bool
    nullable: bool
    description: str


@dataclass(frozen=True)
class ErrorProjection:
    code: str
    description: str


@dataclass(frozen=True)
class PurposeProjection:
    summary: str
    target: str
    preconditions: tuple[str, ...]
    parameter_guidance: str
    result_guidance: str
    failure_guidance: str
    side_effect_guidance: str
    minimum_example: str
    related_flows: tuple[str, ...]
    keywords: tuple[str, ...]
    synonyms: tuple[str, ...]


@dataclass(frozen=True)
class CommandProjection:
    command_id: str
    python_namespace: str
    python_function: str
    contract_version: int
    contract_hash: str
    public_owner: str
    availability: str
    side_effect: str
    state_layers: tuple[str, ...]
    input_fields: tuple[FieldProjection, ...]
    result_fields: tuple[FieldProjection, ...]
    errors: tuple[ErrorProjection, ...]
    purpose: PurposeProjection


@dataclass(frozen=True)
class RegistryProjection:
    registry_hash: str
    commands: tuple[CommandProjection, ...]


def _object(value: Any, code: str) -> Mapping[str, Any]:
    if not isinstance(value, dict):
        raise CommandProjectionError(code, "expected an object")
    return value


def _text(value: Any, code: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise CommandProjectionError(code, "expected non-empty text")
    return value.strip()


def _text_tuple(value: Any, code: str, *, allow_empty: bool = False) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise CommandProjectionError(code, "expected an array of text")
    result = tuple(_text(item, code) for item in value)
    if not allow_empty and not result:
        raise CommandProjectionError(code, "expected at least one text item")
    if len(result) != len(set(result)):
        raise CommandProjectionError(code, "text items must be unique")
    return result


def _fields(value: Any) -> tuple[FieldProjection, ...]:
    if not isinstance(value, list):
        raise CommandProjectionError(
            "command_projection_incomplete", "fields must be an array"
        )
    result: list[FieldProjection] = []
    names: set[str] = set()
    for raw in value:
        item = _object(raw, "command_projection_incomplete")
        try:
            name = _text(item["name"], "command_projection_incomplete")
            wire_type = _text(
                item["wire_type"], "command_projection_incomplete"
            )
            required = item["required"]
            nullable = item["nullable"]
            description = _text(
                item["description"], "command_projection_incomplete"
            )
        except KeyError as exc:
            raise CommandProjectionError(
                "command_projection_incomplete", f"missing field member {exc}"
            ) from exc
        if not _IDENTITY.fullmatch(name) or wire_type not in _WIRE_TYPES:
            raise CommandProjectionError(
                "command_projection_incomplete", "invalid field contract"
            )
        if not isinstance(required, bool) or not isinstance(nullable, bool):
            raise CommandProjectionError(
                "command_projection_incomplete", "field flags must be boolean"
            )
        if name in names:
            raise CommandProjectionError(
                "command_projection_field_duplicate", name
            )
        names.add(name)
        result.append(
            FieldProjection(
                name,
                wire_type,
                required,
                nullable,
                description,
            )
        )
    return tuple(result)


def _errors(value: Any) -> tuple[ErrorProjection, ...]:
    if not isinstance(value, list) or not value:
        raise CommandProjectionError(
            "command_projection_incomplete", "errors must be non-empty"
        )
    result: list[ErrorProjection] = []
    codes: set[str] = set()
    for raw in value:
        item = _object(raw, "command_projection_incomplete")
        try:
            code = _text(item["code"], "command_projection_incomplete")
            description = _text(
                item["description"], "command_projection_incomplete"
            )
        except KeyError as exc:
            raise CommandProjectionError(
                "command_projection_incomplete", f"missing error member {exc}"
            ) from exc
        if not _IDENTITY.fullmatch(code):
            raise CommandProjectionError(
                "command_projection_incomplete", "invalid error code"
            )
        if code in codes:
            raise CommandProjectionError(
                "command_projection_error_duplicate", code
            )
        codes.add(code)
        result.append(ErrorProjection(code, description))
    return tuple(result)


def _purpose(value: Any) -> PurposeProjection:
    item = _object(value, "command_projection_incomplete")
    try:
        return PurposeProjection(
            summary=_text(item["summary"], "command_projection_incomplete"),
            target=_text(item["target"], "command_projection_incomplete"),
            preconditions=_text_tuple(
                item["preconditions"], "command_projection_incomplete"
            ),
            parameter_guidance=_text(
                item["parameter_guidance"], "command_projection_incomplete"
            ),
            result_guidance=_text(
                item["result_guidance"], "command_projection_incomplete"
            ),
            failure_guidance=_text(
                item["failure_guidance"], "command_projection_incomplete"
            ),
            side_effect_guidance=_text(
                item["side_effect_guidance"], "command_projection_incomplete"
            ),
            minimum_example=_text(
                item["minimum_example"], "command_projection_incomplete"
            ),
            related_flows=_text_tuple(
                item["related_flows"], "command_projection_incomplete"
            ),
            keywords=_text_tuple(
                item["keywords"], "command_projection_incomplete"
            ),
            synonyms=_text_tuple(
                item.get("synonyms", []),
                "command_projection_incomplete",
                allow_empty=True,
            ),
        )
    except KeyError as exc:
        raise CommandProjectionError(
            "command_projection_incomplete", f"missing purpose member {exc}"
        ) from exc


def _command(value: Any) -> CommandProjection:
    item = _object(value, "command_projection_incomplete")
    required = {
        "command_id",
        "python_namespace",
        "python_function",
        "contract_version",
        "contract_hash",
        "public_owner",
        "availability",
        "side_effect",
        "state_layers",
        "input_fields",
        "result_fields",
        "errors",
        "purpose",
    }
    if not required <= set(item):
        raise CommandProjectionError(
            "command_projection_incomplete", "command members are incomplete"
        )
    command_id = _text(item["command_id"], "command_projection_incomplete")
    namespace = _text(
        item["python_namespace"], "command_projection_incomplete"
    )
    function = _text(
        item["python_function"], "command_projection_incomplete"
    )
    if (
        not _COMMAND_ID.fullmatch(command_id)
        or not _IDENTITY.fullmatch(namespace)
        or not _IDENTITY.fullmatch(function)
    ):
        raise CommandProjectionError(
            "command_projection_identity_invalid", command_id
        )
    contract_hash = _text(
        item["contract_hash"], "command_projection_incomplete"
    )
    if not _SHA256.fullmatch(contract_hash):
        raise CommandProjectionError(
            "command_projection_hash_invalid", contract_hash
        )
    version = item["contract_version"]
    availability = item["availability"]
    side_effect = item["side_effect"]
    state_layers = _text_tuple(
        item["state_layers"], "command_projection_incomplete"
    )
    if (
        not isinstance(version, int)
        or isinstance(version, bool)
        or version < 1
        or availability not in _AVAILABILITY
        or side_effect not in _SIDE_EFFECTS
    ):
        raise CommandProjectionError(
            "command_projection_incomplete", "invalid command status"
        )
    result_fields = _fields(item["result_fields"])
    if not result_fields:
        raise CommandProjectionError(
            "command_projection_incomplete", "result schema is empty"
        )
    return CommandProjection(
        command_id=command_id,
        python_namespace=namespace,
        python_function=function,
        contract_version=version,
        contract_hash=contract_hash,
        public_owner=_text(
            item["public_owner"], "command_projection_incomplete"
        ),
        availability=availability,
        side_effect=side_effect,
        state_layers=state_layers,
        input_fields=_fields(item["input_fields"]),
        result_fields=result_fields,
        errors=_errors(item["errors"]),
        purpose=_purpose(item["purpose"]),
    )


def load_projection(text: str) -> RegistryProjection:
    """Parse one projection exported by ``FUeAgentImmutableCommandRegistry``."""

    try:
        root = json.loads(text)
    except (TypeError, json.JSONDecodeError) as exc:
        raise CommandProjectionError(
            "command_projection_json_invalid", str(exc)
        ) from exc
    root = _object(root, "command_projection_incomplete")
    if root.get("schema") != "uai.immutable_command_registry.v1":
        raise CommandProjectionError(
            "command_projection_schema_invalid", "unsupported registry schema"
        )
    source = _object(root.get("source"), "command_projection_incomplete")
    if source.get("kind") != "cpp_immutable_command_registry":
        raise CommandProjectionError(
            "command_projection_source_invalid", "projection is not from C++"
        )
    registry_hash = _text(
        root.get("registry_hash"), "command_projection_incomplete"
    )
    if not _SHA256.fullmatch(registry_hash):
        raise CommandProjectionError(
            "command_projection_hash_invalid", registry_hash
        )
    raw_commands = root.get("commands")
    if not isinstance(raw_commands, list) or not raw_commands:
        raise CommandProjectionError(
            "command_projection_incomplete", "commands must be non-empty"
        )
    commands = tuple(_command(item) for item in raw_commands)
    ids: set[str] = set()
    bindings: set[tuple[str, str]] = set()
    for command in commands:
        if command.command_id in ids:
            raise CommandProjectionError(
                "command_projection_id_duplicate", command.command_id
            )
        ids.add(command.command_id)
        binding = (command.python_namespace, command.python_function)
        if binding in bindings:
            raise CommandProjectionError(
                "command_projection_python_binding_duplicate",
                ".".join(binding),
            )
        bindings.add(binding)
    return RegistryProjection(registry_hash, commands)


def render_python_binding(
    projection: RegistryProjection, namespace: str
) -> str:
    """Render thin exact-command functions for one Python namespace."""

    selected = [
        command
        for command in projection.commands
        if command.python_namespace == namespace
        and command.availability == "enabled"
    ]
    if not selected:
        raise CommandProjectionError(
            "command_projection_namespace_missing", namespace
        )
    lines = [
        '"""Generated from the immutable C++ command registry."""',
        "",
        f"CPP_REGISTRY_HASH = {projection.registry_hash!r}",
        "",
    ]
    for command in selected:
        constant = f"{command.python_function.upper()}_COMMAND_CONTRACT_HASH"
        lines.extend(
            [
                f"{constant} = {command.contract_hash!r}",
                "",
                f"def {command.python_function}(client, **params):",
                f"    return client.execute_exact({command.command_id!r}, params, contract_hash={constant})",
                "",
            ]
        )
    return "\n".join(lines)


def render_markdown(
    projection: RegistryProjection, namespace: str
) -> str:
    """Render command reference text from the same immutable projection."""

    selected = [
        command
        for command in projection.commands
        if command.python_namespace == namespace
    ]
    if not selected:
        raise CommandProjectionError(
            "command_projection_namespace_missing", namespace
        )
    lines = [
        f"# `{namespace}` command contracts",
        "",
        f"C++ registry: `{projection.registry_hash}`",
        "",
    ]
    for command in selected:
        purpose = command.purpose
        lines.extend(
            [
                f"## `{command.command_id}`",
                "",
                purpose.summary,
                "",
                f"- Contract: `{command.contract_version}` / `{command.contract_hash}`",
                f"- Owner: `{command.public_owner}`",
                f"- Target: {purpose.target}",
                f"- Side effect: `{command.side_effect}` — {purpose.side_effect_guidance}",
                f"- State layers: {', '.join(command.state_layers)}",
                f"- Parameters: {purpose.parameter_guidance}",
                f"- Result: {purpose.result_guidance}",
                f"- Failures: {purpose.failure_guidance}",
                f"- Discovery keywords: {', '.join(purpose.keywords)}",
                f"- Discovery synonyms: {', '.join(purpose.synonyms) or '(none)' }",
                f"- Minimum example: `{purpose.minimum_example}`",
                "",
                "Declared errors:",
                "",
            ]
        )
        lines.extend(
            f"- `{error.code}`: {error.description}"
            for error in command.errors
        )
        lines.append("")
    return "\n".join(lines)


__all__ = [
    "CommandProjectionError",
    "RegistryProjection",
    "load_projection",
    "render_markdown",
    "render_python_binding",
]
