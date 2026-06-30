from sqlalchemy.ext.asyncio import create_async_engine

from export217_shared.db.config import settings

engine = create_async_engine(
    settings.DB_URL,
    echo=True,
)