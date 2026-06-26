# BGE-M3 Full Hybrid Retrieval Design

## Current Status

- Current `bge_m3` runtime in this project is dense-only.
- The existing adapter uses `BAAI/bge-m3` through the local SentenceTransformers path.
- Current production-safe and fake-safe tests do not exercise sparse or multi-vector retrieval.
- The current dense-only adapter is useful for baseline comparison, but it is not equivalent to full BGE-M3 retrieval.

## Why Dense-Only Is Not Full BGE-M3

- Dense retrieval uses one dense vector per text item.
- Full BGE-M3 can also contribute sparse lexical signals.
- Full BGE-M3 can also contribute multi-vector or ColBERT-style token-level matching.
- Those extra signals change indexing layout, query execution, score fusion, and failure modes.
- A dense-only `bge_m3` score should therefore be treated as a partial implementation, not the final hybrid design.

## Planned Retrieval Modes

- `bge_m3_dense`
  - One dense vector per chunk.
  - Lowest implementation risk.
  - Matches current baseline behavior most closely.
- `bge_m3_dense_sparse`
  - Dense vector plus sparse lexical representation.
  - Requires dual-index or dual-field retrieval planning.
  - Improves precision on lexical anchor terms and distractor-heavy queries.
- `bge_m3_dense_sparse_multivector`
  - Dense vector plus sparse representation plus token-level multi-vector matching.
  - Highest complexity and resource usage.
  - Best future target when long-context and near-duplicate conflict handling matter.

## Retrieval Components

### Dense retrieval

- Store one dense embedding per chunk.
- Query path stays close to the current architecture.
- Supports direct comparison with `multilingual_e5_small`, `multilingual_e5_base`, and `multilingual_e5_large`.

### Sparse retrieval

- Add sparse lexical representations per chunk and query.
- Preserve exact-term evidence better for Czech, Russian, and distractor-heavy cases.
- Requires explicit sparse index design and score normalization.

### Multi-vector / ColBERT-style retrieval

- Store multiple vectors per chunk instead of a single dense vector.
- Enables token-level late interaction scoring.
- Raises storage, indexing, and query-time cost substantially.

## Qdrant Collection Implications

- Dense-only mode can keep the current single-vector collection strategy.
- Dense + sparse likely needs either:
  - one collection with multiple vector payload channels if supported cleanly by the runtime, or
  - coordinated dense and sparse collections with a merge layer.
- Dense + sparse + multi-vector likely needs separate collection conventions or an explicit retrieval mode suffix in collection names.
- Planned collection naming examples:
  - `eternal_world_rag_chunks__bge_m3__dense`
  - `eternal_world_rag_chunks__bge_m3__dense_sparse`
  - `eternal_world_rag_chunks__bge_m3__dense_sparse_multivector`

## Scoring and Merge Strategy

- Retrieve dense candidates first.
- Retrieve sparse candidates separately.
- For multi-vector mode, run late interaction scoring only on a narrowed candidate set.
- Normalize scores before merging because raw dense, sparse, and multi-vector scales are not directly comparable.
- Keep merge behavior deterministic and auditable in benchmark outputs.
- Persist per-mode diagnostics so future reports can show why one mode won.

## Main Risks

- Qdrant collection layout may need structural changes beyond current dense assumptions.
- Sparse and multi-vector scoring can hide bugs behind apparently good top-1 results.
- Storage growth and query latency can rise sharply in the full hybrid mode.
- Debugging becomes harder when dense, sparse, and late-interaction signals disagree.
- Fake-safe tests need dedicated abstractions so full hybrid logic can be validated without real model inference.

## Planned Task Breakdown

1. Add retrieval mode constants and benchmark planning metadata.
2. Add fake-safe config tests for dense, dense+sparse, and dense+sparse+multi-vector modes.
3. Add collection naming and validation helpers without executing real hybrid retrieval.
4. Add sparse result abstraction and score fusion tests.
5. Add multi-vector planning abstraction and candidate narrowing tests.
6. Run manual dense-only BGE-M3 benchmark batch first.
7. Run manual dense+sparse benchmark batch later.
8. Run dense+sparse+multi-vector benchmark only after earlier modes are stable.
