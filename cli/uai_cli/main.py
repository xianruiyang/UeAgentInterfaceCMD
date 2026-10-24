from __future__ import annotations

import argparse
from collections.abc import Sequence
import json
from pathlib import Path
import sys

import uai
from uai.commands import _BINDING_CATALOG
from .model_output import json_output, render_output


def _configure_cli_streams() -> None:
    # Windows pipes otherwise inherit the ANSI locale instead of the report encoding.
    for name in ("stdin", "stdout", "stderr"):
        stream = getattr(sys, name)
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(encoding="utf-8", errors="backslashreplace" if name == "stderr" else "strict")


def _add_format(parser, *, default="compact") -> None:
    parser.add_argument(
        "--format", choices=("compact", "json"), default=default,
        help="Output display: compact fields/TSV for models (default), or JSON for programs.",
    )


def _add_exec_parser(commands) -> None:
    execute = commands.add_parser(
        "exec",
        help="Forward one actual UAI command.",
    )
    execute.add_argument("command_id")
    _add_format(execute, default=argparse.SUPPRESS)
    params = execute.add_mutually_exclusive_group()
    params.add_argument("--params-json", help="JSON object as one shell argument.")
    params.add_argument("--params-file", help="Read a UTF-8 JSON object from a file; avoids shell quoting.")
    params.add_argument("--params-stdin", action="store_true", help="Read a JSON object from stdin; avoids shell quoting.")
    execute.add_argument(
        "--report",
        help="Optional path for the full public result as JSON, independent of stdout format.",
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="ueagentinterfacecmd",
        description="UAI remote client command-line interface.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {uai.__version__}",
    )
    _add_format(parser)
    connection_source = parser.add_mutually_exclusive_group()
    connection_source.add_argument(
        "--connection",
        help="Explicit standalone connection TOML; local projects normally use managed --project discovery.",
    )
    connection_source.add_argument(
        "--project",
        help="Local Unreal project directory or .uproject; defaults to discovery above the current directory.",
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
    _add_format(connection, default=argparse.SUPPRESS)
    _add_exec_parser(commands)
    describe = commands.add_parser("describe", help="Read installed command parameter schemas without connecting.")
    describe.add_argument("command_id")
    describe.add_argument("--variant", help="Select an exact variant ID from this command's description.")
    describe.add_argument("--parameter", help="Show the exact schema of one parameter; omit for a short parameter list.")
    describe.add_argument("--pointer", default="", help="Optional JSON Pointer within the selected schema.")
    _add_format(describe, default=argparse.SUPPRESS)
    return parser


def _load_params(args) -> dict[str, object]:
    source = f"file {args.params_file!r}" if args.params_file else (
        "stdin (--params-stdin)" if args.params_stdin else "argument --params-json"
    )
    location: dict[str, object] = {
        "stage": "input_decode",
        "source_kind": "params_file" if args.params_file else "params_stdin" if args.params_stdin else "params_json",
    }
    if args.params_file:
        location["source_file"] = str(Path(args.params_file).resolve())
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
    except json.JSONDecodeError as exc:
        hint = (
            " If shell quoting changed the JSON, use the installed ueagentinterfacecmd executable"
            " with --params-stdin or --params-file."
            if args.params_json is not None else ""
        )
        raise uai.UsageError.at_source(
            code="cli_params_invalid",
            message=(
                f"{source}: {exc.msg}; line {exc.lineno}, column {exc.colno}"
                f" (character {exc.pos}).{hint}"
            ),
            facts={**location, "line": exc.lineno, "column": exc.colno, "character": exc.pos},
        ) from exc
    except UnicodeDecodeError as exc:
        raise uai.UsageError.at_source(
            code="cli_params_invalid",
            message=f"{source}: cannot decode {exc.encoding} at byte {exc.start}: {exc.reason}",
            facts={**location, "byte_offset": exc.start, "expected_value": exc.encoding},
        ) from exc
    except OSError as exc:
        raise uai.UsageError.at_source(
            code="cli_params_invalid",
            message=f"{source}: cannot read params: {exc.strerror or type(exc).__name__}",
            facts={**location, "errno": exc.errno},
        ) from exc
    if not isinstance(value, dict):
        raise uai.UsageError.at_source(
            code="cli_params_invalid",
            message=f"{source}: command params JSON must be an object, got {type(value).__name__}",
            facts={**location, "json_pointer": "", "expected_value": "object", "actual_type": type(value).__name__},
        )
    return value


def _result_value(result: uai.Result) -> dict[str, object]:
    value = {"ok": result.ok, "payload": result.payload, "error": result.error}
    diagnostics = result.diagnostics
    if diagnostics:
        value["diagnostics"] = diagnostics
    return value


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
            message=f"report file {path!r}: cannot write result: {exc.strerror if isinstance(exc, OSError) else exc.reason}",
        ) from exc


def _connect(args):
    return uai.connect(args.connection) if args.connection else uai.connect_project(args.project)


def _run_exec(args) -> int:
    params = _load_params(args)
    with _connect(args) as client:
        try:
            result = client.execute(args.command_id, params)
        except uai.ServerCommandError as error:
            result = error.result
    value = _result_value(result)
    display_value = value
    if result.ok and args.format == "compact" and args.command_id == "query.command.usage":
        required_params = {}
        for command in params.get("commands", []):
            binding = _BINDING_CATALOG.find(command)
            if binding is not None:
                required_params[command] = {
                    field.name: field.wire_type + (" | null" if field.nullable else "")
                    for field in binding.parameters if field.required
                }
        display_value = {**value, "required_params": required_params}
    print(render_output(display_value, args.format))
    if args.report:
        _write_report(args.report, json_output(value))
    return 0 if result.ok else 5


def _run_connection(args) -> int:
    with _connect(args) as client:
        if args.action == "show":
            print(render_output({"connection_state": client.connection_state}, args.format))
            return 0
        reachable = client.probe()
        print(render_output({"reachable": reachable}, args.format))
        return 0 if reachable else 3


def _local_failure(args, exc: uai.Error, stage: str) -> None:
    diagnostic = dict(exc.diagnostic)
    if diagnostic.get("stage") == "sdk":
        diagnostic["stage"] = stage
    value = {"ok": False, "payload": {}, "error": {
        "code": exc.code, "diagnostic": diagnostic,
    }}
    print(render_output(value, args.format), file=sys.stderr)
    # A failed call still needs a report. If writing the report itself failed,
    # preserve the already emitted command result and never execute it again.
    if getattr(args, "report", None) and exc.code != "cli_report_write_failed":
        try:
            _write_report(args.report, json_output(value))
        except uai.UsageError as report_error:
            print(str(report_error), file=sys.stderr)


def main(argv: Sequence[str] | None = None) -> int:
    _configure_cli_streams()
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command not in {"connection", "exec", "describe"}:
        parser.print_help()
        return 2
    try:
        if args.command == "exec":
            return _run_exec(args)
        if args.command == "describe":
            print(render_output(uai.describe_command(args.command_id, variant=args.variant, parameter=args.parameter, pointer=args.pointer), args.format))
            return 0
        return _run_connection(args)
    except uai.UsageError as exc:
        _local_failure(args, exc, "usage")
        return 2
    except uai.TransportError as exc:
        _local_failure(args, exc, "transport")
        return 3
    except (uai.SerializationError, uai.ProtocolError) as exc:
        _local_failure(args, exc, "serialization" if isinstance(exc, uai.SerializationError) else "protocol")
        return 4


__all__ = ["build_parser", "main"]
