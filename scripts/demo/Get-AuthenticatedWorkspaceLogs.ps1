<#
.SYNOPSIS
  Task 65.7 - bounded, safe observability snapshot for the authenticated
  memorial workspace: structured log event counts, Prometheus metric
  values, and Redis session/chat key metadata.

.DESCRIPTION
  Collects EVIDENCE, never CONTENT. It only ever prints: event names,
  counts, status codes, durations, TTLs, and key-name prefixes/counts. It
  never prints a biography, a memory/chat message body, an email address
  beyond what's already visible in a docker log line the app itself wrote,
  or any Redis VALUE (only key existence/TTL via SCAN, never GET).

.PARAMETER SinceMinutes
  How far back to read backend/celery_worker container logs. Bounded by
  design (default 30 minutes) so this never becomes an unbounded log dump.
#>
param(
    [int]$SinceMinutes = 30,
    [string]$PrometheusUrl = "http://localhost:9090"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..\..

Write-Host "=== Task 65.7 Authenticated Workspace - Observability Snapshot ===" -ForegroundColor Cyan
Write-Host "Window: last $SinceMinutes minute(s)" -ForegroundColor Cyan
Write-Host ""

# --- Structured log event counts (backend) ----------------------------------
Write-Host "--- Backend structured log events (Task 65.7 event names, count only) ---" -ForegroundColor Yellow
$eventsOfInterest = @(
    "browser_session_created",
    "browser_session_resumed",
    "browser_session_revoked",
    "browser_session_expired",
    "browser_session_invalid",
    "biographer_answer_accepted",
    "biographer_candidate_ready_for_review",
    "biographer_stuck_state_repaired",
    "biography_indexing_completed",
    "biography_indexing_failed"
)

$rawLogs = docker compose logs backend --since "${SinceMinutes}m" --no-log-prefix 2>$null
$eventCounts = @{}
foreach ($name in $eventsOfInterest) { $eventCounts[$name] = 0 }
foreach ($line in $rawLogs) {
    foreach ($name in $eventsOfInterest) {
        if ($line -match [regex]::Escape("`"event`": `"$name`"")) {
            $eventCounts[$name]++
        }
    }
}
$eventCounts.GetEnumerator() | Sort-Object Name | ForEach-Object {
    Write-Host ("  {0,-40} {1}" -f $_.Key, $_.Value)
}

$requestCount = ($rawLogs | Select-String -Pattern '"event": "request_completed"').Count
$errorCount = ($rawLogs | Select-String -Pattern '"level": "ERROR"').Count
Write-Host ""
Write-Host "  request_completed total: $requestCount"
Write-Host "  ERROR-level log lines:   $errorCount"

# --- Celery worker job summary -----------------------------------------------
Write-Host ""
Write-Host "--- Celery worker job outcomes (status only) ---" -ForegroundColor Yellow
$workerLogs = docker compose logs celery_worker --since "${SinceMinutes}m" --no-log-prefix 2>$null
$succeeded = ($workerLogs | Select-String -Pattern "succeeded in").Count
$failedJobs = ($workerLogs | Select-String -Pattern "\bfailed\b").Count
Write-Host "  succeeded: $succeeded"
Write-Host "  failed:    $failedJobs"

# --- Prometheus metric values -------------------------------------------------
Write-Host ""
Write-Host "--- Prometheus metric values (Task 65.7 + Task 66.1) ---" -ForegroundColor Yellow
$metricsToQuery = @(
    "eternal_world_browser_session_operations_total",
    "eternal_world_profile_updates_total",
    "eternal_world_biographer_resume_total",
    "eternal_world_biographer_answers_total",
    "eternal_world_chat_operations_total",
    "eternal_world_chat_redis_operations_total",
    "eternal_world_review_actions_total",
    "eternal_world_memory_index_operations_total",
    "eternal_world_localization_fallback_total",
    "ai_action_steps_total",
    "ai_provider_attempts_total"
)
foreach ($metric in $metricsToQuery) {
    try {
        $resp = Invoke-RestMethod -Uri "$PrometheusUrl/api/v1/query?query=$metric" -Method Get
        $series = $resp.data.result
        if ($series.Count -eq 0) {
            Write-Host ("  {0,-42} (no series yet)" -f $metric)
        } else {
            foreach ($s in $series) {
                $labels = ($s.metric.PSObject.Properties | Where-Object { $_.Name -ne "__name__" } | ForEach-Object { "$($_.Name)=$($_.Value)" }) -join ","
                Write-Host ("  {0,-42} {1,-8} [{2}]" -f $metric, $s.value[1], $labels)
            }
        }
    } catch {
        Write-Host ("  {0,-42} (query failed: {1})" -f $metric, $_.Exception.Message) -ForegroundColor Red
    }
}

# --- Redis session/chat key metadata (never values) --------------------------
Write-Host ""
Write-Host "--- Redis key metadata (counts + TTL only, values never read) ---" -ForegroundColor Yellow
$redisPatterns = @(
    "eternal_world:auth:session:*",
    "eternal_world:chat:active:*"
)
foreach ($pattern in $redisPatterns) {
    $keys = docker compose exec -T redis redis-cli --scan --pattern $pattern 2>$null
    $keyList = @($keys | Where-Object { $_ -and $_.Trim() })
    Write-Host "  Pattern: $pattern -> $($keyList.Count) key(s)"
    foreach ($key in ($keyList | Select-Object -First 5)) {
        $ttl = docker compose exec -T redis redis-cli TTL $key 2>$null
        Write-Host "    $key  ttl=${ttl}s"
    }
    if ($keyList.Count -gt 5) {
        Write-Host "    ... ($($keyList.Count - 5) more, not listed)"
    }
}

# --- Docker service/image evidence (no build) --------------------------------
Write-Host ""
Write-Host "--- Docker service state (evidence this script never builds images) ---" -ForegroundColor Yellow
docker compose ps --format "table {{.Name}}\t{{.State}}\t{{.Status}}"
Write-Host ""
docker compose images backend celery_worker frontend 2>$null

Write-Host ""
Write-Host "=== Snapshot complete ===" -ForegroundColor Cyan
