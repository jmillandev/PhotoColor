from typing import NamedTuple, Optional, Self
from uuid import UUID, uuid4  # TODO: Create interface and UUID4 implementation

from kink import inject
from sqlalchemy import Column, ForeignKey, String, Uuid, select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

# TODO: Ilegal import - Infrastructure layer should not import from domain layer
from src.shared.infrastructure.persistence.sqlalchemy.model import Base


class Colors(NamedTuple):
    color1: str  # TODO: Use ValueObject to validate formats
    color2: str
    color3: str
    color4: str
    color5: str


class ColorPalette(Base):
    __tablename__ = "color_palettes"

    id = Column(Uuid, primary_key=True)
    # TODO: TODO: We can store the colors as a list(or json) in a single column.
    # Its closer to the domain model and how our client will use it
    color1 = Column(String(7))
    color2 = Column(String(7))
    color3 = Column(String(7))
    color4 = Column(String(7))
    color5 = Column(String(7))

    photo_id = Column(Uuid, ForeignKey("photos.id", ondelete="CASCADE"))

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
    async def find_by_photo_id(
        cls, id: UUID, sessionmaker: type[AsyncSession]
    ) -> Optional[Self]:
        # TODO: Move to infrastructure layer - ColorPaletteRepository
        async with sessionmaker() as session:
            query = select(cls).where(cls.photo_id == id)
            result = await session.execute(query)
            try:
                return result.scalar_one()
            except NoResultFound:
                return None

    @property
    def colors(self) -> Colors:
        return Colors(
            color1=str(self.color1),
            color2=str(self.color2),
            color3=str(self.color3),
            color4=str(self.color4),
            color5=str(self.color5),
        )
