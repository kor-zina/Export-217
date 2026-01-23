from cleaner import users_manager, utils, parser
from dotenv import load_dotenv

# Environment variables from .env file
load_dotenv()

# Before proceeding, clean_export must be emptied
utils.empty_clean_export_folder()

# Now go
users_manager.foo()

# Wtf I am checking
parser.get_user_list()