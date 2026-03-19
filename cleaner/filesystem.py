import os, re

from cleaner.aliases import FileName, FilePath


def empty_clean_export_folder(files_to_spare: list[FileName] = []) -> None:
    clean_export = os.getenv("CLEAN_EXPORT")

    for filename in os.listdir(clean_export):
        if filename in files_to_spare:
            continue

        file_path = os.path.join(clean_export, filename)

        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # TODO: recursive subfolder removal
        except Exception as e:
            print(f"Failed to delete {file_path}\nReason:\n{e}")
    print(f"clean_export folder has been cleaned.")


def sort_key(filename):
    if filename == "messages.html":
        return 0
    match = re.search(r"messages(\d+)\.html", filename)
    return int(match.group(1) if match else float("inf"))


def get_all_filepaths() -> list[FilePath]:

    messages_htmls = []

    baseline_export = os.getenv("BASELINE_EXPORT")

    filenames = [
        filename
        for filename in os.listdir(baseline_export)
        if re.search("messages\d*.html", filename) is not None
    ]

    filenames.sort(key=sort_key)

    for filename in filenames:
        if re.search("messages\d*.html", filename) is None:
            continue

        file_path = os.path.join(baseline_export, filename)

        if not os.path.isfile(file_path):
            continue

        messages_htmls.append(file_path)

    return messages_htmls
