"""Explicit lifecycle for a reusable SDK authoring environment; never used on import."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
from urllib.parse import urlsplit
import venv

ROOT = Path(__file__).resolve().parents[1]
ENV = ROOT / '.venv-sdk'
MARKER = ENV / '.uai-sdk-environment.json'
IDENTITY = {'owner': 'ueagentinterfacecmd.sdk_environment', 'source': str(ROOT)}
CLI_NAME = 'ueagentinterfacecmd'
CLI_BIN = Path.home() / '.local' / 'bin'


def cli_paths() -> tuple[Path, Path]:
    return CLI_BIN / (CLI_NAME + ('.exe' if os.name == 'nt' else '')), CLI_BIN / f'.{CLI_NAME}.json'


def cli_registration() -> dict:
    _, receipt = cli_paths()
    if not receipt.is_file():
        return {}
    return json.loads(receipt.read_text(encoding='utf-8'))


def owned_launcher(path: Path, registration: dict) -> bool:
    return (
        registration.get('owner') == IDENTITY['owner']
        and path.is_file() and not path.is_symlink()
        and hashlib.sha256(path.read_bytes()).hexdigest() == registration.get('sha256')
    )


def expose_cli_directory() -> None:
    def normalized(value: str) -> str:
        return os.path.normcase(os.path.abspath(os.path.expandvars(value.strip('"'))))

    location = normalized(str(CLI_BIN))
    if location in {normalized(p) for p in os.environ.get('PATH', '').split(os.pathsep) if p}:
        return
    if os.name != 'nt':
        print(f'Add {CLI_BIN} to your shell PATH to use {CLI_NAME} by name.')
        return
    import ctypes
    import winreg

    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Environment') as key:
        try:
            value, kind = winreg.QueryValueEx(key, 'Path')
        except FileNotFoundError:
            value, kind = '', winreg.REG_EXPAND_SZ
        if location not in {normalized(p) for p in value.split(os.pathsep) if p}:
            winreg.SetValueEx(key, 'Path', 0, kind, value.rstrip(';') + (';' if value else '') + str(CLI_BIN))
    result = ctypes.c_size_t()
    ctypes.windll.user32.SendMessageTimeoutW(0xFFFF, 0x001A, 0, ctypes.c_wchar_p('Environment'), 2, 2000, ctypes.byref(result))
    print(f'User PATH includes {CLI_BIN}; reopen existing terminals/apps to inherit the change.')


def require_replaceable_cli() -> None:
    destination, _ = cli_paths()
    registration = cli_registration()
    if (destination.exists() or destination.is_symlink()) and not owned_launcher(destination, registration):
        raise RuntimeError(f'Existing command is not owned by this installer; preserved: {destination}')


def install_cli() -> None:
    require_replaceable_cli()
    destination, receipt = cli_paths()
    source = interpreter().parent / destination.name
    CLI_BIN.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=CLI_BIN, prefix=f'.{CLI_NAME}-', delete=False) as temporary:
        temporary_path = Path(temporary.name)
    try:
        shutil.copy2(source, temporary_path)
        temporary_path.replace(destination)
    finally:
        temporary_path.unlink(missing_ok=True)
    receipt.write_text(json.dumps({**IDENTITY, 'sha256': hashlib.sha256(destination.read_bytes()).hexdigest()}), encoding='utf-8')
    expose_cli_directory()
    print(f'CLI installed: {destination}')
    resolved = shutil.which(CLI_NAME)
    if resolved and Path(resolved).resolve() != destination.resolve():
        print(f'Another command precedes this installation on PATH: {resolved}; use {destination}.')


def uninstall_cli() -> None:
    destination, receipt = cli_paths()
    registration = cli_registration()
    if registration.get('source') != str(ROOT) or registration.get('owner') != IDENTITY['owner']:
        return
    if owned_launcher(destination, registration):
        destination.unlink()
        print(f'Removed CLI: {destination}')
    elif destination.exists() or destination.is_symlink():
        print(f'Preserved CLI replaced outside this installer: {destination}')
    receipt.unlink(missing_ok=True)


def interpreter() -> Path:
    return ENV / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')


def require_environment_location() -> None:
    # Every replacement/removal remains within this tool's exact environment.
    if ENV.is_symlink() or ENV.resolve() != ROOT / '.venv-sdk':
        raise RuntimeError(f'Environment must be a local directory: {ENV}')


def require_owned() -> None:
    require_environment_location()
    if not MARKER.is_file() or json.loads(MARKER.read_text(encoding='utf-8')) != IDENTITY:
        raise RuntimeError(f'Not an environment created by this tool: {ENV}')


def run_python(args: list[str]) -> int:
    if not interpreter().is_file():
        raise RuntimeError('SDK environment is not installed; run sdk_environment.py install once.')
    return subprocess.call([str(interpreter()), *args])


def prepare_installer_proxy(args) -> int:
    socks_proxy = any(
        key.lower().endswith('_proxy') and urlsplit(value).scheme in {'socks4', 'socks5', 'socks5h'}
        for key, value in os.environ.items()
    )
    if not socks_proxy or run_python(['-c', 'import importlib.util,sys; sys.exit(importlib.util.find_spec("socks") is None)']) == 0:
        return 0
    # Bootstrap via the invoking Python's working proxy support, then install offline.
    # Never bypass the user's proxy or change shared Python dependencies.
    with tempfile.TemporaryDirectory(prefix='ueagentinterfacecmd-pip-') as temporary:
        command = [sys.executable, '-m', 'pip', 'download', '--only-binary=:all:', '--no-deps', '--dest', temporary, 'PySocks']
        if args.find_links:
            command.extend(['--find-links', str(args.find_links.resolve())])
        if args.no_index:
            command.append('--no-index')
        code = subprocess.call(command)
        if code:
            return code
        return run_python(['-m', 'pip', 'install', '--no-index', '--find-links', temporary, 'PySocks'])


class InstallFailure(Exception):
    def __init__(self, code: int):
        self.code = code


def install_environment(args) -> int:
    require_environment_location()
    existed = ENV.exists()
    if existed:
        require_owned()
    # Detect command collisions before changing an otherwise working environment.
    require_replaceable_cli()
    cli_files = cli_paths()
    previous_cli = {path: path.read_bytes() if path.is_file() else None for path in cli_files}
    backup = Path(tempfile.mkdtemp(prefix='.uai-sdk-install-', dir=ROOT))
    previous_environment = backup / 'environment'
    cleanup_backup = True
    cli_started = False
    try:
        if existed:
            shutil.copytree(ENV, previous_environment, symlinks=True)
        (backup / 'cli').mkdir()
        for path, content in previous_cli.items():
            if content is not None:
                (backup / 'cli' / path.name).write_bytes(content)
        try:
            if not existed:
                ENV.mkdir()
                MARKER.write_text(json.dumps(IDENTITY), encoding='utf-8')
            venv.EnvBuilder(with_pip=True).create(ENV)
            code = prepare_installer_proxy(args)
            if code:
                raise InstallFailure(code)
            command = ['-m', 'pip', 'install', '--editable', f'{ROOT}[authoring]']
            if args.find_links:
                command.extend(['--find-links', str(args.find_links.resolve())])
            if args.no_index:
                command.append('--no-index')
            code = run_python(command)
            if code:
                raise InstallFailure(code)
            code = run_python(['-c', 'import uai,hjson; print("SDK authoring environment ready")'])
            if code:
                raise InstallFailure(code)
            cli_started = True
            install_cli()
        except BaseException as failure:
            cleanup_backup = False
            try:
                require_environment_location()
                if ENV.exists():
                    shutil.rmtree(ENV)
                if existed:
                    previous_environment.replace(ENV)
                for path, content in previous_cli.items() if cli_started else ():
                    if content is None:
                        path.unlink(missing_ok=True)
                    elif not path.is_file() or path.read_bytes() != content:
                        path.write_bytes(content)
            except (OSError, ValueError, RuntimeError) as recovery_failure:
                cleanup_backup = False
                raise RuntimeError(f'Install failed and recovery could not finish: {recovery_failure}; '
                                   f'previous installation backup retained at {backup}') from failure
            cleanup_backup = True
            print('Installation failed; previous SDK and CLI state restored.', file=sys.stderr)
            if isinstance(failure, InstallFailure):
                return failure.code
            raise
        return 0
    finally:
        if cleanup_backup:
            try:
                shutil.rmtree(backup)
            except OSError as exc:
                print(f'Installation snapshot retained at {backup}: {exc}', file=sys.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='action', required=True)
    install = commands.add_parser('install', help='Install/update SDK, authoring dependencies and the user CLI explicitly')
    install.add_argument('--find-links', type=Path, help='Wheel directory for prepared/offline installation')
    install.add_argument('--no-index', action='store_true', help='Do not query package indexes; use prepared wheels')
    commands.add_parser('status', help='Check imports without contacting UE or a package index')
    commands.add_parser('uninstall', help='Remove this installation\'s user CLI and tool-owned environment')
    run = commands.add_parser('run', help='Run Python arguments in the installed environment; never installs')
    run.add_argument('python_args', nargs=argparse.REMAINDER)
    cli = commands.add_parser('cli', help='Run the installed UAI CLI without activation or temporary Python')
    cli.add_argument('cli_args', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if args.action == 'install':
        return install_environment(args)
    if args.action == 'uninstall':
        if not ENV.exists():
            uninstall_cli()
            print('SDK environment is already absent')
            return 0
        require_owned()
        if Path(sys.prefix).resolve() == ENV.resolve():
            raise RuntimeError('Run uninstall with the base Python, not the environment being removed.')
        uninstall_cli()
        shutil.rmtree(ENV)
        print(f'Removed {ENV}')
        return 0
    if args.action == 'status':
        destination, _ = cli_paths()
        registration = cli_registration()
        print(f'CLI: {destination}; owned={owned_launcher(destination, registration) and registration.get("source") == str(ROOT)}', flush=True)
        print(f'PATH command: {shutil.which(CLI_NAME) or "not found"}', flush=True)
        print(f'Python: {interpreter()}', flush=True)
        return run_python(['-c', 'import sys,uai,hjson; print("ready"); print(sys.executable); print(uai.__file__)'])
    if args.action == 'cli':
        cli_args = args.cli_args[1:] if args.cli_args[:1] == ['--'] else args.cli_args
        return run_python(['-m', 'uai_cli', *cli_args])
    python_args = args.python_args
    if python_args[:1] == ['--']:
        python_args = python_args[1:]
    if not python_args:
        parser.error('run requires Python arguments, e.g. run -- path/to/script.py')
    return run_python(python_args)


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError) as exc:
        print(f'SDK environment: {exc}', file=sys.stderr)
        raise SystemExit(1)
