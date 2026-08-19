# T33 Editor Automation Runner Contract

`scripts/ue/RunSmokeTests.ps1` accepts only structured plans with `preserve_main_editor=true`. Each batch declares whether it needs RHI, Slate, or foreground interaction.

- headless, no rendering: owned `UnrealEditor-Cmd` with `-unattended -NullRHI`;
- headless rendering: owned `UnrealEditor-Cmd` with `-unattended` and RHI enabled;
- Slate or foreground interaction: rejected until a dedicated owned interactive runner exists.

The runner allocates a unique system-temp `UserDir`, UAI port, fault port, and generated credential configuration. It records the exact root process identity and owned descendants, protects every pre-existing main Editor identity, and removes only resources whose identity it owns. The receipt includes worker mode, main-Editor survival, owned-process cleanup, isolation cleanup, and the observed FPS gate.

No runner path injects Automation into the user's main Editor, forces it to the foreground, disables global background throttling, or changes global frame-rate limits. Current-machine 10 FPS claims require a real owned-worker receipt; static configuration is not evidence of runtime FPS.
