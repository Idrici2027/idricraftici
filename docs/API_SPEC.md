
# IDRICI CRAFT — API Specification

## 1. Purpose

This document defines the planned API contract between the IDRICI CRAFT Android application and its backend.

All endpoints described here are specifications and are not yet implemented.

## 2. API Principles

- API base path: `/api/v1`
- Protocol: HTTPS only in production.
- Data format: JSON.
- Character encoding: UTF-8.
- Authentication: Bearer access token.
- All timestamps: ISO 8601 UTC.
- Long-running operations must be asynchronous.
- The server is the source of truth for task status and progress.

## 3. Authentication

Protected endpoints require:

`Authorization: Bearer <access_token>`

Authentication endpoints:

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`
- `POST /api/v1/auth/refresh`
- `POST /api/v1/auth/logout`

The backend must validate tokens and enforce authorization for every resource.

## 4. Standard Response Format

Successful response:

```json
{
  "success": true,
  "data": {},
  "error": null
}
```

Error response:

```json
{
  "success": false,
  "data": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid request",
    "details": {}
  }
}
```

## 5. Projects

### Create Project

`POST /api/v1/projects`

Request:

```json
{
  "name": "My Project",
  "source_type": "description",
  "source": "Build a modern website"
}
```

Supported source types:

- `url`
- `repository`
- `description`

Response:

```json
{
  "success": true,
  "data": {
    "project_id": "project_123",
    "name": "My Project",
    "status": "created"
  },
  "error": null
}
```

### List Projects

`GET /api/v1/projects`

### Get Project

`GET /api/v1/projects/{project_id}`

### Update Project

`PATCH /api/v1/projects/{project_id}`

### Delete Project

`DELETE /api/v1/projects/{project_id}`

All project operations must enforce user ownership.

## 6. Tasks

### Create Task

`POST /api/v1/tasks`

Request:

```json
{
  "project_id": "project_123",
  "workflow": [
    "STUDY",
    "PLAN",
    "BUILD",
    "CHECK",
    "REFINE"
  ],
  "instructions": "Analyze and improve the project"
}
```

Response:

```json
{
  "success": true,
  "data": {
    "task_id": "task_123",
    "project_id": "project_123",
    "status": "queued"
  },
  "error": null
}
```

### Get Task

`GET /api/v1/tasks/{task_id}`

### List Tasks

`GET /api/v1/tasks`

### Cancel Task

`POST /api/v1/tasks/{task_id}/cancel`

Cancellation must be confirmed by the backend.

## 7. Task Status

Allowed task states:

- `queued`
- `running`
- `waiting_for_approval`
- `succeeded`
- `failed`
- `cancelled`

The backend must never report `succeeded` before the required verification is complete.

## 8. Task Events

`GET /api/v1/tasks/{task_id}/events`

The initial implementation may use Server-Sent Events (SSE).

Events should include:

- `task.started`
- `task.progress`
- `task.stage_changed`
- `task.log`
- `task.approval_required`
- `task.completed`
- `task.failed`
- `task.cancelled`

Example event data:

```json
{
  "event": "task.progress",
  "task_id": "task_123",
  "stage": "BUILD",
  "progress": 45,
  "message": "Generating project files"
}
```

Progress values must come from actual execution events, not simulated timers.

## 9. Workflow Stages

The API must recognize these stages:

1. STUDY
2. PLAN
3. BUILD
4. CHECK
5. REFINE

The backend must report the active stage and its actual status.

## 10. Files

### List Project Files

`GET /api/v1/projects/{project_id}/files`

### Get File Metadata

`GET /api/v1/files/{file_id}`

### Download File

`GET /api/v1/files/{file_id}/download`

File access must be restricted to authorized project owners.

Large files should use controlled storage and temporary download URLs when appropriate.

## 11. Pagination

List endpoints should support:

- `limit`
- `cursor`

Responses should include:

```json
{
  "items": [],
  "next_cursor": null
}
```

## 12. Idempotency

Task creation should support an `Idempotency-Key` header to prevent duplicate tasks when a mobile client retries a request.

## 13. HTTP Status Codes

- `200` OK
- `201` Created
- `202` Accepted
- `400` Bad Request
- `401` Unauthorized
- `403` Forbidden
- `404` Not Found
- `409` Conflict
- `422` Unprocessable Entity
- `429` Too Many Requests
- `500` Internal Server Error
- `503` Service Unavailable

## 14. Security Requirements

- Validate every request.
- Enforce user and project ownership.
- Apply rate limits.
- Protect against SSRF.
- Never expose AI provider keys.
- Never trust client-supplied task status.
- Restrict file access.
- Filter secrets from logs.
- Validate uploaded file types and sizes.
- Use secure token storage on Android.

## 15. Android Client Requirements

The Android client must:

- Handle network timeouts.
- Retry safe requests when appropriate.
- Use idempotency keys for task creation.
- Display server-confirmed task states.
- Support interrupted connections.
- Resume event monitoring after reconnection.
- Display meaningful error messages.
- Never assume a task succeeded without backend confirmation.

## 16. Implementation Status

API contract: Defined.

Backend endpoints: Not implemented.

Authentication: Not implemented.

Task event streaming: Not implemented.

This document describes the planned API contract and does not claim that these endpoints are operational.
