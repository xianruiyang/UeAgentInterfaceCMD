from __future__ import annotations

import importlib
import unittest


def _response(*, ok: bool) -> dict[str, object]:
    return {
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

    def test_result_preserves_the_complete_server_response(self) -> None:
        result_type = self._require("Result")
        raw = _response(ok=True)
        result = result_type(raw)

        self.assertIs(result.ok, True)
        self.assertEqual(result.payload, raw["payload"])
        self.assertIsNone(result.error)
        self.assertEqual(result.correlation_id, "corr-001")
        self.assertEqual(result.raw_response, raw)
        self.assertEqual(
            result.raw_response["server_extension"],
            {"preserved": True},
        )

        raw["server_extension"] = {"preserved": False}
        self.assertEqual(
            result.raw_response["server_extension"],
            {"preserved": True},
            "result_must_snapshot_input_response",
        )
        with self.assertRaises(TypeError):
            result.raw_response["server_extension"] = {}
        with self.assertRaises((AttributeError, TypeError)):
            result.ok = False

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
            caught.exception.result.raw_response,
            failed.raw_response,
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

    def test_result_requires_mapping_response_and_correlation(self) -> None:
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
