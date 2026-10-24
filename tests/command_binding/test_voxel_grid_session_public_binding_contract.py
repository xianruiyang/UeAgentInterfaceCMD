from __future__ import annotations

import unittest

import uai
from uai.result import Result
from uai.voxel_grid import VoxelGridHandle


def _response(payload):
    return {
        "ok": True,
        "correlation_id": "test-correlation",
        "payload": payload,
        "error": None,
    }


class _Client:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, object]]] = []
        self.next_revision = 2

    def _execute_voxel_grid_lifecycle(self, command_id, params, handle):
        self.calls.append((command_id, dict(params)))
        if command_id == "mesh.voxel_grid.apply":
            payload = {
                "operation_id": "internal-operation",
                "terminal_status": "succeeded",
                "session_id": "internal-session",
                "grid_id": "internal-grid",
                "revision": self.next_revision,
                "occupied_cell_count": 8,
                "session_closed": True,
                "mesh": {"triangle_count": 24},
                "collision": {"box_count": 1},
                "authoring_state": {"component_path": "internal-component"},
                "durability": {"receipt_id": "internal-receipt"},
                "readback": {"inventory_hash": "internal-hash"},
            }
        else:
            payload = {
                "operation_id": "internal-operation",
                "action": params["action"],
                "terminal_status": "succeeded",
                "readback": {
                    "session_id": "internal-session",
                    "grid_id": "internal-grid",
                    "revision": self.next_revision,
                    "actor_ref": "/Game/Test.Blockout",
                    "occupied_cell_count": 8,
                    "dirty": True,
                    "authoring_state": {"schema": "internal-schema"},
                },
                "errors": [],
                "warnings": [],
            }
        return Result(_response(payload), voxel_grid=handle)


class VoxelGridSessionPublicBindingContractTests(unittest.TestCase):
    def test_failed_begin_uses_the_same_machine_safe_projection(self) -> None:
        failed = Result(
            {
                "ok": False,
                "correlation_id": "test-correlation",
                "payload": {"operation_id": "internal-operation"},
                "error": {
                    "code": "voxel_grid_actor_not_found",
                    "subject_id": "internal-session",
                    "detail": "internal-machine-detail",
                    "terminal_status": "not_started",
                    "retry_safe": True,
                },
            },
            voxel_grid_projection=True,
        )
        self.assertEqual(failed.payload, {})
        self.assertEqual(
            failed.error,
            {
                "code": "voxel_grid_actor_not_found",
                "terminal_status": "not_started",
                "retry_safe": True,
            },
        )

    def test_public_client_attaches_typed_handle_to_begin_result(self) -> None:
        class _Transport:
            def close(self):
                return None

        class _Protocol:
            def __init__(self) -> None:
                self.calls = []

            def invoke(self, **request):
                self.calls.append(request)
                return Result(
                    _response(
                        {
                            "action": "begin",
                            "terminal_status": "succeeded",
                            "readback": {
                                "session_id": "internal-session",
                                "grid_id": "internal-grid",
                                "revision": 1,
                                "actor_ref": "/Game/Test.Blockout",
                            },
                            "errors": [],
                            "warnings": [],
                        }
                    )
                )

        protocol = _Protocol()
        client = uai.Client(
            connection=None,
            transport=_Transport(),
            protocol_client=protocol,
        )
        result = client.mesh.voxel_grid_begin(mode="create", label="Blockout")
        self.assertIsInstance(result.voxel_grid, VoxelGridHandle)
        self.assertEqual(result.payload["readback"], {"actor_ref": "/Game/Test.Blockout"})
        self.assertEqual(
            result._machine_payload["readback"]["actor_ref"],
            "/Game/Test.Blockout",
        )
        self.assertNotIn("session_id", str(result.payload))
        self.assertNotIn("revision", str(result.payload))
        self.assertEqual(protocol.calls[0]["command_id"], "mesh.voxel_grid.begin")
        self.assertEqual(
            protocol.calls[0]["params"],
            {"mode": "create", "label": "Blockout"},
        )

    def test_typed_handle_owns_session_and_revision(self) -> None:
        client = _Client()
        begin_payload = {
            "operation_id": "internal-operation",
            "action": "begin",
            "terminal_status": "succeeded",
            "readback": {
                "session_id": "internal-session",
                "grid_id": "internal-grid",
                "revision": 1,
                "actor_ref": "/Game/Test.Blockout",
                "cell_size": 100.0,
                "occupied_cell_count": 0,
                "dirty": True,
                "authoring_state": {"schema": "internal-schema"},
            },
            "errors": [],
            "warnings": [],
        }
        handle = VoxelGridHandle(client, begin_payload)
        begin = Result(_response(begin_payload), voxel_grid=handle)

        self.assertIs(begin.voxel_grid, handle)
        self.assertEqual(
            begin.payload["readback"],
            {
                "actor_ref": "/Game/Test.Blockout",
                "cell_size": 100.0,
                "occupied_cell_count": 0,
                "dirty": True,
            },
        )
        for name in (
            "session_id",
            "grid_id",
            "revision",
            "operation_id",
            "authoring_state",
        ):
            self.assertNotIn(name, str(begin.payload))
        with self.assertRaises(AttributeError):
            getattr(handle, "session_id")
        with self.assertRaises(AttributeError):
            getattr(handle, "revision")

        bounds = {
            "space": "grid_local",
            "min": {"x": 0, "y": 0, "z": 0},
            "max": {"x": 200, "y": 200, "z": 200},
        }
        changed = handle.add_bounds(bounds)
        self.assertIs(changed.voxel_grid, handle)
        self.assertEqual(client.calls[0][0], "mesh.voxel_grid.session")
        self.assertEqual(client.calls[0][1]["expected_revision"], 1)
        self.assertEqual(client.calls[0][1]["bounds"], bounds)

        applied = handle.apply(collision={"mode": "exact_box_components"})
        self.assertEqual(client.calls[1][0], "mesh.voxel_grid.apply")
        self.assertEqual(client.calls[1][1]["expected_revision"], 2)
        self.assertEqual(
            applied.payload,
            {
                "terminal_status": "succeeded",
                "occupied_cell_count": 8,
                "session_closed": True,
                "mesh": {"triangle_count": 24},
                "collision": {"box_count": 1},
            },
        )
        self.assertTrue(handle.released)
        for name in (
            "session_id",
            "grid_id",
            "revision",
            "operation_id",
            "authoring_state",
            "durability",
            "receipt_id",
            "inventory_hash",
        ):
            self.assertNotIn(name, str(applied.payload))
        with self.assertRaises(uai.UsageError):
            handle.read()

    def test_solid_geometry_observations_survive_public_projection(self) -> None:
        observation = {
            "actor_ref": "/Game/Test.Blockout",
            "actor_label": "Ramp",
            "geometry_representation": "convex_solid",
            "solid_piece_count": 2,
            "volume_cm3": 1200,
            "solid_bounds": {"space": "grid_local", "min": {"x": 0, "y": 0, "z": 0}},
            "changed_volume_cm3": 400,
            "shape": {"kind": "triangular_prism", "space": "grid_local"},
            "collision_mode": "exact_convex",
            "equivalent": True,
            "mesh_equivalent": True,
            "collision_exact_cover": True,
            "collision_convex_count": 2,
        }
        result = Result(_response({
            "volume_cm3": 1200,
            "readback": {**observation, "session_id": "private", "revision": 3},
        }), voxel_grid_projection=True)
        self.assertEqual(result.payload, {"volume_cm3": 1200, "readback": observation})

    def test_shape_mutations_use_the_typed_revision_continuation(self) -> None:
        client = _Client()
        handle = VoxelGridHandle(client, {"readback": {
            "session_id": "internal-session", "grid_id": "internal-grid", "revision": 1,
        }})
        shape = {"kind": "square_pyramid", "space": "world",
                 "center": {"x": 0, "y": 0, "z": 100},
                 "size": {"x": 200, "y": 200, "z": 200}}
        handle.add_shape(shape)
        handle.remove_shape(shape)
        self.assertEqual([call[1]["action"] for call in client.calls], ["add_shape", "remove_shape"])
        self.assertEqual([call[1]["expected_revision"] for call in client.calls], [1, 2])
        self.assertTrue(all(call[1]["shape"] == shape for call in client.calls))


if __name__ == "__main__":
    unittest.main()
