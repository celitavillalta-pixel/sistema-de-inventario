

from tkinter import messagebox
import customtkinter as ctk
from backend_sist_invent import guardar_producto_json
from backend_sist_invent import productos_ingresados
 
def registrar_producto(ventana, logo_label, boton_1, boton_2, boton_3):
     
    
    logo_label.pack_forget()
    boton_1.pack_forget()
    boton_2.pack_forget()
    boton_3.pack_forget() 
    
    
    #Cajita estetica. 
    tarjeta_registro = ctk.CTkScrollableFrame(master=ventana, fg_color="white", corner_radius=15)
    tarjeta_registro.pack(pady=40, padx=40, fill="both", expand=True)

    # labels e inputs.
    
    #Cóigo del producto.
    label_código = ctk.CTkLabel(master=tarjeta_registro, text = "Ingrese el código del producto: ", bg_color="transparent")
    label_código.pack(pady=(15, 2), padx=2)  
    entry_código = ctk.CTkEntry(master=tarjeta_registro, width= 250, height= 40)
    entry_código.pack(pady=(0, 15), padx=10) 
    
    #Categoría del producto (opción múltiple)
    label_categoría = ctk.CTkLabel(master=tarjeta_registro, text = "Seleccione una categoría: ", bg_color="transparent")
    label_categoría.pack(pady=(10, 5), padx=2)
    
    frame_categorias = ctk.CTkFrame(master=tarjeta_registro, fg_color="transparent") #sirve para agrupar los botones de opción
    frame_categorias.pack(pady=(0, 15), padx=10)
    
    opcion = ctk.IntVar()
    opcion.set(0)
    
    cb1 = ctk.CTkRadioButton(master=frame_categorias, text = "Repuestos", variable=opcion, value=1, bg_color="transparent")
    cb1.pack(side="left", padx=10)

    
    cb2 = ctk.CTkRadioButton(master=frame_categorias, text = "Tecnología", variable=opcion, value= 2, bg_color="transparent")
    cb2.pack(side="left", padx=10) 
    
    cb3 = ctk.CTkRadioButton(master=frame_categorias, text="Otro", variable =opcion, value= 3, bg_color="transparent")
    cb3.pack(side="left", padx=10)
    
    
    #Nombre del prooducto.
    label_nombre = ctk.CTkLabel(
        master=tarjeta_registro,
        text="Ingrese el nombre del producto: ",
        bg_color="transparent"
        )
    label_nombre.pack(pady=(10, 2), padx=2)
    entry_nombre = ctk.CTkEntry(master=tarjeta_registro, width= 250, height= 40)
    entry_nombre.pack(pady=(0, 15), padx=10)

    #Cantidad en existencia del producto. 
    label_cantidad = ctk.CTkLabel(
        master =tarjeta_registro,
        text="Ingrese la cantidad en existencia del producto: ",
        bg_color="transparent"
        )
    label_cantidad.pack(pady=(0, 15), padx=10)
    entry_cantidad = ctk.CTkEntry(master=tarjeta_registro, width= 250, height= 40)
    entry_cantidad.pack(pady=(0, 15), padx=10)
    
    #Precio del producto.
    label_precio = ctk.CTkLabel(
        master = tarjeta_registro, 
        text="Ingrese el precio del producto: ",
        bg_color="transparent"
        )
    label_precio.pack(pady=(10, 2), padx=2)
    entry_precio = ctk.CTkEntry(master=tarjeta_registro, width= 250, height= 40)
    entry_precio.pack(pady=(0, 20), padx=10)
    
    def guardar_producto():
        codigo = entry_código.get().strip()
        categoria = opcion.get()
        nombre = entry_nombre.get().strip()
        cantidad = entry_cantidad.get().strip()
        precio = entry_precio.get().strip()
 
        if not codigo or not nombre or not cantidad or not precio:
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return
 
        try:
            cantidad = int(cantidad)
            precio = float(precio)
        except ValueError:
            messagebox.showerror("Error", "La cantidad debe ser un número entero y el precio debe ser un número decimal.")
            return
 
        producto = {
            "codigo": codigo,
            "categoria": categoria,
            "nombre": nombre,
            "cantidad": cantidad,
            "precio": precio,
        }
 
        guardar_producto_json(producto)
        messagebox.showinfo("Éxito", "Producto guardado en inventario.json")
    
    
    #boton de aceptar.
    boton_aceptar = ctk.CTkButton(master = tarjeta_registro, text="Aceptar", font=("Segoe UI", 12, "bold"), bg_color="#E0E0E0", fg_color="#00BFFE", width= 250, height= 40, command=lambda: productos_ingresados(entry_código, entry_nombre, entry_cantidad, entry_precio, opcion, label_precio, label_cantidad, label_nombre, label_código))
    boton_aceptar.pack(pady=10)
    
    boton_volver = ctk.CTkButton(master = tarjeta_registro, text="Volver", font=("Segoe UI", 12, "bold"), bg_color="#E0E0E0", fg_color="#00BFFE", width= 250, height= 40)
    boton_volver.pack(pady=10)
