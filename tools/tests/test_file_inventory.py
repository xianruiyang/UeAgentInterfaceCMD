from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


CURRENT = Path(__file__).resolve()
TOOLS_DIR = CURRENT.parents[1]
sys.path.insert(0, str(TOOLS_DIR))

from uai_repository.file_inventory import (  # noqa: E402
    build_bounded_file_inventory,
)


class FileInventoryTests(unittest.TestCase):
    def test_inventory_is_deterministic_deduplicated_and_excludes_cache(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            nested = root / "nested"
            nested.mkdir()
            (root / "b.txt").write_text("b", encoding="utf-8")
            (nested / "a.txt").write_text("a", encoding="utf-8")
            cache = nested / "__pycache__"
            cache.mkdir()
            (cache / "ignored.pyc").write_bytes(b"ignored")

            inventory = build_bounded_file_inventory((nested, root, root))
            relative = tuple(
                entry.path.relative_to(root).as_posix()
                for entry in inventory.entries
            )

            self.assertEqual(relative, ("b.txt", "nested/a.txt"))

    def test_files_under_filters_suffix_and_keeps_explicit_file(
        self,
    ) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            source = root / "source"
            source.mkdir()
            (source / "a.py").write_text("a", encoding="utf-8")
            (source / "b.md").write_text("b", encoding="utf-8")
            external = root / "external.json"
            external.write_text("{}", encoding="utf-8")

            inventory = build_bounded_file_inventory(
                (source,),
                explicit_files=(external,),
            )

            self.assertEqual(
                inventory.files_under(source, suffixes={".py"}),
                ((source / "a.py").resolve(),),
            )
            self.assertIn(
                external.resolve(),
                tuple(entry.path for entry in inventory.entries),
            )

    def test_read_text_uses_one_snapshot_per_inventory(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "value.txt"
            path.write_text("first", encoding="utf-8")
            inventory = build_bounded_file_inventory((path.parent,))

            self.assertEqual(inventory.read_text(path), "first")
            path.write_text("second", encoding="utf-8")
            self.assertEqual(inventory.read_text(path), "first")


if __name__ == "__main__":
    unittest.main()
