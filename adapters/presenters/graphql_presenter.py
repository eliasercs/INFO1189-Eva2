from datetime import datetime
from typing import Optional

class GraphQLPresenter:
    """Presentador específico para respuestas GraphQL"""
    
    @staticmethod
    def present_bebida(bebida) -> Optional[dict]:
        """Convierte objeto Bebida a formato GraphQL"""
        if not bebida:
            return None
        
        return {
            "id": bebida.id,
            "codigo": bebida.codigo,
            "nombre": bebida.nombre,
            "marca": bebida.marca,
            "precio": bebida.precio,
            "stock": bebida.stock,
            "categoriaId": bebida.categoria_id,
            "createdAt": GraphQLPresenter._format_datetime(bebida.created_at),
            "updatedAt": GraphQLPresenter._format_datetime(bebida.updated_at)
        }
    
    @staticmethod
    def present_use_case_result(resultado) -> dict:
        """Convierte resultado del use case a formato GraphQL"""
        # Si es un objeto Bebida (éxito)
        if hasattr(resultado, 'id'):
            return {
                "success": True,
                "data": GraphQLPresenter.present_bebida(resultado),
                "msg": "Operación exitosa"
            }
        
        # Si ya es un diccionario con estructura de error
        if isinstance(resultado, dict) and resultado.get("success") is False:
            return resultado
        
        # Si es un diccionario con estructura de éxito
        if isinstance(resultado, dict) and resultado.get("success") is True:
            return resultado
        
        # Caso inesperado
        return {"success": False, "msg": "Tipo de respuesta inesperado"}
    
    @staticmethod
    def _format_datetime(dt: datetime) -> str:
        """Formatea datetime para GraphQL"""
        if not dt:
            return None
        return dt.isoformat()