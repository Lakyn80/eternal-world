from redis import Redis

from app.core.config import settings


def get_redis_client() -> Redis:
    # Short connect timeout so Redis DNS/connect failures fail fast (CI without
    # a Redis hostname, local misconfig) instead of hanging login/request paths.
    return Redis.from_url(
        settings.redis_url,
        decode_responses=True,
        socket_connect_timeout=2,
    )
