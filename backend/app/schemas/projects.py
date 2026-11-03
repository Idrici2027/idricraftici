"""Project schemas for IDRICI CRAFT."""

from enum import Enum

from pydantic import BaseModel, Field, ConfigDict


class ProjectSourceType(str, Enum):
    """Supported project input sources."""

    URL = "url"
    REPOSITORY = "repository"
    DESCRIPTION = "description"


class ProjectCreate(BaseModel):
    """Validate project creation requests."""

    name: str = Field(min_length=1, max_length=120)
    source_type: ProjectSourceType
    source: str = Field(min_length=1, max_length=10000)


class ProjectUpdate(BaseModel):
    """Validate project update requests."""

    name: str | None = Field(
        default=None,
        min_length=1,
        max_length=120,
    )


class ProjectResponse(BaseModel):
    """Standard project response."""

    model_config = ConfigDict(from_attributes=True)

    project_id: str
    name: str
    status: str
