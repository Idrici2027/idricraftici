"""Workflow execution state management for IDRICI CRAFT."""

from dataclasses import dataclass, field

from app.schemas.tasks import WorkflowStage


@dataclass
class WorkflowExecution:
    """Track the execution of a task's workflow stages."""

    stages: list[WorkflowStage]
    completed_stages: list[WorkflowStage] = field(default_factory=list)
    current_stage: WorkflowStage | None = None
    failed: bool = False

    def __post_init__(self) -> None:
        if not self.stages:
            raise ValueError("A workflow must contain at least one stage.")

        if len(set(self.stages)) != len(self.stages):
            raise ValueError("A workflow cannot contain duplicate stages.")

    @property
    def progress(self) -> int:
        """Return progress based on completed stages."""
        return round(
            len(self.completed_stages) / len(self.stages) * 100
        )

    @property
    def is_complete(self) -> bool:
        """Return whether every workflow stage is completed."""
        return len(self.completed_stages) == len(self.stages)

    def start_next_stage(self) -> WorkflowStage | None:
        """Start the next stage in the configured workflow."""
        if self.failed:
            raise ValueError("A failed workflow cannot continue.")

        if self.current_stage is not None:
            raise ValueError("The current stage must finish first.")

        if self.is_complete:
            return None

        next_stage = self.stages[len(self.completed_stages)]
        self.current_stage = next_stage
        return next_stage

    def complete_current_stage(self) -> WorkflowStage:
        """Mark the active stage as completed."""
        if self.current_stage is None:
            raise ValueError("There is no active stage to complete.")

        completed = self.current_stage
        self.completed_stages.append(completed)
        self.current_stage = None
        return completed

    def fail_current_stage(self) -> WorkflowStage:
        """Mark the active stage as failed."""
        if self.current_stage is None:
            raise ValueError("There is no active stage to fail.")

        failed_stage = self.current_stage
        self.current_stage = None
        self.failed = True
        return failed_stage
