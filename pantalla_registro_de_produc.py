
import tkinter as tk
from tkinter import *


def registrar_producto():
    # Pantalla secundaria para registrar productos.
    registrar_ventana = tk.Toplevel() #Sirve para abrir una ventana scundaria sin cerrar la principal.
    registrar_ventana.title("Registrar Producto")
    registrar_ventana.geometry("500x450")
    registrar_ventana.resizable(False, False)

    # labels e inputs.
    
    #Cóigo del producto.
    label_código = tk.Label(registrar_ventana, text = "Ingrese el código del producto: ", bg="#E0E0E0")
    label_código.pack(pady=10) 
    entry_código = tk.Entry(registrar_ventana)
    entry_código.pack(pady=5) 
    
    #Categoría del producto (opción múltiple)
    label_categoría = tk.Label(registrar_ventana, text = "Seleccione una categoría: ", bg="#E0E0E0")
    label_categoría.pack(pady=10)
    
    opcion = tk.IntVar()
    opcion.set(0)
    
    cb1 = tk.Radiobutton(registrar_ventana, text = "Repuestos", variable=opcion, value=1, bg="#E0E0E0")
    cb1.pack(padx=10) 
    
    cb2 = tk.Radiobutton(registrar_ventana, text = "Tecnología", variable=opcion, value= 2, bg="#E0E0E0")
    cb2.pack(padx=10)
    
    cb3 = tk.Radiobutton(registrar_ventana, text="Otro", variable =opcion, value= 3, bg="#E0E0E0")
    cb3.pack(padx=10)
    
    
    #Nombre del prooducto.
    label_nombre = tk.Label(registrar_ventana, text="Ingrese el nombre del producto: ", bg="#E0E0E0")
    label_nombre.pack(pady=10)
    entry_nombre = tk.Entry(registrar_ventana)
    entry_nombre.pack(pady=5)

    #Cantidad en existencia del producto. 
    label_cantidad = tk.Label(registrar_ventana, text="Ingrese la cantidad en existencia del producto: ", bg="#E0E0E0")
    label_cantidad.pack(pady=10)
    entry_cantidad = tk.Entry(registrar_ventana)
    entry_cantidad.pack(pady=5)
    
    #Precio del producto.
    label_precio = tk.Label(registrar_ventana, text="Ingrese el precio del producto: ", bg="#E0E0E0")
    label_precio.pack(pady=10)
    entry_precio = tk.Entry(registrar_ventana)
    entry_precio.pack(pady=5)
    
    registrar_ventana.configure(bg= "#E0E0E0")