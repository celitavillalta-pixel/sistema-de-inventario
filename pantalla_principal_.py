
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
    text_color= "Black"
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



screen.mainloop()
