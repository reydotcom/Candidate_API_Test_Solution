from sqlalchemy.orm import Mapped, mapped_column
from typing import Annotated

from db.database import Base


intpk = Annotated[int, mapped_column(primary_key=True)]


class AraratInfo(Base):
    __tablename__ = 'ararat_info'
    id: Mapped[intpk]
    text: Mapped[str]


class Cities(Base):
    __tablename__ = 'cities'
    id: Mapped[intpk]
    name: Mapped[str]
    population: Mapped[int]


class Dishes(Base):
    __tablename__ = 'dishes'
    id: Mapped[intpk]
    name: Mapped[str]
