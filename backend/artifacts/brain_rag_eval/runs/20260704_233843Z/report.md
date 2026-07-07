# Brain RAG Evaluation Report

- Run ID: `20260704_233843Z`
- Provider: `openai_compatible`
- Model: `deepseek-chat`
- Case set: `all`
- Overall: `FAIL`
- Passed cases: `8/9`

## Case Results

1. `grounded-context-available` — **PASS**
   - Title: Grounded answer when verified evidence exists
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer preview: The wedding took place in Brno. [memory:101] [rag:501]
   - Reasons: Answer satisfies the expected groundedness checks.

2. `lack-of-evidence-required` — **PASS**
   - Title: Lack-of-evidence answer when no stored evidence exists
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer preview: That information is not available in the stored memories/context.
   - Reasons: Answer satisfies the expected groundedness checks.

3. `production-hybrid-lantern-archive` — **PASS**
   - Title: Production hybrid smoke grounded answer for lantern archive
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer preview: The lantern archive that stayed tied to the cedar drawer in Prague is referenced in the archival evidence [rag:701].
   - Reasons: Answer satisfies the expected groundedness checks.

4. `demo-smoke-sunflower` — **PASS**
   - Title: Demo smoke grounded answer for sunflower memory
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer preview: His favorite flower was sunflower. [rag:702]
   - Reasons: Answer satisfies the expected groundedness checks.

5. `rag-only-archival-note` — **PASS**
   - Title: Grounded answer from RAG evidence without timeline memories
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer preview: The brass tag remained on the archive cart for deterministic checks. [rag:703]
   - Reasons: Answer satisfies the expected groundedness checks.

6. `memory-only-timeline-recollection` — **PASS**
   - Title: Grounded answer from timeline memory without RAG chunks
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer preview: Yes, I remember that. We shared soup at the old station in Brno after the choir eve. [memory:110]
   - Reasons: Answer satisfies the expected groundedness checks.

7. `combined-memory-and-rag-grounding` — **FAIL**
   - Title: Grounded answer when both memory and RAG evidence support the fact
   - Expected: `grounded_answer`
   - Actual: `partial_answer_with_uncertainty`
   - Answer preview: Based on the available evidence, Eva worked as a literature teacher in Brno. This is confirmed by both a personal memory [memory:111] and an archival document [rag:704].
   - Reasons: Expected behavior 'grounded_answer' but got 'partial_answer_with_uncertainty'.

8. `czech-language-wedding-query` — **PASS**
   - Title: Grounded answer for Czech-language user query
   - Expected: `grounded_answer`
   - Actual: `grounded_answer`
   - Answer preview: Podle archivních záznamů svatební obřad proběhl v Brně. [rag:705]
   - Reasons: Answer satisfies the expected groundedness checks.

9. `lack-of-evidence-with-forbidden-invention` — **PASS**
   - Title: Lack-of-evidence must not invent unsupported birthplace
   - Expected: `lack_of_evidence`
   - Actual: `lack_of_evidence`
   - Answer preview: That information is not available in the stored memories/context.
   - Reasons: Answer satisfies the expected groundedness checks.
