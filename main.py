from fastapi import FastAPI, UploadFile, File
from routers.forecast_router import router as forecast_router

app = FastAPI(title="AI Forecast API")

app.include_router(forecast_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "AI Forecast API is running"}