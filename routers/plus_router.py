@router.post(
    "/analyze",
    operation_id="analyzePlus",  # Change this per agent: analyzePlus, analyzePremium
    summary="Analyze Plus Forecast",
    description="Upload file and analyze forecast vs actual using plus agent logic."
)
async def analyze(file: UploadFile = File(...)):
    ...
