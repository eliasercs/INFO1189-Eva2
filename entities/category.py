from dataclasses import dataclass
from typing import Optional
from .grados_alcohol import GradoAlcohol

@dataclass
class Categoria:
    nombre: str
    tipo_grado_id: int
    restriction_edad: bool
    id: Optional[int] = None
    grado_alcohol: Optional[GradoAlcohol] = None