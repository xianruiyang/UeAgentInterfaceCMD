# T33 Editor Automation Runner Contract

`scripts/ue/RunSmokeTests.ps1` accepts structured plans with `preserve_main_editor=true`. A batch may override RHI, Slate, or foreground requirements; omitted RHI flags default to a headless NullRHI worker.

`scripts/ue/UeAutomationCommand.psm1` is the runner's command-transport owner. It builds module loading, filter selection, and exactly one queued `Automation RunTests` command for a batch; callers use the structured runner instead of composing `-ExecCmds` themselves.

- headless, no rendering: owned `UnrealEditor-Cmd` with `-unattended -NullRHI`;
- headless rendering: owned `UnrealEditor-Cmd` with `-unattended` and RHI enabled;
- Slate or foreground interaction: rejected until a dedicated owned interactive runner exists.

The runner allocates a unique system-temp `UserDir`, UAI port, fault port, and generated credential configuration. It records the exact root process identity and owned descendants, protects every pre-existing main Editor identity, and removes only resources whose identity it owns. A diagnostic receipt is optional and, when requested, includes worker mode, main-Editor survival, owned-process cleanup, and isolation cleanup.

Automation results come from the owned run's native JSON report, with per-test paths and unlocalized enum states retained in `automation_results`. A zero process exit is insufficient: failed, skipped, unfinished, or missing requested tests are not reported as passed. Controller error-level completion logs also preserve failure if report export did not finish; localized display text is not parsed as a success token. Reports stay under that run's `runtime_root/automation`.

No runner path injects Automation into the user's main Editor, forces it to the foreground, disables global background throttling, changes global frame-rate limits, or interprets a frame-rate threshold as a development verdict.
