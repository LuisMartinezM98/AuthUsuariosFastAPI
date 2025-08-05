#Patron Repository
from app.domain.user import User
from typing import Optional

class UserRepository:
    _users_db = [
        User(id=1, username="JohnDoe", password="123456"),
        User(id=2, username="JaneDoe", password="123456"),
    ]

    def get_by_username(self, username: str) -> Optional[User]:
        return next((u for u in self._users_db if u.username == username), None)