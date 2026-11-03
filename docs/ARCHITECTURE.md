
# IDRICI CRAFT — System Architecture

## 1. Overview

IDRICI CRAFT is an Android-first AI project creation platform inspired by Craft Anything.

The system uses a client-server architecture. Android handles the user experience, while the backend coordinates AI agents and isolated execution workers.

## 2. System Components

- Android Client: Mobile interface, project management and task monitoring.
- Backend API: Authentication, project management and task coordination.
- Task Orchestrator: Controls the five workflow stages.
- AI Engine: AI-assisted analysis and code generation.
- Execution Workers: Run builds, tests and project operations in isolated environments.
- Database: Stores users, projects, tasks and execution history.
- File Storage: Stores generated project files and artifacts.

## 3. Architecture Flow

1. User submits a website URL, repository URL or project description.
2. Android sends the request to the backend over HTTPS.
3. Backend validates the request and authenticates the user.
4. Backend creates a task.
5. Task Orchestrator assigns work to an execution worker.
6. AI Engine assists with analysis and implementation.
7. Worker executes the required operations in isolation.
8. Backend records progress, logs and generated files.
9. Android displays confirmed results to the user.

Long-running tasks must execute asynchronously.

## 4. Workflow

### STUDY
Inspect the target project and identify its technologies and structure.

### PLAN
Prepare an implementation plan and identify dependencies and risks.

### BUILD
Generate or modify project files using approved AI coding tools.

### CHECK
Run tests, builds and validation checks.

### REFINE
Improve the implementation and repeat relevant checks.

## 5. Android Client

The Android application must provide:

- Original IDRICI CRAFT branding.
- Arabic interface with RTL support.
- Project creation and history.
- Task monitoring.
- File browsing.
- Execution logs.
- Error and success notifications.
- Task cancellation when supported.

The Android application must never contain privileged server credentials or AI provider API keys.

## 6. Backend API

The backend is the only public entry point for the Android client.

Planned API resources:

- /api/v1/projects
- /api/v1/tasks
- /api/v1/tasks/{task_id}
- /api/v1/tasks/{task_id}/events
- /api/v1/tasks/{task_id}/cancel
- /api/v1/files/{file_id}

These endpoints are planned and are not yet implemented.

## 7. Task States

Every task must have a persistent status:

- queued
- running
- waiting_for_approval
- succeeded
- failed
- cancelled

Progress must reflect real execution events. Never display invented progress or claim completion before verification.

## 8. AI Engine

The AI integration must:

- Run on the server.
- Support replaceable AI providers.
- Protect API keys.
- Validate tool operations.
- Apply usage limits and timeouts.
- Support AI-assisted analysis and coding.

## 9. Execution Workers

All demanding operations must run in isolated environments.

Security requirements:

- Separate workspace for every task.
- CPU and memory limits.
- Execution time limits.
- Restricted network access.
- No access to backend secrets.
- Safe file path validation.
- Automatic cleanup after execution.

## 10. Database and Storage

The system must store:

- User information.
- Project metadata.
- Task status.
- Execution history.
- Logs.
- Generated file references.
- Approval records.

Large files must use controlled file storage.

## 11. Security

- HTTPS communication.
- Authentication and authorization.
- Server-side secret management.
- Protection against SSRF.
- Rate limiting.
- Secure worker isolation.
- Sensitive log filtering.
- No credentials committed to GitHub.

Only inspect resources the user is authorized to access.

## 12. Deployment

Planned deployment structure:

- Public Backend API.
- Private Task Orchestrator.
- Isolated Execution Workers.
- Database.
- File Storage.
- External AI Providers.

The final hosting technology will be selected during implementation.

## 13. Upstream Integration

Technical reference:

https://github.com/storytold/craft-anything

Before reusing upstream components:

1. Audit source code.
2. Review dependencies.
3. Verify licensing.
4. Review security.
5. Test compatibility.
6. Preserve required copyright notices.

Rust components may be adapted only after technical review.

## 14. Development Order

1. Audit upstream source.
2. Define API contracts.
3. Implement backend.
4. Implement task management.
5. Implement isolated workers.
6. Integrate AI providers.
7. Build Android application.
8. Integrate files and logs.
9. Run security and integration tests.

## 15. Implementation Status

Architecture defined.

Implementation pending.

This document describes the planned system and does not claim that its components are already operational.
