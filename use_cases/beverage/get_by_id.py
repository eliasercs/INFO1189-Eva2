from typing import List, Dict, Any
from adapters.gateways.beverage_repository import BebidaReadRepository

class ObtenerBebidaCompletaPorIdUseCase:
    def __init__(self, bebida_repository: BebidaReadRepository):
        self.bebida_repository = bebida_repository
    
    def execute(self, bebida_id: int) -> Dict[str, Any]:
        """
        Obtiene una bebida específica con información de categoría y grado de alcohol
        """
        bebida = self.bebida_repository.obtener_bebida_por_id(bebida_id)
        if not bebida:
            raise ValueError(f"Bebida con ID {bebida_id} no encontrada")
        return bebida