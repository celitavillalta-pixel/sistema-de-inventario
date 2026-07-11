

import customtkinter as ctk
import tkinter as tk
from tkinter import *
import backend_sist_invent as backend2

def mostrar_inventario(ventana):

    label_titulo = Label(ventana, text="Inventario guardado", font=("Arial", 14, "bold"))
    label_titulo.pack(pady=10)
    
    lista_productos = Listbox(ventana, width=100, height=15)
    lista_productos.pack(pady=10)
    
    productos = backend2.cargar_inventario()
    
    if productos:
        for producto in productos:
            texto = f"{producto['codigo']} | {producto['nombre']} | {producto['categoria']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']}"
            lista_productos.insert(END, texto)
    else:
        lista_productos.insert(END, "No hay productos registrados en el inventario.")