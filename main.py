from cleaner import filesystem, parser
from dotenv import load_dotenv

from cleaner.aliases import FileName, UserName
from cleaner.messages import joined_classes

# Environment variables from .env file
load_dotenv()

# Before proceeding, clean_export must be emptied
filesystem.empty_clean_export_folder()

# What's is inside
filepaths: list[FileName] = filesystem.get_all_filepaths()