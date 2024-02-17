#!/usr/local/bin/python
from src.shared.infrastructure.persistence.sqlalchemy.model import Base
from src.shared.infrastructure.persistence.sqlalchemy.session import engine


async def create_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


import asyncio

if __name__ == "__main__":
    asyncio.run(create_all())
