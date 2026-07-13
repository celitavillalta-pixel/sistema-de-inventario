
import customtkinter 
from backend_sist_invent import cargar_inventario

customtkinter.set_appearance_mode("light") 
customtkinter.set_default_color_theme("blue") 

def buscar_productos(ventana, limpiar_pantalla=None):

    # Crear frame principal
    tarjeta_busqueda = customtkinter.CTkFrame(master=ventana, fg_color="white", corner_radius=15)
    tarjeta_busqueda.pack(pady=40, padx=40, fill="both", expand=True)

    etiqueta = customtkinter.CTkLabel(
        master=tarjeta_busqueda,
        text="Buscar producto",
        font=("Segoe UI", 18, "bold"), 
        bg_color="transparent", 
        text_color="#00BFFE",
    )
    etiqueta.pack(pady=20)

    entrada_busqueda = customtkinter.CTkEntry(
        master=tarjeta_busqueda,
        placeholder_text="Nombre del producto",
        font=("Segoe UI", 14),
        width=250,
        height=40,
    )
    entrada_busqueda.pack(pady=10)

    resultado = customtkinter.CTkLabel(
        master=tarjeta_busqueda,
        text="",
        font=("Segoe UI", 14),
        bg_color="transparent", 
        text_color="#121212",
    )
    resultado.pack(pady=20)

    def buscar():
        nombre = entrada_busqueda.get().lower()
        inventario = cargar_inventario()
        if not nombre:
            resultado.configure(text="Por favor ingrese un nombre")
            return
        for producto in inventario:
            if producto["nombre"].lower() == nombre:
                resultado.configure(
                    text=f"Producto: {producto['nombre']}\nCantidad: {producto['cantidad']}\nPrecio: ${producto['precio']:.2f}",
                    text_color="#00BFFE"
                )
                return
        resultado.configure(text="Producto no encontrado", text_color="#FF0000")

    boton_buscar = customtkinter.CTkButton(
        master=tarjeta_busqueda,
        text="Buscar",
        font=("Segoe UI", "bold", 14),
        fg_color="#00BFFE",
        text_color="white",
        width=250,
        height=40,
        command=buscar
    )
    boton_buscar.pack(pady=10)
    
    if limpiar_pantalla:
        def volver():
            from pantalla_principal_ import principal_keepit
            principal_keepit(ventana, limpiar_pantalla)
        
        boton_volver = customtkinter.CTkButton(
            master=tarjeta_busqueda,
            text="Volver",
            font=("Segoe UI", "bold", 14),
            fg_color="#E0E0E0",
            text_color="#00BFFE",
            width=250,
            height=40,
            command=volver
        )
        boton_volver.pack(pady=10)