from adapters.gateways.security import SecurityGateway

class JWTProvider(SecurityGateway):
    """Implementación concreta de JWT - Capa Frameworks"""
    
    def __init__(self, secret_key: str):
        self.secret_key = secret_key
    
    def verify_token(self, token: str) -> bool:
        """
        Verifica si el token JWT es válido
        """
        # Implementación simple - en producción usar biblioteca JWT
        return token == self.secret_key