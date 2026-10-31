from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any

from .errors import ProtocolError, UsageError


class RigBakeContextHandle:
    """Retain native binding/revision custody for the existing bake commands."""

    __slots__ = ("_client", "_sequence_ref", "_binding_name", "_controls", "_animation")

    def __init__(self, client: Any, payload: Mapping[str, Any]) -> None:
        context = payload.get("bake_context")
        controls = context.get("controls_input") if isinstance(context, Mapping) else None
        if not isinstance(controls, Mapping) or not isinstance(controls.get("expected_revision"), Mapping):
            raise ProtocolError(code="rig_bake_context_invalid", message="Bake context has no complete controls input.")
        self._client = client
        self._sequence_ref = context["sequence_ref"]
        self._binding_name = context["binding_name"]
        self._controls = deepcopy(dict(controls))
        animation = context.get("animation_input")
        if animation is not None and (not isinstance(animation, Mapping)
                                      or not isinstance(animation.get("expected_revision"), Mapping)):
            raise ProtocolError(code="rig_bake_context_invalid", message="Bake context has an incomplete animation input.")
        self._animation = deepcopy(dict(animation)) if animation is not None else None

    def __repr__(self) -> str:
        return f"RigBakeContextHandle(sequence_ref={self.sequence_ref!r}, binding_name={self.binding_name!r})"

    @property
    def sequence_ref(self) -> str:
        return self._sequence_ref

    @property
    def binding_name(self) -> str:
        return self._binding_name

    @property
    def authored_range(self) -> dict[str, Any]:
        return deepcopy(self._controls["authored_range"])

    @property
    def sample_rate(self) -> dict[str, Any]:
        return deepcopy(self._controls["sample_rate"])

    def bake_controls(self, *, context: Mapping[str, Any] | None = None):
        """Bake into this sequence; use a fresh query after editing or restarting."""
        return self._client.rig.control_bake_controls(
            self._sequence_ref, deepcopy(self._controls), context=context)

    def bake_animation(self, *, context: Mapping[str, Any] | None = None):
        """Export to the existing animation named by the context query."""
        if self._animation is None:
            raise UsageError(code="rig_bake_animation_target_missing",
                             message="Query bake context with target_animation_ref before exporting animation.")
        return self._client.rig.control_bake_animation(
            self._animation["target_animation_ref"], deepcopy(self._animation), context=context)


__all__ = ["RigBakeContextHandle"]
