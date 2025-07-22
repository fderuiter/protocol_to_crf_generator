from fastapi.testclient import TestClient

from protocol_to_crf_generator.api.main import app


def test_map_endpoint_returns_crf_id() -> None:
    client = TestClient(app)
    response = client.post("/map", json={"ir_id": "123"})
    assert response.status_code == 200
    data = response.json()
    assert data["crf_id"]
