"""Typed SDK custody for one VoxelGrid authoring session."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TYPE_CHECKING

from .commands import OMITTED
from .errors import UsageError

if TYPE_CHECKING:
    from .result import Result


def _required_text(value: object, *, field_name: str, property_path: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise UsageError.at_source(
            code=f"voxel_grid_{field_name}_invalid",
            message=f"voxel-grid {field_name} is unavailable",
            facts={"property_path": property_path, "expected_value": "non-empty string", "actual_type": type(value).__name__},
        )
    return value.strip()


def _required_revision(value: object, *, property_path: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise UsageError.at_source(
            code="voxel_grid_revision_invalid",
            message="voxel-grid continuation revision is unavailable",
            facts={"property_path": property_path, "expected_value": "non-negative integer", "actual_type": type(value).__name__},
        )
    return value


def _continuation(payload: object) -> tuple[str, int]:
    if not isinstance(payload, Mapping):
        raise UsageError.at_source(
            code="voxel_grid_continuation_missing",
            message="voxel-grid result has no continuation state",
            facts={"property_path": "payload", "expected_value": "object with session_id and revision",
                   "actual_type": type(payload).__name__},
        )
    source: Mapping[str, Any] = payload
    prefix = "payload"
    readback = payload.get("readback")
    if (
        isinstance(readback, Mapping)
        and "session_id" in readback
        and "revision" in readback
    ):
        source = readback
        prefix += ".readback"
    return (
        _required_text(source.get("session_id"), field_name="session", property_path=f"{prefix}.session_id"),
        _required_revision(source.get("revision"), property_path=f"{prefix}.revision"),
    )


class VoxelGridHandle:
    """Owns machine continuation state while exposing only business actions."""

    __slots__ = ("_client", "_expected_revision", "_released", "_session_id")

    def __init__(self, client: Any, machine_payload: Mapping[str, Any]) -> None:
        self._client = client
        self._session_id, self._expected_revision = _continuation(machine_payload)
        self._released = False

    @property
    def released(self) -> bool:
        return self._released

    def __repr__(self) -> str:
        return f"VoxelGridHandle(released={self._released!r})"

    def _require_open(self) -> None:
        if self._released:
            raise UsageError.at_source(
                code="voxel_grid_handle_released",
                message="voxel-grid session has already been released",
                facts={"property_path": "released", "expected_value": False, "actual_value": True},
            )

    def _update(self, result: "Result", *, release: bool = False) -> "Result":
        if result.ok and not release:
            self._session_id, self._expected_revision = _continuation(
                result._machine_payload
            )
        if result.ok and release:
            self._released = True
        return result

    def _session_action(self, action: str, **business_params: object) -> "Result":
        self._require_open()
        params = {
            "action": action,
            "session_id": self._session_id,
            "expected_revision": self._expected_revision,
            **business_params,
        }
        return self._client._execute_voxel_grid_lifecycle(
            "mesh.voxel_grid.session", params, self
        )

    def read(self, *, projection=OMITTED) -> "Result":
        params: dict[str, object] = {}
        if projection is not OMITTED:
            params["projection"] = projection
        return self._update(self._session_action("read", **params))

    def add_bounds(self, bounds, *, max_operation_cells=OMITTED) -> "Result":
        params: dict[str, object] = {"bounds": bounds}
        if max_operation_cells is not OMITTED:
            params["max_operation_cells"] = max_operation_cells
        return self._update(self._session_action("add_bounds", **params))

    def remove_bounds(self, bounds, *, max_operation_cells=OMITTED) -> "Result":
        params: dict[str, object] = {"bounds": bounds}
        if max_operation_cells is not OMITTED:
            params["max_operation_cells"] = max_operation_cells
        return self._update(self._session_action("remove_bounds", **params))

    def add_shape(self, shape) -> "Result":
        """Union an exact box, square_pyramid or triangular_prism with the grid.

        shape: kind, space (grid_local/component_local/world), center and size
        in centimeters; optional rotation is UE pitch/yaw/roll in degrees.
        A pyramid points along local +Z. A triangular prism has a right XZ
        triangle, low at -X and high at +X, extruded along Y.
        """
        return self._update(self._session_action("add_shape", shape=shape))

    def remove_shape(self, shape) -> "Result":
        """Subtract volume using add_shape's contract, preserving cut openings.

        Full subtraction can be applied: the actor remains editable with zero
        mesh and collision elements. An empty result is not itself an error.
        """
        return self._update(self._session_action("remove_shape", shape=shape))

    def apply(
        self,
        *,
        mesh_build=OMITTED,
        collision=OMITTED,
        material_ref=OMITTED,
        keep_session=OMITTED,
    ) -> "Result":
        self._require_open()
        params: dict[str, object] = {
            "session_id": self._session_id,
            "expected_revision": self._expected_revision,
        }
        for name, value in (
            ("mesh_build", mesh_build),
            ("collision", collision),
            ("material_ref", material_ref),
            ("keep_session", keep_session),
        ):
            if value is not OMITTED:
                params[name] = value
        result = self._client._execute_voxel_grid_lifecycle(
            "mesh.voxel_grid.apply", params, self
        )
        machine_payload = result._machine_payload
        released = bool(
            result.ok
            and isinstance(machine_payload, Mapping)
            and machine_payload.get("session_closed") is True
        )
        return self._update(result, release=released)

    def close(self) -> "Result":
        return self._update(self._session_action("close"), release=True)

    def cancel(self) -> "Result":
        return self._update(self._session_action("cancel"), release=True)


__all__ = ["VoxelGridHandle"]
