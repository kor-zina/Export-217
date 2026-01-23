from cleaner.utils import get_all_messages
from bs4 import BeautifulSoup

def get_user_list():
    messages_htmls = get_all_messages()
    
