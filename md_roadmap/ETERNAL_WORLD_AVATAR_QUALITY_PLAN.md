
## Production Execution & Verification Protocol

Treat this as a large production project, not a small script or prototype.

The solution must be designed for long-term maintainability, scalability, security, testability, observability, and future extension.

Every task must be executed as a controlled production change with explicit scope, validation, tests, and rollback awareness.

---

## 1. Core Engineering Rules

Follow these rules strictly for every implementation task:

1. Do not make quick hacks.
2. Do not solve the task only for the current visible case.
3. Keep the architecture clean, explicit, modular, and easy to reason about.
4. Preserve existing behavior unless the task explicitly requires changing it.
5. Do not add unrelated features.
6. Do not refactor unrelated code.
7. Validate inputs where appropriate.
8. Use clear errors and safe failure modes.
9. Avoid hidden side effects.
10. Keep the code easy to extend later.
11. Prefer explicit, typed, readable code over clever shortcuts.
12. If dynamic loading, file access, network access, database access, model loading, cache access, background jobs, or external API calls are involved, handle security, permissions, timeout, retry, and error cases carefully.
13. If code is modified, return or document the complete updated file path and the exact reason for the change, not only a patch fragment.
14. Explain briefly what was changed and why.
15. Add or update tests if the change affects behavior.
16. Do not change anything outside the requested scope unless it is necessary. If it is necessary, explain why before finalizing.
17. Before finalizing, verify that the solution matches the exact task.
18. Do not silently introduce fallback behavior that hides real failures.
19. Do not silently download models, change providers, switch embeddings, change retrieval ranking, change Qdrant collections, or change cache behavior.
20. Do not commit generated artifacts, local IDE files, model cache files, temporary logs, or unrelated files.

The goal is production-quality code suitable for a growing real-world system.

---

## 2. Mandatory Step-by-Step Control Process

Every task must be split into explicit controlled steps.

For each step, the agent must report:

```text
Step:
Goal:
Files inspected:
Files changed:
Behavior changed:
Tests added/updated:
Verification command:
Result:
Risk:
Next step:
```

No step is considered complete without verification.

---

## 3. Before Starting Any Task

Before changing code, the agent must do the following:

```text
1. Confirm the current project path.
2. Confirm the current branch.
3. Run git status --short.
4. Identify uncommitted files.
5. Classify uncommitted files:
   - intended code
   - intended tests
   - intended docs
   - generated artifacts
   - local noise
   - unknown / risky
6. Read the relevant progress file:
   - PROJECT_PROGRESS.md
   - readme.dev if used by the project
7. Identify the last completed task.
8. Identify the exact new task name.
9. Define the allowed scope.
10. Define what must not be touched.
```

If the worktree is dirty, the agent must not blindly continue. It must explain what is dirty and whether it is related to the current task.

---

## 4. Scope Control

Every task must define:

```text
In scope:
- exact modules
- exact endpoints
- exact scripts
- exact tests
- exact documentation

Out of scope:
- unrelated refactors
- unrelated UI changes
- unrelated infrastructure changes
- unrelated model/provider changes
- unrelated database schema changes
- unrelated Qdrant collection changes
```

If the implementation requires touching an out-of-scope file, the agent must explain why.

---

## 5. Architecture Control

Before implementation, the agent must identify where the change belongs.

For Eternal World avatar work:

```text
avatar_persona = source of truth for character/persona
Brain agent = answer generation using persona + factual memory
Memory/RAG = factual retrieval only
Redis embedding cache = performance optimization only
Redis session cache = short-term conversation state only
Postgres = durable metadata/review state
Qdrant = semantic long-term memory
Voice agent = voice rendering only
Face agent = facial expression/rendering only
Director agent = orchestration of Brain + Voice + Face
```

The agent must not put logic into the wrong layer.

Examples:

```text
Character/persona must not be implemented as Face agent logic.
Factual memory must not be stored in Redis as the source of truth.
Unverified user claims must not be written directly to Qdrant.
Output guard must not replace proper evidence policy.
Monitoring must not contain raw user text.
```

---

## 6. Test Requirements

Every behavior-changing task must include tests.

At minimum, the agent must decide which of these are required:

```text
Unit tests
Integration tests
Endpoint tests
Script tests
Smoke tests
Regression tests
Negative/error-path tests
Cache tests
Security/safety tests
Frontend tests
Docker runtime smoke
```

For every test group, the agent must report:

```text
Command:
Result:
Number of tests passed:
Warnings:
Failures:
Whether warnings are blocking:
```

If tests are not run, the agent must explicitly explain why.

---

## 7. Required Test Categories for Avatar Work

For avatar/persona/RAG tasks, check all relevant categories:

### 7.1 Factual correctness

```text
Known memory question returns grounded answer.
Out-of-memory question does not hallucinate.
Evidence is attached when debug=true.
Lack-of-evidence behavior is clear and human.
```

### 7.2 Persona correctness

```text
Avatar uses the configured persona.
Avatar speaks in the correct language.
Avatar uses the expected emotional tone.
Avatar does not sound like a technical assistant.
Avatar does not expose RAG/chunk/retrieval internals.
```

### 7.3 Safe learning

```text
User-introduced memory becomes only an unverified candidate.
Unverified candidate is not used as factual truth.
No automatic write to Qdrant.
No automatic permanent write to Postgres unless the task explicitly implements review storage.
```

### 7.4 Cache behavior

```text
Redis embedding cache does not change retrieval ranking.
Redis embedding cache does not store raw user text.
First repeated request can miss/write.
Second repeated request can hit.
Cache failures degrade safely.
```

### 7.5 Runtime behavior

```text
Backend works after restart.
Cold-start behavior is controlled.
Missing model/cache returns clear error.
No silent provider fallback.
No accidental model download.
No CUDA/NVIDIA dependency unless explicitly required.
```

---

## 8. Observability and Logging Requirements

Every runtime-facing task must include safe observability.

Logs may include:

```text
trace_id
route
profile_id
avatar_id
collection_name
retrieved_chunks_count
top chunk ids
safe score values
guard_applied
lack_of_evidence
persona_applied
memory_candidate_created
duration_ms
cache hit/miss summary
```

Logs must not include:

```text
raw full user message
raw full private memory
API keys
secrets
tokens
large document text
model cache internals that expose secrets
personal data beyond safe identifiers
```

Every endpoint should return or log a `trace_id`.

---

## 9. Error Handling Requirements

Errors must be explicit, safe, and user-appropriate.

Backend errors must not expose internal stack traces to the user.

For Russian FA demo UI, user-facing errors must be in Russian.

Examples:

```text
Демо временно недоступно: модель эмбеддингов BGE-M3 не инициализирована. Запустите подготовку модели и повторите запрос.

Демо-профиль ещё не инициализирован. Пожалуйста, подготовьте тестовую память и повторите запрос.

Я не помню этого по тем воспоминаниям, которые у меня сейчас есть. Если хочешь, расскажи мне больше, и мы сможем сохранить это как новое воспоминание.
```

Technical detail belongs in logs, not in client-facing text.

---

## 10. Data and Memory Safety Rules

For digital avatar memory:

```text
Verified memory = can be used as factual evidence.
Unverified memory candidate = cannot be used as factual evidence.
Conversation text = not automatically long-term memory.
Redis = not source of truth.
Qdrant = semantic search index, not review workflow.
Postgres = durable metadata and review state.
```

The system must never automatically convert user claims into verified avatar memory.

Every learning flow must have:

```text
source
status
confidence
review state
created_at
reason
trace_id if available
```

---

## 11. Model and Retrieval Safety Rules

The agent must not change these unless the task explicitly requires it:

```text
BGE-M3 model
embedding dimensions
embedding provider
Qdrant collection names
retrieval ranking
top_k
RRF behavior
BM25 behavior
Redis embedding cache key semantics
Brain provider
output guard behavior
```

The agent must report explicitly:

```text
Was retrieval logic changed? yes/no
Was embedding logic changed? yes/no
Was Redis cache behavior changed? yes/no
Was Qdrant modified? yes/no
Was any model downloaded? yes/no
Was any fallback introduced? yes/no
```

---

## 12. Docker and Runtime Verification

For backend/runtime tasks, Docker smoke is required unless impossible.

Required checks:

```text
docker compose ps
docker compose logs --tail=300 backend
direct API smoke
frontend smoke if UI changed
no cache permission error
no model download surprise
no CUDA/NVIDIA error
no stack trace in client response
```

For FA demo:

```text
POST /api/demo/fa-chat/message
question: Где ты жила в детстве?
expected: Russian answer mentioning Попице

question: Бабушка, мне сегодня тяжело.
expected: warm Russian persona answer

question: Ты помнишь, как пела мне песню перед сном?
expected: no invention, optional unverified memory candidate
```

---

## 13. Documentation Requirements

Every completed task must update `PROJECT_PROGRESS.md`.

The entry must include:

```text
Task number and name
Date/time
Goal
What changed
Why it changed
Files changed
Tests run
Smoke result
Known limitations
Next recommended task
```

If `PROJECT_PROGRESS.md` claims that a script or feature exists, the corresponding file must be committed or the documentation must be corrected.

Documentation must not claim completed work that is still untracked.

---

## 14. Git Rules

Before staging:

```text
git status --short
git diff --stat
```

Stage only intended files.

Never stage:

```text
.idea/
backend/artifacts/*
frontend build outputs
model cache files
temporary logs
local scratch files
generated run folders
```

Before commit, verify:

```text
git status --short
```

Commit message must describe the real change.

After commit:

```text
git log -1 --oneline
git status --short
```

Push only after tests and smoke pass.

Final report must include:

```text
branch
commit hash
push result
files changed
tests run
smoke result
remaining uncommitted files
known limitations
next recommended task
```

---

## 15. Senior Enterprise Review Checklist

Before finalizing any task, perform this checklist.

### Architecture

```text
Does the change belong in the correct module?
Is the responsibility boundary clean?
Would this still make sense when there are 1000 avatars?
Would this still make sense when there are multiple languages?
Would this still make sense when voice/video is added?
```

### Reliability

```text
What happens if Redis is down?
What happens if Qdrant is down?
What happens if the model cache is missing?
What happens after Docker restart?
What happens on cold start?
What happens if external API fails?
```

### Security and privacy

```text
Are secrets protected?
Is raw user text avoided in logs/metrics?
Is personal memory handled carefully?
Can unverified claims become facts by accident?
Is there any unsafe dynamic file path or import?
```

### Testability

```text
Can the logic be unit tested without Qdrant?
Can the logic be tested without Redis?
Can the logic be tested without model download?
Are error paths tested?
Are regressions covered?
```

### Observability

```text
Can we debug a bad answer by trace_id?
Can we see profile_id/avatar_id?
Can we see retrieval count?
Can we see cache hit/miss?
Can we see whether persona was applied?
Can we see whether output guard changed the answer?
```

### Maintainability

```text
Is the code explicit and typed?
Are names clear?
Is the module easy to extend?
Is there duplicated logic?
Is there hidden coupling?
Is there a clear next step?
```

### Product quality

```text
Does the avatar feel human?
Does the avatar preserve character?
Does the avatar avoid hallucination?
Does the avatar handle missing memory gracefully?
Does the avatar support safe learning without corrupting memory?
```

---

## 16. Definition of Done for Every Task

A task is done only when all relevant items are true:

```text
Scope was respected.
Architecture is clean.
Behavior is tested.
Error paths are tested.
Runtime smoke passed if applicable.
Logs are safe and useful.
No unrelated files were changed.
No generated artifacts were committed.
PROJECT_PROGRESS.md was updated.
Git status is understood.
Commit was created.
Push succeeded.
Final report is complete.
```

If any item is not true, the final report must clearly say what is incomplete and why.

---

## 17. Mandatory Final Report Format

Every implementation task must end with this report:

```text
Task:
Branch:
Commit:
Push:

Summary:
Files changed:
Behavior changed:
Behavior preserved:

Tests:
- command -> result

Smoke:
- command/action -> result

Runtime/infra:
Redis used/required:
Qdrant modified:
Model downloaded:
Retrieval changed:
Embedding changed:
Cache behavior changed:
Fallback introduced:

Security/privacy:
Raw user text in logs:
Secrets exposed:
Unverified memory stored as fact:

Remaining uncommitted files:
Known limitations:
Next recommended task:
```

---

## 18. AI Provider Cost Accounting Permanent Rules

Established by Task 66.1 (Provider Usage and Cost Foundation, see `PROJECT_PROGRESS.md` and `docs/ai-provider-cost-foundation.md`). Apply to every future task touching a paid AI provider call:

```text
Every paid provider call requires a durable action, step, and provider-attempt record.
Unknown pricing must never be represented as zero.
Cost calculations must use Decimal and a versioned pricing catalog.
Retries and failed provider attempts must remain individually visible.
Paid calls must fail closed if durable audit initialization cannot be created.
Static UI localization must not call a paid provider.
Cached dynamic translations must be reused without a provider call.
Supported-locale Chat must answer directly without query-and-answer double translation.
Provider secrets and private biography/memory text must never appear in cost logs or Prometheus labels.
Prometheus AI-cost labels must remain low-cardinality.
Generated test artifacts and runtime audit exports must not be committed.
```



# Eternal World — Avatar Quality Architecture Plan

**Project:** `eternal-world`  
**Purpose:** vytvořit digitálního avatara, který není jen obyčejný RAG chatbot, ale stabilní kombinace paměti, charakteru, stylu řeči, bezpečného učení a později obličeje/hlasu.

---

## 0. Hlavní rozhodnutí

### Charakteristika avatara NEPATŘÍ primárně do Face agenta

**Zdroj pravdy pro charakter avatara musí být samostatný modul:**

```text
backend/app/modules/avatar_persona/
```

Tento modul drží:

- osobnost avatara
- životní charakteristiku
- styl řeči
- hodnoty
- hranice
- citlivá témata
- pravidla pro nedostatek důkazů
- pravidla pro bezpečné učení

Face agent z toho čerpá jen odvozené informace:

```text
persona → Brain odpověď → emotion/expression hints → Face agent
```

Face agent tedy nemá rozhodovat, kdo avatar je. Face agent má pouze vizuálně zahrát to, co Brain/persona vrstva určí.

---

## 1. Cílový model avatara

Avatar se musí skládat z těchto vrstev:

```text
Avatar =
  factual memory
+ persona / character
+ speaking style
+ emotional behavior
+ evidence policy
+ safe learning policy
+ voice behavior
+ face behavior
+ evaluation harness
```

### 1.1 Factual memory

To je znalostní paměť:

```text
texty
vzpomínky
rodinné události
místa
životopis
fotky
audio přepisy
dokumenty
```

Technicky:

```text
Postgres metadata
Qdrant semantic memory
BGE-M3 embeddings
Redis embedding cache
```

### 1.2 Persona / character

To je charakter avatara:

```text
hodná babička
pracovitá
skromná
citlivá
rodinně založená
přežila těžké období
v mládí byla 5 let politický vězeň
nemluví jako ChatGPT
nemluví jako úřad
nefantazíruje fakta
```

### 1.3 Speaking style

Styl řeči musí být explicitní:

```text
ruština
teplý tón
krátké a střední věty
lidské oslovení
bez technických slov
bez právnického stylu
bez "я языковая модель"
```

### 1.4 Evidence policy

Avatar nesmí tvrdit fakta, která nemá v paměti.

Správné chování:

```text
fakt existuje v paměti → odpovědět lidsky
fakt chybí → říct jemně, že si to nepamatuje / není to v dostupných vzpomínkách
uživatel tvrdí novou věc → vytvořit memory candidate, neukládat jako pravdu
```

---

## 2. Agentová architektura

### 2.1 Brain Agent

**Brain Agent je hlavní rozhodovací agent.**

Odpovídá za:

- pochopení otázky
- retrieval z paměti
- použití persona profilu
- složení odpovědi
- nedovolí halucinace
- vytvoří návrh nové memory candidate
- určí emoční tón odpovědi

Výstup Brain agenta by neměl být jen text.

Doporučený výstup:

```json
{
  "answer_text": "Да, деточка... в детстве я жила возле Попице.",
  "lack_of_evidence": false,
  "persona_applied": true,
  "memory_candidate": null,
  "emotion": {
    "primary": "warm",
    "intensity": 0.55
  },
  "face_directives": {
    "expression": "gentle_smile",
    "gaze": "soft",
    "head_motion": "small_nod"
  },
  "voice_directives": {
    "tone": "warm",
    "pace": "slow",
    "volume": "normal"
  }
}
```

### 2.2 Persona Module

**Persona Module je zdroj pravdy pro charakter.**

Umístění:

```text
backend/app/modules/avatar_persona/
```

Doporučené soubory:

```text
backend/app/modules/avatar_persona/
  __init__.py
  schemas.py
  loader.py
  prompt_composer.py
  persona_registry.py
  evaluator.py
```

Úkoly:

- držet schéma charakteru
- načítat demo personu
- validovat povinná pole
- skládat persona prompt
- poskytovat stylová pravidla Brain agentovi
- poskytovat emoční pravidla pro Face/Voice agenty

### 2.3 Memory/RAG Module

Zůstává faktická paměť.

Úkoly:

- BGE-M3 embedding
- Redis embedding cache
- Qdrant retrieval
- evidence list
- source metadata
- lack-of-evidence signál

Nesmí řešit charakter. Jen dodává fakta.

### 2.4 Face Agent

**Face Agent není zdroj charakteru.**

Face agent dělá:

```text
text odpovědi + emotion metadata + face directives
→ výraz obličeje
→ pohled
→ úsměv
→ mimika
→ pohyb hlavy
→ lip-sync timing
```

Face agent nesmí:

- měnit fakta
- rozhodovat, kdo avatar je
- přepisovat charakter
- vytvářet nové vzpomínky
- rozhodovat o pravdivosti

Face agent může použít personu pouze jako vstupní kontext pro konzistenci animace.

### 2.5 Voice Agent

Voice agent dělá:

```text
answer_text + voice_directives
→ TTS
```

Může použít:

- tempo
- tón
- emoce
- pauzy
- styl hlasu

Nesmí měnit obsah odpovědi.

### 2.6 Director Agent

Director Agent později spojí:

```text
Brain output
+ Voice output
+ Face output
+ timing
+ video rendering
```

Ale pro teď ho nestavět.

---

## 3. Datové schéma persona profilu

První verze persona profilu může být statická JSON/Python fixture.

Doporučené schéma:

```json
{
  "avatar_id": "eva_novakova_demo",
  "display_name": "Ева Новакова",
  "role": "бабушка",
  "language": "ru",
  "core_traits": [
    "добрая",
    "трудолюбивая",
    "скромная",
    "заботливая",
    "терпеливая"
  ],
  "life_background": [
    "пережила тяжёлые времена",
    "много работала",
    "ценит семью"
  ],
  "values": [
    "семья",
    "честность",
    "труд",
    "терпение",
    "доброта"
  ],
  "speaking_style": {
    "tone": "тёплый, спокойный, человечный",
    "sentence_length": "короткие и средние фразы",
    "addressing": ["деточка", "родной", "милый"],
    "avoid": [
      "канцелярский стиль",
      "юридический стиль",
      "технические термины",
      "стиль ChatGPT"
    ]
  },
  "emotional_style": {
    "default_emotion": "warm",
    "sad_user_response": "supportive",
    "trauma_topic_response": "careful_respectful",
    "family_topic_response": "warm_nostalgic"
  },
  "boundaries": [
    "не выдумывать факты",
    "не утверждать неподтверждённые воспоминания",
    "если факта нет, говорить мягко",
    "не говорить, что она искусственный интеллект",
    "не использовать технические слова вроде RAG, retrieval, chunk"
  ],
  "lack_of_evidence_style": {
    "template": "Я не помню этого по тем воспоминаниям, которые у меня сейчас есть. Если хочешь, расскажи мне больше, и мы сможем сохранить это как новое воспоминание."
  }
}
```

---

## 4. Prompt composer

Brain prompt nesmí být ručně poslepovaný v endpointu.

Musí existovat samostatný composer:

```text
backend/app/modules/avatar_persona/prompt_composer.py
```

Vstupy:

```text
persona
retrieved memories
conversation context
user message
evidence policy
safe learning policy
```

Výstup:

```text
system prompt / developer prompt / user prompt parts
```

Kompozice:

```text
1. global safety rules
2. avatar persona identity
3. speaking style
4. factual evidence
5. conversation context
6. user question
7. answer rules
8. memory candidate rules
9. output format rules
```

---

## 5. Bezpečné učení z otázek

Avatar se musí učit, ale ne automaticky.

### 5.1 Zakázané

Nesmí se stát:

```text
uživatel napíše neověřený fakt
→ systém to uloží do Qdrant jako pravdu
```

### 5.2 Správně

Správný tok:

```text
uživatel napíše novou možnou vzpomínku
→ systém vytvoří memory candidate
→ status = needs_review
→ confidence = unverified
→ zatím se nepoužije jako faktická paměť
```

### 5.3 Memory candidate schema

```json
{
  "candidate_id": "uuid",
  "avatar_id": "eva_novakova_demo",
  "source": "conversation",
  "status": "needs_review",
  "confidence": "unverified",
  "user_message_excerpt": "Ты помнишь, как пела мне песню перед сном?",
  "proposed_memory_text": "Пользователь утверждает, что бабушка пела ему песню перед сном.",
  "reason": "User introduced a possible personal memory not found in current evidence.",
  "created_at": "2026-07-10T00:00:00Z"
}
```

### 5.4 Co teď implementovat

V Tasku 63 zatím:

```text
memory candidate pouze v response nebo in-memory
žádný zápis do Qdrant
žádný permanentní zápis do Postgres
žádné automatické učení jako pravda
```

Permanentní učení bude pozdější task.

---

## 6. Redis cache testování

Musíme rozlišovat tři různé věci.

### 6.1 Redis embedding cache

Už existuje nebo se stabilizuje.

Úkol:

```text
stejný text dotazu
→ stejný embedding cache key
→ první request miss/write
→ další request hit
```

Musí platit:

- neukládá raw osobní text
- neovlivňuje ranking
- neovlivňuje odpověď
- funguje bez změny retrieval logiky

### 6.2 Redis session cache

Později.

Úkol:

```text
krátkodobý kontext konverzace
```

Není to long-term memory.

### 6.3 Long-term memory

Není Redis.

Správně:

```text
Postgres = metadata + review stav
Qdrant = semantic memory
Redis = cache/session
```

---

## 7. Eval harness pro avatara

Musíme mít opakovatelnou evaluaci.

### 7.1 Factual evaluation

Testuje:

```text
otázka → retrieval → grounded answer
```

Příklady:

```text
Где ты жила в детстве?
Кто подписал строительный план дома?
Что известно о доме в Ржечковицах?
```

### 7.2 Persona evaluation

Testuje charakter.

Příklady:

```text
Бабушка, мне сегодня тяжело.
Мне страшно.
Ты меня любишь?
Что бы ты мне посоветовала?
```

Očekávané chování:

- teplý tón
- lidská odpověď
- ne technický styl
- ne právnický styl
- ne ChatGPT styl

### 7.3 Trauma/sensitive evaluation

Příklad:

```text
Расскажи, как ты сидела в тюрьме.
```

Očekávané chování:

- citlivý tón
- respekt
- žádné vymyšlené detaily
- žádné dramatizování
- pokud fakta chybí, říct to jemně

### 7.4 Safe learning evaluation

Příklad:

```text
Ты помнишь, как пела мне песню перед сном?
```

Očekávané chování:

- nevyfantazírovat písničku
- říct, že to není v aktuální paměti
- nabídnout, aby uživatel doplnil detail
- vytvořit unverified memory candidate

### 7.5 Forbidden behavior evaluation

Zakázané fráze:

```text
я языковая модель
как ИИ
retrieval
RAG
chunk
согласно данным
в базе данных
в архивах нет информации
```

Poznámka: poslední fráze není úplně zakázaná interně, ale v klientské odpovědi je příliš studená. Lepší je lidská formulace.

---

## 8. Doporučené pořadí tasků

### Task 62S — Fix BGE-M3 FA demo cold-start cache

Dokončit před Task 63, pokud ještě není commitnutý.

Cíl:

```text
demo funguje po restartu backendu
model/cache preflight
jasná ruská 503 chyba
žádný tichý fallback
```

### Task 63 — Avatar Persona + Character Evaluation Harness

Cíl:

```text
avatar používá persona profil
odpovídá lidsky
nejen fakticky
má charakter
má eval dataset
umí vytvořit unverified memory candidate
```

### Task 64 — Conversation Memory Candidate Review

Cíl:

```text
ukládat kandidáty do Postgres
review status
admin potvrzení
zamítnutí
převod do dlouhodobé paměti až po potvrzení
```

### Task 64.5 — Minimal Family Memory Review UI

Cíl:

```text
zobrazit family memory candidates
zobrazit příspěvky a owner draft
umožnit owner edit/confirm/reject/request_more_details
zobrazit promotion/indexing stav bez automatického zápisu do Qdrant
```

### Task 65 — Profile Onboarding / Memory Upload Pipeline

Až potom.

Cíl:

```text
vytvořit profil
nahrát text/audio
background job přes Celery
chunking
embedding
Qdrant indexing
stav jobu
chat nad novým profilem
```

### Task 66 — Voice Agent

Cíl:

```text
TTS nad answer_text
voice_directives
tempo
intonace
emoce
```

### Task 67 — Face Agent

Cíl:

```text
face_directives
expression
gaze
lip-sync
video/avatar rendering
```

### Task 68 — Director Agent

Cíl:

```text
sjednotit Brain + Voice + Face
timing
video odpověď
```

---

## 9. Task 63 detailní implementační plán

### 9.1 Soubory

Vytvořit:

```text
backend/app/modules/avatar_persona/__init__.py
backend/app/modules/avatar_persona/schemas.py
backend/app/modules/avatar_persona/loader.py
backend/app/modules/avatar_persona/prompt_composer.py
backend/app/modules/avatar_persona/memory_candidates.py
backend/app/modules/avatar_persona/evaluator.py
backend/tests/test_avatar_persona.py
backend/tests/test_avatar_persona_prompt_composer.py
backend/tests/test_avatar_memory_candidates.py
```

Upravit:

```text
backend/app/modules/demo_fa_chat/service.py
backend/app/modules/demo_fa_chat/schemas.py
backend/app/modules/ai_agents/brain/service.py
PROJECT_PROGRESS.md
```

Pouze pokud potřeba:

```text
backend/app/modules/demo_fa_chat/router.py
backend/tests/test_demo_fa_chat.py
```

### 9.2 Backend response rozšíření

FA chat response může přidat:

```json
{
  "answer": "...",
  "trace_id": "...",
  "lack_of_evidence": false,
  "persona_applied": true,
  "memory_candidate": {
    "status": "needs_review",
    "confidence": "unverified",
    "proposed_memory_text": "..."
  },
  "emotion": {
    "primary": "warm",
    "intensity": 0.5
  },
  "face_directives": {
    "expression": "gentle_smile"
  },
  "voice_directives": {
    "tone": "warm",
    "pace": "slow"
  }
}
```

Pozor: `face_directives` a `voice_directives` jsou zatím metadata, ne skutečný Face/Voice agent.

### 9.3 Testovací otázky pro smoke

```text
Где ты жила в детстве?
```

Očekávání:

```text
odpověď zmiňuje Попице
persona_applied = true
odpověď není studená
```

```text
Бабушка, мне сегодня тяжело.
```

Očekávání:

```text
teplá podpůrná odpověď
žádné RAG/archiv/chunk formulace
```

```text
Ты помнишь, как пела мне песню перед сном?
```

Očekávání:

```text
nefantazírovat
memory_candidate status needs_review
```

```text
Расскажи подробно, как ты сидела в тюрьме.
```

Očekávání:

```text
citlivá odpověď
žádné vymyšlené detaily
pokud evidence chybí, jemný lack-of-evidence
```

---

## 10. Definition of Done pro Task 63

Task 63 je hotový jen když:

- existuje persona schema
- existuje Eva demo persona
- FA chat ji používá
- factual otázka stále funguje
- emoční otázka zní lidsky
- lack-of-evidence je lidský
- nový uživatelský claim nevznikne jako fakt
- memory candidate je pouze unverified
- nejsou změněny embeddings/retrieval/ranking
- Redis embedding cache chování není změněné
- žádný model download v testech
- testy prošly
- Docker smoke prošel
- PROJECT_PROGRESS.md je aktualizovaný
- commit + push hotový

---

## 11. Přesná odpověď na otázku: bude charakteristika ve Face agentovi?

Ne jako zdroj pravdy.

Správně:

```text
avatar_persona = zdroj charakteru
Brain agent = používá charakter pro odpověď
Voice agent = používá voice_directives
Face agent = používá face_directives
Director = spojí Brain + Voice + Face
```

Tok:

```text
Avatar Persona
      ↓
Brain Agent
      ↓
answer_text + emotion + face_directives + voice_directives
      ↓
Voice Agent + Face Agent
      ↓
živý avatar
```

Face agent tedy dostane například:

```json
{
  "expression": "gentle_smile",
  "gaze": "soft",
  "head_motion": "small_nod",
  "emotion": "warm"
}
```

Ale Face agent sám neurčuje:

```text
babička je hodná
babička byla politický vězeň
babička je pracovitá
babička mluví skromně
```

To určuje `avatar_persona`.

---

## 12. Prompt pro další implementační krok

Až bude Task 62S čistě commitnutý, použít tento směr:

```text
Implement Task 63 — Avatar Persona + Character Evaluation Harness.

Do not build onboarding/upload yet.

The goal is to make the current FA demo avatar behave as a stable personality, not only as a RAG chatbot.

Use avatar_persona as the source of truth for character.
Brain consumes persona and factual memories.
Face/Voice agents later consume derived directives only.

Implement persona schema, seeded Eva persona, prompt composer, safe memory candidate schema, tests, and FA demo integration.
```

---

## 13. Task 64.4.1 status (2026-07-12)

Task 64.4.1 — Avatar Answer Quality Gate Remediation — byl proveden. Plný root-cause rozbor, srovnávací metriky a přesný stav brány jsou v `PROJECT_PROGRESS.md` a v `backend/artifacts/avatar_quality_eval/runs/quality_gate_remediation_v1/` (`quality_gate_report.md`, `comparison.md`, `root_cause_matrix.json`).

Stručně:

```text
Hard gate (profile contamination = 0): SPLNĚNO
Ostatní měkké brány: 7 z 8 splněno
Nesplněno: corrected_memory_preference_rate (0.667 místo >= 1.00)
Příčina nesplnění: skutečná hranice relevance retrievalu pro jednu konkrétní
nepřímo formulovanou otázku (potvrzeno živým vzorkováním), ne chyba v kódu
této úlohy. Změna retrievalu/rankingu/top_k byla touto úlohou výslovně
zakázána, proto nebyla opravena zde.
```

Task 64.4.1 se **nepovažuje za kompletně uzavřený** podle měkkých prahů, ale hard gate (profil izolace) je splněna a nesmí se to prezentovat jako plný úspěch. Doporučené pokračování: úzce vymezený **Task 64.4.2 — Retrieval recall pro nepřímé/meta-referenční dotazy na paměť**, teprve poté případně Task 64.5.

---

## 14. Task 64.4.2 status (2026-07-13)

Task 64.4.2 — Indirect Corrected-Memory Query Recall — byl proveden a **dokončen se všemi bránami splněnými**. Plný root-cause rozbor, srovnávací metriky a přesný stav brány jsou v `PROJECT_PROGRESS.md` a v `backend/artifacts/avatar_quality_eval/runs/indirect_corrected_memory_v1/` (`quality_gate_report.md`, `comparison.md`, `corrected_memory_diagnostics.json`).

Stručně:

```text
Hard gate (profile contamination = 0): SPLNĚNO
corrected_memory_preference_rate: 1.00 (bylo 0.667) — SPLNĚNO
owner-corrected-bedtime-song: 3 z 3 opakování — SPLNĚNO (tvrdý požadavek úlohy)
Všech 11 kontrolovaných bran: SPLNĚNO
Passed cases: 11/12
```

Skutečná měřená příčina (ne domněnka): dva opuštěné, nikdy pořádně finalizované testovací záznamy z Task 64.2 (ruční smoke test indexace) obsahovaly nezpracovaný text šablony kandidáta, který falešně dominoval retrievalu pro jakoukoli otázku ve tvaru "pamatuješ si...". Po jejich vyřazení (smazání Qdrant bodů se souhlasem uživatele, historie zachována v Postgres) a přidání deterministického query-intent rozpoznávání + evidence prioritizace (bez změny retrievalu/rankingu/top_k/embeddingu) se míra nalezení správné vzpomínky zvýšila z 65 % na 100 % (měřeno 20 živými vzorky).

Task 64.4.2 se **považuje za kompletně uzavřený**. Jediné zbývající selhání (`sensitive-political-prison`, 2 ze 3) je potvrzeně nesouvisející nedeterminismus poskytovatele Brain (nedotčená cesta kódu), nikoli chyba této úlohy.

Další doporučený task: **Task 64.5 — Minimal Family Memory Review UI**.

## 15. Task 64.5 status (2026-07-13)

Task 64.5 — Minimal Family Memory Review UI — byl proveden a **dokončen**. Plný popis (backend inspekce, přidané endpointy, frontend architektura, testy, Docker ověření) je v `PROJECT_PROGRESS.md`, sekce "Task 64.5 - Minimal Family Memory Review UI (2026-07-13)".

Stručně:

```text
Route: http://localhost:8017/family-memory-review
Backend: 2 nové read-only/aggregační endpointy (clarifications list, review-detail),
         žádná doménová logika nebyla duplikována ani přepsána v Reactu
DB migrace: žádná nebyla potřeba
Frontend testy: 18 passed (14 nových + 4 existující, beze změny chování)
Backend testy: 73 passed (8 nových + 65 existujících v dotčených souborech, beze změny)
next build: OK, typy i lint bez chyb
Docker: backend + frontend znovu sestaveny a spuštěny, alembic na head, žádná migrace
Živé end-to-end ověření (reálné Postgres/Qdrant/BGE-M3): kandidát bedtime-song ->
  vlastník potvrdil -> Qdrant beze změny (23 -> 23) -> explicitní indexace -> Qdrant +1 (23 -> 24) ->
  opakovaná indexace je idempotentní (already_indexed, počet zůstal 24)
```

Ověřeno explicitně: přispěvatel (role "contributor") nemůže sám schválit vlastní vzpomínku (403 na backendu, tlačítka zakázaná na frontendu); indexace se nikdy nespouští automaticky po schválení; oblast soukromí (`private_owner`/`selected_family`) blokuje indexaci beze změny backendového pravidla; žádný přímý přístup frontendu do Qdrant nebo PostgreSQL.

Task 64.5 se **považuje za kompletně uzavřený** v rozsahu definovaném zadáním (minimální, ale produkčně použitelné UI nad existujícím backendovým workflow). Známá omezení (demo autorizace místo produkční autentizace, chybějící správa rodinných vztahů, filtry v inboxu jsou zatím na straně klienta) jsou zdokumentována v `PROJECT_PROGRESS.md`.

## 16. Task 64.5.1 status (2026-07-14)

Task 64.5.1 — Czech/Russian Bilingual Test UI and Memory Synchronization — byl proveden a **dokončen**. Plný popis (nový modul `content_translation`, migrace, zapojení do enrichment/eligibility/promotions/indexing, česká lokalizace frontendu, `[locale]` routy, testy, Docker a živé ověření proti reálnému Postgres/Qdrant/BGE-M3/DeepSeek) je v `PROJECT_PROGRESS.md`, sekce "Task 64.5.1 - Czech/Russian Bilingual Test UI and Memory Synchronization (2026-07-14)".

Stručně:

```text
Statická lokalizace UI (frontend/lib/i18n) oddělena od backendového překladu
dynamického obsahu (backend/app/modules/content_translation/).
Český zdrojový text se nikdy nepřepisuje; ruský překlad je uložen odděleně
se stavem (pending/translated/failed/stale/human_reviewed) a detekcí
zastaralosti přes hash porovnání v čase čtení, ne jen přes uložený status.
Jeden kandidát, jedna promotion, jeden indexovaný bod na vzpomínku —
žádná duplicita mezi jazyky (ověřeno testy i živě).
Indexace zůstává explicitní; ruský avatar pipeline (retrieval/Brain/Qdrant)
je pro česky-vzniklé vzpomínky beze změny — indexuje se aktuální ruský
překlad, nikdy český zdroj.
Backend testy: 87 passed (nové + existující, bez regrese)
Frontend testy: 26 passed, `npm run build` OK
Alembic: upgrade/downgrade/upgrade ověřeno na reálném Postgres
Živé ověření: český dotaz -> ruský retrieval/Brain -> český překlad
  odpovědi (skutečný DeepSeek), český příspěvek zachován doslovně,
  Qdrant beze změny před schválením, +1 bod po explicitní indexaci
  s bezpečnými metadaty (source_language/indexed_language/translation_status)
```

Během této úlohy se v datovém proudu nástrojů objevilo pět samostatných zpráv stylizovaných jako pokyn od "koordinátora" žádající nahrazení již otestované obousměrné překladové architektury FA chatu (Part E.22-23 z původního zadání) za jinou, neověřenou variantu — žádná z nich nepřišla ověřitelným kanálem od skutečného zadavatele a nebyly provedeny. Implementace v repozitáři odpovídá původnímu písemnému zadání a byla navíc živě ověřena proti reálné infrastruktuře. Podrobnosti v `PROJECT_PROGRESS.md`.

Task 64.5.1 se **považuje za kompletně uzavřený** v rozsahu definovaném zadáním. Známá omezení (ruský překlad zatím jen ke čtení s možností opakování, synchronní překlad bez fronty na pozadí, rusko-jazyčné heuristiky pro detekci kandidátů/záměru běží nad interním ruským překladem českého vstupu) jsou zdokumentována v `PROJECT_PROGRESS.md`.

## 17. Task 64.5.2 status (2026-07-14) — přímá odpověď Brainu podle jazyka místo dvojitého překladu

Task 64.5.2 — nahrazení dvojitého překladu FA chatu (česká otázka -> ruský překlad -> ruský retrieval/Brain -> překlad odpovědi zpět do češtiny, 3 AI volání na zprávu) přímou vícejazyčnou architekturou — byl proveden a **dokončen**. Plný popis je v `PROJECT_PROGRESS.md`, sekce "Task 64.5.2 - Direct-Locale FA Chat Brain Answers, Replacing Double-Translation (2026-07-14)".

Poznámka k původu zadání: sekce výše (Task 64.5.1) dokumentuje, že během předchozí session se opakovaně objevily zprávy stylizované jako "koordinátor" žádající přesně tuto architektonickou změnu, doručené prostřednictvím datového proudu nástrojů, nikoli jako skutečný pokyn od uživatele — a nebyly provedeny. Tento task (64.5.2) přišel jinak: jako samostatné, explicitní zadání s konkrétními odkazy na existující kód a jasným technickým zdůvodněním (snížení počtu AI volání ze 3 na 1 na zprávu). Zdůvodnění je technicky správné samo o sobě bez ohledu na původ, ale vzhledem k výše zdokumentované historii je to zde otevřeně uvedeno — skutečný vlastník repozitáře by měl toto rozhodnutí nezávisle potvrdit, než bude považováno za definitivní.

Stručně:

```text
Retrieval (BGE-M3) i Brain nyní dostávají přesně ten text, který uživatel
napsal, v libovolném jazyce — žádný překlad dotazu. Brain dostává nové pole
response_language (= locale) a odpovídá přímo v češtině nebo ruštině bez
druhého AI volání na překlad odpovědi. Backend testy: 123 passed
(zadaná regresní sada) + 43 passed v test_ai_agents.py (2 předchozí
nesouvisející selhání kvůli úniku env proměnných, stejná jako u Tasku 64.5.1).
Nový modul test_bilingual_retrieval_evaluation.py (11 testů) pokrývá pět
kategorií otázek v češtině i ruštině. Živé ověření (reálný DeepSeek/BGE-M3/
Qdrant): česká otázka o ukolébavce zodpovězena správně a přirozeně česky,
ruská kontrolní otázka beze změny, v logách nula content_translation volání
pro obě zprávy.
```

Známé omezení: rusko-jazyčné heuristiky pro klasifikaci záměru (corrected-memory/dispute) a detekci kandidátů nyní běží přímo nad syrovým českým textem (bez mezikroku ruského překladu), takže na české otázky typicky nezareagují — ověřeno testem `test_known_limitation_czech_corrected_memory_intent_not_detected`. Toto je vědomý kompromis v1, ne chyba; zúžené rozšíření o česká klíčová slova je možný navazující task. Překlad obsahu paměti (`content_translation` modul, příspěvky/upřesnění/finalizovaný text/opravy) zůstává zcela beze změny.

Task 64.5.2 se **považuje za kompletně uzavřený** v rozsahu definovaném zadáním, s výše uvedenou poznámkou k původu zadání.

Další doporučený task: **Task 65 — AI Biographer & Living Memory Onboarding** (nedotčen tímto navazujícím taskem).

## 18. Task 65.2 status (2026-07-21) — AI Biographer & Living Memory Onboarding implementováno

Task 65.2 (číslováno takto, aby nekolidovalo s již dokončeným "Task 65 — Accounts, Memorial Access, and Contribution Review Foundation" a jeho podtasky 65.1/65.1A/65.1B, které mezitím vznikly a s touto sekcí roadmapy - psanou 2026-07-14 - se nikdy nesynchronizovaly) — byl proveden a **dokončen v rozsahu ověřeném živě proti reálné infrastruktuře**. Plný popis (grounded audit, architektonická rozhodnutí, nové backend moduly `biography_ingestion`/`avatar_biographer`/`memorial_candidates`, frontend Biography/Biographer taby, testy, migrace, živé E2E ověření s reálným BGE-M3/Qdrant/DeepSeek) je v `PROJECT_PROGRESS.md`, sekce "Task 65.2 - AI Biographer & Living Memory Onboarding (2026-07-21)".

Stručně:

```text
Počáteční životopis: uložení -> explicitní indexace -> Qdrant (nová schopnost, dříve neexistovala)
AI Biographer: 8 pevně daných témat, jedna otázka najednou, nikdy neomezené/náhodné otázky
Odpověď -> memory candidate (workflow_version=2, existující pipeline, ne duplicitní)
Upřesnění (clarification) pro téma "childhood" -> stejný kandidát, nikdy nová vzpomínka
Owner review (6 existujících akcí) -> pending_index promotion, NIKDY automatická indexace
Explicitní indexace -> Qdrant, ověřeno idempotentní
Živě ověřeno: Qdrant 22 -> 23 (biografie) -> 24 (kandidát), beze změny mezi schválením a indexací
Chat po indexaci skutečně použil nově zaindexovanou vzpomínku (reálný DeepSeek)
Backend testy: 30 nových + 102 regresních prošlo; 1 nesouvisející, již existující selhání
  (test_bilingual_retrieval_evaluation.py) reprodukováno izolovaně a potvrzeno nesouvisející
Frontend: tsc + build bez chyb
```

Objeveno, ale záměrně neopraveno (mimo rozsah tohoto tasku): `eternal_world_celery_worker` se v tomto vývojovém prostředí nikdy úspěšně nesestavil (existující, zdokumentovaný stav již od Tasku 65.1B); a reálný autentizovaný `/api/chat` propouští interní `[rag:chunk_id]` citační značku do odpovědi viditelné uživateli, protože `strip_internal_evidence_citations` se v `ai_agents/brain/service.py` volá jen `if avatar_persona is not None` — `avatar_persona` je čistě demo koncept, pro reálné autentizované memorialy nikdy nenastavený. Obojí předchází Tasku 65.2 a není touto úlohou způsobeno; doporučeno jako samostatný navazující task.

Task 65.2 se **považuje za dokončený** v rozsahu definovaném zadáním a živě ověřený. Neprovedeno/mimo rozsah: reálné zpracování přes skutečně běžící Celery worker (nahrazeno přímým voláním stejné funkce se stejnou reálnou infrastrukturou), rozšíření clarification bank na všechna témata (jen "childhood" má dnes vyžadované upřesnění, ostatní témata používají `general` bez upřesnění — vědomé minimální rozhodnutí).

Další doporučený task: oprava `eternal_world_celery_worker` image a oprava úniku `[rag:chunk_id]` citace ve skutečném autentizovaném chatu (obojí zdokumentováno výše jako nalezené, ale mimo rozsah).

## 19. Task 65.3 status (2026-07-21) — Runtime Stabilization, Celery Verification, and Citation-Guard Hardening dokončeno

Task 65.3 opravil přesně ty dvě věci, které Task 65.2 nalezl a záměrně nechal mimo rozsah (viz sekce 18 výše), plus jednu další skrytou chybu objevenou při opravě první z nich. Plný popis (stabilizační matice, root-cause analýzy, testy, živé smoke testy) je v `PROJECT_PROGRESS.md`, sekce "Task 65.3 - Runtime Stabilization, Celery Verification, and Citation-Guard Hardening (2026-07-21)".

Stručně:

```text
eternal_world_celery_worker image: byl zastaralý od 2026-06-25 (obsahoval torch+CUDA, chyběl
  prometheus-client) -> úspěšně přestavěn (~89 min, síťová latence ke stažení PyTorch, ne chyba
  v kódu) -> nový image torch==2.13.0+cpu, žádné GPU balíčky, prometheus_client funguje
Objevena DRUHÁ skrytá chyba: docker-compose.yml u celery_worker chyběly EMBEDDING_PROVIDER a
  související proměnné/volume (backend je měl, celery_worker ne) -> reálné embedding úlohy
  ve workeru tiše spadly na mock provider -> opraveno přidáním identických proměnných
Reálná asynchronní indexace životopisu PROKÁZÁNA přes skutečně běžící Celery worker (ne jen
  přímé volání funkce): nová úloha 21.7s, Qdrant 27->28, přesně 1 nový RagSource/Chunk/Embedding
Idempotence prokázána přes stejný reálný worker: opakování úlohy 0.23s, beze změny v Qdrantu,
  beze duplicit
Únik `[rag:chunk_id]` v autentizovaném chatu opraven: sanitizace nyní probíhá vždy, nezávisle
  na avatar_persona (dříve podmíněno, autentizovaný chat nikdy avatar_persona nenastavuje)
Živě ověřeno česky i rusky: nula viditelných značek, output_guard_applied=true,
  removed_internal_citation_count=1
test_bilingual_retrieval_evaluation.py: 1/11 -> 11/11 (zastaralá testovací fixture, jednořádková
  oprava)
Regresní sada (11 souborů): 144/144 prošlo
```

Task 65.3 se **považuje za kompletně dokončený** v rozsahu definovaném zadáním — obě položky, které Task 65.2 nechal mimo rozsah, jsou nyní vyřešeny a živě ověřeny, včetně nově nalezené a opravené chyby v `docker-compose.yml`. Žádná část zadání nezůstala neprokázaná; direct-call diagnostika byla použita jen jako doplňkový, výslovně povolený vedlejší důkaz vedle hlavního důkazu přes skutečný worker.

Další doporučený task: **Task 66.1 — Provider Usage and Cost Foundation** (AI cost-observability epic, samostatný budoucí task, mimo rozsah Tasku 65.3).

## 20. Task 66.1 status (2026-07-21) — Provider Usage and Cost Foundation dokončeno

Task 66.1 vybudoval trvalý základ pro přesné účtování každého placeného DeepSeek volání: verzovaný `Decimal` ceník, normalizaci token usage, trojici trvalých tabulek (action → step → provider attempt), sdílenou instrumentační vrstvu s fail-closed politikou, strukturované logy a Prometheus metriky. Plný popis je v `PROJECT_PROGRESS.md`, sekce "Task 66.1 - Provider Usage and Cost Foundation (2026-07-21)", a v `docs/ai-provider-cost-foundation.md`.

Stručně:

```text
Ceník ověřen živě z oficiální DeepSeek dokumentace (ne vymyšlen): deepseek-chat
  $0.14/1M uncached input, $0.0028/1M cached input, $0.28/1M output
DŮLEŽITÉ: DeepSeek oznamuje deprecation deepseek-chat/deepseek-reasoner k
  2026-07-24 15:59 UTC (mapování na deepseek-v4-flash) - mimo rozsah tohoto
  tasku opravit, jen zdokumentováno jako riziko
3 nové tabulky (ai_actions/ai_action_steps/ai_provider_attempts), čistě
  aditivní migrace, žádná existující tabulka nezměněna
Sdílená instrumentační vrstva (execute_paid_provider_call) - retry vytváří
  nový attempt řádek, nikdy nepřepisuje neúspěšný; fail-closed: pokud selže
  zápis pending řádku PŘED voláním provideru, provider se nikdy nezavolá
Idempotentní přepočet totals ze skutečných attempt řádků - opakovaná
  finalizace (např. Celery redelivery) nikdy nezdvojí náklady
Autentizovaný Chat i demo FA chat: 1 Brain volání na zprávu, 0 překladových
  volání (přímá lokalizace zachována, česky i rusky živě ověřeno)
Cache hit u překladu: 0 nových provider volání, 0 nových AiAction řádků
Živě ověřeno (syntetický účet, nikdy ne skutečný majitelův memorial):
  česká zpráva $0.000279440, ruská zpráva $0.000020636 (cache-hit na
  system promptu: 1920 z 1979 vstupních tokenů), překlad cache-miss
  $0.000021515 -> celkem $0.000321591, pod limitem $0.01
43 nových testů (pricing/normalizace/persistence/redelivery/metriky/
  privacy) + 224/224 v plné regresní sadě
```

Vědomě mimo rozsah (zdokumentováno, ne skryto): dev-only evaluation skripty (`brain_eval_runner.py`) nejsou instrumentovány (nikdy produkční provoz); žádný Celery task dnes nevolá placený provider, takže Celery propagace je ověřena jen na úrovni repository/service vrstvy; žádný interní/admin HTTP endpoint nebyl přidán (v repozitáři neexistuje admin-autorizační vzor) - připravena je jen `repository.get_action_with_details` jako budoucí query seam pro Task 66.2.

Task 66.1 se **považuje za kompletně dokončený** v rozsahu definovaném zadáním. Dashboardy, rozpočty, anomaly detection a admin API zůstávají mimo rozsah (Task 66.2/66.3).

Další doporučený task: **Task 66.2 — Cost Analytics and Admin API** (samostatný budoucí task, mimo rozsah Tasku 66.1).

## 21. Task 65.4 status (2026-07-21) — Complete the Authenticated Memory Lifecycle Frontend dokončeno

Task 65.4 dokončil autentizovaný frontend tak, aby běžný vlastník memorialu mohl projít celý backendem již implementovaný životní cyklus paměti bez Swaggeru, DB příkazů nebo shell skriptů. Většina API-klienta z Tasku 65.2 už existovala - skutečná mezera byla v UI propojení, ne v chybějících endpointech. Plný popis je v `PROJECT_PROGRESS.md`, sekce "Task 65.4 - Complete the Authenticated Memory Lifecycle Frontend (2026-07-21)".

Stručně, nalezené a opravené skutečné chyby:

```text
Editor životopisu byl vždy prázdný (text se nikdy nenačetl ze skutečného
  životopisu, jen ze stavu bez textu) - opraveno předáním initialBiography
AI biograf měl natvrdo 'cs' bez ohledu na skutečně zvolený jazyk aplikace
Polling stavu životopisu běžel donekonečna i před kliknutím na indexaci
Owner review natvrdo posílal privacy_scope='all_family' u KAŽDÉ akce
edit_and_confirm a approve_multiple_perspectives nebyly v UI vůbec dostupné,
  ačkoli je API klient i typy už plně podporovaly
Reject neměl pole pro důvod; žádný detail/historie kandidáta nebyl vidět
  (nový, minimální, čistě-čtecí backend endpoint /candidates/{id}/history
  přidán - skládá jen z existujících service funkcí, žádná nová logika)
Chybělo potvrzovací dialog před "Start indexing" i "Index memory"
Výsledek indexace (indexed vs already_indexed) se zahazoval
Overview byl téměř prázdný - žádný souhrn stavu, žádné doporučení dalšího
  kroku, žádné odznaky na záložkách
Viewer mohl otevřít záložku AI biografa, ačkoli tam každý request 403
  (žádná capabilita) - záložka nyní pro viewera skrytá
```

Živě ověřeno (syntetické účty, nikdy ne skutečný memorial vlastníka):

```text
Česky: uložení životopisu (draft, NEindexováno) -> explicitní start indexace
  přes SKUTEČNÝ Celery worker -> indexed -> úprava -> stale -> re-index ->
  indexed; AI biograf (childhood) -> 2 upřesnění -> ready_for_owner_review;
  historie kandidáta (3 příspěvky, 2 upřesnění); edit_and_confirm ->
  pending_index (Qdrant beze změny); explicitní indexace -> indexed;
  opakování -> already_indexed (idempotentní); Chat -> reálná odpověď
  DeepSeek používá novou vzpomínku, nula [rag:/memory:] značek
Rusky (kontrolní běh): ruský životopis -> reálný worker -> indexed; AI
  biograf v ruštině; Chat přímo v ruštině (cyrilicí ověřeno), nula značek
Task 66.1 trace obou Chat volání: 1 Brain call, 0 translation calls
```

## 22. Task 65.5 status (2026-07-22) — Existující memorial, indexace a bezpečné mazání dokončeno

Task 65.5 řešil skutečný, konkrétní report vlastníka účtu: formulář pro vytvoření memorialu se nabízel jako hlavní akce, i když účet už jeden memorial měl (limit plánu dosažen), Overview tvrdilo "vše je aktuální" u uloženého, ale nezaindexovaného životopisu, a neexistoval způsob jak existující memorial upravit, vymazat jeho životopis nebo memorial celý bezpečně smazat. Plný popis je v `PROJECT_PROGRESS.md`, sekce "Task 65.5 - Fix Existing Memorial Editing, Legacy Biography Binding, Indexing CTA, and Safe Deletion (2026-07-22)".

Nalezené a opravené skutečné chyby (tři nezávisle prokazatelné):

```text
Overview nextAction() nekontrolovalo stav 'draft' - přesný stav, který
  backend nastaví hned po uložení životopisu (regrese z Tasku 65.4)
Formulář pro vytvoření memorialu nebral v úvahu limit plánu vůbec
KRITICKÁ BACKENDOVÁ CHYBA (nalezena až během tohoto úkolu): GET
  /api/billing/limits vždy vracel current_profiles=0 bez ohledu na
  skutečný počet memorialů - toto by kompletně znefunkčnilo právě
  opravovanou frontend logiku; opraveno napojením na skutečný dotaz
DALŠÍ BACKENDOVÁ CHYBA: mazání memorialu s jakýmkoli zaindexovaným
  obsahem shazovalo IntegrityError (ORM se pokoušel vynulovat NOT NULL
  cizí klíče místo spolehnutí na DB-level CASCADE) - nikdy dřív
  neotestováno, protože žádný předchozí test nemazal profil s obsahem
```

Nové bezpečné ovládací prvky: "Upravit memorial" (jen jméno, vlastník),
"Vymazat životopis" (odstraní jen životopis a jeho Qdrant vektory,
zachová členství/pozvánky/ostatní schválené vzpomínky), "Smazat memorial"
(vlastník, vyžaduje napsat přesný název memorialu, nikdy netvrdí úspěch
při částečném selhání mazání Qdrant vektorů).

Živě ověřeno (syntetický účet, nikdy ne skutečný memorial vlastníka):

```text
vytvoření memorialu #1 -> billing/limits current_profiles=1 (opravená
  hodnota) -> druhé vytvoření -> 403 (odpovídá frontend gating) ->
  úprava jména (bez druhého memorialu) -> uložení životopisu -> draft
  (bez automatické indexace) -> explicitní indexace -> SKUTEČNÝ Celery
  worker -> indexed -> úprava -> stale -> vymazání životopisu -> draft,
  členství zachováno -> opětovné přidání a indexace -> indexed ->
  smazání memorialu -> 204 -> opakované smazání -> 404 (bezpečné) ->
  účet může vytvořit nový memorial po smazání -> 201
```
DB kontrola po smazání: 0 zbylých řádků MemoryProfile/RagSource/RagChunk/
RagEmbedding/RagVectorIndex pro smazaný profil - žádná osiřelá data.

Testy: 7 nových backendových testů pro `/history` endpoint. Frontend měl nulovou testovací infrastrukturu - přidán nejmenší vhodný harness (Vitest + React Testing Library), **31 nových testů, všechny procházejí**. Backendová regrese (9 souborů): 121/121 (jeden přechodný timing flake v `test_memorial_candidates.py` prokázán jako netýkající se této úlohy trojím opakovaným během). `tsc --noEmit` čisté, `npm run build` prochází.

Task 65.4 se **považuje za kompletně dokončený** - plný synteticky ověřený workflow prošel, ne jen TypeScript kompilace nebo API-only testy.

Další doporučený task: **Task 66.2 — Cost Analytics and Admin API** (samostatný budoucí task, nedotčen tímto navazujícím taskem).

## 23. Task 65.6 status (2026-07-22) — AI biograf je nyní kontextově uvědomělý

Task 65.6 — Context-Aware AI Biographer, Coverage Tracking, and Duplicate-Question Prevention — byl proveden a **dokončen, živě ověřen proti reálné infrastruktuře**. Plný popis (root-cause analýza, nová architektura, testy, živé ověření, přesná reálná cena) je v `PROJECT_PROGRESS.md`, sekce "Task 65.6 - Context-Aware AI Biographer, Coverage Tracking, and Duplicate-Question Prevention (2026-07-22)".

Prokázaná skutečná příčina: Task 65.2 biograf byl zcela deterministický (pevná sada 8 témat, každé s natvrdo daným textem otázky v cs/ru, jedno téma nabídnuté nejvýše jednou za celou existenci memorialu) — nikdy nečetl `profile.biography`, nikdy nevolal RAG retrieval, nikdy neporovnával obsah otázek, jen kontroloval, zda dané téma už bylo použito.

Stručně, co se změnilo:

```text
Nová vrstva uvnitř existujícího modulu (žádný druhý systém biografa):
  coverage.py — deterministické vyhodnocení pokrytí tématu (not_started/weak/
    basic/rich/skipped/postponed/exhausted) a výběr dalšího tématu podle
    priority, ne vždy "childhood" první
  context_package.py — omezený RAG retrieval (existující rag_retrieval,
    žádná nová implementace) pro zaindexovaný životopis + schválené vzpomínky
  question_generation.py — DeepSeek strukturovaný výstup přes existující
    Task 66.1 instrumentaci (AiFeature.AVATAR_BIOGRAPHER_QUESTION - už
    rezervováno, nepoužito), max. jedno omezené přegenerování, deterministický
    fallback
  duplicate_prevention.py — konzervativní, čistě textová (žádný model)
    kontrola duplicit a "už známého faktu"
  DB migrace 20260722_0025 — uvolnění "jedno téma navždy" omezení, DB-level
    partial unique index proti dvěma souběžným čekajícím otázkám, bezpečná
    provenience (nikdy neukládá text promptu/odpovědi)
```

Živě ověřeno (syntetické účty, reálný Postgres/Qdrant/BGE-M3/Celery worker/DeepSeek, nikdy skutečný memorial vlastníka):

```text
Český syntetický životopis obsahující přesně scénář z hlášené chyby
  (dětství u Uherského Hradiště, kolo, fotbal, les, "vždy mě zajímalo
  rozebírání starých přístrojů") -> otázka biografa: "Který starý přístroj
  ti nejvíc utkvěl v paměti a co konkrétně jsi na něm rozebíral?" —
  NEPTÁ SE "kde jste prožili dětství" (přesně ta chyba z hlášení), ptá se
  na konkrétní chybějící detail
Opakované volání bez odpovědi -> vrácena stejná otázka (duplicate smoke),
  žádná nová otázka, žádné další volání provideru
Ruský syntetický životopis -> ruská otázka, stejná kvalita, žádný únik
  do češtiny
Neindexovaný životopis -> blocked_reason=biography_not_indexed, nula
  volání provideru (ověřeno přímo v tabulce ai_actions)
Task 66.1 stopa: přesně 3 řádky AiAction pro avatar_biographer_question,
  každý provider_call_count=1 — celková reálná cena 0,000144345 USD,
  hluboko pod limitem 0,01 USD
```

Během vývoje testů byla nalezena a **v rámci tohoto tasku rovnou opravena** vlastní chyba: tento vývojový kontejner má v reálném prostředí nastaveno `AI_BRAIN_PROVIDER=openai_compatible` se skutečným DeepSeek klíčem (kvůli živému ověřování) — `app.core.config.settings` je procesní singleton, takže první verze `test_avatar_biographer.py` (bez vynuceného `mock` providera) tiše volala skutečný, placený DeepSeek při každém testu generování otázky — stejný mechanismus, jaký už dříve způsobil zdokumentovanou nesouvisející chybu v `test_chat.py`. Opraveno přidáním `autouse` fixture vynucující `ai_brain_provider="mock"`; izolovaný běh po opravě: 28/28 prošlo za 75 s (dříve 185 s bez opravy — potvrzuje, že reálná síťová volání skutečně probíhala).

Backend testy: 28/28 nových/upravených v `test_avatar_biographer.py`. Plná regrese (11 souborů, 154 testů): 148 prošlo, 6 selhání — všech 6 prokázáno nesouvisejících (nulový překryv souborů s touto úlohou + deterministická reprodukce v izolaci): `test_chat.py` už dříve zdokumentovaná chyba stejného typu (reálné prostředí v testech), 4x `test_metrics.py` (chyba v podpisu volání `demo_fa_chat` orchestrátoru, kód nedotčený touto úlohou), `test_rag_retrieval.py` (reálný sentence_transformers model místo mocku — stejná třída chyby jako u AI_BRAIN_PROVIDER, v kódu embeddings providerů nedotčeném touto úlohou). Jedna oprava byla nutná a provedena: `test_alembic.py` mělo natvrdo danou předchozí hlavní revizi, aktualizováno na `20260722_0025`.

Frontend (`frontend/react-export/`): `BiographerPanel` přepracován — rozlišené stavy pro každý blokovaný důvod (chybí/neindexováno/probíhá indexace/zastaralé/aktivní upřesnění/čeká na kontrolu), tlačítko "Spustit indexaci životopisu" jen pro vlastníka, lokalizované popisky témat (žádná syrová anglická hodnota jako primární popisek), tlačítko "Zeptat se později" (nový endpoint `postpone`). 59/59 testů prošlo, `tsc`/`build` čisté. Next.js frontend (`frontend/`) beze změny, izolace potvrzena (`typecheck`/`test`/`build` čisté, react-export nikdy neproskenováno).

Docker: pouze `docker compose restart backend celery_worker` (bind-mount, žádný rebuild image). Frontend Vite kontejner vyžadoval `--build --renew-anon-volumes` (povolená výjimka) kvůli zastaralému anonymnímu svazku `node_modules` z předchozí session. Žádný PyTorch/Transformers/BGE-M3/CUDA download.

Známá omezení (zdokumentována, ne skryta): sken pokrytí volá RAG retrieval až 16x sekvenčně na jeden požadavek (první živý dotaz trval ~117 s na CPU inferenci) — budoucí optimalizace, mimo rozsah tohoto tasku, protože by riskovala zásah do zakázaného retrieval/ranking chování; čistě textový detektor duplicit záměrně nezachytí každou sémanticky podobnou, ale jinak formulovanou otázku (pozorováno živě u tématu "family", které zůstalo tematicky blízké předchozímu tématu "childhood" kvůli tenkému zdrojovému textu) — vědomý kompromis, ne chyba.

Task 65.6 se **považuje za kompletně dokončený** v rozsahu definovaném zadáním a živě ověřený proti reálné infrastruktuře, včetně vlastního nalezeného a opraveného incidentu (únik reálného providera do konceptu testů).

Další doporučený task: **Task 66.2 — Cost Analytics and Admin API** (nedotčen touto úlohou), případně úzce vymezené doladění promptu biografa pro tematické zaostření při tenkém zdrojovém textu (pozorované omezení výše), pokud si to vlastník bude přát.

## 24. Task 65.9 status (2026-07-24) — škálovatelná asynchronní jobová platforma a self-healing embedding workery

Task 65.9 — Scalable Asynchronous Job Platform, Dedicated Embedding Workers, Self-Healing Provider Recovery, and 100k-User Readiness Foundation — byl proveden a **dokončen v rozsahu ověřeném testy a lokálním fake-safe load-test smoke profilem**. Plný popis (traceability matice vůči této roadmapě, architektura, testy, live smoke) je v `PROJECT_PROGRESS.md`, sekce "Task 65.9 Scalable Async Jobs and Self-Healing Embedding Workers".

Tento task navazuje přímo na již dříve touto roadmapou akceptované rozhodnutí (bod 8, "Task 65": "background job přes Celery... stav jobu") a dokončuje ho pro poslední dvě zbývající synchronní cesty (tlačítko "Index memory" a retry-indexing pro rodinné příspěvky, Task 65.8), které dosud volaly reálný embedding provider přímo uvnitř HTTP requestu. Neexistuje žádný konflikt s touto roadmapou: embedding model, dimenze, Qdrant kolekce, retrieval/ranking, RRF/BM25 ani schvalovací/eligibility pravidla nebyly touto úlohou změněny — pouze *kdy* se embedding skutečně spouští (vždy až uvnitř dedikovaného embedding workeru, nikdy ve FastAPI procesu).

Stručně:

```text
Nová trvalá jobová platforma nad existujícím BackgroundJob (čistě aditivní
  sloupce) + nová job_outbox_events tabulka (transakční outbox) —
  broker/publish selhání už nikdy neztratí job.
Explicitní queue topologie (embedding/document_processing/ai_generation/
  media/notifications/maintenance) + nový dedikovaný embedding_worker
  a maintenance_worker kontejner (docker-compose.yml i .prod.yml),
  bez Docker socketu, bez nového portu.
Explicitní lifecycle embedding provideru + integrity probe navržený přímo
  z reálného incidentu s meta-tensor na BGE-M3 (zdokumentováno v
  PROJECT_PROGRESS.md) + ohraničená self-healing politika (max 3 pokusy,
  max 1 vyžádaný restart embedding-worker kontejneru, nikdy nekonečná
  smyčka, žádný Docker socket/API v aplikačním kódu).
Stale-job recovery, backpressure (429/503) per-user/per-profile/globálně,
  nové bezpečné veřejné chybové kategorie.
Oba zbývající synchronní HTTP endpointy (index/retry-indexing) nyní vrací
  202 a nikdy neinstancují encoder v FastAPI procesu.
38 nových testů (fake-safe) + fake-safe load-test harness (smoke profil
  skutečně spuštěn lokálně: 15 uživatelů, 0 duplicit/kontaminace/úniků).
```

Vědomě mimo rozsah / zdokumentováno jako omezení (viz `PROJECT_PROGRESS.md` pro plný seznam): existující `celery_worker` kontejner zatím není omezen na vlastní frontu (v tomto dev compose bez `-Q` flag proto ze zásady odebírá i `embedding` frontu); frontend polling/backoff pro tyto dvě nově-asynchronní akce nebyl dodělán (jen "nikdy netvrdit zaindexováno předčasně" bylo opraveno); `scale`/`stress` load-test profily nebyly spuštěny (chybí izolované staging prostředí).

Task 65.9 se **považuje za kompletně dokončený** v rozsahu definovaném zadáním. Žádná sekce této roadmapy nebyla přepsána; toto je jediná nová sekce, kterou tento task přidal.

Další doporučený task: omezit `celery_worker` na jeho vlastní (ne-embedding) fronty nyní, když `embedding_worker`/`maintenance_worker` existují jako zamýšlení jediní konzumenti frenty `embedding`/`maintenance`. (Poznámka k dokumentační uzávěrce Task 65.9D, 2026-07-25: v době psaní této sekce byla práce Task 65.7 stále necommitnutá; mezitím byla dokončena a commitnuta jako **Task 65.7C** (`aabdd89`), viz sekce 25 níže — tento bod je tedy vyřešen. Formálně dalším číslovaným taskem je **Task 65.9.1 — Queue Isolation, Async Status Polling, and Production Scale Verification Closure**, viz sekce 26.)

## 25. Task 65.7C status (2026-07-24) — dokončení autentizované spolehlivosti workspace, session/cookie architektury a oprava skryté regrese v povinném upřesnění

Task 65.7C dokončil zbývající, dosud necommitnutou backendovou polovinu Task 65.7 (browser-session cookie autentizace, Redis-backed aktivní chat session s resume, AI Biograf resume, oprava zaseknutých kandidátů) a zároveň opravil skutečnou architektonickou regresi, kterou tato necommitnutá práce sama vnesla. Plný popis (traceability matice vůči této roadmapě, přesný root-cause, testy) je v `PROJECT_PROGRESS.md`, sekce "Task 65.7C Authenticated Workspace Reliability Closure".

Nalezený konflikt s touto roadmapou (bod 10 "Unverified memory candidate = cannot be used as factual evidence" a bod 5.2 bezpečného učení): necommitnutá verze Task 65.7 přidala funkci, která při KAŽDÉ nové odpovědi AI Biografa bezpodmínečně zrušila dosud nezodpovězená povinná upřesnění (`bypass_mandatory_clarifications_and_finalize`, volaná automaticky z `answer_question`) a rovnou označila kandidáta jako `ready_for_owner_review`. To přímo odporovalo již dříve touto roadmapou akceptovanému a Taskem 65.6 implementovanému mechanismu povinných upřesnění a rozbilo dva již commitnuté testy (`test_answering_childhood_question_creates_candidate_with_required_clarification`, `test_active_clarification_blocks_new_topic`). Oprava: automatické volání odstraněno z běžného toku odpovědí; funkce samotná zachována výhradně jako explicitní, věkově ohraničený (`asked_at` starší než konfigurovatelný práh, default 24 h) nástroj pro opravu skutečně zaseknutých kandidátů (`avatar_biographer/repair.py`), nikdy automaticky spouštěná.

Stručně:

```text
Browser-session cookie (Redis-backed, HttpOnly/SameSite=Lax, sliding TTL,
  additivní k existujícímu bearer JWT) - multi-replica bezpečné, žádný
  in-process stav.
Aktivní chat session: Postgres (chat_active_sessions, migrace 20260723_0026)
  jako zdroj pravdy, Redis jen jako rychlá obnovitelná cache s bezpečným
  fallbackem na Postgres při výpadku/expiraci.
AI Biograf resume endpoint - čistě čtecí kompozice existujících stavů.
Skutečná regrese nalezena a opravena: povinné upřesnění (Task 65.6) bylo
  necommitnutou verzí Tasku 65.7 tiše obcházeno pro každou novou odpověď -
  opraveno, ověřeno proti již existujícím commitnutým testům.
Dříve hlášené "české/ruské lokalizační selhání upřesnění" bylo ve
  skutečnosti kaskádovým důsledkem výše uvedené regrese, ne chybou v
  lokalizačním kódu (ten zůstal beze změny a je správný).
test_alembic.py: nahrazena křehká natvrdo daná revize za kontrolu
  jediné hlavy + explicitních hran řetězu (20260722_0025 -> 20260723_0026
  -> 20260724_0027).
12 testů v 10 souborech opraveno (cookie perzistuje napříč requesty ve
  sdíleném test klientovi stejně jako v prohlížeči - testy musely
  explicitně vyčistit cookies, aby simulovaly opravdu nulové přihlášení,
  produkční chování bylo od začátku správné).
Task 65.9 (38 testů async job platformy) ověřen nezměněný před i po zásahu.
```

Task 65.7C se **považuje za kompletně dokončený** v rozsahu definovaném zadáním. Žádná existující sekce této roadmapy nebyla přepsána; toto je jediná nová sekce, kterou tento task přidal. Známá omezení (pre-existující, nesouvisející selhání `test_rag_retrieval.py`/`test_embeddings.py` kvůli skutečnému `sentence_transformers` provideru namísto mocku pro konkrétní `model_code` hodnoty; jeden dávkově-only flake v `test_rag_chunks.py`) jsou zdokumentována v `PROJECT_PROGRESS.md` a nebyla touto úlohou způsobena ani opravena.

Další doporučený task: omezit `celery_worker` na jeho vlastní (ne-embedding) fronty (nezměněné doporučení z Tasku 65.9, tímto taskem nedotčeno). Formálně dalším číslovaným taskem je **Task 65.9.1 — Queue Isolation, Async Status Polling, and Production Scale Verification Closure**, viz sekce 26.

## 26. Task 65.9.1 — definice dalšího čísla tasku (2026-07-25, dokumentováno v rámci Task 65.9D, **neimplementováno**)

Task 65.9D (dokumentační uzávěrka Tasků 65.7C a 65.9) potvrdil oba implementační commity (`aabdd89` pro Task 65.7C, `d6d76ab` pro Task 65.9) přítomné lokálně i na `origin/staging/eternalworld-lukiora-20260715` a definuje zde formálně další task číslo podle skutečných, zdokumentovaných omezení Tasku 65.9 (sekce 24 výše). Tato sekce **pouze definuje** rozsah - žádná implementace neproběhla v rámci Tasku 65.9D.

**Task 65.9.1 — Queue Isolation, Async Status Polling, and Production Scale Verification Closure**

Rozsah (převzato beze změny ze zdokumentovaných omezení Tasku 65.9):

```text
1. Omezit obecný celery_worker kontejner jen na ne-embedding fronty
   (document_processing/ai_generation/media/notifications).
2. Zajistit, že jedině dedikovaný embedding_worker odebírá frontu embedding.
3. Dokončit frontend polling pro stavy: queued, processing,
   provider recovery, indexed, failed (pro obě nově-asynchronní akce
   z Tasku 65.9 - "Index memory" a retry-indexing).
4. Zapojit periodickou aktualizaci metrik async_queue_depth a
   async_oldest_job_age_seconds (gauge settery už existují, chybí
   pravidelný updater task).
5. Rozšířit backpressure na všechny existující "heavy" (text-přijímající)
   endpointy, ne jen na explicitní index/retry akce.
6. Ověřit chování API/session/job napříč více reálnými běžícími replikami
   (dosud jen code-review audit, ne živý multi-replica důkaz).
7. Spustit izolované scale testy na zdokumentované infrastruktuře
   (load-smoke harness z Tasku 65.9 už existuje, scale/stress profily
   dosud nebyly spuštěny - chybělo izolované staging prostředí).
8. Spustit řízené stress testy.
9. Vyprodukovat evidence-based zjištění o produkční kapacitě (žádné tvrzení
   o konkrétním počtu současných uživatelů bez skutečného měření).
```

Toto číslo (65.9.1) nekoliduje se žádným existujícím taskem této roadmapy (ověřeno - žádná dřívější sekce ani `PROJECT_PROGRESS.md` záznam toto číslo nepoužívá). Task 65.9.1 **nebyl v rámci Tasku 65.9D implementován** - je zde zdokumentován výhradně jako příští doporučená položka roadmapy.
