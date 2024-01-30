from datetime import datetime
from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, declared_attr, mapped_column
from sqlalchemy import func


class IdMixin:
    """Примесь для моделей с ID"""

    _id_comment = "ID"

    @declared_attr
    def id(cls) -> Mapped[UUID]:
        return mapped_column(
            nullable=False,
            primary_key=True,
            default=uuid4,
            comment=cls._id_comment,
        )


class CreationDateMixin:
    """Примесь для моделей с датой создания"""

    _creation_date_comment: str = "Дата создания"
    _creation_date_nullable: bool = False

    @declared_attr
    def created_at(cls) -> Mapped[UUID]:
        return mapped_column(
            nullable=cls._creation_date_nullable,
            default=datetime.utcnow,
            server_default=func.now(),
            comment=cls._creation_date_comment,
        )


class LevelMixin:
    """Примесь для моделей с уровнем доступа"""

    _level_comment: str = "Уровень доступа"
    _level_nullable: bool = False

    @declared_attr
    def level(cls) -> Mapped[int]:
        return mapped_column(
            default=1,
            nullable=cls._level_nullable,
            comment=cls._level_comment,
        )
