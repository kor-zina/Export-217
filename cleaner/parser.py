from cleaner.aliases import ClassName, FilePath
from bs4 import BeautifulSoup, Tag


def get_soup(filepath: FilePath) -> BeautifulSoup:
    with open(filepath, "r", encoding="utf-8") as f:
        return BeautifulSoup(f, "html.parser")


def get_history(soup: BeautifulSoup):
    body = soup.body
    if body is None:
        return None

    page_wrap = body.find("div", class_="page_wrap")
    if page_wrap is None:
        return None

    page_body = page_wrap.find("div", class_="page_body chat_page")
    if page_body is None:
        return None

    history = page_body.find("div", class_="history")

    return history


def get_classes(element: Tag) -> ClassName:
    # Only process tags (skip strings, comments, etc.)
    if not getattr(element, "attrs", None):
        return None

    class_list = element.get("class")
    if not class_list:
        return None

    return " ".join(sorted(class_list))


def get_subclasses(element: Tag) -> tuple[ClassName]:
    classes: set[ClassName] = set()
    for subelement in element.find_all(recursive=False):
        new_classes = get_classes(subelement)
        classes.add(new_classes)
    return tuple(sorted(classes))


def get_message_classes(filepath: FilePath) -> set[ClassName]:
    soup = get_soup(filepath)
    history = get_history(soup)

    classes = set()
    for element in history.find_all(recursive=False):
        classes.add(get_classes(element))

    return classes


def get_message_body_element_classes(filepath: FilePath) -> set[tuple[ClassName]]:
    soup = get_soup(filepath)
    history = get_history(soup)

    body_classes: set[tuple[ClassName]] = set()
    for message in history.find_all(recursive=False):
        for child in message.children:
            if getattr(child, "attrs", None) is None:
                continue
            if "body" not in child["class"]:
                continue
            body_classes.add(get_subclasses(child))

    return body_classes
