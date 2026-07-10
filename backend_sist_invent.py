
import json
from pathlib import Path
from tkinter import messagebox
 
 
def obtener_ruta_json():
    return Path(__file__).with_name("inventario.json")
 
 
def cargar_inventario():
    ruta = obtener_ruta_json()
    if not ruta.exists():
        return []
 
    with ruta.open("r", encoding="utf-8") as archivo:
        try:
            datos = json.load(archivo)
            return datos if isinstance(datos, list) else []
        except json.JSONDecodeError:
            return []
 
 
def guardar_producto_json(producto):
    inventario = cargar_inventario()
    inventario.append(producto)
 
    with obtener_ruta_json().open("w", encoding="utf-8") as archivo:
        json.dump(inventario, archivo, ensure_ascii=False, indent=2)
 
    return inventario
 
 
def productos_ingresados(entry_codigo, entry_nombre, entry_cantidad, entry_precio, opcion, label_precio, label_cantidad, label_nombre, label_codigo):
    # Función para mostrar los productos ingresados en la pantalla principal.
    codigo = entry_codigo.get().strip()
    nombre = entry_nombre.get().strip()
    cantidad = entry_cantidad.get().strip()
    precio = entry_precio.get().strip()
    categoría = opcion.get()
 
    if not codigo or not nombre or not cantidad or not precio:
        messagebox.showerror("Error", "Por favor, complete todos los campos.")
        return
    
    try:
        cantidad = int(cantidad)
        precio = float(precio)
    except ValueError:
        messagebox.showerror("Error", "La cantidad debe ser un número entero y el precio debe ser un número decimal.")
        return
 
    label_codigo.configure(text=f"Código: {codigo}", font=("Segoe UI", "bold", 14), text_color=("#00BFFE"))
    label_nombre.configure(text=f"Nombre: {nombre}", font=("Segoe UI", "bold", 14), text_color=("#00BFFE"))
    label_cantidad.configure(text=f"Cantidad: {cantidad}", font=("Segoe UI", "bold", 14), text_color= ("#00BFFE"))
    label_precio.configure(text=f"Precio: ${precio:.2f}", font=("Segoe UI", "bold", 14), text_color= ("#00BFFE"))
    categorias = {1: "Repuestos", 2: "Tecnología", 3: "Otro"}
    categorias.configure(text=f"Categoría: {categoría.get(categoría, 'Desconocida')}", font=("Segoe UI", "bold", 14), text_color="#00BFFE")

    entry_codigo.delete(0, 'end')
    entry_nombre.delete(0, 'end')
    entry_cantidad.delete(0, 'end')
    entry_precio.get()
    entry_precio.delete(0, 'end')
    opcion.set(0)  
 
    messagebox.showinfo("Éxito", "Producto registrado correctamente.")