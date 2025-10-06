from entities.beverage import Bebida
from entities.category import Categoria
from entities.grados_alcohol import GradoAlcohol
from typing import Dict, Any, List


class BebidaPresenter:
    @staticmethod
    def present_bebida_completa(bebida_data: Dict[str, Any]) -> Dict[str, Any]:
        
        if not bebida_data:
            return {
                "success": False,
                "data": {},
                "message": "Bebida no encontrada",
                "error_code": "BEBIDA_NO_ENCONTRADA"
            }
        
        grado = GradoAlcohol(
            id=bebida_data["grado_alcohol_id"],
            nombre=bebida_data["grado_alcohol_nombre"],
            descripcion=bebida_data["grado_alcohol_description"],
            horario_limite_venta=bebida_data["grado_alcohol_horario_limite"]
        )
        
        categoria = Categoria(
            id=bebida_data["categoria_id"],
            nombre=bebida_data["categoria_nombre"],
            tipo_grado_id=bebida_data["categoria_tipo_grado"],
            grado_alcohol=grado,
            restriction_edad=bool(bebida_data["categoria_restriction_edad"])
        )
        
        bebida_formateada = Bebida(
            id=bebida_data["id"],
            codigo=bebida_data["codigo"],
            nombre=bebida_data["nombre"],
            marca=bebida_data["marca"],
            precio=bebida_data["precio"],
            stock=bebida_data["stock"],
            categoria_id=bebida_data["categoria_id"],
            categoria=categoria,
            created_at=bebida_data.get("created_at"),
            updated_at=bebida_data.get("updated_at"))
        
        return bebida_formateada
    
    @staticmethod
    def present_bebida(bebida_data: Dict[str, Any]) -> Dict[str, Any]:
        
        if not bebida_data:
            return {
                "success": False,
                "data": {},
                "message": "Bebida no encontrada",
                "error_code": "BEBIDA_NO_ENCONTRADA"
            }
            
        return bebida_data
    @staticmethod
    def to_graphql(bebida: Bebida) -> dict:
        # Misma entidad, diferente formato para GraphQL
        return {
            "id": bebida.id,
            "nombre": bebida.nombre,
            "precio": bebida.precio,
            "stockActual": bebida.stock,  # ← Diferente nombre para GraphQL
            "disponible": bebida.tiene_stock()
        }