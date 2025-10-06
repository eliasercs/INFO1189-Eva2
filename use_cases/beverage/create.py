from datetime import datetime
from entities.beverage import Bebida
from adapters.gateways.beverage_repository import BebidaWriteRepository

class CrearBebidaUseCase:
    def __init__(self, bebida_repository: BebidaWriteRepository):
        self.bebida_repository = bebida_repository

    def execute(self, comando: 'CrearBebidaComando') -> Bebida:
        # Validaciones de aplicación
        if comando.precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")

        if comando.stock < 0:
            raise ValueError("El stock no puede ser negativo")

        # Verificar si el código ya existe
        bebida_existente = self.bebida_repository.obtener_por_codigo(comando.codigo)
        if bebida_existente:
            raise ValueError("Ya existe una bebida con este código")

        # Crear entidad
        bebida = Bebida(
            codigo=comando.codigo,
            nombre=comando.nombre,
            marca=comando.marca,
            precio=comando.precio,
            stock=comando.stock,
            categoria_id=comando.categoria_id
        )

        # Guardar a través del repositorio
        return self.bebida_repository.guardar(bebida)

class CrearBebidaComando:
    def __init__(self, codigo: str, nombre: str, marca: str, precio: int, stock: int, categoria_id: int):
        self.codigo = codigo
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock
        self.categoria_id = categoria_id