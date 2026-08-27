from __future__ import annotations

import inspect
import json
from pathlib import Path
import unittest

import uai

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
                self.assertEqual(command["status"], "active")
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
            "runtime",
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

        operation_ref = {
            "operation_id": "op-fixture",
            "owner_lease_id": "lease-fixture",
            "server_session_id": "session-fixture",
        }
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
        namespaces.runtime.scenario_execute(
            "runtime-session:pie-debug:0:fixture",
            "policy:runtime-scenario:bounded/v1",
            {
                "expected_pause_epoch": 1,
                "expected_workspace_revision": 1,
                "limits": {
                    "wall_seconds": 1,
                    "game_seconds": 1,
                    "frame_count": 1,
                },
                "steps": [],
            },
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
        namespaces.operation.status(operation_ref)
        namespaces.operation.resume(operation_ref, 1)
        namespaces.operation.cancel(operation_ref, "fixture-cancel")
        namespaces.operation.receipt(operation_ref)
        namespaces.operation.reconcile(operation_ref, 1)
        namespaces.operation.release(operation_ref)

        self.assertEqual(
            [command_id for command_id, _ in client.calls],
            list(EXPECTED_PARAMETERS),
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
