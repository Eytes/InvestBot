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
    tg_id: Mapped[int] = mapped_column(
        nullable=False,
        unique=True,
        comment="Telegram ID",
    )

    email: Mapped[str | None] = mapped_column(
        nullable=True,
        unique=True,
        comment="Электронная почта",
    )

    phone_number: Mapped[str | None] = mapped_column(
        nullable=True,
        unique=True,
        comment="Номер телефона",
    )

    # TODO: add password: Mapped[str] = mapped_column(nullable=False)

    surname: Mapped[str] = mapped_column(
        nullable=False,
        comment="Фамилия",
    )

    name: Mapped[str] = mapped_column(
        nullable=False,
        comment="Имя",
    )

    middle_name: Mapped[str | None] = mapped_column(
        nullable=True,
        comment="Отчество",
    )

    donation_amount: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        comment="Общая сумма всех пожертвований в проекты",
    )

    investment_amount: Mapped[int] = mapped_column(
        nullable=False,
        default=0,
        comment="Общая сумма всех инвестиций в проекты",
    )
