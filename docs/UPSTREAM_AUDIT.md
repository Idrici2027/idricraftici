# IDRICI CRAFT — Upstream Source Audit

## 1. Purpose

This document records verified findings from inspecting the original Craft Anything repository.

Upstream repository:
https://github.com/storytold/craft-anything

Audit date: 2026-11-03

## 2. Repository Structure

The upstream repository is organized as a Rust workspace.

Confirmed components include:

- crates/ — reusable Rust libraries.
- apps/craft-anything/ — desktop application.
- apps/craft-anything-cli/ — command-line application.
- apps/craft-anything-web/ — WebAssembly browser application.
- xtask/ — development and maintenance tools.
- docs/ — technical documentation.
- assets/ — application assets.

## 3. Confirmed Technologies

The inspected root Cargo.toml confirms:

- Primary language: Rust.
- Rust edition: 2024.
- Workspace resolver: 3.
- Desktop UI: egui and eframe.
- Serialization: serde and serde_json.
- Configuration support: TOML.
- WebAssembly-related components are present.
- JavaScript analysis components are implemented in Rust.

The upstream workspace includes separate crates for:

- AI.
- Analysis.
- Engine.
- Engines.
- Evidence.
- Formats.
- JavaScript.
- MCP.
- Platform.
- Setup.
- Testing.

These findings describe the upstream project, not an implemented IDRICI CRAFT system.

## 4. Application Architecture Findings

The upstream project provides:

- A desktop application.
- A command-line interface.
- An MCP server interface.
- A browser-based WebAssembly application.
- A Rust-based inspection and analysis engine.

The upstream README describes a workflow involving project inspection, AI-assisted building, checking, and refinement.

The upstream application is not a ready-made Android application.

No independent hosted backend API matching the planned IDRICI CRAFT architecture was confirmed during this initial inspection.

## 5. Android Compatibility

The following decisions are preliminary:

- The upstream desktop UI must not be copied as the Android interface.
- Android requires an independently designed mobile client.
- Rust engine components may be evaluated for server-side reuse.
- Android should communicate with the backend through a documented API.
- Any native Rust integration requires compatibility and security testing.

## 6. License Findings

The upstream repository declares:

MIT OR Apache-2.0.

The repository contains:

- LICENSE-MIT
- LICENSE-APACHE
- NOTICE
- ATTRIBUTION.md

Important restrictions:

- Preserve required copyright and license notices.
- Review third-party dependency licenses.
- Review asset-specific licenses.
- Do not reuse protected trademarks or logos without permission.
- Record modifications to reused components.

Source-code licensing does not automatically grant trademark rights.

## 7. Reuse Assessment

| Component | Initial assessment |
|---|---|
| Rust analysis libraries | Candidate for technical review |
| Rust engine | Candidate for server-side adaptation |
| CLI | Reference for workflow behavior |
| Desktop egui interface | Not suitable as the Android UI |
| WebAssembly viewer | Requires separate compatibility review |
| Branding and logos | Do not reuse without permission |

No component is approved for production reuse yet.

## 8. Security Review

A complete security audit remains pending.

The following areas require source-level inspection:

- AI agent execution.
- External URL processing.
- File system access.
- Command execution.
- MCP tool permissions.
- Network access.
- Dependency vulnerabilities.
- Worker isolation.

IDRICI CRAFT must execute untrusted operations in isolated environments.

## 9. IDRICI CRAFT Integration Direction

The planned independent architecture remains:

- Android client.
- Backend API.
- Task orchestrator.
- AI integration layer.
- Isolated execution workers.
- Database and file storage.

The upstream Rust engine may provide reusable technical components after compatibility, security, and license review.

The IDRICI CRAFT interface and branding remain independently designed.

## 10. Remaining Audit Work

- Inspect the engine crate implementation.
- Inspect AI agent integration.
- Inspect MCP tool execution.
- Inspect file and process operations.
- Review dependency licenses.
- Review security-sensitive code paths.
- Test candidate components before reuse.

## 11. Audit Status

Status: IN PROGRESS

Initial repository structure and technology identification: COMPLETED.

Detailed source-level security review: NOT STARTED.

Component compatibility testing: NOT STARTED.

Production reuse approval: NOT APPROVED.

This report distinguishes verified repository observations from pending technical assessments.

---

Project: IDRICI CRAFT
Repository: Idrici2027/idricraftici
Branch: main
