from typing import Self
from uuid import UUID, uuid4

from kink import inject
from sqlalchemy import Column, String, Uuid, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy_file import FileField

# TODO: Ilegal import - Infrastructure layer should not import from domain layer
from src.shared.infrastructure.persistence.sqlalchemy.model import Base


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Uuid, primary_key=True)
    filename = Column(String(50))
    asset = Column(FileField)

    @classmethod
    def upload(cls, filename: str, asset: bytes) -> Self:
        return cls(
            asset=asset, id=uuid4(), filename=filename  # TODO: Use FilenameGenerator
        )
        # TODO: Record Event PhotoUploded

    @inject
    async def save(self, sessionmaker: type[AsyncSession]) -> None:
        # TODO: Move to infrastructure layer - PhotoRepository
        async with sessionmaker() as session:
            session.add(self)
            await session.commit()

    @classmethod
    @inject
    async def delete(cls, id: UUID, sessionmaker: type[AsyncSession]) -> None:
        # TODO: Move to infrastructure layer - PhotoRepository
        async with sessionmaker() as session:
            await session.execute(delete(cls).where(cls.id == id))
            await session.commit()

    @classmethod
    @inject
    async def find(cls, id: UUID, sessionmaker: type[AsyncSession]) -> Self:
        # TODO: Move to infrastructure layer - PhotoRepository
        async with sessionmaker() as session:
            return await session.get(cls, id)
