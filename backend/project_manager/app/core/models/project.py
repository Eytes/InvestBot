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
    short_info: Mapped[str | None] = mapped_column(
        nullable=True,
    )

    # TODO: add image cover field

    stage: Mapped[str | None] = mapped_column(
        nullable=True,
    )

    full_info: Mapped[str | None] = mapped_column(
        nullable=True,
    )

    targets: Mapped[list[str] | None] = mapped_column(
        nullable=True,
    )

    links: Mapped[dict | None] = mapped_column(
        nullable=True,
    )

    tokens_avalaible: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
    )

    tokens_total: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
    )

    # TODO: add presentation file field
