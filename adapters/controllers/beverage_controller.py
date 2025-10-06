# beverage_controller.py
from fastapi import APIRouter, HTTPException, Depends, Header
from typing import Optional

class BeverageController:
    def __init__(self, crear_bebida_use_case, obtener_bebida_use_case, obtener_bebidas_use_case, actualizar_stock_use_case, eliminar_bebida_use_case, actualizar_bebida_use_case, verificar_jwt_use_case):
        self.crear_bebida_use_case = crear_bebida_use_case
        self.obtener_bebida_use_case = obtener_bebida_use_case
        self.obtener_bebidas_use_case = obtener_bebidas_use_case
        self.actualizar_stock_use_case = actualizar_stock_use_case
        self.eliminar_bebida_use_case = eliminar_bebida_use_case
        self.actualizar_bebida_use_case = actualizar_bebida_use_case
        self.verificar_jwt_use_case = verificar_jwt_use_case
        self.router = APIRouter()
        self._setup_routes()
    
    def _setup_routes(self):
        self.router.post("/", dependencies=[Depends(self._verify_auth)])(self.crear_bebida)
        self.router.get("/{bebida_id}")(self.obtener_bebida)
        self.router.get("/")(self.obtener_bebidas)
        self.router.patch("/{bebida_id}/stock")(self.actualizar_stock)
        self.router.delete("/{bebida_id}")(self.eliminar_bebida)
        self.router.put("/{bebida_id}")(self.actualizar_bebida)
    
    def _verify_auth(self, authorization: Optional[str] = Header(None)):
        """Método para verificar autenticación"""
        if not self.verificar_jwt_use_case.execute(authorization):
            raise HTTPException(401, "Token de autenticación inválido")
    
    def crear_bebida(self, datos: dict):
        bebida_id = self.crear_bebida_use_case.execute(datos)
        return {"id": bebida_id}
    
    def obtener_bebida(self, bebida_id: int):
        bebida = self.obtener_bebida_use_case.execute(bebida_id)
        return bebida
    
    def obtener_bebidas(self):
        bebidas = self.obtener_bebidas_use_case.execute()
        return bebidas
    
    def actualizar_stock(self, bebida_id: int, data: dict):
        print(data)
        resultado = self.actualizar_stock_use_case.execute(bebida_id, data["stock"])
        return resultado
    
    def eliminar_bebida(self, bebida_id: int):
        resultado = self.eliminar_bebida_use_case.execute(bebida_id)
        return resultado
    
    def actualizar_bebida(self, bebida_id: int, datos: dict):
        resultado = self.actualizar_bebida_use_case.execute(bebida_id, datos)
        return resultado