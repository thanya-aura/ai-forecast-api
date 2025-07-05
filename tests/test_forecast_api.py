import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_forecast_analyze_missing_file():
    response = client.post("/api/forecast/analyze")
    assert response.status_code == 422  # Missing file should trigger 422 validation error
