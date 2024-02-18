#!/usr/local/bin/python
from src.shared.infrastructure.persistence.sqlalchemy.model import Base
from src.shared.infrastructure.persistence.sqlalchemy.session import engine

from src.photos.entity import Photo
from src.photo_stats.entity import PhotoStat
from src.color_palettes.entity import ColorPalette

async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


import asyncio

if __name__ == "__main__":
    asyncio.run(create_all())
