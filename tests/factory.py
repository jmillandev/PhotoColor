from factory.alchemy import SQLAlchemyModelFactory  # type: ignore[import-untyped]
from kink import di
from sqlalchemy.ext.asyncio import AsyncSession


class SQLAlchemyFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = None

        @staticmethod
        def sqlalchemy_session_factory():
            return di[type[AsyncSession]]()  # Sessionmaker

    @classmethod
    async def _create(cls, model_class, *args, **kwargs):
        instance = super()._create(model_class, *args, **kwargs)
        async with cls._meta.sqlalchemy_session as session:
            await session.commit()
        return instance
