"""Tests for IDRICI CRAFT API schemas."""

import pytest
from pydantic import ValidationError

from app.schemas.projects import (
    ProjectCreate,
    ProjectSourceType,
    ProjectResponse,
)
from app.schemas.tasks import (
    TaskCreate,
    TaskStatus,
    WorkflowStage,
)
from app.schemas.files import ProjectFileResponse
from app.schemas.events import TaskEvent, TaskEventType


def test_project_create_valid():
    project = ProjectCreate(
        name="My Project",
        source_type=ProjectSourceType.DESCRIPTION,
        source="Build a modern website",
    )

    assert project.name == "My Project"


def test_project_create_rejects_empty_name():
    with pytest.raises(ValidationError):
        ProjectCreate(
            name="",
            source_type="description",
            source="Build a website",
        )


def test_task_create_default_workflow():
    task = TaskCreate(
        project_id="project_123",
        instructions="Build an application",
    )

    assert task.workflow == [
        WorkflowStage.STUDY,
        WorkflowStage.PLAN,
        WorkflowStage.BUILD,
        WorkflowStage.CHECK,
        WorkflowStage.REFINE,
    ]


def test_task_status_values():
    assert TaskStatus.QUEUED.value == "queued"
    assert TaskStatus.SUCCEEDED.value == "succeeded"


def test_project_file_rejects_negative_size():
    with pytest.raises(ValidationError):
        ProjectFileResponse(
            file_id="file_123",
            project_id="project_123",
            name="main.py",
            path="main.py",
            size=-1,
            created_at="2026-11-03T12:00:00Z",
        )


def test_task_event_valid():
    event = TaskEvent(
        event=TaskEventType.PROGRESS,
        task_id="task_123",
        stage=WorkflowStage.BUILD,
        progress=45,
        message="Generating project files",
        timestamp="2026-11-03T12:00:00Z",
    )

    assert event.progress == 45
    assert event.stage == WorkflowStage.BUILD


def test_task_event_rejects_invalid_progress():
    with pytest.raises(ValidationError):
        TaskEvent(
            event=TaskEventType.PROGRESS,
            task_id="task_123",
            progress=120,
            timestamp="2026-11-03T12:00:00Z",
        )
