import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
import sys

CURRENT = Path(__file__).resolve()
CLI_DIR = CURRENT.parents[1] / "cli"
sys.path.insert(0, str(CLI_DIR))

from uai_cli.config import load_app_config


class ConfigTokenFallbackTests(unittest.TestCase):
    def test_load_token_from_ue_ini_when_config_token_empty(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            app_root = root / "UeAgentInterfaceCMD"
            app_root.mkdir(parents=True, exist_ok=True)

            cfg_path = app_root / "uai-cli.default.json"
            cfg_payload = {
                "base_url": "http://127.0.0.1:17777",
                "token": "",
                "timeout_seconds": 60,
            }
            cfg_path.write_text(json.dumps(cfg_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

            ini_dir = root / "Saved/Config/WindowsEditor"
            ini_dir.mkdir(parents=True, exist_ok=True)
            ini_path = ini_dir / "UeAgentInterface.ini"
            ini_path.write_text(
                "[/Script/UeAgentInterface.UeAgentInterfaceSettings]\n"
                "AuthToken=test-token-from-ini\n",
                encoding="utf-8",
            )

            with patch("uai_cli.config.detect_app_root", return_value=app_root):
                config = load_app_config(
                    config_path=None,
                    base_url=None,
                    token=None,
                    timeout_seconds=None,
                    allow_nonloopback=False,
                    require_token=True,
                )

            self.assertEqual(config.token, "test-token-from-ini")


if __name__ == "__main__":
    unittest.main()
