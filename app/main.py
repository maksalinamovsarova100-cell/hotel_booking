from fastapi import FastAPI

from app.core.config import settings
from fastapi import FastAPI

from app.auth.router import router as auth_router



app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }

app.include_router(auth_router)
