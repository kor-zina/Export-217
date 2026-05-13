import asyncio

from export217_shared.db.base import Base
from export217_shared.db.engine import engine

# IMPORTANT:
# Import all models so SQLAlchemy registers them
from export217_shared.db.models import *  # noqa: F403


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main() -> None:
    await init_db()


if __name__ == "__main__":
    asyncio.run(main())