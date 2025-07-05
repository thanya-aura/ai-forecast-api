from fastapi import APIRouter, UploadFile, File, HTTPException
from services.plus_service import analyze_plus

router = APIRouter()

@router.post(
    "/plus/analyze",
    operation_id="analyzePlus",
    summary="Plus Margin Analysis",
    description="Run plus-tier margin analysis with added variance and override features."
)
async def analyze_plus_api(file: UploadFile = File(...)):
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only .csv or .xlsx files are supported.")

    contents = await file.read()
    return analyze_plus(contents, file.filename)
