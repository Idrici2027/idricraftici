
"""Main entry point for the IDRICI CRAFT API."""

from fastapi import FastAPI

app = FastAPI(
    title="IDRICI CRAFT API",
    description="Backend API for the IDRICI CRAFT application.",
    version="0.1.0",
)


@app.get("/", tags=["General"])
async def root() -> dict[str, str]:
    """Return basic API information."""
    return {
        "name": "IDRICI CRAFT",
        "status": "online",
        "version": "0.1.0",
    }


@app.get("/health", tags=["Health"])
async def health_check() -> dict[str, str]:
    """Check whether the API is responding."""
    return {
        "status": "healthy",
        "service": "idrici-craft-backend",
    }
