param(
    [switch]$Clean
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

if ($Clean) {
    Remove-Item -Recurse -Force "$Root\dist" -ErrorAction SilentlyContinue
    Remove-Item -Recurse -Force "$Root\build_tmp" -ErrorAction SilentlyContinue
}

Write-Host "[1/3] Check PyInstaller ..."
python -m PyInstaller --version | Out-Null
$hasPyInstaller = ($LASTEXITCODE -eq 0)

if (-not $hasPyInstaller) {
    Write-Host "[2/3] Install PyInstaller ..."
    python -m pip install pyinstaller
    if ($LASTEXITCODE -ne 0) {
        throw "Install pyinstaller failed."
    }
} else {
    Write-Host "[2/3] PyInstaller already installed"
}

Write-Host "[3/3] Build one-file executable ..."
python -m PyInstaller `
  --onefile `
  --name uai-cli `
  --paths "$Root\cli" `
  --distpath "$Root\dist" `
  --workpath "$Root\build_tmp" `
  --specpath "$Root\build_tmp" `
  "$Root\build_entry.py"
if ($LASTEXITCODE -ne 0) {
    throw "PyInstaller build failed."
}

Copy-Item "$Root\uai-cli.default.json" "$Root\dist\uai-cli.default.json" -Force

Write-Host "Build done: $Root\dist\uai-cli.exe"
