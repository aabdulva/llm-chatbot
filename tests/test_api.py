from fastapi.testclient import TestClient
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Add project root to PATH

from app.api import app

client = TestClient(app)

def test_read_main():
    response = client.get("/ask?question=Hello")
    assert response.status_code == 200
    assert isinstance(response.json()["response"], str)