from __future__ import annotations

import importlib
import json
import unittest


def _response(*, ok: bool) -> dict[str, object]:
    return {
        "schema": "uai.command.v1",
        "version": 1,
        "message_kind": "command_result",
        "ok": ok,
        "payload": {
            "unicode": "蓝图",
            "integer": 9007199254740993,
        },
        "error": (
            None
            if ok
            else {
                "code": "server_rejected",
                "message": "request rejected",
                "details": {"field": "asset_path"},
            }
        ),
        "correlation_id": "corr-001",
        "request_id": "request-001",
        "command_id": "sample.execute",
        "command_binding_hash": "binding-hash",
        "server_extension": {"preserved": True},
    }


class ResultErrorContractTests(unittest.TestCase):
    def _uai(self):
        return importlib.import_module("uai")

    def _require(self, name: str):
        value = getattr(self._uai(), name, None)
        self.assertIsNotNone(value, f"public_uai_symbol_missing:{name}")
        return value

    def test_layered_errors_are_available_from_root(self) -> None:
        base = self._require("Error")
        for name in (
            "UsageError",
            "SerializationError",
            "TransportError",
            "ProtocolError",
        ):
            with self.subTest(name=name):
                error_type = self._require(name)
                self.assertTrue(
                    issubclass(error_type, base),
                    f"public_error_not_uai_error:{name}",
                )
                error = error_type(
                    code="test_code",
                    message="test message",
                )
                self.assertEqual(error.code, "test_code")
                self.assertEqual(error.message, "test message")
                self.assertIn("test_code", str(error))
        self.assertTrue(
            issubclass(self._require("ServerCommandError"), base),
            "public_error_not_uai_error:ServerCommandError",
        )

    def test_declared_command_reason_and_nested_diagnostics_survive_every_wrapper(self) -> None:
        leaf = {"schema": "uai.input.diagnostic/1", "code": "value_invalid",
                "stage": "preflight", "message": "Wrong element type", "json_pointer": "/commands/2",
                "schema_path": "/items/type", "keyword": "type", "expected": "string", "actual": None,
                "suggested_fix": "Supply a command name",
                "diagnostics": [{"code": "invalid_value", "actual_value": False}],
                "unchecked": [{"code": "dependency_unavailable", "reason": "Previous field is invalid"}]}
        carrier = leaf
        for schema in ("uai.runtime.diagnostic/1", "uai.operation.failure/1", "uai.verification.diagnostic/1"):
            carrier = {"schema": schema, "code": schema.split(".")[1] + "_failed",
                       "stage": "wrapper", "cause": carrier}
        raw = _response(ok=False)
        raw["error"] = {"code": "outer_failed", "detail": "private", "subject_id": "private",
                        "diagnostic": carrier}
        result = self._require("Result")(raw)
        actual = result.error["diagnostic"]
        for _ in range(3):
            actual = actual["cause"]
        self.assertEqual(actual, leaf)
        self.assertNotIn("private", json.dumps(result.error))
        with self.assertRaises(self._require("ServerCommandError")) as caught:
            result.raise_for_error()
        self.assertIn("/commands/2", str(caught.exception))
        self.assertEqual(result._machine_response, raw)

    def test_runtime_message_and_large_business_integer_are_not_discarded(self) -> None:
        raw = _response(ok=False)
        raw["error"] = {"code": "lookup_failed", "diagnostic": {
            "schema": "uai.runtime.diagnostic/1", "code": "lookup_failed", "stage": "command",
            "message": "/Game/Missing.Asset", "expected_value": 9007199254740993}}
        public = self._require("Result")(raw).error["diagnostic"]
        self.assertEqual(public["message"], "/Game/Missing.Asset")
        self.assertEqual(public["expected_value"], 9007199254740993)

    def test_operation_receipt_preserves_public_diagnostic_without_reprojecting_values(self) -> None:
        diagnostic = {
            "code": "property_conflict", "message": "The property changed after preparation.",
            "json_pointer": "/settings", "actual_value": {"identity": "business property"},
            "cause": {"code": "changed", "unchecked": [{"reason": "Later properties were not read"}]},
        }
        raw = _response(ok=True)
        raw["payload"] = {"error_code": "property_conflict", "diagnostic": diagnostic,
                          "operation_ref": "private"}
        result = self._require("Result")(raw, long_running=True)
        self.assertEqual(result.payload, {"error_code": "property_conflict", "diagnostic": diagnostic})
        raw["payload"].update(status="succeeded", warnings=[diagnostic])
        for options in ({}, {"long_running": True}, {"voxel_grid_projection": True},
                        {"model_result_fields": (("status", ("status",)),)}):
            with self.subTest(options=options):
                projected = self._require("Result")(raw, **options)
                self.assertEqual(projected.payload["warnings"], [diagnostic])
                self.assertNotIn("operation_ref", projected.payload)
        diagnostic["actual_value"]["identity"] = "mutated after Result construction"
        self.assertEqual(result.payload["diagnostic"]["actual_value"]["identity"], "business property")

    def test_pie_receipt_failure_keeps_native_error_and_ordered_flow_results(self) -> None:
        from uai.pie import _flow_result
        raw = _response(ok=True)
        flow = {"execution": {"status": "failed"}, "snapshot": {"paused": True, "updated": True},
                "results": [{"kind": "read", "value": False}], "diagnostics": ["Input target disappeared"]}
        diagnostic = {"code": "native_input_target_missing", "message": "Input target disappeared.",
                      "target_path": "/Game/Example.Actor", "unchecked": [{"reason": "Flow stopped before the next input"}]}
        raw["payload"] = {"error_code": "native_input_target_missing", "retry_safe": False, "diagnostic": diagnostic,
                          "latest_signal": {"payload": {"flow": flow}}}
        receipt = self._require("Result")(raw, long_running=True)
        self.assertEqual(receipt.payload["error_code"], "native_input_target_missing")
        self.assertEqual(receipt.payload["latest_signal"]["payload"]["flow"], flow)
        result = _flow_result(None, receipt)
        self.assertFalse(result.ok)
        self.assertEqual(result.error, {"code": "native_input_target_missing", "retry_safe": False, "diagnostic": diagnostic})
        self.assertEqual(result.payload, flow)
        raw["ok"] = False
        raw["error"] = {"code": "receipt_unavailable", "retry_safe": False}
        result = _flow_result(None, self._require("Result")(raw, long_running=True))
        self.assertEqual(result.error["code"], "receipt_unavailable")

    def test_result_preserves_business_payload_but_hides_transport_correlation(
        self,
    ) -> None:
        result_type = self._require("Result")
        raw = _response(ok=True)
        result = result_type(raw)

        self.assertIs(result.ok, True)
        self.assertEqual(result.payload, raw["payload"])
        self.assertIsNone(result.error)
        with self.assertRaises(AttributeError):
            result.correlation_id

        raw["server_extension"] = {"preserved": False}
        with self.assertRaises((AttributeError, TypeError)):
            result.ok = False

    def test_public_projection_hides_machine_identity_at_any_depth(self) -> None:
        result_type = self._require("Result")
        raw = _response(ok=True)
        raw["payload"] = {
            "operation_ref": "business-operation-ref",
            "binding_hash": "business-binding-hash",
            "nested": {
                "request_id": "business-request-id",
                "label": "readable business value",
            },
        }
        result = result_type(raw)

        self.assertEqual(
            result.payload,
            {"nested": {"label": "readable business value"}},
        )
        self.assertEqual(result._machine_response, raw)

    def test_public_result_hides_unstructured_handler_diagnostics(self) -> None:
        result_type = self._require("Result")
        raw = _response(ok=False)
        raw["error"] = {
            "code": "server_rejected",
            "message": "request rejected",
            "subject_id": "internal-subject",
            "detail": "unstructured private handler detail",
            "details": {
                "command_id": "business-command-id",
                "request_id": "business-request-id",
                "reason": "readable failure reason",
            },
        }
        result = result_type(raw)

        self.assertEqual(result.error, {"code": "server_rejected"})
        self.assertEqual(result._machine_response, raw)


    def test_runtime_failure_exposes_cause_stage_without_private_detail(self) -> None:
        raw = _response(ok=False)
        raw["error"] = {
            "code": "viewport_graph_runtime_unavailable",
            "retry_safe": True,
            "terminal_status": "not_started",
            "diagnostic": {
                "schema": "uai.runtime.diagnostic/1",
                "code": "descriptor_registry_invalid",
                "stage": "timeline_spatial",
            },
        }
        result = self._require("Result")(raw)
        self.assertEqual(result.error, raw["error"])
        self.assertEqual(result._machine_response, raw)


    def test_operation_failure_preserves_runtime_cause_without_private_detail(self) -> None:
        raw = _response(ok=False)
        raw["error"] = {
            "code": "operation_failed",
            "mutation_started": False,
            "diagnostic": {
                "schema": "uai.operation.failure/1",
                "code": "operation_failed",
                "stage": "execution",
                "mutation_started": False,
                "cause": {
                    "schema": "uai.runtime.diagnostic/1",
                    "code": "runtime_creation_failed",
                    "stage": "discovery",
                },
            },
        }
        result = self._require("Result")(raw)
        self.assertEqual(result.error, raw["error"])
        self.assertEqual(result._machine_response, raw)


    def test_operation_mismatch_preserves_all_structured_differences(self) -> None:
        # The server supplies public comparison evidence; the SDK preserves it.
        differences = [
            {"kind": "value", "path": f"/value/{index}", "left": index, "right": index + 1}
            for index in range(10)
        ] + [{"kind": "value", "path": "/nested", "left": None, "right": {"label": "球体"}},
             {"kind": "identity_mismatch", "path": "/entries/0/identity",
              "left": {"$type": "canonical_identity", "target_kind": "mesh", "object_role": "geometry"}},
             {"kind": "missing_right", "path": "/entries/1",
              "left": {"$type": "state_entry",
                       "value": {"properties": {"Identity": {"value": "business"},
                                                 "generation": {"value": 9}}}}}]
        raw = _response(ok=False)
        raw["error"] = {"code": "verification_semantic_mismatch",
            "mutation_started": True, "retry_safe": False, "diagnostic": {
                "schema": "uai.operation.failure/1", "code": "verification_semantic_mismatch",
                "stage": "verification", "mutation_started": True, "retry_safe": False,
                "verification": {"status": "mismatch", "effect_outcome": "different",
                    "targets": [{"oracle_kind": "persisted", "status": "mismatch",
                    "target": {"kind": "mesh", "selectors": {"selector": "/Game/Probe.Mesh"}, "role": "geometry"},
                    "comparison": {"differences": differences}}]},
            }}
        result = self._require("Result")(raw)
        self.assertFalse(result.ok)
        self.assertFalse(result.error["retry_safe"])
        diagnostic = result.error["diagnostic"]
        self.assertEqual(diagnostic["verification"]["status"], "mismatch")
        self.assertEqual(diagnostic["verification"]["targets"][0]["target"]["selectors"], {"selector": "/Game/Probe.Mesh"})
        self.assertEqual(diagnostic["verification"]["targets"][0]["comparison"]["differences"], differences)
        self.assertEqual(result._machine_response, raw)

    def test_authoring_failure_preserves_recovery_values_and_related_sources(self) -> None:
        diagnostic = {
            "schema": "uai.authoring.diagnostic/1", "code": "semantic_snapshots_different",
            "stage": "final_readback", "transaction_status": "rolled_back",
            "rollback_attempted": True, "rollback_succeeded": False, "retry_safe": False,
            "asset_applied": False, "retry_import": False, "recovery_action": "inspect_state",
            "expected_value": None, "actual_value": False, "proposed_value": False,
            "expected_value_present": True, "actual_value_present": True,
            "source_kind": "related_input", "semantic_pointer": "/graphs/g/nodes/n/pins/0/type",
            "related_sources": [{"source_file": "graphs/eventgraph.hjson", "json_pointer": "/nodes/MakeArray",
                                 "line": 7, "column": 3},
                                {"source_kind": "native_compile_event", "script_path": "/Game/FX/Module.Module",
                                 "node_guid": "native-node", "pin_guid": "native-pin",
                                 "stack_guids": ["outer-call", "inner-call"]}],
            "diagnostics": [{"code": "value_mismatch", "expected_value": "Pawn", "actual_value": "Actor",
                             "proposed_value": None, "json_pointer": "/fields/TargetType",
                             "expected_value_present": True, "actual_value_present": True}],
        }
        raw = _response(ok=False)
        raw["error"] = {"code": diagnostic["code"], "diagnostic": diagnostic}
        public = self._require("Result")(raw).error["diagnostic"]
        self.assertEqual(public, diagnostic)
        diagnostic.update(code="workspace_refresh_failed", transaction_status="committed",
                          asset_applied=True, retry_import=False, recovery_action="export_workspace")
        raw["error"] = {"code": diagnostic["code"], "diagnostic": diagnostic}
        committed = self._require("Result")(raw).error["diagnostic"]
        self.assertTrue(committed["asset_applied"])
        self.assertFalse(committed["retry_import"])
        self.assertEqual(committed["recovery_action"], "export_workspace")


    def test_oracle_failure_preserves_stage_and_structured_underlying_cause(self) -> None:
        diagnostic = {"schema": "uai.verification.diagnostic/1",
            "code": "verification_oracle_unavailable", "stage": "persisted_observe",
            "cause_code": "asset_read_failed", "cause": {
                "schema": "uai.authoring.diagnostic/1", "code": "asset_read_failed",
                "property_path": "/mesh", "message": "Cannot read mesh"}}
        for nested in (False, True):
            with self.subTest(nested=nested):
                carrier = {"schema": "uai.operation.failure/1", "code": diagnostic["code"],
                    "stage": "verification", "cause": diagnostic} if nested else diagnostic
                raw = _response(ok=False)
                raw["error"] = {"code": diagnostic["code"], "diagnostic": carrier}
                error = self._require("Result")(raw).error["diagnostic"]
                public = error["cause"] if nested else error
                self.assertEqual(public, diagnostic)

    def test_candidate_recovery_preserves_server_name_and_choices(self) -> None:
        cases = (
            {'code': 'candidate_ambiguous', 'name': 'Smooth Step',
             'choose': {'form': ['expression', 'function']}},
            {'code': 'candidate_selector_invalid', 'name': 'Multiply',
             'choose': [{'form': 'scalar', 'source': 'Engine'},
                        {'form': 'vector', 'source': 'Project'}]},
            {'code': 'candidate_selector_invalid', 'name': 'Unique'},
        )
        for recovery in cases:
            with self.subTest(code=recovery['code'], name=recovery['name']):
                raw = _response(ok=False)
                raw['error'] = {'code': recovery['code'], 'subject_id': 'preflight',
                                'diagnostic': {'schema': 'uai.authoring.diagnostic/1', **recovery}}
                result = self._require('Result')(raw)
                self.assertEqual(result.error, {'code': recovery['code'], 'diagnostic': {'schema': 'uai.authoring.diagnostic/1', **recovery}})
                self.assertEqual(result._machine_response, raw)
                exposed = result.error
                exposed['diagnostic']['name'] = 'changed by caller'
                self.assertEqual(result.error, {'code': recovery['code'], 'diagnostic': {'schema': 'uai.authoring.diagnostic/1', **recovery}})

    def test_candidate_error_does_not_expose_arbitrary_detail(self) -> None:
        for detail in ('handler diagnostic', '{broken',
                       json.dumps({'code': 'other', 'name': 'wrong'}),
                       json.dumps({'code': 'candidate_ambiguous', 'request_id': 'private'})):
            with self.subTest(detail=detail):
                raw = _response(ok=False)
                raw['error'] = {'code': 'candidate_ambiguous', 'detail': detail}
                self.assertEqual(self._require('Result')(raw).error,
                                 {'code': 'candidate_ambiguous'})

    def test_server_failure_remains_a_result_by_default(self) -> None:
        result_type = self._require("Result")
        result = result_type(_response(ok=False))
        self.assertIs(result.ok, False)
        self.assertEqual(result.error["code"], "server_rejected")
        self.assertEqual(result.payload["unicode"], "蓝图")

    def test_raise_for_error_wraps_without_losing_result(self) -> None:
        result_type = self._require("Result")
        server_error_type = self._require("ServerCommandError")
        failed = result_type(_response(ok=False))
        with self.assertRaises(server_error_type) as caught:
            failed.raise_for_error()
        self.assertIs(caught.exception.result, failed)
        self.assertEqual(
            caught.exception.result.payload,
            failed.payload,
        )

        succeeded = result_type(_response(ok=True))
        self.assertIs(succeeded.raise_for_error(), succeeded)

    def test_result_requires_an_explicit_boolean_ok_field(self) -> None:
        result_type = self._require("Result")
        protocol_error_type = self._require("ProtocolError")
        for value in (1, "true", None):
            raw = _response(ok=True)
            raw["ok"] = value
            with self.subTest(value=value):
                with self.assertRaises(protocol_error_type) as caught:
                    result_type(raw)
                self.assertEqual(
                    caught.exception.code,
                    "response_ok_invalid",
                )

    def test_result_requires_mapping_response_and_internal_correlation(self) -> None:
        result_type = self._require("Result")
        protocol_error_type = self._require("ProtocolError")
        with self.assertRaises(protocol_error_type) as not_mapping:
            result_type(["not", "a", "mapping"])
        self.assertEqual(
            not_mapping.exception.code,
            "response_envelope_invalid",
        )

        raw = _response(ok=True)
        del raw["correlation_id"]
        with self.assertRaises(protocol_error_type) as missing:
            result_type(raw)
        self.assertEqual(
            missing.exception.code,
            "response_correlation_missing",
        )


if __name__ == "__main__":
    unittest.main()
