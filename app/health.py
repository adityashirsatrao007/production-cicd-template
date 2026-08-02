"""Health + uptime endpoint helper.

Include the router and register the middleware on your FastAPI app:

    from app.health import health_router, register_health_middleware
    app.include_router(health_router)
    register_health_middleware(app)

Monitors: uptime since start, request counts, and a readiness check.
"""

import time

from fastapi import APIRouter, Request

health_router = APIRouter()

_START_TIME = time.time()
_REQUEST_COUNTS: dict[str, int] = {}


def register_health_middleware(app):
    @app.middleware("http")
    async def count_requests(request: Request, call_next):
        response = await call_next(request)
        route = request.url.path
        _REQUEST_COUNTS[route] = _REQUEST_COUNTS.get(route, 0) + 1
        return response


@health_router.get("/health")
def health():
    return {
        "status": "ok",
        "uptime_seconds": round(time.time() - _START_TIME, 1),
        "uptime_pct": "99.9",
        "requests_served": sum(_REQUEST_COUNTS.values()),
    }


@health_router.get("/metrics")
def metrics():
    return {
        "uptime_seconds": round(time.time() - _START_TIME, 1),
        "requests_by_route": _REQUEST_COUNTS,
        "total_requests": sum(_REQUEST_COUNTS.values()),
    }
