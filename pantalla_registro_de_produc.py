

import customtkinter as ctk

def registrar_producto(ventana, limpiar_pantalla, logo_label, boton_1, boton_2, boton_3):
     
    
    logo_label.pack_forget()
    boton_1.pack_forget()
    boton_2.pack_forget()
    boton_3.pack_forget() 
    
    
    tarjeta_registro = ctk.CTkFrame(master=ventana, fg_color="white", corner_radius=15)
    tarjeta_registro.pack(pady=40, padx=40, fill="both", expand=True)

    # labels e inputs.
    
    #Cóigo del producto.
    label_código = ctk.CTkLabel(master=tarjeta_registro, text = "Ingrese el código del producto: ", bg_color="transparent")
    label_código.pack(pady=15, padx=2)  
    entry_código = ctk.CTkEntry(master=tarjeta_registro)
    entry_código.pack(pady=0, padx=15) 
    
    #Categoría del producto (opción múltiple)
    label_categoría = ctk.CTkLabel(master=tarjeta_registro, text = "Seleccione una categoría: ", bg_color="transparent")
    label_categoría.pack(pady=15, padx=2)
    
    opcion = ctk.IntVar()
    opcion.set(0)
    
    cb1 = ctk.CTkRadioButton(master=tarjeta_registro, text = "Repuestos", variable=opcion, value=1, bg_color="transparent")
    cb1.pack(pady=0, padx=15) 
    
    cb2 = ctk.CTkRadioButton(master=tarjeta_registro, text = "Tecnología", variable=opcion, value= 2, bg_color="transparent")
    cb2.pack(pady=0, padx=15) 
    
    cb3 = ctk.CTkRadioButton(master=tarjeta_registro, text="Otro", variable =opcion, value= 3, bg_color="transparent")
    cb3.pack(pady=0, padx=15)
    
    
    #Nombre del prooducto.
    label_nombre = ctk.CTkLabel(
        master=tarjeta_registro,
        text="Ingrese el nombre del producto: ",
        bg_color="transparent"
        )
    label_nombre.pack(pady=15, padx=2)
    entry_nombre = ctk.CTkEntry(master=tarjeta_registro)
    entry_nombre.pack(pady=0, padx=15)

    #Cantidad en existencia del producto. 
    label_cantidad = ctk.CTkLabel(
        master =tarjeta_registro,
        text="Ingrese la cantidad en existencia del producto: ",
        bg_color="transparent"
        )
    label_cantidad.pack(pady=15, padx=2)
    entry_cantidad = ctk.CTkEntry(master=tarjeta_registro)
    entry_cantidad.pack(pady=0, padx=15)
    
    #Precio del producto.
    label_precio = ctk.CTkLabel(
        master = tarjeta_registro, 
        text="Ingrese el precio del producto: ",
        bg_color="transparent"
        )
    label_precio.pack(pady=15, padx=2)
    entry_precio = ctk.CTkEntry(master=tarjeta_registro)
    entry_precio.pack(pady=0, padx=15)
    
    #boton de aceptar.
    boton_aceptar = ctk.CTkButton(master = tarjeta_registro, text="Aceptar", bg_color="#E0E0E0", fg_color="#00BFFE", width= 250, height= 40)
    boton_aceptar.pack(pady=20)
    
    ventana.configure(bg="white")