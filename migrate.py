#!/usr/local/bin/python
import asyncio

from src.color_palettes.entity import ColorPalette  # noqa: F401
from src.photo_stats.entity import PhotoStat  # noqa: F401
from src.photos.entity import Photo  # noqa: F401
from src.shared.infrastructure.persistence.sqlalchemy.model import Base
from src.shared.infrastructure.persistence.sqlalchemy.session import engine


async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(create_all())
