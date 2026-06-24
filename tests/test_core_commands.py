import unittest
from pathlib import Path
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_core.commands import __all__ as command_modules
from uai_core.commands import material as active_material
from uai_core.commands.core_level_assets_landscape import asset_delete
from uai_core.commands.deprecated import __all__ as deprecated_command_modules
from uai_core.commands.deprecated import material as deprecated_material
from uai_core.commands.deprecated.core_level_assets_landscape import spawn_actor
from uai_core.commands.material import material_apply_folder


class _FakeUaiCore:
    def __init__(self):
        self.calls = []

    def exec(self, command, params=None, **kwargs):
        self.calls.append({"command": command, "params": params or {}, "kwargs": kwargs})
        return {"command": command, "params": params or {}, "kwargs": kwargs}


class CoreCommandWrapperTests(unittest.TestCase):
    def test_active_command_wrapper_executes_named_command(self):
        fake = _FakeUaiCore()

        result = material_apply_folder(
            fake,
            request_id="apply-material",
            preflight=False,
            asset_path="/Game/M_Test",
            create_if_missing=True,
        )

        self.assertEqual(result["command"], "material_apply_folder")
        self.assertEqual(result["params"]["asset_path"], "/Game/M_Test")
        self.assertTrue(result["params"]["create_if_missing"])
        self.assertEqual(result["kwargs"]["request_id"], "apply-material")
        self.assertFalse(result["kwargs"]["preflight"])
        self.assertNotIn("allow_deprecated", result["kwargs"])

    def test_deprecated_wrapper_requires_use_case_and_allows_deprecated(self):
        fake = _FakeUaiCore()

        with self.assertRaises(TypeError):
            spawn_actor(fake, kind="static_mesh")

        result = spawn_actor(fake, deprecated_use_case="migration", kind="static_mesh")

        self.assertEqual(result["command"], "spawn_actor")
        self.assertTrue(result["kwargs"]["allow_deprecated"])
        self.assertEqual(result["kwargs"]["deprecated_use_case"], "migration")

    def test_active_and_deprecated_modules_are_separated(self):
        self.assertIn("material", command_modules)
        self.assertIn("material", deprecated_command_modules)
        self.assertTrue(hasattr(active_material, "material_apply_folder"))
        self.assertFalse(hasattr(active_material, "material_add_expression"))
        self.assertTrue(hasattr(deprecated_material, "material_add_expression"))

    def test_docstrings_keep_lightweight_input_output_and_doc_reference(self):
        doc = material_apply_folder.__doc__ or ""

        self.assertIn("\u8f93\u5165:", doc)
        self.assertIn("\u8f93\u51fa:", doc)
        self.assertIn("docs/commands/05_Material.md", doc)
        self.assertIn("CommandResult", doc)

    def test_command_group_follows_document_module_name(self):
        fake = _FakeUaiCore()

        result = asset_delete(fake, asset_path="/Game/Old", dry_run=True)

        self.assertEqual(result["command"], "asset_delete")
        self.assertEqual(result["params"], {"asset_path": "/Game/Old", "dry_run": True})


if __name__ == "__main__":
    unittest.main()