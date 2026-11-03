
"""Central API router for IDRICI CRAFT version 1."""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["Health"])
async def api_v1_health() -> dict[str, str]:
    """Check API v1 availability."""
    return {
        "status": "healthy",
        "version": "v1",
        "service": "idrici-craft",
    }
