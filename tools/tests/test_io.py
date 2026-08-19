import tempfile
import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
TOOLS_DIR = CURRENT.parents[1]
sys.path.insert(0, str(TOOLS_DIR))

from uai_repository.io import load_json_file


class UtilsJsonTests(unittest.TestCase):
    def test_load_json_file_supports_utf8_bom(self):
        payload = "{\n  \"a\": 1,\n  \"b\": \"ok\"\n}\n"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "with_bom.json"
            path.write_text(payload, encoding="utf-8-sig")
            data = load_json_file(path)
            self.assertEqual(data["a"], 1)
            self.assertEqual(data["b"], "ok")


if __name__ == "__main__":
    unittest.main()
