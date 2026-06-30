from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from export217_shared.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_name: Mapped[str]
