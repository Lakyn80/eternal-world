# Brain RAG Eval — multilingual family avatar (cs, ru, en, es, fr)
# Run from repository root: .\scripts\run_brain_rag_eval_multilingual.ps1

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..

Write-Host "=== Brain RAG Eval preflight ===" -ForegroundColor Cyan
docker compose exec backend python scripts/run_brain_rag_eval.py --preflight
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$caseSets = @(
    "family_avatar_cs",
    "family_avatar_ru",
    "family_avatar_en",
    "family_avatar_es",
    "family_avatar_fr"
)

$results = @()

foreach ($caseSet in $caseSets) {
    Write-Host ""
    Write-Host "=== Running case set: $caseSet ===" -ForegroundColor Cyan
    docker compose exec backend python scripts/run_brain_rag_eval.py --case-set $caseSet
    $exitCode = $LASTEXITCODE
    $results += [PSCustomObject]@{
        CaseSet = $caseSet
        ExitCode = $exitCode
        Status = if ($exitCode -eq 0) { "PASS" } else { "FAIL" }
    }
    if ($exitCode -ne 0) {
        Write-Host "FAILED: $caseSet" -ForegroundColor Red
    } else {
        Write-Host "PASSED: $caseSet" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "=== Summary ===" -ForegroundColor Cyan
$results | Format-Table -AutoSize

Write-Host ""
Write-Host "QA reports (parallel CS/RU/EN/ES/FR questions):" -ForegroundColor Yellow
Write-Host "  backend/artifacts/brain_rag_eval/runs/<run_id>/qa_report.md"
Write-Host "  backend/artifacts/brain_rag_eval/qa_report.md  (latest per run — overwritten each eval)"

$failed = @($results | Where-Object { $_.ExitCode -ne 0 })
if ($failed.Count -gt 0) {
    Write-Host ""
    Write-Host "$($failed.Count) case set(s) failed." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "All multilingual case sets passed." -ForegroundColor Green
exit 0
