# Real Question Evaluation Report

## Client Summary
- Batch label: `Batch B Attempted`
- Source dataset: deterministic fictional eval corpus
- Real client/user data: no
- Purpose: retrieval quality testing
- Models compared:
  - `multilingual_e5_base`
  - `qwen3_embedding_0_6b`
- Baseline provider: `multilingual_e5_base`
- Newly evaluated provider: `qwen3_embedding_0_6b`
- Comparison scope: Qwen3 0.6B was attempted but not completed; no final Batch B comparison or winner was produced.
- Weaker historical providers intentionally excluded: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2, multilingual_e5_large
- Winner: `none`
- Recommendation: Keep `multilingual_e5_base` as the production recommendation and skip Qwen for now in this environment.

## Technical Summary
- Run type: `full_version_batch_b_attempted`
- Execution mode: `full_version_batch_b_attempted`
- Benchmark status: `attempted_not_completed`
- Used fake models: `false`
- Historical current winner before Batch B Attempted: `multilingual_e5_base`
- Any new provider beat baseline/current winner: `none`
- Timestamp: unknown
- Incomplete reason: Qwen3 0.6B benchmark attempt was not completed in this local Docker runtime due to runtime instability and poor cost-benefit for continued debugging.

## Dataset Questions Used

## Baseline Provider
- `multilingual_e5_base`

## Newly Evaluated Provider
- `qwen3_embedding_0_6b`

## Per-Question Result Comparison
## Aggregate Metrics

## Winner
- Batch B Attempted winner: `none`

## Recommendation
- Recommended active model: `multilingual_e5_base`
- Production recommendation: Keep `multilingual_e5_base` as the production recommendation and skip Qwen for now in this environment.

## Safety Notes
- Only newly run provider: `qwen3_embedding_0_6b`
- Baseline reused from existing artifact: `multilingual_e5_base`
- Excluded weaker historical providers: multilingual_e5_small, bge_m3, paraphrase_multilingual_mpnet_base_v2, multilingual_e5_large
- Latest real artifacts overwritten: `false`
- Latest fake artifacts overwritten: `false`
- Latest incremental artifacts overwritten: `false`
- Latest full-version Batch A artifacts overwritten: `false`
- Qwen3 0.6B benchmark attempted but not completed in this environment.
- Recommendation: skip Qwen for now and reconsider on a cleaner Linux/WSL/GPU/stronger runtime.

## Artifact Files
- Latest Markdown: `artifacts\real_question_eval\latest_full_version_batch_b_attempted\real_question_eval_report.md`
- Latest JSON: `artifacts\real_question_eval\latest_full_version_batch_b_attempted\real_question_eval_result.json`
- Archived Markdown: `artifacts\real_question_eval\runs\20260627_143439Z_full_version_batch_b_attempted\real_question_eval_report.md`
- Archived JSON: `artifacts\real_question_eval\runs\20260627_143439Z_full_version_batch_b_attempted\real_question_eval_result.json`

## Developer Details
