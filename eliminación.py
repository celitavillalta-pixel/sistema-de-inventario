
import customtkinter 
from CTkListbox import CTkListbox

 
customtkinter.set_appearance_mode("light")  # Modos: "System" (predeterminado), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Temas: "blue" (predeterminado), "green", "dark-blue"


import tkinter as tk
from tkinter import messagebox
 
       
 
def pantalla_eliminacion(ventana, limpiar_pantalla):
    limpiar_pantalla()
    
    #Declaracion de funcion
    def eliminar_producto():
        producto = lista_productos.curselection()
        #Confirmar elimiacion
        if producto:
            confirmar = messagebox.askyesno(
                "Eliminar producto", "¿Seguro que desea eliminar el producto?"
            )
        #Por si no seleciono produto para eliminar
            if confirmar:
                lista_productos.delete(producto)
        else:
            messagebox.showwarning(
                "Aviso", "Seleccione un producto primero"
            )
#Frame de eliminacion    
    tajeta_eliminación = customtkinter.CTkFrame(
        master = ventana,
        bg_color="#E0E0E0",
        
    )
    tajeta_eliminación.pack(pady=40, padx=40, fill="both", expand=True)  
    
    #Titulo de frame
    lbl = customtkinter.CTkLabel(
        master=tajeta_eliminación,
        text="Selecione el producto a eliminar",
        font=("Segoe UI", 14, "bold"),
        bg_color="transparent",
        fg_color="#00BFFE" 
    )
    lbl.pack(pady = 30)
    
    #Lista de productos
    lista_productos = CTkListbox(
        master=tajeta_eliminación, 
        width=250,
        height=200,
        font=("Segoe UI", 12),
        bg_color="#E0E0E0", 
        text_color="#121212"
    )
    lista_productos.pack(pady=30)
    
    
    lista_productos.insert("END", "Dell OptiPlex 7010")
    lista_productos.insert("END", "HD ProDesk 400 G9")
    lista_productos.insert("END", "Lenovo ThinkCentre M70S")
    lista_productos.insert("END", "Acer Veriton X")
    lista_productos.insert("END", "ASUS ExpertCenter D5")
    lista_productos.insert("END", "Dell Inspiron 15")
    lista_productos.insert("END", "HP Pavilion 15")
    lista_productos.insert("END", "Lenovo IdeaPad 3")
    lista_productos.insert("END", "Logitech M185")
    lista_productos.insert("END", "Logitech G203")
    
    #boton de eliminacion
    btn_eliminar = customtkinter.CTkButton(
        master=tajeta_eliminación,
        text="Eliminar",
        command=eliminar_producto,
        bg_color="#00BFFE",
        fg_color="#00BFFE",
        font=("Segoe UI", 12, "bold"),
        width= 250, 
        height= 40,
        cursor="hand2"
    )
    btn_eliminar.pack(pady=20)
 
