# Sistema de Gestión de Productos y Compras con Pyro4

Este es un sistema de gestión de productos y compras, desarrollado en Python, que utiliza **Pyro4** para la comunicación entre servicios y **SQLite** como base de datos. El sistema permite que un administrador gestione productos y usuarios, y que un cliente pueda ver productos, registrarse y realizar compras.

## Tabla de Contenidos

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Servicios](#servicios)
- [Estructura de la Base de Datos](#estructura-de-la-base-de-datos)
- [Autor](#autor)

## Características

- **Administración de Productos**: Un administrador puede agregar, modificar y eliminar productos.
- **Gestión de Usuarios**: Un administrador puede agregar, modificar y eliminar usuarios.
- **Cliente**: Un cliente puede ver la lista de productos, registrarse en el sistema y realizar compras.
- **Servicios**: El sistema cuenta con tres servicios principales:
  - Servicio de **Producto**
  - Servicio de **Venta**
  - Servicio de **Usuario**

## Requisitos

- Python 3.x
- Pyro4
- SQLite

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>

2. Crea y activa un entorno virtual:
python3 -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate

3. Instala las dependencias necesarias:
pip install -r requirements.txt

## Uso
1. Inicia el servidor Pyro4

python -m Pyro4.naming

2. Ejecuta los servicios

# Servicio de Productos
python servicio_producto.py

# Servicio de Ventas
python servicio_venta.py

# Servicio de Usuarios
python servicio_usuario.py

3. Ejecuta el Cliente

python cliente.py
