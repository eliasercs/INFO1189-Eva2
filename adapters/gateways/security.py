from abc import ABC, abstractmethod

class SecurityGateway(ABC):
    """Interface para operaciones de seguridad"""
    
    @abstractmethod
    def verify_token(self, token: str) -> bool:
        pass