from __future__ import annotations

import os
from fastapi import FastAPI
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
from slowapi.util import get_remote_address

DEFAULT_LIMIT = os.getenv("RATE_LIMIT", "5/minute")


def setup_rate_limiter(app: FastAPI) -> Limiter:
    """Configure rate limiting on the given FastAPI application."""

    limiter = Limiter(key_func=get_remote_address, default_limits=[DEFAULT_LIMIT])
    app.state.limiter = limiter
    app.add_exception_handler(
        RateLimitExceeded, _rate_limit_exceeded_handler  # type: ignore[arg-type]
    )
    app.add_middleware(SlowAPIMiddleware)
    return limiter


__all__ = ["setup_rate_limiter", "DEFAULT_LIMIT"]
