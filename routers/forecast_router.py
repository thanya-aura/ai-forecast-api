from fastapi import APIRouter, UploadFile, File, HTTPException
from services.forecast_service import analyze_forecast
from utils.loader import load_forecast_from_file

router = APIRouter()

@router.post(
    "/forecast/analyze",
    operation_id="analyzeForecast",  # ✅ Resolves OpenAPI warning
    summary="Analyze Forecast vs Actuals",
    description="Upload a CSV or Excel file to compare forecast vs actuals using AI-powered logic."
)
async def analyze_forecast_api(file: UploadFile = File(...)):
    """
    Analyze uploaded forecast vs actuals Excel or CSV file.
    """
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="❌ Only .csv or .xlsx files are supported.")

    try:
        contents = await file.read()
        df = load_forecast_from_file(contents, file.filename)
        result = analyze_forecast(df)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"⚠️ Analysis failed: {str(e)}")
