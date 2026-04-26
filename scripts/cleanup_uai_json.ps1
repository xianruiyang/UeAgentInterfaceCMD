param(
    [Parameter(Mandatory = $false)]
    [string]$ProjectRoot = (Resolve-Path "..\\..").Path,
    [Parameter(Mandatory = $false)]
    [int]$TmpMax = 120,
    [Parameter(Mandatory = $false)]
    [int]$TmpKeep = 40,
    [Parameter(Mandatory = $false)]
    [int]$ReportsMax = 200,
    [Parameter(Mandatory = $false)]
    [int]$ReportsKeep = 120
)

$scriptPath = Join-Path $ProjectRoot "scripts\\cleanup_uai_json.ps1"
if (-not (Test-Path $scriptPath)) {
    throw "missing_script: $scriptPath"
}

powershell -ExecutionPolicy Bypass -File $scriptPath `
    -ProjectRoot $ProjectRoot `
    -TmpMax $TmpMax `
    -TmpKeep $TmpKeep `
    -ReportsMax $ReportsMax `
    -ReportsKeep $ReportsKeep
