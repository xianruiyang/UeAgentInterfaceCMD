from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


PROJECT = Path(r"D:\program\UE\GptProjectTest")
POWERSHELL = shutil.which("pwsh.exe") or shutil.which("pwsh") or "pwsh.exe"
MODULE = PROJECT / "scripts/ue/automation/UeEditorBuildLifecycle.psm1"
SCRIPT = PROJECT / "scripts/ue/automation/Invoke-UePluginBuildLifecycle.ps1"
LIFECYCLE_MODULE = PROJECT / "scripts/ue/UeLifecycleHost.psm1"


def _powershell_json(script: str) -> object:
    completed = subprocess.run(
        [
            str(POWERSHELL),
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-Command",
            script,
        ],
        check=True,
        cwd=PROJECT,
        text=True,
        capture_output=True,
        encoding="utf-8",
    )
    return json.loads(completed.stdout.strip())


def test_build_lifecycle_closes_builds_and_restores_only_when_needed() -> None:
    payload = _powershell_json(
        f"Import-Module -Force '{MODULE}'; "
        "$running = New-UeEditorBuildLifecyclePlan -WasMainEditorRunning $true; "
        "$closed = New-UeEditorBuildLifecyclePlan -WasMainEditorRunning $false; "
        "[pscustomobject]@{running=$running;closed=$closed} | ConvertTo-Json -Depth 8 -Compress"
    )
    assert payload["running"]["actions"] == [
        "graceful_close_main_editor",
        "ordinary_development_build",
        "restore_main_editor_minimized",
    ]
    assert payload["closed"]["actions"] == ["ordinary_development_build"]
    assert payload["running"]["live_coding_allowed"] is False
    assert payload["running"]["force_kill_allowed"] is False


def test_live_coding_inputs_are_rejected_by_the_build_lifecycle() -> None:
    payload = _powershell_json(
        f"Import-Module -Force '{MODULE}'; "
        "$values = @('-LiveCoding', '-LiveCoding=true', 'LiveCoding.Compile'); "
        "$results = foreach ($value in $values) { Test-UeEditorBuildLifecycleArgument -Argument $value }; "
        "$results | ConvertTo-Json -Depth 8 -Compress"
    )
    assert all(item["success"] is False for item in payload)
    assert {item["failure_code"] for item in payload} == {"build_live_coding_forbidden"}


def test_vscode_build_task_uses_the_restoring_lifecycle_entry() -> None:
    tasks = json.loads((PROJECT / ".vscode/tasks.json").read_text(encoding="utf-8-sig"))
    build = next(item for item in tasks["tasks"] if item["group"] == "build")
    assert build["args"][4].endswith("scripts\\ue\\automation\\Invoke-UePluginBuildLifecycle.ps1")
    assert "LiveCoding" not in json.dumps(build, ensure_ascii=False)


def test_smoke_runner_owns_worker_isolation_without_global_throttle_overrides() -> None:
    source = (PROJECT / "scripts/ue/RunSmokeTests.ps1").read_text(encoding="utf-8-sig")
    assert '"headless_nullrhi"' in (PROJECT / "scripts/ue/UeLifecycleHost.psm1").read_text(encoding="utf-8-sig")
    assert '"headless_rhi"' in (PROJECT / "scripts/ue/UeLifecycleHost.psm1").read_text(encoding="utf-8-sig")
    assert "-UserDir=$isolationRoot" in source
    assert "New-UeLifecycleOwnedServerAllocation" in source
    assert "Stop-UeLifecycleOwnedProcesses" in source
    assert "main_editor_survival" in source
    forbidden = ["t.MaxFPS", "Use Less CPU when in Background", "DisableBackgroundThrottle"]
    assert all(item not in source for item in forbidden)


def test_smoke_runner_plugin_override_is_opt_in_and_rejects_argument_injection() -> None:
    runner = PROJECT / "scripts/ue/RunSmokeTests.ps1"
    source = runner.read_text(encoding="utf-8-sig")
    assert "[string[]]$EnablePlugins = @()" in source
    assert "$EnablePlugins.Count -gt 0 -and $batches.Count -ne 1" in source
    assert 'if ($EnablePlugins.Count -gt 0) { $args += "-EnablePlugins=$($EnablePlugins -join \',\')" }' in source
    for invalid in ("ModelViewViewModel -ExecCmds=Quit", "ModelViewViewModel,Other"):
        completed = subprocess.run(
            [str(POWERSHELL), "-NoProfile", "-File", str(runner),
             "-UERoot", "unused", "-ProjectPath", "unused", "-PlanPath", "unused",
             "-EnablePlugins", invalid],
            cwd=PROJECT, text=True, capture_output=True, encoding="utf-8",
        )
        assert completed.returncode != 0
        assert "EnablePlugins" in completed.stderr
        assert "Pattern" in completed.stderr or "pattern" in completed.stderr


def test_owned_process_tree_rejects_reused_pid_ancestry() -> None:
    payload = _powershell_json(
        f"Import-Module -Force '{LIFECYCLE_MODULE}'; "
        "$rootTime = [datetime]'2026-08-11T16:49:45Z'; "
        "$snapshot = @("
        "[pscustomobject]@{ProcessId=400;ParentProcessId=0;CreationDate=$rootTime},"
        "[pscustomobject]@{ProcessId=401;ParentProcessId=400;CreationDate=[datetime]'2026-08-10T03:09:16Z'},"
        "[pscustomobject]@{ProcessId=402;ParentProcessId=400;CreationDate=[datetime]'2026-08-11T16:49:46Z'},"
        "[pscustomobject]@{ProcessId=403;ParentProcessId=402;CreationDate=[datetime]'2026-08-11T16:49:47Z'},"
        "[pscustomobject]@{ProcessId=404;ParentProcessId=401;CreationDate=[datetime]'2026-08-11T16:49:48Z'}"
        "); "
        "$root = [pscustomobject]@{process_id=400;start_time_utc='2026-08-11T16:49:45.0000000Z'}; "
        "$present = @(Get-UeOwnedProcessTreeIds -RootProcessId 400 -RootProcessIdentity $root -ProcessSnapshot $snapshot); "
        "$absent = @(Get-UeOwnedProcessTreeIds -RootProcessId 999 -RootProcessIdentity ([pscustomobject]@{process_id=999;start_time_utc='2026-08-11T16:49:45.0000000Z'}) -ProcessSnapshot $snapshot); "
        "[pscustomobject]@{present=$present;absent=$absent} | ConvertTo-Json -Depth 8 -Compress"
    )
    assert payload["present"] == [400, 402, 403]
    assert payload["absent"] == []


def test_plan_only_entry_never_changes_editor_or_build_state() -> None:
    completed = subprocess.run(
        [
            str(POWERSHELL),
            "-NoProfile",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(SCRIPT),
            "-UERoot",
            r"D:\Epic Games\UE_5.6",
            "-ProjectPath",
            str(PROJECT / "GptProjectTest.uproject"),
            "-PlanOnly",
            "-AssumeMainEditorRunning",
        ],
        check=True,
        cwd=PROJECT,
        text=True,
        capture_output=True,
        encoding="utf-8",
    )
    payload = json.loads(completed.stdout.strip())
    assert payload["plan_only"] is True
    assert payload["actions"][-1] == (
        "restore_main_editor_uai_ready_minimized"
    )
