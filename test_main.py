from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_character():
    response = client.get("/characters/Test")
    assert response.status_code == 200
    assert response.json()["name"] == "Test"
