def mostrar_inventario():
    ventana = ctk.CTkToplevel(screen)
    ventana.title("Mostrar Inventario")
    ventana.geometry("350x300")

    etiqueta = ctk.CTkLabel(
        ventana,
        text="Buscar producto",
        font=("Helvetica", 16)
    )
    etiqueta.pack(pady=10)

    entrada_busqueda = ctk.CTkEntry(
        ventana,
        placeholder_text="Nombre del producto"
    )
    entrada_busqueda.pack(pady=10)

    resultado = ctk.CTkLabel(
        ventana,
        text="",
        font=("Helvetica", 14)
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

    boton_buscar = ctk.CTkButton(
        ventana,
        text="Buscar",
        command=buscar
    )
    boton_buscar.pack(pady=10)