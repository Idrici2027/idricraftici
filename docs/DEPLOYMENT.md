
# IDRICI CRAFT — Deployment Guide

## 1. Purpose

This document defines the deployment strategy for IDRICI CRAFT.

It describes how the backend and Android application will be configured, tested, and deployed.

## 2. Deployment Principles

- Keep development and production environments separate.
- Never expose secrets in the Android application.
- Store sensitive credentials on the backend.
- Verify deployments before accepting them.
- Keep deployment configuration documented.
- Use secure communication between components.
- Maintain a recovery procedure.

## 3. Backend Deployment

The backend will be deployed as an independent service.

Deployment requirements:

- Supported runtime environment.
- Application dependencies.
- Database connectivity.
- Environment configuration.
- Secure API configuration.
- Application logging.
- Health check endpoint.

The backend must pass its initial tests before production deployment.

## 4. Environment Variables

Sensitive configuration must be provided through the deployment platform's environment variable settings.

Examples of configuration categories:

- Application environment.
- Database connection.
- Authentication secrets.
- AI provider credentials.
- API configuration.
- External service credentials.

Actual secret values must never be committed to Git.

## 5. Database Deployment

The production database must:

- Use authenticated connections.
- Restrict unauthorized access.
- Support backups.
- Protect stored user data.
- Apply database migrations safely.

Development databases must remain separate from production databases.

## 6. Android Application Build

The Android application must be built using the verified project configuration.

Build requirements:

- Valid Android project structure.
- Correct application identifier.
- Required permissions only.
- Backend API configuration.
- Correct application branding.
- Successful build verification.

Release builds must not contain development secrets.

## 7. Android Release Preparation

Before preparing a release:

- Verify application startup.
- Verify backend connectivity.
- Verify authentication.
- Verify project creation.
- Verify Arabic RTL interface.
- Review application permissions.
- Check critical errors.
- Record the release version.

## 8. Deployment Verification

After deployment, verify:

- Backend service availability.
- Health check response.
- API connectivity.
- Database connectivity.
- Authentication behavior.
- Application communication.
- Error logging.

A successful deployment operation does not automatically mean the application is fully verified.

## 9. Rollback and Recovery

Deployment procedures must include:

- Previous stable version identification.
- Configuration backup.
- Database backup where applicable.
- Rollback procedure.
- Service recovery verification.

Never perform destructive production changes without a recovery plan.

## 10. Deployment Status

Use the following statuses:

- NOT CONFIGURED
- IN PROGRESS
- DEPLOYED
- FAILED
- VERIFIED

DEPLOYED means the deployment operation completed.

VERIFIED means the deployed service passed its required checks.

## 11. Current Project Status

Project: IDRICI CRAFT

Repository: Idrici2027/idricraftici

Branch: main

Current status: DEPLOYMENT DOCUMENTATION

No production deployment is claimed by the existence of this document.

Actual deployment details must be recorded after the corresponding services are implemented.
