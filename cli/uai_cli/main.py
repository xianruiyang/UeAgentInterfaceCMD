from __future__ import annotations

import argparse
from collections.abc import Sequence
import json
from pathlib import Path
import sys

import uai


def _add_exec_parser(commands) -> None:
    execute = commands.add_parser(
        "exec",
        help="Forward one actual UAI command.",
    )
    execute.add_argument("command_id")
    execute.add_argument(
        "--contract-hash",
        help="Exact sha256 contract identity obtained from command discovery.",
    )
    params = execute.add_mutually_exclusive_group()
    params.add_argument("--params-json")
    params.add_argument("--params-file")
    params.add_argument("--params-stdin", action="store_true")
    execute.add_argument(
        "--report",
        help="Optional path for the same lossless result JSON.",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="uai-cli",
        description="UAI remote client command-line interface.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {uai.__version__}",
    )
    parser.add_argument(
        "--connection",
        help="Path to one complete UAI Connection TOML file.",
    )
    commands = parser.add_subparsers(dest="command")
    connection = commands.add_parser(
        "connection",
        help="Inspect or probe the configured connection.",
    )
    connection.add_argument(
        "action",
        choices=("show", "probe"),
    )
    _add_exec_parser(commands)
    return parser


def _load_params(args) -> dict[str, object]:
    try:
        if args.params_file:
            text = Path(args.params_file).read_text(
                encoding="utf-8-sig"
            )
        elif args.params_stdin:
            text = sys.stdin.read()
        elif args.params_json is not None:
            text = args.params_json
        else:
            return {}
        value = json.loads(text)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise uai.UsageError(
            code="cli_params_invalid",
            message="command params cannot be read as JSON",
        ) from exc
    if not isinstance(value, dict):
        raise uai.UsageError(
            code="cli_params_invalid",
            message="command params JSON must be an object",
        )
    return value


def _result_json(result: uai.Result) -> str:
    return json.dumps(
        dict(result.raw_response),
        ensure_ascii=False,
        separators=(",", ":"),
    )


def _write_report(path: str, text: str) -> None:
    try:
        Path(path).write_text(
            text + "\n",
            encoding="utf-8",
            newline="\n",
        )
    except (OSError, UnicodeError) as exc:
        raise uai.UsageError(
            code="cli_report_write_failed",
            message=f"result report cannot be written: {path}",
        ) from exc


def _run_exec(args) -> int:
    params = _load_params(args)
    with uai.connect(args.connection) as client:
        if args.contract_hash:
            result = client.execute_exact(
                args.command_id,
                params,
                contract_hash=args.contract_hash,
            )
        else:
            result = client.execute(args.command_id, params)
    text = _result_json(result)
    print(text)
    if args.report:
        _write_report(args.report, text)
    return 0 if result.ok else 5


def _run_connection(args) -> int:
    with uai.connect(args.connection) as client:
        if args.action == "show":
            print(
                json.dumps(
                    {
                        "connection_state": client.connection_state,
                    },
                    ensure_ascii=False,
                )
            )
            return 0
        reachable = client.probe()
        print(
            json.dumps(
                {
                    "reachable": reachable,
                },
                ensure_ascii=False,
            )
        )
        return 0 if reachable else 3


def main(argv: Sequence[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command not in {"connection", "exec"}:
        parser.print_help()
        return 2
    if not args.connection:
        print("--connection is required", file=sys.stderr)
        return 2
    try:
        if args.command == "exec":
            return _run_exec(args)
        return _run_connection(args)
    except uai.UsageError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    except uai.TransportError as exc:
        print(str(exc), file=sys.stderr)
        return 3
    except (uai.SerializationError, uai.ProtocolError) as exc:
        print(str(exc), file=sys.stderr)
        return 4


__all__ = ["build_parser", "main"]
