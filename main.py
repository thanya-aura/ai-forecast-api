from fastapi import FastAPI
from routers.standard_router import router as standard_router
from routers.plus_router import router as plus_router
from routers.premium_router import router as premium_router
from routers.forecast_router import router as forecast_router

app = FastAPI(
    title="AI Forecast API",
    description="Unified API for Standard, Plus, Premium, and Forecast Agents",
    version="1.0.0"
)

# Register all routers with correct prefixes
app.include_router(standard_router, prefix="/standard", tags=["Standard"])
app.include_router(plus_router, prefix="/plus", tags=["Plus"])
app.include_router(premium_router, prefix="/premium", tags=["Premium"])
app.include_router(forecast_router, prefix="/forecast", tags=["Forecast"])

# Optional route inspector (for debugging)
if __name__ == "__main__":
    import uvicorn
    for route in app.routes:
        print(f"{route.path}  →  {route.name}")
    uvicorn.run(app, host="0.0.0.0", port=8000)
