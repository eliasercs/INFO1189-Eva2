from adapters.presenters.beverage_presenter import BebidaPresenter
from adapters.gateways.beverage_repository import BebidaRepository
from entities.beverage import Bebida

class ActualizarBebidaUseCase:
    def __init__(self, repository: BebidaRepository):
        self.repository = repository
    
    def execute(self, bebida_id: int, datos_completos: dict) -> dict:
        """
        Actualiza TODOS los campos de una bebida (PUT)
        """
        # Validaciones
        campos_requeridos = ["codigo", "nombre", "precio", "stock", "categoria_id"]
        for campo in campos_requeridos:
            if campo not in datos_completos:
                return {"success": False, "msg": f"Campo requerido: {campo}"}
        
        if datos_completos.get('precio', 0) <= 0:
            return {"success": False, "msg": "El precio debe ser mayor a 0"}
        
        if datos_completos.get('stock', 0) < 0:
            return {"success": False, "msg": "El stock no puede ser negativo"}
        
        # Verificar que existe
        bebida_existente = self.repository.obtener_bebida_por_id(bebida_id)
        if not bebida_existente:
            return {"success": False, "msg": f"Bebida con ID {bebida_id} no encontrada"}
        
        # Crear objeto Bebida actualizado
        bebida_actualizada = Bebida(
            id=bebida_id,
            codigo=datos_completos['codigo'],
            nombre=datos_completos['nombre'],
            marca=datos_completos.get('marca', ''),
            precio=datos_completos['precio'],
            stock=datos_completos['stock'],
            categoria_id=datos_completos['categoria_id'],
            created_at=bebida_existente.created_at,  # Mantener fecha creación original
            updated_at=None  # Se actualizará en el repository
        )
        
        # Actualizar
        resultado = self.repository.actualizar(bebida_actualizada)
        if not resultado:
            return {"success": False, "msg": "Error al actualizar la bebida"}
        
        return BebidaPresenter.present_bebida(resultado)