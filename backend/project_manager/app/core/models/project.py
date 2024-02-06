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
        comment="Короткое описание проекта",
    )

    # TODO: add image cover field

    stage: Mapped[str | None] = mapped_column(
        nullable=True,
        comment="Стадия проекта",
    )

    full_info: Mapped[str | None] = mapped_column(
        nullable=True,
        comment="Полная информация о проекте",
    )

    targets: Mapped[list[str] | None] = mapped_column(
        nullable=True,
        comment="Цели проекта",
    )

    links: Mapped[dict | None] = mapped_column(
        nullable=True,
        comment="Ссылки на социальные сети и сайты проекта",
    )

    tokens_avalaible: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        comment="Количество доступных к покупке токенов проекта",
    )

    tokens_total: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        comment="Общее количество токенов проекта",
    )

    # TODO: add presentation file field
