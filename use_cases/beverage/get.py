from typing import List, Dict, Any
from adapters.gateways.beverage_repository import BebidaReadRepository

class ObtenerBebidasUseCase:
    def __init__(self, bebida_repository: BebidaReadRepository):
        self.bebida_repository = bebida_repository
    
    def execute(self) -> Dict[str, Any]:
        """
        Obtiene una bebida específica con información de categoría y grado de alcohol
        """
        bebida = self.bebida_repository.obtener_bebidas()
        if not bebida:
            raise ValueError(f"Bebidas no encontradas")
        return bebida