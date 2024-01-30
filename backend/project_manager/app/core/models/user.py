from sqlalchemy.orm import Mapped, mapped_column

from backend.project_manager.app.core.models.base import Base
from backend.project_manager.app.core.models.mixins import (
    CreationDateMixin,
    IdMixin,
    LevelMixin,
)


class User(
    Base,
    IdMixin,
    CreationDateMixin,
    LevelMixin,
):
    # email: Mapped[str] = mapped_column(
    #     nullable=False,
    #     unique=True,
    # )
    tg_id: Mapped[int] = mapped_column(
        nullable=False,
        unique=True,
    )

    email: Mapped[str | None] = mapped_column(
        nullable=True,
        unique=True,
    )

    phone_number: Mapped[str | None] = mapped_column(
        nullable=True,
        unique=True,
    )

    # TODO: add password: Mapped[str] = mapped_column(nullable=False)

    surname: Mapped[str] = mapped_column(
        nullable=False,
    )

    name: Mapped[str] = mapped_column(
        nullable=False,
    )

    middle_name: Mapped[str | None] = mapped_column(
        nullable=True,
    )

    donation_amount: Mapped[int | None] = mapped_column(
        nullable=False,
        default=0,
    )

    investment_amount: Mapped[int | None] = mapped_column(
        nullable=False,
        default=0,
    )
