from pathlib import Path
import sys

current_dir = Path(__file__).resolve().parent
cli_dir = current_dir / "cli"
sys.path.insert(0, str(cli_dir))

from uai_cli.main import main

if __name__ == "__main__":
    raise SystemExit(main())

