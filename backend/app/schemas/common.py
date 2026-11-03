"""Standard API response schemas for IDRICI CRAFT."""

from typing import Generic, TypeVar

from pydantic import BaseModel


T = TypeVar("T")


class APIError(BaseModel):
    """Standard API error structure."""

    code: str
    message: str
    details: dict = {}


class APIResponse(BaseModel, Generic[T]):
    """Standard API response envelope."""

    success: bool
    data: T | None = None
    error: APIError | None = None
