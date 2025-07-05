import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_forecast_analyze_missing_file():
    """
    Test that calling /forecast/analyze without a file returns 422 Unprocessable Entity.
    """
    response = client.post("/forecast/analyze")  # ✅ Corrected path (no /api prefix)
    assert response.status_code == 422

