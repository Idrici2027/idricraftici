Idricraftici

An Android-first client and server platform inspired by Craft Anything.

Idricraftici aims to bring project inspection and AI-assisted rebuilding to Android users. The Android app will provide the interface, while a separate server will execute demanding operations.

«Status: Initial planning and architecture stage. Features are not yet implemented.»

Vision

The intended workflow:

1. Study — inspect a website, application, repository, or project.
2. Plan — prepare an implementation plan.
3. Build — use an AI coding agent to create a new project.
4. Check — compare the result with the original target.
5. Refine — improve the implementation based on findings.

Architecture

- Android client: Mobile interface and task monitoring.
- Backend API: Authentication and task management.
- Rust engine: Compatible components adapted from the upstream engine after technical review.
- Execution workers: Isolated server environments for demanding operations.
- AI coding agent: Integration with supported coding agents.

Upstream project

Technical reference: https://github.com/storytold/craft-anything

Idricraftici is a separate project. All reused code and assets must comply with their licenses and trademark restrictions. Required copyright and license notices will be preserved.

Planned repository structure

idricraftici/
├── android_app/
├── backend/
├── engine/
├── workers/
├── docs/
└── README.md

Development roadmap

- [x] Create the GitHub repository.
- [x] Define the initial project direction.
- [ ] Audit the upstream source and dependencies.
- [ ] Finalize architecture and security.
- [ ] Implement the backend.
- [ ] Integrate compatible Rust components.
- [ ] Build the Android application.
- [ ] Test the complete system.

Development principles

- Build and review one file at a time.
- Keep Android, backend, and engine components separate.
- Never expose API keys or server credentials in the APK.
- Execute untrusted tasks in isolated environments.
- Never describe planned features as completed features.
