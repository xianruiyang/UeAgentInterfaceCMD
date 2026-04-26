import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.templating import deep_merge, normalize_phases, render_value


class TemplatingTests(unittest.TestCase):
    def test_deep_merge(self):
        left = {"a": 1, "nested": {"x": 1, "y": 2}}
        right = {"nested": {"y": 3, "z": 4}, "b": 2}
        merged = deep_merge(left, right)
        self.assertEqual(merged["a"], 1)
        self.assertEqual(merged["b"], 2)
        self.assertEqual(merged["nested"]["x"], 1)
        self.assertEqual(merged["nested"]["y"], 3)
        self.assertEqual(merged["nested"]["z"], 4)

    def test_render_value_full_variable(self):
        value = "{{limit}}"
        output = render_value(value, {"limit": 20})
        self.assertEqual(output, 20)

    def test_render_value_inline_variable(self):
        value = "asset={{asset_path}}"
        output = render_value(value, {"asset_path": "/Game/Test"})
        self.assertEqual(output, "asset=/Game/Test")

    def test_normalize_phases_dict(self):
        raw = {
            "A": [{"command": "list_actors", "params": {}}],
            "B": {"commands": [{"command": "get_world_state", "params": {}}]},
        }
        normalized = normalize_phases(raw)
        self.assertEqual(len(normalized), 2)
        self.assertEqual(normalized[0]["name"], "A")
        self.assertEqual(normalized[1]["name"], "B")


if __name__ == "__main__":
    unittest.main()
