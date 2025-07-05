from fastapi import APIRouter, UploadFile, File, HTTPException
from services.premium_service import analyze_premium

router = APIRouter()

@router.post(
    "/premium/analyze",
    operation_id="analyzePremium",
    summary="Premium Margin Analysis",
    description="Run advanced premium-level analysis with forecasting, simulation, and GPT support."
)
async def analyze_premium_api(file: UploadFile = File(...)):
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only .csv or .xlsx files are supported.")

    contents = await file.read()
    return analyze_premium(contents, file.filename)
