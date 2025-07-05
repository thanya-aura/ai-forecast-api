from fastapi import APIRouter, UploadFile, File, HTTPException
from services.standard_service import analyze_standard

router = APIRouter()

@router.post(
    "/standard/analyze",
    operation_id="analyzeStandard",
    summary="Standard Margin Analysis",
    description="Run standard-level margin analysis on uploaded Excel or CSV file."
)
async def analyze_standard_api(file: UploadFile = File(...)):
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only .csv or .xlsx files are supported.")

    contents = await file.read()
    return analyze_standard(contents, file.filename)
