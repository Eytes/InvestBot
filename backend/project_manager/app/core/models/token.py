from uuid import UUID

from backend.project_manager.app.core.models.base import Base
from backend.project_manager.app.core.models.mixins import (
    CreationDateMixin,
    IdMixin,
    LevelMixin,
)
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Token(
    Base,
    IdMixin,
    LevelMixin,
):
    project_id: Mapped[UUID] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
    )

    user_id: Mapped[UUID | None] = mapped_column(
        ForeignKey("users.id"),
        nullable=True,
    )

    weight: Mapped[int] = mapped_column(
        nullable=False,
        default=1,
    )

    price: Mapped[int] = mapped_column(
        nullable=False,
    )
