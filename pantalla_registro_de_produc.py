

import customtkinter as ctk


def registrar_producto():
    # Pantalla secundaria para registrar productos.
    registrar_ventana = ctk.CTkToplevel() #Sirve para abrir una ventana scundaria sin cerrar la principal.
    registrar_ventana.title("Registrar Producto")
    registrar_ventana.geometry("500x550")
    registrar_ventana.resizable(False, False)

    # labels e inputs.
    
    #Cóigo del producto.
    label_código = ctk.CTkLabel(registrar_ventana, text = "Ingrese el código del producto: ", bg_color="transparent")
    label_código.pack(pady=10) 
    entry_código = ctk.CTkEntry(registrar_ventana)
    entry_código.pack(pady=5) 
    
    #Categoría del producto (opción múltiple)
    label_categoría = ctk.CTkLabel(registrar_ventana, text = "Seleccione una categoría: ", bg_color="transparent")
    label_categoría.pack(pady=10)
    
    opcion = ctk.IntVar()
    opcion.set(0)
    
    cb1 = ctk.CTkRadioButton(registrar_ventana, text = "Repuestos", variable=opcion, value=1, bg_color="transparent")
    cb1.pack(padx=10) 
    
    cb2 = ctk.CTkRadioButton(registrar_ventana, text = "Tecnología", variable=opcion, value= 2, bg_color="transparent")
    cb2.pack(padx=10)
    
    cb3 = ctk.CTkRadioButton(registrar_ventana, text="Otro", variable =opcion, value= 3, bg_color="transparent")
    cb3.pack(padx=10)
    
    
    #Nombre del prooducto.
    label_nombre = ctk.CTkLabel(registrar_ventana, text="Ingrese el nombre del producto: ", bg_color="transparent")
    label_nombre.pack(pady=10)
    entry_nombre = ctk.CTkEntry(registrar_ventana)
    entry_nombre.pack(pady=5)

    #Cantidad en existencia del producto. 
    label_cantidad = ctk.CTkLabel(registrar_ventana, text="Ingrese la cantidad en existencia del producto: ", bg_color="transparent")
    label_cantidad.pack(pady=10)
    entry_cantidad = ctk.CTkEntry(registrar_ventana)
    entry_cantidad.pack(pady=5)
    
    #Precio del producto.
    label_precio = ctk.CTkLabel(registrar_ventana, text="Ingrese el precio del producto: ", bg_color="transparent")
    label_precio.pack(pady=10)
    entry_precio = ctk.CTkEntry(registrar_ventana)
    entry_precio.pack(pady=5)
    
    #boton de aceptar.
    boton_aceptar = ctk.CTkButton(master = registrar_ventana, text="Aceptar", bg_color="#00BFFE", text_color="Black", width= 250, height= 40)
    boton_aceptar.pack(pady=20)
    
    registrar_ventana.configure(bg= "#E0E0E0")