"""Tests for the IDRICI CRAFT workflow engine."""

import pytest

from app.schemas.tasks import WorkflowStage
from app.services.workflow import WorkflowExecution


def create_workflow():
    return WorkflowExecution(
        stages=[
            WorkflowStage.STUDY,
            WorkflowStage.PLAN,
            WorkflowStage.BUILD,
            WorkflowStage.CHECK,
            WorkflowStage.REFINE,
        ]
    )


def test_workflow_starts_with_zero_progress():
    workflow = create_workflow()

    assert workflow.progress == 0
    assert workflow.is_complete is False


def test_workflow_starts_study_stage():
    workflow = create_workflow()

    assert workflow.start_next_stage() == WorkflowStage.STUDY


def test_workflow_progress_after_completion():
    workflow = create_workflow()

    workflow.start_next_stage()
    workflow.complete_current_stage()

    assert workflow.progress == 20


def test_workflow_runs_all_five_stages():
    workflow = create_workflow()

    for stage in workflow.stages:
        assert workflow.start_next_stage() == stage
        workflow.complete_current_stage()

    assert workflow.is_complete is True
    assert workflow.progress == 100
    assert workflow.start_next_stage() is None


def test_workflow_cannot_start_two_stages():
    workflow = create_workflow()

    workflow.start_next_stage()

    with pytest.raises(ValueError):
        workflow.start_next_stage()


def test_workflow_cannot_complete_without_active_stage():
    workflow = create_workflow()

    with pytest.raises(ValueError):
        workflow.complete_current_stage()


def test_workflow_failure_stops_execution():
    workflow = create_workflow()

    workflow.start_next_stage()
    failed = workflow.fail_current_stage()

    assert failed == WorkflowStage.STUDY
    assert workflow.failed is True

    with pytest.raises(ValueError):
        workflow.start_next_stage()


def test_workflow_rejects_empty_stages():
    with pytest.raises(ValueError):
        WorkflowExecution(stages=[])


def test_workflow_rejects_duplicate_stages():
    with pytest.raises(ValueError):
        WorkflowExecution(
            stages=[
                WorkflowStage.STUDY,
                WorkflowStage.STUDY,
            ]
        )
