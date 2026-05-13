from sqlalchemy.ext.asyncio import async_sessionmaker

from export217_shared.db.engine import engine

SessionFactory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)