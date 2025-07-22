from fastapi.testclient import TestClient

from protocol_to_crf_generator.api.main import app


def test_validate_endpoint_returns_status() -> None:
    client = TestClient(app)
    response = client.post("/validate", json={"crf_id": "123"})
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "valid"
