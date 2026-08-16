"""Bounded threadpool bridge for transitional sync I/O (Task 65.13.12).

Starlette/AnyIO ``run_in_threadpool`` can deadlock under sync ``TestClient``
when an async endpoint nests multiple bridge calls. A dedicated bounded
executor keeps Brain awaits on the event loop while sync Redis/DB/RAG work
runs off-loop without sharing that framework pool.
"""

from __future__ import annotations

import asyncio
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from time import perf_counter
from typing import TypeVar

from app.core.metrics import observe_chat_threadpool_bridge

T = TypeVar("T")

#: Bounded — never create an unbounded pool (Task 65.13.12 Part V).
_CHAT_BRIDGE_EXECUTOR = ThreadPoolExecutor(
    max_workers=32,
    thread_name_prefix="ew-chat-bridge",
)


async def run_sync_in_chat_bridge(
    func: Callable[..., T],
    /,
    *args,
    operation: str = "other",
    **kwargs,
) -> T:
    """Run blocking sync work in the chat bridge executor and await the result."""

    loop = asyncio.get_running_loop()
    started = perf_counter()
    call = partial(func, *args, **kwargs) if kwargs else partial(func, *args)
    try:
        return await loop.run_in_executor(_CHAT_BRIDGE_EXECUTOR, call)
    finally:
        observe_chat_threadpool_bridge(
            operation=operation,
            duration_seconds=perf_counter() - started,
        )
