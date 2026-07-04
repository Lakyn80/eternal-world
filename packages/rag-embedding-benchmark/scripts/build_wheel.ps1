$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot

python -m pip install --upgrade build
python -m build

Write-Host "Wheel artifacts:"
Get-ChildItem dist
