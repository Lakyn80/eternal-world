# Eternal World — Modular Autobiographical Memory Engine

Act as a **Senior Enterprise AI Architect, Retrieval Engineer and Backend Engineer**.

This document is the long-term implementation roadmap for evolving Eternal World from its current MVP RAG architecture into a robust autobiographical memory engine.

The existing MVP must remain deployable and usable throughout the migration.

Do not redesign or replace working systems unnecessarily.

The system must evolve incrementally.

---

# 0. Core engineering principle

The current MVP uses:

```text
memory / biography / contribution
→ embedding
→ vector database
→ retrieval
→ LLM grounded answer
```

This remains the foundation.

Do **not** replace embedding-based RAG.

The target architecture will progressively become:

```text
                         USER QUERY
                              │
                              ▼
                      Query Understanding
                              │
             ┌────────────────┼────────────────┐
             │                │                │
             ▼                ▼                ▼
        Dense Vector       Lexical         Metadata
         Retrieval         Retrieval        Filtering
             │                │                │
             └────────────────┼────────────────┘
                              │
                              ▼
                      Candidate Fusion
                              │
                              ▼
                           Reranker
                              │
                              ▼
                 Temporal / Graph Expansion
                              │
                              ▼
                     Evidence Selection
                              │
                              ▼
                             LLM
                              │
                              ▼
                     Grounded Response
```

Later:

```text
Autobiographical Memory Engine
=
Dense Retrieval
+ Sparse Retrieval
+ Metadata
+ Timeline
+ Entity Relationships
+ Reranking
+ Evidence Grounding
```

---

# 1. Non-negotiable architectural rules

## 1.1 Existing MVP stays functional

At every phase:

```text
existing vector RAG must continue working
```

A new module must never require completing all future modules.

Every phase must be independently deployable.

---

## 1.2 No big-bang rewrite

Never implement several architectural layers simultaneously.

Every module follows:

```text
AUDIT
↓
DESIGN
↓
IMPLEMENT
↓
UNIT TESTS
↓
INTEGRATION TESTS
↓
QUALITY / REGRESSION TEST
↓
REPORT
↓
COMMIT
```

Do not proceed automatically to the next module.

---

## 1.3 Backward compatibility

Existing:

* memories
* contributions
* biographies
* embeddings
* Qdrant collections
* approved content
* source attribution
* memorial memberships

must remain compatible.

Avoid destructive migrations.

If reindexing is required:

```text
old index remains usable
until new index is verified
```

---

## 1.4 Evidence-first generation

The AI must never invent autobiographical facts.

Target behavior:

```text
sufficient evidence
→ answer from memory sources

insufficient evidence
→ explicitly say that the information is not recorded
```

Hallucination suppression is more important than conversational fluency.

---

## 1.5 Provenance must survive every transformation

Every retrievable unit must remain traceable to an original source.

Eventually every result should be able to resolve:

```text
retrieved chunk
→ canonical memory
→ contribution / biography / source
→ author
→ source date
→ approval state
```

Never create knowledge that loses provenance.

---

# 2. Current MVP baseline — freeze before evolution

Before building the advanced memory system, establish the current system as the benchmark.

Do not modify retrieval yet.

## Module M0 — Retrieval Baseline

### Goal

Measure exactly how the existing embedding RAG performs.

### Audit

Document:

* embedding model
* embedding dimensions
* Qdrant collections
* chunking strategy
* chunk size
* chunk overlap
* metadata stored in Qdrant
* retrieval `top_k`
* similarity metric
* score thresholds
* reranking if any
* prompt structure
* source attribution
* indexing pipeline
* reindex/retry behavior

### Create a golden evaluation dataset

Prepare representative questions:

```text
direct factual
semantic paraphrase
name lookup
exact date
location
relationship
timeline
multi-memory
ambiguous
unanswerable
contradictory sources
```

Examples:

```text
What was Martin's first job?

How did Martin describe his father?

Who was with Martin in Cornwall?

What happened in 1989?

What happened between his marriage and Helen's birth?

Did Martin ever live in France?
```

Include expected source memories.

### Metrics

Measure:

```text
Recall@K
MRR
source precision
answer groundedness
answer correctness
unanswerable detection
latency
```

This baseline becomes the reference for every future retrieval change.

### Stop condition

Do not proceed until the baseline can be reproduced.

Do not optimize yet.

---

# 3. Module M1 — Structured Memory Metadata

This is the first enhancement after MVP.

## Goal

Give every memory structured autobiographical metadata without replacing embeddings.

Target structure:

```text
memory_id
profile_id

event_date
event_date_start
event_date_end
date_precision

location
location_normalized

people[]
relationships[]

topics[]
event_type

source_type
source_author
source_id

privacy_scope
approval_status

confidence
language

created_at
updated_at
```

### Phase M1.1 — Schema audit

Determine which fields already exist.

Classify fields as:

```text
existing
partially represented
missing
derivable
```

Do not change schema yet.

### Phase M1.2 — Metadata schema

Design the smallest normalized representation.

Avoid premature ontology complexity.

Dates must support:

```text
exact date
month
year
approximate date
date range
unknown
```

### Phase M1.3 — Extraction pipeline

Metadata extraction should prefer deterministic parsing first:

```text
dates
known user names
existing relationship records
known locations
```

Use LLM extraction only where deterministic parsing is insufficient.

LLM output must use strict structured validation.

### Phase M1.4 — Index metadata

Add selected metadata to Qdrant payloads.

Do not rebuild all retrieval logic yet.

### Phase M1.5 — Validation

Test extraction against manually labelled memories.

Required metrics:

```text
date extraction accuracy
person extraction precision
location extraction precision
relationship precision
```

### Stop

Do not proceed to hybrid retrieval automatically.

---

# 4. Module M2 — Hybrid Retrieval

Current dense embeddings remain.

Add lexical retrieval.

Target:

```text
Dense search
+
Sparse / BM25 search
```

## Why

Dense retrieval is strong for semantic meaning.

Sparse retrieval is strong for:

```text
names
dates
numbers
places
exact phrases
rare terms
```

---

## Phase M2.1 — Lexical engine audit

Determine the smallest suitable implementation based on current infrastructure.

Evaluate existing PostgreSQL full-text capabilities before adding another infrastructure service.

Possible architectures:

```text
PostgreSQL FTS
Qdrant sparse vectors
OpenSearch / Elasticsearch
```

Prefer the smallest operational footprint that meets the requirements.

Do not introduce Elasticsearch solely because it is common.

---

## Phase M2.2 — Sparse indexing

Create sparse searchable representation for approved canonical memories.

Index only content eligible for AI retrieval.

Preserve provenance.

---

## Phase M2.3 — Parallel retrieval

For one query run:

```text
dense search
sparse search
```

independently.

Do not yet change generation.

Log both candidate sets.

---

## Phase M2.4 — Candidate fusion

Implement deterministic candidate fusion.

Evaluate:

```text
Reciprocal Rank Fusion
weighted score fusion
```

Start with Reciprocal Rank Fusion unless evaluation evidence favors another approach.

Avoid arbitrary magic coefficients.

---

## Phase M2.5 — A/B evaluation

Compare:

```text
dense-only
vs
hybrid
```

against M0 golden dataset.

Hybrid retrieval should only replace dense-only as default if it produces measurable improvement without unacceptable latency.

### Stop

Commit separately.

Do not proceed to reranking.

---

# 5. Module M3 — Reranking

## Goal

Improve relevance after initial retrieval.

Architecture:

```text
dense top K
+
sparse top K
↓
fusion
↓
20–50 candidates
↓
reranker
↓
best 5–10
```

---

## Phase M3.1 — Benchmark candidates

Evaluate appropriate rerankers.

Potential categories:

```text
cross-encoder
BGE reranker
LLM reranking
provider reranking API
```

Prefer self-hostable deterministic reranking where quality is sufficient.

Measure:

```text
quality
latency
VRAM/RAM
cost
```

---

## Phase M3.2 — Reranking abstraction

Create an interface such as:

```text
rerank(query, candidates)
```

Generation code must not know which reranker implementation is used.

---

## Phase M3.3 — Evaluation

Compare:

```text
hybrid without rerank
vs
hybrid + rerank
```

Measure:

```text
MRR
Recall@5
source relevance
latency
```

No rollout unless quality improves measurably.

---

# 6. Module M4 — Query Understanding

Do not immediately send every question directly into the same retriever.

Introduce query classification.

Target categories:

```text
semantic_fact
exact_lookup
person_query
relationship_query
timeline_query
date_range_query
multi_hop_query
summary_query
unanswerable_or_external
```

---

## Phase M4.1 — Deterministic routing first

Use obvious rules where possible.

Examples:

```text
year/date detected
→ temporal filter candidate

known person
→ person metadata

exact quoted phrase
→ lexical emphasis
```

---

## Phase M4.2 — LLM query planner

Only after deterministic routing.

Structured output:

```json
{
  "query_type": "...",
  "people": [],
  "date_range": null,
  "locations": [],
  "topics": [],
  "search_query": "..."
}
```

Validate using Pydantic or equivalent strict schema.

Never allow the planner to bypass access controls.

---

# 7. Module M5 — Temporal Memory Engine

This is a major Eternal World differentiator.

A human life is chronological.

## Goal

Create first-class support for:

```text
events
dates
date ranges
before/after relationships
life periods
timeline queries
```

Target examples:

```text
What happened in 1989?

What happened after Martin married Margaret?

What happened between 1972 and 1975?

What did Martin do before moving to Manchester?

Which memories are from the 1990s?
```

---

## Phase M5.1 — Date normalization

Normalize dates into machine-queryable representation.

Never discard original text representation.

---

## Phase M5.2 — Timeline retrieval

Support:

```text
before
after
between
during decade
nearest previous event
nearest following event
```

---

## Phase M5.3 — Timeline UI

Only after backend retrieval works.

Timeline should remain based on approved evidence.

AI must never invent missing years to fill visual gaps.

---

# 8. Module M6 — Entity Resolution

Before building a graph, solve entity identity.

Example problem:

```text
Mum
Mother
Margaret
Margaret Smith
his wife
Grandma
```

may refer to the same person depending on context.

## Phase M6.1

Create explicit person/entity registry per memorial.

## Phase M6.2

Map mentions to known entities.

Use:

```text
deterministic IDs
aliases
relationship context
```

LLM may propose mappings but must not silently merge uncertain identities.

## Phase M6.3

Introduce confidence and review for ambiguous entity merges.

Do not build graph traversal yet.

---

# 9. Module M7 — Relationship Graph

Only after entity resolution is reliable.

Graph concepts:

```text
Person
Event
Location
Memory
Organization
Object
```

Relations:

```text
parent_of
child_of
married_to
friend_of
worked_at
lived_in
visited
attended
participant_in
occurred_at
occurred_on
mentioned_in
source_of
```

---

## Phase M7.1 — Graph representation

First evaluate whether relational PostgreSQL tables are sufficient.

Do not introduce Neo4j solely because this is called a graph.

Start with normalized edge tables if appropriate:

```text
entity_nodes
entity_edges
```

Only introduce a dedicated graph database if query complexity requires it.

---

## Phase M7.2 — Graph extraction

Create relationships only from approved sources.

Each edge requires provenance:

```text
edge
→ source memory
```

No unsupported inferred family facts should become canonical.

---

## Phase M7.3 — Graph retrieval

Support questions such as:

```text
Who was related to Martin?

Who was present at the Cornwall trip?

How was Helen related to Margaret?
```

---

# 10. Module M8 — Graph + Vector Retrieval

Do not replace embeddings.

Combine:

```text
vector candidate
+
metadata
+
graph neighbors
```

Example:

```text
query: Who was with Martin in Cornwall?

vector retrieval
→ Cornwall memory

entity extraction
→ Martin
→ Cornwall

graph expansion
→ event participants

evidence retrieval
→ participant source memories
```

Only source-backed graph information may reach the LLM.

---

# 11. Module M9 — Multi-Hop Autobiographical Reasoning

Examples:

```text
Who became part of the family after Martin's marriage but before his first grandchild?

Which places did Martin live in before moving to Manchester?

Which family members appear in memories from both the 1980s and 1990s?
```

Architecture:

```text
query planner
↓
retrieval step 1
↓
intermediate entities/events
↓
retrieval step 2
↓
evidence merge
↓
answer
```

Hard maximum hop count required.

Avoid uncontrolled autonomous agent loops.

Start with:

```text
max_hops = 2
```

Expand only if benchmarks justify it.

---

# 12. Module M10 — Contradictory Memories

Humans may remember the same event differently.

Do not overwrite disagreement.

Example:

```text
Helen:
"The trip happened in June."

Margaret:
"It was August."
```

The system should preserve both.

Target answer:

```text
Helen remembered it as June, while Margaret's account places it in August.
```

Never silently select one as truth unless authoritative metadata exists.

Introduce:

```text
source identity
source confidence
conflict group
```

---

# 13. Module M11 — Memory Confidence

Introduce retrieval confidence separate from vector similarity.

Possible factors:

```text
retrieval score
reranker score
source approval
source directness
number of corroborating memories
entity confidence
temporal consistency
```

Do not collapse these into an unexplained magic score.

Keep components inspectable.

---

# 14. Module M12 — Grounded Answer Engine

The final answer generator receives structured evidence.

Conceptually:

```text
Question

Evidence:
1. memory_id
   source
   author
   date
   text

2. memory_id
   ...

Relationships:
...

Timeline:
...
```

LLM instruction:

```text
Answer only from supplied evidence.

Do not invent missing autobiographical facts.

If evidence is insufficient, explicitly state that the information is not recorded.

If sources disagree, describe the disagreement.

Separate direct evidence from reasonable synthesis.
```

---

# 15. Module M13 — Source Citations in Product UI

Every generated statement should be inspectable.

UI concept:

```text
Martin started work as a compositor in 1966.

Sources:
• First job — recorded by Martin
• Biography, chapter 2
```

User should be able to open the underlying memory.

This is especially important for memorial trust.

---

# 16. Module M14 — Evaluation Platform

Do not rely on manual impressions.

Create permanent retrieval regression tests.

Dataset structure:

```text
question
expected_memory_ids
expected_entities
expected_answer_facts
must_not_contain
answerable
```

Run automatically after retrieval changes.

Metrics:

```text
Recall@1
Recall@5
Recall@10

MRR

answer groundedness
citation correctness
hallucination rate

latency p50
latency p95
```

Every major retrieval change must show:

```text
before
vs
after
```

---

# 17. Module M15 — Retrieval Observability

Add structured traces.

For each query retain operational telemetry such as:

```text
query type
filters
dense candidates
sparse candidates
fusion ranking
reranker output
graph expansion
final evidence IDs
latency per stage
```

Do not log private memory contents unnecessarily.

Prefer IDs and diagnostic scores.

---

# 18. Module M16 — Cost Control

Every AI-powered retrieval/generation operation must be measurable.

Track:

```text
embedding calls
reranker calls
LLM tokens
OCR
voice
future avatar usage
```

No production AI operation should be economically invisible.

Use deterministic processing where possible before invoking LLMs.

---

# 19. Module M17 — Privacy and Access Control

Every retrieval path must enforce memorial membership before data retrieval.

This includes future:

```text
dense retrieval
sparse retrieval
timeline retrieval
graph traversal
reranking
```

Never retrieve globally and filter private content only afterward.

Tenant/profile isolation must be part of the query boundary.

Test against cross-memorial data leakage.

---

# 20. Module M18 — Delete and Reindex Correctness

Because this is personal memorial data, deletion must propagate.

Target:

```text
delete / revoke memory
↓
remove canonical searchable state
↓
remove vector
↓
remove sparse index
↓
remove graph edges derived solely from source
↓
invalidate caches
```

Restore/reapproval must rebuild all necessary derived representations.

Use background jobs with explicit states.

---

# 21. Module M19 — Versioned Knowledge

Do not destructively overwrite approved knowledge.

Eventually use:

```text
source version
canonical memory version
index version
graph extraction version
embedding model version
```

This allows safe reprocessing when embedding/extraction models change.

---

# 22. Module M20 — Model Migration Strategy

Embedding models will improve.

Never tie database identity to one embedding model.

Support:

```text
embedding_model
embedding_version
index_version
```

Future migration:

```text
old Qdrant collection
+
new collection

dual validation
↓
switch alias
↓
retire old collection later
```

No downtime required.

---

# 23. Recommended implementation order

Do NOT skip dependencies.

Implement in this order:

```text
M0  Baseline evaluation

M1  Structured metadata

M2  Hybrid dense + sparse retrieval

M3  Reranking

M4  Query understanding

M5  Temporal memory

M6  Entity resolution

M7  Relationship graph

M8  Graph + vector retrieval

M9  Multi-hop reasoning

M10 Contradiction handling

M11 Confidence model

M12 Grounded answer engine

M13 Source citations

M14 Permanent evaluation framework

M15 Observability

M16 Cost accounting

M17 Retrieval security hardening

M18 Delete/reindex consistency

M19 Versioned knowledge

M20 Embedding/index migration
```

Some cross-cutting modules such as security/evaluation/observability may be pulled earlier if existing architecture requires them, but do not use that as justification for a large rewrite.

---

# 24. Mandatory workflow for EVERY module

When implementing any module from this roadmap, follow exactly these steps.

## STEP A — Audit only

Inspect current code.

Return:

```text
existing architecture
reusable components
gaps
risks
DB impact
API impact
FE impact
migration requirements
test impact
```

Do not implement.

---

## STEP B — Architecture decision

Propose the smallest compatible implementation.

Explicitly state:

```text
what changes
what stays unchanged
data flow
transaction boundaries
failure modes
fallback behavior
```

Do not implement until the module scope is clear.

---

## STEP C — Backend foundation

Implement only backend/domain/data changes.

Run focused tests.

Stop if tests fail.

---

## STEP D — Retrieval/indexing layer

Implement retrieval/indexing changes independently.

Do not modify generation logic unless required by this module.

---

## STEP E — Frontend

Only if this module requires visible UI changes.

Do not redesign unrelated UI.

---

## STEP F — Integration

Connect the new module to the current RAG pipeline.

Maintain a fallback path to the previous retrieval implementation where feasible.

---

## STEP G — Evaluation

Run the golden dataset.

Compare:

```text
before
after
```

No architecture change should be considered successful merely because tests compile.

---

## STEP H — Regression tests

Run relevant:

```text
unit
integration
retrieval
authorization
indexing
frontend
build
```

---

## STEP I — Final report

Return:

```text
1. architecture before
2. architecture after
3. files changed
4. DB migrations
5. API changes
6. retrieval changes
7. tests
8. benchmark change
9. latency change
10. known limitations
11. rollback strategy
12. next recommended module
```

---

## STEP J — STOP

Do not automatically:

```text
commit
push
deploy
start next module
```

Wait for explicit instruction.

---

# 25. Definition of done

The future Eternal World memory engine is successful when it can reliably answer:

### Semantic

```text
How did Martin feel about his first job?
```

### Exact

```text
What happened on 14 June 1989?
```

### Temporal

```text
What happened after Martin's wedding?
```

### Relationship

```text
Who was Helen's grandmother?
```

### Multi-hop

```text
Which people Martin worked with later appeared in family memories?
```

### Contradictory evidence

```text
When did the Cornwall trip happen?
```

while being able to respond:

```text
The available memories disagree.
```

### Unknown

```text
What was Martin's favorite restaurant in Paris?
```

when there is no source:

```text
I don't have a recorded memory that answers that.
```

The final objective is not simply:

```text
a chatbot with embeddings
```

but:

```text
a source-grounded,
chronological,
relationship-aware,
auditable
autobiographical memory engine.
```

---

# 26. MVP rule

The existing embedding RAG is sufficient for the initial MVP.

Do not delay MVP launch to complete this roadmap.

The roadmap is intentionally incremental.

Each module must improve the live system independently and measurably.

Launch first.

Measure real usage.

Then evolve the memory engine module by module.
