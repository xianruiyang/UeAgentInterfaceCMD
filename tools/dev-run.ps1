param(
    [string]$Plan = ".\plans\sample_plan_list_actors.json",
    [string]$Vars = ".\vars\sample_vars.json"
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

python ".\run_uai_cli.py" doctor --json-output
python ".\run_uai_cli.py" run --plan $Plan --vars $Vars --json-output
