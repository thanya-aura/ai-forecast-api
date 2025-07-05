from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter()

@router.post(
    "/analyze",
    operation_id="analyze_standard",
    summary="Analyze Standard Forecast",
    description="Upload file and analyze forecast vs actual using standard agent logic."
)
async def analyze(file: UploadFile = File(...)):
    if not file.filename.endswith((".csv", ".xlsx")):
        raise HTTPException(status_code=400, detail="Only .csv or .xlsx files are supported.")
    contents = await file.read()
    # Placeholder logic for standard forecast analysis
    return {
        "agent": "standard",
        "rows": 100,
        "average_variance": 12.5,
        "commentary": "Standard forecast looks stable.",
        "red_flags": []
    }
