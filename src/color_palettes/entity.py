from typing import NamedTuple, Self
from uuid import UUID, uuid4  # TODO: Create interface and UUID4 implementation

from kink import inject
from sqlalchemy import Column, String, Uuid
from sqlalchemy.ext.asyncio import AsyncSession

# TODO: Ilegal import - Infrastructure layer should not import from domain layer
from src.shared.infrastructure.persistence.sqlalchemy.model import Base


class Colors(NamedTuple):
    color1: str
    color2: str
    color3: str
    color4: str
    color5: str


class ColorPalette(Base):
    __tablename__ = "color_palettes"

    id = Column(Uuid, primary_key=True)
    color1 = Column(String(6))
    color2 = Column(String(6))
    color3 = Column(String(6))
    color4 = Column(String(6))
    color5 = Column(String(6))
    photo_id = Column(Uuid)  # TODO: Add foreign key to photo

    @classmethod
    def generate(cls, photo_id: UUID, colors: Colors) -> Self:
        return cls(
            id=uuid4(),
            photo_id=photo_id,
            color1=colors[0],
            color2=colors[1],
            color3=colors[2],
            color4=colors[3],
            color5=colors[4],
        )

    @inject
    async def save(self, sessionmaker: type[AsyncSession]) -> None:
        # TODO: Move to infrastructure layer - ColorPaletteRepository
        async with sessionmaker() as session:
            session.add(self)
            await session.commit()

    @classmethod
    @inject
    async def find_by_photo_id(cls, id: UUID, sessionmaker: type[AsyncSession]) -> Self:
        # TODO: Move to infrastructure layer - ColorPaletteRepository
        async with sessionmaker() as session:
            return await session.query(cls).filter_by(photo_id=id).first()
