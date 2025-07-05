@router.post(
    "/analyze",
    operation_id="analyzeStandard",  # Change this per agent: analyzePlus, analyzePremium
    summary="Analyze Standard Forecast",
    description="Upload file and analyze forecast vs actual using standard agent logic."
)
async def analyze(file: UploadFile = File(...)):
    ...
