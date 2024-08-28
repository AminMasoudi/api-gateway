from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.schema import PrimaryKeyConstraint


class Base(
    DeclarativeBase
    ):
    ...

class Backend(Base):
    __tablename__ = "Backends"
    __table_args__ = (
        PrimaryKeyConstraint("id"),
    )

    id:Mapped[int]
    host: Mapped[str]
    path: Mapped[str]
    service: Mapped[str] 