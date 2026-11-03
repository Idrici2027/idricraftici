
# IDRICI CRAFT — Testing Strategy

## 1. Purpose

This document defines the testing strategy for IDRICI CRAFT.

Its purpose is to ensure that every component is tested before being considered complete or verified.

## 2. Testing Principles

- Test each component independently.
- Verify integration between Android and backend.
- Test both successful and failed operations.
- Protect user data and credentials.
- Test Arabic and right-to-left layouts.
- Never mark a feature as VERIFIED without evidence.
- Record defects and their resolution.

## 3. Testing Levels

### 3.1 Unit Testing

Test individual functions and components.

Examples:

- Input validation.
- Authentication logic.
- API request handling.
- Workflow state transitions.
- File validation.
- Error handling.

### 3.2 Integration Testing

Verify communication between components.

Examples:

- Android to backend communication.
- Backend to database communication.
- Backend to AI provider integration.
- Workflow engine to execution workers.
- Generated files to validation services.

### 3.3 System Testing

Test the complete application as one system.

Examples:

- Application startup.
- User authentication.
- Project creation.
- AI workflow execution.
- Project file generation.
- Results display.
- Error recovery.

### 3.4 Security Testing

Verify that the system protects users and infrastructure.

Examples:

- Authentication and authorization.
- API access restrictions.
- Secret and credential protection.
- Input validation.
- File operation restrictions.
- External URL validation.
- Worker isolation.
- Resource limits.

### 3.5 User Interface Testing

Verify the Android application interface.

Examples:

- Navigation.
- Screen rendering.
- Responsive layouts.
- Arabic language support.
- Right-to-left text direction.
- Input fields and buttons.
- Loading and error states.
- Workflow progress display.

## 4. Core Workflow Tests

The five workflow stages must be tested individually and together.

### STUDY

- Understand user requests.
- Inspect supported URLs.
- Analyze project requirements.
- Handle incomplete input.

### PLAN

- Generate structured plans.
- Identify required components.
- Identify dependencies.
- Detect missing requirements.

### BUILD

- Generate project files.
- Create valid source code.
- Modify existing files safely.
- Track generated artifacts.

### CHECK

- Validate generated files.
- Execute available tests.
- Detect errors.
- Report actual results.

### REFINE

- Analyze detected errors.
- Apply corrections.
- Repeat relevant tests.
- Report verified improvements.

## 5. Test Environments

Testing must use separate environments when applicable:

- Local development.
- Backend testing.
- Android testing.
- Integration testing.
- Production verification.

Production credentials must not be exposed in test environments.

## 6. Test Data

- Use controlled test accounts.
- Use non-sensitive sample projects.
- Avoid real user secrets.
- Keep test data separate from production data.
- Remove temporary test data when no longer required.

## 7. Defect Management

Every discovered defect should include:

- Defect description.
- Affected component.
- Steps to reproduce.
- Expected result.
- Actual result.
- Severity.
- Resolution status.
- Verification result.

Severity levels:

- CRITICAL
- HIGH
- MEDIUM
- LOW

## 8. Release Acceptance Criteria

A release candidate must satisfy these requirements:

- Application starts successfully.
- Main navigation works.
- Authentication works correctly.
- Project creation works.
- Backend communication works.
- Core workflow stages are tested.
- Generated files are validated.
- Critical security tests pass.
- Arabic RTL interface is verified.
- No unresolved critical defects remain.

## 9. Testing Status

Use the following statuses:

- NOT TESTED
- IN PROGRESS
- PASSED
- FAILED
- BLOCKED
- VERIFIED

PASSED means the test produced the expected result.

VERIFIED means the result has been reviewed and supported by recorded evidence.

## 10. Current Testing Status

Project: IDRICI CRAFT

Repository: Idrici2027/idricraftici

Branch: main

Current status: TESTING STRATEGY DOCUMENTATION

No software test is considered passed merely because this document exists.

Actual test results must be recorded after implementation begins.
