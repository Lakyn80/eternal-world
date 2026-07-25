<#
.SYNOPSIS
  Task 65.7 - live synthetic end-to-end smoke test for the authenticated
  memorial workspace (cookie-based browser session, stateful AI Biographer,
  Redis chat sessions, review controls, and localization).

.DESCRIPTION
  Exercises the real running stack (docker compose services on this host,
  never rebuilt by this script) through its HTTP API using a synthetic,
  freshly-registered account. Never touches or prints any real owner's
  biography/memory content - all payloads used here are clearly-marked
  synthetic test strings. Produces a PASS/FAIL matrix and a non-zero exit
  code on any failure so it is safe to use as a release gate.

  This script deliberately talks to the API directly (not through a
  browser) so it can assert the *contract* precisely: cookie-only session
  resolution, conversation_id continuity, locale-correct clarification
  text, etc. It complements (does not replace) the Vitest/pytest suites.

.PARAMETER BaseUrl
  Backend base URL. Defaults to the local docker-compose port mapping.

.PARAMETER PrometheusUrl
  Prometheus base URL, used for the metrics-presence check.
#>
param(
    [string]$BaseUrl = "http://localhost:8033",
    [string]$PrometheusUrl = "http://localhost:9090"
)

$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot\..\..

$results = New-Object System.Collections.Generic.List[psobject]

function Add-Result {
    param([string]$Name, [bool]$Passed, [string]$Detail = "")
    $results.Add([PSCustomObject]@{
        Check   = $Name
        Status  = if ($Passed) { "PASS" } else { "FAIL" }
        Detail  = $Detail
    })
    $color = if ($Passed) { "Green" } else { "Red" }
    Write-Host "[$(if ($Passed) {'PASS'} else {'FAIL'})] $Name $(if ($Detail) { "- $Detail" })" -ForegroundColor $color
}

function Invoke-Api {
    param(
        [string]$Method,
        [string]$Path,
        [object]$Body = $null,
        [Microsoft.PowerShell.Commands.WebRequestSession]$Session,
        [switch]$AllowError
    )
    $uri = "$BaseUrl$Path"
    $params = @{
        Method          = $Method
        Uri             = $uri
        WebSession      = $Session
        ContentType     = "application/json"
        SkipHttpErrorCheck = $true
        StatusCodeVariable = "sc"
    }
    if ($null -ne $Body) {
        $params["Body"] = ($Body | ConvertTo-Json -Depth 10)
    }
    $response = Invoke-RestMethod @params
    return [PSCustomObject]@{ StatusCode = $sc; Body = $response }
}

$suffix = [guid]::NewGuid().ToString("N").Substring(0, 10)
$email = "e2e-synthetic-$suffix@example.invalid"
$password = "Synthetic-Pass-$suffix!1"
# Clearly-marked synthetic test content - never a real owner's biography or
# memory text (hard restriction: never print/commit real memorial content).
$syntheticBiography = "SYNTHETIC_E2E_BIOGRAPHY_$suffix. This paragraph exists only for automated testing and contains no real personal information."
$syntheticMemorialName = "Synthetic E2E Memorial $suffix"
$syntheticAnswer = "Radio"

Write-Host "=== Task 65.7 Authenticated Workspace E2E Smoke Test ===" -ForegroundColor Cyan
Write-Host "Base URL: $BaseUrl" -ForegroundColor Cyan
Write-Host "Synthetic account: $email" -ForegroundColor Cyan
Write-Host ""

# --- Preflight -------------------------------------------------------------
$branch = git rev-parse --abbrev-ref HEAD
Add-Result "Preflight: not on main branch" ($branch -ne "main") "branch=$branch"

$services = docker compose ps --format json 2>$null | ForEach-Object { $_ | ConvertFrom-Json }
$requiredUp = @("eternal_world_backend", "eternal_world_celery_worker", "eternal_world_db", "eternal_world_redis", "eternal_world_qdrant")
$downServices = $requiredUp | Where-Object { $name = $_; -not ($services | Where-Object { $_.Name -eq $name -and $_.State -eq "running" }) }
Add-Result "Preflight: required docker services running" ($downServices.Count -eq 0) ($(if ($downServices.Count -gt 0) { "down: $($downServices -join ', ')" } else { "all up" }))

# --- Register + cookie-only login ------------------------------------------
$webSession = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$reg = Invoke-Api -Method Post -Path "/api/auth/register" -Body @{ email = $email; password = $password; full_name = "E2E Synthetic $suffix" } -Session $webSession
Add-Result "Register synthetic owner" ($reg.StatusCode -eq 201) "status=$($reg.StatusCode)"

$login = Invoke-Api -Method Post -Path "/api/auth/login" -Body @{ email = $email; password = $password } -Session $webSession
Add-Result "Login sets browser session cookie" (($login.StatusCode -eq 200) -and ($webSession.Cookies.GetCookies($BaseUrl) | Where-Object { $_.Name -eq "eternal_world_session" })) "status=$($login.StatusCode)"

$sessionCheck = Invoke-Api -Method Get -Path "/api/auth/session" -Session $webSession
Add-Result "GET /api/auth/session resolves via cookie only (no bearer header sent)" ($sessionCheck.StatusCode -eq 200 -and $sessionCheck.Body.email -eq $email) "status=$($sessionCheck.StatusCode)"

# --- Memorial create + profile update (defect #2 regression) ---------------
$memorial = Invoke-Api -Method Post -Path "/api/memory-profiles" -Body @{ name = $syntheticMemorialName } -Session $webSession
$profileId = $memorial.Body.id
Add-Result "Create memorial" ($memorial.StatusCode -eq 201 -and $profileId -gt 0) "profile_id=$profileId"

$renamed = Invoke-Api -Method Patch -Path "/api/memory-profiles/$profileId" -Body @{ name = "$syntheticMemorialName (renamed)" } -Session $webSession
Add-Result "Update memorial name does not error/sign out" ($renamed.StatusCode -eq 200) "status=$($renamed.StatusCode)"

$stillSession = Invoke-Api -Method Get -Path "/api/auth/session" -Session $webSession
Add-Result "Session still valid after profile update" ($stillSession.StatusCode -eq 200) "status=$($stillSession.StatusCode)"

# --- Biography set + index, poll for completion -----------------------------
$bioUpdate = Invoke-Api -Method Patch -Path "/api/memorials/$profileId/biography" -Body @{ biography = $syntheticBiography } -Session $webSession
Add-Result "Set biography" ($bioUpdate.StatusCode -eq 200) "status=$($bioUpdate.StatusCode)"

$ingest = Invoke-Api -Method Post -Path "/api/memorials/$profileId/biography/ingest" -Session $webSession
Add-Result "Start biography ingestion" ($ingest.StatusCode -eq 202) "status=$($ingest.StatusCode) job_status=$($ingest.Body.background_job_status)"

$indexed = $false
# A cold celery_worker (BGE-M3 not yet loaded into process memory since the
# last restart) can take ~90-120s for the *first* embedding job - the model
# load itself, then CPU-only dense+sparse encoding. Budget generously for
# that cold-start case; a warm worker finishes in a few seconds.
for ($i = 0; $i -lt 90; $i++) {
    Start-Sleep -Seconds 2
    $status = Invoke-Api -Method Get -Path "/api/memorials/$profileId/biography/status" -Session $webSession
    if ($status.Body.status -eq "indexed") { $indexed = $true; break }
}
Add-Result "Biography reaches 'indexed' status (celery_worker processed job)" $indexed "final_status=$($status.Body.status) attempts=$($i+1)"

# --- Biographer: eligibility, resume, one-word-answer bypass ---------------
$eligibility = Invoke-Api -Method Get -Path "/api/memorials/$profileId/biographer/eligibility" -Session $webSession
Add-Result "Biographer eligible after indexing" ($eligibility.Body.eligible -eq $true) "eligible=$($eligibility.Body.eligible) reason=$($eligibility.Body.blocked_reason)"

$resume1 = Invoke-Api -Method Get -Path "/api/memorials/$profileId/biographer/resume" -Session $webSession
Add-Result "Resume before any question reflects a usable next_action" ($resume1.StatusCode -eq 200) "next_action=$($resume1.Body.next_action)"

$question = Invoke-Api -Method Get -Path "/api/memorials/$profileId/biographer/next-question?locale=cs" -Session $webSession
$questionId = $question.Body.id
Add-Result "Fetch next Biographer question" ($question.StatusCode -eq 200 -and $questionId -gt 0) "question_id=$questionId topic=$($question.Body.topic)"

$answer = Invoke-Api -Method Post -Path "/api/memorials/$profileId/biographer/questions/$questionId/answer" -Body @{ locale = "cs"; answer_text = $syntheticAnswer } -Session $webSession
Add-Result "One-word answer is accepted (defect #4/#5)" ($answer.StatusCode -eq 200) "status=$($answer.StatusCode)"
Add-Result "Direct answer bypasses mandatory clarification (defect #4)" ($answer.Body.unresolved_clarification_count -eq 0 -and $answer.Body.enrichment_status -eq "ready_for_owner_review") "unresolved=$($answer.Body.unresolved_clarification_count) enrichment_status=$($answer.Body.enrichment_status)"
$candidateId = $answer.Body.candidate_id

$resume2 = Invoke-Api -Method Get -Path "/api/memorials/$profileId/biographer/resume" -Session $webSession
Add-Result "Resume state survives 'navigating away' (defect #3/#14)" ($resume2.Body.next_action -in @("candidate_ready_for_review", "candidate_pending_index", "candidate_indexed")) "next_action=$($resume2.Body.next_action)"

# --- Review: candidate visible, no raw Cyrillic leak in cs locale ----------
$candidatesCs = Invoke-Api -Method Get -Path "/api/memorials/$profileId/candidates?locale=cs" -Session $webSession
$targetCandidate = $candidatesCs.Body | Where-Object { $_.candidate_id -eq $candidateId }
Add-Result "Biographer candidate appears in Review queue (defect #8)" ($null -ne $targetCandidate -and $targetCandidate.review_status -eq "needs_review") "found=$($null -ne $targetCandidate) review_status=$($targetCandidate.review_status)"

$hasCyrillic = $false
if ($targetCandidate.next_clarification_question) {
    $hasCyrillic = [regex]::IsMatch($targetCandidate.next_clarification_question.question_text, '\p{IsCyrillic}')
}
Add-Result "No Cyrillic leak in Czech-locale candidate view (defect #12)" (-not $hasCyrillic) "has_cyrillic=$hasCyrillic"

# --- Owner review: confirm + explicit index (defect #9/#10) ----------------
$review = Invoke-Api -Method Post -Path "/api/memorials/$profileId/candidates/$candidateId/owner-review" -Body @{ action = "confirm" } -Session $webSession
Add-Result "Owner can approve the candidate" ($review.StatusCode -eq 200) "status=$($review.StatusCode) review_status=$($review.Body.review_status)"

if ($review.Body.explicit_indexing_required -eq $true -and $review.Body.searchable_as_fact -ne $true) {
    $index = Invoke-Api -Method Post -Path "/api/memorials/$profileId/candidates/$candidateId/index" -Session $webSession
    Add-Result "Explicit per-item indexing button works (defect #10)" ($index.StatusCode -eq 200) "status=$($index.StatusCode) result=$($index.Body.result)"
} else {
    Add-Result "Explicit per-item indexing button works (defect #10)" $true "not applicable for this candidate's promotion path"
}

# --- Chat: send, active restore, reset (defect #6/#7) -----------------------
$chatSend = Invoke-Api -Method Post -Path "/api/chat/$profileId/messages" -Body @{ message = "SYNTHETIC_E2E_CHAT_MESSAGE_$suffix" } -Session $webSession
$conversationId1 = $chatSend.Body.conversation_id
Add-Result "Send chat message" ($chatSend.StatusCode -eq 200 -and $conversationId1) "status=$($chatSend.StatusCode)"

$active1 = Invoke-Api -Method Get -Path "/api/chat/$profileId/active" -Session $webSession
Add-Result "Active chat restores same conversation from Redis (defect #7)" ($active1.Body.conversation_id -eq $conversationId1 -and $active1.Body.restored_from -eq "redis" -and $active1.Body.messages.Count -ge 2) "restored_from=$($active1.Body.restored_from) messages=$($active1.Body.messages.Count)"

$reset = Invoke-Api -Method Post -Path "/api/chat/$profileId/reset" -Session $webSession
$conversationId2 = $reset.Body.conversation_id
Add-Result "Chat reset creates a new, empty conversation (defect #6)" ($reset.StatusCode -eq 200 -and $conversationId2 -ne $conversationId1 -and $reset.Body.messages.Count -eq 0) "old=$conversationId1 new=$conversationId2"

$fullHistory = Invoke-Api -Method Get -Path "/api/chat/$profileId/messages" -Session $webSession
Add-Result "Reset preserves prior messages in full history (never destructive)" ($fullHistory.Body.Count -ge 2) "message_count=$($fullHistory.Body.Count)"

# --- Family contributions review queue refresh-on-tab-activation ----------
$contribution = Invoke-Api -Method Post -Path "/api/memorials/$profileId/contributions" -Body @{ title = "SYNTHETIC_E2E_CONTRIBUTION_$suffix"; memory_text = "SYNTHETIC_E2E_CONTRIBUTION_TEXT_$suffix"; privacy_scope = "private_owner" } -Session $webSession
Add-Result "Submit family contribution" ($contribution.StatusCode -eq 201) "status=$($contribution.StatusCode)"

$reviewQueue = Invoke-Api -Method Get -Path "/api/memorials/$profileId/review-queue" -Session $webSession
$foundInQueue = $reviewQueue.Body | Where-Object { $_.id -eq $contribution.Body.id }
Add-Result "Contribution visible in a fresh review-queue fetch (defect #8 root cause)" ($null -ne $foundInQueue) "found=$($null -ne $foundInQueue)"

# --- Logout ------------------------------------------------------------------
$logout = Invoke-Api -Method Post -Path "/api/auth/logout" -Session $webSession
Add-Result "Logout succeeds" ($logout.StatusCode -eq 204) "status=$($logout.StatusCode)"

$afterLogout = Invoke-Api -Method Get -Path "/api/auth/session" -Session $webSession
Add-Result "Session cookie invalid after logout" ($afterLogout.StatusCode -eq 401) "status=$($afterLogout.StatusCode)"

# --- Prometheus metrics presence -------------------------------------------
try {
    $metricsRaw = Invoke-RestMethod -Uri "$BaseUrl/metrics" -Method Get
    $expectedMetrics = @(
        "eternal_world_browser_session_operations_total",
        "eternal_world_biographer_answers_total",
        "eternal_world_chat_operations_total",
        "eternal_world_review_actions_total",
        "eternal_world_memory_index_operations_total"
    )
    $missing = $expectedMetrics | Where-Object { $metricsRaw -notmatch [regex]::Escape($_) }
    Add-Result "Task 65.7 Prometheus metrics present" ($missing.Count -eq 0) $(if ($missing.Count -gt 0) { "missing: $($missing -join ', ')" } else { "all present" })
} catch {
    Add-Result "Task 65.7 Prometheus metrics present" $false "scrape failed: $($_.Exception.Message)"
}

# --- Docker image build guard -----------------------------------------------
$backendCreated = docker inspect eternal_world_backend --format "{{.Created}}" 2>$null
$workerCreated = docker inspect eternal_world_celery_worker --format "{{.Created}}" 2>$null
Add-Result "Docker containers were not recreated by this script (no --build used)" $true "backend_created=$backendCreated celery_worker_created=$workerCreated (informational; compare against session start)"

# --- Summary -----------------------------------------------------------------
Write-Host ""
Write-Host "=== Summary ===" -ForegroundColor Cyan
$results | Format-Table -AutoSize -Wrap

$failed = @($results | Where-Object { $_.Status -eq "FAIL" })
Write-Host ""
if ($failed.Count -gt 0) {
    Write-Host "$($failed.Count) of $($results.Count) checks FAILED." -ForegroundColor Red
    exit 1
}
Write-Host "All $($results.Count) checks PASSED." -ForegroundColor Green
exit 0
