from fastapi import APIRouter

from app.core.metrics import build_metrics_response


router = APIRouter(tags=["metrics"])


@router.get("/metrics")
def metrics() -> object:
    return build_metrics_response()
