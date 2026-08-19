from __future__ import annotations

import json
from pathlib import Path
import unittest

import uai

try:
    from uai.uai_protocol import (
        CommandRequest,
        UaiCommandCodec,
    )
except ImportError:
    CommandRequest = None
    UaiCommandCodec = None


FIXTURE_PATH = (
    Path(__file__).resolve().parent
    / "fixtures"
    / "uai_command_v1_vectors.json"
)


class PublicCommandCodecContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.fixture = json.loads(
            FIXTURE_PATH.read_text(encoding="utf-8")
        )

    def test_canonical_vectors_match_models(self) -> None:
        for vector_name in ("request", "success", "failure"):
            with self.subTest(vector=vector_name):
                expected = json.dumps(
                    self.fixture[vector_name]["model"],
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                )
                self.assertEqual(
                    self.fixture[vector_name]["canonical"],
                    expected,
                    f"canonical_fixture_mismatch:{vector_name}",
                )

    def _codec(self):
        self.assertIsNotNone(
            CommandRequest,
            "public_command_request_model_missing",
        )
        self.assertIsNotNone(
            UaiCommandCodec,
            "public_command_codec_missing",
        )
        return UaiCommandCodec()

    def _request(self):
        model = self.fixture["request"]["model"]
        return CommandRequest(
            command_id=model["command_id"],
            command_binding_hash=model["command_binding_hash"],
            params=model["params"],
            correlation_id=model["correlation_id"],
            request_id=model["request_id"],
        )

    def test_encode_request_matches_canonical_cross_language_vector(
        self,
    ) -> None:
        codec = self._codec()
        encoded = codec.encode_request(self._request())
        self.assertIs(type(encoded), bytes)
        self.assertEqual(
            encoded,
            self.fixture["request"]["canonical"].encode("utf-8"),
        )

    def test_exact_values_survive_request_encoding(self) -> None:
        codec = self._codec()
        encoded = codec.encode_request(self._request())
        decoded = json.loads(encoded.decode("utf-8"))
        params = decoded["params"]
        self.assertEqual(params["unicode"], "协议/蓝图")
        self.assertEqual(
            params["large_integer"],
            9007199254740993,
        )
        self.assertIsNone(params["nullable"])
        self.assertEqual(params["empty_string"], "")
        self.assertEqual(params["empty_array"], [])
        self.assertEqual(params["empty_object"], {})
        self.assertNotEqual(
            params["large_integer"],
            float(params["large_integer"]),
            "large_integer_was_rounded_through_double",
        )
        self.assertNotIn(
            "omitted",
            params,
            "omitted_parameter_was_materialized",
        )

    def test_codec_adds_no_depth_or_token_policy_gate(self) -> None:
        codec = self._codec()
        nested: dict[str, object] = {"leaf": "保留"}
        for _index in range(64):
            nested = {"child": nested}
        model = self.fixture["request"]["model"]
        request = CommandRequest(
            command_id=model["command_id"],
            command_binding_hash=model["command_binding_hash"],
            params={"nested": nested},
            correlation_id=model["correlation_id"],
            request_id=model["request_id"],
        )
        encoded = codec.encode_request(request)
        decoded = json.loads(encoded.decode("utf-8"))
        current = decoded["params"]["nested"]
        for _index in range(64):
            current = current["child"]
        self.assertEqual(current, {"leaf": "保留"})

    def test_success_result_is_lossless(self) -> None:
        codec = self._codec()
        model = self.fixture["success"]["model"]
        result = codec.decode_result(
            self.fixture["success"]["canonical"].encode("utf-8"),
            expected_request=self._request(),
        )
        self.assertIsInstance(result, uai.Result)
        self.assertTrue(result.ok)
        self.assertEqual(
            dict(result.raw_response),
            model,
        )

    def test_server_failure_remains_a_lossless_result(self) -> None:
        codec = self._codec()
        model = self.fixture["failure"]["model"]
        result = codec.decode_result(
            self.fixture["failure"]["canonical"].encode("utf-8"),
            expected_request=self._request(),
        )
        self.assertIsInstance(result, uai.Result)
        self.assertFalse(result.ok)
        self.assertEqual(dict(result.raw_response), model)
        with self.assertRaises(uai.ServerCommandError) as raised:
            result.raise_for_error()
        self.assertIs(raised.exception.result, result)

    def test_invalid_envelope_is_protocol_error(self) -> None:
        codec = self._codec()
        with self.assertRaises(uai.ProtocolError):
            codec.decode_result(
                b'{"ok":true}',
                expected_request=self._request(),
            )

    def test_protocol_module_contains_no_http_or_business_selector(
        self,
    ) -> None:
        codec = self._codec()
        module_root = Path(codec.__class__.__module__.replace(".", "/"))
        source_root = (
            Path(__file__).resolve().parents[2]
            / "cli"
            / module_root
        )
        text = "\n".join(
            path.read_text(encoding="utf-8-sig")
            for path in source_root.glob("*.py")
        )
        for forbidden in (
            "http.client",
            "urllib",
            "/api/",
            "descriptor_id",
            "StartsWith",
            "startswith(",
            "fallback",
            "max_depth",
            "depth_limit",
            "token_limit",
            "max_tokens",
        ):
            with self.subTest(forbidden=forbidden):
                self.assertNotIn(
                    forbidden,
                    text,
                    f"public_command_protocol_forbidden:{forbidden}",
                )


if __name__ == "__main__":
    unittest.main()
