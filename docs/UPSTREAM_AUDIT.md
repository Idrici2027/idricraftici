IDRICI CRAFT — Upstream Source Audit

1. Purpose

This document defines the technical audit process for the original Craft Anything repository.

Upstream repository:
https://github.com/storytold/craft-anything

2. Audit Objectives

- Understand the original system architecture.
- Identify programming languages and frameworks.
- Identify frontend and backend components.
- Review dependencies.
- Identify reusable modules.
- Evaluate compatibility with Android and our backend.
- Identify security risks.

3. Source Code Review

The audit must inspect:

- Repository structure.
- Main application entry points.
- Frontend implementation.
- Backend implementation.
- API communication.
- AI integration.
- Build and deployment configuration.
- Database and storage components.

4. Technology Identification

Record the actual technologies discovered during inspection.

Do not assume a framework or programming language without verifying the source code.

5. Reusable Components

Each candidate component must be evaluated for:

- Technical compatibility.
- License compatibility.
- Security.
- Maintenance requirements.
- Integration complexity.

6. License Compliance

Before reusing any source code:

- Identify the repository license.
- Review third-party dependency licenses.
- Preserve copyright notices.
- Follow redistribution requirements.
- Document modifications.

7. Security Review

Inspect:

- Authentication.
- API security.
- Secret management.
- File operations.
- External URL processing.
- Code execution.
- Worker isolation.
- Dependency vulnerabilities.

8. Android Compatibility

Evaluate which components can:

- Run directly on Android.
- Communicate with Android through an API.
- Be adapted for server-side execution.
- Be replaced with native Android components.

9. Audit Results

The following fields must be completed after actual source inspection:

- Confirmed technologies.
- Reusable components.
- Required modifications.
- Security findings.
- License findings.
- Integration recommendations.

10. Audit Status

Current status: NOT STARTED

No upstream component is approved for reuse until the technical and license reviews are completed.

---

Project: IDRICI CRAFT
