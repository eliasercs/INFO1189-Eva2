from adapters.presenters.beverage_presenter import BebidaPresenter
from adapters.gateways.beverage_repository import BebidaRepository

class ActualizarStockBebidaUseCase:
    def __init__(self, repository : BebidaRepository):
        self.repository = repository
    
    def execute(self, bebida_id: int, nuevo_stock: int) -> dict:
        """
        Actualiza el stock de una bebida
        """
        # Validaciones
        if nuevo_stock < 0:
            return {"success": False, "msg": "El stock no puede ser negativo"}
        
        # Verificar que existe
        bebida_existente = self.repository.obtener_bebida_por_id(bebida_id)
        if not bebida_existente:
            return {"success": False, "msg": f"Bebida con ID {bebida_id} no encontrada"}
        
        # Actualizar stock
        resultado = self.repository.actualizar_stock(bebida_id, nuevo_stock)
        if not resultado:
            return {"success": False, "msg": "Error al actualizar el stock"}
        
        return BebidaPresenter.present_bebida(resultado)