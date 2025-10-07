# 🛍️ Proyecto: Tienda de Licores

Este proyecto corresponde a una aplicación web que simula una tienda de licores, permitiendo gestionar productos, realizar compras y visualizar información de bebidas alcohólicas de diferentes tipos. Fue desarrollado como parte de la evaluación del ramo INFO1189, con el objetivo de aplicar conceptos de desarrollo web y gestión de información en un entorno simulado de comercio electrónico.

## Modelo Entidad Relación

![MER](/docs/assets/MER.png)

## ⚙️ Tecnologías Utilizadas

Lenguaje principal: Python
Framework: Fast API
Backend: Fast API
Base de datos: MariaDB
Infraestructura: Docker
Control de versiones: Git / GitHub

## Documentación de Backend

| Método | Ruta | Descripción | Body (JSON) | Parámetros Query | Headers |
|--------|------|-------------|-------------|------------------|---------|
| `POST` | `/bebidas/` | Registrar nueva bebida a la botillería | `codigo` `nombre` `marca` `precio` `stock` `categoria_id` | - | `Authorization: Bearer token` |
| `GET` | `/bebidas/` | Obtener un listado de bebidas alcohólicas | - | - | - |
| `GET` | `/bebidas/{id}` | Obtener el recurso de bebida alcohólica | - | `id` | - |
| `PATCH` | `/bebidas/{id}/stock` | Actualizar el stock de bebidas alcohólica | `stock` | - |
| `DELETE` | `/bebidas/{id}` | Eliminar una bebida alcohólica del inventario | - | `id` | - | - |
| `PUT` | `/bebidas/{id}` | Actualizar una bebida. | `codigo` `nombre` `marca` `precio` `stock` `categoria_id` | `id` | - |

## Documentación GraphQL

Obtener listado de bebidas

```
query {
  bebidas {
    id
    codigo
    nombre
    precio
    stock
  }
}
```

Obtener una bebida en específica

```
query {
  bebida(id: 1) {
    id
    nombre
    marca
    precio
  }
}
```

Incorporar una nueva bebida

```
mutation {
  createBebida(input: {
    codigo: "GQL-002"
    nombre: "Bebida GraphQL"
    marca: "Test"
    precio: 2000
    stock: 50
    categoriaId: 1
  }) {
    id
    codigo
    nombre
  }
}
```

## 🚀 Instalación y Ejecución
Opción 1 — Desde código fuente

```bash
# Clonar el repositorio
git clone https://github.com/PatricioValdesExamen/INFO1189-Eva2.git
cd INFO1189-Eva2

# Instalar dependencias
pip install requirements.txt

# Ejecutar en modo desarrollo
python main.py
```


El sistema está dividido en capas para mantener una estructura clara:

Lógica de negocio (Backend o scripts): validaciones, cálculos y operaciones con datos.

Persistencia (Base de datos o almacenamiento local): guarda la información de los productos o compras.

## 📚 Autores

Proyecto desarrollado por:

- Eliaser Concha 
- Patricio Valdés 