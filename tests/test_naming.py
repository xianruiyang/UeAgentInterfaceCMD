import unittest
from datetime import datetime
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.naming import build_short_asset_name


class NamingTests(unittest.TestCase):
    def test_build_short_asset_name(self):
        now = datetime(2026, 3, 5, 10, 30, 0)
        value = build_short_asset_name("blueprint", "Door Auto Open", max_len=24, now=now, tag_mode="date")
        self.assertTrue(value.startswith("BP_"))
        self.assertLessEqual(len(value), 24)
        self.assertTrue(value.endswith("_0305"))

    def test_build_short_asset_name_without_tag(self):
        now = datetime(2026, 3, 5, 10, 30, 0)
        value = build_short_asset_name("blueprint", "Door Auto Open", max_len=20, now=now, tag_mode="none")
        self.assertTrue(value.startswith("BP_"))
        self.assertLessEqual(len(value), 20)
        self.assertNotIn("0305", value)

    def test_build_short_asset_name_defaults(self):
        now = datetime(2026, 3, 5, 10, 30, 0)
        value = build_short_asset_name("blueprint", "Door Auto Open", now=now)
        self.assertTrue(value.startswith("BP_"))
        self.assertLessEqual(len(value), 20)
        self.assertNotIn("0305", value)


if __name__ == "__main__":
    unittest.main()
