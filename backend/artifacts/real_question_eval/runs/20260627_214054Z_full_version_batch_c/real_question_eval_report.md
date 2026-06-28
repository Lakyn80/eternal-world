# Real Question Evaluation Report

## Client Summary
- Batch label: `Batch C`
- Source dataset: deterministic fictional eval corpus
- Real client/user data: no
- Purpose: retrieval quality testing
- Models compared:
  - `multilingual_e5_base`
  - `jina_embeddings_v3`
- Baseline provider: `multilingual_e5_base`
- Newly evaluated provider: `jina_embeddings_v3`
- Comparison scope: Only multilingual_e5_base and jina_embeddings_v3 are allowed in the final Batch C comparison.
- Weaker historical providers intentionally excluded: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2, multilingual_e5_large, qwen3_embedding_0_6b, qwen3_embedding_4b, qwen3_embedding_8b
- Winner: `none`
- Recommendation: Batch C does not show a clear enough win over the baseline `multilingual_e5_base`; keep `multilingual_e5_base` as the production recommendation.

## Technical Summary
- Run type: `full_version_batch_c`
- Execution mode: `full_version_batch_c_real_eval`
- Benchmark status: `failed`
- Used fake models: `false`
- Historical current winner before Batch C: `multilingual_e5_base`
- Any new provider beat baseline/current winner: `none`
- Timestamp: 2026-06-27T21:40:54.116214+00:00
- Incomplete reason: Jina Batch C did not complete after successful Hugging Face asset prefetch because the backend process was killed during repeated jina_embeddings_v3 local model loads, consistent with container memory exhaustion. No completed comparison result was produced.

## Dataset Questions Used

## Baseline Provider
- `multilingual_e5_base`

## Newly Evaluated Provider
- `jina_embeddings_v3`

## Per-Question Result Comparison
## Aggregate Metrics

## Winner
- Batch C winner: `none`

## Recommendation
- Recommended active model: `none`
- Production recommendation: Batch C does not show a clear enough win over the baseline `multilingual_e5_base`; keep `multilingual_e5_base` as the production recommendation.

## Safety Notes
- Only newly run provider: `jina_embeddings_v3`
- Baseline reused from existing artifact: `multilingual_e5_base`
- Excluded weaker historical providers: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2, multilingual_e5_large, qwen3_embedding_0_6b, qwen3_embedding_4b, qwen3_embedding_8b
- Latest real artifacts overwritten: `false`
- Latest fake artifacts overwritten: `false`
- Latest incremental artifacts overwritten: `false`
- Latest full-version Batch A artifacts overwritten: `false`
- Qwen3 0.6B was skipped as attempted/not completed and is not part of Batch C.
- Hugging Face asset prefetch succeeded and removed the earlier network/cache blocker.
- The post-prefetch offline rerun still ended with the local backend process being killed during repeated jina_embeddings_v3 loads, so no completed Batch C comparison was produced.

## Artifact Files
- Latest Markdown: `/app/artifacts/real_question_eval/latest_full_version_batch_c/real_question_eval_report.md`
- Latest JSON: `/app/artifacts/real_question_eval/latest_full_version_batch_c/real_question_eval_result.json`
- Archived Markdown: `/app/artifacts/real_question_eval/runs/20260627_214054Z_full_version_batch_c/real_question_eval_report.md`
- Archived JSON: `/app/artifacts/real_question_eval/runs/20260627_214054Z_full_version_batch_c/real_question_eval_result.json`

## Developer Details
