"""Installation state transitions in an isolated tree; never change user PATH."""
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


SOURCE = Path(__file__).resolve().parents[2] / 'tools' / 'sdk_environment.py'
spec = importlib.util.spec_from_file_location('uai_sdk_environment_under_test', SOURCE)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallationLifecycleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='uai-sdk-install-test-')
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'cmd'
        self.root.mkdir()
        self.environment = self.root / '.venv-sdk'
        self.bin = Path(self.temporary.name) / 'user-bin'
        self.identity = {'owner': installer.IDENTITY['owner'], 'source': str(self.root)}
        self.globals = patch.multiple(installer, ROOT=self.root, ENV=self.environment,
                                     MARKER=self.environment / '.uai-sdk-environment.json',
                                     CLI_BIN=self.bin, IDENTITY=self.identity)
        self.globals.start()
        self.addCleanup(self.globals.stop)
        self.path_exposure = patch.object(installer, 'expose_cli_directory')
        self.path_exposure.start()
        self.addCleanup(self.path_exposure.stop)

    def existing_installation(self):
        self.environment.mkdir()
        installer.MARKER.write_text(json.dumps(self.identity), encoding='utf-8')
        (self.environment / 'dependency.txt').write_bytes(b'previous dependency')
        (self.environment / 'pyvenv.cfg').write_bytes(b'previous configuration')
        self.bin.mkdir()
        destination, receipt = installer.cli_paths()
        destination.write_bytes(b'previous launcher')
        receipt.write_text(json.dumps({**self.identity, 'sha256': hashlib.sha256(destination.read_bytes()).hexdigest()}), encoding='utf-8')

    def state(self):
        return {str(path.relative_to(Path(self.temporary.name))): path.read_bytes()
                for path in Path(self.temporary.name).rglob('*') if path.is_file()}

    def build_environment(self, path):
        path.mkdir(exist_ok=True)
        (path / 'pyvenv.cfg').write_bytes(b'new configuration')
        (path / 'dependency.txt').write_bytes(b'new dependency')
        scripts = installer.interpreter().parent
        scripts.mkdir(exist_ok=True)
        (scripts / installer.cli_paths()[0].name).write_bytes(b'new launcher')

    def invoke(self, action='install', pip_exit=0):
        # Dependency failure is injected after a mutation, as a failed pip update may
        # have installed earlier packages. Actual installer control flow is exercised.
        def run(args):
            return pip_exit if args[:3] == ['-m', 'pip', 'install'] else 0
        with patch('sys.argv', [str(SOURCE), action]), redirect_stdout(io.StringIO()), \
             patch.object(installer.venv.EnvBuilder, 'create', side_effect=self.build_environment), \
             patch.object(installer, 'prepare_installer_proxy', return_value=0), \
             patch.object(installer, 'run_python', side_effect=run):
            return installer.main()

    def test_failed_update_restores_previous_installation(self):
        self.existing_installation()
        before = self.state()
        self.assertEqual(self.invoke(pip_exit=23), 23)
        self.assertEqual(self.state(), before)

    def test_failed_first_install_removes_partial_environment(self):
        self.assertEqual(self.invoke(pip_exit=23), 23)
        self.assertFalse(self.environment.exists())
        self.assertFalse(installer.cli_paths()[0].exists())
        self.assertFalse(installer.cli_paths()[1].exists())

    def test_failed_cli_publication_restores_environment_and_both_files(self):
        self.existing_installation()
        before = self.state()
        publish = installer.install_cli
        def fail_after_publish():
            publish()
            raise OSError('injected publication failure')
        with patch.object(installer, 'install_cli', side_effect=fail_after_publish):
            with self.assertRaisesRegex(OSError, 'injected publication failure'):
                self.invoke()
        self.assertEqual(self.state(), before)

    def test_successful_update_and_uninstall(self):
        self.existing_installation()
        self.assertEqual(self.invoke(), 0)
        destination, receipt = installer.cli_paths()
        self.assertEqual(destination.read_bytes(), b'new launcher')
        self.assertTrue(installer.owned_launcher(destination, installer.cli_registration()))
        self.assertEqual((self.environment / 'dependency.txt').read_bytes(), b'new dependency')
        self.assertEqual(self.invoke('uninstall'), 0)
        self.assertFalse(self.environment.exists())
        self.assertFalse(destination.exists())
        self.assertFalse(receipt.exists())

    def test_uninstall_preserves_externally_replaced_command(self):
        self.existing_installation()
        destination, receipt = installer.cli_paths()
        destination.write_bytes(b'external command')
        self.assertEqual(self.invoke('uninstall'), 0)
        self.assertEqual(destination.read_bytes(), b'external command')
        self.assertFalse(receipt.exists())
        self.assertFalse(self.environment.exists())

    def test_command_collision_is_reported_before_environment_mutation(self):
        self.existing_installation()
        installer.cli_paths()[0].write_bytes(b'external command')
        before = self.state()
        with self.assertRaisesRegex(RuntimeError, 'not owned'):
            self.invoke()
        self.assertEqual(self.state(), before)

    def test_failed_recovery_retains_the_previous_environment_and_cli(self):
        self.existing_installation()
        destination, receipt = installer.cli_paths()
        remove = installer.shutil.rmtree
        def cannot_remove_environment(path, *args, **kwargs):
            if Path(path) == self.environment:
                raise PermissionError('injected locked environment')
            return remove(path, *args, **kwargs)
        with patch.object(installer.shutil, 'rmtree', side_effect=cannot_remove_environment):
            with self.assertRaisesRegex(RuntimeError, 'backup retained'):
                self.invoke(pip_exit=23)
        backups = list(self.root.glob('.uai-sdk-install-*'))
        self.assertEqual(len(backups), 1)
        self.assertEqual((backups[0] / 'environment' / 'dependency.txt').read_bytes(), b'previous dependency')
        self.assertEqual((backups[0] / 'cli' / destination.name).read_bytes(), b'previous launcher')
        self.assertEqual((backups[0] / 'cli' / receipt.name).read_bytes(), receipt.read_bytes())


if __name__ == '__main__':
    unittest.main()
