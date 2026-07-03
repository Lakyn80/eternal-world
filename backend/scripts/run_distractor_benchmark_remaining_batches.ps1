$ErrorActionPreference = "Continue"
Set-Location $PSScriptRoot | Out-Null
Set-Location ..

$Art = "artifacts/real_question_eval/eternal_world_distractor_full_benchmark"
$Ds = "app/modules/real_question_eval/datasets/eternal_world_distractor_v1.json"
$LogDir = Join-Path $Art "run_logs"
New-Item -ItemType Directory -Force -Path $LogDir | Out-Null

$EnvFlags = @(
    "-e", "REAL_QUESTION_EVAL_USE_REAL_LOCAL_MODELS=1",
    "-e", "SENTENCE_TRANSFORMERS_DEVICE=cpu"
)

function Invoke-BenchmarkBatch {
    param(
        [string]$Name,
        [string[]]$DockerArgs
    )
    $LogPath = Join-Path $LogDir "$Name.log"
    Write-Host "=== START $Name ===" 
    $command = @("compose", "exec") + $EnvFlags + @(
        "backend", "python", "scripts/run_real_question_eval.py",
        "--use-real-local-models",
        "--artifact-dir", $Art,
        "--dataset-file", $Ds
    ) + $DockerArgs
    & docker @command 2>&1 | Tee-Object -FilePath $LogPath
    $exitCode = $LASTEXITCODE
    Write-Host "=== END $Name exit_code=$exitCode log=$LogPath ==="
    return $exitCode
}

$results = @{}

if (-not (Test-Path (Join-Path $Art "latest_full_version_batch_b/real_question_eval_summary.json"))) {
    $results["batch_b"] = Invoke-BenchmarkBatch "batch_b_qwen3_embedding_0_6b" @(
        "--rerun-attempted-full-version-batch-b",
        "--full-version-batch-b-providers", "qwen3_embedding_0_6b"
    )
} else {
    Write-Host "SKIP batch_b: artifact already exists"
}

if (-not (Test-Path (Join-Path $Art "latest_full_version_batch_c/real_question_eval_summary.json"))) {
    $results["batch_c"] = Invoke-BenchmarkBatch "batch_c_jina_embeddings_v3" @(
        "--full-version-batch-c-providers", "jina_embeddings_v3"
    )
} else {
    Write-Host "SKIP batch_c: artifact already exists"
}

if (-not (Test-Path (Join-Path $Art "latest_full_version_batch_d/real_question_eval_summary.json"))) {
    $results["batch_d"] = Invoke-BenchmarkBatch "batch_d_bge_m3_hybrid" @(
        "--full-version-batch-d-providers", "bge_m3_dense_sparse,bge_m3_dense_sparse_multivector"
    )
} else {
    Write-Host "SKIP batch_d: artifact already exists"
}

python scripts/generate_distractor_full_benchmark_aggregate.py
Write-Host "Remaining batch exit codes:"
$results.GetEnumerator() | ForEach-Object { Write-Host "$($_.Key)=$($_.Value)" }
