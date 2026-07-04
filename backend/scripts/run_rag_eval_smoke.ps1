$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..\..")

docker compose exec backend python scripts/run_rag_eval_smoke.py
exit $LASTEXITCODE
