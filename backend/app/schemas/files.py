"""Project file schemas for IDRICI CRAFT."""

from pydantic import BaseModel, ConfigDict, Field


class ProjectFileResponse(BaseModel):
    """Project file metadata returned by the API."""

    model_config = ConfigDict(from_attributes=True)

    file_id: str
    project_id: str
    name: str
    path: str
    content_type: str | None = None
    size: int = Field(ge=0)
    created_at: str


class FileDownloadResponse(BaseModel):
    """File download information."""

    file_id: str
    download_url: str
    expires_at: str
