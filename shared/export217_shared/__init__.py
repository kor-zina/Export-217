from sqlalchemy import select

from export217_shared.db.models.user import User
from export217_shared.db.session import SessionFactory
from export217_shared.db.engine import engine
from export217_shared.db.base import Base

async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def insert_users(users: list[User]) -> None:
    async with SessionFactory() as session:
        for user in users:
            session.add(user)
        await session.commit()

async def get_users() -> list[User]:
    async with SessionFactory() as session:
        users = await session.execute(select(User))
    return users.scalars().all()

async def hello_db() -> None:
    await init_db()

    await insert_users([User(telegram_name="Beltaine")])
    for user in await get_users():
        print(f"{user.id}\t{user.telegram_name}")
