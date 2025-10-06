from fastapi import FastAPI
from frameworks.persistence.database.connection import crear_conexion
from frameworks.persistence.beverage_repository_impl import BebidaRepositoryImpl
from use_cases.beverage.create import CrearBebidaUseCase
from use_cases.beverage.get_by_id import ObtenerBebidaCompletaPorIdUseCase
from use_cases.beverage.get import ObtenerBebidasUseCase
from use_cases.beverage.update_stock import ActualizarStockBebidaUseCase
from use_cases.beverage.delete import EliminarBebidaUseCase
from use_cases.beverage.update import ActualizarBebidaUseCase
from adapters.controllers.beverage_controller import BeverageController

app = FastAPI(
    title="Gestión de Bebidas API",
    description="API para gestionar bebidas utilizando arquitectura limpia",
    version="1.0.0"
)

db_connection = crear_conexion()

bebida_repository = BebidaRepositoryImpl(db_connection)  # ← Inyección de dependencia

agregar_bebida = CrearBebidaUseCase(bebida_repository)  # ← Inyección de dependencia
obtener_bebida_id = ObtenerBebidaCompletaPorIdUseCase(bebida_repository)  # ← Inyección de dependencia
obtener_bebidas = ObtenerBebidasUseCase(bebida_repository)  # ← Inyección de dependencia
actualizar_stock = ActualizarStockBebidaUseCase(bebida_repository)  # ← Inyección de dependencia
eliminar_bebida = EliminarBebidaUseCase(bebida_repository)  # ← Inyección de dependencia
actualizar_bebida = ActualizarBebidaUseCase(bebida_repository)  # ← Inyección de dependencia

controller = BeverageController(agregar_bebida, obtener_bebida_id, obtener_bebidas, actualizar_stock, eliminar_bebida, actualizar_bebida)
app.include_router(controller.router, prefix="/bebidas")