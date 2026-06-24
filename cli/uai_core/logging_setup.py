from __future__ import annotations

import logging
from pathlib import Path

from .utils import get_hostname
from .version import BUILD_TAG, __version__


def setup_logging(logs_dir: Path, clear_on_start: bool, log_level: str) -> Path:
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = logs_dir / f"uai_cli_{get_hostname()}.log"
    if clear_on_start and log_path.exists():
        log_path.write_text("", encoding="utf-8")

    level = getattr(logging, log_level.upper(), logging.INFO)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    logger = logging.getLogger()
    for handler in list(logger.handlers):
        handler.close()
        logger.removeHandler(handler)
    logger.setLevel(level)

    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    logging.info("VERSION_TAG=%s CLI_VERSION=%s", BUILD_TAG, __version__)
    return log_path
