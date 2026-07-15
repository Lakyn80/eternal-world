from __future__ import annotations

import json
import sys

from app.db.session import SessionLocal
from app.modules.rag_evaluation.brain_eval_e2e_bootstrap import ensure_family_avatar_ru_e2e_bootstrap


def main() -> int:
    db = SessionLocal()
    try:
        result = ensure_family_avatar_ru_e2e_bootstrap(db)
    finally:
        db.close()

    print(
        json.dumps(
            {
                "user_id": result.user_id,
                "profile_id": result.profile_id,
                "source_id": result.source_id,
                "model_code": result.model_code,
                "collection_name": result.collection_name,
                "retrieval_mode": result.retrieval_mode,
                "top_k": result.top_k,
                "collection_rebuilt": result.collection_rebuilt,
                "memory_count": len(result.memory_ids_by_fact_id),
                "chunk_count": len(result.chunk_ids_by_fact_id),
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
