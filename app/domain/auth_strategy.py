#Patron Strategy
from abc import ABC, abstractclassmethod
from app.domain.user import User

class AuthStrategy(ABC):
    @abstractclassmethod
    def authenticate(self, user: User):
        pass
class JWTStrategy(AuthStrategy):
    def authenticate(slef, user: User):
        return f"jwt-token-for-{user.username}"
    
class SessionStrategy(AuthStrategy):
    def authenticate(self, user: User):
        return f"session-cookie-for-{user.username}"