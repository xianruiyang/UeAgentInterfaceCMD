"""On-demand descriptions from the installed generated command contract."""

from __future__ import annotations

import json

from .commands import _BINDING_CATALOG
from .errors import UsageError


def describe_command(
    command_id: str, *, parameter: str | None = None, pointer: str = "",
    variant: str | None = None,
) -> dict[str, object]:
    """Read the generated base or variant contract without connecting."""
    binding = _BINDING_CATALOG.find(command_id)
    if binding is None:
        raise UsageError.at_source(code="command_unknown", message="command is not in the installed catalog",
                         facts={"stage": "command_metadata", "command_id": command_id})
    identity: dict[str, object] = {"command": command_id}
    variants = [{"variant_id": item.variant_id, "summary": item.summary} for item in binding.variants]
    selected_variant = None
    request_schema: dict[str, object] = {}
    if variant is not None:
        selected_variant = next((item for item in binding.variants if item.variant_id == variant), None)
        if selected_variant is None:
            raise UsageError.at_source(code="command_variant_unknown", message="variant is not defined for this command",
                             facts={"stage": "command_metadata", "command_id": command_id,
                                    "property_path": "variant", "actual_value": variant,
                                    "expected_value": [item.variant_id for item in binding.variants]})
        identity["variant_id"] = variant
        request_schema = json.loads(selected_variant.request_schema_json)
    elif variants:
        identity["variants"] = variants
    if parameter is None:
        if pointer:
            raise UsageError.at_source(code="schema_parameter_required", message="a schema pointer requires a parameter",
                             facts={"stage": "command_metadata", "command_id": command_id, "pointer": pointer, "property_path": "parameter", "actual_present": False})
        if selected_variant is not None:
            return {
                **identity,
                "summary": selected_variant.summary,
                "parameter_guidance": selected_variant.parameter_guidance,
                "result_guidance": selected_variant.result_guidance,
                "minimum_example": selected_variant.minimum_example,
                "request_schema": request_schema,
            }
        return {
            **identity,
            "parameters": [
                {"name": item.name, "type": item.wire_type, "required": item.required,
                 "nullable": item.nullable, "schema_available": bool(item.schema_json)}
                for item in binding.parameters
            ],
        }
    selected = next((item for item in binding.parameters if item.name == parameter), None)
    if selected is None:
        raise UsageError.at_source(code="command_parameter_unknown", message="parameter is not defined for this command",
                         facts={"stage": "command_metadata", "command_id": command_id, "parameter": parameter,
                                     "expected_value": [item.name for item in binding.parameters]})
    schema = request_schema.get("properties", {}).get(parameter) if selected_variant is not None else None
    if schema is None and selected.schema_json:
        schema = json.loads(selected.schema_json)
    if schema is None:
        return {**identity, "parameter": parameter, "type": selected.wire_type,
                "required": selected.required, "nullable": selected.nullable, "schema_available": False}
    if pointer:
        if not pointer.startswith("/"):
            raise UsageError.at_source(code="schema_pointer_invalid", message="schema pointer must start with /",
                             facts={"stage": "command_metadata", "command_id": command_id, "parameter": parameter, "pointer": pointer})
        try:
            for encoded in pointer[1:].split("/"):
                token = encoded.replace("~1", "/").replace("~0", "~")
                if isinstance(schema, list):
                    if not token.isdigit() or (len(token) > 1 and token.startswith("0")):
                        raise ValueError
                    schema = schema[int(token)]
                else:
                    schema = schema[token]
        except (KeyError, IndexError, ValueError, TypeError) as exc:
            raise UsageError.at_source(code="schema_pointer_not_found", message="schema pointer does not resolve",
                             facts={"stage": "command_metadata", "command_id": command_id, "parameter": parameter, "pointer": pointer}) from exc
    return {**identity, "parameter": parameter, "pointer": pointer, "schema": schema}


__all__ = ["describe_command"]
