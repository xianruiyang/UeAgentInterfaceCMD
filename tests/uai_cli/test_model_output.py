from __future__ import annotations

import json
import unittest

from uai_cli.main import build_parser
from uai_cli.model_output import compact_output


class ModelOutputTests(unittest.TestCase):
    def test_tabular_records_share_header_and_keep_values_and_order(self):
        value = {"assets": [
            {"name": "Cube", "count": 9007199254740993, "enabled": True, "note": None},
            {"note": "null", "count": 0, "name": "球\t体\n", "enabled": False},
        ]}
        lines = compact_output(value).splitlines()
        self.assertEqual(lines[0], "assets[2]{name\tcount\tenabled\tnote}:")
        decoded = []
        for line in lines[1:]:
            cells = []
            for cell in line[2:].split("\t"):
                try:
                    cells.append(json.loads(cell))
                except json.JSONDecodeError:
                    cells.append(cell)
            decoded.append(dict(zip(value["assets"][0], cells)))
        self.assertEqual(decoded, value["assets"])

    def test_strings_do_not_masquerade_as_types_or_structure(self):
        values = ["", "null", "true", "false", "01", "1e3", "- item", "# comment", "[2]", "{}", "a:b", "x\\y", "a\nnext", "a\u2028b", "a\x00b", " padded "]
        for text in values:
            with self.subTest(text=text):
                output = compact_output({"value": text})
                self.assertEqual(len(output.splitlines()), 1)
                self.assertEqual(json.loads(output.removeprefix("value: ")), text)
        self.assertEqual(compact_output({"value": None}), "value: null")

    def test_irregular_and_nested_values_are_not_forced_into_table(self):
        text = compact_output({"items": [{"x": 1}, {"y": 2}, None, [], {}, {"nested": [True, False]}]})
        self.assertIn("items[6]:", text)
        self.assertNotIn("items[6]{", text)
        for fragment in ("x: 1", "y: 2", "- null", "- []", "- {}", "nested[2]: true\tfalse"):
            self.assertIn(fragment, text)
        self.assertEqual(compact_output({"a": [], "b": {}, "c": ""}), 'a: []\nb: {}\nc: ""')

    def test_weird_keys_and_scalar_lists_preserve_boundaries(self):
        text = compact_output({"a\tb": {"x:y": ["a\tb", "", None, "null", True]}})
        self.assertEqual(text, '"a\\tb":\n  "x:y"[5]: "a\\tb"\t""\tnull\t"null"\ttrue')

    def test_format_option_applies_before_or_after_subcommand(self):
        parser = build_parser()
        for argv in (["--format", "json", "exec", "example"], ["exec", "example", "--format", "json"], ["connection", "show", "--format", "json"]):
            self.assertEqual(parser.parse_args(argv).format, "json")
        self.assertEqual(parser.parse_args(["exec", "example"]).format, "compact")


if __name__ == "__main__":
    unittest.main()
