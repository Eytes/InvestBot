from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import ForeignKey

from backend.project_manager.app.core.models.base import Base
from backend.project_manager.app.core.models.mixins import (
    CreationDateMixin,
    IdMixin,
    LevelMixin,
)


class Token(
    Base,
    IdMixin,
    LevelMixin,
):
    project_id: Mapped[int] = mapped_column(
        ForeignKey("projects.id"),
        nullable=False,
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"),
    )

    weight: Mapped[int] = mapped_column(
        nullable=False,
        default=1,
    )

    price: Mapped[int] = mapped_column(
        nullable=False,
    )
