from fastapi import FastAPI
from frameworks.persistence.database.connection import crear_conexion
from frameworks.persistence.beverage_repository_impl import BebidaRepositoryImpl
from use_cases.beverage.create import CrearBebidaUseCase
from use_cases.beverage.get_by_id import ObtenerBebidaCompletaPorIdUseCase
from use_cases.beverage.get import ObtenerBebidasUseCase
from use_cases.beverage.update_stock import ActualizarStockBebidaUseCase
from use_cases.beverage.delete import EliminarBebidaUseCase
from use_cases.beverage.update import ActualizarBebidaUseCase
from use_cases.security.verify_jwt import VerifyAuthUseCase
from adapters.controllers.beverage_controller import BeverageController
from frameworks.security.jwt_provider import JWTProvider

from frameworks.web.graphql import create_graphql_app

app = FastAPI(
    title="Gestión de Bebidas API",
    description="API para gestionar bebidas utilizando arquitectura limpia",
    version="1.0.0"
)

db_connection = crear_conexion()

bebida_repository = BebidaRepositoryImpl(db_connection)  # ← Inyección de dependencia

jwt_provider = JWTProvider(secret_key="secreto123")

agregar_bebida = CrearBebidaUseCase(bebida_repository)  # ← Inyección de dependencia
obtener_bebida_id = ObtenerBebidaCompletaPorIdUseCase(bebida_repository)  # ← Inyección de dependencia
obtener_bebidas = ObtenerBebidasUseCase(bebida_repository)  # ← Inyección de dependencia
actualizar_stock = ActualizarStockBebidaUseCase(bebida_repository)  # ← Inyección de dependencia
eliminar_bebida = EliminarBebidaUseCase(bebida_repository)  # ← Inyección de dependencia
actualizar_bebida = ActualizarBebidaUseCase(bebida_repository)  # ← Inyección de dependencia
verificar_jwt = VerifyAuthUseCase(jwt_provider)

graphql_app = create_graphql_app(
    obtener_bebidas_use_case=obtener_bebidas,
    obtener_bebida_por_id_use_case=obtener_bebida_id,
    crear_bebida_use_case=agregar_bebida
)

controller = BeverageController(agregar_bebida, obtener_bebida_id, obtener_bebidas, actualizar_stock, eliminar_bebida, actualizar_bebida, verificar_jwt)
app.include_router(controller.router, prefix="/bebidas")
app.add_route("/graphql", graphql_app)