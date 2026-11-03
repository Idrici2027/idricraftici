
# IDRICI CRAFT — Security Policy

## 1. Purpose

This document defines the security requirements for IDRICI CRAFT.

Security must be considered in every component, including the Android application, backend API, AI integrations, databases, file storage and execution workers.

## 2. Security Principles

- Security by design.
- Least privilege.
- Defense in depth.
- Zero trust for user input and generated code.
- Isolation of untrusted operations.
- No secrets inside the Android APK.
- Explicit authorization for sensitive operations.

## 3. Android Application Security

The Android client must:

- Communicate with the backend over HTTPS.
- Store authentication tokens securely.
- Never contain AI provider API keys.
- Never contain database passwords.
- Validate user input before sending requests.
- Avoid exposing sensitive information in logs.
- Handle authentication expiration safely.
- Avoid storing sensitive project data unnecessarily.

Certificate pinning may be considered after evaluating certificate rotation and recovery risks.

## 4. Backend Security

The backend must:

- Authenticate every protected request.
- Enforce authorization on every resource.
- Validate all incoming data.
- Apply request rate limits.
- Use secure HTTP headers.
- Protect against injection attacks.
- Protect against Cross-Site Request Forgery where applicable.
- Protect against Server-Side Request Forgery (SSRF).
- Use secure session and token expiration.
- Avoid exposing internal errors to clients.

## 5. Secrets Management

All sensitive credentials must remain on the server.

Examples:

- AI provider API keys.
- Database credentials.
- Storage credentials.
- Signing keys.
- Authentication secrets.

Requirements:

- Use environment variables or a dedicated secrets manager.
- Never commit secrets to GitHub.
- Never include secrets in application builds.
- Rotate compromised credentials immediately.
- Restrict access to production secrets.
- Filter credentials from logs and error reports.

## 6. AI Integration Security

AI-generated output must always be considered untrusted.

Requirements:

- Validate AI-generated commands before execution.
- Restrict available tools and permissions.
- Prevent unauthorized file access.
- Prevent secret disclosure through prompts or logs.
- Apply input and output limits.
- Apply execution timeouts.
- Require approval for sensitive operations.
- Do not allow AI output to bypass backend authorization.

Prompt injection must be treated as a security risk, especially when processing external websites and repositories.

## 7. Execution Worker Isolation

Every project task must execute in an isolated workspace.

Workers must have:

- Separate task workspaces.
- CPU limits.
- Memory limits.
- Disk usage limits.
- Execution time limits.
- Restricted network access.
- No direct access to backend secrets.
- No unrestricted host filesystem access.
- Automatic cleanup after task completion.

Untrusted project code must never execute directly inside the main backend process.

## 8. Repository and URL Security

When importing external repositories or websites:

- Validate URLs.
- Restrict access to private network addresses.
- Block cloud metadata endpoints.
- Prevent access to localhost and internal services.
- Limit download sizes.
- Limit redirects.
- Validate downloaded files.
- Avoid executing imported scripts automatically.

Only access resources that the user is authorized to inspect.

## 9. File Storage Security

Requirements:

- Enforce project ownership.
- Validate file paths.
- Prevent directory traversal.
- Validate upload types and sizes.
- Use controlled download access.
- Use temporary download URLs when appropriate.
- Prevent unauthorized file enumeration.
- Avoid exposing internal storage paths.

## 10. Database Security

- Use parameterized queries.
- Apply least-privilege database accounts.
- Restrict database network access.
- Encrypt sensitive data where appropriate.
- Back up important data securely.
- Protect backups from unauthorized access.
- Avoid storing unnecessary sensitive information.

## 11. Logging and Monitoring

The system should record:

- Authentication events.
- Authorization failures.
- Task execution events.
- Worker failures.
- Security-related errors.
- Administrative actions.

Logs must not contain:

- Passwords.
- Access tokens.
- API keys.
- Private credentials.
- Unnecessary personal data.

Security events should be monitored for suspicious activity.

## 12. User Approval

Sensitive operations may require explicit user approval.

Examples:

- Deleting important project files.
- Publishing a project publicly.
- Deploying to production.
- Accessing external services.
- Performing destructive operations.

The backend must enforce approval requirements.

## 13. Dependency Security

- Review dependencies before adoption.
- Prefer maintained packages.
- Check known vulnerabilities.
- Pin important dependency versions.
- Remove unused dependencies.
- Review licenses.
- Update vulnerable components.

## 14. Incident Response

When a security incident is detected:

1. Identify the affected component.
2. Restrict or disable the affected operation.
3. Revoke compromised credentials.
4. Preserve relevant security logs.
5. Investigate the root cause.
6. Apply and test a fix.
7. Restore services safely.

## 15. Security Testing

Before production deployment, perform:

- Authentication tests.
- Authorization tests.
- Input validation tests.
- SSRF tests.
- File access tests.
- Worker isolation tests.
- Dependency vulnerability checks.
- Secret scanning.
- API security tests.

## 16. Implementation Status

Security requirements: Defined.

Security controls: Not yet fully implemented.

Security testing: Pending.

This document defines planned security requirements and does not claim that all protections are already operational.
