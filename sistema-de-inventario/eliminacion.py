import customtkinter 
import tkinter as tk
from tkinter import messagebox
from backend_sist_invent import cargar_inventario
import json
from pathlib import Path

customtkinter.set_appearance_mode("light")  # Modos: "System" (predeterminado), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Temas: "blue" (predeterminado), "green", "dark-blue"


def pantalla_eliminacion(ventana, limpiar_pantalla):
    limpiar_pantalla()
    
    # Cargar inventario
    inventario = cargar_inventario()
    productos_seleccionados = {"indice": None}
    
    # Declaracion de funcion
    def eliminar_producto():
        if productos_seleccionados["indice"] is not None:
            confirmar = messagebox.askyesno(
                "Eliminar producto", "¿Seguro que desea eliminar este producto?"
            )
            if confirmar:
                inventario.pop(productos_seleccionados["indice"])
                # Guardar cambios
                ruta = Path(__file__).with_name("inventario.json")
                with ruta.open("w", encoding="utf-8") as archivo:
                    json.dump(inventario, archivo, ensure_ascii=False, indent=2)
                messagebox.showinfo("Éxito", "Producto eliminado correctamente")
                actualizar_lista()
        else:
            messagebox.showwarning(
                "Aviso", "Seleccione un producto primero"
            )
    
    def actualizar_lista():
        lista_productos.delete(0, tk.END)
        inventario_actualizado = cargar_inventario()
        for producto in inventario_actualizado:
            lista_productos.insert(tk.END, f"{producto['nombre']} (${producto['precio']:.2f})")
    
    def on_select(_):
        selection = lista_productos.curselection()
        if selection:
            productos_seleccionados["indice"] = selection[0]
    
    #Frame de eliminacion    
    tarjeta_eliminacion = customtkinter.CTkFrame(
        master=ventana,
        fg_color="white",
        corner_radius=15
    )
    tarjeta_eliminacion.pack(pady=40, padx=40, fill="both", expand=True)  
    
    #Titulo de frame
    lbl = customtkinter.CTkLabel(
        master=tarjeta_eliminacion,
        text="Seleccione el producto a eliminar",
        font=("Segoe UI", 14, "bold"),
        bg_color="transparent",
        text_color="#00BFFE" 
    )
    lbl.pack(pady=30)
    
    #Lista de productos con Listbox estándar
    frame_listbox = customtkinter.CTkFrame(master=tarjeta_eliminacion, fg_color="white")
    frame_listbox.pack(pady=10, padx=20, fill="both", expand=True)
    
    lista_productos = tk.Listbox(
        master=frame_listbox, 
        width=40,
        height=12,
        font=("Segoe UI", 11),
        bg="white",
        fg="#121212",
        border=1
    )
    lista_productos.pack(fill="both", expand=True)
    lista_productos.bind("<<ListboxSelect>>", on_select)
    
    # Actualizar lista con productos del inventario
    actualizar_lista()
    
    #Botones
    frame_botones = customtkinter.CTkFrame(master=tarjeta_eliminacion, fg_color="transparent")
    frame_botones.pack(pady=20)
    
    btn_eliminar = customtkinter.CTkButton(
        master=frame_botones,
        text="Eliminar",
        command=eliminar_producto,
        bg_color="transparent",
        fg_color="#00BFFE",
        font=("Segoe UI", 12, "bold"),
        width=120, 
        height=40,
        cursor="hand2"
    )
    btn_eliminar.pack(side="left", padx=10)
    
    def volver_pantalla_principal():
        """Volver a la pantalla principal"""
        tarjeta_eliminacion.destroy()
        from pantalla_principal_ import principal_keepit
        principal_keepit(ventana, limpiar_pantalla)
    
    btn_volver = customtkinter.CTkButton(
        master=frame_botones,
        text="Volver",
        command=volver_pantalla_principal,
        bg_color="transparent",
        fg_color="#E0E0E0",
        text_color="#00BFFE",
        font=("Segoe UI", 12, "bold"),
        width=120,
        height=40,
        cursor="hand2"
    )
    btn_volver.pack(side="left", padx=10)
