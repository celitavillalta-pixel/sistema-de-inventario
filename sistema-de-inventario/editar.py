from tkinter import messagebox
import customtkinter as ctk
from backend_sist_invent import cargar_inventario, obtener_ruta_json
import json

def editar_producto(ventana, limpiar_pantalla):
    
    limpiar_pantalla()
    
    # Crear frame principal
    tarjeta_editar = ctk.CTkScrollableFrame(master=ventana, fg_color="white", corner_radius=15)
    tarjeta_editar.pack(pady=40, padx=40, fill="both", expand=True)
    
    # Título
    titulo = ctk.CTkLabel(
        master=tarjeta_editar,
        text="Editar Producto",
        font=("Segoe UI", 20, "bold"),
        bg_color="transparent",
        text_color="#00BFFE"
    )
    titulo.pack(pady=20)
    
    # Búsqueda de producto
    label_buscar = ctk.CTkLabel(
        master=tarjeta_editar,
        text="Ingrese el código del producto a editar:",
        bg_color="transparent",
        font=("Segoe UI", 12)
    )
    label_buscar.pack(pady=(10, 5))
    
    entry_codigo_buscar = ctk.CTkEntry(
        master=tarjeta_editar,
        width=250,
        height=40,
        placeholder_text="Código del producto"
    )
    entry_codigo_buscar.pack(pady=(0, 20))
    
    # Frame para campos editables (inicialmente oculto)
    frame_campos = ctk.CTkFrame(master=tarjeta_editar, fg_color="transparent")
    frame_campos.pack(pady=20, padx=10, fill="both", expand=False)
    
    # Variables para guardar los campos editables
    campos_editables = {}
    producto_actual = {"datos": None, "indice": None}
    
    def buscar_producto():
        codigo = entry_codigo_buscar.get().strip()
        
        if not codigo:
            messagebox.showerror("Error", "Ingrese un código de producto")
            return
        
        inventario = cargar_inventario()
        producto_encontrado = None
        indice = None
        
        for i, prod in enumerate(inventario):
            if prod["codigo"] == codigo:
                producto_encontrado = prod
                indice = i
                break
        
        if not producto_encontrado:
            messagebox.showerror("Error", f"Producto con código '{codigo}' no encontrado")
            return
        
        # Guardar datos del producto
        producto_actual["datos"] = producto_encontrado
        producto_actual["indice"] = indice
        
        # Limpiar frame de campos anteriores
        for widget in frame_campos.winfo_children():
            widget.destroy()
        
        campos_editables.clear()
        
        # Crear campos editables
        # Código (no editable)
        label_codigo = ctk.CTkLabel(master=frame_campos, text="Código:", bg_color="transparent")
        label_codigo.pack(pady=(10, 2))
        entry_codigo = ctk.CTkEntry(master=frame_campos, width=250, height=40)
        entry_codigo.insert(0, producto_encontrado["codigo"])
        entry_codigo.configure(state="disabled")
        entry_codigo.pack(pady=(0, 15))
        
        # Nombre
        label_nombre = ctk.CTkLabel(master=frame_campos, text="Nombre:", bg_color="transparent")
        label_nombre.pack(pady=(10, 2))
        entry_nombre = ctk.CTkEntry(master=frame_campos, width=250, height=40)
        entry_nombre.insert(0, producto_encontrado["nombre"])
        entry_nombre.pack(pady=(0, 15))
        campos_editables["nombre"] = entry_nombre
        
        # Cantidad
        label_cantidad = ctk.CTkLabel(master=frame_campos, text="Cantidad:", bg_color="transparent")
        label_cantidad.pack(pady=(10, 2))
        entry_cantidad = ctk.CTkEntry(master=frame_campos, width=250, height=40)
        entry_cantidad.insert(0, str(producto_encontrado["cantidad"]))
        entry_cantidad.pack(pady=(0, 15))
        campos_editables["cantidad"] = entry_cantidad
        
        # Precio
        label_precio = ctk.CTkLabel(master=frame_campos, text="Precio:", bg_color="transparent")
        label_precio.pack(pady=(10, 2))
        entry_precio = ctk.CTkEntry(master=frame_campos, width=250, height=40)
        entry_precio.insert(0, str(producto_encontrado["precio"]))
        entry_precio.pack(pady=(0, 15))
        campos_editables["precio"] = entry_precio
        
        # Categoría
        label_categoria = ctk.CTkLabel(master=frame_campos, text="Categoría:", bg_color="transparent")
        label_categoria.pack(pady=(10, 2))
        
        frame_cat = ctk.CTkFrame(master=frame_campos, fg_color="transparent")
        frame_cat.pack(pady=(0, 15))
        
        opcion = ctk.IntVar()
        opcion.set(producto_encontrado.get("categoria", 1))
        
        categorias = [
            ("Repuestos", 1),
            ("Tecnología", 2),
            ("Otro", 3)
        ]
        
        for texto, valor in categorias:
            cb = ctk.CTkRadioButton(master=frame_cat, text=texto, variable=opcion, value=valor, bg_color="transparent")
            cb.pack(side="left", padx=10)
        
        campos_editables["categoria"] = opcion
        
        # Botones
        frame_botones = ctk.CTkFrame(master=frame_campos, fg_color="transparent")
        frame_botones.pack(pady=20)
        
        def guardar_cambios():
            try:
                nombre = campos_editables["nombre"].get().strip()
                cantidad = int(campos_editables["cantidad"].get().strip())
                precio = float(campos_editables["precio"].get().strip())
                categoria = campos_editables["categoria"].get()
                
                if not nombre:
                    messagebox.showerror("Error", "El nombre no puede estar vacío")
                    return
                
                # Actualizar producto en inventario
                inventario = cargar_inventario()
                inventario[producto_actual["indice"]]["nombre"] = nombre
                inventario[producto_actual["indice"]]["cantidad"] = cantidad
                inventario[producto_actual["indice"]]["precio"] = precio
                inventario[producto_actual["indice"]]["categoria"] = categoria
                
                # Guardar en archivo
                ruta = obtener_ruta_json()
                with ruta.open("w", encoding="utf-8") as archivo:
                    json.dump(inventario, archivo, ensure_ascii=False, indent=2)
                
                messagebox.showinfo("Éxito", "Producto actualizado correctamente")
                
                # Limpiar campos
                entry_codigo_buscar.delete(0, "end")
                for widget in frame_campos.winfo_children():
                    widget.destroy()
                campos_editables.clear()
                
            except ValueError:
                messagebox.showerror("Error", "La cantidad debe ser un número entero y el precio debe ser un número decimal")
        
        def volver_principal():
            """Volver a pantalla principal"""
            tarjeta_editar.destroy()
            from pantalla_principal_ import principal_keepit
            principal_keepit(ventana, limpiar_pantalla)
        
        btn_guardar = ctk.CTkButton(
            master=frame_botones,
            text="Guardar Cambios",
            font=("Segoe UI", 12, "bold"),
            bg_color="transparent",
            fg_color="#00BFFE",
            width=150,
            height=40,
            command=guardar_cambios
        )
        btn_guardar.pack(side="left", padx=10)
        
        btn_volver = ctk.CTkButton(
            master=frame_botones,
            text="Volver",
            font=("Segoe UI", 12, "bold"),
            bg_color="transparent",
            fg_color="#E0E0E0",
            text_color="#00BFFE",
            width=150,
            height=40,
            command=volver_principal
        )
        btn_volver.pack(side="left", padx=10)
    
    # Botón buscar
    boton_buscar = ctk.CTkButton(
        master=tarjeta_editar,
        text="Buscar Producto",
        font=("Segoe UI", 12, "bold"),
        bg_color="#E0E0E0",
        fg_color="#00BFFE",
        width=250,
        height=40,
        command=buscar_producto
    )
    boton_buscar.pack(pady=20)
    
    # Botón volver sin producto seleccionado
    def volver_sin_editar():
        tarjeta_editar.destroy()
        from pantalla_principal_ import principal_keepit
        principal_keepit(ventana, limpiar_pantalla)
    
    boton_volver_inicial = ctk.CTkButton(
        master=tarjeta_editar,
        text="Volver a Pantalla Principal",
        font=("Segoe UI", 12, "bold"),
        bg_color="transparent",
        fg_color="#E0E0E0",
        text_color="#00BFFE",
        width=250,
        height=40,
        command=volver_sin_editar
    )
    boton_volver_inicial.pack(pady=10)
