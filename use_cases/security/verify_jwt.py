from adapters.gateways.security import SecurityGateway

class VerifyAuthUseCase:
    def __init__(self, security_gateway: SecurityGateway):
        self.security_gateway = security_gateway
    
    def execute(self, authorization_header: str) -> bool:
        """
        Verifica si el header de autorización es válido
        """
        if not authorization_header:
            return False
        
        # Extraer el token del header "Bearer {token}"
        parts = authorization_header.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return False
        
        token = parts[1]
        return self.security_gateway.verify_token(token)