"""Task event database model for IDRICI CRAFT."""

from datetime import datetime

from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class TaskEvent(Base):
    """An event emitted during task execution."""

    __tablename__ = "task_events"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    task_id: Mapped[str] = mapped_column(
        String(36),
        ForeignKey("tasks.task_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    event: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    stage: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    progress: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    message: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[str | None] = mapped_column(
        String(40),
        nullable=True,
    )

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
        index=True,
    )
