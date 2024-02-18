from dataclasses import dataclass
from typing import Self
from uuid import uuid4  # TODO: Create interface and UUID4 implementation

from kink import inject
from sqlalchemy import Column, Integer, Uuid, func, select, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession

# TODO: Ilegal import - Infrastructure layer should not import from domain layer
from src.shared.infrastructure.persistence.sqlalchemy.model import Base


@dataclass
class RgbStat:
    red: int
    green: int
    blue: int


class PhotoStat(Base):
    __tablename__ = "photo_stats"

    id = Column(Uuid, primary_key=True)
    red = Column(Integer)
    green = Column(Integer)
    blue = Column(Integer)
    photo_id = Column(Uuid, ForeignKey('photos.id', ondelete='CASCADE'))

    @classmethod
    def calculate(cls, photo_id: uuid4, red: int, green: int, blue: int) -> Self:
        return cls(id=uuid4(), photo_id=photo_id, red=red, green=green, blue=blue)

    @classmethod
    @inject
    async def avg(cls, sessionmaker: type[AsyncSession]) -> Self:
        # TODO: Move to infrastructure layer as a Repository
        query = select(
            cls,
            func.round(func.avg(cls.red)).label("red"),
            func.round(func.avg(cls.green)).label("green"),
            func.round(func.avg(cls.blue)).label("blue"),
        )
        async with sessionmaker() as session:
            result = await session.execute(query)
            return result.one()

    @inject
    async def save(self, sessionmaker: type[AsyncSession]) -> None:
        # TODO: Move to infrastructure layer as a Repository
        async with sessionmaker() as session:
            session.add(self)
            await session.commit()
