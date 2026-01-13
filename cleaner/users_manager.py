from pydantic import BaseModel
from cleaner.type_aliases import UserType, UserName

USER_TYPES = [
    'bot', 'reader', 'player', 'master'
]

class User(BaseModel):
    name: UserName
    pseudonyms: list[UserName]
    type: UserType

def foo():
    print("You're good to go")