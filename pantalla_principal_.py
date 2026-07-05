
import customtkinter as ctk
from pantalla_registro_de_produc import registrar_producto 
 

#tamaños de la pantalla en general. 

screen = ctk.CTk()
screen.title("Sistema de inventario.")
screen.geometry("400x500")
screen.resizable(False, False)

#Labels. 

label_principal = ctk.CTkLabel(
    master = screen, 
    text= "INVENTARIO", 
    font= ("Helvetica", 25, "bold"),
    bg_color= "transparent"
    ) 
label_principal.pack(pady= 40)  

screen.configure(bg_color = "#E0E0E0") 

#busqueda del producto dentro del boton de mostrar inventario (girm)
inventario = []

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

#Botones 

boton_1= ctk.CTkButton(
    master=screen, 
    text = "Ingresar Producto",
    font= ("Times New Roman", 15),
    bg_color= "#00BFFE",
    text_color= "Black",
    width= 250,
    height= 40,
    command = registrar_producto
    )
boton_1.pack(pady=20)

boton_2= ctk.CTkButton(
    master=screen, 
    text = "Mostrar Inventario", 
    font= ("Times New Roman", 15), 
    bg_color= "#00BFFE",
    width= 250,
    height= 40,
    text_color= "Black",
    command = mostrar_inventario
    )
boton_2.pack(pady=20)  

boton_3 = ctk.CTkButton(
    master=screen, 
    text = "Eliminar Productos", 
    font = ("Times New Roman", 15), 
    bg_color = "#00BFFE", 
    text_color = "Black",
    width = 250,
    height = 40
    )
boton_3.pack(pady= 20) 


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
screen.mainloop()
