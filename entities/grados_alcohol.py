from dataclasses import dataclass
from typing import Optional

@dataclass
class GradoAlcohol:
    nombre: str
    descripcion: str
    horario_limite_venta: str
    id: Optional[int] = None
