from dataclasses import dataclass
from typing import Self
from uuid import UUID, uuid4

from kink import inject
from sqlalchemy import Column, ForeignKey, Integer, Uuid, func, select
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
    photo_id = Column(Uuid, ForeignKey("photos.id", ondelete="CASCADE"))

    @classmethod
    def calculate(cls, photo_id: UUID, red: int, green: int, blue: int) -> Self:
        return cls(id=uuid4(), photo_id=photo_id, red=red, green=green, blue=blue)

    @classmethod
    @inject
    async def avg(cls, sessionmaker: type[AsyncSession]) -> RgbStat:
        # TODO: Move to infrastructure layer as a Repository
        query = select(
            cls,
            func.round(func.avg(cls.red)).label("red"),
            func.round(func.avg(cls.green)).label("green"),
            func.round(func.avg(cls.blue)).label("blue"),
        )
        async with sessionmaker() as session:
            result = await session.execute(query)
            data = result.one()
        try:
            return RgbStat(
                red=int(data.red), green=int(data.green), blue=int(data.blue)
            )
        except TypeError:
            return RgbStat(red=0, green=0, blue=0)

    @inject
    async def save(self, sessionmaker: type[AsyncSession]) -> None:
        # TODO: Move to infrastructure layer as a Repository
        async with sessionmaker() as session:
            session.add(self)
            await session.commit()
