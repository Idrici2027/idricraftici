
"""Main entry point for the IDRICI CRAFT API."""

from fastapi import FastAPI

from app.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    description="Backend API for the IDRICI CRAFT application.",
    version=settings.app_version,
    debug=settings.debug,
)


@app.get("/", tags=["General"])
async def root() -> dict[str, str]:
    """Return basic API information."""
    return {
        "name": "IDRICI CRAFT",
        "status": "online",
        "version": settings.app_version,
    }


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    """Check whether the API is responding."""
    return {
        "status": "healthy",
        "service": "idrici-craft-backend",
    }
