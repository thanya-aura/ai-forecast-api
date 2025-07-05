from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

@router.post(
    "/analyze",
    operation_id="analyze_plus",
    summary="Analyze Plus Forecast",
    description="Upload file and analyze forecast vs actual using plus agent logic."
)
async def analyze(file: UploadFile = File(...)):
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only .csv or .xlsx files are supported.")
    contents = await file.read()
    # Placeholder logic for plus forecast analysis
    return {
        "agent": "plus",
        "rows": 150,
        "average_variance": 9.8,
        "commentary": "Driver-based tuning applied.",
        "red_flags": ["Revenue drop in Q2"]
    }
