import asyncio

from tqdm import tqdm

from export217_shared.db.models.user import User  # pyright: ignore[reportMissingImports]
from export217_refiner.files import get_sorted_message_paths, read_users_from_file  # pyright: ignore[reportMissingImports]


async def read_users_from_html() -> list[User]:
    file_paths = get_sorted_message_paths()
    users: list[str] = set()
    for path in tqdm(file_paths, desc="Parsing users", unit="file"):
        users.update(read_users_from_file(path))
    return users


async def main() -> None:
    users = await read_users_from_html()
    # with open("/home/kor-zina/dev-projects/Export217/users.txt", mode="w", encoding="UTF-8") as file:
    #     file.writelines([u + "\n" for u in users])


if __name__ == "__main__":
    asyncio.run(main())
