from abc import ABC, abstractmethod
from typing import List, Optional
from entities.beverage import Bebida

class BebidaReadRepository(ABC):
    @abstractmethod
    def obtener_bebida_por_id(self, id: int) -> Optional[Bebida]:
        pass
    
    @abstractmethod
    def obtener_bebidas(self) -> List[Bebida]:
        pass

class BebidaWriteRepository(ABC):
    @abstractmethod
    def guardar(self, bebida: Bebida) -> Bebida:
        pass
    
    @abstractmethod
    def actualizar(self, bebida: Bebida) -> Optional[Bebida]:
        pass
    
    @abstractmethod
    def actualizar_stock(self, id, nuevo_stock: int) -> Optional[Bebida]:
        pass
    
    @abstractmethod
    def eliminar(self, id: int) -> bool:
        pass

class BebidaRepository(BebidaReadRepository, BebidaWriteRepository):
    pass