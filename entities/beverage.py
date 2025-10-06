from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from .category import Categoria

@dataclass
class Bebida:
    codigo: str
    nombre: str
    marca: str
    precio: int
    stock: int
    categoria_id: int
    categoria: Optional[Categoria] = None
    
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None