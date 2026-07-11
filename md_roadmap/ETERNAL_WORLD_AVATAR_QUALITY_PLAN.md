
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
