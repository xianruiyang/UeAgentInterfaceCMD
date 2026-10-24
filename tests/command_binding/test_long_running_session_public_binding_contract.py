from __future__ import annotations

import inspect
import json
from pathlib import Path
import unittest

import uai
from uai.operation import OperationHandle, OperationNamespace
from uai.result import Result

try:
    from uai.commands.generated import GeneratedCommandNamespaces
except ImportError:
    GeneratedCommandNamespaces = None


REPO_ROOT = Path(__file__).resolve().parents[2]
MANIFEST = (
    REPO_ROOT.parent
    / "Plugins"
    / "UeAgentInterface"
    / "Resources"
    / "UaiCommandManifest.json"
)

EXPECTED_PARAMETERS: dict[str, tuple[str, ...]] = {
    "job.compile_build": (
        "family_id",
        "subject_ref",
        "policy_id",
        "parameters",
    ),
    "editor.session": (
        "family_id",
        "subject_ref",
        "policy_id",
        "parameters",
    ),
    "runtime.scenario.execute": (
        "subject_ref",
        "policy_id",
        "parameters",
    ),
    "capture.image.execute": (
        "subject_ref",
        "policy_id",
        "parameters",
    ),
    "capture.media.execute": (
        "subject_ref",
        "policy_id",
        "parameters",
    ),
    "capture.render.execute": (
        "subject_ref",
        "policy_id",
        "parameters",
    ),
    "editor.safe_exit": (
        "dirty_resolution",
        "external_witness",
    ),
    "operation.status": ("operation_ref",),
    "operation.resume": (
        "operation_ref",
        "expected_generation",
    ),
    "operation.cancel": ("operation_ref", "reason"),
    "operation.receipt": ("operation_ref",),
    "operation.reconcile": (
        "operation_ref",
        "expected_generation",
    ),
    "operation.release": ("operation_ref",),
}

EXPECTED_METHODS: dict[str, tuple[str, str]] = {
    "job.compile_build": ("job", "compile_build"),
    "editor.session": ("editor", "session"),
    "runtime.scenario.execute": ("runtime", "scenario_execute"),
    "capture.image.execute": ("capture", "image_execute"),
    "capture.media.execute": ("capture", "media_execute"),
    "capture.render.execute": ("capture", "render_execute"),
    "editor.safe_exit": ("editor", "safe_exit"),
    "operation.status": ("operation", "status"),
    "operation.resume": ("operation", "resume"),
    "operation.cancel": ("operation", "cancel"),
    "operation.receipt": ("operation", "receipt"),
    "operation.reconcile": ("operation", "reconcile"),
    "operation.release": ("operation", "release"),
}

INTERNAL_LIFECYCLE_COMMANDS = {
    "runtime.scenario.execute",
    "operation.status",
    "operation.resume",
    "operation.cancel",
    "operation.receipt",
    "operation.reconcile",
    "operation.release",
}


class _Client:
    def __init__(self) -> None:
        self.calls: list[tuple[str, dict[str, object]]] = []

    def execute(
        self,
        command_id: str,
        params: dict[str, object],
    ):
        self.calls.append((command_id, params))
        return object()


class LongRunningSessionPublicBindingContractTests(unittest.TestCase):
    def test_long_running_projection_and_typed_handle_custody(self) -> None:
        operation_ref = {
            "operation_id": "op",
            "owner_lease_id": "lease",
            "server_session_id": "session",
        }

        class _HandleClient:
            def __init__(self) -> None:
                self.calls: list[tuple[str, dict[str, object]]] = []
                self.reject_release = True

            def execute(self, command_id, params):
                self.calls.append((command_id, dict(params)))
                if command_id == "operation.release" and self.reject_release:
                    return Result({
                        "ok": False,
                        "correlation_id": "correlation",
                        "payload": {},
                        "error": {"code": "operation_not_terminal"},
                    })
                generation = 1 if command_id == "operation.resume" else 0
                return Result(
                    {
                        "ok": True,
                        "correlation_id": "correlation",
                        "payload": {
                            "schema": "uai.long_running.snapshot.v1",
                            "operation_ref": operation_ref,
                            "descriptor_id": "descriptor",
                            "binding_hash": "binding",
                            "generation": generation,
                            "phase": "terminal" if command_id == "operation.release" else "running",
                            "lifecycle_status": "released" if command_id == "operation.release" else "running",
                            "stop_requested": False,
                            "retry_safe": False,
                            "terminal": command_id == "operation.release",
                            "latest_signal": {"type_id": "fixture.signal", "revision": 1, "payload": {"value": "ok", "content_hash": "business"}},
                        },
                        "error": None,
                    }
                )

            def _execute_operation_lifecycle(self, command_id, params):
                return self.execute(command_id, params)

        client = _HandleClient()
        handle = OperationHandle(client, operation_ref, 0)
        projected = Result(
            {
                "ok": True,
                "correlation_id": "correlation",
                "payload": {
                    "operation_ref": operation_ref,
                    "descriptor_id": "descriptor",
                    "binding_hash": "binding",
                    "generation": 0,
                    "phase": "running",
                    "lifecycle_status": "running",
                    "stop_requested": False,
                    "retry_safe": False,
                    "terminal": False,
                    "latest_signal": {"type_id": "fixture.signal", "revision": 1, "payload": {"value": "ok", "content_hash": "business"}},
                },
                "error": None,
            },
            long_running=True,
            operation=handle,
        )
        self.assertEqual(
            projected.payload,
            {
                "phase": "running",
                "lifecycle_status": "running",
                "stop_requested": False,
                "retry_safe": False,
                "terminal": False,
                "latest_signal": {"type_id": "fixture.signal", "payload": {"value": "ok"}},
            },
        )
        self.assertEqual(projected.operation, handle)
        with self.assertRaises(AttributeError):
            handle.generation

        failed_projected = Result(
            {
                "ok": False,
                "correlation_id": "correlation",
                "payload": {"operation_ref": operation_ref, "generation": 0},
                "error": {
                    "code": "failed",
                    "operation_ref": operation_ref,
                    "content_hash": "machine-value",
                    "fingerprint": "machine-value",
                },
            },
            long_running=True,
        )
        self.assertEqual(failed_projected.payload, {})
        self.assertEqual(
            failed_projected.error,
            {"code": "failed"},
        )

        ordinary = Result(
            {
                "ok": True,
                "correlation_id": "correlation",
                "payload": {"operation_ref": operation_ref, "generation": 0},
                "error": None,
            }
        )
        self.assertEqual(ordinary.payload, {"generation": 0})
        self.assertIn("operation_ref", ordinary._machine_payload)
        self.assertIn("generation", ordinary._machine_payload)
        with self.assertRaises(AttributeError):
            ordinary.correlation_id

        resumed = handle.resume()
        self.assertEqual(client.calls[0][0], "operation.resume")
        self.assertEqual(client.calls[0][1]["expected_generation"], 0)
        self.assertIs(resumed.operation, None)
        reconciled = handle.reconcile()
        self.assertEqual(client.calls[1][0], "operation.reconcile")
        self.assertEqual(client.calls[1][1]["expected_generation"], 1)
        self.assertIs(reconciled.operation, None)
        rejected = handle.release()
        self.assertFalse(rejected.ok)
        self.assertEqual(rejected.error["code"], "operation_not_terminal")
        self.assertFalse(handle.released)
        self.assertTrue(handle.resume().ok)
        self.assertEqual(client.calls[-1][0], "operation.resume")
        client.reject_release = False
        released = handle.release()
        self.assertTrue(handle.released)
        self.assertEqual(client.calls[-1][0], "operation.release")
        self.assertTrue(released.ok)
        with self.assertRaises(uai.UsageError):
            handle.status()

        namespace = OperationNamespace(
            client,
            type("Generated", (), {"plan_execute": lambda *_args: "planned"})(),
        )
        self.assertEqual(namespace.plan_execute([], "stop", "serial"), "planned")
        for name in ("status", "resume", "cancel", "receipt", "reconcile", "release"):
            self.assertFalse(
                hasattr(namespace, name),
                f"operation_namespace_must_not_expose_low_level_{name}",
            )

    def test_cpp_manifest_contains_exact_long_running_bindings(
        self,
    ) -> None:
        payload = json.loads(MANIFEST.read_text(encoding="utf-8"))
        commands = {
            item["command_id"]: item
            for item in payload["commands"]
        }
        missing = sorted(set(EXPECTED_PARAMETERS) - set(commands))
        self.assertEqual(
            missing,
            [],
            "long_running_cpp_manifest_commands_missing:"
            + ",".join(missing),
        )
        for command_id, expected_parameters in EXPECTED_PARAMETERS.items():
            with self.subTest(command_id=command_id):
                command = commands[command_id]
                self.assertEqual(
                    (command["namespace"], command["method"]),
                    EXPECTED_METHODS[command_id],
                )
                self.assertEqual(
                    command["status"],
                    "dormant"
                    if command_id in INTERNAL_LIFECYCLE_COMMANDS
                    else "active",
                )
                self.assertEqual(
                    tuple(
                        parameter["name"]
                        for parameter in command["parameters"]
                    ),
                    expected_parameters,
                    f"long_running_parameter_order_mismatch:{command_id}",
                )
                for parameter in command["parameters"]:
                    self.assertTrue(parameter["required"])
                    self.assertFalse(parameter["nullable"])

    def test_generated_methods_forward_one_exact_command_each(
        self,
    ) -> None:
        self.assertIsNotNone(
            GeneratedCommandNamespaces,
            "generated_command_namespaces_missing",
        )
        client = _Client()
        namespaces = GeneratedCommandNamespaces(client)
        expected_namespaces = (
            "job",
            "editor",
            "capture",
            "operation",
        )
        missing_generated = [
            namespace
            for namespace in expected_namespaces
            if not hasattr(namespaces, namespace)
        ]
        self.assertEqual(
            missing_generated,
            [],
            "generated_namespaces_missing:"
            + ",".join(missing_generated),
        )
        missing_client = [
            namespace
            for namespace in expected_namespaces
            if inspect.getattr_static(uai.Client, namespace, None) is None
        ]
        self.assertEqual(
            missing_client,
            [],
            "client_namespaces_missing:" + ",".join(missing_client),
        )

        namespaces.job.compile_build(
            "asset_compile",
            "/Game/UAI/Fixture.Asset",
            "policy:asset-compile/default/v1",
            {},
        )
        namespaces.editor.session(
            "asset_editor",
            "/Game/UAI/Fixture.Asset",
            "policy:asset-editor/open/v1",
            {},
        )
        self.assertFalse(
            hasattr(namespaces, "runtime"),
            "runtime scenario continuation must stay behind RuntimeSessionHandle",
        )
        namespaces.capture.image_execute(
            "viewport:owned-fixture",
            "policy:image-capture/png/v1",
            {},
        )
        namespaces.capture.media_execute(
            "audio-submix:owned-fixture",
            "policy:media-recording/wav/v1",
            {},
        )
        namespaces.capture.render_execute(
            "/Game/UAI/FixtureRT.FixtureRT",
            "policy:render-resource/clear/v1",
            {},
        )
        namespaces.editor.safe_exit(
            {
                "mode": "reject",
                "save_resources": [],
                "discard_resources": [],
            },
            {
                "schema": "uai.safe_exit.external_witness_ref.v1",
                "launch_id": "1" * 32,
                "exit_attempt_id": "2" * 32,
                "nonce": "3" * 64,
            },
        )
        for method in ("status", "resume", "cancel", "receipt", "reconcile", "release"):
            self.assertFalse(
                hasattr(namespaces.operation, method),
                f"generated_operation_namespace_must_hide_{method}",
            )

        self.assertEqual(
            [command_id for command_id, _ in client.calls],
            [
                command_id
                for command_id in EXPECTED_PARAMETERS
                if command_id not in INTERNAL_LIFECYCLE_COMMANDS
            ],
            "generated_methods_must_forward_each_actual_command_once",
        )
        for command_id, params in client.calls:
            with self.subTest(command_id=command_id):
                self.assertEqual(
                    tuple(params),
                    EXPECTED_PARAMETERS[command_id],
                    f"generated_method_parameter_mapping_mismatch:{command_id}",
                )


if __name__ == "__main__":
    unittest.main()
