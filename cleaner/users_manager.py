from pydantic import BaseModel
from cleaner.type_aliases import UserRole, UserName

ROLES = [
    'bot', 'reader', 'player', 'master'
]

class User(BaseModel):
    name: UserName
    pseudonyms: list[UserName]
    Role: UserRole

def foo():
    print("You're good to go")