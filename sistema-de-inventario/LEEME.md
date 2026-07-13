# Sistema de Inventario KeepIt

Un sistema de gestión de inventario con interfaz gráfica desarrollado en Python usando customtkinter.

## Instalación

### 1. Crear entorno virtual (si no lo tienes)
```bash
python -m venv .venv
```

### 2. Activar entorno virtual
**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Windows (CMD):**
```bash
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar el programa:
```bash
python inicio_de_sesion.py
```

## Características

- ✅ Autenticación de usuarios
- ✅ Registro de nuevas cuentas
- ✅ Agregar productos al inventario
- ✅ Buscar productos
- ✅ Eliminar productos
- ✅ Persistencia de datos en JSON

## Estructura de archivos

- `inicio_de_sesion.py` - Pantalla de login y registro
- `pantalla_principal_.py` - Menú principal
- `pantalla_registro_de_produc.py` - Registro de productos
- `buscar_productos.py` - Búsqueda de productos
- `eliminacion.py` - Eliminación de productos
- `backend_sist_invent.py` - Funciones de base de datos
- `imagen_logo.py` - Configuración del logo
- `inventario.json` - Base de datos de productos
- `usuarios.txt` - Base de datos de usuarios

## Requisitos

- Python 3.8+
- customtkinter 5.0+
- Pillow 9.0+

---
**Desarrollado con ❤️**
