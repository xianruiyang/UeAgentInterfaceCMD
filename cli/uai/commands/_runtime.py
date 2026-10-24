from __future__ import annotations

from dataclasses import dataclass, field
import keyword
from types import MappingProxyType
from typing import Protocol


def _required_text(field_name: str, value: str) -> str:
    normalized = str(value).strip()
    if not normalized:
        raise ValueError(f"{field_name}_missing")
    return normalized


class _Omitted:
    __slots__ = ()

    def __repr__(self) -> str:
        return "OMITTED"


OMITTED = _Omitted()


@dataclass(frozen=True, slots=True)
class CommandParameterBinding:
    name: str
    wire_type: str
    required: bool
    nullable: bool
    schema_json: str = field(default="", repr=False)

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "name",
            _required_text("command_parameter_name", self.name),
        )
        object.__setattr__(
            self,
            "wire_type",
            _required_text(
                "command_parameter_wire_type",
                self.wire_type,
            ),
        )
        if type(self.required) is not bool:
            raise TypeError("command_parameter_required_invalid")
        if type(self.nullable) is not bool:
            raise TypeError("command_parameter_nullable_invalid")
        if not isinstance(self.schema_json, str):
            raise TypeError("command_parameter_schema_invalid")


@dataclass(frozen=True, slots=True)
class CommandVariantBinding:
    variant_id: str
    request_schema_json: str = field(repr=False)
    summary: str = ""
    parameter_guidance: str = ""
    result_guidance: str = ""
    minimum_example: str = ""


@dataclass(frozen=True, slots=True)
class ModelResultFieldBinding:
    name: str
    source_path: tuple[str, ...]

    def __post_init__(self) -> None:
        name = _required_text("model_result_field_name", self.name)
        if not name.isidentifier() or keyword.iskeyword(name):
            raise ValueError("model_result_field_name_invalid")
        object.__setattr__(self, "name", name)
        source_path = tuple(
            _required_text("model_result_source_path_segment", segment)
            for segment in self.source_path
        )
        if not source_path:
            raise ValueError("model_result_source_path_missing")
        object.__setattr__(self, "source_path", source_path)


@dataclass(frozen=True, slots=True)
class CommandBinding:
    command_id: str
    binding_hash: str = field(repr=False)
    namespace: str = ""
    method: str = ""
    parameters: tuple[CommandParameterBinding, ...] = ()
    model_result_fields: tuple[ModelResultFieldBinding, ...] = ()
    min_wire_version: int = 1
    max_wire_version: int = 1
    status: str = "active"
    supports_operation_recovery: bool = False
    variants: tuple[CommandVariantBinding, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(
            self,
            "command_id",
            _required_text("command_binding_id", self.command_id),
        )
        binding_hash = _required_text(
            "command_binding_hash",
            self.binding_hash,
        )
        if not binding_hash.startswith("sha256:"):
            raise ValueError("command_binding_hash_invalid")
        object.__setattr__(self, "binding_hash", binding_hash)
        object.__setattr__(self, "parameters", tuple(self.parameters))
        names = tuple(item.name for item in self.parameters)
        if len(names) != len(set(names)):
            raise ValueError("command_binding_parameter_duplicate")
        object.__setattr__(self, "variants", tuple(self.variants))
        variant_ids = tuple(item.variant_id for item in self.variants)
        if len(variant_ids) != len(set(variant_ids)):
            raise ValueError("command_binding_variant_duplicate")
        object.__setattr__(
            self,
            "model_result_fields",
            tuple(self.model_result_fields),
        )
        model_result_names = tuple(
            item.name for item in self.model_result_fields
        )
        if len(model_result_names) != len(set(model_result_names)):
            raise ValueError("model_result_field_duplicate")
        if (
            isinstance(self.min_wire_version, bool)
            or isinstance(self.max_wire_version, bool)
            or self.min_wire_version <= 0
            or self.max_wire_version < self.min_wire_version
        ):
            raise ValueError("command_binding_wire_range_invalid")
        if self.status not in {"active", "dormant", "disabled", "deprecated"}:
            raise ValueError("command_binding_status_invalid")


class CommandBindingCatalog:
    __slots__ = ("_bindings",)

    def __init__(
        self,
        bindings: tuple[CommandBinding, ...],
    ) -> None:
        by_id: dict[str, CommandBinding] = {}
        for binding in bindings:
            if not isinstance(binding, CommandBinding):
                raise TypeError("command_binding_catalog_entry_invalid")
            if binding.command_id in by_id:
                raise ValueError("command_binding_catalog_duplicate")
            by_id[binding.command_id] = binding
        self._bindings = MappingProxyType(by_id)

    @property
    def command_ids(self) -> tuple[str, ...]:
        return tuple(sorted(self._bindings))

    @property
    def bindings(self) -> tuple[CommandBinding, ...]:
        return tuple(self._bindings[command_id] for command_id in self.command_ids)

    def find(self, command_id: str) -> CommandBinding | None:
        return self._bindings.get(command_id)


class CommandExecutor(Protocol):
    def execute(
        self,
        command_id: str,
        params: dict[str, object],
    ): ...


__all__ = [
    "CommandBinding",
    "CommandBindingCatalog",
    "CommandExecutor",
    "CommandParameterBinding",
    "ModelResultFieldBinding",
    "OMITTED",
]
