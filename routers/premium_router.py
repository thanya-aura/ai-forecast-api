@router.post(
    "/analyze",
    operation_id="analyzePremium",  # Change this per agent: analyzePlus, analyzePremium
    summary="Analyze Premium Forecast",
    description="Upload file and analyze forecast vs actual using premium agent logic."
)
async def analyze(file: UploadFile = File(...)):
    ...
