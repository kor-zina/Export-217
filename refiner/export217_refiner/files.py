import re
from pathlib import Path

from bs4 import BeautifulSoup

from export217_shared.settings import settings  # pyright: ignore[reportMissingImports]


def get_sorted_message_paths() -> list[Path]:
    """Returns a list of Path objects sorted numerically by their index."""
    pattern = re.compile(r"^messages(?:(\d+))?\.html$")

    # Sort key
    def extract_index(path: Path) -> int:
        match = pattern.match(path.name)
        index_str = match.group(1)
        return int(index_str) if index_str else 1

    matched_files = [
        p
        for p in settings.LOCAL_DATA.iterdir()
        if p.is_file() and pattern.match(p.name)
    ]

    return sorted(matched_files, key=extract_index)


def read_users_from_file(path: Path) -> set[str]:
    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Step 1: navigate explicitly and defensively
    body = soup.body
    if body is None:
        return set()

    page_wrap = body.find("div", class_="page_wrap")
    if page_wrap is None:
        return set()

    page_body = page_wrap.find("div", class_="page_body chat_page")
    if page_body is None:
        return set()

    history = page_body.find("div", class_="history")
    if history is None:
        return set()

    # Step 2: collect classes
    users = set()

    for message in history.children:
        if message == "\n":
            continue

        m_body = message.find("div", class_="body")
        if m_body is None:
            continue

        from_name = m_body.find("div", class_="from_name")
        if from_name is None:
            continue

        forwarded = m_body.find(
            "div", class_=lambda c: c and "forwarded" in c and "body" in c
        )
        if forwarded is not None:
            continue

        raw_nickname = from_name.find(string=True, recursive=False)

        via_pattern = r"\bvia\s+@\S+"
        raw_nickname = re.sub(via_pattern, "", raw_nickname)

        datetime_pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}"
        raw_nickname = re.sub(datetime_pattern, "", raw_nickname)

        users.add(raw_nickname.strip())

    return users
