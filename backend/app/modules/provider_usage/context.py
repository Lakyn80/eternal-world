from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any

from app.modules.provider_usage.enums import AiFeature, ExecutionSource


@dataclass(frozen=True)
class AiCallContext:
    """Everything needed to attribute one paid-provider-call-eligible
    operation to a durable ``AiAction``, without threading raw user/request
    objects through Brain/translation internals.

    Deliberately a plain, JSON-serializable dataclass (not a Pydantic model
    bound to ORM objects) so the *same* type can be:
    - passed in-process through a FastAPI request handler, or
    - serialized via ``to_task_kwargs``/``from_task_kwargs`` as plain Celery
      task arguments (never relying on process-local ``contextvars``, which
      do not cross the FastAPI-to-Celery process boundary).
    """

    feature: AiFeature
    execution_source: ExecutionSource
    trace_id: str | None = None
    requested_locale: str | None = None
    resolved_locale: str | None = None
    user_id: int | None = None
    memorial_id: int | None = None
    conversation_id: int | None = None
    message_id: int | None = None
    celery_task_id: str | None = None

    def to_task_kwargs(self) -> dict[str, Any]:
        """Flat, JSON-safe representation for passing through Celery task
        arguments (enum members serialize as their plain string value)."""

        return {
            "feature": self.feature.value,
            "execution_source": self.execution_source.value,
            "trace_id": self.trace_id,
            "requested_locale": self.requested_locale,
            "resolved_locale": self.resolved_locale,
            "user_id": self.user_id,
            "memorial_id": self.memorial_id,
            "conversation_id": self.conversation_id,
            "message_id": self.message_id,
            "celery_task_id": self.celery_task_id,
        }

    @classmethod
    def from_task_kwargs(cls, payload: dict[str, Any]) -> "AiCallContext":
        return cls(
            feature=AiFeature(payload["feature"]),
            execution_source=ExecutionSource(payload["execution_source"]),
            trace_id=payload.get("trace_id"),
            requested_locale=payload.get("requested_locale"),
            resolved_locale=payload.get("resolved_locale"),
            user_id=payload.get("user_id"),
            memorial_id=payload.get("memorial_id"),
            conversation_id=payload.get("conversation_id"),
            message_id=payload.get("message_id"),
            celery_task_id=payload.get("celery_task_id"),
        )

    def with_celery_task_id(self, celery_task_id: str) -> "AiCallContext":
        return replace(self, celery_task_id=celery_task_id, execution_source=ExecutionSource.CELERY)


def development_test_context(*, trace_id: str | None = None) -> AiCallContext:
    """Fallback context for internal/dev/eval call sites that have no real
    user-facing identity (RAG evaluation scripts, ad-hoc diagnostics). Never
    used for real authenticated or demo user traffic - those always build an
    explicit ``AiCallContext`` with their real feature/execution_source."""

    return AiCallContext(
        feature=AiFeature.DEVELOPMENT_TEST,
        execution_source=ExecutionSource.INTERNAL,
        trace_id=trace_id,
    )
