from sqlalchemy import pool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy import event
from src.shared.config import settings

engine = create_async_engine(
    str(settings.DATABASE_URI), echo=True, poolclass=pool.NullPool
)


def sessionmaker():
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


SqlAlchemySession = sessionmaker()

# TODO: Remove when implement another driver or when implement EventBus
@event.listens_for(engine.sync_engine, "connect")
def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute('PRAGMA foreign_keys = ON')
