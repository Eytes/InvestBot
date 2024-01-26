from sqlalchemy.orm import Mapped, mapped_column

from backend.project_manager.app.core.models.base import Base
from backend.project_manager.app.core.models.mixins import (
    CreationDateMixin,
    IdMixin,
    LevelMixin,
)


class Project(
    Base,
    IdMixin,
    CreationDateMixin,
    LevelMixin,
):
    info: Mapped[str] = mapped_column(
        nullable=True,
    )

    stage: Mapped[str] = mapped_column(
        nullable=True,
    )

    description: Mapped[str] = mapped_column(
        nullable=True,
    )
