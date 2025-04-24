from app.api import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_chat():
    response = client.get("/ask?question=Hello")
    assert response.status_code == 200
    assert len(response.json()["response"]) > 0