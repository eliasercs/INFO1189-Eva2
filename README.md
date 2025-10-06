🛍️ Proyecto: Tienda de Licores
📘 Descripción General

Este proyecto corresponde a una aplicación web que simula una tienda de licores, permitiendo gestionar productos, realizar compras y visualizar información de bebidas alcohólicas de diferentes tipos. Fue desarrollado como parte de la evaluación del ramo INFO1189, con el objetivo de aplicar conceptos de desarrollo web y gestión de información en un entorno simulado de comercio electrónico.

La aplicación permite:

Visualizar un catálogo de licores disponibles.

Agregar productos al carrito de compras.

Realizar operaciones básicas de gestión (crear, editar, eliminar).

Mostrar información detallada de cada producto.

⚙️ Tecnologías Utilizadas

Lenguaje principal: JavaScript

Framework: React

Frontend: HTML5, CSS3, JavaScript

Backend: Node.js + Express

Base de datos: MongoDB

Control de versiones: Git / GitHub

📁 Estructura del Proyecto
INFO1189-Eva2/
│
├── src/                 # Código fuente principal
│   ├── components/      # Componentes de interfaz o módulos
│   ├── assets/          # Imágenes, íconos y recursos
│   ├── pages/           # Páginas principales de la app
│   ├── styles/          # Archivos CSS o estilos
│   └── main.*           # Punto de entrada (index.js / app.py / etc.)
│
├── public/              # Archivos estáticos (HTML, favicon, etc.)
├── package.json         # Dependencias y scripts (Node.js)
├── requirements.txt     # Dependencias (Python)
├── README.md            
└── ...

🚀 Instalación y Ejecución
Opción 1 — Desde código fuente

```bash
# Clonar el repositorio
git clone https://github.com/PatricioValdesExamen/INFO1189-Eva2.git
cd INFO1189-Eva2

# Instalar dependencias
npm install

# Ejecutar en modo desarrollo
npm run dev
```


Opción 2 — Ejecutar versión desplegada

Acceder a:

🌐 https://info1189-eva2.vercel.app

🧩 Funcionalidades Principales
Funcionalidad	Descripción
🛒 Catálogo de productos	Lista de licores con imagen, descripción y precio.
➕ Agregar al carrito	Permite seleccionar productos y añadirlos al carrito.
🧾 Detalle del producto	Muestra información ampliada sobre un producto específico.
🛍️ Gestión de stock	Control básico de inventario (opcional).
👤 Perfil del usuario	Simula inicio de sesión o información de cliente.
🧠 Arquitectura del Proyecto

El sistema está dividido en capas para mantener una estructura clara:

Interfaz de usuario (Frontend): manejo visual, estilos y componentes.

Lógica de negocio (Backend o scripts): validaciones, cálculos y operaciones con datos.

Persistencia (Base de datos o almacenamiento local): guarda la información de los productos o compras.

🧪 Pruebas

Incluye pruebas básicas de funcionamiento manual:

Verificar carga correcta del catálogo.

Comprobar funcionamiento del carrito.

Validar precios y totales de compra.

Confirmar que los botones y enlaces funcionen correctamente.

📚 Autores

Proyecto desarrollado por:

- Eliaser Concha 
- Patricio Valdés 


🏁 Conclusión

El proyecto Tienda de Licores demuestra la aplicación de los conocimientos en desarrollo web, organización modular del código y diseño de interfaces funcionales y atractivas.
Su estructura es fácilmente escalable, permitiendo futuras mejoras como autenticación de usuarios, integración con base de datos y pasarela de pago.