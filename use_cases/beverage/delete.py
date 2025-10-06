from adapters.gateways.beverage_repository import BebidaRepository

class EliminarBebidaUseCase:
    def __init__(self, repository: BebidaRepository):
        self.repository = repository
    
    def execute(self, bebida_id: int) -> dict:
        """
        Elimina una bebida por ID
        """
        # Verificar que existe
        bebida_existente = self.repository.obtener_bebida_por_id(bebida_id)
        if not bebida_existente:
            return {"success": False, "msg": f"Bebida con ID {bebida_id} no encontrada"}
        
        # Eliminar
        eliminado = self.repository.eliminar(bebida_id)
        if not eliminado:
            return {"success": False, "msg": "Error al eliminar la bebida"}
        
        return {
            "success": True, 
            "msg": f"Bebida {bebida_id} eliminada correctamente",
            "data": {
                "id": bebida_id,
                "eliminado": True
            }
        }