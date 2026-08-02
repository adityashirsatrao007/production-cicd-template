from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.health import health_router, register_health_middleware

app = FastAPI()
app.include_router(health_router)
register_health_middleware(app)

client = TestClient(app)


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    body = resp.json()
    assert body["status"] == "ok"
    assert body["uptime_seconds"] >= 0


def test_metrics_tracks_requests():
    client.get("/health")
    body = client.get("/metrics").json()
    assert body["total_requests"] >= 2
