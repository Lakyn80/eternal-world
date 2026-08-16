"""Shared httpx.AsyncClient lifecycle for the Brain provider (Task 65.13.12).

One process-wide client is reused so keep-alive connections are not
discarded on every chat turn. Callers may still pass a per-request timeout
to ``client.post(...)``.
"""

from __future__ import annotations

import asyncio
import threading

import httpx

from app.core.config import settings

_async_client: httpx.AsyncClient | None = None
_async_lock: asyncio.Lock | None = None
_async_lock_init = threading.Lock()


def _get_async_lock() -> asyncio.Lock:
    global _async_lock
    if _async_lock is None:
        with _async_lock_init:
            if _async_lock is None:
                _async_lock = asyncio.Lock()
    return _async_lock


def build_brain_async_timeout(timeout_seconds: float | None = None) -> httpx.Timeout:
    """Preserve the existing overall timeout contract; bound connect separately."""

    total = float(timeout_seconds if timeout_seconds is not None else settings.ai_brain_timeout_seconds)
    connect = min(10.0, total)
    return httpx.Timeout(
        timeout=total,
        connect=connect,
        read=total,
        write=total,
        pool=total,
    )


def build_brain_async_limits() -> httpx.Limits:
    """Connection pool sized above the default Brain admission cap (8)."""

    return httpx.Limits(
        max_connections=32,
        max_keepalive_connections=16,
        keepalive_expiry=30.0,
    )


async def get_shared_brain_async_http_client(
    *,
    timeout_seconds: float | None = None,
) -> httpx.AsyncClient:
    """Return the process-wide AsyncClient, creating it on first use."""

    global _async_client
    async with _get_async_lock():
        if _async_client is None or _async_client.is_closed:
            _async_client = httpx.AsyncClient(
                timeout=build_brain_async_timeout(timeout_seconds),
                limits=build_brain_async_limits(),
            )
        return _async_client


async def aclose_shared_brain_async_http_client() -> None:
    """Close the shared client (tests / process shutdown)."""

    global _async_client
    async with _get_async_lock():
        client = _async_client
        _async_client = None
        if client is not None and not client.is_closed:
            await client.aclose()


def reset_shared_brain_async_http_client_for_tests() -> None:
    """Drop the shared client reference without awaiting close (tests only)."""

    global _async_client
    _async_client = None
