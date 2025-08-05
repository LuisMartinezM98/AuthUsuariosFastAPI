#Serviec Layer + Strategy Pattern
from app.domain.auth_strategy import AuthStrategy
from app.repositories.user_repository import UserRepository

class AuthService:
    def __init__(self, strategy: AuthStrategy, user_repo: UserRepository):
        self.strategy = strategy
        self.user_repo = user_repo


    def login(self, username: str, password: str):
        user = self.user_repo.get_by_username(username)
        if not user or user.password != password:
            raise Exception("Invalid credentials")
        return self.strategy.authenticate(user)