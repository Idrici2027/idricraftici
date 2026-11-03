"""Task schemas for IDRICI CRAFT."""

from enum import Enum

from pydantic import BaseModel, Field, ConfigDict


class WorkflowStage(str, Enum):
    """Supported AI workflow stages."""

    STUDY = "STUDY"
    PLAN = "PLAN"
    BUILD = "BUILD"
    CHECK = "CHECK"
    REFINE = "REFINE"


class TaskStatus(str, Enum):
    """Possible task execution states."""

    QUEUED = "queued"
    RUNNING = "running"
    WAITING_FOR_APPROVAL = "waiting_for_approval"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


class TaskCreate(BaseModel):
    """Validate task creation requests."""

    project_id: str = Field(min_length=1, max_length=120)

    workflow: list[WorkflowStage] = Field(
        default_factory=lambda: [
            WorkflowStage.STUDY,
            WorkflowStage.PLAN,
            WorkflowStage.BUILD,
            WorkflowStage.CHECK,
            WorkflowStage.REFINE,
        ],
        min_length=1,
        max_length=5,
    )

    instructions: str = Field(
        min_length=1,
        max_length=10000,
    )


class TaskResponse(BaseModel):
    """Standard task response."""

    model_config = ConfigDict(from_attributes=True)

    task_id: str
    project_id: str
    status: TaskStatus
