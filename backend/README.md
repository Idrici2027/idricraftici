
# IDRICI CRAFT Backend

The backend API for IDRICI CRAFT.

## Overview

This service provides the server-side foundation for the IDRICI CRAFT application.

It will handle:

- API endpoints for the Android application.
- AI agent orchestration.
- Project planning and generation workflows.
- Project validation and refinement.
- Database access and persistence.

## Technology Stack

- Python 3.11+
- FastAPI
- Pydantic
- SQLAlchemy
- PostgreSQL
- Alembic

## Development Setup

From the `backend` directory:

```bash
python -m venv .venv
```

Activate the virtual environment, then install the project:

```bash
pip install -e ".[dev]"
```

## Running the API

The application entry point will be:

```bash
uvicorn app.main:app --reload
```

## Testing

Run the test suite with:

```bash
pytest
```

## Code Quality

Run Ruff with:

```bash
ruff check .
```

## Project Status

The backend foundation is under development. API routes, AI orchestration, database models, and tests will be added incrementally.

## License

Proprietary. All rights reserved.
