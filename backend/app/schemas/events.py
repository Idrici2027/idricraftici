"""Task event schemas for IDRICI CRAFT."""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

from app.schemas.tasks import WorkflowStage, TaskStatus


class TaskEventType(str, Enum):
    """Supported task event types."""

    STARTED = "task.started"
    PROGRESS = "task.progress"
    STAGE_CHANGED = "task.stage_changed"
    LOG = "task.log"
    APPROVAL_REQUIRED = "task.approval_required"
    COMPLETED = "task.completed"
    FAILED = "task.failed"
    CANCELLED = "task.cancelled"


class TaskEvent(BaseModel):
    """Task execution event."""

    event: TaskEventType
    task_id: str
    stage: WorkflowStage | None = None
    progress: int | None = Field(default=None, ge=0, le=100)
    message: str | None = Field(default=None, max_length=5000)
    status: TaskStatus | None = None
    timestamp: datetime
