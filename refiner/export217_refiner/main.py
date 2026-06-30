import asyncio

from sqlalchemy import select

from export217_shared.db.base import Base
from export217_shared.db.engine import engine
from export217_shared.db.models.user import User
from export217_shared.db.session import SessionFactory


async def main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with SessionFactory() as session:
        user = User(
            telegram_name="Beltaine",
        )

        session.add(user)

        await session.commit()

    async with SessionFactory() as session:
        result = await session.execute(select(User))

        users = result.scalars().all()

        for user in users:
            print(user.id, user.telegram_name)


if __name__ == "__main__":
    asyncio.run(main())
