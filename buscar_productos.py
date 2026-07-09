
import customtkinter 

customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("blue") 

def buscar_productos(ventana):

    etiqueta = customtkinter.CTkLabel(
        ventana,
        text="Buscar producto",
        font=("Helvetica", 16), 
        bg_color= "#E0E0E0", 
        text_color= "#00BFFE",
    )
    etiqueta.pack(pady=10)

    entrada_busqueda = customtkinter.CTkEntry(
        ventana,
        placeholder_text="Nombre del producto",
          font=("segoe UI", 24, "bold"),
          bg_color= "#E0E0E0", 
          text_color= "#00BFFE",
    )
    entrada_busqueda.pack(pady=10)

    resultado = customtkinter.CTkLabel(
        ventana,
        text="",
        font=("Helvetica", 14),
        bg_color= "#E0E0E0", 
        text_color= "#00BFFE",
    )
    resultado.pack(pady=15)

    def buscar():
        nombre = entrada_busqueda.get().lower()
        for producto in inventario:
            if producto["nombre"].lower() == nombre:
                resultado.configure(
                    text=f"Producto: {producto['nombre']}\nCantidad: {producto['cantidad']}"
                )
                return
        resultado.configure(text="Producto no encontrado")

    boton_buscar = customtkinter.CTkButton(
        ventana,
        text="Buscar",
        font=("Segoe UI", "bold", 14),
        fg_color ="#E0E0E0",
        text_color= "#00BFFE",
        command=buscar
    )
    boton_buscar.pack(pady=10)