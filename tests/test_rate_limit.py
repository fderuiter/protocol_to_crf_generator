from importlib import reload

from fastapi.testclient import TestClient

import protocol_to_crf_generator.api.main as main
import protocol_to_crf_generator.api.rate_limit as rate_limit


def test_rate_limit_exceeded(monkeypatch):
    monkeypatch.setenv("RATE_LIMIT", "2/minute")
    reload(rate_limit)
    reload(main)
    client = TestClient(main.app)
    assert client.get("/health").status_code == 200
    assert client.get("/health").status_code == 200
    response = client.get("/health")
    assert response.status_code == 429


