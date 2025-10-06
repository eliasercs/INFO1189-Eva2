from adapters.presenters.beverage_presenter import BebidaPresenter
from adapters.gateways.beverage_repository import BebidaRepository
from entities.beverage import Bebida
from datetime import datetime

class CrearBebidaUseCase:
    def __init__(self, repository: BebidaRepository):
        self.repository = repository
    
    def execute(self, datos_bebida: dict) -> dict:
        """
        Crea una nueva bebida
        """
        # Validaciones
        if not datos_bebida.get('nombre'):
            return {"success": False, "msg": "El nombre es requerido"}
        
        if datos_bebida.get('precio', 0) <= 0:
            return {"success": False, "msg": "El precio debe ser mayor a 0"}
        
        if datos_bebida.get('stock', 0) < 0:
            return {"success": False, "msg": "El stock no puede ser negativo"}
        
        codigo_existente = self.repository.obtener_por_codigo(datos_bebida['codigo'])
        if codigo_existente is not None:
            return {
                "success": False, 
                "msg": f"Ya existe una bebida con el código '{datos_bebida['codigo']}'"
            }
        
        # Crear entidad Bebida
        bebida = Bebida(
            id=None,
            codigo=datos_bebida['codigo'],
            nombre=datos_bebida['nombre'],
            marca=datos_bebida.get('marca', ''),
            precio=datos_bebida['precio'],
            stock=datos_bebida.get('stock', 0),
            categoria_id=datos_bebida['categoria_id'],
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        
        # Guardar
        bebida_guardada = self.repository.guardar(bebida)
        
        if not bebida_guardada:
            return {"success": False, "msg": "Error al guardar la bebida"}
        
        return BebidaPresenter.present_bebida(bebida_guardada)